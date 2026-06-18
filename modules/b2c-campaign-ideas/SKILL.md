# B2C Campaign Ideas

## Scope
Generate marketing campaign ideas for consumer (B2C) growth, grounded in the product's actual
features and differentiators as found in the repos. Output is marketing strategy, not code
changes — but each idea should reference a real, shippable capability.

## Inputs
- repos/: user-facing features, onboarding flows, sharing/referral hooks, notifications.
- meta/: brand/positioning docs, target-audience notes if provided.
- project_type relevance: b2c (most relevant); for "both", complement the B2B module.

## Method
1. Identify the product's consumer-facing hooks (features that delight, share, or retain).
2. Optionally use web_search to ground ideas in current channel/format trends (save research/).
3. Propose campaigns: channel, message, hook feature, and a rough success metric.
4. Turn the most promising campaigns into tasks (e.g. instrument a referral event, add a share CTA).

## Standards
Standard growth-marketing framing (acquisition, activation, retention, referral, revenue).

## Output
Follow the output templates in `templates/`.
1. write_analysis("b2c-campaign-ideas", <markdown: campaigns with channel/message/hook/metric>)
2. write_tasks("b2c-campaign-ideas", { ... }) — task id prefix `B2C-`.

## Constraints
Repos are read-only. Tie each campaign to a real feature in the code. Mark any required code
instrumentation as its own task with an agentic_spec.
