#!/usr/bin/env python3
"""Validate the repository: topology, unit contracts, catalog, links, then unit tests.

One command, locally and in CI:  python development/validate.py

Every rule here is the executable form of a rule in README.md ("Model"). A rule that can
be decided mechanically is decided here; README explains meaning, it is not the control.

Exit code 0 when everything holds; 1 with one line per violation otherwise.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# --- Model -----------------------------------------------------------------------------
# Top level = role. Anything else at the top level is an architecture decision: add it
# here, in the same change, or the check fails.
TOP_LEVEL = {"skills", "agents", "systems", "development", ".github", "README.md", "LICENCE", ".gitignore"}
KIND_ROOT = {"skill": "skills", "agent": "agents", "system": "systems"}
STATUSES = {"design", "shipped"}
LICENSE = "CC-BY-NC-4.0"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

# Runtime never carries development material, and never points into it.
RUNTIME_FORBIDDEN_NAMES = {"README.md", "tests", "evals", "docs", "dist"}
RUNTIME_FORBIDDEN_REFS = ("development/", "systems/")

# Local, git-ignored artifacts: never committed, so never a violation.
IGNORED = {".git", ".claude", "dist", "node_modules", "__pycache__", ".DS_Store", ".pytest_cache"}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def visible(path: Path) -> bool:
    return not any(part in IGNORED for part in path.relative_to(REPO_ROOT).parts)


def frontmatter(path: Path) -> dict[str, str]:
    """Flat key: value pairs of the YAML frontmatter; one level of nesting is flattened as parent.child."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    parent = None
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if not sep or not key.strip():
            continue
        if line.startswith((" ", "\t")) and parent:
            fields[f"{parent}.{key.strip()}"] = value.strip().strip("'\"")
        else:
            parent = key.strip()
            fields[parent] = value.strip().strip("'\"")
    return {}


def strip_fences(text: str) -> str:
    out, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append(line)
    return "\n".join(out)


# --- Checks ----------------------------------------------------------------------------
def check_top_level(errors: list[str]) -> None:
    for entry in REPO_ROOT.iterdir():
        if entry.name not in TOP_LEVEL and entry.name not in IGNORED:
            errors.append(f"{entry.name}: not part of the top-level model (README.md, Model); a new role is an architecture decision")


def check_skills(errors: list[str]) -> dict[str, str]:
    units: dict[str, str] = {}
    root = REPO_ROOT / "skills"
    if not root.is_dir():
        errors.append("skills/ is missing")
        return units
    for entry in sorted(root.iterdir()):
        if not visible(entry):
            continue
        if not entry.is_dir():
            errors.append(f"{rel(entry)}: only skill directories belong directly under skills/")
            continue
        units[entry.name] = "skill"
        skill_md = entry / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{rel(entry)}: missing SKILL.md")
            continue
        fm = frontmatter(skill_md)
        if fm.get("name") != entry.name:
            errors.append(f"{rel(skill_md)}: frontmatter name {fm.get('name')!r} != directory name {entry.name!r}")
        if not fm.get("description"):
            errors.append(f"{rel(skill_md)}: frontmatter description is missing")
        if fm.get("license") != LICENSE:
            errors.append(f"{rel(skill_md)}: frontmatter license must be {LICENSE} (the artifact installs alone and carries its license)")
        if not SEMVER.match(fm.get("metadata.version", "")):
            errors.append(f"{rel(skill_md)}: frontmatter metadata.version must be semver (units are versioned separately)")
        for path in entry.rglob("*"):
            if not visible(path):
                continue
            if path.name in RUNTIME_FORBIDDEN_NAMES:
                errors.append(f"{rel(path)}: not runtime; it belongs in development/{entry.name}/")
            if path.suffix in {".md", ".json", ".py", ".txt", ".yaml", ".yml"}:
                text = path.read_text(encoding="utf-8", errors="replace")
                for ref in RUNTIME_FORBIDDEN_REFS:
                    if ref in text:
                        errors.append(f"{rel(path)}: runtime references {ref!r}; installed alone, it must not depend on the repository")
    return units


def check_agents(errors: list[str]) -> dict[str, str]:
    units: dict[str, str] = {}
    root = REPO_ROOT / "agents"
    if not root.is_dir():
        return units
    for entry in sorted(root.iterdir()):
        if not visible(entry):
            continue
        if not (entry.is_file() and entry.suffix == ".md"):
            errors.append(f"{rel(entry)}: only <name>.md agent files belong under agents/")
            continue
        units[entry.stem] = "agent"
        fm = frontmatter(entry)
        if fm.get("name") != entry.stem:
            errors.append(f"{rel(entry)}: frontmatter name {fm.get('name')!r} != file name {entry.stem!r}")
        if not fm.get("description"):
            errors.append(f"{rel(entry)}: frontmatter description is missing")
        text = entry.read_text(encoding="utf-8")
        for ref in RUNTIME_FORBIDDEN_REFS:
            if ref in text:
                errors.append(f"{rel(entry)}: runtime references {ref!r}; installed alone, it must not depend on the repository")
    return units


def check_systems(errors: list[str], runtime_units: dict[str, str]) -> dict[str, str]:
    units: dict[str, str] = {}
    root = REPO_ROOT / "systems"
    if not root.is_dir():
        return units
    for entry in sorted(root.iterdir()):
        if not visible(entry):
            continue
        if not entry.is_dir():
            errors.append(f"{rel(entry)}: only system directories belong directly under systems/")
            continue
        units[entry.name] = "system"
        manifest = entry / "system.json"
        if not (entry / "README.md").is_file():
            errors.append(f"{rel(entry)}: missing README.md")
        if not manifest.is_file():
            errors.append(f"{rel(entry)}: missing system.json (the composition)")
            continue
        for path in entry.rglob("*"):
            if visible(path) and path.is_file() and path.name not in {"README.md", "system.json"}:
                errors.append(f"{rel(path)}: a system directory holds only README.md and system.json; runtime goes to skills/ or agents/, the rest to development/{entry.name}/")
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel(manifest)}: invalid JSON ({exc})")
            continue
        if data.get("name") != entry.name:
            errors.append(f"{rel(manifest)}: name {data.get('name')!r} != directory name {entry.name!r}")
        pieces = data.get("pieces")
        if not isinstance(pieces, list) or not pieces:
            errors.append(f"{rel(manifest)}: pieces must be a non-empty list")
            continue
        for piece in pieces:
            name, kind, status = piece.get("name"), piece.get("kind"), piece.get("status")
            label = f"{rel(manifest)} piece {name!r}"
            if kind not in ("skill", "agent"):
                errors.append(f"{label}: kind must be skill or agent (systems do not nest)")
                continue
            if status not in STATUSES:
                errors.append(f"{label}: status must be one of {sorted(STATUSES)}")
                continue
            exists = runtime_units.get(name) == kind
            if status == "shipped" and not exists:
                errors.append(f"{label}: status is shipped but {KIND_ROOT[kind]}/{name} does not exist")
            if status == "design" and exists:
                errors.append(f"{label}: status is design but {KIND_ROOT[kind]}/{name} exists — update the status")
    return units


def check_development(errors: list[str], units: dict[str, str]) -> None:
    root = REPO_ROOT / "development"
    for entry in sorted(root.iterdir()):
        if not visible(entry):
            continue
        if entry.is_dir() and entry.name not in units:
            errors.append(f"{rel(entry)}: {entry.name!r} is not a skill, agent or system")
        if entry.is_file() and entry.name != Path(__file__).name:
            errors.append(f"{rel(entry)}: development/ holds one directory per unit plus this validator, nothing else")


def check_stray_runtime(errors: list[str]) -> None:
    for path in REPO_ROOT.rglob("SKILL.md"):
        if not visible(path):
            continue
        parts = path.relative_to(REPO_ROOT).parts
        if not (len(parts) == 3 and parts[0] == "skills"):
            errors.append(f"{rel(path)}: SKILL.md is only valid at skills/<name>/SKILL.md")


def check_catalog(errors: list[str], units: dict[str, str]) -> None:
    """README.md's catalog table is a projection of the filesystem; it must list exactly the units."""
    readme = REPO_ROOT / "README.md"
    listed: dict[str, str] = {}
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\|\s*\[([a-z0-9-]+)\]\([^)]*\)\s*\|\s*(skill|agent|system)\s*\|", line)
        if match:
            listed[match.group(1)] = match.group(2)
    for name, kind in units.items():
        if name not in listed:
            errors.append(f"README.md: catalog does not list {kind} {name!r}")
        elif listed[name] != kind:
            errors.append(f"README.md: catalog lists {name!r} as {listed[name]}, it is a {kind}")
    for name in listed:
        if name not in units:
            errors.append(f"README.md: catalog lists {name!r}, which does not exist")


def check_links(errors: list[str]) -> None:
    """Every relative markdown link outside skills/ resolves. Runtime is checked by its own tests."""
    for path in REPO_ROOT.rglob("*.md"):
        if not visible(path) or path.relative_to(REPO_ROOT).parts[0] == "skills":
            continue
        text = strip_fences(path.read_text(encoding="utf-8"))
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
            target = match.group(1)
            if re.match(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", target, re.I):
                continue
            target = target.split("#")[0]
            if target and not (path.parent / target).exists():
                errors.append(f"{rel(path)}: links to missing {target}")


def run_unit_tests(errors: list[str], units: dict[str, str]) -> int:
    """Convention over configuration: development/<unit>/tests/ is discovered and run; no per-unit CI."""
    ran = 0
    for name in sorted(units):
        tests = REPO_ROOT / "development" / name / "tests"
        if not tests.is_dir():
            continue
        ran += 1
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(tests)],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if result.returncode != 0:
            errors.append(f"development/{name}/tests: failed\n{result.stderr.strip()}")
    return ran


def compile_python(errors: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "compileall", "-q", "skills", "development"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        errors.append(f"python does not compile:\n{result.stdout.strip()}\n{result.stderr.strip()}")


def main() -> int:
    errors: list[str] = []
    check_top_level(errors)
    runtime = check_skills(errors) | check_agents(errors)
    units = runtime | check_systems(errors, runtime)
    check_development(errors, units)
    check_stray_runtime(errors)
    check_catalog(errors, units)
    check_links(errors)
    if errors:
        print(f"structure invalid ({len(errors)}):")
        for error in errors:
            print(f"- {error}")
        return 1
    compile_python(errors)
    suites = run_unit_tests(errors, units)
    if errors:
        print(f"checks failed ({len(errors)}):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"valid: {len(units)} units ({', '.join(sorted(units))}); {suites} test suite(s) passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
