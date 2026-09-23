# Task: Optimize - Hybrid Executor

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-hybrid-executor` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-hybrid-executor
name: "Optimize Hybrid Executor"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Projeta a conversao para Worker ou Hybrid, inventaria scripts existentes e define o minimo prompt residual do agente."
```

## Purpose

Executar a parte de implementação que move trabalho determinístico para script e deixa no agente apenas o que ainda exige interpretação.

## Inputs

```yaml
inputs:
  priority_matrix:
    type: object
    required: true
  target_files:
    type: array
    required: true
```

## Workflow / Steps

### Step 1: Inventariar scripts existentes

- Reusar scripts antes de criar novos.
- Detectar onde a task já pode virar wrapper.

### Step 2: Projetar conversão

- Definir o que vai para Worker script.
- Definir o prompt mínimo residual do Agent/Hybrid.

### Step 3: Emitir plano de implementação

- Produzir diff plan, paths afetados e backup requirement.

## Output

```yaml
output:
  schema:
    worker_conversion_plan: []
    hybrid_prompt_minimization: []
    backup_requirements: []
```

## Acceptance Criteria

- [ ] Cada conversão prioriza script-first
- [ ] Nenhuma mudança destrutiva é proposta sem backup requirement explícito

## Related Documents

- `optimize.md`
- `optimize-gap-zero.md`
- `optimize-empirical-validation.md`
