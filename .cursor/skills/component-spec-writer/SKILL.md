---
name: component-spec-writer
description: Writes a component spec for a design system component: variants, states, content rules, token hooks, and QA checklist. Use when the user asks for a component spec, variant matrix, component API, or design-system documentation.
---

# Component Spec Writer

## Defaults

- **Tool-agnostic**: describe behaviors and token hooks without requiring a specific tool/plugin.
- **System-first**: prefer extending existing primitives/patterns over creating new components.
- **Spec is implementable**: include states, content rules, a11y, and QA checklist by default.

## Constraints

- **Do not invent** token sets, platform constraints, or existing component APIs—state assumptions and offer options.
- **Ask at most 3 clarifying questions** if it changes the API surface (platform(s), theming, accessibility target).
- **Minimize invalid combinations**: prefer constraints via prop design rather than long “invalid combos” lists.

## Clarifying questions (ask max 3)

Ask only if it changes the spec’s API surface or required states.

1. What are the **platform targets** (web/iOS/Android) and any parity requirements?
2. What’s the **theming model** (light/dark, high-contrast, multiple brands) and must-support themes?
3. What’s the **accessibility target** and any content constraints (localization, dynamic type)?

## Inputs to request (only if missing)

- Component name + intended purpose
- Primary use cases and non-goals
- Target platforms (web/iOS/Android) and theming needs
- Any existing tokens/components to align with

## Output template

```markdown
## Component: [Name]
### Assumptions/constraints
- …

### Purpose
- **What it is**: …
- **When to use**: …
- **When not to use**: …

### Anatomy
- **Slots**: label, icon, leading/trailing, supporting text, badge, etc.
- **Content rules**: max chars/lines, truncation, localization, dynamic type

### Variants (inputs)
- **Variant props**:
  - `size`: …
  - `tone` (or `intent`): …
  - `emphasis`: …
  - `icon`: none | leading | trailing | only
  - `state`: enabled | hover | pressed | focused | disabled | loading

### States & behaviors
- **Interaction**: hover/press/focus behaviors
- **Loading**: …
- **Disabled**: …
- **Error** (if applicable): …

### Layout rules
- Padding/gap rules by size
- Alignment rules
- Responsive behavior

### Accessibility
- Name/label rules
- Focus behavior (if applicable)
- Touch target minimums
- Contrast considerations

### Token hooks
- **Color tokens**: …
- **Typography tokens**: …
- **Spacing/radius/elevation tokens**: …

### Analytics (optional)
- Recommended event names + properties

### QA checklist
- [ ] Variant matrix covered
- [ ] Empty/long text handled
- [ ] Loading/disabled verified
- [ ] A11y verified (labels/focus/targets)
- [ ] Theming verified (dark/high-contrast)
```

## Variant matrix guidance

If the component is complex, include a compact matrix showing which combinations are valid/invalid and why (default to minimizing invalid combos).

## Evidence + confidence rule

When making spec decisions beyond what the user provided, include:
- **Evidence**: what input drove the decision (existing pattern, constraint, platform guideline, user-provided requirement)
- **Confidence**: High | Med | Low (what would raise confidence?)

