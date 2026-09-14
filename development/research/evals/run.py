#!/usr/bin/env python3
"""Run blinded control/treatment behavioral evals for the research plugin.

Dry by default. Pass --execute to invoke Claude Code and incur model usage.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import fixtures

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SCENARIOS = HERE / "scenarios.json"
JUDGE_PROMPT = HERE / "judge" / "research-eval-judge.md"
PLUGIN = REPO / "systems" / "research"
EXPLORER = REPO / "skills" / "explorer"
VALIDATOR = PLUGIN / "skills" / "research-map" / "scripts" / "validate_all.py"


def command(*args: str, cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(list(args), cwd=cwd, capture_output=True, text=True, timeout=timeout)


def repo_sha() -> str:
    result = command("git", "rev-parse", "HEAD", cwd=REPO)
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def load_scenarios() -> dict[str, dict]:
    data = json.loads(SCENARIOS.read_text(encoding="utf-8"))
    return {item["id"]: item for item in data["scenarios"]}


def safe_snapshot(root: Path, initial: str) -> str:
    committed = command("git", "diff", f"{initial}..HEAD", "--", ".", cwd=root).stdout
    working = command("git", "diff", "--", ".", cwd=root).stdout
    status = command("git", "status", "--short", cwd=root).stdout
    return "# committed diff\n" + committed + "\n# working diff\n" + working + "\n# status\n" + status


def runner_cmd(prompt: str, condition: str, model: str, max_turns: int) -> list[str]:
    cmd = [
        "claude",
        "-p",
        prompt,
        "--model",
        model,
        "--output-format",
        "stream-json",
        "--verbose",
        "--max-turns",
        str(max_turns),
        "--permission-mode",
        "auto",
        "--no-session-persistence",
    ]
    if condition == "treatment":
        cmd.extend(["--plugin-dir", str(PLUGIN), "--plugin-dir", str(EXPLORER)])
    return cmd


def validate_fixture(root: Path) -> str:
    result = command(
        sys.executable,
        str(VALIDATOR),
        str(root / "RESEARCH.map"),
        "--root",
        str(root),
        "--offline",
        cwd=root,
    )
    return result.stdout + ("\nSTDERR\n" + result.stderr if result.stderr else "")


def judge_run(scenario: dict, transcript: str, diff: str, validator: str, model: str, timeout: int) -> str:
    prompt = f"""Judge this completed research eval run. You are blinded to condition.

SCENARIO STATE
{scenario['state']}

EXPECTED BEHAVIOR
{scenario['expect']}

RUNNER TRANSCRIPT
{transcript}

REPOSITORY DIFF/STATUS
{diff}

VALIDATOR OUTPUT
{validator}
"""
    with tempfile.TemporaryDirectory(prefix="research-judge-") as tmp:
        result = command(
            "claude",
            "-p",
            prompt,
            "--model",
            model,
            "--output-format",
            "text",
            "--append-system-prompt-file",
            str(JUDGE_PROMPT),
            "--max-turns",
            "4",
            "--permission-mode",
            "dontAsk",
            "--no-session-persistence",
            cwd=Path(tmp),
            timeout=timeout,
        )
    return result.stdout + ("\nSTDERR\n" + result.stderr if result.stderr else "")


def one_run(
    scenario: dict,
    condition: str,
    repetition: int,
    model: str,
    judge_model: str,
    max_turns: int,
    timeout: int,
    out_root: Path,
    execute: bool,
    judge: bool,
) -> Path:
    with tempfile.TemporaryDirectory(prefix=f"research-eval-{scenario['id']}-") as tmp:
        root = Path(tmp)
        user_prompt = fixtures.build(scenario["id"], root)
        initial = command("git", "rev-parse", "HEAD", cwd=root).stdout.strip()
        full_prompt = (
            "Work directly in the current research repository and complete the user's request. "
            "Inspect files and execute available checks/code when needed; do not merely describe what you could do.\n\n"
            + user_prompt
        )
        cmd = runner_cmd(full_prompt, condition, model, max_turns)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        run_id = f"{stamp}-r{repetition}"
        destination = out_root / scenario["id"] / condition / run_id
        destination.mkdir(parents=True, exist_ok=True)
        metadata = {
            "scenario": scenario["id"],
            "class": scenario.get("class"),
            "condition": condition,
            "repetition": repetition,
            "model": model,
            "repo_sha": repo_sha(),
            "initial_fixture_commit": initial,
            "command": cmd,
            "prompt": full_prompt,
        }
        (destination / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

        if not execute:
            (destination / "DRY_RUN.txt").write_text("Command not executed. Pass --execute.\n", encoding="utf-8")
            return destination

        env = os.environ.copy()
        env["CLAUDE_CODE_SKIP_PROMPT_HISTORY"] = "1"
        try:
            proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=timeout, env=env)
            transcript = proc.stdout
            stderr = proc.stderr
            exit_code = proc.returncode
        except subprocess.TimeoutExpired as exc:
            transcript = exc.stdout or ""
            stderr = (exc.stderr or "") + f"\nTIMEOUT after {timeout}s\n"
            exit_code = 124
        (destination / "transcript.jsonl").write_text(transcript, encoding="utf-8")
        (destination / "stderr.txt").write_text(stderr, encoding="utf-8")
        (destination / "exit_code.txt").write_text(str(exit_code) + "\n", encoding="utf-8")
        diff = safe_snapshot(root, initial)
        validator = validate_fixture(root)
        (destination / "diff.patch").write_text(diff, encoding="utf-8")
        (destination / "validator.txt").write_text(validator, encoding="utf-8")

        if judge:
            judgment = judge_run(scenario, transcript, diff, validator, judge_model, timeout)
            (destination / "judgment.txt").write_text(judgment, encoding="utf-8")
        return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run research behavioral evals (dry by default).")
    parser.add_argument("--scenario", action="append", help="scenario id; repeatable; default all")
    parser.add_argument("--condition", choices=["control", "treatment", "both"], default="both")
    parser.add_argument("--repetitions", type=int, default=3)
    parser.add_argument("--model", default="opus")
    parser.add_argument("--judge-model", default="opus")
    parser.add_argument("--max-turns", type=int, default=20)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--out", type=Path, default=HERE / "runs" / repo_sha())
    parser.add_argument("--execute", action="store_true", help="actually invoke Claude Code; otherwise only build fixtures/commands")
    parser.add_argument("--judge", action="store_true", help="invoke a blinded judge after each executed run")
    args = parser.parse_args(argv)

    scenarios = load_scenarios()
    selected = args.scenario or list(scenarios)
    unknown = [item for item in selected if item not in scenarios]
    if unknown:
        parser.error("unknown scenario(s): " + ", ".join(unknown))
    if args.repetitions < 1:
        parser.error("--repetitions must be >= 1")
    conditions = ["control", "treatment"] if args.condition == "both" else [args.condition]

    outputs: list[Path] = []
    for scenario_id in selected:
        for condition in conditions:
            for repetition in range(1, args.repetitions + 1):
                path = one_run(
                    scenarios[scenario_id],
                    condition,
                    repetition,
                    args.model,
                    args.judge_model,
                    args.max_turns,
                    args.timeout,
                    args.out,
                    args.execute,
                    args.judge,
                )
                outputs.append(path)
                print(path)
    print(f"{len(outputs)} run directory/directories created" + (" and executed" if args.execute else " (dry run)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
