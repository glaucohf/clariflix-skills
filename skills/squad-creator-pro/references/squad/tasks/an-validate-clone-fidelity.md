# Task: Validate Clone -- Fidelity Score

**Task ID:** an-validate-clone-fidelity
**Parent Task:** `an-validate-clone.md`
**Purpose:** Calculate fidelity score using an-fidelity-score v2.0 methodology (8 layers x 5 binary checkpoints)
**Execution Type:** Hybrid (Worker script 90%)
**Model:** `Haiku`
**Haiku Eligible:** YES

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validate Clone -- Fidelity Score |
| **status** | `active` |
| **responsible_executor** | @squad-chief |
| **execution_type** | Hybrid |
| **input** | Clone file path + preflight YAML |
| **output** | Fidelity percentage with layer breakdown |
| **action_items** | 2 steps |
| **acceptance_criteria** | 40 checkpoints scored, weighted formula applied |

---

## Workflow

### Step 1: Score 8 Layers (5 Binary Checkpoints Each)

**Use the exact methodology from `tasks/an-fidelity-score.md` v2.0**

- 8 layers x 5 binary checkpoints each = 40 total checkpoints
- Observable layers (L1-L4) weighted 0.8
- Deep layers (L5-L8) weighted 1.0

Layers:

- L1: Behavioral Patterns
- L2: Communication Style
- L3: Decision Making
- L4: Emotional Responses
- L5: Core Values
- L6: Mental Models
- L7: Identity Markers
- L8: Paradoxes and Contradictions

### Step 2: Calculate Weighted Score

```python
observable_raw = sum(L1_score, L2_score, L3_score, L4_score)  # 0-20
deep_raw = sum(L5_score, L6_score, L7_score, L8_score)         # 0-20

fidelity_percent = ((observable_raw * 0.8) + (deep_raw * 1.0)) / 36 * 100

classification:
  if fidelity_percent < 40: "incomplete"
  elif fidelity_percent < 60: "basic"
  elif fidelity_percent < 75: "intermediate"
  elif fidelity_percent < 85: "premium"
  else: "elite"
```

---

## Output Contract

```yaml
fidelity_score:
  methodology: "an-fidelity-score v2.0 (binary checkpoints)"
  overall_percentage: "{%}"
  observable_score: "{n}/20"
  deep_score: "{n}/20"
  classification: "incomplete|basic|intermediate|premium|elite"
  layers:
    - layer: "L1: Behavioral Patterns"
      score: {0-5}
      checkpoints_passed: []
    - layer: "L2: Communication Style"
      score: {0-5}
      checkpoints_passed: []
    # ... all 8 layers
```

---

## Completion Criteria

- [ ] All 40 checkpoints scored (8 layers x 5 each)
- [ ] Observable vs deep weighting applied
- [ ] Classification assigned
- [ ] Layer breakdown documented

---

## Handoff

| Attribute | Value |
|-----------|-------|
| **Next Task** | `an-validate-clone-hackability.md` |
| **Trigger** | Fidelity score complete |
| **Artifact** | `fidelity_score` YAML |

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of an-validate-clone.md_

## Acceptance Criteria

- [ ] 40 checkpoints scored
- [ ] weighted formula applied
