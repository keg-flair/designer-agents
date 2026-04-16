---
name: analytics-insights
description: Translates product analytics (funnels, events, conversion, drop-off) into UX insights, hypotheses, and experiment ideas. Use when the user provides metrics, dashboards, event tables, or asks “what do these numbers mean for UX?”.
---

# Analytics → UX Insights

## Inputs to request (only if missing)

- Metric definitions (conversion, activation, retention) and timeframe
- Segment definitions (new vs returning, geo, device, plan)
- Event/funnel steps and known tracking limitations
- Screenshots of relevant UI or flow description

## Reasoning approach

1. Restate definitions and confirm what is actually measured.
2. Identify the “biggest leaks” by impact (volume × drop-off).
3. Generate hypotheses rooted in UX mechanisms (comprehension, trust, effort, latency).
4. Propose:
   - quick diagnostic checks (breakdown, cohort, step-time)
   - design changes (copy, structure, defaults)
   - measurement improvements (events/properties)

## Output template

```markdown
## Analytics insight summary
- **Goal metric**: …
- **Timeframe/segment(s)**: …
- **Key anomaly**: …

## Funnel/metric readout
- **Step 1 → 2**: …
- **Step 2 → 3**: …
- **Biggest opportunity**: …

## Hypotheses (ranked)
### H1: …
- **Mechanism**: why users drop off (effort, confusion, trust, etc.)
- **Where in UI**: …
- **Evidence**: metric pattern + screenshot cues
- **Design changes to try**:
  1. …
  2. …
- **What to measure**: event/property changes + success criteria

## Quick follow-up analyses
- Segment breakdowns to run
- Step-time analysis ideas
- Error/latency correlation checks

## Instrumentation gaps
- Missing events/properties
- Ambiguous definitions
```

## Quality bar

- Don’t over-claim causality; label uncertain hypotheses.
- Prefer the smallest change that tests the highest-impact hypothesis.

