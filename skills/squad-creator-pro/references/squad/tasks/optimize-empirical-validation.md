# Task: Optimize - Empirical Validation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-empirical-validation` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-empirical-validation
name: "Optimize Empirical Validation"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Roda o preflight/script, compara com baseline e salva o teste empírico da task otimizada."
```

## Purpose

Validar empiricamente se a otimização proposta realmente funciona. Esta task cobre a parte do monólito que executa script, compara baseline e salva test case.

## Inputs

```yaml
inputs:
  gap_zero_patch_plan:
    type: object
    required: true
  target_files:
    type: array
    required: true
```

## Workflow / Steps

### Step 1: Executar superfície otimizada

- Rodar preflight/script do Worker.
- Rodar comparação rápida com baseline quando aplicável.

### Step 2: Registrar evidência

- Salvar test case, resultado e divergências.
- Produzir relatório empírico por target otimizado.

## Output

```yaml
output:
  schema:
    empirical_results: []
    saved_test_cases: []
    validation_report: []
```

## Acceptance Criteria

- [ ] Toda otimização implementada tem evidência empírica
- [ ] Test case ou payload equivalente é preservado para rerun

## Related Documents

- `optimize.md`
- `optimize-bias-test.md`
- `optimize-post-economy.md`
