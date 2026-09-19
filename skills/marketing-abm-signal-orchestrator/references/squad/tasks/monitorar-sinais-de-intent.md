---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Account Universe Map (lista de contas Tier 1/2), configuracao de fontes de intent, thresholds de scoring por tipo de sinal, webhooks de Clay/Apollo/HubSpot"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Intent Signal Alert (JSON estruturado): conta_id, tipo_de_sinal, intensidade (1-10), stakeholders_envolvidos, fonte, timestamp, contexto_raw, recommended_tier_action"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de novo sinal nas fontes configuradas; job scheduling diário para varredura de fontes que não tem webhook; alerta de mudança de status de conta no CRM"
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

# Monitorar Sinais De Intent

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais De Intent |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Agente de Sinais de Intent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente fontes de intent (Clay, Apollo, Bombora, job postings, funding news, tech stack changes, visitas ao site, engajamento com conteudo) para as contas do Account Universe. Qualifica e escora sinais brutos, filtra falsos positivos, e dispara alertas estruturados para o Nexus quando threshold de intent e atingido.

## Input

- Account Universe Map (lista de contas Tier 1/2), configuracao de fontes de intent, thresholds de scoring por tipo de sinal, webhooks de Clay/Apollo/HubSpot

## Output

- Intent Signal Alert (JSON estruturado): conta_id, tipo_de_sinal, intensidade (1-10), stakeholders_envolvidos, fonte, timestamp, contexto_raw, recommended_tier_action

## Trigger

Webhook de novo sinal nas fontes configuradas; job scheduling diário para varredura de fontes que não tem webhook; alerta de mudança de status de conta no CRM

## Knowledge base (o que o executor consulta)

- Account Universe Map atualizado, histórico de sinais por conta, thresholds calibrados por vertical, lista de stakeholders mapeados por conta, dicionário de sinais de compra por ICP

## Action Items

1. Confirmar o gatilho e carregar a entrada (Account Universe Map (lista de contas Tier 1/2), configuracao de fontes de intent, thresholds de scoring por tipo de si…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Intent Signal Alert (JSON estruturado): conta_id, tipo_de_sinal, intensidade (1-10), stakeholders_envolvidos, fonte, ti…) e persistir no artefato do squad.
4. Entregar ao critic Aegis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Intent Signal Alert (JSON estruturado): conta_id, tipo_de_sinal, intensidade (1-10), stakeholders_envolvidos, fonte, timestamp, contexto_raw, recommended_tier_…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
