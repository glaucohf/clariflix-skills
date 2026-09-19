---
task: analyzeTrending()
responsavel: "Scout"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: domain
    tipo: string
    obrigatorio: false
  - nome: timeframe
    tipo: string
    obrigatorio: false
  - nome: max_results
    tipo: integer
    obrigatorio: false
Saida:
  - nome: trending_analysis
    tipo: string
    obrigatorio: true
  - nome: prioritized_topics
    tipo: string
    obrigatorio: true
  - nome: sid_angles
    tipo: string
    obrigatorio: true
Checklist:
  - "[ ] Mínimo 5 trends identificadas e pontuadas"
  - "[ ] Ângulo específico do Sid para cada trend"
  - "[ ] Priorização clara com fontes documentadas"
---


# Task: Analyze Trending Topics

**Task ID:** analyze-trending
**Agent:** @trend-scout
**Priority:** MEDIUM
**Tools Required:** WebFetch, WebSearch

---

## Objetivo

Identificar e analisar temas em alta no ecossistema de Cybersecurity e AI que representem oportunidades de conteúdo para o LinkedIn do Sid.

---

## Inputs

| Parameter | Description | Default |
|-----------|-------------|---------|
| DOMAIN | Domínio de busca | `cybersecurity,ai,automation` |
| TIMEFRAME | Janela temporal | `última semana` |
| MAX_RESULTS | Máximo de trends | `10` |

---

## Workflow

### Step 1: Scan de Fontes

Buscar em fontes prioritárias:

**Cybersecurity:**
- CVEs críticas recentes (CVSS 8+)
- Incidentes de segurança noticiados
- Novas ferramentas/frameworks lançados
- Conferências e talks publicadas
- Mudanças regulatórias

**AI/Automation:**
- Lançamentos de modelos (Claude, GPT, Gemini, etc.)
- Novas ferramentas de AI para security
- Papers relevantes publicados
- Debates éticos em alta
- Automações virais ou inovadoras

**LinkedIn Específico:**
- Temas trending no LinkedIn News Brasil
- Posts virais no nicho de tech/security
- Discussões quentes em grupos relevantes

### Step 2: Avaliar Relevância

Para cada trend, pontuar:

| Critério | Peso | Score 1-5 |
|----------|------|-----------|
| Relevância para expertise do Sid | 30% | |
| Interesse do público-alvo | 25% | |
| Janela de oportunidade | 20% | |
| Potencial de engajamento | 15% | |
| Originalidade do ângulo possível | 10% | |

**Score mínimo para recomendar: 3.5/5**

### Step 3: Definir Ângulos

Para cada trend aprovada:
- Ângulo genérico (o que todo mundo vai falar)
- Ângulo Sid (perspectiva única baseada na expertise)
- Hook sugerido
- Formato ideal

### Step 4: Priorizar

Ordenar por:
1. Trending + alta relevância (publicar ASAP)
2. Trending + média relevância (publicar esta semana)
3. Evergreen + alta relevância (guardar no backlog)

---

## Output

```markdown
# Trending Analysis — {{DATE}}

## 🔴 Publicar ASAP (trending agora)

### 1. {{TREND}}
- **Score:** {{X}}/5
- **Fonte:** {{fonte}}
- **Ângulo genérico:** {{o que todos vão falar}}
- **Ângulo Sid:** {{perspectiva única}}
- **Hook:** "{{sugestão}}"
- **Formato:** {{post/carousel/storytelling}}
- **Janela:** {{tempo restante de relevância}}

## 🟡 Publicar esta semana

### 2. {{TREND}}
...

## 🟢 Backlog (evergreen)

### 3. {{TREND}}
...

## Fontes Consultadas

| Fonte | URL | Data |
|-------|-----|------|
| ... | ... | ... |
```

---

## Success Criteria

- [ ] Mínimo 5 trends identificadas
- [ ] Todas pontuadas com o framework de relevância
- [ ] Ângulo específico do Sid para cada uma (não genérico)
- [ ] Priorização clara (ASAP / esta semana / backlog)
- [ ] Fontes documentadas

---

*Task Version: 1.0*
*Created: 2026-03-11*
