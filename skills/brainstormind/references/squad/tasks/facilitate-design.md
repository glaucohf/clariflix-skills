---
task: facilitateDesign()
responsavel: "DesignFacilitator"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: selectedInsight
    tipo: JSON
    descricao: "gate de transicao -> DesignFacilitator"
    obrigatorio: true
  - nome: top3Json
    tipo: JSON
    descricao: "filterAndRank() R2 -> DesignFacilitator (contexto)"
    obrigatorio: false
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> DesignFacilitator"
    obrigatorio: true

Saida:
  - nome: designDocument
    tipo: file
    descricao: "-> buildReport()"
    obrigatorio: true
  - nome: decisionLog
    tipo: file
    descricao: "-> buildReport()"
    obrigatorio: true
  - nome: understandingSummary
    tipo: file
    descricao: "-> buildReport()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] selected_insight.json existe em .brainstorm-tmp/"
    - "[ ] Usuario escolheu insight no gate de transicao"
  post-conditions:
    - "[ ] Understanding Lock confirmado pelo usuario"
    - "[ ] Pelo menos 1 abordagem de design aceita"
    - "[ ] Decision Log completo"
    - "[ ] Suposicoes documentadas"
    - "[ ] Riscos reconhecidos"
    - "[ ] Design salvo em .brainstorm-tmp/design/"
---

# facilitateDesign()

```
[insight selecionado] --> [DesignFacilitator <-> usuario] --> [design/ validado]
```

Processo interativo de 7 etapas: contexto, perguntas (1 por vez), requisitos nao-funcionais, Understanding Lock, explorar abordagens, design incremental, Decision Log. NAO implementa codigo.
