# Task: Squad Fusion - Structure

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-structure` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: squad-fusion-structure
name: "Squad Fusion Structure"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Executa o ETL load: cria a estrutura final do squad fusionado com config, assets e metadados de rastreabilidade."
```

## Purpose

Transformar o workspace temporário validado na estrutura final do squad fusionado, sem perder metadados de origem.

## Workflow / Steps

### Step 1: Criar o target final

- Materializar `squads/{target_name}/`.
- Escrever config, assets fusionados e arquivos obrigatórios.

### Step 2: Preservar rastreabilidade

- Registrar `final_counts`, `config_valid` e metadados de fusão.
- Garantir que README e artefatos de auditoria reflitam a fusão.

## Output

```yaml
output:
  schema:
    squad_path: string
    config_valid: true
    final_counts: {}
```

## Acceptance Criteria

- [ ] O target final é criado de forma determinística
- [ ] Config e contagens finais fecham com o workspace validado
- [ ] Metadados de fusão permanecem acessíveis
