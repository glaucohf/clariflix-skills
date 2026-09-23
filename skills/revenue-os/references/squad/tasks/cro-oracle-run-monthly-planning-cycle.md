---
task: Run Monthly Planning Cycle
responsavel: "@cro-oracle-guardian"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - monthly_results: Resultado mensal consolidado (MRR, CAC, churn, conversao por canal)
  - next_month_target: Meta do mes seguinte vinda do macro_revenue_plan
  - weekly_actions_log: Historico de acoes semanais e outcomes
Saida: |
  - monthly_plan: Plano mensal atualizado com frentes e owners
  - reallocation_map: Rebalanceamento de recursos (budget, time, foco)
  - lessons_learned: Aprendizados do mes que alteram politica
Checklist:
  - "[ ] Consolidar aprendizados mensais (o que funcionou + o que nao)"
  - "[ ] Repriorizar portfolio (matar/escalar/iterar)"
  - "[ ] Rebalancear budget entre canais/frentes"
  - "[ ] Confirmar plano do mes seguinte com owners"
  - "[ ] Atualizar macro_revenue_plan se meta trimestral estiver em risco"
---

# *run-monthly-planning-cycle

Executa ciclo mensal de planejamento orientado por resultado e realocacao de foco.

## Step-by-Step

1. **Consolidar resultados** — Ler `monthly_results` e comparar com meta mensal do macro_revenue_plan.
2. **Analisar variancia** — Calcular `delta = atual - meta`. Categorizar: superamos, bateu, 80-99%, <80%.
3. **Extrair lessons_learned** — Para cada frente (CCO/CMO/CGO), 1-3 aprendizados do mes.
4. **Aplicar regra matar/escalar/iterar** — Cada experimento/canal/frente recebe veredito:
   - Matar se ROI < 0 ou nao tem caminho de melhoria clara
   - Escalar se ROI > target + pipeline de escala ja testado
   - Iterar se ROI positivo mas nao batendo target (max 2 iteracoes antes de matar)
5. **Rebalancear budget** — Mover % de budget de frentes "matar/iterar" para "escalar".
6. **Atualizar macro_revenue_plan se necessario** — Se projetado nao bate meta trimestral, replanejar decomposicao.
7. **Confirmar plano com owners** — Apresentar plano do mes seguinte, coletar ajustes, aprovar.

## Veto Conditions

- VETO se `monthly_results` estiver incompleto (faltam KPIs chave) → acionar revops para completar
- VETO se 100% das frentes forem "escalar" → provavel viés de confirmacao, revisar com devil's advocate
- VETO se rebalanceamento mover >50% do budget de uma unica decisao → muito agressivo, dividir em 2 meses
- VETO se meta trimestral estiver em risco >20% e nenhum plano de recuperacao definido

## Output Example

```yaml
monthly_plan:
  mes: M2
  meta_mensal: "R$ 35k MRR novo"
  frentes:
    - frente: "Paid social Instagram"
      veredito: escalar
      budget_novo: "R$ 15k (+50%)"
      owner: "@cmo-marketing-director"
    - frente: "LinkedIn outbound"
      veredito: matar
      razao: "CAC 3x maior que breakeven apos 6 semanas"
    - frente: "Webinar evergreen"
      veredito: iterar
      hipotese: "Reduzir duracao de 60min -> 30min para aumentar watch rate"
      owner: "@cgo-growth-director"
      deadline_teste: "2026-05-15"

reallocation_map:
  de: { "LinkedIn outbound": "R$ 8k" }
  para: { "Paid social Instagram": "R$ 5k", "Email nurturing upgrade": "R$ 3k" }

lessons_learned:
  - "Paid social tem escala saudavel ate R$ 20k/mes sem degradar CAC"
  - "Outbound frio em LinkedIn nao funciona para nosso ICP (preferem inbound)"
  - "Webinars longos perdem >50% audiencia nos 15 min iniciais"
```

## Completion Criteria

- Cada frente tem veredito (matar/escalar/iterar) com razao documentada
- Rebalanceamento de budget soma zero (o que sai de um lugar entra em outro)
- Plano do mes seguinte com frentes + owners + budget aprovado
- Log atualizado com decisoes + aprendizados

## Handoff

Plano mensal distribuido para CCO/CMO/CGO via `wf-cro-command-chain`. Primeiro `*control-weekly-metrics` do novo mes agendado para 1 semana.
