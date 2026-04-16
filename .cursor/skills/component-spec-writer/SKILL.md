---
name: component-spec-writer
description: Writes a component spec for a design system component: variants, states, content rules, token hooks, and QA checklist. Use when the user asks for a component spec, variant matrix, component API, or design-system documentation.
---

# Component Spec Writer

## Inputs to request (only if missing)

- Component name + intended purpose
- Primary use cases and non-goals
- Target platforms (web/iOS/Android) and theming needs
- Any existing tokens/components to align with

## Output template

```markdown
## Component: [Name]
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

