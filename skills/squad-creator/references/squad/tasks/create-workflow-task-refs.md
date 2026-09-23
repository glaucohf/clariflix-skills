# Task: Resolve and Bind Task References

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-workflow-task-refs` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-workflow-task-refs
name: Resolve and Bind Task References
category: workflow-creation
agent: squad-chief
elicit: true
autonomous: false
description: >
  Assign agents to workflow phases, resolve task_ref bindings
  for each step, define handoff points between phases, and
  map agent synergies and conflicts. Applies
  executor-matrix-framework.md for agent assignment.
```

## Purpose

Resolve concrete task file references (task_ref) for every step in each phase, assign primary and secondary agents to phases, define handoff points with context passing, and identify agent synergies and conflicts. This bridges the abstract phase design to executable task bindings.

## Prerequisites

- [ ] Phase design complete (create-workflow-phases output, SC_PHS_001 passed)
- [ ] `data/executor-matrix-framework.md` is accessible
- [ ] Target squad agents are known (from config.yaml)

## Inputs

```yaml
inputs:
  - name: phase_design
    type: object
    required: true
    source: previous_task
    description: "Phase structure from create-workflow-phases"

  - name: squad_name
    type: string
    required: true
    source: previous_task
    description: "Target squad identifier"

  - name: squad_config
    type: object
    required: true
    source: filesystem
    description: "Squad config.yaml with agent definitions"
```

## Workflow / Steps

### Step 1: Assign Agents to Phases

**Apply: executor-matrix-framework.md**

```yaml
agent_assignment:
  template: |
    agents_by_phase:
      PHASE-{N}:
        primary:
          - "{primary_agent_1}"
          - "{primary_agent_2}"
        secondary:
          - "{secondary_agent_1}"

  criteria:
    primary_agent: "Main executor for the phase"
    secondary_agent: "Supports or validates primary"
```

**Elicitation:**

```yaml
elicit_agents:
  for_each_phase:
    - "Which agent is PRIMARY for Phase {N}?"
    - "Which agents SUPPORT this phase?"
    - "Are these agents defined in the squad?"
```

### Step 2: Resolve task_ref Bindings

For each task listed in each phase, resolve the concrete task file:

```yaml
resolve_task_ref:
  for_each_task_in_phase:
    check_existing:
      - path: "squads/{squad_name}/tasks/{task_file}"
      - exists: true | false

    if_exists:
      action: "Bind task_ref to existing file"

    if_not_exists:
      options:
        - "Create task via *create-task (recommended)"
        - "Mark as placeholder with TODO"
        - "Reference a task from another squad"

    binding_format: "task_ref, agent, required, description, output"
```

### Step 3: Define Handoff Points

```yaml
handoff_points:
  template: |
    handoffs:
      - from_phase: PHASE-{N}
        to_phase: PHASE-{N+1}
        from_agent: "{agent_1}"
        to_agent: "{agent_2}"
        context_passed:
          - "{context_item_1}"
          - "{context_item_2}"
        validation: "{handoff_validation}"

  criteria:
    - "Clear sender and receiver"
    - "Context preserved between phases"
    - "Validation at handoff"
```

### Step 4: Map Synergies and Conflicts

Document which agents work well together and which should not share phases.

### Step 5: Validate Agent Assignments

**Checkpoint SC_AGN_001:**

```yaml
heuristic_id: SC_AGN_001
name: "Agents Assigned"
blocking: true
criteria:
  - all_phases_have_primary_agent
  - all_task_refs_resolved_or_marked
  - handoff_points_defined
  - agents_exist_in_squad_config
```

## Output

```yaml
output:
  name: task_ref_bindings
  format: yaml
  structure:
    agents_by_phase: {}      # Phase -> agent mapping
    task_refs: []             # Resolved task_ref per step
    handoff_points: []        # Phase-to-phase handoffs
    synergies: []             # Agent synergy patterns
    conflicts: []             # Agent conflict patterns
    unresolved_tasks: []      # Tasks that need creation
    checkpoint_SC_AGN_001: "PASS | FAIL"
```

## Acceptance Criteria

- [ ] Every phase has at least one primary agent assigned
- [ ] All task_ref values resolved to existing files or marked as TODO
- [ ] Handoff points defined for each phase transition
- [ ] Agents referenced exist in squad config.yaml
- [ ] Synergies and conflicts documented
- [ ] Checkpoint SC_AGN_001 passes

## Veto Conditions

- Phase has no agent assigned
- task_ref references non-existent file without acknowledgment
- Agent not defined in squad config
- No handoff points between consecutive phases

## Related Documents

- `data/executor-matrix-framework.md` -- Agent assignment framework
- `create-workflow-phases.md` -- Preceding task (phase design)
- `create-workflow-gates.md` -- Next task (quality gates)
- `create-workflow.md` -- Parent composed task

---

_Task Version: 1.0.0_
_Extracted from: create-workflow.md PHASE 3 (Agent Assignment)_
