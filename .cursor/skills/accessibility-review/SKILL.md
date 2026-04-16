---
name: accessibility-review
description: Reviews UI screenshots, flows, or specs for accessibility issues and fixes (WCAG-informed). Use when the user mentions accessibility, WCAG, contrast, keyboard navigation, screen readers, focus, semantics, or inclusive design.
---

# Accessibility Review

## Inputs to request (only if missing)

- Platform (web/iOS/Android) and interaction model (touch/keyboard)
- Any known standards target (e.g., WCAG AA) and constraints (brand colors, legacy UI)
- Screenshots or a link to the flow; note key components used

## Review checklist (prioritize these)

- **Contrast & color reliance**: text/icon contrast; meaning conveyed by color alone
- **Focus & keyboard** (web/desktop): tab order, focus visibility, traps, skip links
- **Touch targets** (mobile): minimum sizing, spacing, gesture alternatives
- **Content structure**: headings, landmarks, grouping, labels
- **Forms**: explicit labels, required fields, error messaging, helper text
- **Motion**: reduced motion, avoids vestibular triggers, no essential info in animation only
- **States**: empty/loading/error states are perceivable and actionable

## Output template

```markdown
## Accessibility review summary
- **Scope**: …
- **Highest risk areas**: …

## Findings (prioritized)
### Must-fix (blocks users)
- **Issue**: …
  - **Where**: …
  - **Who it affects**: …
  - **Why**: …
  - **Fix**: …
  - **How to verify**: manual check + tooling suggestion

### Should-fix (meaningful friction)
…

### Nice-to-have (polish)
…

## Quick regression checklist for future PRs
- [ ] Contrast is acceptable for text/icons
- [ ] Focus is visible and order is logical
- [ ] Form fields have labels + errors are announced/obvious
- [ ] Touch targets meet minimum size
- [ ] Reduced-motion path exists
```

## Guidance style

- Prefer specific remediations (“increase text to 14px and use token `fg/primary`”) over vague (“make it more accessible”).
- If you can’t verify from screenshots, state assumptions and give a verification plan.

