<!--
  Raw analysis document skeleton.
  The agent fills this in and writes it via write_analysis("<module-id>", <content>).
  Keep headings; replace the guidance in each section with findings grounded in evidence
  (cite repo paths and line numbers, e.g. repos/web/src/search.ts:42).
-->

# {Module Name} — Analysis

- **Module:** {module-id}
- **Run:** {runId}
- **Project type:** {b2c | b2b | both}
- **Repos analyzed:** {repos/...}

## Summary

A few sentences: the headline findings and overall posture.

## Scope & Method

What was inspected, which tools/standards were applied, and any explicit exclusions.

## Findings

For each finding, include: what, where (evidence path:line), why it matters, and severity.

### Finding 1 — {title}
- **Evidence:** repos/.../file.ext:NN
- **Severity:** {high | medium | low}
- **Details:** ...

## Recommendations

Prioritized, actionable next steps. Each should map to one or more kanban tasks.

## Notes & Limitations

Assumptions, areas not covered, follow-up suggestions, and any online research used
(research/ files carry a provenance header — never confuse them with repo source).
