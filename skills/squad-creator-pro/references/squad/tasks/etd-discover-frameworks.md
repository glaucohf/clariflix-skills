---
task-id: etd-discover-frameworks
name: "ETD Phase 1: Descoberta de Frameworks"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
model_rationale: "Síntese de frameworks requer interpretação profunda de múltiplas fontes"
estimated-time: 20 min
complexity: medium
parent_task: extract-thinking-dna

inputs:
  required:
    - mind_name: "Nome do expert a clonar"
    - domain: "Area de expertise"
    - sources: "Fontes validadas com metodologia documentada"

outputs:
  primary:
    - frameworks_yaml: "Bloco YAML com primary_framework, secondary_frameworks, diagnostic_framework"

elicit: true
---

# ETD Phase 1: Descoberta de Frameworks

> **Objetivo:** Identificar os frameworks operacionais do expert -- o "sistema operacional" mental.
>
> **Tempo estimado:** 20 minutos

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-DF-001 | Sources must contain methodology content for framework extraction | Verify at least 3 sources describe processes or methodologies | VETO - BLOCK. Insufficient methodology content in sources. |

---

## Step 1: Framework Principal (O "Sistema Operacional")

Todo expert tem UM framework que usa para TUDO. Encontre-o.

**Perguntas para identificar:**
- "Qual processo ele SEMPRE segue?"
- "O que ele ensina primeiro para iniciantes?"
- "Se pudesse ensinar apenas UMA coisa, o que seria?"

```yaml
primary_framework:
  name: ""                    # Nome do framework
  creator: "{mind_name}"      # Quem criou
  acronym: ""                 # Se tiver (AIDA, PASTOR, etc)
  purpose: ""                 # Para que serve

  steps:
    - step: 1
      name: ""
      action: ""
      output: ""
    - step: 2
      name: ""
      action: ""
      output: ""
    # ... continue

  when_to_use: ""
  when_NOT_to_use: ""

  evidence:
    - source: ""
      quote: ""
```

**Elicit:** Apresente o framework encontrado e peça validação antes de avançar.

---

## Step 2: Frameworks Secundários (2-4)

Outros frameworks que usa para situações específicas.

```yaml
secondary_frameworks:
  - name: ""
    purpose: ""
    steps: []
    trigger: "quando usar"
```

**Perguntas-guia:**
- "Que processos alternativos usa para situações diferentes?"
- "Quando abandona o framework principal?"
- "Que métodos secundários complementam o principal?"

---

## Step 3: Framework de Diagnóstico

Como o expert AVALIA uma situação antes de agir?

```yaml
diagnostic_framework:
  name: ""
  questions:
    - "Primeira pergunta que faz"
    - "Segunda pergunta"
    - "Terceira pergunta"
  red_flags: ["sinais de problema"]
  green_flags: ["sinais positivos"]
```

**Perguntas-guia:**
- "Quais são as 3 primeiras perguntas que faz ao avaliar algo novo?"
- "Que sinais indicam que algo vai dar errado?"
- "Que sinais indicam que está no caminho certo?"

---

## Output

Entregue bloco YAML completo contendo:
- primary_framework com 3+ steps e evidence
- 2-4 secondary_frameworks com triggers
- diagnostic_framework com questions, red_flags, green_flags

---

## Quality Check

- [ ] Framework principal com 3+ steps claros
- [ ] Framework principal tem evidence (source + quote)
- [ ] 2+ frameworks secundários com trigger definido
- [ ] Framework de diagnóstico com 3+ questions
- [ ] Red flags e green flags preenchidos

**Score mínimo:** 4/5 items checked

## Task Anatomy

- **Executor:** Agent
- **Inputs:** mind_name; domain; sources
- **Outputs:** Bloco YAML com primary_framework, secondary_frameworks, diagnostic_framework
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] All veto conditions checked and none triggered
- [ ] Output artifact produced: Bloco YAML com primary_framework, secondary_frameworks, diagnostic_framework
- [ ] Task output validated against quality standards
