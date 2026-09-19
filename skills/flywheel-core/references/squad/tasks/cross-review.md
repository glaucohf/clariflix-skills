---
task: crossReview()
responsavel: HardeningSpecialist
responsavel_type: agent
atomic_layer: hardening
Entrada:
  - campo: bead_id
    tipo: string
    origen: agent
    obrigatorio: true
Saida:
  - campo: review_report
    tipo: path
    destino: workspace
    persistido: true
Checklist:
  - "Pre-condition: Trabalho do Bead está concluído e enviado para revisão."
  - "Post-condition: Relatórios de revisão de múltiplos modelos foram gerados."
---

# cross review
Inicia uma revisão cruzada multi-modelo para validar uma implementação.

## Processo
1. Acionar sub-agentes com diferentes arquétipos ou modelos (Claude, GPT, Gemini).
2. Consolidar os feedbacks recebidos em um relatório único.
3. Decidir sobre o 'Merge' ou retorno para o executor.
