# Task: Upgrade Squad - Inventory

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `upgrade-squad-inventory` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: upgrade-squad-inventory
name: "Upgrade Squad Inventory"
category: upgrade
agent: squad-chief
elicit: false
autonomous: true
description: "Wrapper fino sobre o inventário estrutural canônico do base, com leitura adicional dos sinais avançados que o pack pro precisa."
```

## Purpose

Executar primeiro o inventário estrutural definido em `squads/squad-creator/tasks/upgrade-squad-inventory.md`. Depois disso, enriquecer o output com sinais avançados do target: `workspace_integration`, `artifact_contracts`, `supported_modes`, `journey_log`, `model-routing`, `test-cases`, `minds/` e ativos de runtime.

## Workflow / Steps

### Step 1: Carregar o baseline herdado

- Ler `squads/squad-creator/tasks/upgrade-squad-inventory.md` por completo.
- Executar o inventário estrutural sem alterar os critérios do base.

### Step 2: Enriquecer para o overlay pro

- Detectar se o target já possui `workspace_integration`, `artifact_contracts` e `supported_modes`.
- Detectar presença de `minds/`, `config/model-routing.yaml`, `test-cases/` e ativos runtime em `.aiox/`.
- Marcar quais desses sinais são nativos, ausentes ou parciais.

## Output

```yaml
output:
  schema:
    structural_inventory: {}
    advanced_signals:
      workspace_contract: "missing | partial | present"
      artifact_contracts: "missing | partial | present"
      supported_modes: "missing | partial | present"
      journey_log: "missing | partial | present"
      model_routing: "missing | present"
      minds: "missing | present"
      runtime_assets: []
```

## Acceptance Criteria

- [ ] O task canônico do base é carregado antes do enriquecimento
- [ ] O inventário estrutural não é redefinido localmente
- [ ] O output já separa baseline estrutural de sinais avançados do pack

## Related Documents

- `squads/squad-creator/tasks/upgrade-squad-inventory.md`
- `upgrade-squad-gap.md`
