# Task: Optimize Workflow - Checkpoints

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-checkpoints` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-workflow-checkpoints
name: "Optimize Workflow Checkpoints"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Inventaria checkpoints, distingue gates humanos legítimos de gates heurísticos e produz plano de conversão."
```

## Purpose

Executar a dimensão D3. Esta task reduz checkpoints humanos desnecessários sem remover gates críticos.

## Inputs

```yaml
inputs:
  workflow_files:
    type: array
    required: true
```

## Workflow / Steps

### Step 1: Inventariar checkpoints

- Localizar `checkpoint`, `approval_required`, `human_review`, `gate`.

### Step 2: Classificar

- `KEEP_HUMAN`
- `HEURISTIC_CANDIDATE`
- `REMOVE_IF_REDUNDANT`

## Output

```yaml
output:
  schema:
    checkpoint_inventory: []
    heuristic_conversion_candidates: []
    human_gate_exceptions: []
```

## Acceptance Criteria

- [ ] Todo checkpoint encontrado recebe destino explícito
- [ ] Gates humanos críticos são preservados

## Related Documents

- `optimize-workflow.md`
- `checklists/quality-gate-checklist.md`
