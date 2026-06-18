# Workspace Index

## Scope
Build and refresh the workspace index: scan repositories, meta documents, and run
artefacts; merge user annotations with AI/heuristic descriptions; write
`.workspace-index.json`.

This module runs deterministically (no LLM agent loop). Select it in the Pipeline
tab to rebuild the index on demand, or rely on automatic indexing after clone/pull,
meta changes, and pipeline runs.

## Output
Updated `.workspace-index.json` at the project root.
