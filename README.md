# Designer Agents (Cursor Skills)

A small suite of **Cursor project skills** for Senior Product Designers working on **UX/UI** and **design systems**.

These agents are optimized for **screenshots**, **Figma links/component names**, and **lightweight analytics**, and they output artifacts that are easy to paste into **Figma pages**, **Notion**, or **design-system docs**.

## Quick start (use in any repo)

1. Copy this repo’s `.cursor/` folder into your product/design repo.
2. In Cursor, ask a task in plain language and attach screenshots/links/metrics as needed.

Example prompts:
- “Audit this onboarding flow for friction. Prioritize P0/P1 issues and propose fixes.”
- “Write a component spec for `Button` with variants, states, token hooks, and QA checklist.”
- “Synthesize these interviews into themes, insights, and opportunities.”
- “Given this funnel drop-off, propose UX hypotheses and what to measure next.”

## Skill catalog

- **UX Audit** (`.cursor/skills/ux-audit/`)
  - Use for: heuristic review, friction analysis, flow critique
  - Output: prioritized findings (P0–P2), quick wins, validation plan
- **Accessibility Review** (`.cursor/skills/accessibility-review/`)
  - Use for: WCAG-informed issues + remediations (contrast, focus, labels, motion)
  - Output: must-fix/should-fix/nice-to-have + verification checklist
- **Design System Governance** (`.cursor/skills/design-system-governance/`)
  - Use for: contribution workflow, decision records, release notes
  - Output: copy/paste governance artifacts (templates)
- **Component Spec Writer** (`.cursor/skills/component-spec-writer/`)
  - Use for: component documentation, variant matrix, states/behaviors, token hooks
  - Output: spec doc with slots, variants, a11y, theming, QA checklist
- **Research Synthesis** (`.cursor/skills/research-synthesis/`)
  - Use for: turning raw notes into themes → insights → opportunities
  - Output: evidence-backed insights + hypotheses + next steps
- **Analytics → UX Insights** (`.cursor/skills/analytics-insights/`)
  - Use for: interpreting funnels/events to propose UX mechanisms + experiments
  - Output: ranked hypotheses, follow-up analyses, instrumentation gaps

## How these work

Each skill is a folder under `.cursor/skills/<skill-name>/` with a `SKILL.md` containing:
- when to use it (discoverability)
- what inputs to request (only if missing)
- a repeatable method/checklist
- a deliverable template

## Docs

- Usage tips and example workflows: `docs/USAGE.md`
- Full skills catalog: `docs/SKILLS.md`
- How to author a new skill: `docs/WRITING_SKILLS.md`

## Publishing / development

If you’re missing `git` on macOS, install Apple Command Line Tools:

```bash
xcode-select --install
```


