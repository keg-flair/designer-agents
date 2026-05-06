#!/usr/bin/env python3
"""Repository preflight checks for the designer-agent skill suite.

This script is intentionally zero-dependency and complements the eval harness.
It checks the repo structure that tends to drift when skills, docs, and evals
change together.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import agent_eval_harness as eval_harness


ROOT = Path(__file__).resolve().parents[1]
CURSOR_SKILLS_DIR = ROOT / ".cursor" / "skills"
CLAUDE_SKILLS_DIR = ROOT / "skills"
DOCS_DIR = ROOT / "docs"
CASES_PATH = ROOT / "evals" / "cases.json"
RUBRIC_PATH = ROOT / "evals" / "rubric.json"

CURSOR_ONLY_SKILL_PREFIXES = ("figma-",)
SPECIAL_EVAL_SKILLS = {"cross-agent"}
REQUIRED_DOCS = [
    ROOT / "README.md",
    DOCS_DIR / "README.md",
    DOCS_DIR / "HOUSE_STYLE.md",
    DOCS_DIR / "SKILLS.md",
    DOCS_DIR / "WRITING_SKILLS.md",
    ROOT / "evals" / "README.md",
]


def skill_files(base_dir: Path) -> list[Path]:
    return sorted(base_dir.glob("*/SKILL.md"))


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter")

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return fields
        match = re.fullmatch(r"([a-zA-Z0-9_-]+):\s*(.*)", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()

    raise ValueError("unterminated YAML frontmatter")


def check_skill_frontmatter(paths: list[Path], errors: list[str]) -> set[str]:
    names: set[str] = set()
    for path in paths:
        folder_name = path.parent.name
        try:
            fields = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue

        name = fields.get("name", "")
        description = fields.get("description", "")
        if name != folder_name:
            errors.append(f"{path.relative_to(ROOT)}: frontmatter name must be '{folder_name}'")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            errors.append(f"{path.relative_to(ROOT)}: frontmatter name must be lowercase kebab-case")
        if not description:
            errors.append(f"{path.relative_to(ROOT)}: missing description")
        names.add(folder_name)
    return names


def check_mirrors(cursor_names: set[str], claude_names: set[str], errors: list[str]) -> None:
    for name in sorted(claude_names):
        if name not in cursor_names:
            errors.append(f"skills/{name}/SKILL.md has no matching .cursor skill")

    for name in sorted(cursor_names):
        if name.startswith(CURSOR_ONLY_SKILL_PREFIXES):
            continue
        if name not in claude_names:
            errors.append(f".cursor/skills/{name}/SKILL.md is missing a Claude-compatible mirror")


def check_eval_cases(known_skill_names: set[str], errors: list[str]) -> None:
    cases = eval_harness.load_cases(CASES_PATH)
    rubric = eval_harness.load_rubric(RUBRIC_PATH)

    errors.extend(eval_harness.validate_cases(cases))
    if not rubric.get("categories"):
        errors.append("evals/rubric.json must contain at least one category")

    allowed = known_skill_names | SPECIAL_EVAL_SKILLS
    for case in cases:
        skill = str(case.get("skill", ""))
        if skill not in allowed:
            errors.append(f"{case.get('id', '<unknown>')}: unknown eval skill '{skill}'")


def check_required_docs(errors: list[str]) -> None:
    for path in REQUIRED_DOCS:
        if not path.exists():
            errors.append(f"Missing required doc: {path.relative_to(ROOT)}")


def print_summary(label: str, count: int) -> None:
    print(f"OK: {label}: {count}")


def run() -> int:
    errors: list[str] = []

    check_required_docs(errors)

    cursor_paths = skill_files(CURSOR_SKILLS_DIR)
    claude_paths = skill_files(CLAUDE_SKILLS_DIR)
    cursor_names = check_skill_frontmatter(cursor_paths, errors)
    claude_names = check_skill_frontmatter(claude_paths, errors)

    check_mirrors(cursor_names, claude_names, errors)
    check_eval_cases(cursor_names, errors)

    if errors:
        print("Preflight failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print_summary("Cursor skills", len(cursor_names))
    print_summary("Claude-compatible skills", len(claude_names))
    print_summary("Eval cases", len(eval_harness.load_cases(CASES_PATH)))
    print("Preflight passed.")
    return 0


def main(argv: list[str] | None = None) -> int:
    if argv:
        print("Usage: python3 scripts/check_repo.py")
        return 2
    return run()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
