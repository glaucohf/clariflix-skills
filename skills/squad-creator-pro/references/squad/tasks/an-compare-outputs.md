---
task-id: an-compare-outputs
name: "Compare Model Outputs"
version: 2.0.0
execution_type: Orchestrator
model: Opus
model_rationale: "Orchestrator stub -- delegates to 3 atomic sub-tasks. Opus REQUIRED (evaluator independence)."
haiku_eligible: false
note: "Decomposed from v1.0.0 monolith (349 lines, 4 dimensions) into 3 atomic tasks."
estimated-time: 20-30 min
complexity: medium

inputs:
  required:
    - task_name: "Task being evaluated (e.g., an-assess-sources)"
    - opus_baseline: "Path to Opus output file"
    - haiku_output: "Path to Haiku output file"
    - task_file: "Original task definition (for reference)"

outputs:
  primary:
    - qualification_report: "Full qualification report with decision"

elicit: false
---

# Compare Model Outputs

**Command:** `*compare-outputs`

> **CRITICAL:** Evaluator Independence -- Opus ONLY. NEVER use Haiku to evaluate Haiku.

---

## Pipeline (3 Atomic Tasks)

| Phase | Task ID | Name | Est. Time |
|-------|---------|------|-----------|
| 1 | `an-compare-outputs-load` | Load Inputs & Extract Comparable Items | 5 min |
| 2 | `an-compare-outputs-score` | Score 4 Evaluation Dimensions | 10 min |
| 3 | `an-compare-outputs-report` | Generate Qualification Report | 5 min |

---

## Execution Flow

```
an-compare-outputs-load
  | comparable_items (items, scores, tiers, checkpoints, recommendations)
  v
an-compare-outputs-score
  | dimension_scores (tier_match, score_variance, checkpoint_match, recommendation_quality)
  v
an-compare-outputs-report
  | qualification_report (FINAL OUTPUT)
  v
[QUALIFIED | CONDITIONAL | NOT_QUALIFIED]
```

---

## Evaluator Rules

```yaml
evaluator_rules:
  model: "opus"
  blind_mode: false
  bias_mitigation:
    - "Score WHAT IS WRITTEN, not what you expect"
    - "Do NOT assume Opus is better - measure objectively"
    - "If outputs are equivalent, say so"
```

---

## Qualification Thresholds

| Decision | Criteria |
|----------|---------|
| QUALIFIED | >= 85 points AND no veto triggered |
| CONDITIONAL | 70-84 points OR veto with mitigation possible |
| NOT_QUALIFIED | < 70 points OR hard veto |

---

## Output

Save to: `squads/squad-creator-pro/test-cases/{task_name}/qualification-report.yaml`

---

## Completion Criteria

- [ ] Both output files loaded and parsed
- [ ] All 4 dimensions scored using rubric
- [ ] Veto conditions checked
- [ ] Total score calculated
- [ ] Decision determined (QUALIFIED/CONDITIONAL/NOT_QUALIFIED)
- [ ] Report saved to test-cases/{task}/qualification-report.yaml

## Task Anatomy

- **Executor:** Agent
- **Inputs:** task_name; opus_baseline; haiku_output; task_file
- **Outputs:** Full qualification report with decision
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] All veto conditions checked and none triggered
- [ ] Output artifact produced: Full qualification report with decision
- [ ] Task output validated against quality standards
