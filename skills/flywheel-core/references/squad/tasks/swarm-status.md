---
task: swarmStatus()
responsavel: SwarmCoordinator
responsavel_type: agent
atomic_layer: coordination
Entrada:
  - campo: request
    tipo: string
    origen: orchestrator
    obrigatorio: true
Saida:
  - campo: dashboard
    tipo: string
    destino: user
    persistido: false
Checklist:
  - "Pre-condition: O enxame está em operação ativa."
  - "Post-condition: Dashboard de progresso e ocupação exibido com sucesso."
---

# swarm status
Exibe o status atual de ocupação e progresso de todos os agentes do enxame.

## Processo
1. Coletar o estado de todos os agentes registrados.
2. Ler o status dos LOCKS e Beads ativos.
3. Gerar interface visual de monitoramento para o operador.
