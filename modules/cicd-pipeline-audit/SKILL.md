# CI/CD Pipeline Audit

## Scope
Evaluate the quality, security, and reliability of CI/CD configuration: pipeline coverage
(build/test/lint/release), secret handling, permission scoping, caching, action/version
pinning, and supply-chain hardening. Static review of pipeline config only.

## Inputs
- repos/: `.github/workflows/*`, `.gitlab-ci.yml`, `azure-pipelines.yml`, `Jenkinsfile`,
  `.circleci/`, `bitbucket-pipelines.yml`, build scripts, Dockerfiles relevant to CI.
- meta/: release process or deployment requirements if provided.
- project_type relevance: both.

## Method
1. Locate pipeline files with `grep_repo`/`list_directory`.
2. Assess coverage: are build, test, lint, and security steps present and gating?
3. Check security: unpinned third-party actions (`@main`), broad `permissions`, secrets echoed
   to logs, `pull_request_target` misuse, missing least-privilege tokens.
4. Check reliability: caching, matrix correctness, flaky-step patterns, missing concurrency
   controls, no environment protection on deploy.
5. Recommend concrete config improvements.

## Standards
Provider best practices (GitHub Actions hardening guide), least-privilege, SLSA concepts,
pinned dependencies by digest/tag.

## Output
Follow the output templates in `templates/`.
1. write_analysis("cicd-pipeline-audit", <markdown grouped by coverage/security/reliability>)
2. write_tasks("cicd-pipeline-audit", { ... }) — task id prefix `CICD-`.

## Constraints
Repos are read-only. Cite the exact workflow file and line for each finding.
