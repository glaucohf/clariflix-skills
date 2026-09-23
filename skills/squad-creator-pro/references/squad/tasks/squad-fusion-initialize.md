# Task: Squad Fusion - Initialize

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-initialize` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: squad-fusion-initialize
name: "Squad Fusion Initialize"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Resolve sources/target, cria workspace temporário, backup path e audit log antes de qualquer leitura profunda."
```

## Purpose

Garantir que a fusão começa em ambiente controlado: fontes válidas, target resolvido, rollback preparado e trilha de auditoria aberta.

## Workflow / Steps

### Step 1: Validar entrada

- Confirmar `sources.length >= 2`.
- Confirmar que todos os squads fonte existem e são legíveis.
- Validar `target_name` em kebab-case.

### Step 2: Preparar runtime

- Gerar `fusion_id`, `workspace_path`, `backup_path` e `audit_log_path`.
- Registrar parâmetros de execução (`mode`, `dry_run`, `keep_sources`, `verbose`).

## Output

```yaml
output:
  schema:
    fusion_id: string
    workspace_path: string
    backup_path: string
    audit_log_path: string
    inputs_valid: true
```

## Acceptance Criteria

- [ ] Pelo menos duas fontes válidas foram confirmadas
- [ ] Workspace, backup e audit log foram definidos
- [ ] O processo bloqueia cedo quando houver input inválido
