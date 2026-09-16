#!/usr/bin/env python3
"""
book_checks.py — deterministic checks for a served brand-book package.

Decides only the mechanical part of the package shape: the book is self-contained
(no scripts, no external requests), every relative reference resolves inside the
folder, every image carries alt text, no file in the folder is unreachable from the
book, a print stylesheet exists, and no brand contract is served from the folder.
It establishes nothing about what the pages teach or how they look.

Usage:
    python book_checks.py path/to/served-folder

Exit 0 = no blocking package failures.
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

CSS_URL = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)", re.IGNORECASE)
CSS_IMPORT = re.compile(r"@import\s+(?:url\()?\s*['\"]?([^'\")\s;]+)", re.IGNORECASE)
SVG_HREF = re.compile(r"""(?:xlink:)?href\s*=\s*(['"])([^'"]+)\1""", re.IGNORECASE)
PRINT_MEDIA = re.compile(r"@media[^{]*\bprint\b", re.IGNORECASE)
REF_ATTRS = {"src", "href", "data", "poster", "xlink:href"}
HOST_FILES = {"_redirects", "_headers", ".htaccess"}
CONTRACT_KEYS = {"creative_direction", "strategy"}


def _classify(ref: str) -> str:
    """fragment | skip | script | external | absolute | relative"""
    ref = ref.strip()
    if not ref or ref.startswith("#"):
        return "fragment"
    lower = ref.lower()
    if lower.startswith(("data:", "mailto:", "tel:", "blob:")):
        return "skip"
    if lower.startswith("javascript:"):
        return "script"
    if lower.startswith("//") or urlsplit(ref).scheme:
        return "external"
    if ref.startswith("/"):
        return "absolute"
    return "relative"


class _BookParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str, str]] = []  # (attr, value, tag)
        self.css: list[str] = []
        self.scripts = 0
        self.images_missing_alt = 0
        self.images_empty_alt = 0
        self.images = 0
        self._in_style = False

    def _tag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "script":
            self.scripts += 1
        if tag == "img":
            self.images += 1
            if "alt" not in a:
                self.images_missing_alt += 1
            elif not a["alt"].strip():
                self.images_empty_alt += 1
        if "style" in a:
            self.css.append(a["style"])
        for key, value in a.items():
            if key in REF_ATTRS and value:
                self.refs.append((key, value, tag))
            elif key == "srcset" and value:
                for candidate in value.split(","):
                    token = candidate.strip().split()
                    if token:
                        self.refs.append(("srcset", token[0], tag))

    def handle_starttag(self, tag, attrs):
        self._tag(tag.lower(), attrs)
        if tag.lower() == "style":
            self._in_style = True

    def handle_startendtag(self, tag, attrs):
        self._tag(tag.lower(), attrs)

    def handle_endtag(self, tag):
        if tag.lower() == "style":
            self._in_style = False

    def handle_data(self, data):
        if self._in_style:
            self.css.append(data)


def _css_refs(text: str) -> list[str]:
    return [m.group(2) for m in CSS_URL.finditer(text)] + CSS_IMPORT.findall(text)


def inspect_folder(folder: str | Path) -> dict:
    root = Path(folder).resolve()
    failures: list[str] = []
    warnings: list[str] = []
    passed: list[str] = []

    if not root.is_dir():
        return {"verdict": "PACKAGE_INVALID", "failures": [f"not a directory: {root}"],
                "warnings": [], "passed": [], "counts": {}}

    files = sorted(p for p in root.rglob("*") if p.is_file())
    books = sorted(p for p in root.iterdir() if p.is_file() and p.suffix.lower() in {".html", ".htm"})
    if not books:
        failures.append("no HTML book at the folder root")

    reached: set[Path] = set(books)
    external: list[str] = []
    absolute: list[str] = []
    broken: list[str] = []
    print_css = False
    scripts = 0
    images = missing_alt = empty_alt = 0
    queue: list[Path] = list(books)
    seen: set[Path] = set()

    def resolve(ref: str, source: Path, kind: str) -> None:
        nonlocal scripts
        cls = _classify(ref)
        if cls in {"fragment", "skip"}:
            return
        if cls == "script":
            scripts += 1
            return
        if cls == "external":
            if kind != "link":
                external.append(f"{source.relative_to(root)} -> {ref}")
            return
        if cls == "absolute":
            absolute.append(f"{source.relative_to(root)} -> {ref}")
            return
        path_part = unquote(urlsplit(ref).path)
        target = (source.parent / path_part).resolve()
        if root not in target.parents and target != root:
            broken.append(f"{source.relative_to(root)} -> {ref} (outside folder)")
            return
        if not target.is_file():
            broken.append(f"{source.relative_to(root)} -> {ref}")
            return
        reached.add(target)
        if target not in seen and target.suffix.lower() in {".html", ".htm", ".css", ".svg"}:
            queue.append(target)

    while queue:
        source = queue.pop()
        if source in seen:
            continue
        seen.add(source)
        text = source.read_text(encoding="utf-8", errors="replace")
        suffix = source.suffix.lower()
        if suffix in {".html", ".htm"}:
            parser = _BookParser()
            parser.feed(text)
            scripts += parser.scripts
            images += parser.images
            missing_alt += parser.images_missing_alt
            empty_alt += parser.images_empty_alt
            css_text = "\n".join(parser.css)
            print_css = print_css or bool(PRINT_MEDIA.search(css_text))
            for ref in _css_refs(css_text):
                resolve(ref, source, "css")
            for attr, value, tag in parser.refs:
                kind = "link" if tag == "a" and attr == "href" else "asset"
                resolve(value, source, kind)
        elif suffix == ".css":
            print_css = print_css or bool(PRINT_MEDIA.search(text))
            for ref in _css_refs(text):
                resolve(ref, source, "css")
        elif suffix == ".svg":
            for m in SVG_HREF.finditer(text):
                resolve(m.group(2), source, "asset")
            if re.search(r"<script\b", text, re.IGNORECASE):
                scripts += 1

    if scripts:
        failures.append(f"scripts found ({scripts}) — the book must be static")
    else:
        passed.append("no scripts")

    if external:
        failures.append(f"external requests ({len(external)}): {external[:5]}")
    else:
        passed.append("no external requests (hyperlinks excepted)")

    if absolute:
        failures.append(f"absolute paths break relocation ({len(absolute)}): {absolute[:5]}")
    if broken:
        failures.append(f"unresolved references ({len(broken)}): {broken[:5]}")
    if not absolute and not broken:
        passed.append("every reference resolves inside the folder")

    if missing_alt:
        failures.append(f"images without alt attribute: {missing_alt} of {images}")
    else:
        passed.append(f"all {images} images carry alt")
    if empty_alt:
        warnings.append(f"images with empty alt (decorative only): {empty_alt}")

    if books and not print_css:
        failures.append("no print stylesheet (@media print) found")
    elif books:
        passed.append("print stylesheet present")

    contracts = []
    for path in files:
        if path.suffix.lower() != ".json":
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and (
            "schema_version" in (data.get("meta") or {}) or CONTRACT_KEYS & set(data)
        ):
            contracts.append(str(path.relative_to(root)))
    if contracts:
        failures.append(f"brand contract served publicly: {contracts}")
    else:
        passed.append("no contract inside the served folder")

    orphans = sorted(
        str(p.relative_to(root)) for p in files
        if p not in reached and not p.name.startswith(".")
        and not p.name.upper().startswith("README") and p.name not in HOST_FILES
    )
    if orphans:
        failures.append(f"files the book never reaches ({len(orphans)}): {orphans[:10]}")
    else:
        passed.append("every file is reachable from the book")

    counts = {
        "files": len(files),
        "books": len(books),
        "images": images,
        "svg": sum(1 for p in files if p.suffix.lower() == ".svg"),
    }
    return {
        "verdict": "PACKAGE_INVALID" if failures else "PACKAGE_VALID",
        "failures": failures,
        "warnings": warnings,
        "passed": passed,
        "counts": counts,
        "scope_note": "Package-shape checks only; they say nothing about what the book teaches or how it looks.",
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip())
        return 2
    report = inspect_folder(argv[1])
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["verdict"] == "PACKAGE_VALID" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
