#!/usr/bin/env python3
"""Validate AutoResearcher state syntax and selected evidence/status invariants.

Passing does not establish theorem correctness, true code provenance or novelty.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator


class ResearchStateError(ValueError):
    pass


def validate_state(data: dict, schema_path: Path | None = None) -> None:
    root = Path(__file__).resolve().parents[1]
    schema_path = schema_path or root / "schemas" / "research_state.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(Draft202012Validator(schema).iter_errors(data))
    if errors:
        err = sorted(errors, key=lambda e: (list(map(str, e.path)), e.message))[0]
        raise ResearchStateError(f"schema at {list(err.path)}: {err.message}")

    def unique(records: list, label: str) -> set[str]:
        ids = [obj["id"] for obj in records]
        if len(ids) != len(set(ids)):
            raise ResearchStateError(f"duplicate {label} id")
        return set(ids)

    obj = data["research_object"]
    node_ids = unique(obj["nodes"], "flow node")
    derivation_ids = unique(data["derivations"], "derivation")
    hypothesis_ids = unique(data["hypotheses"], "hypothesis")
    experiment_ids = unique(data["experiments"], "experiment")
    unique(data["decisions"], "decision")
    unique(data.get("branches", []), "branch")

    for n in obj["nodes"]:
        if n["verification"] == "SOURCE_VERIFIED" and not n.get("locator"):
            raise ResearchStateError(f"node {n['id']} asserts SOURCE_VERIFIED but has no source locator")
    for edge in obj["edges"]:
        if edge["from"] not in node_ids or edge["to"] not in node_ids:
            raise ResearchStateError(f"flow edge points to a missing node: {edge}")
    if obj.get("closed_for_scoped_question") and any(
        e["decision_relevant"] for e in obj["unknown_edges"]
    ):
        raise ResearchStateError("scoped flow is declared closed while decision-relevant edges remain unknown")

    for h in data["hypotheses"]:
        if set(h.get("derivation_ids", [])) - derivation_ids:
            raise ResearchStateError(f"hypothesis {h['id']} cites missing derivation")

    for e in data["experiments"]:
        if set(e.get("hypothesis_ids", [])) - hypothesis_ids:
            raise ResearchStateError(f"experiment {e['id']} cites missing hypothesis")
        if e["status"] in {"OBSERVED", "INCONCLUSIVE"} and not any(
            a["kind"] == "ARTIFACT" for a in e["artifacts"]
        ):
            raise ResearchStateError(f"experiment {e['id']} claims empirical outcome without an artifact locator")
        if not e["why_not_derivable"].strip():
            raise ResearchStateError(f"experiment {e['id']} has no residual empirical justification")

    for d in data["decisions"]:
        drefs = d.get("derivation_ids", [])
        if set(drefs) - derivation_ids:
            raise ResearchStateError(f"decision {d['id']} cites missing derivation")
        if set(d.get("experiment_ids", [])) - experiment_ids:
            raise ResearchStateError(f"decision {d['id']} cites missing experiment")
        if d["route"] == "ACCEPT_CONDITIONAL":
            by_id = {a["id"]: a for a in data["derivations"]}
            if not drefs or not all(by_id[r]["status"] in {"CHECKED", "CONDITIONAL"} for r in drefs):
                raise ResearchStateError("ACCEPT_CONDITIONAL requires scoped checked or conditional derivation")
        if d["route"] == "EXPERIMENT" and not d.get("experiment_ids"):
            raise ResearchStateError("EXPERIMENT decision must link an experiment")

    novelty = data["novelty"]
    if novelty["status"] in {"AUDITED", "VALIDATED"} and not novelty["nearest_prior_art"]:
        raise ResearchStateError("audited/validated novelty status lacks nearest-prior-art comparison")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="+", type=Path)
    args = p.parse_args()
    for path in args.files:
        validate_state(json.loads(path.read_text(encoding="utf-8")))
        print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
