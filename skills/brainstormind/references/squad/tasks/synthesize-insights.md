---
task: synthesizeInsights()
responsavel: "Synthesizer"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - nome: top3Json
    tipo: JSON
    descricao: "filterAndRank() R2 -> Synthesizer"
    obrigatorio: true
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> Synthesizer"
    obrigatorio: true

Saida:
  - nome: finalOutput
    tipo: file
    descricao: "-> orquestrador (apresentar ao usuario) + -> buildReport()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] top3.json existe em .brainstorm-tmp/"
    - "[ ] topic.txt acessivel"
  post-conditions:
    - "[ ] final_output.md gerado com formato polido"
    - "[ ] Cada insight tem explicacao + origem + justificativa"
---

# synthesizeInsights()

```
[top3.json + topic] --> [Synthesizer] --> [final_output.md]
```

Formata os 3 insights finais em documento polido com explicacoes detalhadas, trace de origem e metricas do processo.
