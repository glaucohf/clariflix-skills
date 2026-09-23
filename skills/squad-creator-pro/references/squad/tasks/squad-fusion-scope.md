# Task: Squad Fusion - Scope

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-scope` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: squad-fusion-scope
name: "Squad Fusion Scope"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Aplica o escopo escolhido para manter apenas componentes coerentes com o domínio do squad fusionado."
```

## Purpose

Filtrar componentes fora do domínio ou desalinhados com o target, evitando um squad fusionado inflado e incoerente.

## Workflow / Steps

### Step 1: Aplicar política de escopo

- Interpretar `scope` como `full`, `filtered` ou `manual`.
- Quando houver keywords, usar correspondência semântica e estrutural.

### Step 2: Fechar lista final

- Produzir `final_components` e `excluded_components`.
- Justificar exclusões com base em escopo, não em preferência subjetiva.

## Output

```yaml
output:
  schema:
    final_components: []
    excluded_components: []
```

## Acceptance Criteria

- [ ] O escopo aplicado é rastreável
- [ ] Os componentes finais são coerentes com o target
- [ ] As exclusões têm motivo explícito
