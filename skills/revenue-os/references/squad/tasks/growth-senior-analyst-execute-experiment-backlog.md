---
task: Execute Experiment Backlog
responsavel: "@growth-senior-analyst"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - growth_ops_cycle: Sprint de growth com experimentos
  - experiment_tracker: Tracker ativo com status de cada experimento
  - instrumentation_access: Acesso a dashboard + ferramentas de teste
Saida: |
  - experiment_results_log: Log detalhado de cada experimento com resultados
  - statistical_significance: Analise de significancia estatistica
  - recommendation_per_experiment: Kill / continue / scale
Checklist:
  - "[ ] Setup do experimento (instrumentacao, split de audiencia)"
  - "[ ] Rodar experimento por periodo minimo definido"
  - "[ ] Registrar resultados diariamente no tracker"
  - "[ ] Analise de significancia ao final"
  - "[ ] Recomendacao kill/continue/scale"
---

# *execute-experiment-backlog

Executa experimentos priorizados do sprint de growth com rigor estatistico.

## Step-by-Step

1. **Setup do experimento** — Instrumentar tracking, definir split de audiencia (controle vs tratamento), validar com manager.
2. **Calcular tamanho minimo da amostra** — Baseado em baseline + uplift esperado + significancia (95%).
3. **Lancar em ambiente controlado** — Rollout para 10% primeiro, monitorar 24h, depois full rollout.
4. **Monitorar diariamente** — KPIs primario + guardrails. Se guardrail estourar, pausar.
5. **Aguardar periodo minimo** — Nao decidir antes de ter tamanho de amostra suficiente.
6. **Analise final** — Significancia estatistica + magnitude do efeito + side effects.
7. **Recomendacao** — Kill (falhou), Continue (ainda inconclusivo, estender), Scale (sucesso, deploy full).

## Veto Conditions

- VETO se decidir antes de amostra minima → conclusao e ruido, nao sinal
- VETO se ignorar guardrail estourado → experimento prejudica outras metricas
- VETO se nao tiver grupo controle → sem comparacao, nao ha experimento
- VETO se recomendacao for "continue" >2 vezes para mesmo experimento → vira zumbi, forcar decisao

## Output Example

```yaml
experiment_results_log:
  experimento_id: EXP-12A
  titulo: "Chat AI no onboarding sobe ativacao 14d"

  setup:
    baseline_atual: "60% ativacao 14d"
    target: "75%"
    minimum_sample: "400 usuarios por grupo (controle + tratamento)"
    duracao_planejada: "2 semanas"

  execucao:
    data_inicio: "2026-05-06"
    data_fim: "2026-05-18"
    usuarios_controle: 412
    usuarios_tratamento: 398

  resultados:
    controle:
      ativacao_14d: "59.2%"
      nps: "42"
      tickets_suporte: 18
    tratamento:
      ativacao_14d: "68.8%"
      nps: "44"
      tickets_suporte: 22

  analise:
    uplift: "+9.6 pontos percentuais (+16.2% relativo)"
    significancia: "p-value = 0.012 (significativo, 95% confianca)"
    magnitude: "Menor que target (75%) mas positiva"
    guardrails:
      nps: "OK (subiu marginalmente)"
      tickets_suporte: "OK (aumento 22% dentro do guardrail de 30%)"

statistical_significance:
  test_usado: "Chi-square para proporcoes"
  p_value: 0.012
  confidence_interval: "95%"
  is_significant: true

recommendation_per_experiment:
  experimento_id: EXP-12A
  recomendacao: scale
  justificativa: |
    Significativo (p=0.012), uplift de 9.6pp eleva ativacao de 60% para 68.8%.
    Abaixo do target de 75% mas muito acima do baseline. Guardrails OK.
    Recomendacao: deploy full e iniciar experimento de refinamento (EXP-13A) para alcancar 75%.
```

## Completion Criteria

- Experimento rodou por periodo minimo com amostra suficiente
- Significancia estatistica calculada (p-value + CI)
- Guardrails monitorados e OK (ou experimento foi pausado)
- Recomendacao clara com justificativa

## Handoff

Resultados entregues no sprint review (sexta). `@growth-senior-manager` toma decisao final junto com `@cgo-growth-director`. Se scale, handoff para `@revops-automation-engineer` deployar full.
