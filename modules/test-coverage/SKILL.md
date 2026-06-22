# Test Coverage

## Scope
Assess automated test coverage and testing maturity: existing unit/integration/e2e tests,
frameworks, coverage tooling, and CI gates. Identify gaps and produce tasks to add tests or
integrate third-party coverage tools — static review only; no test execution or installs in repos.

## Inputs
- repos/: test files (`*test*`, `*spec*`, `__tests__/`), framework configs (`jest.config`,
  `vitest.config`, `pytest.ini`, `pyproject.toml` test sections, `Cargo.toml` dev-deps),
  coverage config (`.coveragerc`, `coverage.xml`, Istanbul/nyc, codecov.yml), CI workflow
  test and coverage steps.
- meta/: quality or release requirements if provided.
- project_type relevance: both.

## Method
1. Per repo, locate test directories and configs with `list_directory`/`grep_repo`.
2. Infer stack (Jest, Vitest, pytest, cargo test, etc.) and whether coverage is collected
   locally or in CI.
3. Sample high-risk areas with little or no test signal (critical services, auth, payments,
   data transforms) via `grep_repo` and targeted `read_file`.
4. Where CI exists but lacks coverage reporting, note alignment with cicd-pipeline-audit
   findings; recommend thresholds and upload steps (Codecov, Coveralls, Azure coverage).
5. Recommend third-party tools when absent: pytest-cov, vitest coverage, Istanbul/c8,
   mutation testing (optional) — include setup steps in tasks, not live installs.
6. Prioritize by risk and effort (S/M/L).

## Standards
Testing pyramid, meaningful coverage over vanity metrics, CI gating on test + coverage where
appropriate, provider docs for chosen stack.

## Output
Follow the output templates in `templates/`.
1. write_analysis("test-coverage", <markdown: per-repo inventory, gaps, tool recommendations>)
2. write_tasks("test-coverage", { ... }) — task id prefix `TST-`.

Each task's `agentic_spec` must name the target repo, files to test or config to add, and
how to verify (run test suite, generate coverage report, confirm CI step).

## Constraints
Repos are read-only. Do not run tests or install packages. Cite evidence paths for every
finding. Transient fetch failures are tolerated — retry or note uncertainty.
