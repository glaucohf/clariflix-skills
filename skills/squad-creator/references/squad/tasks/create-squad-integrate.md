# Task: Squad Integration — Dependencies, Documentation & Activation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-integrate` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: create-squad-integrate
name: "Squad Integration"
category: squad-creation
agent: squad-chief
elicit: false
autonomous: true
description: "Wire internal dependencies, create knowledge base, generate documentation, prepare COO handoff, and publish activation surfaces."
```

## Purpose

Wire all squad components together by verifying cross-references, creating the domain knowledge base, generating complete documentation, preparing workspace integration handoffs when required, and publishing the chief activation command and codex skill.

## Prerequisites

- [ ] `create-squad-components` completed (all agents, workflows, tasks created)
- [ ] All agents pass quality gates
- [ ] All workflows pass contract validation
- [ ] `config.yaml` has valid `entry_agent` and `workspace_integration.level`

## Inputs

```yaml
inputs:
  phase_3_output:
    type: object
    required: true
    description: "Output from create-squad-components"
    fields: [agents_created, workflows_created, tasks_created, templates_created]
  squad_name:
    type: string
    required: true
  entry_agent:
    type: string
    required: true
  slash_prefix:
    type: string
    required: true
  workspace_integration_level:
    type: string
    required: true
    description: "none | read_only | controlled_runtime_consumer | workspace_first"
```

## Workflow / Steps

### Step 4.1: Wire Dependencies

```yaml
wire_dependencies:
  for_each_agent:
    - verify tasks exist
    - verify templates exist
    - verify checklists exist
    - update dependencies block

  missing_dependency_policy:
    - if dependency referenced but doesn't exist -> FAIL phase
    - create explicit remediation queue with missing file paths
    - never create stubs/placeholders in final squad artifacts
```

### Step 4.2: Create Knowledge Base

```yaml
create_knowledge_base:
  file: "data/{squad_name}-kb.md"

  sections:
    - domain_overview: "What this domain is about"
    - key_concepts: "Essential terminology"
    - best_practices: "From domain research"
    - common_patterns: "Reusable patterns"
    - anti_patterns: "What to avoid"
    - regulatory: "If applicable"
```

### Step 4.3: Generate Documentation

```yaml
generate_documentation:
  readme:
    file: "README.md"
    sections:
      - overview
      - installation
      - quick_start
      - agents_list
      - workflows_list
      - tasks_list
      - templates_list
      - usage_examples

  config:
    file: "config.yaml"
    validate: true
```

### Step 4.4: Prepare COO Workspace Handoff

```yaml
prepare_coo_handoff:
  trigger:
    - "created squad declares workspace_integration.level = controlled_runtime_consumer"
    - "created squad declares workspace_integration.level = workspace_first"

  rule: |
    squad-creator nao executa integracao real com workspace.
    Ele prepara um handoff para COO/aiox-workspace com contrato, paths e acoes pendentes.

  if_c_level_exists:
    handoff_target: "@coo"
    artifact: ".aiox/squad-runtime/create-squad/{squad_name}/workspace-handoff.yaml"
    must_include:
      - squad_name
      - requested_workspace_level
      - rationale
      - read_paths
      - write_paths
      - template_namespace
      - requested_workspace_actions
      - dependencies_on_existing_domains_or_businesses

  if_c_level_missing:
    artifact: ".aiox/squad-runtime/create-squad/{squad_name}/workspace-handoff.yaml"
    status: "pending_coo_unavailable"
    note: "Nao executar integracao. Apenas registrar handoff pendente."
```

**VETO-SQD-005:** If the workflow attempts to write directly into `workspace/` during squad creation, HALT and generate COO handoff instead.

### Step 4.5: Publish Chief Activation Surfaces

```yaml
publish_chief_activation:
  command_sync:
    task: "sync-ide-command"
    input:
      type: "squad"
      name: "{squad_name}"
    must_produce:
      - ".claude/commands/{slash_prefix}/agents/{entry_agent}.md"

  codex_skill_sync:
    task: "sync-chief-codex-skill"
    input:
      squad_name: "{squad_name}"
    must_produce:
      - ".codex/skills/{entry_agent}/SKILL.md"

  blocking_rule: "Do not finalize squad creation if either artifact is missing"
```

## Output

```yaml
phase_4_output:
  dependencies_wired: true
  missing_dependencies: []
  knowledge_base: "data/{squad_name}-kb.md"
  readme_complete: true
  coo_handoff_status: "not_required | prepared | pending_coo_unavailable"
  command_published: ".claude/commands/{slash_prefix}/agents/{entry_agent}.md"
  codex_skill_published: ".codex/skills/{entry_agent}/SKILL.md"
  status: "PASS"
```

## Acceptance Criteria

- [ ] All internal dependencies verified (no broken references)
- [ ] Knowledge base created with domain content
- [ ] README.md complete with all sections
- [ ] COO handoff prepared when `workspace_integration.level` requires it
- [ ] Chief activation command published
- [ ] Codex skill published
- [ ] No stubs or placeholders remain in final artifacts

## Veto Conditions

- **VETO-SQD-005:** Direct workspace mutation attempted (must use COO handoff)
- Missing dependency referenced by an agent with no remediation
- Chief activation command or codex skill not produced

## Related Documents

- `create-squad.md` (parent composed task)
- `create-squad-components.md` (previous step)
- `create-squad-validate.md` (next step)
- `tasks/sync-ide-command.md`

---

_Task Version: 1.0.0_
_Extracted from: create-squad.md PHASE 4_
