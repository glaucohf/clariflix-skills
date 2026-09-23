---
task: Run Growth Experiments
responsavel: "@experimentation-analyst"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - backlog: Lista de hipoteses priorizadas
  - baseline_metrics: Metricas atuais de referencia
  - experiment_tracker: Tracker ativo (saida do growth-senior-manager)
Saida: |
  - experiment_cycle: Plano semanal de testes em execucao
  - decision_log: Log de decisoes (continuar, parar, escalar)
  - learnings_library: Biblioteca de aprendizados para reuso
Checklist:
  - "[ ] Priorizar backlog por ICE + balanco AARRR"
  - "[ ] Setup experimental rigoroso (controle + variante)"
  - "[ ] Executar com monitoramento diario"
  - "[ ] Decisao baseada em significancia estatistica"
  - "[ ] Documentar aprendizados (positivos e negativos)"
---

# *run-growth-experiments

Executa ciclo semanal de experimentacao para melhorar receita sem depender de achismo.

## Step-by-Step

1. **Priorizar backlog** — ICE score + balanco AARRR + capacidade do sprint.
2. **Desenhar experimento** — Hipotese, variantes, metrica primaria, guardrails, amostra minima.
3. **Setup instrumentacao** — Tracking do evento-chave para cada variante.
4. **Lancar em fases** — 10% primeiro, 24h de monitoramento, full rollout se estavel.
5. **Monitorar diariamente** — Primary metric + guardrails. Pausar se guardrail estoura.
6. **Analise final** — Significancia estatistica (p<0.05) + magnitude + side effects.
7. **Documentar e registrar decisao** — Kill/continue/scale + adicionar a learnings_library.

## Veto Conditions

- VETO se experimento nao tiver grupo controle → nao e experimento, e implementacao
- VETO se decidir antes de amostra minima → ruido vira conclusao
- VETO se ignorar guardrail estourado → experimento estraga metrica vizinha
- VETO se learnings_library nao for alimentada → squad reaprende de zero

## Output Example

```yaml
experiment_cycle:
  sprint_atual: "Sprint 12"
  experimentos_rodando: 3

  lista:
    - exp_id: EXP-12A
      hipotese: "Chat AI no onboarding sobe ativacao 14d de 60% para 75%"
      status: "running (week 2 of 2)"
      owner: "@experimentation-analyst"
      progress: "72% amostra minima atingida"

    - exp_id: EXP-12B
      hipotese: "Carousel com case real aumenta CTR Instagram de 1.8% para 2.5%"
      status: "running (week 1 of 2)"
      owner: "@experimentation-analyst"
      progress: "40% amostra minima atingida"

    - exp_id: EXP-12C
      hipotese: "Email de welcome com video sobe ativacao D+3 de 40% para 55%"
      status: "setup"
      owner: "@experimentation-analyst"
      lancamento: "2026-05-08"

  proximos_do_backlog:
    - "Programa de referral 10% discount"
    - "Demo assincrona via Loom como pre-SQL"
    - "Dynamic pricing por volume"

decision_log:
  semana_atual:
    - exp_id: EXP-11A
      resultado: "PASS"
      decisao: "SCALE"
      dados: "Uplift +9.6pp significativo (p=0.012), guardrails OK"

    - exp_id: EXP-11B
      resultado: "FAIL"
      decisao: "KILL"
      dados: "Variante inferior ao controle em 5%, kill_criteria ativado"
      aprendizado: "Single CTA superior a multiple CTA para nosso ICP"

    - exp_id: EXP-11C
      resultado: "INCONCLUSIVO"
      decisao: "ESTENDER 1 semana"
      dados: "Diferenca dentro da margem de erro, amostra insuficiente"

learnings_library:
  aquisicao:
    - learning: "Carousel Instagram tem CTR 2x maior que single image para nosso ICP"
      data: "2026-03-15"
      experimento: "EXP-09A"
      confianca: "alta"

    - learning: "LinkedIn posts >500 chars performam 40% melhor que curtos"
      data: "2026-02-20"
      experimento: "EXP-07B"
      confianca: "media"

  ativacao:
    - learning: "Email de boas-vindas com video aumenta engajamento 30%"
      data: "2026-04-10"
      experimento: "EXP-10C"
      confianca: "alta"

  retention:
    - learning: "Check-in D+14 via call reduz churn em 20%"
      data: "2026-03-28"
      experimento: "EXP-08A"
      confianca: "alta"

  conversao:
    - learning: "Remocao de campos opcionais em form reduz friccao 15%"
      data: "2026-04-05"
      experimento: "EXP-10A"
      confianca: "alta"

cadencia_execucao:
  segunda: "Review sprint anterior + kick-off experimentos novos"
  terca_quinta: "Monitoramento diario + ajustes"
  sexta: "Analise final + decisoes + documentacao"
```

## Completion Criteria

- 2-3 experimentos rodando por sprint (nao mais)
- Cada experimento tem hipotese + controle + guardrails + amostra minima + kill criteria
- Decisao final baseada em significancia estatistica (p<0.05)
- Learnings documentados (positivos e negativos) para reuso futuro

## Handoff

Resultados viram input para `@growth-senior-manager *run-growth-operations`. Learnings validados alimentam `@cgo-growth-director *prioritize-growth-bets` como heuristics. Experimentos bem-sucedidos escalam via `@revops-automation-engineer`.
