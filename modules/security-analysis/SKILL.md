# Security Analysis

## Scope
Identify security flaws in the target repositories: injection, broken auth/session handling,
sensitive-data exposure, insecure deserialization, SSRF, misconfigured CORS/headers, secrets
in source, and unsafe dependencies surfaced in code. This module does NOT perform dynamic
scanning, fuzzing, or live penetration testing — analysis is static, from source only.

## Inputs
- repos/: application source, especially request handlers, auth/session code, input parsing,
  templating/rendering, file/network IO, and config (`.env*`, CI secrets references).
- meta/: security requirements, threat models, or compliance docs if provided.
- project_type relevance: both (auth and data-handling risks apply to b2c and b2b).

## Method
1. Map entry points: HTTP routes, CLI args, message consumers, file uploads.
2. Trace untrusted input to sinks (DB, shell, filesystem, templating, redirects).
3. Use `grep_repo` for risky patterns: `eval(`, `exec(`, `child_process`, `os.system`,
   `pickle.loads`, raw SQL string concatenation, `dangerouslySetInnerHTML`, `verify=False`,
   hardcoded tokens/keys, `Access-Control-Allow-Origin: *`.
4. Review auth: password storage, session/cookie flags, JWT validation, authz checks per route.
5. Check config and headers (CSP, HSTS, secure cookies) and secret management.
6. Map each finding to OWASP Top 10 (2021) and assign severity.

## Standards
OWASP Top 10 (2021), OWASP ASVS where relevant, CWE references for specific weaknesses.

## Output
Follow the output templates in `templates/` (synced from contextful-files).
1. write_analysis("security-analysis", <markdown following templates/analysis.md>)
2. write_tasks("security-analysis", { ...validates against templates/tasks.schema.json... })
   Use task id prefix `SEC-`. Always cite evidence as repos/<name>/<path>:<line>.

## Constraints
Repos are read-only. Do not run modules other than this one. Prefer `grep_repo` over reading
whole files; only `read_file` specific suspect files. Use web_search/web_fetch only to confirm
CVE/standard details, and save any fetched material under research/ with the provenance header.
