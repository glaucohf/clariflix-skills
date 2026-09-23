# Task: Create Pipeline Scaffolding (Extension Wrapper)

**Task ID:** create-pipeline
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a criação real de pipeline scaffolding ao owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task base

---

## Purpose

Este wrapper existe porque `create-pipeline` no pro não deve manter uma implementação paralela do mesmo scaffolding já definido no base.

Além disso, os artefatos de referência para pipeline já pertencem ao base:

- `squads/squad-creator/data/pipeline-patterns.md`
- `squads/squad-creator/templates/pipeline-state-tmpl.py`
- `squads/squad-creator/templates/pipeline-progress-tmpl.py`
- `squads/squad-creator/templates/pipeline-runner-tmpl.py`
- `squads/squad-creator/tasks/create-pipeline.md`

O papel desta task é somente normalizar inputs e delegar.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `squad_name` | string | No | Nome canônico do squad alvo |
| `pack_name` | string | No | Alias legado do pro; deve virar `squad_name` |
| `phase_definitions` | list | Yes | Definições de fases do pipeline |
| `requirements` | object | No | Requisitos adicionais do pipeline |
| `item_noun` | string | No | Nome do item processado |

---

## Preconditions

- [ ] `squads/squad-creator/tasks/create-pipeline.md` existe
- [ ] Os templates de pipeline existem em `squads/squad-creator/templates/`
- [ ] O squad alvo existe em `squads/{squad_name}/` ou `squads/{pack_name}/`

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
```

### Step 2: Delegate to Base Task

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/create-pipeline.md"
  payload:
    - squad_name
    - phase_definitions
    - requirements
    - item_noun
  prohibition:
    - "Do NOT keep local references to removed pipeline templates inside squad-creator-pro"
    - "Do NOT fork pipeline scaffolding logic locally"
```

### Step 3: Reconcile Outputs

```yaml
reconcile_outputs:
  primary_outputs:
    - "squads/{squad_name}/lib/__init__.py"
    - "squads/{squad_name}/lib/pipeline_state.py"
    - "squads/{squad_name}/lib/progress.py"
    - "squads/{squad_name}/lib/phase_runner.py"
  return_shape:
    delegated_task: "squads/squad-creator/tasks/create-pipeline.md"
    execution_mode: "base-delegated"
```

---

## Output

```yaml
output:
  name: delegated_pipeline_creation
  format: yaml
  structure:
    delegated_task: "squads/squad-creator/tasks/create-pipeline.md"
    normalized_squad_name: "{squad_name}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] `pack_name` e `squad_name` são reconciliados corretamente
- [ ] A criação real do scaffolding é delegada ao base
- [ ] Nenhuma dependência quebrada de template/data permanece no pro
- [ ] Chamadas existentes do pro continuam compatíveis

---

## Veto Conditions

- `squad_name` e `pack_name` apontarem para squads diferentes
- A task base `create-pipeline.md` não existir
- O `pro` tentar manter scaffolding local divergente

---

## Related Documents

- `squads/squad-creator/tasks/create-pipeline.md` -- owner canônico
- `squads/squad-creator/data/pipeline-patterns.md` -- referência canônica

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed create-pipeline output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
