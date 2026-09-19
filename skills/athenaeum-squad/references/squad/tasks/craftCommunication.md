---
task: craftCommunication()
responsavel: "CommunicationSpecialist"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - campo: solutionPlan
    tipo: object
    origen: "designSolution()"
    obrigatorio: true

Saida:
  - campo: communicationStrategy
    tipo: object
    destino: "compileFinalReport()"
    persistido: true

Checklist:
  pre-conditions:
    - "[ ] Required input is available"
    - "[ ] Current task objective is clear"
  post-conditions:
    - "[ ] Output artifact has been generated"
    - "[ ] Output is usable by the next task"
---

# craftCommunication()

## Usage Guide

Execute this task as part of the Athenaeum Squad pipeline, respecting the declared input/output contracts.
