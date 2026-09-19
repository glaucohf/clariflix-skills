---
task: filterAndRank()
responsavel: "FilterRanker"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: itemFiles
    tipo: array<file>
    descricao: "generateIdeas() -> FilterRanker"
    obrigatorio: true
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> FilterRanker"
    obrigatorio: true
  - nome: roundId
    tipo: string
    descricao: "r1 (Top 10) ou r2 (Top 3 final)"
    obrigatorio: true

Saida:
  - nome: rankedJson
    tipo: JSON
    descricao: "-> generateIdeas() R2 (top10) ou -> synthesizeInsights() (top3)"
    obrigatorio: true
  - nome: rankedSummary
    tipo: file
    descricao: "-> orquestrador (titulos curtos)"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Todos os 10 arquivos agent-*.txt existem no round"
    - "[ ] topic.txt acessivel"
  post-conditions:
    - "[ ] R1: top10.json + top10_summary.txt gerados"
    - "[ ] R2: top3.json gerado com explicacoes detalhadas"
    - "[ ] Duplicatas removidas"
    - "[ ] Outliers preservados (selecao Pareto)"
---

# filterAndRank()

```
[100 itens] --> [FilterRanker] --> [top10.json ou top3.json]
```

Le todos os arquivos de itens, remove duplicatas, aplica selecao Pareto (Top N + wildcards), e escreve resultado ranqueado em JSON estruturado.
