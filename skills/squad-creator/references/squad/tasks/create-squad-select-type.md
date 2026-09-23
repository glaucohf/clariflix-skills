# Task: Squad Type Selection — Template Approach & Use Case Mapping

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-select-type` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-squad-select-type
name: "Squad Type Selection"
category: squad-creation
agent: squad-chief
elicit: true
autonomous: false
description: "Select squad type from catalog, choose template approach (operational vs expert), and map use cases to agent roles."
```

## Purpose

Determine the best squad archetype from `squad-type-definitions.yaml`, choose between operational and expert template approaches, and produce an initial agent roster with tier assignments and use case coverage.

## Prerequisites

- [ ] `create-squad-discover` completed successfully (PHASE 0 output available)
- [ ] `data/squad-type-definitions.yaml` exists and is readable
- [ ] Domain viability confirmed (score >= 6 or user override)
- [ ] Squad name and entry agent defined

## Inputs

```yaml
inputs:
  phase_0_output:
    type: object
    required: true
    description: "Output from create-squad-discover"
    fields: [viability_score, decision, squad_name, entry_agent, slash_prefix, pattern_prefix, mode]
  domain:
    type: string
    required: true
  purpose:
    type: string
    required: true
  use_cases:
    type: list
    required: true
  target_user:
    type: string
    required: true
```

## Workflow / Steps

### Step 1.1: Load Squad Type Definitions

```yaml
load_squad_types:
  file: "data/squad-type-definitions.yaml"
  required: true

  extract:
    - available_types: "List of squad archetypes"
    - type_characteristics: "What each type is optimized for"
    - recommended_agent_counts: "Min/max agents per type"
    - template_approaches: "Operational vs Expert patterns"
```

### Step 1.2: Select Squad Type

```yaml
squad_type_selection:
  decision_inputs:
    - domain: "{domain}"
    - purpose: "{purpose}"
    - use_cases: "{use_cases}"
    - target_user: "{target_user}"

  matching_criteria:
    - domain_alignment: "Which type best fits the domain?"
    - use_case_coverage: "Which type covers the most use cases?"
    - complexity_match: "Does type complexity match squad needs?"

  elicit_if_ambiguous:
    question: "Multiple squad types could work. Which approach fits best?"
    present_options:
      - type: "Describe each matching type with pros/cons"
      - recommendation: "Highlight best match with rationale"
```

**Decision Point:**
```
IF clear single match:
    -> AUTO-SELECT and inform user
ELSE IF 2-3 close matches:
    -> PRESENT options with rationale
    -> ASK user to select
ELSE:
    -> WARN: "Domain is unusual. Using generic template."
    -> PROCEED with generic structure
```

### Step 1.3: Choose Template Approach

```yaml
template_approach:
  operational:
    description: "Agents defined by function/role, not based on specific experts"
    best_for: "Technical domains, process-heavy workflows"
    agent_naming: "Function-based (e.g., analyzer, writer, reviewer)"
    example: "data-squad with etl-agent, query-optimizer, schema-designer"

  expert_template:
    description: "Agents modeled after domain expert archetypes using web research"
    best_for: "Creative domains, knowledge-heavy workflows"
    agent_naming: "Archetype-based (e.g., strategist, master-copywriter)"
    example: "copy-squad with headline-specialist, persuasion-expert"

  decision_tree:
    - IF domain is technical/process-oriented:
        approach: "operational"
    - ELSE IF domain is creative/knowledge-oriented:
        approach: "expert_template"
    - ELSE:
        approach: "hybrid (operational core + expert specialists)"
```

### Step 1.4: Map Use Cases to Agent Roles

```yaml
use_case_agent_mapping:
  for_each_use_case:
    - use_case: "{use_case}"
      derive:
        - required_roles: "What agent roles are needed?"
        - tier_suggestion: "Which tier should handle this?"
        - shared_roles: "Can an existing role cover this?"

  output:
    agent_roster:
      - role: "diagnostician"
        tier: 0
        covers_use_cases: ["all - initial analysis"]
      - role: "primary-executor"
        tier: 1
        covers_use_cases: ["use_case_1", "use_case_2"]
      - role: "specialist"
        tier: 3
        covers_use_cases: ["use_case_3"]

  constraints:
    min_agents: 3
    max_agents: 12
    must_have_tier_0: true
    must_have_orchestrator: true
```

## Output

```yaml
phase_1_output:
  squad_type: "{selected_type}"
  template_approach: "operational | expert_template | hybrid"
  agent_roster:
    - role: "{role_name}"
      tier: "{0|1|2|3}"
      covers: ["use_case_list"]
  total_agents_planned: "{N}"
  checkpoint_status: "PASS | FAIL"
```

## Acceptance Criteria

- [ ] Squad type selected from `squad-type-definitions.yaml`
- [ ] Template approach defined (operational, expert_template, or hybrid)
- [ ] Agent roster has at least one Tier 0 agent
- [ ] Agent roster has an orchestrator role
- [ ] All input use cases mapped to at least one agent role
- [ ] Agent count within 3-12 range
- [ ] Checkpoint SC_TPL_001 passes

## Veto Conditions

- Agent roster missing Tier 0 agent
- Agent roster missing orchestrator
- Use cases left unmapped to any agent role
- Agent count exceeds 12 without PRD/epic execution mode

## Related Documents

- `create-squad.md` (parent composed task)
- `create-squad-discover.md` (previous step)
- `create-squad-architecture.md` (next step)
- `data/squad-type-definitions.yaml`
- `data/tier-system-framework.md`

---

_Task Version: 1.0.0_
_Extracted from: create-squad.md PHASE 1_
