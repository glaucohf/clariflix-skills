# Task: Squad Architecture — Tiers, Relationships & Quality Gates

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-architecture` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-squad-architecture
name: "Squad Architecture"
category: squad-creation
agent: squad-chief
elicit: true
autonomous: false
description: "Define tier structure, plan agent relationships and handoffs, design quality gates for the squad."
```

## Purpose

Transform the agent roster from type selection into a complete architectural blueprint with tier assignments, handoff maps, agent synergies/conflicts, and quality gates that govern transitions between tiers.

## Prerequisites

- [ ] `create-squad-select-type` completed successfully (PHASE 1 output available)
- [ ] Agent roster with tier suggestions defined
- [ ] `data/tier-system-framework.md` loaded
- [ ] `data/decision-heuristics-framework.md` loaded

## Inputs

```yaml
inputs:
  phase_1_output:
    type: object
    required: true
    description: "Output from create-squad-select-type"
    fields: [squad_type, template_approach, agent_roster, total_agents_planned]
  squad_name:
    type: string
    required: true
  mode:
    type: enum
    required: true
    description: '"incremental" or "yolo"'
```

## Workflow / Steps

### Step 2.1: Define Tier Structure

**Apply: tier-system-framework.md**

```yaml
tier_structure_design:
  orchestrator:
    purpose: "Coordinates all tiers, routes requests"
    agent_id: "{squad_name}-chief"

  tier_0_diagnosis:
    purpose: "First contact, analysis, classification"
    agents: "From roster where tier == 0"
    required: true

  tier_1_masters:
    purpose: "Primary experts with core execution capability"
    agents: "From roster where tier == 1"

  tier_2_systematizers:
    purpose: "Framework creators and methodology agents"
    agents: "From roster where tier == 2"

  tier_3_specialists:
    purpose: "Specific format/channel experts"
    agents: "From roster where tier == 3"

  tools:
    purpose: "Validation, checklists, calculators"
    examples: ["quality-checker", "compliance-validator"]
```

### Step 2.2: Plan Agent Relationships

```yaml
agent_relationships:
  handoff_map:
    - from: "orchestrator"
      to: "tier_0_agents"
      when: "New request arrives"

    - from: "tier_0_agents"
      to: "tier_1_agents"
      when: "Diagnosis complete, execution needed"

  synergies:
    - agents: ["diagnosis-agent", "master-agent"]
      pattern: "Diagnosis feeds master context"

  conflicts:
    - agents: ["aggressive-style", "conservative-style"]
      reason: "Contradictory approaches"
```

### Step 2.3: Design Quality Gates

```yaml
quality_gates_design:
  gates:
    - id: "QG-001"
      name: "Request Classification"
      transition: "Input -> Tier 0"
      type: "routing"
      criteria: "Request type identified"

    - id: "QG-002"
      name: "Diagnosis Complete"
      transition: "Tier 0 -> Tier 1"
      type: "blocking"
      criteria: "Analysis approved, requirements clear"

    - id: "QG-003"
      name: "Draft Review"
      transition: "Execution -> Output"
      type: "blocking"
      criteria: "Quality checklist passed"

  escalation_paths:
    - on_failure: "Return to previous tier with feedback"
    - on_repeated_failure: "Escalate to human review"
```

## Output

```yaml
phase_2_output:
  tier_structure:
    orchestrator: "{squad}-chief"
    tier_0: ["{diagnosis-agent-1}", "{diagnosis-agent-2}"]
    tier_1: ["{master-agent-1}", "{master-agent-2}"]
    tier_2: ["{systematizer-1}", "{systematizer-2}"]
    tier_3: ["{specialist-1}", "{specialist-2}"]
    tools: ["{tool-1}", "{tool-2}"]
  quality_gates: "{N}"
  handoffs: "{N}"
  architecture_score: "{score}/10"
```

## Acceptance Criteria

- [ ] Tier 0 defined with at least one agent
- [ ] Orchestrator agent defined as `{squad_name}-chief`
- [ ] Quality gates >= 3
- [ ] Handoff map complete (all tier transitions covered)
- [ ] Agent synergies and conflicts documented
- [ ] Checkpoint SC_ARC_001 passes
- [ ] In incremental mode: human approval obtained

## Veto Conditions

- Missing Tier 0 definition
- Missing orchestrator definition
- Fewer than 3 quality gates
- Incomplete handoff map (orphan agents with no incoming/outgoing handoffs)

## Related Documents

- `create-squad.md` (parent composed task)
- `create-squad-select-type.md` (previous step)
- `create-squad-scaffold.md` (next step)
- `data/tier-system-framework.md`
- `data/decision-heuristics-framework.md`

---

_Task Version: 1.0.0_
_Extracted from: create-squad.md PHASE 2_
