# Workspace Index

## Scope

Build and refresh the workspace index: scan repositories, meta documents, and run
artefacts; enrich each item with a bounded AI agent (or reuse cache/heuristics); write
`.workspace-index.json`.

**Select this module in the Pipeline tab** when you want to scan the workspace and build
or refresh the index. Progress streams live in **Results → Activity** for the run.

Indexing does **not** run automatically on git clone/pull, meta upload/delete, or other
pipeline modules — only when this module is explicitly run.

## How it runs

The app uses a dedicated **agentic indexer** (not the standard module-agent loop):

1. **Scan** — enumerate repos, meta docs, and run artefacts (`SCAN_START` / `SCAN_DONE`).
2. **Enumerate** — write a skeleton `.workspace-index.json`; cached items skip AI.
3. **Per item** — up to 6 turns per item with tools: `gather_context`, `read_file`,
   `list_directory`, `grep_repo`. Agents prefer docs/README/specs via `gather_context`
   before reading whole trees.
4. **Output** — each item gets a one-line `description` and 3–8 `keywords`; activity is
   persisted to `runs/<runId>/workspace-index/activity.jsonl`.

Items whose content hash unchanged since the last run are **cache hits** (no LLM call).
Manual description/keyword edits in the GUI write directly to `.workspace-index.json`
and are preserved on the next run.

## Output

Updated `.workspace-index.json` at the project root.
