# Task: Optimize - Post Economy

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-post-economy` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-post-economy
name: "Optimize Post Economy"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Inventaria mudanças, calcula economia pós-refatoração e emite o before/after final da otimização."
```

## Purpose

Fechar a otimização com métrica de economia, breakdown por script e comparação consolidada. Esta task cobre a fase 8 do monólito original e o modo `--post`.

## Inputs

```yaml
inputs:
  empirical_results:
    type: object
    required: false
  bias_findings:
    type: object
    required: false
  roi_summary:
    type: object
    required: true
```

## Workflow / Steps

### Step 1: Inventariar mudanças

- Capturar arquivos tocados, executor anterior e executor final.

### Step 2: Calcular economia

- Recalcular custo projetado.
- Gerar before/after e breakdown por script ou task.

### Step 3: Emitir relatório final

- Consolidar economia, risco residual e próximos passos.

## Output

```yaml
output:
  schema:
    changed_files: []
    token_economics: []
    comparison_table: []
    final_economy_report: "path or inline payload"
```

## Acceptance Criteria

- [ ] O relatório final mostra antes, depois e economia projetada
- [ ] O modo `--post` consegue reutilizar artefatos anteriores sem reexecutar todo o pipeline

## Related Documents

- `optimize.md`
- `optimize-roi-report.md`
- `optimize-empirical-validation.md`
