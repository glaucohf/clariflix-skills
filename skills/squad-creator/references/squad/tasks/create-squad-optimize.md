# Task: Optimize Squad Workflows Post-Creation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-optimize` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-squad-optimize
name: "Optimize Squad Workflows"
category: squad-creation
agent: squad-chief
elicit: false
autonomous: true
description: "Run determinism analysis and optimization pass on all squad workflows after creation, before validation."
```

## Purpose

Scan all workflows in the newly created squad for non-deterministic patterns, missing task_refs, ambiguous transitions, and optimization opportunities. Apply fixes automatically where possible, then re-validate workflow contracts to confirm compliance.

## Prerequisites

- [ ] `create-squad-integrate` completed (all components wired)
- [ ] Squad workflows exist at `squads/{squad_slug}/workflows/*.yaml`
- [ ] Workflow contract schema available for re-validation

## Inputs

```yaml
inputs:
  squad_slug:
    type: string
    required: true
    description: "Slug of the squad being optimized"
  workflows_path:
    type: string
    required: true
    description: "Path to squad workflows directory"
    default: "squads/{squad_slug}/workflows/"
```

## Workflow / Steps

### Step 1: Scan Workflows for Issues

- Read all `*.yaml` files in `squads/{squad_slug}/workflows/`
- For each workflow, check:
  - Every phase has a `task_ref` pointing to an existing task file
  - All state transitions are reachable (no orphan states)
  - No ambiguous trigger names (unique per workflow)
  - `on_success` and `on_failure` handlers are defined where needed
- Produce `analysis-summary.yaml` with findings

### Step 2: Apply Deterministic Fixes

- For each issue found in Step 1:
  - Missing `task_ref`: flag as CRITICAL (cannot auto-fix without task)
  - Orphan states: flag as HIGH, suggest removal
  - Duplicate triggers: rename with suffix to disambiguate
  - Missing handlers: add default `on_failure: { trigger: fail }` where absent
- Log all changes applied

### Step 3: Generate Determinism Report

- Produce `determinism-analysis-report.md` with:
  - Summary of issues found
  - Fixes applied automatically
  - Remaining issues requiring manual intervention
  - Compliance score (0-10)

### Step 4: Re-validate Workflow Contracts

- Run contract validation on all modified workflows
- Confirm all workflows pass after optimization
- If any fail, log failures and flag for fix_cycle

## Output

```yaml
outputs:
  analysis_summary:
    path: ".aiox/squad-runtime/optimize/{squad_slug}/analysis-summary.yaml"
    description: "Structured findings from workflow scan"
  determinism_report:
    path: ".aiox/squad-runtime/optimize/{squad_slug}/determinism-analysis-report.md"
    description: "Human-readable optimization report"
```

## Acceptance Criteria

- [ ] All workflows in squad scanned for determinism issues
- [ ] Auto-fixable issues applied without breaking existing contracts
- [ ] Determinism report generated with compliance score
- [ ] Re-validation confirms all workflows pass contracts
- [ ] CRITICAL issues (missing task_refs) are flagged, not silently skipped

## Veto Conditions

- **VETO if** optimization introduces breaking changes to workflow contracts
- **VETO if** auto-fix removes phases or transitions without explicit approval
- **VETO if** compliance score is below 6.0 and no issues are flagged

## Related Documents

- `squads/squad-creator/workflows/create-squad.yaml` (optimization phase)
- `squads/squad-creator/tasks/create-squad-validate.md` (downstream validation)
- `squads/squad-creator/tasks/create-workflow-task-refs.md` (task_ref resolution)
