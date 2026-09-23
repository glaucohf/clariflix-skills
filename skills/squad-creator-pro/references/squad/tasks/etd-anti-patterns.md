---
task-id: etd-anti-patterns
name: "ETD Phase 4: Anti-Patterns"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
model_rationale: "Identificar anti-patterns requer interpretação profunda de filosofia do expert"
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
    - anti_patterns_yaml: "Bloco YAML com never_do e common_mistakes"

elicit: true
---

# ETD Phase 4: Anti-Patterns

> **Objetivo:** Documentar o que o expert NUNCA faria e os erros comuns que corrige nos outros.
>
> **Tempo estimado:** 10 minutos

---

## Step 1: O Que Este Expert NUNCA Faria

```yaml
anti_patterns:
  never_do:
    - action: ""
      reason: ""
      quote: ""  # se tiver

  # Exemplo Eugene Schwartz:
  never_do:
    - action: "Criar desejo do zero"
      reason: "Desejo já existe, você só canaliza"
      quote: "You cannot create desire, you can only channel it"

    - action: "Focar em features antes de benefits"
      reason: "Ninguém compra features"
```

**Perguntas-guia:**
- "O que este expert condena publicamente?"
- "Que práticas comuns ele considera erradas?"
- "O que faz ele perder a paciência?"
- "Que conselho vai CONTRA o senso comum do domínio?"

**Elicit:** Apresente cada anti-pattern e peça validação.

---

## Step 2: Erros Comuns que Corrige

O que o expert vê outros fazerem errado?

```yaml
common_mistakes:
  - mistake: ""
    correction: ""
    how_expert_does_it: ""
```

**Perguntas-guia:**
- "Que erros vê repetidamente em iniciantes?"
- "O que faz diferente da maioria dos profissionais do domínio?"
- "Onde a indústria inteira está errada, segundo ele?"

---

## Output

Entregue bloco YAML completo contendo:
- 3+ never_do entries com action + reason
- 3+ common_mistakes com correction + how_expert_does_it
- Quotes diretas quando disponíveis

---

## Quality Check

- [ ] 3+ anti-patterns identificados com reason
- [ ] 3+ common_mistakes com correction
- [ ] Anti-patterns são consistentes com frameworks e heurísticas das fases anteriores
- [ ] Quotes diretas incluídas quando disponíveis nas fontes

**Score mínimo:** 3/4 items checked

## Task Anatomy

- **Executor:** Agent
- **Inputs:** mind_name; domain; sources
- **Outputs:** Bloco YAML com never_do e common_mistakes
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified

## Acceptance Criteria

- [ ] Output artifact produced: Bloco YAML com never_do e common_mistakes
- [ ] Task output validated against quality standards
