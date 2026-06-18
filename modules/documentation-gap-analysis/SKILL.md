# Documentation Gap Analysis

## Scope
Find missing, stale, or inadequate documentation: README quality, setup/run instructions,
architecture docs, API docs, inline docs for public interfaces, and changelog hygiene.
Compare documented behavior against actual code to detect drift.

## Inputs
- repos/: `README*`, `docs/`, `CONTRIBUTING*`, `CHANGELOG*`, code comments/docstrings, API
  schema files, example/config files.
- meta/: documentation standards if provided.
- project_type relevance: both.

## Method
1. Inventory existing docs with `list_directory`/`grep_repo`.
2. Assess setup docs by checking referenced scripts/commands actually exist in the repo.
3. Detect drift: documented endpoints/flags/config vs what the code implements.
4. Identify undocumented public APIs, env vars, and configuration.
5. Prioritize gaps by how much they block contributors or users.

## Standards
Diátaxis (tutorials/how-to/reference/explanation) as a framing; keep-a-changelog conventions.

## Output
Follow the output templates in `templates/`.
1. write_analysis("documentation-gap-analysis", <markdown: gaps grouped by doc type>)
2. write_tasks("documentation-gap-analysis", { ... }) — task id prefix `DOC-`.

## Constraints
Repos are read-only. When flagging drift, cite both the doc location and the code location.
