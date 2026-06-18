<!--
  Per-run rollup skeleton, written to runs/{runId}/run-summary.md.
  Aggregates the module analyses for this run.
-->

# Run Summary — {runId}

- **Project:** {display_name}
- **Project type:** {b2c | b2b | both}
- **Modules template version:** {modules=vX.Y.Z}
- **Completed modules:** {count} / {selected}
- **Status:** {complete | failed | cancelled}

## Highlights

Top cross-cutting findings across all modules in this run.

## Per-module results

### {module-id}
- **Status:** {SUCCESS | ERROR}
- **Top tasks:** {N high-priority}
- **Summary:** one-line takeaway. See `runs/{runId}/{module-id}/analysis.md`.

## Suggested next steps

The highest-leverage tasks to tackle first, drawn from each module's tasks.json.
