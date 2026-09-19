---
task: buildReport()
responsavel: "ReportBuilder"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - nome: finalOutput
    tipo: file
    descricao: "synthesizeInsights() -> ReportBuilder"
    obrigatorio: true
  - nome: designFiles
    tipo: directory
    descricao: "facilitateDesign() -> ReportBuilder"
    obrigatorio: false
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> ReportBuilder"
    obrigatorio: true

Saida:
  - nome: brainReport
    tipo: file
    descricao: "-> usuario (entrega final)"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] final_output.md existe"
    - "[ ] design/ existe (se Fase 2 executada)"
  post-conditions:
    - "[ ] brain_report.md gerado e consolidado"
    - "[ ] Ambas as fases documentadas"
    - "[ ] Rastreabilidade completa mantida"
---

# buildReport()

```
[final_output.md + design/] --> [ReportBuilder] --> [brain_report.md]
```

Consolida todos os artefatos das Fases 1 e 2 em documento final autocontido com rastreabilidade completa.
