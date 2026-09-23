# Task: Define Quality Gates and Conditions

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-workflow-gates` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-workflow-gates
name: Define Quality Gates and Conditions
category: workflow-creation
agent: squad-chief
elicit: true
autonomous: false
description: >
  Define checkpoints per phase, veto conditions, error handling
  procedures, and circuit breakers. Applies
  decision-heuristics-framework.md for checkpoint logic.
```

## Purpose

Design the complete validation layer for the workflow: per-phase checkpoints with specific criteria, veto conditions that block progress, error handling procedures for failures, and circuit breakers for escalation. This ensures the workflow has built-in quality enforcement at every transition.

## Prerequisites

- [ ] Phase design complete (create-workflow-phases output)
- [ ] Agent assignments complete (create-workflow-task-refs output)
- [ ] `data/decision-heuristics-framework.md` is accessible

## Inputs

```yaml
inputs:
  - name: phase_design
    type: object
    required: true
    source: previous_task
    description: "Phase structure from create-workflow-phases"

  - name: task_ref_bindings
    type: object
    required: true
    source: previous_task
    description: "Agent and task bindings from create-workflow-task-refs"
```

## Workflow / Steps

### Step 1: Define Checkpoints Per Phase

```yaml
checkpoint_design:
  every_phase_must_have:
    - criteria: "List of specific validation items"
    - human_review: "true for important decisions"
    - message: "Context for the reviewer"

  checkpoint_template: |
    checkpoint:
      criteria:
        - "{criterion_1}"
        - "{criterion_2}"
        - "{criterion_3}"
      human_review: {true|false}
      message: "{reviewer_context}"
```

**Elicitation:**

```yaml
elicit_checkpoint:
  for_each_phase:
    - "What must be true to complete Phase {N}?"
    - "List 2-4 specific criteria"
    - "Does this checkpoint need human review?"
    - "What context should the reviewer have?"
```

### Step 2: Set Veto Conditions

**Apply: decision-heuristics-framework.md**

```yaml
veto_conditions:
  purpose: "Define conditions that BLOCK progress"

  template: |
    checkpoint_config:
      - phase: PHASE-{N}
        heuristic: "{heuristic_id}"
        criteria: "{criteria}"
        veto_condition: "{veto_condition}"

  examples:
    - veto: "Vision unclear (<0.7 clarity score)"
    - veto: "Missing required outputs"
    - veto: "Quality score below 7.0"
    - veto: "Security validation failed"
    - veto: "Human review rejected"
```

### Step 3: Design Error Handling

```yaml
error_handling:
  template: |
    error_handling:
      on_phase_failure:
        - log_error: true
        - notify_stakeholders: true
        - create_remediation_task: true
        - halt_workflow: {true|false}

      on_checkpoint_failure:
        - log_failure_reason: true
        - return_to_previous_phase: {true|false}
        - max_retries: {count}

      on_veto_triggered:
        - halt_immediately: true
        - escalate_to: "{escalation_target}"
        - document_reason: true
```

### Step 4: Define Circuit Breakers

Max 3 retries per checkpoint. Escalation path: phase owner, then squad-chief, then @master. Configurable timeout per phase; on timeout: halt and escalate.

### Step 5: Validate Checkpoints

**Checkpoint SC_CKP_001:**

```yaml
heuristic_id: SC_CKP_001
name: "Checkpoints Complete"
blocking: true
criteria:
  - all_phases_have_checkpoint
  - all_checkpoints_have_criteria
  - veto_conditions_defined
  - error_handling_defined
```

## Output

```yaml
output:
  name: gates_and_conditions
  format: yaml
  structure:
    checkpoints: []         # Per-phase checkpoint definitions
    veto_conditions: []     # Blocking conditions
    error_handling: {}      # Failure procedures
    circuit_breakers: {}    # Escalation and timeout config
    checkpoint_SC_CKP_001: "PASS | FAIL"
```

## Acceptance Criteria

- [ ] Every phase has a checkpoint with 2+ criteria
- [ ] Human review flag set for each checkpoint
- [ ] Veto conditions defined (at least 1 per critical phase)
- [ ] Error handling covers phase failure, checkpoint failure, veto triggered
- [ ] Circuit breakers defined with escalation path
- [ ] Checkpoint SC_CKP_001 passes

## Veto Conditions

- Any phase without a checkpoint
- No veto conditions defined for the workflow
- Error handling section missing
- No escalation path defined

## Related Documents

- `data/decision-heuristics-framework.md` -- Checkpoint logic framework
- `create-workflow-task-refs.md` -- Preceding task (agent/task bindings)
- `create-workflow-generate.md` -- Next task (YAML generation)
- `create-workflow.md` -- Parent composed task

---

_Task Version: 1.0.0_
_Extracted from: create-workflow.md PHASE 2 (Checkpoint Design)_
