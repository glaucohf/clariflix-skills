# Task: Create Complete Squad (Extension Contract Adapter)

**Task ID:** create-squad
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` sem manter um segundo monólito de criação, expondo apenas o contrato necessário para os workflows canônicos do pack
**Orchestrator:** @squad-chief
**Mode:** Workflow-owned
**Quality Standard:** Herdado dos workflows pro `wf-create-squad` e `wf-context-aware-create-squad`

---

## Purpose

Este arquivo continua local ao `squad-creator-pro` porque o workflow context-aware do pack o consome em ações internas específicas. Ao mesmo tempo, ele não deve mais carregar uma implementação end-to-end paralela de criação de squad.

**Regra não negociável:** a orquestração completa de criação de squad no pro pertence a:

- `workflows/wf-create-squad.yaml` -- entrypoint/router do pack
- `workflows/wf-context-aware-create-squad.yaml` -- execução greenfield/resume

O papel deste adapter é duplo:

1. manter compatibilidade para chamadas legadas a `create-squad`;
2. documentar e estabilizar o contrato interno usado por `wf-context-aware-create-squad`.

---

## Supported Invocation Modes

| Mode | When Used | Owner |
|------|-----------|-------|
| `delegate_full_creation` | Chamadas diretas ou legadas para criar um squad completo | `workflows/wf-create-squad.yaml` |
| `persist_creation_plan` | Fase interna do workflow context-aware | Este adapter + runtime `.aiox` |
| `enforce_native_scope_gate` | Fase interna do workflow context-aware | Este adapter + runtime `.aiox` |
| `create_architecture` | Fase interna do workflow context-aware | Este adapter + runtime `.aiox` |

---

## Canonical Owners

- `workflows/wf-create-squad.yaml` -- router principal do pack
- `workflows/wf-context-aware-create-squad.yaml` -- owner da execução context-aware
- `tasks/create-agent.md` -- criação de agentes no pro
- `tasks/create-task.md` -- wrapper para criação de tasks via base
- `tasks/create-workflow.md` -- wrapper para criação de workflows via base
- `tasks/optimize-workflow.md` -- otimização obrigatória pós-criação

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `domain` | string | No | Domínio do squad |
| `purpose` | string | No | Objetivo principal |
| `target_user` | string | No | Público-alvo |
| `use_cases` | list | No | Casos de uso principais |
| `mode` | string | No | `incremental`, `yolo` ou modo legado |
| `squad_name` | string | No | Nome canônico do squad |
| `pack_name` | string | No | Alias legado; deve ser normalizado para `squad_name` |
| `action` | string | No | `delegate_full_creation`, `persist_creation_plan`, `enforce_native_scope_gate`, `create_architecture` |
| `creation_plan_path` | path | No | Caminho para `creation-plan.yaml` |
| `prd_path` | path | No | Caminho para PRD do squad |
| `context_payload` | object | No | Discovery, decisões e runtime state já produzidos pelo workflow |

---

## Preconditions

- [ ] `workflows/wf-create-squad.yaml` existe
- [ ] `workflows/wf-context-aware-create-squad.yaml` existe
- [ ] O chamador entende se está pedindo delegação full ou uma ação interna específica
- [ ] O runtime `.aiox/squad-runtime/create-squad/{squad_name}/` pode ser persistido

---

## Workflow

### Step 1: Normalize Target Squad

```yaml
normalize_target:
  rules:
    - if: "squad_name is empty AND pack_name exists"
      then: "set squad_name = pack_name"
    - if: "action is empty"
      then: "set action = delegate_full_creation"
    - if: "both squad_name and pack_name exist AND differ"
      then: "block and reconcile target"
```

### Step 2: Route by Invocation Mode

```yaml
route_by_action:
  delegate_full_creation:
    owner: "workflows/wf-create-squad.yaml"
    rule: "Direct calls should route to the workflow router, not to a local monolith"
  internal_actions:
    allowed:
      - persist_creation_plan
      - enforce_native_scope_gate
      - create_architecture
    owner: "workflows/wf-context-aware-create-squad.yaml"
```

### Step 3: Internal Contract Actions

```yaml
internal_contracts:
  persist_creation_plan:
    responsibilities:
      - "Persist creation-plan.yaml before any artifact creation"
      - "Emit or update docs/projects/{squad_name}/prd.md when required"
      - "Record complete artifact checklist for later resume"
    outputs:
      - ".aiox/squad-runtime/create-squad/{squad_name}/creation-plan.yaml"
      - "docs/projects/{squad_name}/prd.md"

  enforce_native_scope_gate:
    responsibilities:
      - "Apply thresholds for epic/PRD gating"
      - "Block premature creation when scope exceeds guardrails"
      - "Persist gate decision in runtime state"
    outputs:
      - ".aiox/squad-runtime/create-squad/{squad_name}/state.json"
      - "docs/projects/{squad_name}/epics/"

  create_architecture:
    responsibilities:
      - "Compare at least two sequencing alternatives"
      - "Stress-test dependencies and not-before conditions"
      - "Persist architecture rationale and workspace integration contract"
    outputs:
      - ".aiox/squad-runtime/create-squad/{squad_name}/workspace-integration-level.yaml"
      - ".aiox/squad-runtime/create-squad/{squad_name}/architecture-decision-record.yaml"
```

### Step 4: Downstream Creation Ownership

```yaml
downstream_creation:
  note: >
    Este adapter não cria agentes, tasks ou workflows diretamente. Quando a
    criação completa é aprovada, o workflow canônico do pro delega para:
      - create-agent.md
      - create-task.md
      - create-workflow.md
      - optimize-workflow.md
      - modules de integration e quality gates
  prohibition:
    - "Do NOT reintroduce local end-to-end creation phases here"
    - "Do NOT duplicate agent/task/workflow generation logic in this file"
```

---

## Output

```yaml
output:
  name: create_squad_contract_result
  format: yaml
  structure:
    action: "{action}"
    normalized_squad_name: "{squad_name}"
    owner:
      delegate_full_creation: "workflows/wf-create-squad.yaml"
      internal_actions: "workflows/wf-context-aware-create-squad.yaml"
    emitted_artifacts:
      - ".aiox/squad-runtime/create-squad/{squad_name}/*"
      - "docs/projects/{squad_name}/*"
    status: "delegated-or-contracted"
```

---

## Acceptance Criteria

- [ ] Chamadas diretas a `create-squad` são roteadas para `wf-create-squad.yaml`
- [ ] As três ações internas usadas por `wf-context-aware-create-squad` estão explicitamente documentadas
- [ ] Nenhum pipeline end-to-end paralelo permanece neste arquivo
- [ ] Ownership de criação downstream fica explícito em `create-agent`, `create-task`, `create-workflow` e `optimize-workflow`
- [ ] `squad-creator-pro` continua operando como extensão do base, não como implementação paralela

---

## Veto Conditions

- `create-squad.md` tentar recriar localmente o fluxo completo de greenfield/resume
- `squad_name` e `pack_name` apontarem para squads diferentes
- `workflows/wf-create-squad.yaml` ou `workflows/wf-context-aware-create-squad.yaml` não existirem
- Algum chamador depender de fases antigas de criação completa que hoje pertencem ao workflow canônico

---

## Related Documents

- `workflows/wf-create-squad.yaml` -- router principal do pack
- `workflows/wf-context-aware-create-squad.yaml` -- owner context-aware
- `tasks/create-agent.md` -- criação de agentes no pro
- `tasks/create-task.md` -- wrapper delegado ao base
- `tasks/create-workflow.md` -- wrapper delegado ao base
- `tasks/optimize-workflow.md` -- otimização obrigatória pós-criação
- `squads/squad-creator/tasks/create-squad.md` -- versão composta do base, sem as responsabilidades específicas do pack

---

_Task Version: 3.0.0_
_Role: compatibility contract adapter for upgrade-pack orchestration_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed create-squad output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
