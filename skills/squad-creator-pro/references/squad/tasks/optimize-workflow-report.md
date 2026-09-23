# Task: Optimize Workflow - Report

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-report` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-workflow-report
name: "Optimize Workflow Report"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Consolida D1-D6 em um relatório de otimização e backlog de implementação."
```

## Purpose

Fechar o modo `--scan` com um artefato único de decisão. Esta task junta necessidade de fases, paralelização, checkpoints, executor, GAP ZERO e custo.

## Inputs

```yaml
inputs:
  phase_necessity_table:
    type: object
    required: true
  parallel_groups:
    type: object
    required: false
  checkpoint_inventory:
    type: object
    required: false
  executor_distribution_table:
    type: object
    required: false
  monthly_projection:
    type: object
    required: false
```

## Workflow / Steps

### Step 1: Consolidar findings

- Unificar D1-D6.
- Priorizar recomendações.

### Step 2: Emitir relatório

- Gerar resumo executivo.
- Gerar fila do que entra em `--implement`.

## Output

```yaml
output:
  schema:
    optimization_report: []
    implementation_backlog: []
```

## Acceptance Criteria

- [ ] O relatório finaliza o modo scan
- [ ] A fila de implementação está ordenada por impacto e risco

## Related Documents

- `optimize-workflow.md`
- `optimize-workflow-apply.md`
