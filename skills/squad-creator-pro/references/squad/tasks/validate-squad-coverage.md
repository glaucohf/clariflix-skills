# Task: Validate Squad - Coverage

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-coverage` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-coverage
name: "Validate Squad Coverage"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Mede cobertura operacional do squad: checklists, tarefas orfas, fases, data files, registry e service catalog."
```

## Purpose

Verificar se o squad cobre o proprio escopo de forma minimamente sustentavel, antes da analise subjetiva de qualidade.

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
  detected_type:
    type: string
    required: true
```

## Workflow / Steps

### Step 1: Cobertura de checklists

- Calcular `checklists / tasks_complexas`.
- Usar threshold bloqueante quando a cobertura ficar abaixo do minimo aceito.

### Step 2: Cobertura de tasks e fases

- Detectar tasks orfas.
- Para squads `pipeline`, validar se toda fase relevante tem suporte operacional.

### Step 3: Cobertura de dados e integracoes

- Medir uso de arquivos em `data/`.
- Validar `data/tool-registry.yaml` quando aplicavel.
- Cruzar referencias de servicos contra o `service-catalog` central quando existirem.

## Output

```yaml
output:
  schema:
    status: "PASS | ABORT | WARN"
    metrics:
      checklist_coverage: "0%"
      orphan_tasks: 0
      phase_coverage: "N/A"
      data_usage: "0%"
      tool_registry: "PASS | WARN | N/A"
      service_catalog_compliance: "PASS | WARN | FAIL | N/A"
    issues: []
```

## Acceptance Criteria

- [ ] Checklist coverage e orphan detection sao medidos explicitamente
- [ ] Pipeline squads recebem validacao de cobertura por fases
- [ ] Service catalog compliance entra como parte do output
- [ ] Falhas bloqueantes sao separadas de warnings

## Related Documents

- `validate-squad.md`
- `validate-squad-cross-references.md`
- `data/tool-registry.yaml`
