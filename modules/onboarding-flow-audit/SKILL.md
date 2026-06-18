# Onboarding Flow Audit

## Scope
Evaluate the new-user onboarding experience for friction: signup/login flows, first-run
experience, empty states, required steps, error messaging, and time-to-first-value. Static
review of the relevant UI/flow source and any onboarding copy.

## Inputs
- repos/: auth/signup screens, onboarding wizards, empty-state components, default content,
  email/notification templates tied to activation.
- meta/: onboarding goals, funnel metrics, or UX research if provided.
- project_type relevance: both (b2c self-serve and b2b team setup both matter).

## Method
1. Trace the path from landing to first meaningful action in the code.
2. Identify friction: excessive required fields, unclear errors, dead ends, missing guidance,
   no progress indication, forced steps before value.
3. Evaluate empty states and defaults: do they teach and guide?
4. Recommend specific UX improvements mapped to the components involved.

## Standards
Activation/time-to-value heuristics, Nielsen usability heuristics, progressive disclosure.

## Output
Follow the output templates in `templates/`.
1. write_analysis("onboarding-flow-audit", <markdown: step-by-step friction map>)
2. write_tasks("onboarding-flow-audit", { ... }) — task id prefix `ONB-`.

## Constraints
Repos are read-only. Note where a finding requires live usability testing to confirm.
Cite the component/route for each friction point.
