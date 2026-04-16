## Contributing

### Add a new agent (Cursor skill)

1. Create a new folder in `.cursor/skills/<skill-name>/`
2. Add a `SKILL.md` with YAML frontmatter:

```markdown
---
name: skill-name
description: What it does + when to use it (include trigger terms).
---
```

3. Keep `SKILL.md` concise (aim: < 500 lines) and include:
   - Inputs to request (only if missing)
   - A repeatable workflow/checklist
   - A copy/paste-ready output template

### Naming rules

- `name`: lowercase, numbers, hyphens only
- Folder name should match `name`

### Style

- Prefer “Figma-ready” outputs: crisp checklists, component/token naming, variant matrices.
- Default to a **single recommended approach** with an escape hatch, not a menu of options.

