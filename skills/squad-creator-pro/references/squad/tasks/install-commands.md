# Task: Install Squad Commands (Extension Wrapper)

**Task ID:** install-commands
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a instalação real de comandos ao workflow atômico do `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado do base workflow

---

## Purpose

Esta task mantém compatibilidade para chamadas do pro que ainda invocam `install-commands` diretamente.

O owner canônico do processo é:

- `squads/squad-creator/workflows/wf-install-commands.yaml`
- `squads/squad-creator/tasks/install-commands.md`

No `pro`, esta task não deve mais descrever um processo completo próprio.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `squad_name` | string | No | Nome canônico do squad alvo |
| `pack_name` | string | No | Alias legado do pro; deve virar `squad_name` |
| `ide` | string | No | IDE específica |
| `all_ides` | boolean | No | Instalar em todas as IDEs detectadas |
| `copy_mode` | boolean | No | Copiar em vez de symlink |
| `dry_run` | boolean | No | Pré-visualizar sem escrever |
| `uninstall` | boolean | No | Remover instalação |

---

## Preconditions

- [ ] `squads/squad-creator/workflows/wf-install-commands.yaml` existe
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

### Step 2: Delegate to Base Workflow

```yaml
delegate_to_base:
  workflow: "squads/squad-creator/workflows/wf-install-commands.yaml"
  payload:
    - squad_name
    - ide
    - all_ides
    - copy_mode
    - dry_run
    - uninstall
  prohibition:
    - "Do NOT maintain a parallel install-commands flow in squad-creator-pro"
```

### Step 3: Reconcile Outputs

```yaml
reconcile_outputs:
  return_shape:
    delegated_workflow: "squads/squad-creator/workflows/wf-install-commands.yaml"
    execution_mode: "base-delegated"
    normalized_squad_name: "{squad_name}"
```

---

## Output

```yaml
output:
  name: delegated_install_commands
  format: yaml
  structure:
    delegated_workflow: "squads/squad-creator/workflows/wf-install-commands.yaml"
    normalized_squad_name: "{squad_name}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] `pack_name` e `squad_name` são reconciliados corretamente
- [ ] A instalação real é delegada ao workflow base
- [ ] Nenhum processo paralelo de install-commands permanece no pro
- [ ] Chamadas existentes do pro continuam compatíveis

---

## Veto Conditions

- `squad_name` e `pack_name` apontarem para squads diferentes
- O workflow base `wf-install-commands.yaml` não existir
- O `pro` tentar manter regras locais incompatíveis com o fluxo base

---

## Related Documents

- `squads/squad-creator/workflows/wf-install-commands.yaml` -- owner canônico
- `squads/squad-creator/tasks/install-commands.md` -- wrapper composto do base

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed install-commands output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
