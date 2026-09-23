# Task: Squad Components — Agents, Workflows & Tasks Creation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-components` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: create-squad-components
name: "Squad Components Creation"
category: squad-creation
agent: squad-chief
elicit: false
autonomous: true
description: "Create all squad components — agents (template-driven with research), orchestrator, workflows, and tasks — with quality gates."
```

## Purpose

Create the core functional components of the squad: agents from templates enriched with domain research, the orchestrator agent with routing logic, multi-step workflows with checkpoints, and atomic tasks following Task Anatomy. Each component passes its quality gate before proceeding.

## Prerequisites

- [ ] `create-squad-scaffold` completed (directory structure exists)
- [ ] Agent roster with tier assignments available (from PHASE 1-2)
- [ ] Templates available: `templates/agent-tmpl.md`, `templates/workflow-tmpl.yaml`
- [ ] Frameworks loaded: `data/executor-matrix-framework.md`
- [ ] WebSearch tool available (for domain research)

## Inputs

```yaml
inputs:
  scaffold_output:
    type: object
    required: true
    description: "Output from create-squad-scaffold"
    fields: [base_path, directories_created]
  agent_roster:
    type: list
    required: true
    description: "Agent roles with tier assignments from architecture phase"
  tier_structure:
    type: object
    required: true
    description: "Complete tier structure from architecture phase"
  quality_gates:
    type: list
    required: true
    description: "Quality gate definitions from architecture phase"
  squad_name:
    type: string
    required: true
  template_approach:
    type: string
    required: true
    description: "operational | expert_template | hybrid"
```

## Workflow / Steps

### Step 3.2: Create Agents (Template-Driven)

For each agent in the roster:

```yaml
for_each_agent_role:
  template: "templates/agent-tmpl.md"

  process:
    step_1_load_template:
      action: "Load templates/agent-tmpl.md as base structure"

    step_2_research_role:
      action: "Research domain best practices for this role via WebSearch"
      focus:
        - "What methodologies exist for this role?"
        - "What are the key frameworks and processes?"
        - "What vocabulary and terminology is standard?"
        - "What are common anti-patterns?"

    step_3_fill_template:
      action: "Fill template sections with researched content"
      sections:
        - agent_metadata: "name, id, title, icon, whenToUse"
        - persona: "role, style, identity, focus"
        - core_principles: "5-10 principles from domain research"
        - commands: "Role-specific commands"
        - voice_dna: "Domain-appropriate vocabulary and tone"
        - output_examples: "3+ realistic examples"
        - anti_patterns: "Domain-specific never_do/always_do"
        - completion_criteria: "Per task type"
        - handoff_to: "3+ handoff scenarios"

    step_4_validate:
      action: "Run agent-quality-gate.md for each agent"
      blocking: true
      retry_on_fail: true
      max_retries: 2

  quality_gate:
    blocking: true
    min_lines: 300
    required_sections:
      - voice_dna
      - output_examples
      - anti_patterns
      - completion_criteria
```

### Step 3.3: Create Orchestrator Agent

```yaml
create_orchestrator:
  agent_id: "{squad_name}-chief"
  role: "Squad Orchestrator"
  tier: "orchestrator"

  special_capabilities:
    - "Route requests to appropriate tier"
    - "Manage multi-agent workflows"
    - "Track context across handoffs"
    - "Report squad status"

  commands:
    - "*help" - List all squad capabilities
    - "*route" - Route request to best agent
    - "*status" - Show current context
    - "*handoff" - Transfer to specific agent

  must_include:
    - tier_routing_logic
    - quality_gate_checks
    - context_preservation
```

### Step 3.4: Create Workflows

```yaml
create_workflows:
  criteria:
    - spans_multiple_agents: true
    - has_intermediate_checkpoints: true
    - output_feeds_next_step: true

  template: "templates/workflow-tmpl.yaml"

  minimum_structure:
    - phases: 3+
    - checkpoints_per_phase: 1+
    - framework_references: 2+

  quality_standard:
    min_lines: 500

  contract_validation:
    blocking: true
    command_per_file: >
      node infrastructure/scripts/squads/validate_workflow_contract_single.cjs
      --file {workflow_file}
      --strict
      --fail-on-warnings
    policy:
      - validate_immediately_after_creation: true
      - stop_on_first_failure: true
      - rerun_after_fix_until_pass: true
```

### Step 3.5: Create Tasks

**Apply: executor-matrix-framework.md**

```yaml
create_tasks:
  task_anatomy:
    - id: "Unique identifier"
    - purpose: "What and why"
    - executor: "Human | Agent | Hybrid | Worker"
    - inputs: "What it needs"
    - preconditions: "What must be true"
    - steps: "How to execute"
    - outputs: "What it produces"
    - validation: "How to verify"

  executor_assignment:
    decision_tree:
      - IF rule_based AND low_stakes -> Worker
      - ELSE IF needs_judgment -> Hybrid (AI draft, human approve)
      - ELSE IF creative_synthesis -> Agent
      - ELSE -> Human

  quality_standard:
    simple_tasks: 300+ lines
    complex_tasks: 500+ lines
```

## Output

```yaml
phase_3_output:
  agents_created: "{N}"
  all_pass_quality_gate: true
  workflows_created: "{N}"
  tasks_created: "{N}"
  templates_created: "{N}"
  total_lines: "{N}"
```

## Acceptance Criteria

- [ ] All agents pass SC_AGT_001 (300+ lines, voice_dna, output_examples, anti_patterns, completion_criteria)
- [ ] Orchestrator agent exists with routing logic
- [ ] All complex operations have workflows (3+ phases, checkpoints)
- [ ] All workflows pass contract validation (strict mode)
- [ ] All tasks follow Task Anatomy (8 fields)
- [ ] Executor assigned for each task
- [ ] **VETO-SQD-003:** `config.yaml` references a valid entry agent file

## Veto Conditions

- **VETO-SQD-003:** Entry agent referenced in `config.yaml` does not exist as a file
- Agent fails quality gate after 2 retries
- Workflow fails contract validation after fix cycle

## Related Documents

- `create-squad.md` (parent composed task)
- `create-squad-scaffold.md` (previous step)
- `create-squad-integrate.md` (next step)
- `templates/agent-tmpl.md`
- `templates/workflow-tmpl.yaml`
- `data/executor-matrix-framework.md`
- `checklists/agent-quality-gate.md`

---

_Task Version: 1.0.0_
_Extracted from: create-squad.md PHASE 3 (Steps 3.2-3.5)_
