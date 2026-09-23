# Task: Validate Squad - Type Detect

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-type-detect` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-type-detect
name: "Validate Squad Type Detect"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Detecta o tipo do squad e carrega os requisitos contextuais que guiam as etapas seguintes da validacao."
```

## Purpose

Identificar se o squad e do tipo `expert`, `pipeline` ou `hybrid` usando sinais estruturais reais do diretorio, sem inferencia livre. O resultado desta task governa a validacao contextual e os vetos especificos.

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
  type_override:
    type: string
    required: false
```

## Workflow / Steps

### Step 1: Coletar sinais

- Contar arquivos em `agents/`, `tasks/` e `workflows/`.
- Verificar presenca de `voice_dna`, `behavioral_states`, heuristicas e organizacao por tiers.
- Verificar se o squad depende fortemente de workflow/orchestrator.

### Step 2: Aplicar regras de classificacao

```yaml
signals:
  expert:
    - "voice_dna presente em agentes"
    - "nomes de especialistas reais ou personas densas"
    - "organizacao por tiers orientada a especialistas"
  pipeline:
    - "workflows dominam a operacao"
    - "um orquestrador central coordena fases"
    - "tasks > agents * 3"
  hybrid:
    - "mistura de heuristicas, personas e pipelines"
    - "behavioral_states ou persona_profile presentes"
    - "executor/fallback logic presente"
```

### Step 3: Resolver empate

- `type_override` vence, se fornecido.
- Empate entre `expert` e `pipeline`: preferir `pipeline` quando o fluxo for o centro da operacao.
- Empate entre `pipeline` e `hybrid`: preferir `hybrid` quando houver heuristicas formais.

## Output

```yaml
output:
  schema:
    detected_type: "expert | pipeline | hybrid"
    confidence: 0.0
    signals:
      agents_count: N
      tasks_count: N
      workflows_count: N
      voice_dna_present: true
      heuristics_present: true
    requirements_profile:
      required_components: []
      veto_family: []
```

## Acceptance Criteria

- [ ] O tipo do squad e determinado usando sinais observaveis, nao intuicao
- [ ] `type_override` e respeitado quando informado
- [ ] O output inclui confianca e justificativa resumida
- [ ] O resultado pode ser consumido pelas tasks contextual e veto

## Related Documents

- `validate-squad.md`
- `validate-squad-contextual.md`
- `validate-squad-veto.md`
- `squads/squad-creator/data/squad-type-definitions.yaml`
