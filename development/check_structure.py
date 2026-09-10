#!/usr/bin/env python3
"""Verify the repository topology.

Rules (see README.md, "Topology"):
- skills/<name>/       runtime skill: SKILL.md with frontmatter `name` == <name>;
                       no development, documentation or build files inside.
- agents/<name>.md     runtime agent: frontmatter `name` == <name>.
- systems/<name>/      composition: README.md listing the pieces; no runtime content.
- development/<unit>/  and docs/<unit>/: <unit> must be a skill, agent or system.
- SKILL.md appears only under skills/<name>/SKILL.md.

Exit code 0 when the tree conforms; 1 with one line per violation otherwise.
"""

from __future__ import annotations

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]

RUNTIME_FORBIDDEN = {"README.md", "tests", "evals", "docs", "dist"}
# Local, git-ignored artifacts: never committed, so never a structure violation.
SCAN_EXCLUDE = {".git", ".claude", "dist", "node_modules", "__pycache__", ".DS_Store"}


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if sep and key.strip():
            fields[key.strip()] = value.strip().strip("'\"")
    return {}


def check_skills(errors: list[str]) -> set[str]:
    names: set[str] = set()
    root = REPO_ROOT / "skills"
    if not root.is_dir():
        errors.append("skills/ is missing")
        return names
    for entry in sorted(root.iterdir()):
        rel = entry.relative_to(REPO_ROOT).as_posix()
        if not entry.is_dir():
            errors.append(f"{rel}: only skill directories belong directly under skills/")
            continue
        names.add(entry.name)
        skill_md = entry / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{rel}: missing SKILL.md")
        else:
            name = frontmatter(skill_md).get("name")
            if name != entry.name:
                errors.append(f"{rel}/SKILL.md: frontmatter name {name!r} != directory name {entry.name!r}")
            if not frontmatter(skill_md).get("description"):
                errors.append(f"{rel}/SKILL.md: frontmatter description is missing")
        for path in entry.rglob("*"):
            if any(part in SCAN_EXCLUDE for part in path.relative_to(entry).parts):
                continue
            if path.name in RUNTIME_FORBIDDEN:
                errors.append(
                    f"{path.relative_to(REPO_ROOT).as_posix()}: not runtime; "
                    f"move it to development/{entry.name}/ or docs/{entry.name}/"
                )
    return names


def check_agents(errors: list[str]) -> set[str]:
    names: set[str] = set()
    root = REPO_ROOT / "agents"
    if not root.is_dir():
        return names
    for entry in sorted(root.iterdir()):
        rel = entry.relative_to(REPO_ROOT).as_posix()
        if not (entry.is_file() and entry.suffix == ".md"):
            errors.append(f"{rel}: only <name>.md agent files belong under agents/")
            continue
        names.add(entry.stem)
        name = frontmatter(entry).get("name")
        if name != entry.stem:
            errors.append(f"{rel}: frontmatter name {name!r} != file name {entry.stem!r}")
    return names


def check_systems(errors: list[str]) -> set[str]:
    names: set[str] = set()
    root = REPO_ROOT / "systems"
    if not root.is_dir():
        return names
    for entry in sorted(root.iterdir()):
        rel = entry.relative_to(REPO_ROOT).as_posix()
        if not entry.is_dir():
            errors.append(f"{rel}: only system directories belong directly under systems/")
            continue
        names.add(entry.name)
        if not (entry / "README.md").is_file():
            errors.append(f"{rel}: missing README.md")
        for path in entry.rglob("SKILL.md"):
            errors.append(f"{path.relative_to(REPO_ROOT).as_posix()}: runtime belongs in skills/, not systems/")
    return names


def check_units_dir(errors: list[str], dirname: str, units: set[str]) -> None:
    root = REPO_ROOT / dirname
    if not root.is_dir():
        return
    for entry in sorted(root.iterdir()):
        if entry.is_dir() and entry.name not in units and entry.name not in SCAN_EXCLUDE:
            errors.append(
                f"{entry.relative_to(REPO_ROOT).as_posix()}: {entry.name!r} is not a skill, agent or system"
            )


def check_stray_skill_md(errors: list[str]) -> None:
    for path in REPO_ROOT.rglob("SKILL.md"):
        rel = path.relative_to(REPO_ROOT)
        if rel.parts[0] in SCAN_EXCLUDE:
            continue
        if not (len(rel.parts) == 3 and rel.parts[0] == "skills"):
            errors.append(f"{rel.as_posix()}: SKILL.md is only valid at skills/<name>/SKILL.md")


def main() -> int:
    errors: list[str] = []
    units = check_skills(errors) | check_agents(errors) | check_systems(errors)
    check_units_dir(errors, "development", units)
    check_units_dir(errors, "docs", units)
    check_stray_skill_md(errors)
    if errors:
        print("structure check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"structure ok: {len(units)} units")
    return 0


if __name__ == "__main__":
    sys.exit(main())
