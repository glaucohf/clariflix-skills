---
task-id: etd-decision-architecture
name: "ETD Phase 3: Arquitetura de Decisão"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
model_rationale: "Mapear pipeline de decisão requer síntese de padrões cognitivos complexos"
estimated-time: 15 min
complexity: medium
parent_task: extract-thinking-dna

inputs:
  required:
    - mind_name: "Nome do expert a clonar"
    - domain: "Area de expertise"
    - sources: "Fontes validadas com metodologia documentada"

outputs:
  primary:
    - decision_architecture_yaml: "Bloco YAML com decision_pipeline, decision_weights, risk_profile"

elicit: true
---

# ETD Phase 3: Arquitetura de Decisao

> **Objetivo:** Mapear COMO o expert processa decisoes complexas -- pipeline, pesos e perfil de risco.
>
> **Tempo estimado:** 15 minutos

---

## Step 1: Pipeline de Decisao

Como o expert processa uma decisao complexa, passo a passo?

```yaml
decision_pipeline:
  name: ""
  stages:
    - stage: "Input"
      action: "O que coleta primeiro"

    - stage: "Analysis"
      action: "Como analisa"
      frameworks_used: []

    - stage: "Options"
      action: "Como gera alternativas"

    - stage: "Selection"
      action: "Como escolhe"
      criteria: []

    - stage: "Validation"
      action: "Como verifica a decisao"
```

**Perguntas-guia:**
- "Qual a primeira coisa que faz ao receber um problema?"
- "Como analisa as opções disponíveis?"
- "Que critérios usa para a escolha final?"
- "Como valida que a decisão foi correta?"

**Elicit:** Apresente o pipeline mapeado e peça validação.

---

## Step 2: Criterios de Decisao (Pesos)

O que pesa mais nas decisoes deste expert?

```yaml
decision_weights:
  - criterion: ""
    weight: "alto|medio|baixo"
    rationale: ""

# Exemplo Dan Kennedy:
decision_weights:
  - criterion: "ROI mensuravel"
    weight: "alto"
    rationale: "Se nao pode medir, nao faca"
  - criterion: "Velocidade de implementacao"
    weight: "alto"
    rationale: "Dinheiro ama velocidade"
  - criterion: "Perfeicao"
    weight: "baixo"
    rationale: "Done > Perfect"
```

---

## Step 3: Risk Profile

Como o expert lida com risco?

```yaml
risk_profile:
  tolerance: "alto|medio|baixo"

  risk_seeking_domains:
    - domain: ""
      behavior: "arrisca mais quando..."

  risk_averse_domains:
    - domain: ""
      behavior: "conservador quando..."

  risk_mitigation:
    - strategy: ""
      when: ""
```

**Perguntas-guia:**
- "Em que situações arrisca mais?"
- "Quando fica conservador?"
- "Que estratégias de mitigação usa?"

---

## Output

Entregue bloco YAML completo contendo:
- decision_pipeline com 3-5 stages
- 3+ decision_weights com rationale
- risk_profile com tolerance, risk_seeking, risk_averse, mitigation

---

## Quality Check

- [ ] Pipeline de decisão com 3+ stages mapeados
- [ ] 3+ critérios de decisão com peso e rationale
- [ ] Risk profile com tolerance definido
- [ ] Risk seeking e risk averse domains documentados
- [ ] Pipeline referencia frameworks extraídos na Phase 1

**Score mínimo:** 4/5 items checked

## Task Anatomy

- **Executor:** Agent
- **Inputs:** mind_name; domain; sources
- **Outputs:** Bloco YAML com decision_pipeline, decision_weights, risk_profile
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified

## Acceptance Criteria

- [ ] Output artifact produced: Bloco YAML com decision_pipeline, decision_weights, risk_profile
- [ ] Task output validated against quality standards
