---
task: generateIdeas()
responsavel: "IdeaGenerator"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> IdeaGenerator"
    obrigatorio: true
  - nome: associationType
    tipo: string
    descricao: "defineThemes() -> IdeaGenerator (R1) ou top10_summary.txt -> IdeaGenerator (R2)"
    obrigatorio: true
  - nome: roundId
    tipo: string
    descricao: "r1 ou r2"
    obrigatorio: true

Saida:
  - nome: itemsFile
    tipo: file
    descricao: "-> filterAndRank()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Topico disponivel em .brainstorm-tmp/topic.txt"
    - "[ ] Tipo de associacao (R1) ou item top-10 (R2) definido"
    - "[ ] Diretorio .brainstorm-tmp/{round}/ existe"
  post-conditions:
    - "[ ] 10 itens escritos em .brainstorm-tmp/{round}/agent-{N}.txt"
    - "[ ] Formato: N. Titulo | keywords | score | impact/effort"
    - "[ ] Agente retornou apenas 'Done'"
---

# generateIdeas()

```
[topic + type] --> [IdeaGenerator x10] --> [10 arquivos agent-{N}.txt]
```

10 instancias Haiku em paralelo (UM bloco de mensagem). Cada uma gera 10 itens estruturados e escreve em arquivo. Retorna apenas "Done".
