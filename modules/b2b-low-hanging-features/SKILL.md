# B2B Low-hanging Features

## Scope

Find **high-value, low-effort B2B product opportunities** — features that would make the
platform more attractive to business buyers and are cheap to add because the codebase (especially
the API/backend) already supports most of the work.

Do **not** produce a generic B2B checklist (SSO, RBAC, etc.) unless repo evidence shows a real gap.
Every finding must fall into one of the three opportunity types below and cite where the hook
would attach.

### Opportunity type A — API-ready, UI-missing (cross-platform parity)

Features **already supported by the API/backend** (or internal admin tools) that are **not yet
exposed** on one or more customer-facing or partner-facing platforms.

Typical pattern: backend endpoint + backoffice UI exist, but the business portal / my-pages /
mobile app / external integrator surface does not.

For each repo set, identify the **interfacing platforms** (e.g. internal admin UI, business
customer portal, consumer app, partner API) and map which capabilities exist where.

**Good example:** Service-account API key issuance exists in `repos/API` and backoffice, but
business customers cannot self-serve keys in `repos/my_pages`.

### Opportunity type B — Competitor gap with internal scaffolding

Features **offered by competing platforms** in this product category that **this platform lacks
in the UI**, where the repos may already contain partial support (models, endpoints, unused
flags, backoffice-only flows).

Use `web_fetch` on competitor marketing pages, feature lists, or docs (save summaries under
`research/` with provenance headers). Do **not** call `web_search` — it is unavailable.

For each competitor feature gap, **grep the repos** for related models, endpoints, or UI before
claiming greenfield work. Prefer opportunities where internal scaffolding exists.

### Opportunity type C — Commonplace B2B function missing

Standard B2B SaaS expectations the platform **does not meet**, grounded in repo evidence — not
a generic industry list.

**Good examples (from prior runs):**
- **Audit log** for organization admin actions (notification logs exist, but no admin-action trail)
- **Usage / billing dashboard** for business customers (reports exist in admin, not in portal)
- **Seat-based billing hooks** (billing exists per-product, but no per-seat / per-employee model)

Only include items where you can point to existing billing, auth, logging, or reporting
infrastructure that could be extended rather than built from scratch.

## Inputs

- repos/: API/backend, admin UI, customer/business portals, mobile apps — all cloned repos.
- meta/: roadmap, sales feedback, target-account requirements, named competitors if provided.
- project_type relevance: **b2b** (primary); for **both**, focus on business-customer flows.

## Method

Work in three passes — one per opportunity type. Stop each pass once you have 1–3 grounded items
or clear evidence the type does not apply.

### Pass 1 — Cross-platform parity (type A)

1. Call `gather_context` on **every** cloned repo (use subpaths for large repos, e.g.
   `repos/API/src`).
2. Inventory the **external/partner API** and key org-admin endpoints (`grep_repo` on route
   registration, OpenAPI/DOCS.md, controller modules).
3. For each major B2B capability found in API or backoffice, check whether it appears in
   customer-facing repos (business portal routes, services, menus).
4. Record gaps where API + admin exist but a customer/partner UI does not.

### Pass 2 — Competitive gaps (type B)

1. Identify 2–4 competitors from meta docs or, if none provided, from `web_fetch` of the
   product category (save under `research/`).
2. List 3–5 B2B features competitors highlight (SSO, team management, usage reports, API
   self-service, audit trails, etc.).
3. For each, search repos for existing support. Classify as: **already built elsewhere**,
   **partial scaffolding**, or **no support**.
4. Keep only gaps where effort is low because scaffolding exists (type B) or type A/C also applies.

### Pass 3 — Commonplace B2B gaps (type C)

1. Check auth (SSO/SAML/OIDC), org RBAC, audit/activity logs, usage/reporting dashboards,
   API self-service, and billing models (per-seat, per-org) against repo evidence.
2. Prefer gaps where infrastructure exists but the B2B buyer-facing experience is incomplete —
   audit logs, billing summaries, and seat counters are common wins.
3. Estimate effort (S/M/L) from how much existing code can be reused.

### Finalize

- Aim for **4–8 findings** across the three types, ranked by value-to-effort.
- Label each finding with its type: `[A]`, `[B]`, or `[C]`.
- Write outputs once findings are summarized — do not exhaustively catalog shared UI libraries.

**Turn budget:** after one pass per type, stop exploring and call `write_analysis` +
`write_tasks`. Partial output beats no output.

## Standards

B2B buyer expectations: RBAC, SSO/OIDC, audit logging, admin self-service, usage/reporting,
API access, consolidated billing. Apply only when repo evidence confirms a gap.

## Output

Follow the output templates in `templates/`.

Structure findings under three subsections (skip empty sections):

```markdown
## Findings

### Type A — API-ready, UI-missing
### Type B — Competitor gap (internal support)
### Type C — Commonplace B2B gap
```

Each finding: title, type tag, evidence (`repos/...:line`), severity, which platform(s) would
surface it, and effort (S/M/L).

1. `write_analysis("b2b-low-hanging-features", <markdown>)`
2. `write_tasks("b2b-low-hanging-features", { ... })` — task id prefix `B2B-`; each task should
   state opportunity type and target repo(s) in `rationale` / `agentic_spec`.

## Constraints

Repos are read-only. Ground every suggestion in existing code. Cite hook points for API, admin
UI, and customer portal separately when relevant. Avoid speculative full rewrites.
