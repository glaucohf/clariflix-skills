---
task: blunderHunt()
responsavel: HardeningSpecialist
responsavel_type: agent
atomic_layer: hardening
Entrada:
  - campo: scope
    tipo: string
    origen: agent
    obrigatorio: true
Saida:
  - campo: blunder_log
    tipo: path
    destino: workspace
    persistido: true
Checklist:
  - "Pre-condition: Implementação alvo está disponível para análise."
  - "Post-condition: O arquivo BLUNDER_LOG.md contém as incoerências identificadas."
---

# blunder hunt
Realiza uma busca intensiva por erros e incoerências em uma área específica do código.

## Processo
1. Analisar o escopo definido em busca de erros lógicos óbvios.
2. Comparar a implementação com o plano estratégico (Plan Space).
3. Registrar cada falha ou oportunidade de melhoria no log de blunders.
