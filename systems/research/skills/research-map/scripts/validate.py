#!/usr/bin/env python3
"""research-map validate — mechanical checks of a research repository against its RESEARCH.map.

    python validate.py [RESEARCH.map] [--root DIR] [--offline] [--strict] [--min-int 20] [--only map,numbers,...]

Checks (each PASS / FAIL / NOT_VERIFIED, with the offending lines):
  map        sections present and ordered; pointers resolve; gate and hypothesis states valid;
             every fact-once-wrong names a producing notebook; Last session has a date and a Next line
  numbers    every number quoted in the documents exists in a committed aggregate at the quoted precision
  decisions  every D-<n> has a revision condition; ids unique and increasing
  citations  every DOI / URL in the references resolves (NOT_VERIFIED with --offline)
  notebooks  no committed notebook carries outputs or execution counts

Exit 1 on any FAIL; with --strict also on NOT_VERIFIED. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

SECTIONS = [
    "Layout", "Question", "Hypotheses", "Gates", "Facts that were once wrong",
    "Provenance", "Verification", "Open decisions", "Last session",
]
LAYOUT_KEYS = ["protocol", "decisions", "aggregates", "documents", "notebooks", "references"]
GATE_STATES = {"reached", "pending", "blocked"}
HYPOTHESIS_STATES = {"CONFIRMED", "REFUTED", "INCONCLUSIVE", "BLOCKED", "NOT_VERIFIED", "—", "-"}
IGNORE_MARK = "<!-- rm:ignore -->"
DOC_SUFFIXES = {".md", ".qmd", ".rmd", ".tex", ".txt"}
AGGREGATE_SUFFIXES = {".csv", ".tsv", ".json"}

NUMBER = re.compile(r"(?<![\w.,\-])(\d{1,3}(?:[.,]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?)(?![\w])")
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s\"'<>{}]+)")
DECISION_START = re.compile(r"^(?:#{1,6}\s*|[-*]\s*\*\*|\*\*)?D-(\d+)\b", re.M)
REVISION = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Revision condition|Revise when)(?:\*\*)?\s*:", re.I | re.M)


@dataclass
class Result:
    name: str
    status: str = "PASS"
    summary: str = ""
    lines: list[str] = field(default_factory=list)

    def fail(self, line: str) -> None:
        self.status = "FAIL"
        self.lines.append(line)


# --- map ---------------------------------------------------------------------------------
def parse_sections(text: str) -> tuple[dict[str, list[str]], list[str]]:
    sections: dict[str, list[str]] = {}
    order: list[str] = []
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            order.append(current)
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return sections, order


def parse_layout(lines: list[str]) -> dict[str, list[str]]:
    layout: dict[str, list[str]] = {}
    for line in lines:
        match = re.match(r"^\s*[-*]\s*([a-z]+)\s*:\s*(.+)$", line)
        if match:
            layout[match.group(1)] = [p.strip().strip("`") for p in match.group(2).split(",") if p.strip()]
    return layout


def table_rows(lines: list[str]) -> list[list[str]]:
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:] if rows else []  # drop header


def pointers_in(lines: list[str]) -> list[str]:
    found = []
    for line in lines:
        for token in re.findall(r"`([^`\n]+)`", line):
            if " " in token or not ("/" in token or "." in token):
                continue
            found.append(token)
    return found


def check_map(text: str, root: Path) -> tuple[Result, dict[str, list[str]]]:
    result = Result("map")
    sections, order = parse_sections(text)
    present = [s for s in order if s in SECTIONS]
    for name in SECTIONS:
        if name not in sections:
            result.fail(f"missing section '## {name}'")
    if present != [s for s in SECTIONS if s in sections]:
        result.fail("sections out of order; required order: " + " → ".join(SECTIONS))

    layout = parse_layout(sections.get("Layout", []))
    for key in LAYOUT_KEYS:
        if key not in layout:
            result.fail(f"Layout: missing key '{key}'")
        else:
            for path in layout[key]:
                if not (root / path).exists():
                    result.fail(f"Layout: {key} → {path} does not exist")

    pointer_count = 0
    for name, lines in sections.items():
        if name in {"Layout", "Verification"}:
            continue
        for pointer in pointers_in(lines):
            pointer_count += 1
            target = pointer.split("#")[0]
            if target and not (root / target).exists():
                result.fail(f"{name}: pointer `{pointer}` does not resolve")

    for row in table_rows(sections.get("Gates", [])):
        if len(row) < 2:
            continue
        state = row[1].lower()
        if state not in GATE_STATES:
            result.fail(f"Gates: '{row[0]}' has state '{row[1]}' (valid: {sorted(GATE_STATES)})")
        elif state == "blocked" and (len(row) < 3 or not row[2]):
            result.fail(f"Gates: '{row[0]}' is blocked but names nobody in 'Blocked by'")

    for row in table_rows(sections.get("Hypotheses", [])):
        if len(row) >= 4 and row[3] not in HYPOTHESIS_STATES:
            result.fail(f"Hypotheses: '{row[0]}' has state '{row[3]}' (valid: {sorted(HYPOTHESIS_STATES - {'-'})})")

    for row in table_rows(sections.get("Facts that were once wrong", [])):
        if len(row) < 3 or not pointers_in([row[2]]):
            result.fail(f"Facts that were once wrong: '{row[0] if row else '?'}' has no producing notebook pointer")

    last = sections.get("Last session", [])
    if not any(re.match(r"^\s*[-*]\s*\d{4}-\d{2}-\d{2}", l) for l in last):
        result.fail("Last session: no dated line (`- YYYY-MM-DD: ...`)")
    if not any(re.search(r"\bNext:", l) for l in last):
        result.fail("Last session: no `Next:` line")

    result.summary = f"{len(present)}/{len(SECTIONS)} sections, {pointer_count} pointers"
    return result, layout


# --- numbers -----------------------------------------------------------------------------
def interpretations(token: str) -> list[tuple[float, int]]:
    """All (value, decimals) readings of a token: 5,913 · 5.913 · 1,234.56 · 1.234,56 · 0,61 · 0.61.

    `5.913` is thousands in pt-BR and three decimals in English; both readings are returned and a
    match on either counts. A leading zero (`0.125`, `0,613`) is never thousands.
    """
    grouped = re.fullmatch(r"(\d{1,3})((?:[.,]\d{3})+)", token)
    if grouped:
        readings = []
        if not token.startswith("0"):
            readings.append((float(re.sub(r"[.,]", "", token)), 0))
        if grouped.group(2).count(".") + grouped.group(2).count(",") == 1:
            readings.append((float(token.replace(",", ".")), 3))
        return readings
    match = re.fullmatch(r"(\d{1,3}(?:[.,]\d{3})+)([.,])(\d+)", token)
    if match:
        integer = re.sub(r"[.,]", "", match.group(1))
        return [(float(f"{integer}.{match.group(3)}"), len(match.group(3)))]
    match = re.fullmatch(r"(\d+)[.,](\d+)", token)
    if match:
        return [(float(f"{match.group(1)}.{match.group(2)}"), len(match.group(2)))]
    return [(float(token), 0)]


def iter_files(root: Path, paths: list[str], suffixes: set[str]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        path = root / p
        if path.is_file() and path.suffix.lower() in suffixes:
            files.append(path)
        elif path.is_dir():
            files.extend(f for f in sorted(path.rglob("*")) if f.is_file() and f.suffix.lower() in suffixes)
    return files


def aggregate_values(files: list[Path]) -> list[float]:
    values: list[float] = []

    def walk(obj) -> None:
        if isinstance(obj, bool):
            return
        if isinstance(obj, (int, float)):
            values.append(float(obj))
        elif isinstance(obj, str):
            for token in NUMBER.findall(obj):
                values.extend(v for v, _ in interpretations(token))
        elif isinstance(obj, dict):
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)

    for file in files:
        text = file.read_text(encoding="utf-8", errors="replace")
        if file.suffix.lower() == ".json":
            try:
                walk(json.loads(text))
                continue
            except json.JSONDecodeError:
                pass
        # Delimited text: one cell at a time, so a value after a comma is still a value.
        for line in text.splitlines():
            for cell in re.split(r"[,;\t|]", line):
                cell = cell.strip().strip('"\'')
                if re.fullmatch(r"-?\d[\d.,]*", cell):
                    values.extend(v for v, _ in interpretations(cell.lstrip("-")))
    return values


class Matcher:
    def __init__(self, values: list[float]):
        self.values = values
        self.cache: dict[int, set[float]] = {}

    def rounded(self, decimals: int) -> set[float]:
        if decimals not in self.cache:
            self.cache[decimals] = {round(v, decimals) for v in self.values}
        return self.cache[decimals]

    def has(self, value: float, decimals: int) -> bool:
        return round(value, decimals) in self.rounded(decimals)


def check_numbers(root: Path, layout: dict[str, list[str]], min_int: int) -> Result:
    result = Result("numbers")
    documents = iter_files(root, layout.get("documents", []), DOC_SUFFIXES)
    aggregates = iter_files(root, layout.get("aggregates", []), AGGREGATE_SUFFIXES)
    matcher = Matcher(aggregate_values(aggregates))
    checked = 0
    for doc in documents:
        fenced = False
        for lineno, line in enumerate(doc.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if line.lstrip().startswith("```"):
                fenced = not fenced
                continue
            low = line.lower()
            if fenced or IGNORE_MARK in line or line.lstrip().startswith("#") or "doi" in low or "http" in low:
                continue
            for match in NUMBER.finditer(line):
                token = match.group(1)
                readings = interpretations(token)
                if all(d == 0 and (v < min_int or (len(token) == 4 and 1900 <= v <= 2100)) for v, d in readings):
                    continue
                tail = line[match.end():match.end() + 5]
                if re.match(r"\s?%\s?(CI|IC)\b", tail):  # a confidence level, not a result
                    continue
                checked += 1
                percent = line[match.end():match.end() + 1] == "%"
                if any(matcher.has(v, d) or (percent and matcher.has(v / 100, d + 2)) for v, d in readings):
                    continue
                result.fail(f"{doc.relative_to(root)}:{lineno}  {token}")
    result.summary = f"{checked} numbers in {len(documents)} document(s) against {len(aggregates)} aggregate file(s)"
    return result


# --- decisions ---------------------------------------------------------------------------
def check_decisions(root: Path, layout: dict[str, list[str]]) -> Result:
    result = Result("decisions")
    files = [root / p for p in layout.get("decisions", []) if (root / p).is_file()]
    total = 0
    for file in files:
        text = file.read_text(encoding="utf-8", errors="replace")
        starts = list(DECISION_START.finditer(text))
        previous = 0
        seen: set[int] = set()
        for i, start in enumerate(starts):
            total += 1
            number = int(start.group(1))
            end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
            block = text[start.start():end]
            label = f"{file.relative_to(root)}: D-{number}"
            if number in seen:
                result.fail(f"{label} appears twice")
            if number < previous:
                result.fail(f"{label} is out of order (after D-{previous}); the log is append-only")
            seen.add(number)
            previous = max(previous, number)
            if not REVISION.search(block):
                result.fail(f"{label} has no `Revision condition:`")
    result.summary = f"{total} decision(s) in {len(files)} file(s)"
    return result


# --- citations ---------------------------------------------------------------------------
def resolves(url: str, timeout: float = 10.0) -> str:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "research-map-validate"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return "ok" if response.status < 400 else f"http {response.status}"
    except urllib.error.HTTPError as exc:
        return "ok" if exc.code < 400 else f"http {exc.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return f"unreachable ({exc.reason if hasattr(exc, 'reason') else exc})"


def check_citations(root: Path, layout: dict[str, list[str]], offline: bool) -> Result:
    result = Result("citations")
    files = [root / p for p in layout.get("references", []) if (root / p).is_file()]
    targets: list[tuple[str, str]] = []
    for file in files:
        text = file.read_text(encoding="utf-8", errors="replace")
        rel = str(file.relative_to(root))
        if file.suffix.lower() == ".bib":
            entries = re.split(r"(?m)^@", text)[1:]
            for entry in entries:
                key = re.match(r"\w+\{([^,\s]+)", entry)
                name = key.group(1) if key else "?"
                doi = re.search(r"doi\s*=\s*[{\"]\s*(?:https?://doi\.org/)?([^}\"\s]+)", entry, re.I)
                url = re.search(r"url\s*=\s*[{\"]\s*([^}\"\s]+)", entry, re.I)
                if doi:
                    targets.append((f"{rel}:{name}", "https://doi.org/" + doi.group(1)))
                elif url:
                    targets.append((f"{rel}:{name}", url.group(1)))
                else:
                    result.fail(f"{rel}: entry {name} has neither doi nor url")
        else:
            for doi in DOI.findall(text):
                targets.append((rel, "https://doi.org/" + doi.rstrip(".,;)")))
    if offline:
        if result.status == "PASS":
            result.status = "NOT_VERIFIED"
        result.summary = f"{len(targets)} target(s) not checked (--offline)"
        return result
    unreachable = 0
    for label, url in targets:
        status = resolves(url)
        if status.startswith("unreachable"):
            unreachable += 1
            result.lines.append(f"{label}  {url}  {status}")
        elif status != "ok":
            result.fail(f"{label}  {url}  {status}")
    if unreachable and result.status == "PASS":
        result.status = "NOT_VERIFIED"
    result.summary = f"{len(targets)} target(s), {unreachable} unreachable"
    return result


# --- notebooks ---------------------------------------------------------------------------
def check_notebooks(root: Path, layout: dict[str, list[str]]) -> Result:
    result = Result("notebooks")
    files = iter_files(root, layout.get("notebooks", []), {".ipynb"})
    for file in files:
        try:
            notebook = json.loads(file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            result.fail(f"{file.relative_to(root)}: invalid JSON ({exc})")
            continue
        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            if cell.get("outputs") or cell.get("execution_count") is not None:
                result.fail(f"{file.relative_to(root)}: cell {index} has outputs or an execution count; clear before committing")
    result.summary = f"{len(files)} notebook(s)"
    return result


# --- run ---------------------------------------------------------------------------------
def run(map_path: Path, root: Path, offline: bool, min_int: int, only: set[str] | None) -> list[Result]:
    text = map_path.read_text(encoding="utf-8")
    map_result, layout = check_map(text, root)
    results = [map_result]
    checks = {
        "numbers": lambda: check_numbers(root, layout, min_int),
        "decisions": lambda: check_decisions(root, layout),
        "citations": lambda: check_citations(root, layout, offline),
        "notebooks": lambda: check_notebooks(root, layout),
    }
    for name, check in checks.items():
        if only is None or name in only:
            results.append(check())
    if only is not None and "map" not in only:
        results = results[1:]
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a research repository against its RESEARCH.map.")
    parser.add_argument("map", nargs="?", default="RESEARCH.map")
    parser.add_argument("--root", help="repository root (default: the map's directory)")
    parser.add_argument("--offline", action="store_true", help="do not resolve citations; report NOT_VERIFIED")
    parser.add_argument("--strict", action="store_true", help="exit 1 on NOT_VERIFIED too")
    parser.add_argument("--min-int", type=int, default=20, help="integers below this are not checked (default 20)")
    parser.add_argument("--only", help="comma-separated subset: map,numbers,decisions,citations,notebooks")
    args = parser.parse_args(argv)

    map_path = Path(args.map).resolve()
    if not map_path.is_file():
        print(f"research-map validate: {map_path} not found")
        return 1
    root = Path(args.root).resolve() if args.root else map_path.parent
    only = set(args.only.split(",")) if args.only else None
    results = run(map_path, root, args.offline, args.min_int, only)

    print(f"research-map validate — {root}")
    for r in results:
        print(f"{r.name:<11}{r.status:<14}{r.summary}")
        for line in r.lines:
            print(f"  {line}")
    failed = any(r.status == "FAIL" for r in results)
    unverified = any(r.status == "NOT_VERIFIED" for r in results)
    verdict = "FAIL" if failed else ("NOT_VERIFIED" if unverified else "PASS")
    print(f"RESULT {verdict}")
    return 1 if failed or (args.strict and unverified) else 0


if __name__ == "__main__":
    sys.exit(main())
