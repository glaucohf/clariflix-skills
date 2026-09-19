---
task: assessEmotionalFactors()
responsavel: "EmotionalMediator"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - campo: systemMap
    tipo: object
    origen: "analyzeSystems()"
    obrigatorio: true

Saida:
  - campo: emotionalInsights
    tipo: object
    destino: "assessCulturalInfluences()"
    persistido: true

Checklist:
  pre-conditions:
    - "[ ] Required input is available"
    - "[ ] Current task objective is clear"
  post-conditions:
    - "[ ] Output artifact has been generated"
    - "[ ] Output is usable by the next task"
---

# assessEmotionalFactors()

## Usage Guide

Execute this task as part of the Athenaeum Squad pipeline, respecting the declared input/output contracts.
