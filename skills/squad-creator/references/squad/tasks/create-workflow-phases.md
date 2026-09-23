# Task: Design Workflow Phases

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-workflow-phases` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-workflow-phases
name: Design Workflow Phases
category: workflow-creation
agent: squad-chief
elicit: true
autonomous: false
description: >
  Design the phase structure for a workflow: define each phase
  with tier classification, tasks, duration, and inline structures.
  Applies tier-system-framework.md for phase tier assignment.
```

## Purpose

Design the complete phase structure of a workflow through interactive elicitation. Each phase receives a tier classification (0-3), task assignments, duration, and optional inline structures for domain-specific guidance. This phase produces the structural backbone that all subsequent phases build upon.

## Prerequisites

- [ ] Phase 0 classification complete (create-workflow-classify output)
- [ ] `data/tier-system-framework.md` is accessible
- [ ] Phase count is known (>= 3)

## Inputs

```yaml
inputs:
  - name: phase_0_classification
    type: object
    required: true
    source: previous_task
    description: "Classification output from create-workflow-classify"

  - name: squad_name
    type: string
    required: true
    source: previous_task
    description: "Target squad identifier"
```

## Workflow / Steps

### Step 1: Design Phase Structure

**Apply: tier-system-framework.md**

```yaml
tier_definitions:
  tier_0: "Foundation - Must complete before anything else"
  tier_1: "Core - Main execution phase"
  tier_2: "Advanced - Enhancement and optimization"
  tier_3: "Polish - Final quality assurance"

for_each_phase:
  - phase_number: "Sequential number (1, 2, 3...)"
  - phase_name: "Human-readable name"
  - phase_days: "Duration (e.g., 'Days 1-2')"
  - phase_tier: "0, 1, 2, or 3"
  - phase_description: "What this phase accomplishes"
  - phase_tasks: "List of tasks in this phase"
```

### Step 2: Elicit Each Phase

**Elicitation per phase:**

```yaml
elicit_phase:
  phase_identity:
    - "What is the name of Phase {N}?"
    - "What days does it span?"
    - "What tier is it? (0=foundation, 1=core, 2=advanced, 3=polish)"

  phase_content:
    - "What tasks belong to this phase?"
    - "Which agent executes each task?"
    - "What does this phase produce?"

  phase_checkpoint:
    - "What must be true to complete this phase?"
    - "Does it need human review?"
```

**Phase template:**

```yaml
phase_template:
  structure: |
    - id: PHASE-{phase_number}
      name: "{phase_name}"
      days: "{phase_days}"
      tier: {phase_tier}
      description: |
        {phase_description}

      tasks:
        - task_file: "{task_file}"
          agent: "{agent_id}"
          required: true
          description: "{task_description}"
          output: "{output_file}"

      checkpoint:
        criteria:
          - "{criterion_1}"
          - "{criterion_2}"
        human_review: true
        message: "{checkpoint_message}"
```

### Step 3: Add Inline Structures (If Needed)

```yaml
inline_structure_criteria:
  add_when:
    - "Phase produces complex multi-part output"
    - "Detailed step-by-step guidance is needed"
    - "Timing/duration specifications are important"
    - "Domain-specific formatting required"

  examples:
    email_sequence:
      pattern: "SOS structure with cliffhangers"
    webinar_structure:
      pattern: "Introduction, content, close with durations"
    call_script:
      pattern: "Phased script with timing and elements"
```

### Step 4: Validate Phase Structure

**Checkpoint SC_PHS_001:**

```yaml
heuristic_id: SC_PHS_001
name: "Phases Defined"
blocking: true
criteria:
  - phases_count >= 3
  - all_phases_have_tier
  - all_phases_have_tasks
  - tier_0_exists  # Foundation phase required
```

## Output

```yaml
output:
  name: phase_design
  format: yaml
  structure:
    phases: []        # Array of phase definitions
    phase_count: "{N}"
    inline_structures: "{count}"
    checkpoint_SC_PHS_001: "PASS | FAIL"
```

## Acceptance Criteria

- [ ] At least 3 phases designed
- [ ] Every phase has id, name, days, tier, description
- [ ] Every phase has at least 1 task assigned
- [ ] Tier 0 (foundation) phase exists
- [ ] Tiers assigned via tier-system-framework.md
- [ ] Inline structures added where domain guidance is needed
- [ ] Checkpoint SC_PHS_001 passes

## Veto Conditions

- Fewer than 3 phases defined
- No tier 0 (foundation) phase
- Any phase missing tasks
- Tier assignment skipped (not using framework)

## Related Documents

- `data/tier-system-framework.md` -- Phase tier classification
- `create-workflow-classify.md` -- Preceding task (classification)
- `create-workflow-task-refs.md` -- Next task (task binding)
- `create-workflow.md` -- Parent composed task

---

_Task Version: 1.0.0_
_Extracted from: create-workflow.md PHASE 1_
