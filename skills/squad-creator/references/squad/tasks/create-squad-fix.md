# Task: Fix Validation Failures (Fix Cycle)

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-fix` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-squad-fix
name: "Fix Validation Failures"
category: squad-creation
agent: squad-chief
elicit: false
autonomous: true
description: "Read validation failures, apply targeted fixes, and re-validate. Max 3 iterations before escalation."
```

## Purpose

Remediate validation failures reported by `create-squad-validate`. Parse the validation report, classify each failure by severity, apply targeted fixes, and re-run validation. Repeat up to 3 iterations. If failures persist, log the fix cycle and escalate.

## Prerequisites

- [ ] `create-squad-validate` completed with failures
- [ ] Validation report exists at `.aiox/squad-runtime/create-squad/{squad_slug}/validation/validation-report.md`
- [ ] Squad files accessible at `squads/{squad_slug}/`

## Inputs

```yaml
inputs:
  squad_slug:
    type: string
    required: true
    description: "Slug of the squad being fixed"
  validation_report:
    type: file
    required: true
    path: ".aiox/squad-runtime/create-squad/{squad_slug}/validation/validation-report.md"
    description: "Validation report with categorized failures"
  max_iterations:
    type: integer
    required: false
    default: 3
    description: "Maximum fix-revalidate cycles before escalation"
```

## Workflow / Steps

### Step 1: Parse Validation Failures

- Read the validation report
- Extract each failure with: category, severity (CRITICAL/HIGH/MEDIUM/LOW), file path, description
- Sort by severity (CRITICAL first)
- Skip LOW severity items (document only)

### Step 2: Apply Targeted Fixes (per iteration)

- For each CRITICAL/HIGH failure:
  - Read the affected file
  - Identify the specific issue (missing field, broken reference, schema violation)
  - Apply the minimal fix that resolves the issue
  - Log the fix: what changed, why, which file
- For MEDIUM failures:
  - Attempt auto-fix if pattern is known
  - Otherwise document as technical debt

### Step 3: Re-validate

- Run the same validation pipeline from `create-squad-validate`
- Compare new results against previous iteration
- If all CRITICAL/HIGH resolved: mark fix cycle as SUCCESS
- If failures remain and iteration < max: return to Step 2
- If failures remain and iteration == max: proceed to Step 4

### Step 4: Generate Fix Cycle Log

- Produce `fix-cycle-log.md` with:
  - Iterations completed
  - Fixes applied per iteration
  - Remaining failures (if any)
  - Recommendation: SUCCESS or ESCALATE

## Output

```yaml
outputs:
  fix_cycle_log:
    path: ".aiox/squad-runtime/create-squad/{squad_slug}/validation/fix-cycle-log.md"
    description: "Complete log of fix cycle iterations and outcomes"
  fix_result:
    type: enum
    values: [SUCCESS, ESCALATE]
    description: "Whether all CRITICAL/HIGH issues were resolved"
```

## Acceptance Criteria

- [ ] All CRITICAL failures addressed within max iterations
- [ ] Each fix is minimal and targeted (no broad rewrites)
- [ ] Fix cycle log documents every change with rationale
- [ ] Re-validation runs after each fix iteration
- [ ] Escalation triggered cleanly when max iterations exhausted

## Veto Conditions

- **VETO if** a fix introduces new CRITICAL failures (regression)
- **VETO if** fixes modify files outside the squad directory without justification
- **VETO if** fix cycle exceeds max_iterations without escalation

## Related Documents

- `squads/squad-creator/tasks/create-squad-validate.md` (upstream validation)
- `squads/squad-creator/workflows/create-squad.yaml` (fix_cycle phase)
- `squads/squad-creator/checklists/squad-checklist.md` (validation criteria)
