---
task: assessEthics()
responsavel: "EthicsConsultant"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - campo: culturalInsights
    tipo: object
    origen: "assessCulturalInfluences()"
    obrigatorio: true

Saida:
  - campo: ethicalInsights
    tipo: object
    destino: "generateCreativeInsights()"
    persistido: true

Checklist:
  pre-conditions:
    - "[ ] Required input is available"
    - "[ ] Current task objective is clear"
  post-conditions:
    - "[ ] Output artifact has been generated"
    - "[ ] Output is usable by the next task"
---

# assessEthics()

## Usage Guide

Execute this task as part of the Athenaeum Squad pipeline, respecting the declared input/output contracts.
