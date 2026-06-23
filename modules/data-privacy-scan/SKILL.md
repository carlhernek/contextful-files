# Data Privacy Scan

## Scope
Identify personal-data (PII) handling and privacy-compliance gaps: what PII is collected,
where it flows, how it's stored/logged, consent and retention handling, third-party data
sharing, and data-subject-rights support (access/deletion). Static, source-based review.

## Inputs
- repos/: data models/schemas, logging code, analytics/tracking integrations, cookie/consent
  code, export/delete endpoints, privacy policy text if in repo.
- meta/: privacy policy, DPA, or compliance requirements if provided.
- project_type relevance: both.

## Method
1. Call `gather_context` on each relevant repo first.
2. Inventory PII fields in models/schemas (`grep_repo` with `glob: "*.{ts,cs,java,py}"` for email, phone, address, dob, ssn, payment data — do not grep lockfiles or whole-repo without a glob).
3. Trace PII into logs and analytics — flag PII written to logs or third parties.
4. Check consent mechanisms (cookies/tracking) and retention/deletion handling.
5. Assess data-subject-rights support (export, deletion) and lawful-basis hooks.
6. Map findings to relevant principles (GDPR/CCPA) and assign severity.
7. Write outputs once you have a solid PII inventory and top gaps — avoid re-reading every shared component.

## Standards
GDPR principles (data minimization, purpose limitation, storage limitation, DSAR), CCPA/CPRA.

## Output
Follow the output templates in `templates/`.
1. write_analysis("data-privacy-scan", <markdown: PII inventory + flow + gaps>)
2. write_tasks("data-privacy-scan", { ... }) — task id prefix `PRIV-`.

## Constraints
Repos are read-only. PII in logs or sent to third parties without consent is high severity.
This is not legal advice — frame findings as engineering risks. Cite evidence path:line.
