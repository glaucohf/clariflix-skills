---
task: analyzeSystems()
responsavel: "SystemsAnalyst"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - campo: warRoomInsights
    tipo: object
    origen: "facilitateWarRoom()"
    obrigatorio: true

Saida:
  - campo: systemMap
    tipo: object
    destino: "assessEmotionalFactors()"
    persistido: true

Checklist:
  pre-conditions:
    - "[ ] Required input is available"
    - "[ ] Current task objective is clear"
  post-conditions:
    - "[ ] Output artifact has been generated"
    - "[ ] Output is usable by the next task"
---

# analyzeSystems()

## Usage Guide

Execute this task as part of the Athenaeum Squad pipeline, respecting the declared input/output contracts.
