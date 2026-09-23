# Task: Create Squad Workflow (Extension Wrapper)

**Task ID:** create-workflow
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a criação real de workflows ao pipeline atômico do `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado do base workflow

---

## Purpose

Este arquivo existe para manter compatibilidade com workflows do `squad-creator-pro` que ainda invocam `create-workflow` diretamente durante a montagem de squads.

**Regra não negociável:** a criação estrutural de workflows pertence ao base. O `squad-creator-pro` pode enriquecer contexto, mas não deve manter uma segunda implementação completa de `create-workflow`.

Owner canônico da criação de workflow:

- `squads/squad-creator/workflows/wf-create-workflow.yaml`
- `squads/squad-creator/tasks/create-workflow-classify.md`
- `squads/squad-creator/tasks/create-workflow-phases.md`
- `squads/squad-creator/tasks/create-workflow-task-refs.md`
- `squads/squad-creator/tasks/create-workflow-gates.md`
- `squads/squad-creator/tasks/create-workflow-generate.md`
- `squads/squad-creator/tasks/create-workflow-register.md`

O papel deste wrapper é:

1. normalizar inputs legados do pro;
2. transferir contexto adicional já descoberto pelo pro;
3. delegar a criação para o pipeline atômico do base;
4. devolver o workflow criado no formato esperado pelos chamadores do pro.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workflow_purpose` | string | Yes | Objetivo principal do workflow |
| `workflow_name` | string | No | Nome humano do workflow |
| `workflow_id` | string | No | Identificador em kebab-case |
| `squad_name` | string | No | Nome canônico do squad alvo |
| `pack_name` | string | No | Alias legado usado no pro; deve ser normalizado para `squad_name` |
| `duration` | string | No | Duração esperada |
| `phase_count` | int | No | Número estimado de fases |
| `source_artifacts` | list | No | Artefatos de discovery, PRD ou research vindos do pro |
| `integration_notes` | object | No | Restrições arquiteturais ou handoffs já definidos |

---

## Preconditions

- [ ] `squads/squad-creator/workflows/wf-create-workflow.yaml` existe
- [ ] O squad alvo existe em `squads/{squad_name}/` ou `squads/{pack_name}/`
- [ ] O chamador entende que este wrapper não define pipeline próprio
- [ ] Qualquer discovery, PRD ou research adicional do pro já foi produzido antes da delegação

---

## Workflow

### Step 1: Normalize Target Squad

```yaml
normalize_target:
  rules:
    - if: "squad_name is empty AND pack_name exists"
      then: "set squad_name = pack_name"
    - if: "both squad_name and pack_name exist AND differ"
      then: "block and reconcile target"
    - verify_path: "squads/{squad_name}/"
```

### Step 2: Build Base Payload

```yaml
build_base_payload:
  required_fields:
    - workflow_purpose
    - squad_name
  optional_fields:
    - workflow_name
    - workflow_id
    - duration
    - phase_count
    - source_artifacts
    - integration_notes
  rule: >
    O contexto do pro pode enriquecer o desenho das fases, task_refs e handoffs,
    mas não cria uma metodologia paralela de create-workflow.
```

### Step 3: Delegate to Base Workflow

```yaml
delegate_to_base:
  workflow: "squads/squad-creator/workflows/wf-create-workflow.yaml"
  execution_contract:
    - use_base_classification: true
    - use_base_phase_design: true
    - use_base_task_binding: true
    - use_base_gate_definition: true
    - use_base_generation: true
    - use_base_registration: true
  prohibition:
    - "Do NOT recreate create-workflow-* atomics inside squad-creator-pro"
    - "Do NOT fork quality gates or workflow state rules locally"
```

### Step 4: Reconcile Outputs for Pro Callers

```yaml
reconcile_outputs:
  primary_outputs:
    - "squads/{squad_name}/workflows/wf-{workflow_id}.yaml"
    - "squads/{squad_name}/config.yaml"
    - "squads/{squad_name}/README.md"
  enrichments:
    - if_source_artifacts: "Preserve architectural provenance in handoff summary"
    - if_integration_notes: "Carry forward pro-specific integration constraints"
  return_shape:
    workflow_file: "path to created workflow"
    delegated_workflow: "squads/squad-creator/workflows/wf-create-workflow.yaml"
    execution_mode: "base-delegated"
```

---

## Output

```yaml
output:
  name: delegated_workflow_creation
  format: yaml
  structure:
    workflow_file: "squads/{squad_name}/workflows/wf-{workflow_id}.yaml"
    delegated_workflow: "squads/squad-creator/workflows/wf-create-workflow.yaml"
    normalized_squad_name: "{squad_name}"
    inherited_context:
      source_artifacts: ["optional artifacts"]
      integration_notes: "{optional}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] `pack_name` e `squad_name` são reconciliados corretamente
- [ ] A criação real do workflow é delegada ao workflow base
- [ ] Nenhuma implementação paralela de create-workflow permanece no pro
- [ ] Workflows do pro que dependem de `create-workflow` continuam compatíveis
- [ ] Contexto adicional do pro é preservado sem duplicar a lógica do base

---

## Veto Conditions

- `squad-creator-pro` tentar executar pipeline próprio de create-workflow
- `squad_name` e `pack_name` apontarem para squads diferentes
- O workflow base `wf-create-workflow.yaml` não existir
- Algum chamador do pro depender de fase inventada que não exista no base

---

## Related Documents

- `squads/squad-creator/workflows/wf-create-workflow.yaml` -- owner canônico
- `squads/squad-creator/tasks/create-workflow.md` -- wrapper composto do base
- `workflows/wf-context-aware-create-squad.yaml` -- chamador do pro
- `workflows/wf-create-squad.yaml` -- chamador do pro

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed create-workflow output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
