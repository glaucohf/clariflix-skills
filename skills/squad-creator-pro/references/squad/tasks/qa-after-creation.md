# Task: QA After Creation (Extension Wrapper)

**Task ID:** qa-after-creation
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega o QA pós-criação ao workflow atômico do `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado do base workflow

---

## Purpose

Esta task mantém compatibilidade com gatilhos e referências do `squad-creator-pro` para `qa-after-creation`.

O owner canônico do pipeline é:

- `squads/squad-creator/workflows/wf-qa-after-creation.yaml`
- `squads/squad-creator/tasks/qa-after-creation.md`

O `pro` não deve manter uma segunda implementação de QA pós-criação quando a estrutura já está padronizada no base.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `created_component` | string | Yes | Caminho do componente criado |
| `component_type` | enum | Yes | `squad`, `agent`, `task`, `workflow`, `template` |
| `creation_task` | string | No | Task que disparou o QA |
| `auto_fix` | boolean | No | Tentativa de auto-fix para issues menores |
| `specialist_context` | object | No | Contexto opcional vindo de workflows do pro |

---

## Preconditions

- [ ] `squads/squad-creator/workflows/wf-qa-after-creation.yaml` existe
- [ ] O componente alvo existe no path informado

---

## Workflow

### Step 1: Build Base QA Payload

```yaml
build_base_payload:
  required_fields:
    - created_component
    - component_type
  optional_fields:
    - creation_task
    - auto_fix
    - specialist_context
  rule: >
    O contexto adicional do pro pode enriquecer a interpretação do relatório,
    mas não cria um pipeline paralelo de QA.
```

### Step 2: Delegate to Base Workflow

```yaml
delegate_to_base:
  workflow: "squads/squad-creator/workflows/wf-qa-after-creation.yaml"
  payload:
    - created_component
    - component_type
    - creation_task
    - auto_fix
    - specialist_context
  prohibition:
    - "Do NOT maintain a second QA-after-creation implementation in squad-creator-pro"
```

### Step 3: Reconcile Outputs

```yaml
reconcile_outputs:
  return_shape:
    delegated_workflow: "squads/squad-creator/workflows/wf-qa-after-creation.yaml"
    execution_mode: "base-delegated"
    created_component: "{created_component}"
    component_type: "{component_type}"
```

---

## Output

```yaml
output:
  name: delegated_qa_after_creation
  format: yaml
  structure:
    delegated_workflow: "squads/squad-creator/workflows/wf-qa-after-creation.yaml"
    created_component: "{created_component}"
    component_type: "{component_type}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] O QA real é delegado ao workflow base
- [ ] Gatilhos existentes do pro continuam compatíveis
- [ ] Nenhuma segunda implementação de QA-after-creation permanece no pro
- [ ] O contexto adicional do pro pode ser carregado sem duplicar o pipeline

---

## Veto Conditions

- O workflow base `wf-qa-after-creation.yaml` não existir
- O componente informado não existir
- O `pro` tentar manter regras locais incompatíveis com o QA base

---

## Related Documents

- `squads/squad-creator/workflows/wf-qa-after-creation.yaml` -- owner canônico
- `squads/squad-creator/tasks/qa-after-creation.md` -- wrapper composto do base

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed qa-after-creation output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
