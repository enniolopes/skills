#!/usr/bin/env python3
"""Build the installable Branding Studio runtime bundle."""

from pathlib import Path
import sys
import zipfile


SKILL_NAME = "branding-studio"

RUNTIME_FILES = (
    "SKILL.md",
    "references/apply.md",
    "references/audit.md",
    "references/brand-book.md",
    "references/create.md",
    "references/creative-direction.md",
    "references/evolve.md",
    "references/identity-craft.md",
    "references/knowledge.md",
    "references/naming.md",
    "references/spec-schema.md",
    "templates/brand-spec.template.json",
    "templates/portfolio.template.json",
    "scripts/asset_checks.py",
    "scripts/color_tools.py",
    "scripts/portfolio_collision.py",
    "scripts/validate_structure.py",
)

IGNORED_DIRS = {"__pycache__", "dist"}
IGNORED_NAMES = {".DS_Store"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}

DEV_ROOT = Path(__file__).resolve().parent
REPO_ROOT = DEV_ROOT.parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / SKILL_NAME
DEFAULT_OUTPUT = REPO_ROOT / "dist" / f"{SKILL_NAME}.zip"


def runtime_file_set() -> set[str]:
    files: set[str] = set()
    for path in SKILL_ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(SKILL_ROOT)
        if any(part in IGNORED_DIRS for part in rel.parts):
            continue
        if path.name in IGNORED_NAMES or path.suffix in IGNORED_SUFFIXES:
            continue
        files.add(rel.as_posix())
    return files


def validate_runtime_boundary() -> None:
    expected = set(RUNTIME_FILES)
    actual = runtime_file_set()
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if not missing and not unexpected:
        return

    details = []
    if missing:
        details.append("missing runtime files: " + ", ".join(missing))
    if unexpected:
        details.append(
            "unexpected files inside skills/branding-studio: "
            + ", ".join(unexpected)
            + ". Move development/docs/build artifacts outside the runtime directory."
        )
    raise RuntimeError("runtime boundary mismatch:\n- " + "\n- ".join(details))


def package(output: Path | None = None) -> Path:
    validate_runtime_boundary()

    output = (output or DEFAULT_OUTPUT).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for rel in RUNTIME_FILES:
            source = SKILL_ROOT / rel
            archive.write(source, Path(SKILL_NAME) / rel)

    expected_archive = {f"{SKILL_NAME}/{rel}" for rel in RUNTIME_FILES}
    with zipfile.ZipFile(output) as archive:
        actual_archive = set(archive.namelist())

    if actual_archive != expected_archive:
        raise RuntimeError("invalid package contents")

    return output


def main() -> int:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    path = package(output)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
