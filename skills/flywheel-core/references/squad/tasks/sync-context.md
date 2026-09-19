---
task: syncContext()
responsavel: BeadManager
responsavel_type: agent
atomic_layer: memory
Entrada:
  - campo: request
    tipo: string
    origen: orchestrator
    obrigatorio: true
Saida:
  - campo: sync_status
    tipo: string
    destino: workspace
    persistido: false
Checklist:
  - "Pre-condition: Arquivo BEADS.md e LOCKS.json estão acessíveis."
  - "Post-condition: O estado do workspace está sincronizado com a memória dos Beads."
---

# Sync Context
Sincroniza o estado atual do workspace com a memória dos Beads.

## Processo
1. Ler o arquivo BEADS.md e LOCKS.json.
2. Verificar a integridade do workspace atual.
3. Atualizar os metadados dos Beads conforme o progresso.
