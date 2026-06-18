# Localization Readiness

## Scope
Assess how ready the product is for internationalization and localization: i18n framework
usage, externalized strings, locale-aware formatting (dates/numbers/currency), pluralization,
RTL support, and locale routing. Static review from source.

## Inputs
- repos/: i18n config and message catalogs, UI components with user-facing text, date/number
  formatting code, CSS for layout direction.
- meta/: target locales/markets if provided.
- project_type relevance: both (market expansion concern).

## Method
1. Detect i18n framework (or its absence) via `grep_repo` (e.g. i18next, react-intl, gettext).
2. Find hardcoded user-facing strings that bypass the catalog.
3. Check locale-aware formatting for dates, numbers, and currency.
4. Assess RTL readiness: logical CSS properties vs physical (left/right), `dir` handling.
5. Check pluralization and locale-routing/detection.

## Standards
Unicode CLDR concepts, BCP 47 locale tags, WCAG language-of-page, CSS logical properties.

## Output
Follow the output templates in `templates/`.
1. write_analysis("localization-readiness", <markdown: readiness scorecard + gaps>)
2. write_tasks("localization-readiness", { ... }) — task id prefix `L10N-`.

## Constraints
Repos are read-only. Cite representative hardcoded-string locations rather than every instance.
