# Task: Optimize - Binary Checkpoints

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-binary-checkpoints` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-binary-checkpoints
name: "Optimize Binary Checkpoints"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Converte scoring subjetivo em checkpoints binários, thresholds e critérios calibrados."
```

## Purpose

Reduzir subjetividade operacional antes de qualquer migração de executor. Esta task ataca a parte do monólito focada em scores vagos, gates interpretativos e calibração mínima.

## Inputs

```yaml
inputs:
  binary_conversion_candidates:
    type: object
    required: true
  target_files:
    type: array
    required: true
```

## Workflow / Steps

### Step 1: Detectar scoring subjetivo

- Localizar `1-5`, `rate`, `avalie`, `score` sem threshold operacional.

### Step 2: Converter para binário

- Trocar julgamento vago por PASS/FAIL, YES/NO ou threshold mensurável.

### Step 3: Adicionar calibração mínima

- Registrar regra de decisão e fallback quando o critério falhar.

## Output

```yaml
output:
  schema:
    checkpoint_patch_plan: []
    calibrated_thresholds: []
```

## Acceptance Criteria

- [ ] Os candidatos binários viram critérios mensuráveis
- [ ] O patch plan preserva gates humanos legítimos

## Related Documents

- `optimize.md`
- `optimize-gatekeeper-detection.md`
- `checklists/quality-gate-checklist.md`
