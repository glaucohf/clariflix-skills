---
task: Build Acquisition Plan
responsavel: "@demand-gen-architect"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - icp_profile: Segmentos alvo
  - revenue_goal: Meta de receita trimestral
  - channel_portfolio: Portfolio de canais priorizado (saida do CMO)
Saida: |
  - acquisition_plan: Plano detalhado de aquisicao por canal
  - campaign_calendar: Calendario de campanhas 4-6 semanas a frente
  - budget_allocation: Alocacao de budget por canal + contingencia
Checklist:
  - "[ ] Calcular SQLs necessarios a partir da meta de receita"
  - "[ ] Distribuir volume de leads por canal"
  - "[ ] Definir CAC target por canal"
  - "[ ] Criar calendario de campanhas com tema semanal"
---

# *build-acquisition-plan

Cria plano de aquisicao para gerar demanda qualificada alinhada com meta de receita.

## Step-by-Step

1. **Calcular SQLs necessarios** — Meta de receita / ticket medio = clientes. Clientes / conversao SQL->cliente = SQLs.
2. **Distribuir por canal** — Baseado em channel_portfolio e performance historica.
3. **Definir CAC target** — CAC maximo sustentavel = LTV / 3 (regra 3:1 minimum).
4. **Calcular budget por canal** — SQLs_canal * CAC_canal = budget_canal.
5. **Montar calendario** — 4-6 semanas com tema por semana + canal + volume esperado.
6. **Definir contingencia** — 10-15% do budget reservado para emergencia (kill canal, double down em winner).
7. **Validar consistencia** — Soma SQLs por canal = total necessario + 20% buffer.

## Veto Conditions

- VETO se CAC target for >LTV/3 → unidade economica nao fecha
- VETO se algum canal exceder 70% da dependencia → risco de um unico ponto de falha
- VETO se orcamento total exceder 30% da receita esperada
- VETO se calendario nao cobrir pelo menos 4 semanas → planejamento reativo demais

## Output Example

```yaml
acquisition_plan:
  meta_receita_trimestral: "R$ 100k MRR"
  ticket_medio: "R$ 3.000"
  clientes_necessarios: 34
  conversao_sql_cliente: "25%"
  sqls_necessarios: 136
  sqls_com_buffer_20: 163

  distribuicao_por_canal:
    - canal: "Paid Instagram"
      share: "55%"
      sqls_target: 90
      cac_target: "R$ 375"
      budget: "R$ 33.750"

    - canal: "Linkedin organic"
      share: "25%"
      sqls_target: 41
      cac_target: "R$ 0 (tempo)"
      budget: "R$ 0"

    - canal: "Content SEO"
      share: "15%"
      sqls_target: 25
      cac_target: "R$ 200"
      budget: "R$ 5.000"

    - canal: "Experimentacao"
      share: "5%"
      sqls_target: 7
      cac_target: "N/A (teste)"
      budget: "R$ 3.000"

  total_budget: "R$ 41.750 + contingencia R$ 5.000 = R$ 46.750"

campaign_calendar:
  - semana: "S1-S2"
    tema: "Case: 14 dias ate primeira venda"
    canais_ativos: [paid_ig, linkedin, content]

  - semana: "S3-S4"
    tema: "Stack comercial completa"
    canais_ativos: [paid_ig, linkedin]

  - semana: "S5-S6"
    tema: "Governanca CRO/CCO/CMO/CGO"
    canais_ativos: [paid_ig, linkedin, content]

budget_allocation:
  paid_ig: "R$ 33.750"
  content_seo: "R$ 5.000"
  experimentacao: "R$ 3.000"
  contingencia: "R$ 5.000"
  total: "R$ 46.750"
```

## Completion Criteria

- SQLs calculados matematicamente a partir da meta (nao chute)
- Distribuicao por canal sem dependencia >70% de um unico canal
- CAC target por canal <LTV/3
- Calendario 4-6 semanas com tema e canais ativos por semana
- Contingencia reservada (10-15%)

## Handoff

Plano passa para `@demand-gen-architect *create-campaign-briefs` e `@marketing-senior-manager *run-campaign-operations`. Owners de canal comecam execucao.
