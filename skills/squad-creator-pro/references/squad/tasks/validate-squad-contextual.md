# Task: Validate Squad - Contextual

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-contextual` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: validate-squad-contextual
name: "Validate Squad Contextual"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Aplica validacao especifica ao tipo detectado do squad: expert, pipeline ou hybrid."
```

## Purpose

Avaliar se o squad e bom para o tipo de sistema que ele afirma ser. Nao existe validacao unica para todos os perfis.

## Inputs

```yaml
inputs:
  detected_type:
    type: string
    required: true
  squad_name:
    type: string
    required: true
  squad_path:
    type: string
    required: false
    default: "squads/{squad_name}/"
```

## Workflow / Steps

### Expert

- Validar `voice_dna`, exemplos, objecoes e organizacao por tiers.

### Pipeline

- Validar definicao de workflow, checkpoints, outputs intermediarios e completude do orquestrador.

### Hybrid

- Validar `persona_profile`, `behavioral_states`, heuristicas, process standards e modelo de executor/fallback.

## Output

```yaml
output:
  schema:
    squad_type: "expert | pipeline | hybrid"
    score: 0.0
    checks: {}
    issues: []
```

## Acceptance Criteria

- [ ] O output muda conforme o tipo detectado
- [ ] O score e calculado com criterios especificos do tipo
- [ ] Issues mostram o gap contextual real do squad

## Related Documents

- `validate-squad.md`
- `validate-squad-type-detect.md`
- `validate-squad-veto.md`
