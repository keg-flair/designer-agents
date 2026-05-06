# Cursor Designer Agents

A small suite of **Cursor-first (Claude-compatible)** skills for Senior Product Designers working on **UX/UI** and **design systems**.

These agents are optimized for **screenshots**, **Figma links/component names**, and **lightweight analytics**, and they output artifacts that are easy to paste into **Figma pages**, **Notion**, or **design-system docs**.

## Repository

- **GitHub**: `https://github.com/keg-flair/cursor-designer-agents`

## What’s in this repo

- **Skills (agents)**: `.cursor/skills/` — Cursor project skills (`.cursor/skills/<skill-name>/SKILL.md`)
- **Rules (always-on guidance)**: `.cursor/rules/` — persistent Cursor rules for consistent outputs
- **Skills (Claude-compatible)**: `skills/` — tool-agnostic skills you can paste into a Claude Project
- **Commands (copy/paste prompts)**: `docs/COMMANDS.md`
- **Templates (fillable outlines)**: `docs/templates/`
- **Golden examples (reference outputs)**: `docs/examples/`
- **Eval harness (stress tests)**: `evals/` + `scripts/agent_eval_harness.py`
- **Docs index**: `docs/README.md`
- **House style**: `docs/HOUSE_STYLE.md`

## Source of truth + divergence policy (important)

- **Canonical definitions live in** `.cursor/skills/` and `.cursor/rules/` (Cursor-optimized + enforced).
- The `skills/` folder contains **Claude-compatible variants** of overlapping skills.
- **Divergence is allowed and expected**:
  - `.cursor/skills/` can be stricter (Cursor rules, tool integrations, more prescriptive formats)
  - `skills/` should stay tool-agnostic and lighter-weight
- For skill changes, follow the maintenance checklist and drift contract in `docs/WRITING_SKILLS.md`.

## Quick start (Cursor, use in any repo)

1. Copy this repo’s `.cursor/` folder into your product/design repo (includes **skills** under `.cursor/skills/` and **rules** under `.cursor/rules/`).
2. Optional: bookmark `docs/COMMANDS.md`, keep `docs/templates/` handy, and skim `docs/examples/` for output shape.
3. In Cursor, ask a task in plain language and attach screenshots/links/metrics as needed.

## Quick start (Claude Projects)

1. Create (or open) a Claude **Project** you use for design work.
2. Copy a skill file from `skills/<skill-name>/SKILL.md` into your Project knowledge (or paste it into chat).
3. Ask for the deliverable in plain language and attach screenshots/links/context as needed.

## Run an eval

Use the zero-dependency eval harness to validate fixtures, generate prompts, and manually score agent outputs.

```bash
python3 scripts/check_repo.py
python3 scripts/agent_eval_harness.py validate
python3 scripts/agent_eval_harness.py list --priority P0
python3 scripts/agent_eval_harness.py start --priority P0 --name p0-smoke
```

The preflight command checks required docs, skill frontmatter, Cursor/Claude mirror coverage, and eval skill references. The run command writes prompts, a manifest, an output folder, and a scorecard under `eval-runs/<run-name>/`. Generated `eval-runs/` artifacts are local-only and ignored by git.

## Docs

- Docs index: `docs/README.md`
- House style: `docs/HOUSE_STYLE.md`
- Usage tips and example workflows: `docs/USAGE.md`
- Command-style prompts: `docs/COMMANDS.md`
- Fillable templates: `docs/templates/`
- Golden examples: `docs/examples/`
- Agent eval harness: `evals/README.md`
- Full skills catalog: `docs/SKILLS.md`
- How to author a new skill: `docs/WRITING_SKILLS.md`


