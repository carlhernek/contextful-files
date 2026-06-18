# Licensing Compatibility

## Scope
Review open-source license compatibility: the project's own license vs the licenses of its
dependencies, flagging conflicts (e.g. GPL/AGPL copyleft in a permissively licensed product),
missing attributions, and unknown/unlicensed dependencies. Source/manifest review only.

## Inputs
- repos/: `LICENSE*`, dependency manifests/lockfiles, `NOTICE`/attribution files, vendored code.
- meta/: licensing policy or distribution model (SaaS vs distributed) if provided.
- project_type relevance: both.

## Method
1. Determine the project's own license.
2. Enumerate dependencies from manifests; determine each dependency's license (use web_fetch to
   confirm where unclear; save to research/ with provenance).
3. Flag conflicts considering the distribution model (copyleft obligations differ for SaaS vs
   distributed binaries; AGPL triggers even for network use).
4. Identify missing attributions/NOTICE entries and unknown-license packages.

## Standards
SPDX license identifiers, OSI license categories (permissive / weak-copyleft / strong-copyleft),
copyleft obligations by distribution mode.

## Output
Follow the output templates in `templates/`.
1. write_analysis("licensing-compatibility", <markdown: license inventory + conflict matrix>)
2. write_tasks("licensing-compatibility", { ... }) — task id prefix `LIC-`.

## Constraints
Repos are read-only. Not legal advice — frame as compliance risk. Use SPDX identifiers; verify
ambiguous licenses via research before asserting a conflict.
