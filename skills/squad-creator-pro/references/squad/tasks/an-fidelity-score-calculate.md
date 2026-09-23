---
task-id: an-fidelity-score-calculate
name: "Calculate Score, Classify & Report"
version: 1.0.0
execution_type: Hybrid
model: Haiku
model_rationale: "Score calculation is deterministic. LLM only synthesizes recommendations (5%)."
haiku_eligible: true
estimated-time: 5 min
complexity: low

inputs:
  required:
    - layer_scores: "8 layers with checkpoint details from Phase 2"
    - clone_files: "File map from Phase 1"

outputs:
  primary:
    - fidelity_report: "Complete report with scores, classification, gaps, and trajectory"

elicit: false
---

# Task: Calculate Score, Classify & Report

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-fidelity-score-calculate` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

- **Parent Task:** `an-fidelity-score` (orchestrator stub)
- **Sequence:** Phase 3 of 3
- **Previous Task:** `an-fidelity-score-layers`
- **Next Task:** None (final phase)

## Purpose

Apply the deterministic weighted scoring formula, classify the clone version, identify gaps with specific remediation, and generate the full fidelity report.

## Workflow / Steps

### Step 1: Calculate Weighted Score

```python
# Observable layers (weight 0.8)
L1 = behavioral_patterns_score  # 0-5
L2 = communication_style_score  # 0-5
L3 = routines_habits_score      # 0-5
L4 = recognition_patterns_score # 0-5

# Deep layers (weight 1.0)
L5 = mental_models_score        # 0-5
L6 = values_hierarchy_score     # 0-5
L7 = core_obsessions_score      # 0-5
L8 = productive_paradoxes_score # 0-5

observable_raw = (L1 + L2 + L3 + L4)       # max 20
observable_weighted = observable_raw * 0.8   # max 16

deep_raw = (L5 + L6 + L7 + L8)             # max 20
deep_weighted = deep_raw * 1.0              # max 20

total_weighted = observable_weighted + deep_weighted  # max 36
percentage = (total_weighted / 36) * 100
```

### Step 2: Classify (Deterministic)

| Percentage | Classification | Version |
|------------|----------------|---------|
| 0-59% | Incomplete | V0.x |
| 60-74% | Basic | V1.0 |
| 75-84% | Intermediate | V2.0 |
| 85-92% | Premium | V3.0 |
| 93-100% | Elite | V3.5+ |

### Step 3: Identify Gaps

For each layer with score < 4:
- Which checkpoint failed
- Where to add (file section)
- Example of what it should look like

### Step 4: Generate Report (LLM: synthesize recommendations)

```yaml
fidelity_report:
  clone: "{name}"
  clone_file: "{path}"
  date: "{ISO date}"
  scores:
    observable:
      behavioral_patterns: { score, passed, failed }
      communication_style: { score, passed, failed }
      routines_habits: { score, passed, failed }
      recognition_patterns: { score, passed, failed }
      subtotal_raw: 0
      subtotal_weighted: 0
    deep:
      mental_models: { score, passed, failed }
      values_hierarchy: { score, passed, failed }
      core_obsessions: { score, passed, failed }
      productive_paradoxes: { score, passed, failed }
      subtotal_raw: 0
      subtotal_weighted: 0
    overall:
      total_weighted: 0
      max_possible: 36
      percentage: "0%"
      classification: ""
      version: "V0.0"
  gaps:
    - layer: ""
      checkpoint_failed: 0
      checkpoint_name: ""
      what_to_add: ""
      where_to_add: ""
      example: ""
  trajectory:
    current_version: ""
    next_milestone: ""
    gaps_to_close: 0
    estimated_effort: ""
```

## Output

```yaml
fidelity_report: { complete report as above }
```

## Acceptance Criteria

- [ ] Weighted score calculated with formula
- [ ] Classification assigned deterministically
- [ ] Gaps listed with specific remediation
- [ ] Report YAML generated in specified format
- [ ] Trajectory to next milestone documented

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-fidelity-score.md` | Parent orchestrator |
| `an-fidelity-score-layers.md` | Previous phase |
| `checklists/mind-validation.md` | Validation checklist |
