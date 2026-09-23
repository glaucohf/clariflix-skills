# Task: Optimize Workflow - Load

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-load` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-workflow-load
name: "Optimize Workflow Load"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Resolve o target, carrega os workflows alvo e valida a estrutura mínima antes de qualquer análise."
```

## Purpose

Resolver `target` e produzir o inventário factual dos workflows a otimizar. Esta task impede otimização sobre YAML inválido ou alvo ambíguo.

## Inputs

```yaml
inputs:
  target:
    type: string
    required: true
  mode:
    type: string
    required: false
    default: scan
```

## Workflow / Steps

### Step 1: Resolver target

- Se `target` for arquivo, operar em um workflow.
- Se `target` for nome de squad, listar `workflows/*.yaml` do squad.

### Step 2: Carregar e validar

- Ler cada workflow por completo.
- Confirmar `workflow.id` e `sequence` ou estrutura equivalente.
- Registrar necessidade de backup para `--implement`.

## Output

```yaml
output:
  schema:
    resolved_scope: "single-workflow | squad"
    workflow_files: []
    structure_valid: true
    backups_required: true
```

## Acceptance Criteria

- [ ] O alvo é resolvido sem ambiguidade
- [ ] Workflows inválidos são bloqueados antes da análise

## Related Documents

- `optimize-workflow.md`
- `optimize-workflow-phase-necessity.md`
