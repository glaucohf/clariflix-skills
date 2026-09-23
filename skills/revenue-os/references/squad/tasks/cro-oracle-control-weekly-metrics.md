---
task: Control Weekly Metrics
responsavel: "@cro-oracle-guardian"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - weekly_dashboard: KPIs semanais (leading + lagging) do revenue-dashboard
  - incident_log: Incidentes operacionais da semana (bugs, escalacoes, bloqueios)
  - macro_revenue_plan: Plano macro ativo com metas mensais
Saida: |
  - weekly_actions: Lista priorizada de acoes corretivas/preventivas
  - triggers_fired: Gatilhos ativados por desvio de KPI
  - director_assignments: Quem (CCO/CMO/CGO) recebe cada acao
Checklist:
  - "[ ] Revisar KPI leading (acoes) vs target"
  - "[ ] Revisar KPI lagging (resultado) vs meta mensal"
  - "[ ] Detectar desvio > 15% em qualquer indicador"
  - "[ ] Acionar diretor responsavel com contexto + deadline"
  - "[ ] Registrar decisoes em log de governanca"
---

# *control-weekly-metrics

Monitora metricas semanais e aciona ajustes taticos na cadeia executiva.

## Step-by-Step

1. **Abrir dashboard** — Ler `weekly_dashboard` com KPIs leading e lagging da semana.
2. **Comparar vs target** — Para cada KPI, calcular `(atual / target) - 1`. Flag: verde (>=95%), amarelo (80-94%), vermelho (<80%).
3. **Revisar incident_log** — Identificar incidentes que explicam desvios.
4. **Disparar triggers** — Regras:
   - KPI vermelho 1 semana → acionar diretor com plano em 48h
   - KPI vermelho 2 semanas seguidas → escalar para ciclo mensal de planejamento
   - KPI leading vermelho + lagging verde → sem acao imediata, observar proxima semana
5. **Priorizar acoes** — Top 3 acoes que mais movem agulha (80/20).
6. **Assignar diretores** — Cada acao tem owner unico (CCO/CMO/CGO) e deadline (max 1 semana).
7. **Registrar no log** — Decisoes + owners + deadlines em log de governanca.

## Veto Conditions

- VETO se dashboard estiver desatualizado >24h → pausar revisao, acionar `@revops-automation-engineer` para fix
- VETO se nao houver baseline (primeira semana do plano) → registrar baseline e pular para proxima rodada
- VETO se 100% dos KPIs estiverem vermelhos → problema sistemico, escalar para `*run-monthly-planning-cycle` imediatamente

## Output Example

```yaml
weekly_actions:
  - acao: "Refazer segmentacao de audiencia paid social (CAC subiu 40%)"
    owner: "@cmo-marketing-director"
    deadline: "2026-05-02"
    kpi_alvo: "CAC payback"
  - acao: "Auditar script de demo (conversao SQL→cliente caiu de 25% para 16%)"
    owner: "@cco-commercial-director"
    deadline: "2026-04-30"
    kpi_alvo: "Conversao SQL->cliente"

triggers_fired:
  - { kpi: "CAC payback", status: vermelho, semanas_consecutivas: 1 }
  - { kpi: "Conversao SQL->cliente", status: vermelho, semanas_consecutivas: 2, acao: "escalar para ciclo mensal" }
```

## Completion Criteria

- Todos os KPIs revisados (100% dos leading + lagging ativos)
- Acoes priorizadas limitadas a top 3 (evitar dispersao)
- Cada acao com owner unico e deadline max 1 semana
- Log de governanca atualizado

## Handoff

Acoes distribuidas para CCO/CMO/CGO. Se trigger de "2 semanas vermelhas", handoff automatico para `*run-monthly-planning-cycle`.
