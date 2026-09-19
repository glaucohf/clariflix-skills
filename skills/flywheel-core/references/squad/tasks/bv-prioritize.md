---
task: bvPrioritize()
responsavel: SwarmCoordinator
responsavel_type: agent
atomic_layer: coordination
Entrada:
  - campo: beads_file
    tipo: path
    origen: workspace
    obrigatorio: true
Saida:
  - campo: next_task
    tipo: string
    destino: orchestrator
    persistido: true
Checklist:
  - "Pre-condition: BEADS.md existe e contém o grafo de dependências."
  - "Post-condition: O ID da próxima tarefa de maior impacto foi identificado."
---

# BV Prioritize
Analisa a topologia do grafo de dependências (bv) e define a próxima tarefa de maior impacto.

## Processo
1. Carregar o grafo de Beads do arquivo BEADS.md.
2. Calcular o caminho crítico e dependências bloqueadas.
3. Identificar o Bead com maior centralidade de saída não concluído.
4. Retornar o ID da tarefa para o SwarmCoordinator.
