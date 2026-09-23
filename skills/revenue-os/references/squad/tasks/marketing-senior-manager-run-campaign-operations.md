---
task: Run Campaign Operations
responsavel: "@marketing-senior-manager"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - channel_portfolio: Portfolio de canais com metas por canal
  - marketing_masterplan: Masterplan com pilares narrativos
  - available_assets: Criativos e content disponiveis
Saida: |
  - campaign_ops_plan: Plano de operacao de campanhas (calendario + asset map)
  - monitoring_routine: Rotina de monitoramento (KPIs diarios + semanais)
  - creative_refresh_cycle: Ciclo de troca de criativos
Checklist:
  - "[ ] Definir calendario de campanhas (4-6 semanas a frente)"
  - "[ ] Mapear asset por campanha (criativo + landing + email)"
  - "[ ] Definir rotina diaria e semanal de monitoramento"
  - "[ ] Definir ciclo de refresh de criativos (fadiga)"
---

# *run-campaign-operations

Operacionaliza campanhas nos canais priorizados com rotina de monitoramento.

## Step-by-Step

1. **Absorver portfolio** — Ler `channel_portfolio` + metas por canal.
2. **Montar calendario de campanhas** — 4-6 semanas a frente. Por canal + por semana + tema.
3. **Mapear assets necessarios** — Para cada campanha: criativos, landing pages, email sequences, copy.
4. **Checar gaps de assets** — O que existe? O que falta? Acionar `@marketing-senior-analyst` para producao.
5. **Montar rotina de monitoramento** — Diaria: CPM/CPC/CTR/CPL. Semanal: CAC/conversao/qualidade SQL.
6. **Definir refresh cycle** — Criativos tem vida util de 2-4 semanas. Planejar substituicao antes da fadiga.
7. **Configurar alertas** — Dashboard dispara alerta se KPI sair do range por 2 dias.

## Veto Conditions

- VETO se calendario exceder 6 semanas a frente → muita antecipacao vira desperdicio quando contexto muda
- VETO se alguma campanha lanca sem assets validados → campanha falha por problema evitavel
- VETO se nao houver refresh cycle definido → fadiga de criativo mata performance
- VETO se KPI diario nao puder ser monitorado no dashboard → operacao vira cega

## Output Example

```yaml
campaign_ops_plan:
  calendario:
    - semana: "S1 (05-11 Mai)"
      canal: "Paid Instagram"
      tema: "Case: 14 dias ate primeira venda"
      assets: ["creative-carousel-01", "lp-case-study", "email-seq-demo"]
      budget: "R$ 7.500"
      meta_sqls: 50

    - semana: "S2 (12-18 Mai)"
      canal: "Paid Instagram"
      tema: "Stack comercial completa"
      assets: ["creative-video-01", "lp-feature-stack"]
      budget: "R$ 7.500"
      meta_sqls: 50

    - semana: "S1 (05-11 Mai)"
      canal: "Linkedin organic"
      tema: "Governanca CRO/CCO/CMO/CGO"
      assets: ["linkedin-post-01", "linkedin-post-02", "linkedin-post-03"]
      meta_sqls: 30

monitoring_routine:
  diario_09h:
    kpis: [impressoes, CPM, CPC, CTR, CPL]
    acao_se_fora_range: "Analista investiga em 2h"
  semanal_segunda:
    kpis: [CAC_por_canal, qualidade_SQL, conversao_LP]
    acao: "Decisao de manter/aumentar/reduzir budget"

creative_refresh_cycle:
  vida_util_padrao: "3 semanas"
  fadiga_trigger: "CTR cai >20% em 7 dias"
  refresh_pipeline: "Sempre ter 2 criativos em teste + 2 em fila"

alertas:
  - kpi: "CPL"
    range_esperado: "R$ 50-80"
    alerta: "Se >R$ 120 por 2 dias"
  - kpi: "CTR"
    range_esperado: "1.5%-3%"
    alerta: "Se <1% por 2 dias"
```

## Completion Criteria

- Calendario com 4-6 semanas mapeadas
- Cada campanha tem assets identificados e validados
- Rotina diaria + semanal com owner claro
- Refresh cycle definido com trigger de fadiga

## Handoff

`@marketing-senior-analyst` executa producao de criativos e monitora KPIs diarios. Reporta para `@cmo-marketing-director` semanalmente.
