# Task: Optimize Workflow - Cost Projection

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-cost-projection` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-workflow-cost-projection
name: "Optimize Workflow Cost Projection"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Calcula custo atual, custo otimizado e economia projetada para o workflow."
```

## Purpose

Executar a dimensão D6. Esta task transforma as análises anteriores em métrica de custo e priorização.

## Inputs

```yaml
inputs:
  executor_distribution_table:
    type: object
    required: true
  parallel_groups:
    type: object
    required: false
  cost:
    type: number
    required: false
    default: 10
```

## Workflow / Steps

### Step 1: Calcular custo atual

- Tokens e tempo por execução no estado atual.

### Step 2: Calcular custo otimizado

- Projeção com paralelização e redistribuição de executor.

## Output

```yaml
output:
  schema:
    current_cost: []
    optimized_cost: []
    monthly_projection: []
```

## Acceptance Criteria

- [ ] O before/after é calculado com premissas explícitas
- [ ] A projeção final é reutilizável pelo relatório e pelo modo `--implement`

## Related Documents

- `optimize-workflow.md`
- `optimize-workflow-report.md`
