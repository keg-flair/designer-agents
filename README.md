# Designer Agents (Cursor Skills)

Reusable Cursor **project skills** for a Senior Product Designer specializing in **UX/UI** and **design systems**.

## What's included

- `.cursor/skills/ux-audit/`: heuristic + UX audit from screenshots/flows
- `.cursor/skills/accessibility-review/`: WCAG-oriented accessibility review
- `.cursor/skills/design-system-governance/`: standards, contribution workflow, release notes
- `.cursor/skills/component-spec-writer/`: Figma-ready component spec + variant matrix
- `.cursor/skills/research-synthesis/`: turn raw notes into insights + themes + opportunities
- `.cursor/skills/analytics-insights/`: translate funnel/event metrics into design hypotheses

## Install (Cursor)

1. Copy the `.cursor/` folder from this repo into your project repo.
2. In Cursor, ask for what you want, e.g.:
   - “Run a UX audit on these screenshots and propose fixes.”
   - “Write a component spec for `Button` with variants and token hooks.”
   - “Synthesize these interviews into themes and opportunities.”

## Working style

These skills are **tool-agnostic** (no assumptions about Figma plugins or a specific token tool). They are optimized for:
- screenshots
- Figma links / component names
- lightweight analytics (funnels, events, conversion)

## Publishing to GitHub

If `git` isn’t available on your Mac yet, install Apple Command Line Tools:

```bash
xcode-select --install
```

Then initialize and push:

```bash
git init
git add .
git commit -m "Add Cursor skills for product design and design systems"
git remote add origin <your-repo-url>
git push -u origin main
```

