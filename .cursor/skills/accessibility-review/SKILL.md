---
name: accessibility-review
description: Reviews UI screenshots, flows, or specs for accessibility issues and fixes (WCAG-informed). Use when the user mentions accessibility, WCAG, contrast, keyboard navigation, screen readers, focus, semantics, or inclusive design.
---

# Accessibility Review

## Defaults

- **WCAG-informed**: default target is **WCAG 2.2 AA** unless the user specifies otherwise.
- **Tool-agnostic**: do not assume specific design tools/plugins.
- **Actionable fixes**: include concrete remediations and how to verify.

## Constraints

- **Do not invent** implementation details (DOM semantics, ARIA, focus order) if only screenshots are provided—state assumptions and provide a verification plan.
- **Ask at most 3 clarifying questions** if platform/standard materially changes guidance.
- **Prioritize blocked access first** (can’t perceive/operate/understand) before polish.

## Clarifying questions (ask max 3)

Ask only if it changes the remediation guidance.

1. What’s the **platform + interaction model** (web keyboard, mobile touch, desktop app)?
2. Is there a required **a11y target** (default WCAG 2.2 AA) or internal policy?
3. Are there **non-negotiable constraints** (brand colors, legacy UI, component library limits)?

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
- **Assumptions/constraints**: …
- **Scope**: …
- **Highest risk areas**: …

## Findings (prioritized)
### Must-fix (blocks users)
- **Issue**: …
  - **Where**: …
  - **Who it affects**: …
  - **Why**: …
  - **Evidence**: screenshot cue(s) and/or spec detail(s)
  - **Confidence**: High | Med | Low (what would raise confidence?)
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
- Every finding must include **Evidence** + **Confidence**; if confidence is low, include a concrete verification step.

