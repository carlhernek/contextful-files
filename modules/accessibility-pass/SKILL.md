# Accessibility Pass

## Scope
Assess WCAG conformance of the product's user interfaces from source: semantic markup, ARIA,
keyboard operability, focus management, color contrast (where defined in code/tokens), form
labeling, and alt text. Static source review only — no live screen-reader or browser testing.

## Inputs
- repos/: frontend code (HTML/JSX/TSX/Vue/Svelte), component libraries, CSS/Tailwind theme
  tokens, design-system files.
- meta/: accessibility requirements or design specs if provided.
- project_type relevance: both (a11y applies regardless of audience).

## Method
1. Locate UI components and templates with `list_directory`/`grep_repo`.
2. Check for: missing `alt`, non-semantic clickable `div`/`span`, missing form `label`/`for`,
   `tabindex` misuse, `aria-*` correctness, focus traps, `outline: none` without replacement,
   and headings hierarchy.
3. Inspect color tokens/contrast definitions where contrast is encoded in source.
4. Map each issue to a WCAG 2.2 success criterion (level A/AA) and assign severity.

## Standards
WCAG 2.2 AA, WAI-ARIA Authoring Practices.

## Output
Follow the output templates in `templates/`.
1. write_analysis("accessibility-pass", <markdown grouped by WCAG criterion>)
2. write_tasks("accessibility-pass", { ... }) — task id prefix `A11Y-`.

## Constraints
Repos are read-only. Prefer `grep_repo` to find patterns across many components. Note where a
finding can only be confirmed by runtime testing (out of scope) as a limitation.
