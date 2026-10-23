#!/usr/bin/env python3
"""Summarize human-reviewed paired prompt evaluations; this script does not run a model."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DIMENSIONS = ("mechanism", "math", "decision", "evidence", "efficiency")


class ReviewError(ValueError):
    pass


def compare(data: dict) -> dict:
    reviews = data.get("reviews")
    if not isinstance(reviews, list) or not reviews:
        raise ReviewError("reviews must be a nonempty list")
    seen = set()
    totals = {variant: {k: 0 for k in DIMENSIONS} for variant in ("baseline", "candidate")}
    wins = {"candidate": 0, "baseline": 0, "tie": 0}
    regressions = []
    for item in reviews:
        if not isinstance(item, dict) or not isinstance(item.get("case_id"), str) or not item["case_id"].strip():
            raise ReviewError("each review needs a nonempty case_id")
        case = item["case_id"]
        if case in seen:
            raise ReviewError(f"duplicate case_id: {case}")
        seen.add(case)
        case_sum = {}
        for variant in ("baseline", "candidate"):
            scores = item.get(variant)
            if not isinstance(scores, dict) or set(scores) != set(DIMENSIONS):
                raise ReviewError(f"{case}/{variant} must specify exactly {', '.join(DIMENSIONS)}")
            for key in DIMENSIONS:
                value = scores[key]
                if type(value) not in (int, float) or not (0 <= value <= 5):
                    raise ReviewError(f"{case}/{variant}/{key} must be a number from 0 to 5")
                totals[variant][key] += value
            case_sum[variant] = sum(scores.values())
        if item.get("critical_regression") is True:
            regressions.append(case)
        elif item.get("critical_regression") not in (True, False, None):
            raise ReviewError(f"{case}: critical_regression must be boolean")
        if case_sum["candidate"] > case_sum["baseline"]:
            wins["candidate"] += 1
        elif case_sum["candidate"] < case_sum["baseline"]:
            wins["baseline"] += 1
        else:
            wins["tie"] += 1
    n = len(reviews)
    averages = {
        variant: {key: round(totals[variant][key] / n, 3) for key in DIMENSIONS}
        for variant in totals
    }
    return {"case_count": n, "averages": averages, "case_score_wins": wins,
            "critical_regression_case_ids": regressions,
            "status": "REVIEW_SUMMARY_ONLY_NOT_MODEL_EVIDENCE"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("review_file", type=Path)
    args = parser.parse_args()
    result = compare(json.loads(args.review_file.read_text(encoding="utf-8")))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
