# API Surface Analysis

## Scope
Map the product's API surface (HTTP/GraphQL/RPC endpoints) and evaluate authentication,
authorization, input validation, versioning, error handling, and documentation coverage.
Identify auth gaps and inconsistent patterns. Static review from route/handler source.

## Inputs
- repos/: route definitions, controllers/handlers, middleware, API schemas (OpenAPI/GraphQL
  SDL/proto), auth guards.
- meta/: API specs or contracts if provided.
- project_type relevance: both (B2B often needs documented, versioned public APIs).

## Method
1. Enumerate endpoints via `grep_repo` (router decorators, route tables, schema files).
2. For each endpoint, determine: method/path, auth requirement, authz checks, input validation,
   and rate limiting.
3. Flag unauthenticated state-changing endpoints, missing authz, unvalidated input, inconsistent
   error shapes, and undocumented endpoints.
4. Compare implemented endpoints against any API schema/spec for drift.

## Standards
REST/GraphQL conventions, OWASP API Security Top 10, OpenAPI as the documentation contract.

## Output
Follow the output templates in `templates/`.
1. write_analysis("api-surface-analysis", <markdown: endpoint inventory table + gap analysis>)
2. write_tasks("api-surface-analysis", { ... }) — task id prefix `API-`.

## Constraints
Repos are read-only. Provide an endpoint inventory even if large; cite handler path:line.
Use `grep_repo` caps rather than reading entire route trees.
