# Task: Create Squad Task (Extension Wrapper)

**Task ID:** create-task
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a criação real de tasks ao pipeline atômico do `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado do base workflow

---

## Purpose

Este arquivo existe para manter compatibilidade com workflows e handoffs do `squad-creator-pro` que ainda referenciam `create-task` diretamente.

**Regra não negociável:** o `squad-creator-pro` é um upgrade-pack do `squad-creator`, não uma implementação paralela. Portanto, a lógica principal de criação de task vive no base e **não deve ser duplicada aqui**.

Owner canônico da criação de task:

- `squads/squad-creator/workflows/wf-create-task.yaml`
- `squads/squad-creator/tasks/create-task-classify.md`
- `squads/squad-creator/tasks/create-task-anatomy.md`
- `squads/squad-creator/tasks/create-task-executor.md`
- `squads/squad-creator/tasks/create-task-generate.md`
- `squads/squad-creator/tasks/create-task-validate.md`
- `squads/squad-creator/tasks/create-task-register.md`

O papel deste wrapper é apenas:

1. normalizar inputs vindos dos workflows do pro;
2. preservar contexto rico já produzido no pro;
3. delegar a execução para o pipeline atômico do base;
4. devolver outputs no formato esperado pelos chamadores do pro.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `task_purpose` | string | Yes | Objetivo principal da task |
| `task_name` | string | Yes | Nome humano da task |
| `squad_name` | string | No | Nome canônico do squad alvo |
| `pack_name` | string | No | Alias legado usado no pro; deve ser normalizado para `squad_name` |
| `complexity` | enum | No | `simple` ou `complex` |
| `source_framework` | string | No | Framework extraído em workflows de pesquisa/clonagem |
| `source_artifacts` | list | No | Artefatos upstream que ajudam a detalhar a task |
| `integration_notes` | object | No | Restrições ou observações trazidas por workflows do pro |

---

## Preconditions

- [ ] `squads/squad-creator/workflows/wf-create-task.yaml` existe
- [ ] O squad alvo existe em `squads/{squad_name}/` ou `squads/{pack_name}/`
- [ ] O chamador entende que este wrapper não possui pipeline próprio
- [ ] Qualquer contexto especial do pro já foi produzido antes da delegação

---

## Workflow

### Step 1: Normalize Target Squad

```yaml
normalize_target:
  rules:
    - if: "squad_name is empty AND pack_name exists"
      then: "set squad_name = pack_name"
    - if: "both squad_name and pack_name exist AND differ"
      then: "block and ask for reconciliation"
    - verify_path: "squads/{squad_name}/"
```

### Step 2: Build Base Payload

```yaml
build_base_payload:
  required_fields:
    - task_purpose
    - task_name
    - squad_name
  optional_context:
    - source_framework
    - source_artifacts
    - integration_notes
  rule: >
    Contexto do pro pode enriquecer a elicitação e os exemplos, mas não cria
    novas fases, novos gates, nem uma metodologia paralela de create-task.
```

### Step 3: Delegate to Base Workflow

```yaml
delegate_to_base:
  workflow: "squads/squad-creator/workflows/wf-create-task.yaml"
  execution_contract:
    - use_base_classification: true
    - use_base_anatomy_definition: true
    - use_base_executor_design: true
    - use_base_generation: true
    - use_base_validation: true
    - use_base_registration: true
  prohibition:
    - "Do NOT recreate create-task-* atomics inside squad-creator-pro"
    - "Do NOT fork line-count rules or validation gates locally"
```

### Step 4: Reconcile Outputs for Pro Callers

```yaml
reconcile_outputs:
  primary_outputs:
    - "squads/{squad_name}/tasks/{task_id}.md"
    - "squads/{squad_name}/config.yaml"
    - "squads/{squad_name}/README.md"
  enrichments:
    - if_source_framework: "Preserve framework provenance in examples or integration notes"
    - if_source_artifacts: "Keep artifact traceability in handoff summary"
  return_shape:
    task_file: "path to created task"
    delegated_workflow: "squads/squad-creator/workflows/wf-create-task.yaml"
    execution_mode: "base-delegated"
```

---

## Output

```yaml
output:
  name: delegated_task_creation
  format: yaml
  structure:
    task_file: "squads/{squad_name}/tasks/{task_id}.md"
    delegated_workflow: "squads/squad-creator/workflows/wf-create-task.yaml"
    normalized_squad_name: "{squad_name}"
    inherited_context:
      source_framework: "{optional}"
      source_artifacts: ["optional artifacts"]
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] `pack_name` e `squad_name` são reconciliados corretamente
- [ ] A criação real da task é delegada ao workflow base
- [ ] Nenhuma fase paralela de create-task é definida no pro
- [ ] Workflows do pro que dependem de `create-task` continuam compatíveis
- [ ] Contexto adicional do pro é preservado sem duplicar a lógica do base

---

## Veto Conditions

- `squad-creator-pro` tentar executar pipeline próprio de create-task
- `squad_name` e `pack_name` apontarem para squads diferentes
- O workflow base `wf-create-task.yaml` não existir
- Algum chamador do pro depender de fase inventada que não exista no base

---

## Related Documents

- `squads/squad-creator/workflows/wf-create-task.yaml` -- owner canônico
- `squads/squad-creator/tasks/create-task.md` -- wrapper composto do base
- `workflows/wf-context-aware-create-squad.yaml` -- chamador do pro
- `workflows/wf-research-then-create-agent.yaml` -- chamador do pro

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed create-task output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
