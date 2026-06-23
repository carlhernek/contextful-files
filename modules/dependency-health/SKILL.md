# Dependency Health

## Scope
Assess the health of third-party dependencies: outdated versions, known-vulnerable packages,
unmaintained/abandoned libraries, and duplicated or conflicting versions. Source-based review
of manifests and lockfiles; no package installation or live audit execution.

## Inputs
- repos/: dependency manifests and lockfiles (`package.json`/`package-lock.json`/`yarn.lock`/
  `pnpm-lock.yaml`, `requirements.txt`/`pyproject.toml`/`uv.lock`, `Cargo.toml`/`Cargo.lock`,
  `go.mod`/`go.sum`, `pom.xml`, `Gemfile.lock`, etc.).
- meta/: dependency or supply-chain policy if provided.
- project_type relevance: both.

## Method
1. Call `gather_context` on each relevant repo first.
2. Locate all manifests/lockfiles with `list_directory`/`grep_repo`.
3. Extract direct dependencies and pinned versions.
4. Use web_search/web_fetch to check latest stable versions and known CVEs/advisories for the
   most critical packages; save findings under research/ with provenance headers.
5. Flag majorly outdated, vulnerable, or unmaintained packages; note version conflicts.
6. Recommend upgrade paths, noting breaking-change risk (S/M/L effort).
7. Write outputs once dependency risks are summarized.

## Standards
Semantic versioning, public advisory databases (CVE/GHSA), maintenance signals (last release).

## Output
Follow the output templates in `templates/`.
1. write_analysis("dependency-health", <markdown: per-ecosystem table of risks + upgrades>)
2. write_tasks("dependency-health", { ... }) — task id prefix `DEP-`.

## Constraints
Repos are read-only; never install packages. Verify advisory claims via research before
asserting a CVE. Transient fetch failures are tolerated (turns refunded) — retry.
