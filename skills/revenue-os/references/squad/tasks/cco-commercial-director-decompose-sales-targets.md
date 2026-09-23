---
task: Decompose Sales Targets
responsavel: "@cco-commercial-director"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - revenue_target: Meta de receita (trimestral ou mensal)
  - commercial_strategy: Segmentos priorizados com targets
  - conversion_rates: Taxas de conversao historicas ou benchmark
Saida: |
  - sales_target_tree: Arvore hierarquica de metas (time -> canal -> periodo)
  - weekly_quotas: Quotas semanais por executor
  - activity_targets: Metas de atividade (leads, demos, propostas) que sustentam a meta de receita
Checklist:
  - "[ ] Quebrar meta mensal em semanal"
  - "[ ] Definir quota por frente e executor"
  - "[ ] Calcular atividades necessarias a partir de conversion_rates"
  - "[ ] Validar que soma das quotas = meta total"
---

# *decompose-sales-targets

Desdobra metas comerciais em quotas operacionais executaveis por semana e executor.

## Step-by-Step

1. **Validar entrada** — Meta numerica clara + conversion_rates disponiveis.
2. **Decompor mensal -> semanal** — Regra: semana 1 e 4 tendem a ser mais leves, semanas 2-3 mais pesadas.
3. **Distribuir por segmento** — Usar targets do `commercial_strategy` para cada segmento.
4. **Calcular atividades necessarias** — Trabalhar para tras a partir da meta: vendas / conversao = demos -> demos / conversao = SQLs -> etc.
5. **Atribuir quotas por executor** — Cada analista/manager tem quota clara.
6. **Validar soma** — Soma das quotas individuais = meta total (sem furo nem sobreposicao).
7. **Publicar no CRM** — Quotas viram targets visiveis no dashboard.

## Veto Conditions

- VETO se soma das quotas for diferente da meta total (>5% de variancia)
- VETO se conversion_rates nao existirem e nao houver benchmark do segmento → calcular atividades vira chute
- VETO se algum executor ficar com quota >150% da media → burnout garantido

## Output Example

```yaml
sales_target_tree:
  meta_mensal: "R$ 48.000 novo MRR"
  por_segmento:
    founders_solo:
      meta: "R$ 24.000 (8 clientes x R$ 3k)"
      executor: "@commercial-senior-analyst (Ana)"
      quota_semanal: "2 vendas/semana"
    agencias:
      meta: "R$ 24.000 (3 clientes x R$ 8k)"
      executor: "@commercial-senior-manager (Bruno)"
      quota_semanal: "~1 venda/semana"

activity_targets:
  founders_solo:
    vendas_mes: 8
    demos_mes: 32  # 25% conversao
    sqls_mes: 128  # 25% conversao
    leads_mes: 640  # 20% conversao
  agencias:
    vendas_mes: 3
    demos_mes: 15
    sqls_mes: 60
    leads_mes: 200

weekly_quotas:
  "@commercial-senior-analyst":
    leads_qualificados: 32
    demos_realizadas: 8
    vendas_fechadas: 2
  "@commercial-senior-manager":
    leads_qualificados: 12
    demos_realizadas: 4
    vendas_fechadas: 1
```

## Completion Criteria

- Metas decompostas em 4 semanas com distribuicao realista
- Cada executor tem quota semanal (leads/demos/vendas)
- Atividades calculadas a partir de conversion_rates (nao chute)
- Soma das quotas = 100% da meta mensal

## Handoff

Quotas publicadas no CRM + dashboard. `@commercial-senior-manager` operacionaliza rotina semanal. Revisao em `*control-weekly-metrics`.
