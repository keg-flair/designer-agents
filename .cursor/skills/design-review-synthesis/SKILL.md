---
name: design-review-synthesis
description: Synthesizes competing UX audit, accessibility, analytics, research, and stakeholder inputs into one prioritized design recommendation. Use when multiple agents, reviewers, metrics, or design critiques disagree and the user needs conflicts, trade-offs, rationale, what to measure, and a test plan.
---

# Design Review Synthesis

## Defaults

- **Decision-first**: produce one recommended path, not an averaged compromise.
- **Evidence-weighted**: prioritize direct behavioral evidence over plausible but unverified opinions.
- **Conflict-aware**: name disagreements clearly and turn them into trade-offs or tests.
- **Actionable**: include what changes, why, risks, and how to verify.

## Constraints

- **Do not invent** evidence, metrics, user segments, implementation details, or reviewer intent.
- **Do not flatten conflict** into vague consensus; preserve meaningful disagreement.
- **Ask at most 3 clarifying questions** only if the decision, success metric, or constraints are missing and would change the recommendation.
- **Separate observation vs interpretation** when evidence is partial.

## Clarifying questions (ask max 3)

Ask only if the answer would change the recommendation.

1. What decision must this synthesis support, and by when?
2. Which signal should carry the most weight: user research, analytics, accessibility risk, business goal, or implementation constraint?
3. What is the success metric or guardrail for the recommended change?

## Inputs to request (only if missing)

- Review findings or agent outputs to synthesize
- Known metrics/funnel data and definitions
- Research snippets or usability observations
- Accessibility constraints and must-fix issues
- Product/business constraints, timeline, and owner
- Desired decision or scope boundary

## Synthesis workflow

1. Extract each input into claims, evidence, confidence, and proposed action.
2. Identify conflicts: goals, evidence quality, scope, effort, accessibility, and measurement.
3. Weight signals by confidence and decision relevance.
4. Recommend one path with an escape hatch if constraints differ.
5. Define what to measure and what would change the recommendation.

## Output template

```markdown
## Recommendation
- **Recommended path**: …
- **User goal**: …
- **What changes**: …
- **Why it helps**: …
- **Risk / trade-off**: …
- **Confidence**: High | Medium | Low

## Evidence readout
- **Strongest signal**: …
- **Supporting signals**: …
- **Weak or missing signals**: …

## Conflicts
- **Conflict**: …
  - **Why it matters**: …
  - **Resolution**: …

## Rationale
- …

## What to measure
- **Primary metric**: …
- **Guardrails**: …
- **Qualitative checks**: …

## Test plan / how to verify
- …

## Open questions
- …
```

## Quality bar

- Start with the recommendation unless evidence is too thin; if too thin, state the minimum needed to decide.
- Use priority language (P0/P1/P2 or must/should/nice) when conflicts imply sequencing.
- Include accessibility and measurement guardrails when the recommendation changes a flow or UI.
- Prefer a reversible smallest test when evidence conflicts.
