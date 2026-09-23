# Task: Validate Squad - Cross References

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-cross-references` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-cross-references
name: "Validate Squad Cross References"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Valida handoffs, referencias de tasks, templates e checklists para impedir links quebrados ou dependencias fantasma."
```

## Purpose

Garantir que as referencias internas do squad apontem para artefatos reais e coerentes. Esta task protege contra drift estrutural silencioso.

## Inputs

```yaml
inputs:
  squad_name:
    type: string
    required: true
  squad_path:
    type: string
    required: false
    default: "squads/{squad_name}/"
```

## Workflow / Steps

### Step 1: Handoffs

- Verificar se todos os `handoff_to` apontam para agentes existentes.

### Step 2: Task references

- Verificar se tasks referenciadas em workflows, agentes ou docs operacionais existem.

### Step 3: Template e checklist references

- Verificar paths de templates e checklists citados nas tasks.
- Tratar ausencias como warning quando nao forem gates bloqueantes.

## Output

```yaml
output:
  schema:
    status: "PASS | ABORT | WARN"
    broken_handoffs: 0
    broken_task_refs: []
    missing_templates: []
    missing_checklists: []
```

## Acceptance Criteria

- [ ] Handoffs quebrados bloqueiam a validacao
- [ ] Task refs invalidos sao listados com path ou id
- [ ] Templates/checklists ausentes ficam visiveis no output

## Related Documents

- `validate-squad.md`
- `validate-squad-coverage.md`
