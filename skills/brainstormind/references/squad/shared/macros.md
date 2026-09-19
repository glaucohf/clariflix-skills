# Shared Macros — Brain Squad

> Leia este arquivo UMA VEZ. Todas as regras de naming, formato e validacao estao aqui.

---

## {{NAMING_RULES}}

| Elemento | Convencao | Padrao | Exemplo |
|----------|-----------|--------|---------|
| Agent ID | kebab-case | `{id}` no manifesto | `filter-ranker` |
| Agent filename | `{id}.md` | Match agent.id | `filter-ranker.md` |
| Agent name | PascalCase | YAML `agent.name` | `FilterRanker` |
| Task identifier | camelCase() | Exato do registro | `filterAndRank()` |
| Task filename | kebab-case.md | Do registro de tasks | `filter-and-rank.md` |
| Workflow name | snake_case | YAML field | `brain_pipeline` |
| Workflow filename | kebab-case.yaml | Nomeado como acima | `brain-pipeline.yaml` |
| Command names | `*kebab-case` | YAML commands array | `*generate-ideas` |
| Input/Output fields | camelCase | YAML Entrada/Saida | `topicText` |

---

## {{ARCHETYPE_TABLE}}

| Archetype | Quando usar | Tom tipico |
|-----------|-------------|------------|
| Builder | Cria artefatos (ideias, documentos) | creative, collaborative |
| Guardian | Valida, filtra, ranqueia | analytical, assertive |
| Balancer | Otimiza, prioriza, reconcilia | pragmatic, strategic |
| Flow_Master | Orquestra, coordena fluxo | strategic, collaborative |

---

## {{AGENT_FORMAT}}

```yaml
---
agent:
  name: "{PascalCase}"
  id: "{kebab-case}"
  title: "{Titulo Profissional}"
  icon: "{emoji}"
  whenToUse: "{caso de uso especifico}"

persona_profile:
  archetype: "{Builder|Guardian|Balancer|Flow_Master}"
  communication:
    tone: "{tom da lista}"

persona:
  role: "{descricao de 1 linha}"
  core_principles:
    - "{principio 1}"
    - "{principio 2}"
  responsibility_boundaries:
    - "Handles: {o que faz}"
    - "Delegates: {o que outros fazem}"

commands:
  - name: "*{command-name}"
    visibility: squad
    description: "{o que faz}"

dependencies:
  tasks: ["{task-file}.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---
```

---

## {{TASK_FORMAT}}

```yaml
---
task: {camelCase}()
responsavel: "{AgentName}"
responsavel_type: Agente
atomic_layer: {Atom|Molecule|Organism}

Entrada:
  - nome: {fieldName}
    tipo: {type}
    descricao: "{origem} -> {destino}"
    obrigatorio: true

Saida:
  - nome: {fieldName}
    tipo: {type}
    descricao: "{task ou agente consumidor}"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] {condicao}"
  post-conditions:
    - "[ ] {condicao}"
---
```

---

## {{WORKFLOW_FORMAT}}

```yaml
workflow_name: snake_case
description: "{proposito}"

agent_sequence:
  - {agent-id-1}
  - {agent-id-2}

key_commands:
  - "*{main-command}"

trigger_threshold: 1
typical_duration: "N-M minutes"

success_indicators:
  - "{condicao observavel}"

transitions:
  {phase_name}:
    trigger: "{condicao de completude}"
    confidence: 0.90
    next_steps:
      - command: "*{next-command}"
        description: "{o que acontece}"
        priority: 1
```

---

## {{MODEL_ROUTING}}

| Nivel | Modelo | Quando usar |
|-------|--------|-------------|
| low | haiku | Geracao de itens, saida previsivel, 1-2 passos |
| medium | sonnet | Filtragem, ranking, sintese, 3-5 passos |
| high | opus | Orquestracao, facilitacao de design, 6+ passos |

---

## {{FILE_CONTRACTS}}

Todos os dados transitam por arquivos em `.brainstorm-tmp/`:

| Arquivo | Produtor | Consumidor |
|---------|----------|------------|
| `topic.txt` | Orchestrador | Todos |
| `r1/agent-{N}.txt` | IdeaGenerator x10 | FilterRanker |
| `top10.json` | FilterRanker | IdeaGenerator R2 |
| `top10_summary.txt` | FilterRanker | Orchestrador |
| `r2/agent-{N}.txt` | IdeaGenerator x10 | FilterRanker |
| `top3.json` | FilterRanker | Synthesizer, DesignFacilitator |
| `final_output.md` | Synthesizer | Orchestrador |
| `selected_insight.json` | Orchestrador | DesignFacilitator |
| `brain_report.md` | ReportBuilder | Usuario |
