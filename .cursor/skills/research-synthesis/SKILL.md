---
name: research-synthesis
description: Synthesizes UX research notes into themes, insights, opportunities, and follow-up questions. Use when the user provides interview notes, survey results, usability findings, or asks for research synthesis.
---

# Research Synthesis

## Defaults

- **Evidence-backed**: keep a clear chain from notes → themes → insights → opportunities.
- **Tool-agnostic**: do not assume a particular research repository tool.
- **Decision-friendly**: produce hypotheses and success signals, not just themes.

## Constraints

- **Do not invent** participant quotes, counts, or segments—use only what is provided.
- **Ask at most 3 clarifying questions** if study goal/context is missing and would change synthesis.
- **Separate observation vs interpretation**: label insights as “so-what” and tie to evidence.

## Clarifying questions (ask max 3)

Ask only if missing context would change clustering or “so what”.

1. What’s the **study goal / decision it should inform**?
2. Who were the **participants / segment(s)** (and any key differences to preserve)?
3. What’s the **scope boundary** (product area, timeframe, out-of-scope topics)?

## Inputs to request (only if missing)

- Study goal + research questions
- Participant/context (who, where, segment)
- Raw notes/transcripts or summary bullets
- Any constraints: timeline, scope, product area

## Synthesis workflow

1. Extract observations as atomic statements.
2. Cluster into themes (avoid “topic lists”; capture causality).
3. Convert themes into insights (so-what).
4. Map insights to opportunities and testable hypotheses.
5. Identify gaps and follow-up questions.

## Output template

```markdown
## Research synthesis summary
- **Assumptions/constraints**: …
- **Study goal**: …
- **Participants/context**: …
- **Top themes (headline)**:
  1. …
  2. …
  3. …

## Themes → insights → opportunities
### Theme: …
- **What we heard/observed**: …
- **Insight (so what)**: …
- **Opportunity**: …
- **Hypothesis**: If we … then … because …
- **Success signals**: metrics + qualitative indicators
- **Evidence**: quote(s), note snippet(s), counts (if provided)
- **Confidence**: High | Med | Low (what would raise confidence?)
- **Risks/notes**: …

## Evidence snippets
- “…” — P3
- “…” — P7

## Open questions
- …

## Recommended next steps
- …
```

## Quality bar

- Keep insights falsifiable and tied to evidence.
- Don’t propose solutions before establishing the underlying need.

