# Task: Optimize - Gatekeeper Detection

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-gatekeeper-detection` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-gatekeeper-detection
name: "Optimize Gatekeeper Detection"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Detecta padroes de gatekeeper, checkpoints subjetivos e dependencias humanas mal posicionadas antes da implementacao."
```

## Purpose

Separar o que é validação legítima do que é gargalo humano desnecessário. Esta task governa conversões de checkpoint e impede automação insegura.

## Inputs

```yaml
inputs:
  analysis_table:
    type: object
    required: true
  scope_patch_plan:
    type: object
    required: false
```

## Workflow / Steps

### Step 1: Detectar gatekeepers

- Procurar scores subjetivos, checkpoints vagos e aprovações humanas sem threshold.
- Identificar where a human gate is structural versus accidental.

### Step 2: Qualificar o gate

- Manter gates realmente críticos.
- Marcar gates convertíveis para binário ou heurístico.
- Preparar lista de conversão para as phases seguintes.

## Output

```yaml
output:
  schema:
    gatekeeper_findings: []
    binary_conversion_candidates: []
    human_gate_exceptions: []
```

## Acceptance Criteria

- [ ] Todo gate identificado tem rationale
- [ ] Candidatos a conversão binária ficam separados de gates humanos legítimos

## Related Documents

- `optimize.md`
- `optimize-binary-checkpoints.md`
- `checklists/quality-gate-checklist.md`
