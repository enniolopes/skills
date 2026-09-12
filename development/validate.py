#!/usr/bin/env python3
"""Minimal repository validation for installable runtime integrity.

One command locally and in CI:  python development/validate.py

CI proves only mechanical properties: installability, runtime boundaries, syntax and unit
contracts. It does not judge semantic or creative quality.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LICENSE = "CC-BY-NC-4.0"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
SKILL_TOKEN_CAP = 5000
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".yaml", ".yml"}
RUNTIME_FORBIDDEN_NAMES = {"README.md", "tests", "evals", "docs", "dist"}
RUNTIME_FORBIDDEN_REFS = ("development/", "systems/")
SYSTEM_TOP = {".claude-plugin", "README.md", "skills", "agents"}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_json(path: Path, errors: list[str]) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{rel(path)}: invalid JSON ({exc})")
        return None
    if not isinstance(data, dict):
        errors.append(f"{rel(path)}: JSON root must be an object")
        return None
    return data


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    parent: str | None = None
    for line in lines[1:]:
        if line.strip() == "---":
            return out
        key, sep, value = line.partition(":")
        if not sep or not key.strip():
            continue
        if line.startswith((" ", "\t")) and parent:
            out[f"{parent}.{key.strip()}"] = value.strip().strip("'\"")
        else:
            parent = key.strip()
            out[parent] = value.strip().strip("'\"")
    return {}


def estimate_tokens(text: str) -> int:
    wide = sum(1 for c in text if ord(c) > 127)
    return round((len(text) - wide) / 4 + wide)


def check_runtime_tree(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*"):
        if path.name in RUNTIME_FORBIDDEN_NAMES:
            errors.append(f"{rel(path)}: development material inside runtime")
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="replace")
            for ref in RUNTIME_FORBIDDEN_REFS:
                if ref in text:
                    errors.append(f"{rel(path)}: runtime depends on repository path {ref!r}")


def check_skill(path: Path, names: dict[str, str], errors: list[str]) -> None:
    skill = path / "SKILL.md"
    if not skill.is_file():
        errors.append(f"{rel(path)}: missing SKILL.md")
        return
    fm = frontmatter(skill)
    if fm.get("name") != path.name:
        errors.append(f"{rel(skill)}: name must match directory")
    if not fm.get("description"):
        errors.append(f"{rel(skill)}: missing description")
    if fm.get("license") != LICENSE:
        errors.append(f"{rel(skill)}: license must be {LICENSE}")
    if not SEMVER.match(fm.get("metadata.version", "")):
        errors.append(f"{rel(skill)}: metadata.version must be semver")
    if estimate_tokens(skill.read_text(encoding="utf-8")) > SKILL_TOKEN_CAP:
        errors.append(f"{rel(skill)}: exceeds {SKILL_TOKEN_CAP}-token runtime cap")
    previous = names.get(path.name)
    if previous:
        errors.append(f"{rel(path)}: runtime name duplicates {previous}")
    names[path.name] = rel(path)
    check_runtime_tree(path, errors)


def check_agent(path: Path, names: dict[str, str], errors: list[str]) -> None:
    fm = frontmatter(path)
    if fm.get("name") != path.stem or not fm.get("description"):
        errors.append(f"{rel(path)}: agent needs matching name and description")
    previous = names.get(path.stem)
    if previous:
        errors.append(f"{rel(path)}: runtime name duplicates {previous}")
    names[path.stem] = rel(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    for ref in RUNTIME_FORBIDDEN_REFS:
        if ref in text:
            errors.append(f"{rel(path)}: runtime depends on repository path {ref!r}")


def discover_runtime(errors: list[str], plugins: dict[str, dict]) -> tuple[set[str], dict[str, tuple[str, str]]]:
    names: dict[str, str] = {}
    units: set[str] = set()
    expected_plugins: dict[str, tuple[str, str]] = {}

    skills = REPO_ROOT / "skills"
    if not skills.is_dir():
        errors.append("skills/: missing")
    else:
        for path in sorted(p for p in skills.iterdir() if p.is_dir()):
            check_skill(path, names, errors)
            units.add(path.name)
            expected_plugins[path.name] = (f"./skills/{path.name}", "skill")

    agents = REPO_ROOT / "agents"
    if agents.is_dir():
        for path in sorted(agents.glob("*.md")):
            check_agent(path, names, errors)
            units.add(path.stem)

    systems = REPO_ROOT / "systems"
    if systems.is_dir():
        for system in sorted(p for p in systems.iterdir() if p.is_dir()):
            units.add(system.name)
            expected_plugins[system.name] = (f"./systems/{system.name}", "system")
            unexpected = [p.name for p in system.iterdir() if p.name not in SYSTEM_TOP]
            if unexpected:
                errors.append(f"{rel(system)}: unexpected runtime entries: {', '.join(sorted(unexpected))}")
            manifest = system / ".claude-plugin" / "plugin.json"
            data = load_json(manifest, errors) if manifest.is_file() else None
            if data is None:
                if not manifest.is_file():
                    errors.append(f"{rel(system)}: missing plugin.json")
            else:
                if data.get("name") != system.name:
                    errors.append(f"{rel(manifest)}: name must match system directory")
                if not SEMVER.match(str(data.get("version", ""))):
                    errors.append(f"{rel(manifest)}: version must be semver")
                if data.get("license") != LICENSE:
                    errors.append(f"{rel(manifest)}: license must be {LICENSE}")
                for dep in data.get("dependencies", []):
                    dep_name = dep if isinstance(dep, str) else dep.get("name")
                    if dep_name not in plugins:
                        errors.append(f"{rel(manifest)}: unknown plugin dependency {dep_name!r}")
            nested_skills = system / "skills"
            if nested_skills.is_dir():
                for path in sorted(p for p in nested_skills.iterdir() if p.is_dir()):
                    check_skill(path, names, errors)
            nested_agents = system / "agents"
            if nested_agents.is_dir():
                for path in sorted(nested_agents.glob("*.md")):
                    check_agent(path, names, errors)
    return units, expected_plugins


def marketplace(errors: list[str]) -> dict[str, dict]:
    path = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    data = load_json(path, errors) if path.is_file() else None
    if data is None:
        if not path.is_file():
            errors.append(".claude-plugin/marketplace.json: missing")
        return {}
    out: dict[str, dict] = {}
    for item in data.get("plugins", []):
        if not isinstance(item, dict) or not item.get("name"):
            errors.append(f"{rel(path)}: every plugin needs a name")
            continue
        name = item["name"]
        if name in out:
            errors.append(f"{rel(path)}: duplicate plugin {name!r}")
        out[name] = item
    return out


def check_marketplace(plugins: dict[str, dict], expected: dict[str, tuple[str, str]], errors: list[str]) -> None:
    if set(plugins) != set(expected):
        errors.append(".claude-plugin/marketplace.json: entries must match installable units")
        return
    for name, (source, kind) in expected.items():
        item = plugins[name]
        if item.get("source") != source or not item.get("description"):
            errors.append(f"marketplace {name!r}: wrong source or missing description")
        if kind == "skill" and item.get("strict") is not False:
            errors.append(f"marketplace {name!r}: standalone skill needs strict=false")
        if kind == "system" and "strict" in item:
            errors.append(f"marketplace {name!r}: system must not override strict")


def compile_python(errors: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "compileall", "-q", "skills", "systems", "development"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        errors.append("python compile failed: " + (result.stderr or result.stdout).strip())


def run_tests(units: set[str], errors: list[str]) -> int:
    suites = 0
    for name in sorted(units):
        path = REPO_ROOT / "development" / name / "tests"
        if not path.is_dir():
            continue
        suites += 1
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(path)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            errors.append(f"{rel(path)}: tests failed\n{result.stderr.strip()}")
    return suites


def main() -> int:
    errors: list[str] = []
    plugins = marketplace(errors)
    units, expected = discover_runtime(errors, plugins)
    check_marketplace(plugins, expected, errors)
    compile_python(errors)
    suites = run_tests(units, errors)
    if errors:
        print(f"invalid ({len(errors)}):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"valid: {len(units)} installable units; {suites} test suite(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
