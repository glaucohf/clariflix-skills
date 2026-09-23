# Task: Validate Squad — Reconciliation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-reconcile` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-reconcile
name: "Validate Squad Reconciliation"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Merge deterministic facts with reviewer verdicts, apply blocker caps, produce dimension scores and final score."
```

## Purpose

Merge the deterministic collection results (preflight) with the optional semantic review verdicts (deep review). Apply blocker caps and penalties so that deterministic vetoes always remain authoritative. Produce dimension-level scores and a single final score.

## Prerequisites

- [ ] Preflight completed (`validate-squad-preflight`)
- [ ] Type detection completed (`validate-squad-type-detect`)
- [ ] Deep review completed or skipped (`validate-squad-deep-review`)

## Inputs

```yaml
inputs:
  preflight_results:
    type: file
    required: true
    path: "/tmp/preflight-results.yaml"
    description: "Deterministic collection output"
  type_detection:
    type: object
    required: true
    description: "Output from validate-squad-type-detect"
  deep_review:
    type: object
    required: false
    description: "Output from validate-squad-deep-review (null if skipped)"
```

## Workflow / Steps

### Step 1: Establish Deterministic Base

Read all deterministic results from preflight. These are facts -- not negotiable.

```yaml
deterministic_base:
  structure:
    config_valid: true/false
    entry_agent_exists: true/false
    entry_agent_activatable: true/false
    missing_references_pct: N%
    broken_handoffs: N
  security:
    critical_count: N
    warning_count: N
  coverage:
    checklist_coverage: N%
    orphan_tasks: N
    phase_coverage: N%
    data_usage: N%
```

### Step 2: Merge Semantic Scores (if deep review was performed)

If deep review was skipped (quick mode), use deterministic scoring only.

If deep review was performed, merge:

```yaml
merge_rules:
  - Deterministic blockers cap the final score and prevent PASS
  - Semantic review refines diagnosis and priorities; it does not replace hard facts
  - New dimensions are additive in JSON and report output
  - Reclassifications (FALSE_POSITIVE) may adjust warnings but never remove blockers
```

### Step 3: Calculate Final Score

```yaml
score_calculation:
  precondition:
    structure: "PASS"
    coverage: "PASS"
    veto: "PROCEED"

  # If deep review was performed
  formula_deep: "(semantic_score x 0.80) + (contextual_score x 0.20)"

  # If quick mode (no deep review)
  formula_quick: "deterministic_score from preflight scoring.py"

  interpretation:
    9.0-10.0: "EXCELLENT - Gold standard reference"
    7.0-8.9: "PASS - Production ready"
    5.0-6.9: "CONDITIONAL - Needs improvements"
    0.0-4.9: "FAIL - Significant rework needed"
```

### Step 4: Apply Blocker Caps

```yaml
blocker_caps:
  - if structure == ABORT: final_score = min(final_score, 4.9)  # Force FAIL
  - if coverage == ABORT: final_score = min(final_score, 4.9)   # Force FAIL
  - if security.critical > 0: final_score = min(final_score, 4.9)
  - if broken_handoffs > 0: final_score = min(final_score, 6.9)  # Cap at CONDITIONAL
```

### Step 5: Produce Reconciled Output

Combine all sources into a single reconciled payload that preserves backward compatibility with existing JSON contract fields: `final_score`, `deterministic`, `workflow_contracts`, `production`, `claude_analysis`.

## Output

```yaml
output:
  schema:
    final_score: 0.0-10.0
    result: "EXCELLENT | PASS | CONDITIONAL | FAIL"
    mode: "deep | quick"
    deterministic:
      structure_status: "PASS | ABORT"
      coverage_status: "PASS | ABORT"
      security_status: "CLEAN | WARNING | CRITICAL"
    semantic:
      status: "REVIEWED | SKIPPED"
      scores:
        prompt_quality: N
        pipeline_coherence: N
        checklist_actionability: N
        documentation: N
    contextual:
      type: "expert | pipeline | hybrid"
      score: N
    blocker_caps_applied: []
    reclassifications: []
```

## Acceptance Criteria

- [ ] Deterministic facts are never overridden by semantic review
- [ ] Blocker caps correctly force score ceilings
- [ ] Quick mode produces valid score without semantic input
- [ ] Deep mode merges both sources with correct weighting
- [ ] Output preserves backward-compatible JSON fields
- [ ] Score interpretation matches the defined thresholds

## Veto Conditions

- Preflight results missing -> VETO (cannot reconcile without base data)
- Type detection missing -> VETO (cannot apply contextual weights)

## Related Documents

- `validate-squad.md` (parent composed task)
- `validate-squad-preflight.md` (deterministic source)
- `validate-squad-deep-review.md` (semantic source)
- `validate-squad-veto.md` (uses reconciled data for veto check)
- `validate-squad-report.md` (uses reconciled data for report)
