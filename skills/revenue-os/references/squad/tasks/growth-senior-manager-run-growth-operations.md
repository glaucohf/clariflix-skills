---
task: Run Growth Operations
responsavel: "@growth-senior-manager"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - prioritized_bets: Apostas de crescimento priorizadas (saida do CGO)
  - growth_system: Sistema AARRR com loops definidos
  - executor_capacity: Capacidade de analysts + engenheiros
Saida: |
  - growth_ops_cycle: Ciclo operacional de growth (sprints de 2 semanas)
  - experiment_tracker: Tracker de experimentos com status
  - weekly_growth_review: Agenda da revisao semanal
Checklist:
  - "[ ] Definir sprint de growth (2 semanas)"
  - "[ ] Atribuir owners por experimento"
  - "[ ] Definir metricas de sucesso por experimento"
  - "[ ] Configurar tracker de experimentos"
---

# *run-growth-operations

Operacionaliza backlog de growth em sprints de 2 semanas com rituais claros.

## Step-by-Step

1. **Absorver apostas priorizadas** — Ler `prioritized_bets` do CGO.
2. **Dividir em sprints de 2 semanas** — Cada sprint tem 1-3 experimentos ativos.
3. **Atribuir owners** — Cada experimento tem 1 owner executor (analyst) + 1 owner decisor (manager).
4. **Definir metricas de sucesso** — Por experimento: metrica primaria + guardrails (o que nao pode piorar).
5. **Configurar tracker** — Quadro visual (Kanban ou similar) com status: backlog / setup / running / analysis / decision.
6. **Agendar rituais:**
   - Semana 1 segunda: planning (60 min)
   - Semana 2 sexta: review + decisao kill/continue/scale (60 min)
   - Diario 17h: standup async de 5 min (update em canal)
7. **Alinhar com marketing ops** — Experimentos que tocam canais pagos precisam coordenar com `@marketing-senior-manager`.

## Veto Conditions

- VETO se >3 experimentos simultaneos em 1 sprint → foco perdido
- VETO se experimento nao tiver metrica primaria numerica → impossivel decidir
- VETO se nao houver guardrails → experimento pode estragar outras metricas

## Output Example

```yaml
growth_ops_cycle:
  sprint_atual: "Sprint 12 (05-18 Mai)"
  experimentos_ativos:
    - id: EXP-12A
      hipotese: "Chat AI no onboarding sobe ativacao 14d de 60% para 75%"
      owner_executor: "@growth-senior-analyst"
      owner_decisor: "@growth-senior-manager"
      metrica_primaria: "% clientes que ativam stack em 14d"
      baseline: "60%"
      target: "75%"
      guardrails:
        - "Nao piorar NPS >-5"
        - "Nao aumentar tickets de suporte >20%"
      duracao: "2 semanas (sprint inteiro)"
      status: "running"

    - id: EXP-12B
      hipotese: "Case de video na LP sobe conversao visitante->SQL de 2% para 3.5%"
      owner_executor: "@marketing-senior-analyst"
      owner_decisor: "@growth-senior-manager"
      metrica_primaria: "conversao LP"
      baseline: "2%"
      target: "3.5%"
      guardrails:
        - "Qualidade SQL nao pode cair >10%"
      duracao: "2 semanas"
      status: "setup"

experiment_tracker:
  board: "Kanban com 5 colunas"
  colunas: ["backlog", "setup", "running", "analysis", "decision"]
  sla_por_coluna:
    setup: "max 3 dias"
    running: "min 2 semanas"
    analysis: "max 3 dias"

rituais:
  sprint_planning:
    quando: "Semana 1, segunda, 14:00"
    duracao_min: 60
    participantes: ["@growth-senior-manager", "@growth-senior-analyst"]
    output: "Experimentos do sprint definidos + atribuidos"

  sprint_review:
    quando: "Semana 2, sexta, 16:00"
    duracao_min: 60
    participantes: ["@growth-senior-manager", "@growth-senior-analyst", "@cgo-growth-director (opcional)"]
    output: "Decisao por experimento: kill / continue / scale"

  daily_standup_async:
    horario: "17:00 (msg em canal)"
    template: "Ontem: X | Hoje: Y | Bloqueio: Z"

weekly_growth_review:
  quando: "Sexta 16h (durante sprint review)"
  agenda:
    - "Status dos experimentos ativos (10 min cada)"
    - "Decisoes kill/continue/scale"
    - "Proximos 2-3 experimentos do sprint seguinte"
```

## Completion Criteria

- Sprint com 1-3 experimentos ativos (nao mais)
- Cada experimento tem hipotese + metrica + baseline + target + guardrails + owners
- Tracker visual ativo com SLAs por coluna
- Rituais de planning + review + standup agendados

## Handoff

`@growth-senior-analyst` executa setup e monitoramento diario. Reporta para `@cgo-growth-director` via sprint review quinzenal.
