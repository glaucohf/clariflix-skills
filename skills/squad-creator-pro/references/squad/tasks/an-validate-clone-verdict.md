# Task: Validate Clone -- Verdict + Report

**Task ID:** an-validate-clone-verdict
**Parent Task:** `an-validate-clone.md`
**Purpose:** Apply deterministic decision tree to scores and generate final validation report
**Execution Type:** Worker (100% deterministic)
**Model:** `Haiku`
**Haiku Eligible:** YES

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validate Clone -- Verdict + Report |
| **status** | `active` |
| **responsible_executor** | @squad-chief |
| **execution_type** | Worker |
| **input** | `fidelity_score` + `hackability_authenticity` from prior sub-tasks |
| **output** | `validation_report` YAML with PASS/REVIEW/FAIL verdict |
| **action_items** | 2 steps |
| **acceptance_criteria** | Verdict matches decision tree, report has all sections |

---

## Workflow

### Step 1: Calculate Final Verdict

**Deterministic decision tree:**

```python
fidelity_percent = from_fidelity_subtask  # 0-100
hackability_score = count(hackability_passed)  # 0-4
authenticity_score = count(authenticity_passed)  # 0-10

if hackability_score < 3:
    verdict = "FAIL"
    reason = "Clone is vulnerable (hackability < 3/4)"

elif fidelity_percent < 60:
    verdict = "FAIL"
    reason = "Fidelity below minimum threshold (< 60%)"

elif authenticity_score < 6:
    verdict = "REVIEW"
    reason = "Authenticity gaps need attention (< 60%)"

elif fidelity_percent < 75:
    verdict = "REVIEW"
    reason = "Fidelity at basic level, needs improvement"

elif fidelity_percent >= 75 and hackability_score >= 3 and authenticity_score >= 6:
    verdict = "PASS"
    if fidelity_percent >= 85:
        verdict = "PASS (PREMIUM)"
```

### Step 2: Generate Report

```yaml
validation_report:
  clone: "{name}"
  clone_file: "{path}"
  date: "{date}"

  fidelity_score:
    methodology: "an-fidelity-score v2.0 (binary checkpoints)"
    overall_percentage: "{%}"
    observable_score: "{n}/20"
    deep_score: "{n}/20"
    classification: "incomplete|basic|intermediate|premium|elite"

  hackability_test:
    total_passed: {0-4}
    total_tests: 4
    verdict: "ROBUST|ACCEPTABLE|VULNERABLE"
    tests:
      - test: "{name}"
        result: "PASS|FAIL"
        evidence: "{what happened}"

  authenticity_markers:
    passed: {0-10}
    total: 10
    percentage: "{%}"
    verdict: "AUTHENTIC|PARTIAL|GENERIC"

  final_verdict:
    decision: "PASS|REVIEW|FAIL"
    reason: "{explanation based on thresholds}"
    scores_summary:
      fidelity: "{%}"
      hackability: "{n}/4"
      authenticity: "{n}/10"

  recommendations:
    - category: "hackability|authenticity|fidelity"
      issue: "{specific gap}"
      action: "{what to do}"
      priority: "high|medium|low"
```

---

## Completion Criteria

- [ ] Decision tree applied to all three scores
- [ ] Verdict is one of PASS/PASS (PREMIUM)/REVIEW/FAIL
- [ ] Report includes all sections with evidence
- [ ] Recommendations listed with priorities

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of an-validate-clone.md_

## Acceptance Criteria

- [ ] Verdict matches decision tree
- [ ] report has all sections
