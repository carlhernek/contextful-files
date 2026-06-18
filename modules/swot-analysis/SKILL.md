# SWOT Analysis

## Scope
Produce a Strengths / Weaknesses / Opportunities / Threats analysis of the product implied by
the repositories, benchmarked against competitors via online research. This module assesses
product/market posture, not code quality (other modules cover that).

## Inputs
- repos/: feature surface, README/docs, public API, pricing/marketing pages if present.
- meta/: product specs, positioning docs, target-market notes.
- project_type relevance: both (frame strengths/threats per b2c or b2b emphasis).

## Method
1. Infer the product's core value proposition and feature set from repos and meta docs.
2. Use web_search/web_fetch to identify 2-5 comparable competitors and their differentiators.
   Save fetched pages under research/ with provenance headers.
3. Categorize internal factors (Strengths, Weaknesses) grounded in repo/meta evidence and
   external factors (Opportunities, Threats) grounded in research.
4. Convert the most actionable items into tasks (e.g. close a competitive gap, exploit an edge).

## Standards
Classic SWOT framing. Clearly separate evidence-based claims (cite repo/meta) from
research-based claims (cite research/ source URLs).

## Output
Follow the output templates in `templates/`.
1. write_analysis("swot-analysis", <markdown with Strengths/Weaknesses/Opportunities/Threats>)
2. write_tasks("swot-analysis", { ... }) — task id prefix `SWOT-`.

## Constraints
Repos are read-only. Online research is required; if web_fetch/web_search transiently fail,
retry (turns are refunded). Never present research/ content as original repo material.
