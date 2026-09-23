---
task-id: an-fidelity-score-layers
name: "Execute 8 Layer Checklists"
version: 1.0.0
execution_type: Worker
model: Haiku
model_rationale: "Binary checkpoint evaluation (section exists? grep match?). 95% deterministic."
haiku_eligible: true
estimated-time: 5 min
complexity: low

inputs:
  required:
    - clone_files: "File map from Phase 1"
    - preflight_scores: "Script scores from Phase 1"

outputs:
  primary:
    - layer_scores: "8 layers x 5 checkpoints each with PASS/FAIL"

elicit: false
---

# Task: Execute 8 Layer Checklists

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-fidelity-score-layers` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

- **Parent Task:** `an-fidelity-score` (orchestrator stub)
- **Sequence:** Phase 2 of 3
- **Previous Task:** `an-fidelity-score-identify`
- **Next Task:** `an-fidelity-score-calculate`

## Purpose

Use preflight scores from the worker script to validate each layer's 5 checkpoints. The script already scored all 8 layers -- this task verifies and formats the results.

## Workflow / Steps

### Step 1: Validate Preflight Scores Against Checklists

For each of the 8 layers, confirm the script's checkpoint results:

**Layer 1: Behavioral Patterns** (Observable, weight 0.8)
- Where: `persona:`, `behavioral_patterns:`, `modes:`, `states:`
- Checkpoints: greeting ritual, response structure, modes/states, trigger responses, anti-patterns

**Layer 2: Communication Style** (Observable, weight 0.8)
- Where: `voice_dna:`, `vocabulary:`, `writing_style:`
- Checkpoints: signature phrases (3+), vocabulary always, vocabulary never, sentence structure, metaphors

**Layer 3: Routines & Habits** (Observable, weight 0.8)
- Where: `workflow:`, `steps:`, `ritual:`, `process:`
- Checkpoints: opening ritual, workflow steps, checkpoint habit, closing ritual, error handling

**Layer 4: Recognition Patterns** (Observable, weight 0.8)
- Where: `heuristics:`, `red_flags:`, `patterns:`, `recognition:`
- Checkpoints: red flags, green flags, decision rules, pattern IDs, thresholds

**Layer 5: Mental Models** (Cognitive, weight 1.0)
- Where: `thinking_dna:`, `frameworks:`, `mental_models:`
- Checkpoints: primary framework, decision architecture, named frameworks (3+), framework steps, anti-patterns

**Layer 6: Values Hierarchy** (Deep, weight 1.0)
- Where: `core_beliefs:`, `values:`, `principles:`
- Checkpoints: core beliefs (3+), what defends, what rejects, trade-offs, non-negotiables

**Layer 7: Core Obsessions** (Deep, weight 1.0)
- Where: repetition of themes, `obsessions:`, `focus:`
- Checkpoints: recurring themes (3+), named obsessions, hills to die on, mission statement, legacy thinking

**Layer 8: Productive Paradoxes** (Deep, weight 1.0)
- Where: `contradictions:`, `paradoxes:`, `tensions:`
- Checkpoints: contradictions section, named paradoxes (2+), feature not bug, context-dependent, integration note

### Step 2: Format Results

```yaml
layer_scores:
  layer_1_behavioral_patterns:
    score: 0  # 0-5
    checkpoints_passed: []
    checkpoints_failed: []
  # ... layers 2-8 ...
```

## Output

```yaml
layer_scores: { 8 layers with checkpoint details }
```

## Acceptance Criteria

- [ ] All 8 layers evaluated
- [ ] Each layer has 5 checkpoints marked PASS or FAIL
- [ ] Scores match preflight script output
- [ ] Observable layers (1-4) and Deep layers (5-8) clearly separated

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-fidelity-score.md` | Parent orchestrator |
| `an-fidelity-score-identify.md` | Previous phase |
| `an-fidelity-score-calculate.md` | Next phase |
