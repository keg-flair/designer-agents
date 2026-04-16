---
name: design-system-governance
description: Creates design-system governance artifacts: standards, contribution workflow, decision records, and release notes. Use when the user mentions design system, component library, tokens, governance, consistency, contribution, or releases.
---

# Design System Governance

## Inputs to request (only if missing)

- What artifacts exist today (tokens, components, guidelines, repos)
- Intended consumers (product teams, marketing, external devs)
- Current pain (inconsistency, velocity, duplication, adoption, quality)
- Release model preference (continuous, weekly, versioned)

## Deliverables (choose what the user asked for)

### 1) Contribution workflow

```markdown
## Contribution workflow (proposal)
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

