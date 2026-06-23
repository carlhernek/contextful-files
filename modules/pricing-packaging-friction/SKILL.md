# Pricing & Packaging Friction

## Scope
Examine how pricing, plans, tiers, quotas, and entitlements are implemented in code, and
identify friction or risk: hardcoded limits, unclear tier gating, missing upgrade paths,
inconsistent entitlement checks, and billing edge cases. Most relevant to B2B.

## Inputs
- repos/: billing/subscription code, plan/tier definitions, feature-flag/entitlement checks,
  quota enforcement, pricing pages/config.
- meta/: pricing model, packaging strategy, or commercial requirements if provided.
- project_type relevance: b2b (primary); for "both", still review consumer plans.

## Method
1. Call `gather_context` on each relevant repo first.
2. Locate where plans/tiers/entitlements are defined and enforced (`grep_repo` with a source glob).
3. Check consistency: is every gated feature checked the same way? Any bypasses?
4. Identify friction: no self-serve upgrade, hardcoded limits, unclear proration/trial logic.
5. Write outputs once packaging patterns are clear.
4. Flag commercial risk: entitlement checks that fail open, missing quota enforcement.

## Standards
SaaS packaging patterns (good/better/best, usage-based), entitlement-check consistency.

## Output
Follow the output templates in `templates/`.
1. write_analysis("pricing-packaging-friction", <markdown: entitlement map + friction points>)
2. write_tasks("pricing-packaging-friction", { ... }) — task id prefix `PRICE-`.

## Constraints
Repos are read-only. Treat fail-open entitlement checks as high severity. Cite the enforcement
code for each finding.
