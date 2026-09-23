---
task-id: an-compare-outputs-report
name: "Generate Qualification Report"
version: 1.0.0
execution_type: Agent
model: Opus
model_rationale: "Opus REQUIRED for evaluator independence. Rationale writing requires judgment."
haiku_eligible: false
estimated-time: 5 min
complexity: low

inputs:
  required:
    - task_name: "Task being evaluated"
    - dimension_scores: "Scores from Phase 2"
    - comparable_items: "Items from Phase 1"

outputs:
  primary:
    - qualification_report: "Complete report with decision and rationale"

elicit: false
---

# Task: Generate Qualification Report

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-compare-outputs-report` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

- **Parent Task:** `an-compare-outputs` (orchestrator stub)
- **Sequence:** Phase 3 of 3
- **Previous Task:** `an-compare-outputs-score`
- **Next Task:** None (final phase)

## Purpose

Determine qualification decision, write rationale, generate recommendations, and save the complete report.

## Workflow / Steps

### Step 1: Determine Decision

```yaml
thresholds:
  QUALIFIED: ">= 85 points AND no veto triggered"
  CONDITIONAL: "70-84 points OR veto with mitigation possible"
  NOT_QUALIFIED: "< 70 points OR hard veto"
```

### Step 2: Write Rationale

Explain the decision based on dimension scores and veto status. Focus on actionable outcomes.

### Step 3: Generate Recommendations

```yaml
recommendations:
  if_qualified:
    - "Update model-routing.yaml: tier = haiku"
    - "Add validated: true with test_date"
  if_conditional:
    - "{Specific fixes needed}"
    - "Re-test after fixes"
  if_not_qualified:
    - "Keep tier = opus"
    - "Document root cause"
```

### Step 4: Assemble Report

```yaml
qualification_report:
  task: "{task_name}"
  evaluation_date: "{ISO date}"
  evaluator: "opus"
  inputs:
    opus_baseline: "{path}"
    haiku_output: "{path}"
  dimension_scores:
    tier_match: { score, match_rate, details }
    score_variance: { score, avg_variance, max_variance, details }
    checkpoint_match: { score, match_rate, details }
    recommendation_quality: { score, assessment, details }
  total_score: "X/100"
  veto_conditions:
    triggered: [...]
    not_triggered: [...]
  decision: "QUALIFIED | CONDITIONAL | NOT_QUALIFIED"
  rationale: "{explanation}"
  recommendations: [...]
```

### Step 5: Save Report

```
squads/squad-creator-pro/test-cases/{task_name}/qualification-report.yaml
```

## Output

```yaml
qualification_report: { complete report }
report_path: "squads/squad-creator-pro/test-cases/{task_name}/qualification-report.yaml"
```

## Acceptance Criteria

- [ ] Decision determined using thresholds
- [ ] Rationale explains the decision
- [ ] Recommendations are actionable
- [ ] Report saved to correct path
- [ ] Report includes all dimension details

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-compare-outputs.md` | Parent orchestrator |
| `an-compare-outputs-score.md` | Previous phase |
