# Writing new skills

## Goal

A skill should produce a **repeatable design artifact** (spec, audit, synthesis, governance doc) with minimal back-and-forth.

## Folder structure

Create:

```
.cursor/skills/<skill-name>/SKILL.md
```

If a skill is tool-agnostic and useful outside Cursor, also add a Claude-compatible variant in:

```
skills/<skill-name>/SKILL.md
```

## Source of truth

- **Primary**: `.cursor/skills/` + `.cursor/rules/` (Cursor behavior and enforcement)
- **Variant**: `skills/` (Claude-compatible versions)

## Divergence policy (recommended)

Divergence between `.cursor/skills/` and `skills/` is allowed and expected.

- `.cursor/skills/` can be stricter and Cursor-specific (rules, integrations, “do X in Cursor” instructions).
- `skills/` should remain tool-agnostic and shorter, and should not reference Cursor-only tooling.

When you update a shared skill, update both versions when it improves both. If not, let them diverge intentionally.

## Drift contract (what must stay consistent)

Even when `.cursor/skills/` and `skills/` diverge, keep these consistent for overlapping skills:

- **Skill identity**: `name` and the core “use when” intent should match.
- **Definitions**: severity meanings (P0/P1/P2; must/should/nice) and confidence meanings (high/med/low) should not contradict `docs/HOUSE_STYLE.md`.
- **Output contract**: the top-level artifact type should be the same (audit vs spec vs synthesis), and the output should remain copy/pasteable.
- **Honesty rules**: never guess as fact; label assumptions; include a verification plan when uncertain.

These may intentionally differ:

- **Cursor-only instructions**: tool integrations (Figma/MCP), repo actions, and “do X in Cursor” mechanics
- **Strictness**: Cursor versions can require additional fields/checks (e.g., explicit evidence, confidence, QA gates)
- **Length and formatting**: Claude-compatible versions can be shorter and more generic

## Maintaining existing skills

Use this checklist when changing a skill so canonical behavior, mirrored variants, docs, examples, and evals do not drift accidentally.

1. Update the canonical Cursor skill in `.cursor/skills/<skill-name>/SKILL.md`.
2. Decide whether the Claude-compatible mirror in `skills/<skill-name>/SKILL.md` also needs the same behavior, a lighter tool-agnostic version, or no change.
3. If the output contract changes, update the matching golden example in `docs/examples/` and any relevant template in `docs/templates/`.
4. If the skill’s purpose, inputs, or output changes, update `docs/SKILLS.md`.
5. If the change creates a new expected behavior or guards against a failure mode, add or update a case in `evals/cases.json`.
6. Run the focused verification commands:

```bash
python3 scripts/check_repo.py
python3 scripts/agent_eval_harness.py validate
python3 scripts/agent_eval_harness.py list --skill <skill-name>
python3 scripts/agent_eval_harness.py render <case-id>
```

For shared skills, a change is ready when the Cursor skill, Claude-compatible variant, docs, examples, and eval case either agree or intentionally diverge under the policy above.

## `SKILL.md` checklist

Include:
- YAML frontmatter:
  - `name`: lowercase, numbers, hyphens only
  - `description`: what it does + when to use it (include trigger terms)
- “Inputs to request (only if missing)”
- A short method/checklist
- A copy/paste output template

## Style guidelines (for this repo)

- Default to **tool-agnostic** guidance.
- Keep outputs **Figma-ready**: crisp sections, variant matrices, token naming hooks, QA checklists.
- Prefer a **single recommended approach** with an escape hatch.
- Don’t over-claim: label assumptions and provide a verification plan when evidence is incomplete.

## Example frontmatter

```markdown
---
name: empty-states
description: Produces empty/loading/error state guidelines and copy recommendations. Use when the user asks for empty states, edge cases, or state design.
---
```

