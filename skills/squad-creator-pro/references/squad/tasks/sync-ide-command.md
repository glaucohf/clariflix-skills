# Task: Sync IDE Command (Extension Wrapper)

**Task ID:** sync-ide-command
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a sincronização real de comandos para o owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task e do worker script base

---

## Purpose

Este wrapper existe para manter compatibilidade com comandos e handoffs do `squad-creator-pro` que ainda chamam `sync-ide-command` diretamente.

**Regra não negociável:** a lógica de sincronização multi-IDE não deve ser mantida em paralelo no pro quando o comportamento é o mesmo do base.

Owners canônicos:

- `squads/squad-creator/tasks/sync-ide-command.md`
- `squads/squad-creator/scripts/sync-ide-command.py`

O papel deste wrapper é apenas:

1. normalizar inputs legados do pro;
2. reconciliar `pack_name` com `squad_name` quando necessário;
3. delegar a sincronização para a task e o script canônicos do base;
4. devolver o resultado no formato esperado pelos chamadores do pro.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | enum | Yes | `agent`, `task`, `workflow` ou `squad` |
| `name` | string | Yes | Nome do componente a sincronizar |
| `squad_name` | string | No | Nome canônico do squad alvo |
| `pack_name` | string | No | Alias legado usado no pro; deve virar `squad_name` |
| `ides` | list | No | IDEs alvo |
| `dry_run` | boolean | No | Executa preview sem escrever |
| `force` | boolean | No | Permite sobrescrita |

---

## Preconditions

- [ ] `squads/squad-creator/tasks/sync-ide-command.md` existe
- [ ] `squads/squad-creator/scripts/sync-ide-command.py` existe
- [ ] O chamador entende que este wrapper não possui engine própria de sync

---

## Workflow

### Step 1: Normalize Target

```yaml
normalize_target:
  rules:
    - if: "squad_name is empty AND pack_name exists"
      then: "set squad_name = pack_name"
    - if: "both squad_name and pack_name exist AND differ"
      then: "block and reconcile target"
```

### Step 2: Delegate to Base

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/sync-ide-command.md"
  worker_script: "squads/squad-creator/scripts/sync-ide-command.py"
  payload:
    - type
    - name
    - squad_name
    - ides
    - dry_run
    - force
  prohibition:
    - "Do NOT maintain a second sync methodology in squad-creator-pro"
    - "Do NOT fork IDE destination rules locally"
```

### Step 3: Reconcile Outputs

```yaml
reconcile_outputs:
  return_shape:
    delegated_task: "squads/squad-creator/tasks/sync-ide-command.md"
    delegated_script: "squads/squad-creator/scripts/sync-ide-command.py"
    normalized_squad_name: "{squad_name}"
    execution_mode: "base-delegated"
```

---

## Output

```yaml
output:
  name: delegated_sync
  format: yaml
  structure:
    delegated_task: "squads/squad-creator/tasks/sync-ide-command.md"
    delegated_script: "squads/squad-creator/scripts/sync-ide-command.py"
    normalized_squad_name: "{squad_name}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] `pack_name` e `squad_name` são reconciliados corretamente
- [ ] A sincronização real é delegada ao base
- [ ] Nenhuma engine paralela de sync permanece no pro
- [ ] Chamadas existentes do pro continuam compatíveis

---

## Veto Conditions

- `squad_name` e `pack_name` apontarem para squads diferentes
- A task ou o worker script base não existirem
- O pro tentar redefinir regras de destino ou formato que já pertencem ao base

---

## Related Documents

- `squads/squad-creator/tasks/sync-ide-command.md` -- owner canônico
- `squads/squad-creator/scripts/sync-ide-command.py` -- execução determinística

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed sync-ide-command output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
