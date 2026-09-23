# Task: Optimize - ROI Report

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-roi-report` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-roi-report
name: "Optimize ROI Report"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Consolida análise, estima custo atual vs futuro e emite o relatório de priorização e implementação."
```

## Purpose

Transformar a análise em plano executável. Esta task calcula ROI e organiza a fila do que deve ser convertido primeiro.

## Inputs

```yaml
inputs:
  analysis_table:
    type: object
    required: true
  scope_patch_plan:
    type: object
    required: false
  gatekeeper_findings:
    type: object
    required: false
```

## Workflow / Steps

### Step 1: Estimar custo e ganho

- Projetar custo atual por task.
- Projetar economia após Worker/Hybrid/binary checkpoint conversion.

### Step 2: Priorizar

- Ordenar por ROI, risco e facilidade de implementação.
- Separar recomendações para `scan`, `implement` e `hybrid`.

### Step 3: Emitir relatório

- Gerar relatório de análise e backlog de implementação.

## Output

```yaml
output:
  schema:
    roi_summary: []
    priority_matrix: []
    scan_report: "path or inline payload"
```

## Acceptance Criteria

- [ ] O relatório finaliza a fase de scan
- [ ] As recomendações têm ordem de prioridade e justificativa

## Related Documents

- `optimize.md`
- `optimize-hybrid-executor.md`
- `optimize-post-economy.md`
