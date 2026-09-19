---
task: analyzeProfile()
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: linkedin_profile_url
    tipo: string
    obrigatorio: true
  - nome: focus_areas
    tipo: string
    obrigatorio: false
Saida:
  - nome: profile_report
    tipo: string
    obrigatorio: true
  - nome: quick_wins
    tipo: string
    obrigatorio: true
  - nome: optimization_recommendations
    tipo: string
    obrigatorio: true
Checklist:
  - "[ ] Todas as 7 dimensões avaliadas com score"
  - "[ ] Mínimo 3 sugestões de headline alternativas"
  - "[ ] Quick wins priorizados por impacto"
---


# Task: Analyze LinkedIn Profile

**Task ID:** analyze-profile
**Agent:** @profile-analyst
**Priority:** MEDIUM
**Tools Required:** WebFetch, Read

---

## Objetivo

Realizar análise completa do perfil LinkedIn do Sid, identificando pontos fortes, gaps e oportunidades de otimização para posicionamento em Segurança Ofensiva e Automação com IA.

---

## Inputs

| Parameter | Description | Default |
|-----------|-------------|---------|
| PROFILE_URL | URL do perfil LinkedIn | `https://www.linkedin.com/in/sidney-fernandes-a448152a8/` |
| FOCUS_AREAS | Áreas de foco para análise | `all` |

---

## Workflow

### Step 1: Coletar Dados do Perfil

Acessar o perfil e extrair:
- Headline atual
- About/Resumo
- Experiências listadas
- Skills e endorsements
- Featured section
- Últimos 5-10 posts (conteúdo e métricas visíveis)

> **Nota:** LinkedIn bloqueia WebFetch (status 999). Alternativas:
> - Pedir ao usuário para colar o conteúdo do perfil
> - Usar Apify LinkedIn Scraper via Docker MCP
> - Analisar com base em informações fornecidas pelo usuário

### Step 2: Análise por Dimensão

Avaliar cada dimensão com score 1-5:

| Dimensão | O que avaliar |
|----------|--------------|
| **Headline** | Keywords, clareza, posicionamento |
| **About** | Hook, storytelling, CTA, keywords |
| **Experiência** | Resultados vs responsabilidades |
| **Featured** | Conteúdo pinado estratégico |
| **Skills** | Alinhamento com posicionamento |
| **Conteúdo** | Frequência, engajamento, consistência |
| **Visual** | Foto, banner, identidade visual |

### Step 3: Benchmark

Comparar com 3-5 perfis de referência no nicho:
- Profissionais de segurança ofensiva no Brasil
- Profissionais que combinam security + AI
- Criadores de conteúdo técnico no LinkedIn BR

### Step 4: Gerar Recomendações

Para cada gap identificado:
1. O que está hoje
2. O que deveria ser
3. Sugestão concreta de texto/ação
4. Prioridade (Alta/Média/Baixa)

---

## Output

```markdown
# LinkedIn Profile Analysis — F0livora

**Data:** {{DATE}}
**Score Geral:** {{SCORE}}/5

## Scores por Dimensão

| Dimensão | Score | Status |
|----------|-------|--------|
| Headline | X/5 | 🟢/🟡/🔴 |
| About | X/5 | 🟢/🟡/🔴 |
| ... | ... | ... |

## Top 3 Quick Wins

1. [Ação imediata de maior impacto]
2. [Segunda ação]
3. [Terceira ação]

## Recomendações Detalhadas

### Headline
**Atual:** ...
**Sugerida:** ...
**Justificativa:** ...

### About
**Sugestão de reescrita:**
...

## Próximos Passos

- [ ] Implementar quick wins
- [ ] Agendar revisão em 30 dias
```

---

## Success Criteria

- [ ] Todas as 7 dimensões avaliadas com score
- [ ] Mínimo 3 sugestões de headline alternativas
- [ ] Sugestão de About completa reescrita
- [ ] Quick wins priorizados por impacto
- [ ] Benchmark com pelo menos 3 perfis de referência

---

*Task Version: 1.0*
*Created: 2026-03-11*
