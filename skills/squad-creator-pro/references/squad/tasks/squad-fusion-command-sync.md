# Task: Squad Fusion - Command Sync

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-command-sync` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: squad-fusion-command-sync
name: "Squad Fusion Command Sync"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Sincroniza commands do squad fusionado com o ambiente de IDE e remove bindings antigos quando a fusão foi aprovada."
```

## Purpose

Garantir que o squad fusionado fique operacional no ambiente de execução, sem deixar comandos órfãos dos squads anteriores.

## Workflow / Steps

### Step 1: Sincronizar novos commands

- Gerar ou atualizar bindings do target final.
- Garantir que os commands apontem para o squad fusionado.

### Step 2: Limpar bindings antigos

- Remover ou desativar commands obsoletos dos squads fonte quando aplicável.
- Produzir `commands_synced` e `old_commands_removed`.

## Output

```yaml
output:
  schema:
    commands_synced: []
    old_commands_removed: []
```

## Acceptance Criteria

- [ ] O target final fica com commands operacionais
- [ ] Commands antigos só saem depois da aprovação da fusão
- [ ] O resultado do sync fica auditável
