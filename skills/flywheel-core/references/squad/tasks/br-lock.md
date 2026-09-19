---
task: brLock()
responsavel: SwarmCoordinator
responsavel_type: agent
atomic_layer: coordination
Entrada:
  - campo: files
    tipo: array
    origen: agent
    obrigatorio: true
  - campo: ttl
    tipo: string
    origen: agent
    obrigatorio: false
Saida:
  - campo: lock_status
    tipo: boolean
    destino: workspace
    persistido: true
Checklist:
  - "Pre-condition: Arquivo alvo não está bloqueado por outro agente."
  - "Post-condition: O arquivo está reservado com um bloqueio consultivo no LOCKS.json."
---

# br lock
Reserva arquivos via bloqueio consultivo para evitar colisões no enxame.

## Processo
1. Verificar disponibilidade dos arquivos solicitados no LOCKS.json.
2. Criar entrada de bloqueio com ID do agente e TTL (Time To Live).
3. Notificar o enxame sobre a reserva do recurso.
