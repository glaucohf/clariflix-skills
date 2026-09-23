# Task: Validate Squad - Veto

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-veto` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-veto
name: "Validate Squad Veto"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Executa vetos universais e vetos especificos por tipo. Qualquer veto encerra a validacao com FAIL."
```

## Purpose

Transformar regras nao negociaveis em decisao binaria. Score alto nao compensa falha estrutural.

## Inputs

```yaml
inputs:
  detected_type:
    type: string
    required: true
  structure_result:
    type: object
    required: true
  security_result:
    type: object
    required: true
  coverage_result:
    type: object
    required: true
  cross_reference_result:
    type: object
    required: true
  contextual_result:
    type: object
    required: true
```

## Workflow / Steps

### Step 1: Vetos universais

- Entry point ausente ou inativavel.
- Config invalido.
- Segredos expostos.
- Referencias criticas quebradas.

### Step 2: Vetos por tipo

- `expert`: ausencia total de `voice_dna` ou capacidade de diagnostico.
- `pipeline`: fluxo sem gate final ou cadeia quebrada de outputs.
- `hybrid`: ausencia de heuristicas/fallback.

## Output

```yaml
output:
  schema:
    status: "PROCEED | VETO"
    triggered_veto: null
    veto_message: null
    family: "universal | expert | pipeline | hybrid"
```

## Acceptance Criteria

- [ ] Vetos universais rodam antes dos vetos por tipo
- [ ] O primeiro veto encontrado encerra a task
- [ ] O motivo do veto fica claro e acionavel

## Related Documents

- `validate-squad.md`
- `validate-squad-contextual.md`
