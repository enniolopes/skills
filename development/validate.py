#!/usr/bin/env python3
"""Validate the repository: topology, unit contracts, catalog projections, links, then unit tests.

One command, locally and in CI:  python development/validate.py

Every rule here is the executable form of a rule in README.md ("Model"). A rule that can
be decided mechanically is decided here; README explains meaning, it is not the control.

Exit code 0 when everything holds; 1 with one line per violation otherwise.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# --- Model -----------------------------------------------------------------------------
# Top level = role. Anything else at the top level is an architecture decision: add it
# here, in the same change, or the check fails.
TOP_LEVEL = {"skills", "agents", "systems", "development", ".claude-plugin", ".github", "README.md", "LICENCE", ".gitignore"}
LICENSE = "CC-BY-NC-4.0"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

# The always-loaded body of a skill. Claude Code's auto-compaction re-attaches only the first
# 5,000 tokens of an invoked skill, silently dropping the tail in exactly the long sessions
# where "always loaded" matters most. The cap is the platform's mechanic, not a preference;
# depth beyond it belongs in references the skill loads on demand.
SKILL_TOKEN_CAP = 5000

# Runtime never carries development material, and never points into the repository.
RUNTIME_FORBIDDEN_NAMES = {"README.md", "tests", "evals", "docs", "dist"}
RUNTIME_FORBIDDEN_REFS = ("development/", "systems/")
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".yaml", ".yml"}

# A system is a Claude Code plugin: manifest, README, and its exclusive pieces.
SYSTEM_TOP = {".claude-plugin", "README.md", "skills", "agents"}

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


def estimate_tokens(text: str) -> int:
    """~4 chars per token for prose; a typographic character (→, ×, ≥) is usually a token by itself."""
    wide = sum(1 for c in text if ord(c) > 127)
    return round((len(text) - wide) / 4 + wide)


def strip_fences(text: str) -> str:
    out, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append(line)
    return "\n".join(out)


def load_json(errors: list[str], path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{rel(path)}: invalid JSON ({exc})")
        return None
    return data if isinstance(data, dict) else None


# --- Runtime contracts -----------------------------------------------------------------
def check_no_repo_refs(errors: list[str], path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    for ref in RUNTIME_FORBIDDEN_REFS:
        if ref in text:
            errors.append(f"{rel(path)}: runtime references {ref!r}; installed alone, it must not depend on the repository")


def check_skill_dir(errors: list[str], entry: Path, owner: str) -> None:
    """One runtime skill directory: SKILL.md contract, size cap, nothing but runtime inside."""
    skill_md = entry / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{rel(entry)}: missing SKILL.md")
        return
    fm = frontmatter(skill_md)
    if fm.get("name") != entry.name:
        errors.append(f"{rel(skill_md)}: frontmatter name {fm.get('name')!r} != directory name {entry.name!r}")
    if not fm.get("description"):
        errors.append(f"{rel(skill_md)}: frontmatter description is missing")
    if fm.get("license") != LICENSE:
        errors.append(f"{rel(skill_md)}: frontmatter license must be {LICENSE} (the artifact installs alone and carries its license)")
    if not SEMVER.match(fm.get("metadata.version", "")):
        errors.append(f"{rel(skill_md)}: frontmatter metadata.version must be semver (units are versioned separately)")
    tokens = estimate_tokens(skill_md.read_text(encoding="utf-8"))
    if tokens > SKILL_TOKEN_CAP:
        errors.append(
            f"{rel(skill_md)}: ~{tokens} tokens, cap {SKILL_TOKEN_CAP} — auto-compaction re-attaches only the "
            f"first {SKILL_TOKEN_CAP} tokens and drops the tail; move depth into a reference file"
        )
    for path in entry.rglob("*"):
        if not visible(path):
            continue
        if path.name in RUNTIME_FORBIDDEN_NAMES:
            errors.append(f"{rel(path)}: not runtime; it belongs in development/{owner}/")
        if path.suffix in TEXT_SUFFIXES:
            check_no_repo_refs(errors, path)


def check_agent_file(errors: list[str], entry: Path) -> None:
    fm = frontmatter(entry)
    if fm.get("name") != entry.stem:
        errors.append(f"{rel(entry)}: frontmatter name {fm.get('name')!r} != file name {entry.stem!r}")
    if not fm.get("description"):
        errors.append(f"{rel(entry)}: frontmatter description is missing")
    check_no_repo_refs(errors, entry)


def check_skills_root(errors: list[str], root: Path, owner: str, names: dict[str, str]) -> None:
    for entry in sorted(root.iterdir()):
        if not visible(entry):
            continue
        if not entry.is_dir():
            errors.append(f"{rel(entry)}: only skill directories belong directly under {rel(root)}/")
            continue
        claim(errors, names, entry.name, "skill", entry)
        check_skill_dir(errors, entry, owner)


def check_agents_root(errors: list[str], root: Path, names: dict[str, str]) -> None:
    for entry in sorted(root.iterdir()):
        if not visible(entry):
            continue
        if not (entry.is_file() and entry.suffix == ".md"):
            errors.append(f"{rel(entry)}: only <name>.md agent files belong under {rel(root)}/")
            continue
        claim(errors, names, entry.stem, "agent", entry)
        check_agent_file(errors, entry)


def claim(errors: list[str], names: dict[str, str], name: str, kind: str, path: Path) -> None:
    """Runtime names are unique across the whole repository: a piece cannot shadow a standalone unit."""
    if name in names:
        errors.append(f"{rel(path)}: name {name!r} already used by {names[name]}")
    names[name] = rel(path)


# --- Structure -------------------------------------------------------------------------
def check_top_level(errors: list[str]) -> None:
    for entry in REPO_ROOT.iterdir():
        if entry.name not in TOP_LEVEL and entry.name not in IGNORED:
            errors.append(f"{entry.name}: not part of the top-level model (README.md, Model); a new role is an architecture decision")


def check_standalone(errors: list[str], names: dict[str, str]) -> dict[str, str]:
    units: dict[str, str] = {}
    skills = REPO_ROOT / "skills"
    if not skills.is_dir():
        errors.append("skills/ is missing")
    else:
        check_skills_root(errors, skills, "<name>", names)
        units.update({e.name: "skill" for e in skills.iterdir() if e.is_dir() and visible(e)})
    agents = REPO_ROOT / "agents"
    if agents.is_dir():
        check_agents_root(errors, agents, names)
        units.update({e.stem: "agent" for e in agents.iterdir() if e.is_file() and e.suffix == ".md" and visible(e)})
    return units


def check_systems(errors: list[str], names: dict[str, str], plugins: set[str]) -> dict[str, str]:
    """A system directory is a plugin: .claude-plugin/plugin.json, README.md, skills/, agents/."""
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
        if not (entry / "README.md").is_file():
            errors.append(f"{rel(entry)}: missing README.md (how to install and use the system)")
        for child in entry.iterdir():
            if visible(child) and child.name not in SYSTEM_TOP:
                errors.append(f"{rel(child)}: a system holds {sorted(SYSTEM_TOP)}; everything else goes to development/{entry.name}/")
        manifest = entry / ".claude-plugin" / "plugin.json"
        if not manifest.is_file():
            errors.append(f"{rel(entry)}: missing .claude-plugin/plugin.json (a system is a plugin)")
        else:
            data = load_json(errors, manifest)
            if data is not None:
                if data.get("name") != entry.name:
                    errors.append(f"{rel(manifest)}: name {data.get('name')!r} != directory name {entry.name!r}")
                if not SEMVER.match(str(data.get("version", ""))):
                    errors.append(f"{rel(manifest)}: version must be semver")
                if data.get("license") != LICENSE:
                    errors.append(f"{rel(manifest)}: license must be {LICENSE}")
                for dep in data.get("dependencies", []):
                    dep_name = dep if isinstance(dep, str) else dep.get("name")
                    if dep_name not in plugins:
                        errors.append(f"{rel(manifest)}: dependency {dep_name!r} is not a plugin in .claude-plugin/marketplace.json")
        if (entry / "skills").is_dir():
            check_skills_root(errors, entry / "skills", entry.name, names)
        if (entry / "agents").is_dir():
            check_agents_root(errors, entry / "agents", names)
    return units


def check_development(errors: list[str], units: dict[str, str]) -> None:
    root = REPO_ROOT / "development"
    for entry in sorted(root.iterdir()):
        if not visible(entry):
            continue
        if entry.is_dir() and entry.name not in units:
            errors.append(f"{rel(entry)}: {entry.name!r} is not a standalone skill, agent or system")
        if entry.is_file() and entry.name != Path(__file__).name:
            errors.append(f"{rel(entry)}: development/ holds one directory per unit plus this validator, nothing else")


def check_stray_runtime(errors: list[str]) -> None:
    for path in REPO_ROOT.rglob("SKILL.md"):
        if not visible(path):
            continue
        p = path.relative_to(REPO_ROOT).parts
        standalone = len(p) == 3 and p[0] == "skills"
        in_system = len(p) == 5 and p[0] == "systems" and p[2] == "skills"
        if not (standalone or in_system):
            errors.append(f"{rel(path)}: SKILL.md is only valid at skills/<name>/SKILL.md or systems/<system>/skills/<name>/SKILL.md")


# --- Projections -----------------------------------------------------------------------
def marketplace_plugins(errors: list[str]) -> dict[str, dict]:
    path = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    if not path.is_file():
        errors.append(".claude-plugin/marketplace.json is missing (the install catalog)")
        return {}
    data = load_json(errors, path)
    if data is None:
        return {}
    plugins = {}
    for plugin in data.get("plugins", []):
        if not isinstance(plugin, dict) or "name" not in plugin:
            errors.append(f"{rel(path)}: every plugin entry needs a name")
            continue
        if plugin["name"] in plugins:
            errors.append(f"{rel(path)}: plugin {plugin['name']!r} listed twice")
        plugins[plugin["name"]] = plugin
    return plugins


def check_marketplace(errors: list[str], plugins: dict[str, dict], standalone: dict[str, str], systems: dict[str, str]) -> None:
    """The marketplace is a projection of the filesystem: one plugin per standalone skill, one per system."""
    path = ".claude-plugin/marketplace.json"
    expected = {n: ("./skills/" + n, "skill") for n, k in standalone.items() if k == "skill"}
    expected.update({n: ("./systems/" + n, "system") for n in systems})
    for name, (source, kind) in expected.items():
        plugin = plugins.get(name)
        if plugin is None:
            errors.append(f"{path}: {kind} {name!r} has no plugin entry")
            continue
        if plugin.get("source") != source:
            errors.append(f"{path}: plugin {name!r} source must be {source!r}")
        if kind == "skill" and plugin.get("strict") is not False:
            errors.append(f"{path}: plugin {name!r} needs \"strict\": false — a standalone skill carries no plugin.json inside its runtime")
        if kind == "system" and "strict" in plugin:
            errors.append(f"{path}: plugin {name!r} must not set strict — its plugin.json is the authority")
        if not plugin.get("description"):
            errors.append(f"{path}: plugin {name!r} has no description")
    for name in plugins:
        if name not in expected:
            errors.append(f"{path}: plugin {name!r} does not correspond to a standalone skill or a system")


def check_catalog(errors: list[str], units: dict[str, str]) -> None:
    """README.md's catalog table lists exactly the units that exist."""
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
    """Every relative markdown link outside runtime resolves. Runtime is checked by its own tests."""
    for path in REPO_ROOT.rglob("*.md"):
        if not visible(path):
            continue
        p = path.relative_to(REPO_ROOT).parts
        if p[0] == "skills" or (p[0] == "systems" and len(p) > 2 and p[2] in {"skills", "agents"}):
            continue
        text = strip_fences(path.read_text(encoding="utf-8"))
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
            target = match.group(1)
            if re.match(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", target, re.I):
                continue
            target = target.split("#")[0]
            if target and not (path.parent / target).exists():
                errors.append(f"{rel(path)}: links to missing {target}")


# --- Execution -------------------------------------------------------------------------
def run_plugin_validate(errors: list[str], systems: dict[str, str]) -> str:
    """The host's own validator, when the CLI is present: the marketplace and every system plugin."""
    claude = shutil.which("claude")
    if not claude:
        return "claude CLI not found, plugin validation skipped"
    targets = [REPO_ROOT] + [REPO_ROOT / "systems" / name for name in sorted(systems)]
    for target in targets:
        result = subprocess.run([claude, "plugin", "validate", str(target)], cwd=REPO_ROOT, capture_output=True, text=True)
        if result.returncode != 0 or "warning" in result.stdout.lower():
            errors.append(f"claude plugin validate {rel(target) or '.'}:\n{(result.stdout + result.stderr).strip()}")
    return f"claude plugin validate passed on {len(targets)} target(s)"


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
        [sys.executable, "-m", "compileall", "-q", "skills", "systems", "development"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        errors.append(f"python does not compile:\n{result.stdout.strip()}\n{result.stderr.strip()}")


def main() -> int:
    errors: list[str] = []
    names: dict[str, str] = {}
    check_top_level(errors)
    plugins = marketplace_plugins(errors)
    standalone = check_standalone(errors, names)
    systems = check_systems(errors, names, set(plugins))
    units = standalone | systems
    check_development(errors, units)
    check_stray_runtime(errors)
    check_marketplace(errors, plugins, standalone, systems)
    check_catalog(errors, units)
    check_links(errors)
    if errors:
        print(f"structure invalid ({len(errors)}):")
        for error in errors:
            print(f"- {error}")
        return 1
    compile_python(errors)
    plugin_note = run_plugin_validate(errors, systems)
    suites = run_unit_tests(errors, units)
    if errors:
        print(f"checks failed ({len(errors)}):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"valid: {len(units)} units ({', '.join(sorted(units))}); {len(names)} runtime pieces; "
          f"{suites} test suite(s) passed; {plugin_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
