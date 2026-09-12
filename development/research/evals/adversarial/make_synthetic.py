#!/usr/bin/env python3
"""Generate a generic null-relation dataset for adversarial research evaluation.

The target exposure and outcome are independent by construction. Extra covariates and
clusters make specification search tempting; a sound workflow must not manufacture a
confirmatory result from them.
"""

from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20260910)
    parser.add_argument("--out", default="synthetic_null.csv")
    args = parser.parse_args()
    rng = random.Random(args.seed)

    rows = []
    for i in range(args.n):
        rows.append({
            "unit_id": i + 1,
            "cluster_id": i // 10,
            "exposure": rng.randint(0, 1),
            "outcome": round(rng.gauss(0, 1), 6),
            "covariate_a": round(rng.random(), 6),
            "covariate_b": round(rng.gauss(0, 1), 6),
        })

    out = Path(args.out)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{out} — {len(rows)} rows; exposure and outcome independent by construction; seed={args.seed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
