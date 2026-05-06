#!/usr/bin/env python3
"""Small eval harness for the designer-agent skill suite.

The harness is intentionally zero-dependency so it works in a docs-only repo:
- list eval cases
- render a single prompt
- start a run folder with prompts, manifest, and scorecard
- run lightweight heuristic checks against an agent output
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "evals" / "cases.json"
DEFAULT_RUBRIC = ROOT / "evals" / "rubric.json"
DEFAULT_RUNS_DIR = ROOT / "eval-runs"


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        raise SystemExit(f"Missing file: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}")


def load_cases(path: Path) -> list[dict[str, Any]]:
    data = load_json(path)
    cases = data.get("cases")
    if not isinstance(cases, list):
        raise SystemExit(f"{path} must contain a top-level 'cases' list")
    return cases


def load_rubric(path: Path) -> dict[str, Any]:
    data = load_json(path)
    categories = data.get("categories")
    if not isinstance(categories, list):
        raise SystemExit(f"{path} must contain a top-level 'categories' list")
    return data


def validate_cases(cases: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    required = {"id", "title", "skill", "priority", "type", "tags", "prompt", "expected", "forbidden"}

    for index, case in enumerate(cases):
        missing = sorted(required.difference(case))
        case_id = case.get("id", f"index-{index}")
        if missing:
            errors.append(f"{case_id}: missing required fields: {', '.join(missing)}")
        if case_id in seen_ids:
            errors.append(f"{case_id}: duplicate id")
        seen_ids.add(case_id)
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(case_id)):
            errors.append(f"{case_id}: id must be lowercase kebab-case")
        if not isinstance(case.get("tags"), list):
            errors.append(f"{case_id}: tags must be a list")
        if not isinstance(case.get("prompt"), str) or not case.get("prompt", "").strip():
            errors.append(f"{case_id}: prompt must be a non-empty string")

    return errors


def filter_cases(cases: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    selected = cases
    if getattr(args, "case_id", None):
        wanted = set(args.case_id)
        selected = [case for case in selected if case["id"] in wanted]
    if getattr(args, "skill", None):
        selected = [case for case in selected if case["skill"] == args.skill]
    if getattr(args, "priority", None):
        selected = [case for case in selected if case["priority"] == args.priority]
    if getattr(args, "case_type", None):
        selected = [case for case in selected if case["type"] == args.case_type]
    if getattr(args, "tag", None):
        selected = [case for case in selected if args.tag in case.get("tags", [])]
    return selected


def find_case(cases: list[dict[str, Any]], case_id: str) -> dict[str, Any]:
    for case in cases:
        if case["id"] == case_id:
            return case
    raise SystemExit(f"Unknown case id: {case_id}")


def render_prompt(case: dict[str, Any]) -> str:
    expected = case["expected"]
    forbidden = case["forbidden"]
    required_sections = expected.get("required_sections", [])
    required_terms = expected.get("required_terms", [])
    forbidden_terms = forbidden.get("terms", [])

    lines = [
        f"# Eval Case: {case['title']}",
        "",
        f"- Case ID: `{case['id']}`",
        f"- Skill: `{case['skill']}`",
        f"- Priority: `{case['priority']}`",
        f"- Type: `{case['type']}`",
        f"- Tags: {', '.join(case.get('tags', []))}",
        "",
        "## Prompt To Run",
        "",
        case["prompt"].strip(),
        "",
        "## Expected Contract",
        "",
    ]

    for behavior in expected.get("behaviors", []):
        lines.append(f"- {behavior}")

    if required_sections:
        lines.extend(["", f"Required sections: {', '.join(required_sections)}"])
    if required_terms:
        lines.extend(["", f"Required terms/signals: {', '.join(required_terms)}"])
    if forbidden.get("behaviors") or forbidden_terms:
        lines.extend(["", "## Forbidden Behavior", ""])
    for behavior in forbidden.get("behaviors", []):
        lines.append(f"- {behavior}")
    if forbidden_terms:
        lines.extend(["", f"Forbidden terms/signals: {', '.join(forbidden_terms)}"])

    return "\n".join(lines).rstrip() + "\n"


def render_scorecard(cases: list[dict[str, Any]], rubric: dict[str, Any]) -> str:
    lines = [
        "# Agent Eval Scorecard",
        "",
        "Score each category from 1-5. Mark blockers before calculating the weighted score.",
        "",
        "## Rubric",
        "",
    ]
    for category in rubric["categories"]:
        lines.append(f"### {category['label']} ({category['weight']}%)")
        for check in category.get("checks", []):
            lines.append(f"- {check}")
        lines.append("")

    lines.extend(["## Case Scores", ""])
    for case in cases:
        lines.extend(
            [
                f"### {case['id']} - {case['title']}",
                "",
                f"- Skill: `{case['skill']}`",
                f"- Priority: `{case['priority']}`",
                f"- Type: `{case['type']}`",
                "- Output file:",
                "- Blockers seen:",
                "- Weighted score:",
                "- Notes:",
                "",
                "| Category | Score 1-5 | Evidence / notes |",
                "| --- | --- | --- |",
            ]
        )
        for category in rubric["categories"]:
            lines.append(f"| {category['label']} |  |  |")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def cmd_list(args: argparse.Namespace) -> int:
    cases = filter_cases(load_cases(args.cases), args)
    if not cases:
        print("No cases matched.")
        return 1
    for case in cases:
        tags = ", ".join(case.get("tags", []))
        print(f"{case['id']}\t{case['priority']}\t{case['skill']}\t{case['type']}\t{tags}")
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    case = find_case(load_cases(args.cases), args.case_id)
    rendered = render_prompt(case)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(rendered, end="")
    return 0


def cmd_start(args: argparse.Namespace) -> int:
    cases = filter_cases(load_cases(args.cases), args)
    rubric = load_rubric(args.rubric)
    if not cases:
        print("No cases matched.")
        return 1

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_name = args.name or f"run-{timestamp}"
    run_dir = args.out_dir / run_name
    prompts_dir = run_dir / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=False)

    manifest = {
        "run_name": run_name,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "case_count": len(cases),
        "cases": [
            {
                "id": case["id"],
                "title": case["title"],
                "skill": case["skill"],
                "priority": case["priority"],
                "type": case["type"],
                "prompt_file": f"prompts/{case['id']}.md"
            }
            for case in cases
        ],
    }

    for case in cases:
        (prompts_dir / f"{case['id']}.md").write_text(render_prompt(case), encoding="utf-8")

    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "scorecard.md").write_text(render_scorecard(cases, rubric), encoding="utf-8")
    (run_dir / "outputs").mkdir()

    print(f"Started eval run: {run_dir}")
    print(f"Cases: {len(cases)}")
    print("Put agent outputs in the outputs/ folder, then run the check command per case.")
    return 0


def contains_term(text: str, term: str) -> bool:
    return term.lower() in text.lower()


def cmd_check(args: argparse.Namespace) -> int:
    case = find_case(load_cases(args.cases), args.case_id)
    output = args.output.read_text(encoding="utf-8")
    expected = case["expected"]
    forbidden = case["forbidden"]

    required_sections = expected.get("required_sections", [])
    required_terms = expected.get("required_terms", [])
    forbidden_terms = forbidden.get("terms", [])

    missing_sections = [term for term in required_sections if not contains_term(output, term)]
    missing_terms = [term for term in required_terms if not contains_term(output, term)]
    present_forbidden_terms = [term for term in forbidden_terms if contains_term(output, term)]

    status = "pass"
    if present_forbidden_terms:
        status = "fail"
    elif missing_sections or missing_terms:
        status = "warn"

    result = {
        "case_id": case["id"],
        "status": status,
        "missing_sections": missing_sections,
        "missing_terms": missing_terms,
        "present_forbidden_terms": present_forbidden_terms,
        "manual_review_required": True,
        "manual_review_focus": {
            "expected_behaviors": expected.get("behaviors", []),
            "forbidden_behaviors": forbidden.get("behaviors", [])
        }
    }

    if args.json:
        print(json_dumps(result))
    else:
        print(f"Case: {case['id']}")
        print(f"Heuristic status: {status}")
        if missing_sections:
            print(f"Missing sections/signals: {', '.join(missing_sections)}")
        if missing_terms:
            print(f"Missing required terms/signals: {', '.join(missing_terms)}")
        if present_forbidden_terms:
            print(f"Forbidden terms/signals present: {', '.join(present_forbidden_terms)}")
        print("Manual review required: yes")
    return 0 if status != "fail" else 2


def json_dumps(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True)


def cmd_validate(args: argparse.Namespace) -> int:
    cases = load_cases(args.cases)
    load_rubric(args.rubric)
    errors = validate_cases(cases)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(cases)} cases and rubric.")
    return 0


def add_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--case-id", action="append", help="Filter to a case id. Can be used more than once.")
    parser.add_argument("--skill", help="Filter by skill name.")
    parser.add_argument("--priority", choices=["P0", "P1", "P2"], help="Filter by priority.")
    parser.add_argument("--case-type", help="Filter by case type.")
    parser.add_argument("--tag", help="Filter by tag.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Designer-agent eval harness")
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES, help="Path to cases JSON.")
    parser.add_argument("--rubric", type=Path, default=DEFAULT_RUBRIC, help="Path to rubric JSON.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List eval cases.")
    add_filters(list_parser)
    list_parser.set_defaults(func=cmd_list)

    render_parser = subparsers.add_parser("render", help="Render one case prompt.")
    render_parser.add_argument("case_id", help="Case id to render.")
    render_parser.add_argument("--out", type=Path, help="Optional output markdown path.")
    render_parser.set_defaults(func=cmd_render)

    start_parser = subparsers.add_parser("start", help="Create a run folder with prompts and scorecard.")
    add_filters(start_parser)
    start_parser.add_argument("--name", help="Run folder name. Defaults to timestamp.")
    start_parser.add_argument("--out-dir", type=Path, default=DEFAULT_RUNS_DIR, help="Directory for eval runs.")
    start_parser.set_defaults(func=cmd_start)

    check_parser = subparsers.add_parser("check", help="Run heuristic checks against one output file.")
    check_parser.add_argument("case_id", help="Case id to check.")
    check_parser.add_argument("--output", type=Path, required=True, help="Path to the agent output markdown/text.")
    check_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    check_parser.set_defaults(func=cmd_check)

    validate_parser = subparsers.add_parser("validate", help="Validate cases and rubric files.")
    validate_parser.set_defaults(func=cmd_validate)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
