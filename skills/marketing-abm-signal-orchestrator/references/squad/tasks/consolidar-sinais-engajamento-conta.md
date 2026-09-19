---
task: prism()
responsavel: "Prism"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados de engajamento de todos os canais (HubSpot, Meta Ads, Google Ads, LinkedIn, Instantly, ClickUp), pipeline CRM vinculado a contas ABM, Account Universe Map com Tiers"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Account Engagement Dashboard (score por conta, touchpoints, fase do funil), pipeline ABM gerado por período, anomaly alerts, relatório executivo semanal, recomendações de reallocation de esforço (contas com score caindo vs subindo)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Scheduled diário (atualiza scores de conta); novo deal criado no CRM vinculado a conta ABM (atribuição); anomalia detectada em conta Tier 1 (alerta imediato); fim de semana (relatório executivo)"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plataformas de ads"
    - "[ ] L3: Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad"
    - "[ ] L3: Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio"
    - "[ ] L2: Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha completa"
    - "[ ] L2: Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana sobre próximos passos"
---

# Consolidar Sinais Engajamento Conta

**Task ID:** `prism()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Consolidar Sinais Engajamento Conta |
| **status** | `pending` |
| **responsible_executor** | Prism (Prism — Agente de Analytics e Atribuição ABM) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Consolida todos os sinais de engajamento da conta (ads, emails, visitas ao site, LinkedIn, WhatsApp, reuniões agendadas) em uma visão unificada do Account Journey. Atribui pipeline gerado ao programa ABM, detecta anomalias (conta que parou de engajar, stakeholder que mudou de empresa), e gera relatório executivo de performance ABM por semana/mês.

## Input

- Dados de engajamento de todos os canais (HubSpot, Meta Ads, Google Ads, LinkedIn, Instantly, ClickUp), pipeline CRM vinculado a contas ABM, Account Universe Map com Tiers

## Output

- Account Engagement Dashboard (score por conta, touchpoints, fase do funil), pipeline ABM gerado por período, anomaly alerts, relatório executivo semanal, recomendações de reallocation de esforço (contas com score caindo vs subindo)

## Trigger

Scheduled diário (atualiza scores de conta); novo deal criado no CRM vinculado a conta ABM (atribuição); anomalia detectada em conta Tier 1 (alerta imediato); fim de semana (relatório executivo)

## Knowledge base (o que o executor consulta)

- Modelo de atribuição ABM multi-touch, benchmarks de engajamento por fase do funil, histórico de performance de campanhas anteriores, mapeamento conta-oportunidade no CRM, métricas de sucesso do squad (KPIs)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados de engajamento de todos os canais (HubSpot, Meta Ads, Google Ads, LinkedIn, Instantly, ClickUp), pipeline CRM vin…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Account Engagement Dashboard (score por conta, touchpoints, fase do funil), pipeline ABM gerado por período, anomaly al…) e persistir no artefato do squad.
4. Entregar ao critic Aegis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Account Engagement Dashboard (score por conta, touchpoints, fase do funil), pipeline ABM gerado por período, anomaly alerts, relatório executivo semanal, recom…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis registrado
- [ ] Gate L3 respeitado: Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto…
- [ ] Gate L3 respeitado: Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi c…
- [ ] Gate L3 respeitado: Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plata… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha c… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana s… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Curadoria do Account Universe Map: adicionar/remover contas do universo ABM e ajustar Tiers requer input estratégico humano (revisão quinzenal) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Aegis | BLOQUEIA entrega |

## Handoff

- **to:** Aegis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
