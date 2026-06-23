# B2B Low-hanging Features

## Scope
Identify high-value, low-effort features that would make the product more attractive to
business (B2B) buyers: team/role management, SSO/SAML, audit logs, admin controls, usage
reporting, API access, SLAs, and seat-based billing hooks. Focus on what is cheap to add given
the existing codebase.

## Inputs
- repos/: existing auth, account/org models, settings, billing, API surface, admin UI.
- meta/: roadmap, sales feedback, target-account requirements if provided.
- project_type relevance: b2b (most relevant); for "both", weigh against b2c priorities.

## Method
1. Call `gather_context` on **every** cloned repo — include API/backend repos, not only frontends. For large repos use a subpath (e.g. `repos/API/src`) rather than the repo root.
2. Inventory current account/org/permission models and integration points (`grep_repo` with a source glob like `*.{ts,cs,java,py}`).
3. Identify B2B gaps (e.g. no org-level roles, no audit trail, no SSO).
4. For each gap, estimate effort (S/M/L) based on how much existing scaffolding can be reused.
5. Prioritize features with the best value-to-effort ratio.
6. Write outputs once you have **3–6 grounded opportunities** — do not exhaustively catalog shared UI component libraries.

## Standards
Common B2B SaaS expectations (RBAC, SSO/SAML/OIDC, audit logging, admin/reporting).

## Output
Follow the output templates in `templates/`.
1. write_analysis("b2b-low-hanging-features", <markdown: opportunities ranked by value/effort>)
2. write_tasks("b2b-low-hanging-features", { ... }) — task id prefix `B2B-`.

## Constraints
Repos are read-only. Ground every suggestion in existing code (cite where the hook would
attach). Avoid speculative features requiring a rewrite.
