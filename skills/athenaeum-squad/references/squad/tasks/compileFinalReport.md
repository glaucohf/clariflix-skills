---
task: compileFinalReport()
responsavel: "ReportSynthesizer"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - campo: communicationStrategy
    tipo: object
    origen: "craftCommunication()"
    obrigatorio: true

Saida:
  - campo: finalReport
    tipo: file
    destino: "output"
    persistido: true

Checklist:
  pre-conditions:
    - "[ ] Required input is available"
    - "[ ] Current task objective is clear"
  post-conditions:
    - "[ ] Output artifact has been generated"
    - "[ ] Output is usable by the next task"
---

# compileFinalReport()

## Usage Guide

Execute this task as part of the Athenaeum Squad pipeline, respecting the declared input/output contracts.
