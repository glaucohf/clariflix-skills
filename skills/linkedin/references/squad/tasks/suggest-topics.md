---
task: suggestTopics()
responsavel: "Link"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: timeframe
    tipo: string
    obrigatorio: false
  - nome: pillar
    tipo: string
    obrigatorio: false
  - nome: count
    tipo: integer
    obrigatorio: false
Saida:
  - nome: topics_list
    tipo: string
    obrigatorio: true
  - nome: urgency_classification
    tipo: string
    obrigatorio: true
  - nome: backlog_table
    tipo: string
    obrigatorio: true
Checklist:
  - "[ ] Mínimo 8 sugestões com mix de trending e evergreen"
  - "[ ] Todos os 4 pilares representados"
  - "[ ] Hook sugerido para cada tópico"
---


# Task: Suggest Content Topics

**Task ID:** suggest-topics
**Agent:** @trend-scout, @linkedin-chief
**Priority:** HIGH
**Tools Required:** WebFetch, WebSearch, Read

---

## Objetivo

Gerar lista de tópicos de conteúdo relevantes e oportunos para o LinkedIn do Sid, cruzando expertise pessoal, tendências do mercado e interesse do público-alvo.

---

## Inputs

| Parameter | Description | Default |
|-----------|-------------|---------|
| TIMEFRAME | Período para sugestões | `próximas 4 semanas` |
| PILLAR | Pilar específico (ou all) | `all` |
| COUNT | Quantidade de sugestões | `8-12` |

---

## Workflow

### Step 1: Mapear Expertise Atual

Cruzar com os pilares definidos:
1. **Segurança Ofensiva** — Pentesting, Red Team, vulnerabilidades
2. **Automação com IA** — AI Agents, LLMs, automações
3. **Bastidores** — Dia a dia em CyberSec
4. **Mentoria** — Dicas para juniores

### Step 2: Scan de Tendências

Buscar temas em alta nas fontes do @trend-scout:
- CVEs recentes com impacto relevante
- Novidades em AI/LLMs (novos modelos, ferramentas)
- Discussões quentes no LinkedIn/Twitter sobre sec
- Conferências ou eventos próximos
- Mudanças regulatórias (LGPD, NIST, etc.)

### Step 3: Cruzar Expertise × Tendência

Para cada tendência identificada, avaliar:
- Sid tem experiência/opinião sobre isso? (1-5)
- O público-alvo se importa? (1-5)
- Janela de oportunidade ainda aberta? (sim/não)
- Formato ideal? (post/carrossel/storytelling)

### Step 4: Gerar Sugestões Estruturadas

Para cada tópico sugerido, entregar:
- Título/tema
- Ângulo específico (não genérico)
- Hook sugerido (primeira linha)
- Formato recomendado
- Pilar de conteúdo
- Nível de urgência (trending agora vs evergreen)

---

## Output

```markdown
# Sugestões de Conteúdo — Semana de {{DATE}}

## Trending (publicar esta semana)

### 1. {{TEMA}}
- **Pilar:** Segurança Ofensiva
- **Formato:** Post texto
- **Ângulo:** {{ângulo específico}}
- **Hook:** "{{primeira linha sugerida}}"
- **Por que agora:** {{contexto da urgência}}

### 2. {{TEMA}}
...

## Evergreen (publicar quando quiser)

### 3. {{TEMA}}
...

## Backlog de Ideias

| # | Tema | Pilar | Formato | Prioridade |
|---|------|-------|---------|------------|
| 1 | ... | ... | ... | Alta |
| 2 | ... | ... | ... | Média |
```

---

## Success Criteria

- [ ] Mínimo 8 sugestões de tópicos
- [ ] Mix de trending + evergreen
- [ ] Todos os 4 pilares representados
- [ ] Hook sugerido para cada tópico
- [ ] Formato recomendado para cada tópico

---

*Task Version: 1.0*
*Created: 2026-03-11*
