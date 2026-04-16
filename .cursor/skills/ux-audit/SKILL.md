---
name: ux-audit
description: Produces a heuristic UX audit and prioritized fix list from screenshots, flows, or Figma links. Use when the user asks for a UX review, usability issues, friction analysis, or “audit these screens”.
---

# UX Audit

## Inputs to request (only if missing)

- Screenshots (or a link) and what platform (web/iOS/Android)
- Primary user goal for the flow
- Target audience + any constraints (accessibility, localization, auth, payments)
- Success metric (conversion, time-to-complete, error rate, retention)

## Method

1. Identify the flow(s) and the “moment of truth” decision points.
2. Evaluate using heuristics:
   - clarity (labels, hierarchy, comprehension)
   - feedback (system status, loading, errors)
   - control (undo/back, escape hatches)
   - efficiency (defaults, shortcuts, reduction of steps)
   - trust (pricing, permissions, privacy, security cues)
   - consistency (patterns, components, copy)
3. Call out risks by severity + frequency.
4. Propose fixes that are:
   - minimal surface-area first (copy/layout)
   - then interaction changes
   - then structural re-architecture
5. Provide concrete before/after guidance and what to validate.

## Output template

Use this structure.

```markdown
## UX audit summary
- **Flow(s) reviewed**: …
- **Primary user goal**: …
- **Top 3 issues (headline)**:
  1. …
  2. …
  3. …

## Prioritized findings
### P0 (ship blocker)
- **Issue**: …
  - **Where**: screen/state
  - **Why it matters**: user impact + business impact
  - **Evidence**: what in UI suggests this (and any metrics provided)
  - **Fix**: specific change(s) to layout/copy/interaction
  - **Edge cases**: errors, empty states, slow network, auth, etc.
  - **How to validate**: metric + qualitative check

### P1 (high impact)
…

### P2 (polish)
…

## Quick wins (≤ 1 day)
- …

## Open questions to resolve
- …
```

## Quality bar

- Prefer actionable, testable recommendations over general advice.
- When uncertain, present 2–3 options with a default and trade-off.
- Keep recommendations consistent with a design-system mindset (reuse patterns, avoid one-offs).

