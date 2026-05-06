# Agent Eval Harness

Use this harness to stress-test the designer-agent skills with repeatable cases and a shared rubric.

## Recommended Workflow

1. Validate the fixtures:

```bash
python3 scripts/agent_eval_harness.py validate
```

2. List cases:

```bash
python3 scripts/agent_eval_harness.py list
python3 scripts/agent_eval_harness.py list --priority P0
python3 scripts/agent_eval_harness.py list --skill analytics-insights
```

3. Start a run:

```bash
python3 scripts/agent_eval_harness.py start --priority P0 --name p0-smoke
```

This creates:

- `eval-runs/<run-name>/prompts/`: one prompt per case
- `eval-runs/<run-name>/outputs/`: put agent outputs here
- `eval-runs/<run-name>/scorecard.md`: manual scoring sheet
- `eval-runs/<run-name>/manifest.json`: run metadata

4. Run each prompt through the target agent or model.

5. Save each response in `outputs/<case-id>.md`.

6. Run lightweight checks:

```bash
python3 scripts/agent_eval_harness.py check analytics-insights-partial-funnel --output eval-runs/p0-smoke/outputs/analytics-insights-partial-funnel.md
```

The check command catches missing required signals and forbidden terms. It does not replace manual review.

## What To Score

Use `rubric.json` for the 1-5 manual score:

- Task success
- Instruction compliance
- Evidence discipline
- Output quality
- Risk and recovery
- Tool discipline

A run should usually pass only if:

- weighted score is 4.0 or higher
- no category is below 3
- no forbidden behavior appears

## Adding Cases

Add cases to `cases.json`. Each case should include:

- `id`: lowercase kebab-case
- `skill`: target skill or `cross-agent`
- `priority`: `P0`, `P1`, or `P2`
- `type`: contract, adversarial, e2e, tool-discipline, fallback, or regression
- `prompt`: the exact prompt to run
- `expected.required_sections`: section labels or signals that should appear
- `expected.required_terms`: important terms or concepts
- `expected.behaviors`: behaviors for manual review
- `forbidden.terms`: phrases that should not appear
- `forbidden.behaviors`: behaviors that fail the case

Keep cases small and decisive. A good case tests one failure mode clearly.

## Test Plan / How To Verify Harness Changes

After editing cases, rubric, or the runner:

```bash
python3 scripts/agent_eval_harness.py validate
python3 scripts/agent_eval_harness.py list --priority P0
python3 scripts/agent_eval_harness.py render ux-audit-vague-flow
python3 scripts/agent_eval_harness.py start --case-id ux-audit-vague-flow --name smoke-local
```

Remove generated local run folders when you no longer need them, or keep them outside git.
