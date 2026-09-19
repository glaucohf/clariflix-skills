# Output Schemas — Brain Squad

## Schema: themes.json

```json
[
  {
    "id": 1,
    "type": "Analogias",
    "description": "Comparacoes com outros dominios"
  }
]
```

## Schema: Item de Geracao (agent-{N}.txt)

```
1. Titulo do Item | keyword1, keyword2, keyword3 | 8 | H/M
2. Outro Item | keyword1, keyword2 | 7 | M/L
```

Formato por linha: `N. Titulo | keywords CSV | relevancia 1-10 | impacto/esforco H/M/L`

## Schema: top10.json

```json
[
  {
    "rank": 1,
    "title": "Titulo do insight",
    "keywords": ["k1", "k2", "k3"],
    "score": 9,
    "source_type": "Analogias",
    "one_line": "Descricao curta de uma linha"
  }
]
```

## Schema: top3.json

```json
[
  {
    "rank": 1,
    "title": "Titulo do insight",
    "explanation": "3-5 sentencas conectando ao topico original",
    "origin": "R1 tipo Analogias -> R2 expansao sobre X",
    "why": "Justificativa: acionabilidade + profundidade + originalidade"
  }
]
```

## Schema: selected_insight.json

```json
{
  "topic": "topico original",
  "title": "titulo do insight selecionado",
  "explanation": "explicacao detalhada",
  "origin": "trace de origem R1 -> R2",
  "why_selected": "justificativa da selecao"
}
```

## Schema: final_output.md

```markdown
# Brainstorming: {TOPIC}

## Processo
- **Rodada 1:** 10 agentes x 10 associacoes = 100 itens gerados
- **Rodada 2:** 10 agentes x 10 expansoes = 100 itens gerados
- **Total explorado:** 200 itens -> filtrado para 3

---

## Insight #1: {Title}

{Explicacao detalhada 3-5 sentencas}

**Origem:** {Origin trace}

---

## Insight #2: {Title}

{Explicacao}

**Origem:** {Origin trace}

---

## Insight #3: {Title}

{Explicacao}

**Origem:** {Origin trace}

---

> Estes 3 insights foram selecionados entre 200 itens gerados por 24 agentes em 2 rodadas de brainstorming divergente.
```

## Schema: brain_report.md

```markdown
# {TOPIC} — Brain Report

## Fase 1: Exploracao Divergente
- Processo: 24 agentes, 2 rodadas, 200 itens explorados
- Top 3 Insights (resumo com titulos e 1 linha cada)

## Fase 2: Design Convergente
- Insight selecionado: {titulo}
- Resumo de entendimento (5-7 bullets)
- Suposicoes documentadas
- Design final (secoes incrementais)
- Decision Log (decisao, alternativas, justificativa)

## Plano de Implementacao
- (se o usuario solicitou handoff)
```
