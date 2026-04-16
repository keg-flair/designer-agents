---
name: design-system-governance
description: Creates design-system governance artifacts: standards, contribution workflow, decision records, and release notes. Use when the user mentions design system, component library, tokens, governance, consistency, contribution, or releases.
---

# Design System Governance

## Defaults

- **Tool-agnostic**: governance should not depend on a specific design tool.
- **Adoption-first**: optimize for clarity, low friction, and repeatable review gates.
- **Reversible decisions**: include rationale and migration guidance when relevant.

## Constraints

- **Do not invent** existing system architecture or team topology—state assumptions and provide options.
- **Ask at most 3 clarifying questions** if it changes governance shape (multi-platform, external consumers, release model).
- **Keep artifacts copy/paste-ready** (templates that teams can use immediately).

## Clarifying questions (ask max 3)

Ask only if it changes the governance model or templates.

1. Who are the **primary consumers** (product teams only vs marketing vs external devs)?
2. What’s the **release model** (continuous, weekly, versioned) and what needs change control?
3. Is the system **single-platform or multi-platform** (web + iOS + Android) and how strict is parity?

## Inputs to request (only if missing)

- What artifacts exist today (tokens, components, guidelines, repos)
- Intended consumers (product teams, marketing, external devs)
- Current pain (inconsistency, velocity, duplication, adoption, quality)
- Release model preference (continuous, weekly, versioned)

## Deliverables (choose what the user asked for)

### 1) Contribution workflow

```markdown
## Contribution workflow (proposal)
### Assumptions/constraints
- …

### When to add vs extend vs deprecate
- **Add new component** when: …
- **Extend existing** when: …
- **Deprecate** when: …

### Request template
- **Problem**:
- **Use cases**:
- **Non-goals**:
- **Accessibility requirements**:
- **Token hooks / theming needs**:
- **Variants needed**:
- **Analytics/telemetry needs** (optional):

### Review gates
- [ ] Design QA: states, empty/loading/error
- [ ] A11y QA: focus/labels/contrast/motion
- [ ] Content: tone, localization readiness
- [ ] Engineering: API shape, theming, performance
```

### 2) Design decision record (DDR)

```markdown
## Design decision record
- **Assumptions/constraints**: …
- **Decision**: …
- **Status**: proposed | accepted | deprecated
- **Context**: …
- **Options considered**:
  1. …
  2. …
- **Decision drivers**: …
- **Outcome**: …
- **Follow-ups**: …
```

### 3) Release notes

```markdown
## Design system release notes
- **Assumptions/constraints**: …
- **Version/date**: …

### Added
- …

### Changed
- …

### Deprecated
- …

### Migration notes
- …
```

## Governance principles

- Prefer **few, flexible primitives** over many one-off components.
- Optimize for **consistency at scale**: tokens + components + guidelines + review gates.
- Make decisions reversible: document rationale + migration paths.

## Evidence + confidence rule

If proposing governance changes (process, release model, review gates), include:
- **Evidence**: what pain/input prompted the change (adoption issue, quality issue, velocity issue)
- **Confidence**: High | Med | Low (what would raise confidence?)

