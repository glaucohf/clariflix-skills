---
task-id: etd-recognition-patterns
name: "ETD Phase 0: Recognition Patterns (Radares Mentais)"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
model_rationale: "Identificar padroes perceptuais requer interpretacao profunda de fontes"
estimated-time: 10 min
complexity: low
parent_task: extract-thinking-dna

inputs:
  required:
    - mind_name: "Nome do expert a clonar"
    - domain: "Area de expertise"
    - sources: "Fontes validadas com metodologia documentada"

outputs:
  primary:
    - recognition_patterns_yaml: "Bloco YAML com instant_detection, blind_spots, attention_triggers"

elicit: true
---

# ETD Phase 0: Recognition Patterns (Radares Mentais)

> **Objetivo:** Extrair o que o expert NOTA PRIMEIRO que outros nao notam.
>
> **Tempo estimado:** 10 minutos

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-RP-001 | Sources must be available and validated before extraction | Verify sources input exists with methodology content | VETO - BLOCK. Run collect-sources first. |

---

## Step 1: Instant Detection (O Que Notam Imediatamente)

Analise as fontes e identifique: o que este expert detecta em menos de 2 segundos?

**Perguntas-guia:**
- "O que este expert vê que ninguém mais vê?"
- "Qual o primeiro sinal que procura em qualquer situação?"
- "O que faz ele dizer 'isso está errado' instantaneamente?"

```yaml
recognition_patterns:
  instant_detection:
    - domain: ""
      pattern: "O que veem em < 2 segundos"
      accuracy: "X/10"
      evidence: ""

  # Exemplo Gary Halbert:
  instant_detection:
    - domain: "Sales letter"
      pattern: "Detecta se o lead está weak em 5 segundos"
      accuracy: "9/10"
      evidence: "Always starts by checking the first 50 words"
```

**Elicit:** Apresente cada pattern encontrado e peça confirmação ao usuário antes de avançar.

---

## Step 2: Blind Spots (O Que NAO Notam)

Todo expert tem pontos cegos. Identifique-os.

```yaml
blind_spots:
  - domain: ""
    what_they_miss: ""
    why: ""
    consequence: ""
```

**Perguntas-guia:**
- "Onde este expert já errou publicamente?"
- "O que outros experts criticam nele?"
- "Que aspecto do domínio ele ignora consistentemente?"

---

## Step 3: Attention Triggers

O que faz o expert "ligar o radar"?

```yaml
attention_triggers:
  - trigger: "Quando vê/ouve..."
    response: "Imediatamente faz..."
    intensity: "alto|médio|baixo"
```

---

## Output

Entregue o bloco `recognition_patterns` completo em YAML, contendo:
- Mínimo 2 instant_detection entries com evidence
- Mínimo 1 blind_spot documentado
- Mínimo 2 attention_triggers

---

## Quality Check

- [ ] 2+ instant_detection patterns com evidence preenchido
- [ ] 1+ blind_spot com consequence documentada
- [ ] 2+ attention_triggers com response preenchido
- [ ] Todos os entries são rastreáveis a fontes

**Score mínimo:** 3/4 items checked

## Task Anatomy

- **Executor:** Agent
- **Inputs:** mind_name; domain; sources
- **Outputs:** Bloco YAML com instant_detection, blind_spots, attention_triggers
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] All veto conditions checked and none triggered
- [ ] Output artifact produced: Bloco YAML com instant_detection, blind_spots, attention_triggers
- [ ] Task output validated against quality standards
