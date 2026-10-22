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

    # Exploration sketches are deliberately independent of registered criteria:
    # creativity needs a cheap record before hypotheses become tested actions.
    # Their schema intentionally has no OBSERVED status or test-evidence gate.
    unique(data.get("exploration_seeds", []), "exploration seed")

    # Optional v2.1-compatible GAPI/MEAR extension. It is not a model-performance
    # oracle; it checks references and prevents simple evidence/status promotion.
    contract = data.get("goal_contract")
    moves = data.get("research_moves", [])
    if moves and contract is None:
        raise ResearchStateError("research_moves require a goal_contract")
    if contract is not None:
        criterion_ids = unique(contract["terminal_criteria"], "terminal criterion")
        proxy_ids = unique(contract["proxy_metrics"], "proxy metric")
    else:
        criterion_ids = set()
        proxy_ids = set()
    move_ids = unique(moves, "research move")
    branch_ids = {item["id"] for item in data.get("branches", [])}
    for move in moves:
        mid = move["id"]
        if set(move["goal_criterion_ids"]) - criterion_ids:
            raise ResearchStateError(f"research move {mid} cites unknown terminal criteria")
        if move["trigger"] == "NEGATIVE_RESULT":
            if not move.get("prior_branch_id") or not move.get("rejected_scope"):
                raise ResearchStateError(f"negative-result move {mid} must bind prior branch and rejection scope")
        if move.get("prior_branch_id") and move["prior_branch_id"] not in branch_ids:
            raise ResearchStateError(f"research move {mid} cites unknown rejected branch")
        if move["trigger"] == "PROXY_IMPROVEMENT" and not move.get("proxy_metric_id"):
            raise ResearchStateError(f"proxy-improvement move {mid} requires a proxy metric")
        if move.get("proxy_metric_id") and move["proxy_metric_id"] not in proxy_ids:
            raise ResearchStateError(f"research move {mid} cites unknown proxy metric")
        comparisons = move["competing_mechanisms"]
        if len({x["id"] for x in comparisons}) != len(comparisons):
            raise ResearchStateError(f"research move {mid} repeats a mechanism id")
        if len({x["prediction"].strip().casefold() for x in comparisons}) != len(comparisons):
            raise ResearchStateError(f"research move {mid} has indistinguishable predictions")
        if move["status"] == "OBSERVED" and not any(
            e["kind"] in {"ARTIFACT", "TRACE"} for e in move["evidence"]
        ):
            raise ResearchStateError(f"research move {mid} claims observation without trace/artifact")

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
