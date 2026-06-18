# Tech Debt Triage

## Scope
Surface and prioritize technical debt: code smells, duplication, oversized
files/functions, dead code, missing tests around risky areas, TODO/FIXME backlog, and brittle
abstractions. Produce a triaged, actionable list rather than an exhaustive lint dump.

## Inputs
- repos/: source tree broadly; test directories; TODO/FIXME markers; config for linters.
- meta/: known pain points or engineering notes if provided.
- project_type relevance: both.

## Method
1. Use `grep_repo` for `TODO`, `FIXME`, `HACK`, `XXX`, `@deprecated`, and large commented blocks.
2. Identify oversized files/functions and obvious duplication patterns.
3. Assess test coverage qualitatively around high-churn or high-risk modules.
4. Triage: rank by (impact x likelihood) vs effort; group related debt into themes.

## Standards
Common refactoring/code-smell taxonomy; testing-pyramid principles.

## Output
Follow the output templates in `templates/`.
1. write_analysis("tech-debt-triage", <markdown: themes, each with evidence + impact>)
2. write_tasks("tech-debt-triage", { ... }) — task id prefix `DEBT-`.

## Constraints
Repos are read-only. Be selective — prioritize debt that blocks change or risks bugs over
cosmetic nits. Cite representative evidence rather than listing every occurrence.
