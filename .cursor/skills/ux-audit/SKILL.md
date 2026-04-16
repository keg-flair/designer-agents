---
name: ux-audit
description: Produces a heuristic UX audit and prioritized fix list from screenshots, flows, or Figma links. Use when the user asks for a UX review, usability issues, friction analysis, or “audit these screens”.
---

# UX Audit

## Defaults

- **Tool-agnostic**: do not assume specific design tools/plugins.
- **Evidence first**: tie each finding to what is visible in the UI, a provided metric, or a stated constraint.
- **Design-system minded**: prefer reusing patterns/tokens/components over one-off UI.
- **Ship-ready**: recommendations include edge cases and a validation plan.

## Constraints

- **Do not invent inputs** (metrics, user segments, policy rules, platform behaviors). If missing, list assumptions explicitly.
- **Ask at most 3 clarifying questions**, only if they materially change prioritization.
- **Separate fact vs hypothesis**: label uncertainty and propose how to verify.

## Clarifying questions (ask max 3)

Ask only if the answer will change priority/recommendations. Otherwise proceed with assumptions.

1. What’s the **primary user goal** for this flow (the “job to be done”)?
2. What’s the **success metric** (conversion, activation, time-to-complete, error rate) and target direction?
3. Any **hard constraints** (a11y level, localization, auth/payments, regulatory/trust requirements)?

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
- **Assumptions/constraints**: …
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
  - **Evidence**: screenshot cue(s) and/or metric(s) and/or user quote(s)
  - **Confidence**: High | Med | Low (what would raise confidence?)
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
- Every prioritized issue must include **Evidence** + **Confidence**.

