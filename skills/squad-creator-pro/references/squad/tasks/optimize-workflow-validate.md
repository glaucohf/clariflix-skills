# Task: Optimize Workflow - Validate

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-validate` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-workflow-validate
name: "Optimize Workflow Validate"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Valida sintaxe, alcançabilidade e integridade estrutural do workflow otimizado antes do handoff final."
```

## Purpose

Fechar o modo `--implement` com validação determinística. Esta task garante que o workflow otimizado ainda parseia, continua alcançável e não introduziu ciclo ou ruptura.

## Inputs

```yaml
inputs:
  changed_workflows:
    type: object
    required: true
```

## Workflow / Steps

### Step 1: Validar YAML

- Confirmar parse do arquivo.

### Step 2: Validar estrutura

- Estados alcançáveis.
- Sequência coerente.
- Sem referência quebrada evidente.

## Output

```yaml
output:
  schema:
    validation_results: []
    rollback_required: false
```

## Acceptance Criteria

- [ ] Workflow otimizado parseia
- [ ] Falhas estruturais bloqueiam fechamento e sinalizam rollback

## Related Documents

- `optimize-workflow.md`
- `optimize-workflow-apply.md`
