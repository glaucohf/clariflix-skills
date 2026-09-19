<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Agents](https://img.shields.io/badge/agents-6-green)
![Tasks](https://img.shields.io/badge/tasks-6-orange)
![Workflows](https://img.shields.io/badge/workflows-2-purple)
![License](https://img.shields.io/badge/license-MIT-yellow)
![AIOS](https://img.shields.io/badge/AIOS-2.1.0+-red)

# Brain Squad

**Workflow Diverge+Converge para brainstorming em escala com design validado.**

`/brain`

</div>

---

Ja teve uma ideia que parecia boa, mas na hora de implementar percebeu que faltava clareza, contexto e validacao?

O Brain Squad resolve isso com um pipeline de 2 fases: primeiro **explode** o tema em 200+ ideias com um swarm de 24 agentes, depois **refina** o melhor insight em design pronto para implementacao.

| Antes (manual) | Depois (Brain Squad) |
|-----------------|---------------------|
| 5-10 ideias por sessao | **200 ideias** em 2 rodadas |
| Ranking por "intuicao" | Ranking **ponderado** com criterios |
| Ideias vagas sem validacao | Design com **Understanding Lock** |
| Sem rastreabilidade | **Decision Log** completo |
| ~12.000 tokens no Opus | **~1.440 tokens** no Opus (-87%) |

---

## Pipeline

```
FASE 1: DIVERGE (Automatico)          FASE 2: CONVERGE (Interativo)
=========================              =========================

TOPIC                                  INSIGHT selecionado
  |                                        |
  v                                        v
ThemeDefiner (10 tipos)             DesignFacilitator
  |                                   1. Contexto
  v                                   2. Perguntas (1/vez)
10x IdeaGenerator (R1)              3. Requisitos NF
  |                                   4. Understanding Lock
  v                                   5. Abordagens
FilterRanker -> Top 10              6. Design incremental
  |                                   7. Decision Log
  v                                        |
10x IdeaGenerator (R2)                     v
  |                                   ReportBuilder
  v                                        |
FilterRanker -> Top 3                      v
  |                                   brain_report.md
  v
Synthesizer -> Output
  |
  v
GATE: usuario escolhe
```

---

## Por que Brain Squad?

**Swarm real, nao teatro.** 24 agentes geram e filtram ideias — o orquestrador so roteia, nunca le os 200 itens.

**Gate de decisao.** Voce escolhe qual insight refinar. Sem surpresas, sem assuncoes.

**Understanding Lock.** Hard gate antes de qualquer design. Nada avanca sem sua confirmacao explicita.

**Token-optimized.** ~65% menos custo que abordagem naive. Haiku gera, Sonnet filtra, Opus so orquestra.

**Outlier preservation.** Selecao Pareto (Top N + wildcards) preserva ideias surpreendentes que ranking puro eliminaria.

---

## Agentes

| Icon | Nome | Archetype | Papel |
|------|------|-----------|-------|
| 🎯 | ThemeDefiner | Builder | Define 10 tipos de associacao para o topico |
| 💡 | IdeaGenerator | Builder | Gera 10 itens por tipo (x10 paralelo) |
| ⚖️ | FilterRanker | Guardian | Filtra, deduplica e ranqueia com Pareto |
| 🧠 | Synthesizer | Builder | Formata output final da Fase 1 |
| 🏗️ | DesignFacilitator | Flow_Master | Facilita design interativo na Fase 2 |
| 📋 | ReportBuilder | Builder | Consolida relatorio final |

## Tasks

| Task | Agente | Atomic Layer |
|------|--------|-------------|
| defineThemes() | ThemeDefiner | Atom |
| generateIdeas() | IdeaGenerator | Organism |
| filterAndRank() | FilterRanker | Organism |
| synthesizeInsights() | Synthesizer | Molecule |
| facilitateDesign() | DesignFacilitator | Organism |
| buildReport() | ReportBuilder | Molecule |

## Workflows

| Nome | Padrao | Descricao |
|------|--------|-----------|
| brain_pipeline | Pipeline + Interativo | Diverge+Converge completo (6 fases + gate) |
| diverge_only | Pipeline | Apenas Fase 1 — gera Top 3 sem design |

## Commands

| Comando | Descricao |
|---------|-----------|
| `/brain` | Pipeline completo (Diverge + Converge) |
| `*define-themes` | Define 10 tipos de associacao |
| `*generate-ideas` | Gera itens em paralelo |
| `*filter-rank-r1` | Filtra R1 para Top 10 |
| `*filter-rank-final` | Filtra R2 para Top 3 |
| `*synthesize` | Sintetiza output final |
| `*facilitate-design` | Inicia facilitacao de design |
| `*build-report` | Gera relatorio consolidado |

---

## Tech Stack

| Tecnologia | Uso |
|------------|-----|
| Claude Code Agent Teams | Orquestracao multi-agente |
| Haiku | Geracao de itens (20x instancias) |
| Sonnet | Filtragem, ranking, sintese (4x instancias) |
| Opus | Orquestracao e facilitacao (1x) |
| JSON | Contratos de dados entre agentes |
| Markdown | Documentos e relatorios |

---

<details>
<summary><strong>FAQ</strong></summary>

**Preciso usar as 2 fases?**
Nao. Use o workflow `diverge_only` se quiser apenas os Top 3 insights sem design.

**Quantos tokens consome?**
~1.440 tokens no Opus + custo Haiku/Sonnet para geracao e ranking. ~65% menos que processar tudo no Opus.

**O design facilitado produz codigo?**
Nao. A Fase 2 produz apenas DESIGN documentado. Implementacao e um handoff opcional apos o relatorio.

**Posso refinar mais de um insight?**
Sim. No gate de transicao, escolha a opcao D para refinar multiplos insights sequencialmente.

**E se eu nao gostar dos 3 insights?**
Encerre no gate e rode o pipeline novamente com o topico refinado.

</details>

---

<div align="center">

**Brain Squad** | MIT License

*Divergir para descobrir. Convergir para construir.*

</div>
