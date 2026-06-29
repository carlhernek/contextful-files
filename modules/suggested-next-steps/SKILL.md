# Suggested Next Steps

## Scope

Produce the workspace **trajectory plan**: what to run next, what to carry over, and what changed
since the last analysis run. This module infers state from run history and index/meta deltas — it
does not ask the user which path to take.

Outputs are concrete `NEXT-*` tasks (ordered module runs, prep steps, follow-ups), not advisory
copy.

## Inputs

- `gather_run_history` (mandatory first tool call)
- `.workspace-index.json` (via history tool delta + optional `read_file`)
- `meta/` documents (especially new/changed items from delta)
- `runs/` artifacts (`run-summary.md`, `tasks.json` from recent runs)
- `project_type` from workspace context (`b2c`, `b2b`, or `both`)

## Method

1. Call **`gather_run_history`** with no arguments. Branch on `mode` from the JSON response.
2. **Do not** ask the user whether this is a first run or a follow-up — the tool decides.

### Initial mode (`mode: "initial"`)

No completed run yet that includes analysis modules beyond `workspace-index`.

1. Read `.workspace-index.json` and skim `meta/` for domain context (requirements, transcripts).
2. Build an ordered **starter module sequence** from `project_type` and the tables below.
3. Emit one `NEXT-*` task per module in run order. Each task `agentic_spec` states what that
   module run should cover and which repos/meta paths matter.
4. Include prep tasks where needed (e.g. transcribe new audio, refresh workspace index).

**Starter order by project type** (skip modules already irrelevant to the workspace):

| Step | b2b | b2c | both |
|------|-----|-----|------|
| 1 | workspace-index | workspace-index | workspace-index |
| 2 | security-analysis | security-analysis | security-analysis |
| 3 | dependency-health | dependency-health | dependency-health |
| 4 | b2b-low-hanging-features | b2c-campaign-ideas | swot-analysis |
| 5 | documentation-gap-analysis | documentation-gap-analysis | documentation-gap-analysis |
| 6 | tech-debt-triage | onboarding-flow-audit | b2b-low-hanging-features + b2c-campaign-ideas |
| 7 | test-coverage | test-coverage | tech-debt-triage |

Adjust order when repos lack signals (e.g. no `package.json` → defer dependency-health).

### Warm mode (`mode: "warm"`)

At least one completed analysis run exists. `anchorUpdatedAt` marks the delta cutoff.

1. Use `runs` and `openTasks` from `gather_run_history` for the timeline.
2. Read `summaryPath` and top `tasks.json` files for the **last 2–3 runs** only (not every artifact).
3. Use `delta.newItems` and `delta.changedItems` to identify meta/index changes since the anchor.
4. Prioritize:
   - High-priority open tasks from `openTasks` (carry-over)
   - Re-run modules only where new/changed meta docs materially affect that module's scope
   - Modules in the starter set that have **never** completed
5. Tasks should be follow-through and targeted re-runs — not a full restatement of every past finding.

## Standards

- Ground every task in evidence paths (runs, meta, repos, or delta items).
- Use imperative titles; no "we recommend" or "consider" phrasing.
- Cite delta items by `path` when meta changed since the anchor run.

## Output

Follow the output templates in `templates/`.

1. `write_analysis("suggested-next-steps", <markdown: mode, trajectory summary, delta summary, module plan>)`
2. `write_tasks("suggested-next-steps", { ... })` — task id prefix `NEXT-`.

## Constraints

Repos are read-only. Prefer `gather_run_history` over manually listing every run folder.
Stop after `write_analysis` + `write_tasks`; do not re-explore completed modules in depth.
