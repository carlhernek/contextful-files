# contextful-files

The versioned content repository for [Contextful](../spec/contextful-spec.md). The desktop app
(`contextful-gui`) clones this repo once and materializes it per project via git worktrees.

This repo is agent-facing content (markdown / JSON / helper scripts) — no application code.
Non-engineers can edit and review modules here.

## Layout

```
agents/                        # generalized agent instruction docs (synced to every project)
  workspace-orchestrator.md    # global policy layer (prepended to all agent prompts)
  project-orchestrator.md      # per-project Q&A coordinator role
  module-agent.md              # per-module analysis agent behavior
modules/
  template-version.txt         # semver, bumped on any SKILL.md/template/agent change
  module-config.json           # per-module runtime limits (maxTurns, etc.)
  module-config.schema.json    # JSON Schema for module-config.json
  <module-id>/SKILL.md         # one folder per analysis module
templates/                     # OUTPUT templates the agents fill in
  analysis.md                  # raw analysis document skeleton
  tasks.schema.json            # kanban tasks JSON schema
  run-summary.md               # per-run rollup skeleton
scripts/                       # optional helper .py scripts (run_script targets)
```

## Agent instruction layers

System prompts are composed at runtime:

- **Module Agent** = `workspace-orchestrator.md` + `module-agent.md` + runtime context + `modules/<id>/SKILL.md`
- **Project Orchestrator** = `workspace-orchestrator.md` + `project-orchestrator.md` + project context

Docs are generalized (not per-project). The sidecar injects workspace-specific facts (repos, project type, tools, run state).

## Releasing changes

Bump `modules/template-version.txt` (semver) whenever any `SKILL.md`, output template, `agents/` doc,
or `module-config.json` changes, then push to `main`. Users pull the update in-app via "Update modules" — no new
app build required.

## Modules & packs

| # | Module | Pack(s) |
|---|--------|---------|
| 1 | Security Analysis | Engineering, Compliance & Risk |
| 2 | SWOT Analysis | Sales & Growth |
| 3 | Accessibility Pass | Engineering, Onboarding & Docs |
| 4 | B2B Low-hanging Features | Sales & Growth |
| 5 | B2C Campaign Ideas | Sales & Growth |
| 6 | Dependency Health | Engineering |
| 7 | CI/CD Pipeline Audit | Engineering |
| 8 | API Surface Analysis | Engineering |
| 9 | Tech Debt Triage | Engineering |
| 10 | Onboarding Flow Audit | Onboarding & Docs |
| 11 | Documentation Gap Analysis | Onboarding & Docs |
| 12 | Pricing & Packaging Friction | Sales & Growth |
| 13 | Localization Readiness | Sales & Growth |
| 14 | Data Privacy Scan | Compliance & Risk |
| 15 | Licensing Compatibility | Compliance & Risk |
| 16 | Workspace Index | *(infrastructure — opt-in, agentic per-item indexer; not in packs)* |
| 17 | Test Coverage | Engineering |

Packs: Engineering (1,3,6,7,8,9,17), Sales & Growth (2,4,5,12,13),
Onboarding & Docs (3,10,11), Compliance & Risk (1,14,15).
