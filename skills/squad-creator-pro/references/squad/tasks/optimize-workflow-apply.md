# Task: Optimize Workflow - Apply

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-apply` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-workflow-apply
name: "Optimize Workflow Apply"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Aplica mudanças estruturais aprovadas no workflow, exigindo backup e rastreabilidade das alterações."
```

## Purpose

Executar o modo `--implement`. Esta task aplica otimizações no YAML do workflow sem pular backup, diff plan ou rastreabilidade.

## Inputs

```yaml
inputs:
  implementation_backlog:
    type: object
    required: true
  workflow_files:
    type: array
    required: true
```

## Workflow / Steps

### Step 1: Confirmar pré-condições

- Backup existe.
- Scan foi concluído.

### Step 2: Aplicar otimizações

- Remover/merge de fases.
- Introduzir paralelização quando segura.
- Ajustar checkpoints e executor.

### Step 3: Atualizar versão

- Registrar versão e nota de otimização.

## Output

```yaml
output:
  schema:
    changed_workflows: []
    backup_paths: []
    version_updates: []
```

## Acceptance Criteria

- [ ] Nenhuma mudança é aplicada sem backup
- [ ] O diff estrutural fica rastreável por workflow

## Related Documents

- `optimize-workflow.md`
- `optimize-workflow-validate.md`
