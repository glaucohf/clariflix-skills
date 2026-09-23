---
task-id: etd-extract-heuristics
name: "ETD Phase 2: Extração de Heurísticas"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
model_rationale: "Heurísticas de decisão requerem síntese interpretativa de padrões implícitos"
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
    - heuristics_yaml: "Bloco YAML com decision_heuristics, veto_heuristics, prioritization_heuristics"

elicit: true
---

# ETD Phase 2: Extracao de Heuristicas

> **Objetivo:** Extrair os atalhos mentais que o expert usa para decidir RAPIDO sem analisar tudo.
>
> **Formato:** "SE [condicao] -> ENTAO [acao]"
>
> **Tempo estimado:** 20 minutos

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EH-001 | All extracted heuristics must be traceable to source evidence | Validate each heuristic has non-empty source field | VETO - BLOCK. Remove unsourced entries or find supporting evidence. |

---

## Step 1: Heuristicas de Decisao (5-10)

Identifique as regras SE/ENTAO que o expert usa repetidamente.

```yaml
decision_heuristics:
  - id: "H001"
    name: ""
    rule: "SE ___ ENTAO ___"
    rationale: "por que funciona"
    exceptions: ["quando NAO usar"]
    source: "onde ele disse isso"

  # Exemplos de Gary Halbert:
  - id: "GH001"
    name: "Hungry Crowd First"
    rule: "SE escolhendo mercado -> ENTAO escolha o mais faminto, nao o maior"
    rationale: "Demanda > Tamanho"
    exceptions: ["mercados saturados demais"]

  - id: "GH002"
    name: "One Reader Rule"
    rule: "SE escrevendo copy -> ENTAO escreva para UMA pessoa especifica"
    rationale: "Conexao emocional > alcance generico"
```

**Perguntas-guia:**
- "Que regras o expert repete consistentemente?"
- "Que conselho ele da para QUALQUER situacao?"
- "O que ele faz sem pensar, por instinto treinado?"

**Elicit:** Apresente cada heuristica e peça validacao.

---

## Step 2: Heuristicas de Veto (Deal-Breakers)

O que faz o expert PARAR ou REJEITAR algo imediatamente?

```yaml
veto_heuristics:
  - trigger: "SE ___"
    action: "ENTAO pare/rejeite"
    reason: ""
```

**Perguntas-guia:**
- "O que faz ele dizer NAO imediatamente?"
- "Que sinais indicam que deve abandonar um projeto/cliente?"
- "Quais sao seus deal-breakers inegociaveis?"

---

## Step 3: Heuristicas de Priorizacao

Como o expert decide O QUE fazer PRIMEIRO?

```yaml
prioritization_heuristics:
  - rule: ""
    example: ""
```

**Perguntas-guia:**
- "Como decide entre duas opcoes igualmente boas?"
- "O que sempre vem primeiro na ordem de execucao?"
- "Que critério usa para priorizar tarefas?"

---

## Output

Entregue bloco YAML completo contendo:
- 5-10 decision_heuristics com rule + rationale + source
- 2+ veto_heuristics com trigger + reason
- 2+ prioritization_heuristics com rule + example

---

## Quality Check

- [ ] 5+ heurísticas de decisão documentadas
- [ ] Todas as heurísticas têm "rationale" (o PORQUE)
- [ ] 2+ heurísticas de veto
- [ ] 2+ heurísticas de priorização
- [ ] Cada heurística rastreável a fonte

**Score mínimo:** 4/5 items checked

## Task Anatomy

- **Executor:** Agent
- **Inputs:** mind_name; domain; sources
- **Outputs:** Bloco YAML com decision_heuristics, veto_heuristics, prioritization_heuristics
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] 5+ heurísticas de decisão documentadas
- [ ] Todas as heurísticas têm "rationale" (o PORQUE)
- [ ] 2+ heurísticas de veto
- [ ] 2+ heurísticas de priori
