#!/usr/bin/env python3
"""Package branding-studio as a portable skill ZIP for supported hosts."""

from pathlib import Path
import sys
import zipfile


SKIP_DIRS = {"dist", "__pycache__"}
SKIP_SUFFIXES = {".pyc", ".pyo"}
SKIP_NAMES = {".DS_Store"}


def should_skip(path: Path, root: Path, output: Path) -> bool:
    if path.resolve() == output.resolve():
        return True
    rel = path.relative_to(root)
    if any(part in SKIP_DIRS for part in rel.parts):
        return True
    if path.name in SKIP_NAMES or path.suffix in SKIP_SUFFIXES:
        return True
    return False


def package(output: Path | None = None) -> Path:
    root = Path(__file__).resolve().parents[1]
    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        raise FileNotFoundError(f"missing required skill file: {skill_file}")

    output = (output or (root / "dist" / f"{root.name}.zip")).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            if not path.is_file() or should_skip(path, root, output):
                continue
            archive.write(path, Path(root.name) / path.relative_to(root))

    required = f"{root.name}/SKILL.md"
    with zipfile.ZipFile(output) as archive:
        if required not in archive.namelist():
            raise RuntimeError(f"invalid package: {required} not found")

    return output


def main() -> int:
    output = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else None
    path = package(output)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
