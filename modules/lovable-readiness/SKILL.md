# Lovable Readiness Audit

## Scope
Deep static readiness audit of vibecoded React + Supabase apps (Lovable/Bolt/v0-style)
across four lenses in one pass: security, scalability, EU GDPR compliance, and WCAG/A11Y.
Targets the pitfalls these rapidly-generated apps repeatedly ship. Source-based only — no
live scanning, load testing, or screen-reader testing.

## Inputs
- repos/: React/Vite/Next frontend, Supabase artifacts (`supabase/migrations/*.sql`,
  `supabase/config.toml`, edge functions under `supabase/functions/`), client init
  (`createClient`), env files (`.env*`, `*.env.example`), and any RLS/policy SQL.
- `supabase/<name>/*.json` (when present): **live Management API config snapshots** for the
  connected project(s) — `meta.json` (ref, name, region/residency, status), `advisors.json`
  or `advisors_security.json`/`advisors_performance.json` (RLS-disabled, unindexed FKs and
  other lints), `auth.json` (sign-up, email confirmation, JWT expiry, OAuth, MFA), `api.json`
  (exposed schemas, `max_rows`), `storage.json`, `functions.json` (`verify_jwt`),
  `database_*.json` (SSL enforcement, pooler), `network.json`, and `api_keys.json` (key
  types/presence only — never secret values). These appear in the workspace index as type
  `supabase`. They are config + advisor metadata only: no SQL and no row data.
- meta/: requirements, privacy policy, DPA, or target audience/region if provided.
- project_type relevance: both (b2c consumer-data risk and b2b tenant-isolation risk apply).

## Method
1. Call `gather_context` on **every** cloned repo first (include any API/edge-function repo).
2. **Check for live Supabase snapshots first.** Look in the workspace index for type `supabase`
   items and `read_file` the relevant `supabase/<name>/*.json`. When present, treat them as the
   **primary, authoritative evidence** for project posture and reconcile source findings against
   them; when absent, fall back to source-only analysis and record that as an explicit
   limitation in the analysis (config could not be verified against the live project).
3. Detect the stack: confirm React + Supabase via `grep_repo` for `@supabase/supabase-js`,
   `createClient`, `supabase/` dirs, and `package.json`. Note framework (Vite vs Next).
4. **Security** — the dominant risk for this stack.
   - When a snapshot exists, lead with `advisors.json`/`advisors_security.json`: RLS-disabled
     tables, missing policies, and `security definer`/exposure lints are authoritative — cite
     `supabase/<name>/advisors_security.json`. Use `auth.json` for open sign-up, disabled email
     confirmation, JWT expiry, and missing MFA; `api.json` for over-broad exposed schemas /
     `max_rows`; `storage.json` for public buckets; `functions.json` for `verify_jwt:false`;
     `network.json` for `0.0.0.0/0` exposure; `database_*.json` for SSL enforcement; and
     `api_keys.json` for which key types exist (presence only).
   - Then use `grep_repo` (scope with `glob: "*.{ts,tsx,js,jsx,sql,toml}"`) for source-side
     issues and to corroborate: RLS disabled / `using (true)` policies vs tables in
     `supabase/migrations/`; secrets shipped to the client (`service_role`,
     `SUPABASE_SERVICE_ROLE`, anything under `VITE_`/`NEXT_PUBLIC_`/`REACT_APP_`); anon-key
     misuse for privileged writes; permissive CORS (`Access-Control-Allow-Origin: *`) in edge
     functions; raw SQL string concatenation; and `dangerouslySetInnerHTML`.
   - Map each finding to OWASP Top 10 (2021) and assign severity.
5. **Scalability** — prefer `advisors_performance.json` (unindexed foreign keys, unused
   indexes, etc.) when present, citing it. Then flag from source: `select('*')` / unbounded
   queries, no pagination (`range`/`limit`), client-side joins and N+1 loops, missing indexes
   for filtered/foreign-key columns, unbounded realtime subscriptions, absent rate limiting,
   large client bundles, and files stored as base64/bytea in rows instead of Storage.
6. **GDPR (EU focus)** — read region / data residency from `meta.json` (authoritative) when
   present; otherwise infer from source/config and note the uncertainty. Also: PII inventory in
   schemas, analytics/tracking firing before consent (PostHog/GA/Sentry), DSAR support
   (export/delete endpoints), retention/deletion, transfers to US sub-processors, and
   lawful-basis hooks. Frame findings as engineering risks, not legal advice.
7. **WCAG / A11Y** — semantic markup vs clickable `div`/`span`, missing `alt`, missing form
   `label`/`for`, focus management and visible focus (`outline: none`), keyboard operability,
   `aria-*` correctness, and contrast encoded in Tailwind/theme tokens. Map to WCAG 2.2 AA.
8. Write outputs once findings are grounded — do not exhaustively read every file.

## Standards
OWASP Top 10 (2021) and Supabase RLS/security guidance; GDPR principles (data minimization,
storage limitation, DSAR, lawful basis); WCAG 2.2 AA and WAI-ARIA Authoring Practices.

## Output
Follow the output templates in `templates/`.
1. write_analysis("lovable-readiness", <markdown grouped into Security / Scalability / GDPR /
   Accessibility sections, each finding citing evidence path:line>)
2. write_tasks("lovable-readiness", { ...validates against templates/tasks.schema.json... })
   Use task id prefix `LOVE-`. Cite evidence as `repos/<name>/<path>:<line>` for source
   findings and `supabase/<name>/<file>.json` for live-config findings.

## Constraints
Repos and `supabase/<name>/*.json` snapshots are read-only. Prefer scoped `grep_repo` over
reading whole files; only `read_file` specific suspect files and the relevant snapshot JSONs.
The snapshots are config + advisor metadata only — never assume they contain database rows or
secret key values. A `service_role` key or secret reachable from client code, and any table
without RLS (whether found in source or flagged by `advisors_security.json`), are high
severity. This is not legal advice — frame GDPR findings as engineering risks. Use
web_search/web_fetch only to confirm CVE/standard details, saving any fetched material under
research/ with the provenance header.
