---
task: Design Commercial Strategy
responsavel: "@cco-commercial-director"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - macro_plan: Plano macro CRO com meta trimestral
  - icp_profile: ICP definido e validado
Saida: |
  - commercial_strategy: Tese comercial + segmentos + abordagem por canal
  - partnership_agenda: Lista priorizada de parcerias com briefs
  - sales_targets_per_segment: Metas por segmento (volume + ticket medio)
Checklist:
  - "[ ] Definir tese comercial (porque comprar agora)"
  - "[ ] Segmentar ICP em 2-4 buckets com prioridade"
  - "[ ] Definir abordagem por segmento (inbound/outbound/parcerias)"
  - "[ ] Listar top 5 parcerias com brief de abordagem"
  - "[ ] Metas numericas por segmento"
---

# *design-commercial-strategy

Define a estrategia comercial macro da area: tese, segmentos, abordagens e parcerias.

## Step-by-Step

1. **Absorver macro_plan** — Ler meta trimestral e mensal.
2. **Formular tese comercial** — "Por que nosso ICP deveria comprar AGORA?" em 1-2 frases.
3. **Segmentar ICP** — Dividir em 2-4 buckets com: tamanho, dor especifica, valor percebido.
4. **Priorizar segmentos** — Matriz tamanho x facilidade de aquisicao. Comecar onde o 80/20 esta.
5. **Definir abordagem por segmento** — Inbound (content + SEO), Outbound (prospeccao ativa), Parcerias (referral), PLG (self-service).
6. **Mapear top parcerias** — 5 parceiros potenciais que ja tem acesso ao ICP.
7. **Definir metas por segmento** — Volume mensal + ticket medio + conversao esperada.

## Veto Conditions

- VETO se tese comercial for generica ("temos o melhor produto") → refazer com angle especifico ao ICP
- VETO se >4 segmentos priorizados → diluicao, cortar para 2-3
- VETO se nenhum segmento tiver abordagem definida → estrategia vira desejo, nao plano

## Output Example

```yaml
commercial_strategy:
  tese: "Founders AIOS que ja construiram produto mas nao sabem vender perdem R$ 50-200k em oportunidades/ano - Revenue OS entrega a primeira venda em 14 dias"

  segmentos_priorizados:
    - segmento: "Founders solo com produto AIOS pronto"
      tamanho_estimado: "~500 pessoas na cohort"
      dor: "Sabe construir, nao sabe operar vendas"
      abordagem: "Inbound (LinkedIn) + demo assistida"
      ticket_medio: "R$ 3k/mes"
      volume_mensal_target: 8

    - segmento: "Agencias que ja usam AIOS para clientes"
      tamanho_estimado: "~80 agencias"
      dor: "Revenda de servicos sem stack comercial propria"
      abordagem: "Outbound + parceria white-label"
      ticket_medio: "R$ 8k/mes"
      volume_mensal_target: 3

partnership_agenda:
  - parceiro: "Comunidade Lendaria"
    brief: "Affiliate program para membros 100+"
    expected: "10-15 leads/mes"
  - parceiro: "AIOS Cohort Alan"
    brief: "Squad oficial recomendado no onboarding"
    expected: "5-8 leads/mes"

sales_targets_per_segment:
  founders_solo: { volume: 8, ticket: 3000, revenue: 24000 }
  agencias: { volume: 3, ticket: 8000, revenue: 24000 }
  total_mensal: 48000
```

## Completion Criteria

- Tese comercial em 1-2 frases especificas (nao generica)
- 2-4 segmentos com dor + abordagem + metas
- Top 5 parcerias com brief e expectativa numerica
- Soma das metas por segmento = meta mensal do macro_plan

## Handoff

Estrategia passa para `@commercial-senior-manager` traduzir em operacao. Parcerias viram backlog de `@commercial-senior-analyst`.
