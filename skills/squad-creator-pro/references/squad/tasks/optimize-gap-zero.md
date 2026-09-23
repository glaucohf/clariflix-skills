# Task: Optimize - Gap Zero

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-gap-zero` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-gap-zero
name: "Optimize Gap Zero"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Aplica EXECUTE FIRST, INPUT REQUIRED e vetos estruturais para eliminar gaps entre handoff e execução."
```

## Purpose

Garantir que a task otimizada já nasça operacionalmente fechada. Esta task cuida da parte de GAP ZERO do monólito original.

## Inputs

```yaml
inputs:
  worker_conversion_plan:
    type: object
    required: true
  backup_requirements:
    type: object
    required: false
```

## Workflow / Steps

### Step 1: Inserir blocos de execução

- Adicionar `EXECUTE FIRST` quando houver preflight obrigatório.
- Declarar `INPUT REQUIRED` quando o output de script for insumo mandatório.

### Step 2: Adicionar vetos e versão

- Registrar veto conditions necessárias.
- Atualizar versão da task quando a conversão alterar o contrato.

## Output

```yaml
output:
  schema:
    gap_zero_patch_plan: []
    added_vetos: []
    version_updates: []
```

## Acceptance Criteria

- [ ] Nenhum preflight mandatório fica implícito
- [ ] Os vetos necessários ficam materializados antes da validação empírica

## Related Documents

- `optimize.md`
- `optimize-empirical-validation.md`
