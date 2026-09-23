# Task: Validate Squad - Structure

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-structure` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-structure
name: "Validate Squad Structure"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Valida config, entrypoint, diretorios obrigatorios e contratos estruturais do squad."
```

## Purpose

Executar o gate estrutural bloqueante antes de qualquer analise qualitativa. Esta task falha quando o squad nao tem a base minima para ser validado com seguranca.

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

### Step 1: Validar configuracao

- Confirmar que `config.yaml` existe e parseia.
- Verificar campos minimos: `name`, `version`, `description`.
- Validar convencoes basicas de nome e versao.

### Step 2: Validar entrypoint

- Verificar que o agente principal existe em `agents/`.
- Confirmar que o entrypoint tem `activation-instructions`.
- Verificar que o comando de ajuda existe ou que o agente tenha menu equivalente.

### Step 3: Validar estrutura minima

- `agents/` e obrigatorio.
- `tasks/`, `workflows/`, `checklists/` e `templates/` sao exigidos quando houver referencias a eles.
- `config/` e `schemas/` sao esperados quando o squad declara validacao formal.

## Output

```yaml
output:
  schema:
    status: "PASS | ABORT"
    config_valid: true
    entry_agent_exists: true
    entry_agent_activatable: true
    missing_directories: []
    blocking_issues: []
```

## Acceptance Criteria

- [ ] Squads sem `config.yaml` ou sem entrypoint sao bloqueados
- [ ] Diretorios exigidos por referencias existentes sao validados
- [ ] O output e deterministico e consumivel pelas fases seguintes

## Related Documents

- `validate-squad.md`
- `validate-squad-security.md`
- `validate-squad-cross-references.md`
