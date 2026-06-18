# Workspace Index

## Scope
Build and refresh the workspace index: scan repositories, meta documents, and run
artefacts; enrich with AI/heuristic descriptions; write `.workspace-index.json`.

This module runs deterministically (no LLM agent loop). **Select it in the Pipeline
tab** when you want to scan the workspace and build or refresh the index.

Indexing does **not** run automatically on git clone/pull, meta upload/delete, or
other pipeline modules — only when this module is explicitly run.

Manual description/keyword edits in the GUI write directly to `.workspace-index.json`
and are preserved on the next run of this module.

## Output
Updated `.workspace-index.json` at the project root.
