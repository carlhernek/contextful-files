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
- meta/: requirements, privacy policy, DPA, or target audience/region if provided.
- project_type relevance: both (b2c consumer-data risk and b2b tenant-isolation risk apply).

## Method
1. Call `gather_context` on **every** cloned repo first (include any API/edge-function repo).
2. Detect the stack: confirm React + Supabase via `grep_repo` for `@supabase/supabase-js`,
   `createClient`, `supabase/` dirs, and `package.json`. Note framework (Vite vs Next).
3. **Security** — the dominant risk for this stack. Use `grep_repo` (scope with
   `glob: "*.{ts,tsx,js,jsx,sql,toml}"`) for:
   - RLS disabled or tables with no policy: `enable row level security`, `using (true)`,
     `policy` definitions vs tables in `supabase/migrations/`.
   - Secrets shipped to the client: `service_role`, `SUPABASE_SERVICE_ROLE`, and any secret
     under a client-exposed prefix (`VITE_`, `NEXT_PUBLIC_`, `REACT_APP_`).
   - Anon-key misuse for privileged writes, public storage buckets (`public: true`),
     open sign-up / disabled email confirmation, missing per-route/page authz guards,
     permissive CORS (`Access-Control-Allow-Origin: *`) in edge functions, raw SQL string
     concatenation, and `dangerouslySetInnerHTML`.
   - Map each finding to OWASP Top 10 (2021) and assign severity.
4. **Scalability** — flag: `select('*')` / unbounded queries, no pagination (`range`/`limit`),
   client-side joins and N+1 query loops, missing indexes for filtered/foreign-key columns,
   unbounded realtime subscriptions, absent rate limiting, large client bundles, and files
   stored as base64/bytea in table rows instead of Storage.
5. **GDPR (EU focus)** — Supabase project region / data residency, PII inventory in schemas,
   analytics/tracking firing before consent (PostHog/GA/Sentry), DSAR support (export/delete
   endpoints), retention/deletion, transfers to US sub-processors, and lawful-basis hooks.
   Frame findings as engineering risks, not legal advice.
6. **WCAG / A11Y** — semantic markup vs clickable `div`/`span`, missing `alt`, missing form
   `label`/`for`, focus management and visible focus (`outline: none`), keyboard operability,
   `aria-*` correctness, and contrast encoded in Tailwind/theme tokens. Map to WCAG 2.2 AA.
7. Write outputs once findings are grounded — do not exhaustively read every file.

## Standards
OWASP Top 10 (2021) and Supabase RLS/security guidance; GDPR principles (data minimization,
storage limitation, DSAR, lawful basis); WCAG 2.2 AA and WAI-ARIA Authoring Practices.

## Output
Follow the output templates in `templates/`.
1. write_analysis("lovable-readiness", <markdown grouped into Security / Scalability / GDPR /
   Accessibility sections, each finding citing evidence path:line>)
2. write_tasks("lovable-readiness", { ...validates against templates/tasks.schema.json... })
   Use task id prefix `LOVE-`. Always cite evidence as repos/<name>/<path>:<line>.

## Constraints
Repos are read-only. Prefer scoped `grep_repo` over reading whole files; only `read_file`
specific suspect files. A `service_role` key or secret reachable from client code, and any
table without RLS, are high severity. This is not legal advice — frame GDPR findings as
engineering risks. Use web_search/web_fetch only to confirm CVE/standard details, saving any
fetched material under research/ with the provenance header.
