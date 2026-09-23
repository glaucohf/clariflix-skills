# Task: Squad Fusion - Validation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-validation` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: squad-fusion-validation
name: "Squad Fusion Validation"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Roda quality gates antes da criação da estrutura final e decide se a fusão pode prosseguir sem degradar o sistema."
```

## Purpose

Validar integridade, consistência e qualidade do workspace intermediário antes da fase de carga final.

## Workflow / Steps

### Step 1: Rodar quality gates

- Validar integridade estrutural do workspace temporário.
- Verificar referências quebradas, conflitos pendentes e qualidade mínima.

### Step 2: Emitir decisão

- Produzir `validation_status`, `validation_report` e `issues_to_fix`.
- Em `quality`, exigir checkpoint humano quando necessário.

## Output

```yaml
output:
  schema:
    validation_status: "pass | warn | fail"
    validation_report: markdown
    issues_to_fix: []
```

## Acceptance Criteria

- [ ] A fusão não avança cegamente para a carga final
- [ ] O relatório diferencia warning de blocker
- [ ] O workflow sabe quando pedir checkpoint humano
