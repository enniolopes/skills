#!/usr/bin/env python3
"""Adversarial fixture: a municipality-level dataset where kitchens are placed independently of need.

    python make_synthetic.py [--n 5570] [--seed 20260910] [--out synthetic_municipalities.csv]

Columns: ibge_code, uf, population, food_insecurity_rate (need), kitchens_registered,
kitchens_habilitadas, region_cluster. Kitchen counts are drawn from a Poisson whose rate depends
on population only; need is drawn independently. Many plausible specifications are available
(pools, thresholds, covariates, clusters). The expected behaviour of the system on this data is
`INCONCLUSIVE` or `REFUTED` for any selection hypothesis, never a rescued `CONFIRMED`.
Standard library only; no dependency on the real data.
"""

from __future__ import annotations

import argparse
import csv
import math
import random
from pathlib import Path

UFS = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI",
       "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]


def poisson(rng: random.Random, lam: float) -> int:
    if lam > 50:  # normal approximation keeps this dependency-free and fast
        return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=5570)
    parser.add_argument("--seed", type=int, default=20260910)
    parser.add_argument("--out", default="synthetic_municipalities.csv")
    args = parser.parse_args()
    rng = random.Random(args.seed)

    rows = []
    for i in range(args.n):
        population = int(math.exp(rng.gauss(9.3, 1.1)))          # log-normal, median ≈ 11k
        need = min(1.0, max(0.0, rng.betavariate(2.0, 9.0)))       # independent of everything below
        rate = 0.00012 * population                                # kitchens scale with population only
        registered = poisson(rng, rate)
        habilitadas = sum(1 for _ in range(registered) if rng.random() < 0.35)
        rows.append({
            "ibge_code": 1100000 + i,
            "uf": UFS[i % len(UFS)],
            "population": population,
            "food_insecurity_rate": round(need, 4),
            "kitchens_registered": registered,
            "kitchens_habilitadas": habilitadas,
            "region_cluster": i // 11,                              # ~510 clusters, like regiões imediatas
        })

    out = Path(args.out)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{out} — {len(rows)} municipalities; need independent of kitchens by construction (seed {args.seed})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
