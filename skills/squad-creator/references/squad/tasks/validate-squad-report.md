# Task: Validate Squad — Report

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-report` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-report
name: "Validate Squad Report"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Emit backward-compatible JSON and human-readable validation report."
```

## Purpose

Generate the final validation report in two formats: a backward-compatible JSON payload preserving existing contract fields, and a human-readable markdown report. The report adapts its depth based on whether quick mode or deep review mode was used.

## Prerequisites

- [ ] Reconciliation completed (`validate-squad-reconcile`)
- [ ] Veto check completed (`validate-squad-veto`)

## Inputs

```yaml
inputs:
  squad_name:
    type: string
    required: true
  squad_path:
    type: string
    required: false
    default: "squads/{squad_name}/"
  reconciled_data:
    type: object
    required: true
    description: "Output from validate-squad-reconcile"
  veto_result:
    type: object
    required: true
    description: "Output from validate-squad-veto"
  detected_type:
    type: string
    required: true
  mode:
    type: string
    required: true
    description: "deep | quick"
```

## Workflow / Steps

### Step 1: Construct Report Structure

```yaml
report_structure:
  header:
    squad_name: "{name}"
    squad_type: "{detected_type}"
    version: "{version from config.yaml}"
    validation_date: "{ISO date}"
    validator: "Squad Architect v5.0"
    mode: "deep | quick"

  executive_summary:
    final_score: "X.X/10"
    result: "EXCELLENT | PASS | CONDITIONAL | FAIL"
    type_detected: "Expert | Pipeline | Hybrid"
    key_strengths: [...]
    key_issues: [...]

  tier_results:
    tier_1_structure:
      status: "PASS | ABORT"
      checks: "X/Y"
      blocking_issues: []
    tier_2_coverage:
      status: "PASS | ABORT"
      metrics:
        checklist_coverage: "X%"
        orphan_tasks: N
        data_usage: "X%"
    tier_3_quality:  # Only in deep mode
      score: "X.X/10"
      breakdown:
        prompt_quality: "X.X (25%)"
        pipeline_coherence: "X.X (25%)"
        checklist_actionability: "X.X (25%)"
        documentation: "X.X (25%)"
    tier_4_contextual:  # Only in deep mode
      type: "Expert | Pipeline | Hybrid"
      score: "X.X/10"
      breakdown: {...}

  veto_status:
    triggered: "None | VXX"
    message: "..."

  issues_by_priority:
    critical: [{ issue, component, fix }]
    high: [{ issue, fix }]
    medium: [{ issue, fix }]

  optimization_section:
    convertible_tasks: N
    potential_savings: "~$X/month"
    note: "Run *optimize for detailed analysis (if pro available)"

  recommendations:
    immediate: [...]
    short_term: [...]

  sign_off:
    validator: "Squad Architect"
    date: "{date}"
    final_score: "X.X/10"
    result: "PASS | CONDITIONAL | FAIL"
```

### Step 2: Emit JSON (backward-compatible)

Preserve existing contract fields:

- `final_score` -- numeric 0.0-10.0
- `deterministic` -- object with structure/security/coverage results
- `workflow_contracts` -- workflow validation details
- `production` -- production maturity evidence
- `claude_analysis` -- semantic review results (null if quick mode)

New dimensions added by extension only, never by replacement.

### Step 3: Emit Human-Readable Report

**Quick mode:** Compact report with score, blocking issues, and top recommendations.

**Deep mode:** Full dimensional report with all tier breakdowns, contextual analysis, optimization opportunities, and prioritized issue list.

### Step 4: Write Report File

Output location: `{squad_path}/docs/validation-report-{date}.md`

Also output summary to console.

## Output

```yaml
output:
  files:
    report: "{squad_path}/docs/validation-report-{date}.md"
    json: "{squad_path}/docs/validation-report-{date}.json"
  console:
    summary: "Quick pass/fail with score"
  schema:
    json_contract:
      final_score: N
      result: "PASS | CONDITIONAL | FAIL"
      deterministic: {...}
      workflow_contracts: {...}
      production: {...}
      claude_analysis: {...}
```

## Acceptance Criteria

- [ ] JSON output preserves all backward-compatible fields
- [ ] Human-readable report generated at correct location
- [ ] Quick mode produces compact report; deep mode produces full report
- [ ] Score and result match reconciliation output
- [ ] Veto status accurately reflected
- [ ] Issues prioritized by severity (critical > high > medium)
- [ ] Console summary printed for immediate feedback

## Veto Conditions

- Reconciled data missing -> cannot generate report (task fails gracefully)
- Veto result missing -> cannot determine final status

## Related Documents

- `validate-squad.md` (parent composed task)
- `validate-squad-reconcile.md` (provides scores and data)
- `validate-squad-veto.md` (provides veto status)
- `data/quality-dimensions-framework.md`
