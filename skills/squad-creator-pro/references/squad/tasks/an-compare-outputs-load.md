---
task-id: an-compare-outputs-load
name: "Load Inputs & Extract Comparable Items"
version: 1.0.0
execution_type: Agent
model: Opus
model_rationale: "Opus REQUIRED for evaluator independence."
haiku_eligible: false
estimated-time: 5 min
complexity: low

inputs:
  required:
    - task_name: "Task being evaluated"
    - opus_baseline: "Path to Opus output file"
    - haiku_output: "Path to Haiku output file"
    - task_file: "Original task definition"

outputs:
  primary:
    - comparable_items: "Structured list of items, scores, tiers, checkpoints, recommendations"

elicit: false
---

# Task: Load Inputs & Extract Comparable Items

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-compare-outputs-load` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

- **Parent Task:** `an-compare-outputs` (orchestrator stub)
- **Sequence:** Phase 1 of 3
- **Previous Task:** None
- **Next Task:** `an-compare-outputs-score`

## Purpose

Load both output files and the task definition, validate structure, and extract all comparable items into a normalized format for scoring.

## Workflow / Steps

### Step 1: Load and Validate Inputs

```yaml
validation:
  - "Both files exist and are valid YAML"
  - "Both files have same structure"
  - "Task file provides context for evaluation"
```

### Step 2: Extract Comparable Items

```yaml
extract:
  items: "List of scored items (sources, dimensions, etc.)"
  scores: "Numerical scores per item"
  tiers: "Classification tiers per item"
  checkpoints: "Binary checkpoints if applicable"
  recommendations: "Action items and priorities"
```

### Step 3: Normalize for Comparison

Align items from both outputs so each can be compared 1:1:
- Match items by ID or name
- Note items present in one output but not the other
- Flag structural differences

## Output

```yaml
comparable_items:
  total_items: 0
  matched_items: 0
  unmatched_items: 0
  items:
    - id: ""
      opus_score: 0
      haiku_score: 0
      opus_tier: ""
      haiku_tier: ""
      opus_checkpoints: []
      haiku_checkpoints: []
  opus_recommendations: []
  haiku_recommendations: []
```

## Acceptance Criteria

- [ ] Both files loaded and parsed successfully
- [ ] All scored items extracted and aligned
- [ ] Structural differences noted
- [ ] Items normalized for 1:1 comparison

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-compare-outputs.md` | Parent orchestrator |
| `an-compare-outputs-score.md` | Next phase |
