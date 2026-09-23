# Task: Squad Fusion -- Elicitation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-elicitation` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `interactive` |

## Metadata

```yaml
id: squad-fusion-elicitation
name: "Squad Fusion Elicitation"
category: fusion
agent: squad-chief
elicit: true
autonomous: false
description: "Coleta inputs do usuario para configurar a fusao: squads fonte, target, escopo, modo e confirmacao final."
```

## Purpose

Coletar todos os inputs necessarios para configurar uma operacao de Squad Fusion. Cinco steps sequenciais coletam squads fonte, nome do target, escopo de merge, modo de execucao e confirmacao final.

## Workflow / Steps

### Step 1: Identificar Squads Fonte

```yaml
elicit:
  id: step_1_sources
  question: "Quais squads deseja fundir?"
  type: multi_select
  options:
    source: "Listar squads disponiveis em squads/"
    display: "nome (agents: N, tasks: N)"
  validation:
    min: 2
    max: 10
    error_if_less: "Fusao requer pelo menos 2 squads"
  hints:
    - "Selecione squads com dominios similares para melhor resultado"
    - "Squads muito diferentes podem resultar em fusao inconsistente"
```

### Step 2: Definir Target

```yaml
elicit:
  id: step_2_target
  question: "Nome do squad resultante?"
  type: text
  default: "Sugerir baseado nos fontes (ex: traffic-masters)"
  validation:
    pattern: "^[a-z][a-z0-9-]*$"
    error: "Nome deve ser kebab-case"
  auto_suggest:
    - Analisar nomes dos fontes
    - Identificar dominio comum
    - Propor nome que representa uniao
```

### Step 3: Definir Escopo

```yaml
elicit:
  id: step_3_scope
  question: "Qual o escopo/dominio do squad fusionado?"
  type: select
  options:
    - label: "Full Merge - Manter todos os componentes"
      value: full
      description: "Combina tudo, ideal para squads complementares"
    - label: "Domain Filter - Filtrar por keywords"
      value: filtered
      description: "Apenas componentes que matcham keywords"
    - label: "Cherry Pick - Selecionar manualmente"
      value: manual
      description: "Voce escolhe cada componente"
  follow_up:
    if: filtered
    then:
      question: "Quais keywords definir o escopo?"
      type: text_array
      example: ["paid traffic", "meta ads", "google ads"]
```

### Step 4: Definir Modo de Execucao

```yaml
elicit:
  id: step_4_mode
  question: "Modo de execucao?"
  type: select
  options:
    - label: "YOLO (automatico, ~15-30 min)"
      value: yolo
      description: |
        - Decisoes automaticas para conflitos
        - Prefer newer version em duplicatas
        - Merge automatico de configs
        - Checkpoint apenas no final
    - label: "QUALITY (checkpoints, ~45-90 min)"
      value: quality
      description: |
        - Checkpoint em cada fase
        - Revisao humana de conflitos
        - Validacao manual de deduplicacao
        - Quality gate rigoroso
```

### Step 5: Confirmar Configuracao

```yaml
elicit:
  id: step_5_confirm
  question: "Confirmar configuracao?"
  type: confirm
  display: |
    RESUMO DA FUSAO

    Squads Fonte: {sources.join(', ')}
    Target: {target_name}
    Escopo: {scope}
    Modo: {mode}

    Componentes a fundir:
    - Agents: {total_agents} -> ~{estimated_agents}
    - Tasks: {total_tasks} -> ~{estimated_tasks}
    - Workflows: {total_workflows} -> ~{estimated_workflows}
  options:
    - "Confirmar e executar"
    - "Modificar configuracao"
    - "Cancelar"
```

## Output

```yaml
fusion_config:
  sources: ["{squad-a}", "{squad-b}", ...]
  target_name: "{target-name}"
  scope: "full | filtered | manual"
  scope_keywords: ["..."]  # only if scope=filtered
  mode: "yolo | quality"
  confirmed: true
```

## Acceptance Criteria

- [ ] All 5 elicitation steps presented in sequence
- [ ] Validation enforced: minimum 2 sources, kebab-case target name
- [ ] CLI argument bypass works when `--sources` and `--target` provided
- [ ] Confirmation summary accurately reflects collected inputs
- [ ] Cancel option aborts without side effects

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-SFU-001 | Fewer than 2 valid source squads selected | BLOCK. Provide at least two valid source squads. |

## Related Documents

- `squad-fusion.md` -- Parent stub task
- `squad-fusion-discovery.md` -- Next phase (Phase 1)
