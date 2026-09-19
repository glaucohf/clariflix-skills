---
task: hermes()
responsavel: "Hermes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "ABM Copy Package validado pelo Aegis (Critic), Account Intelligence Profile com contatos e canais preferidos, configuração de cadência (N touches, intervalos, canais), credenciais Instantly/Apollo/HubSpot Sequences"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sequências ativas no CRM, log de todos os touches por stakeholder, taxa de abertura/resposta em tempo real, alertas de hot lead (respondeu, clicou 3x, visitou pricing page), handoff estruturado para SDR humano quando engajamento qualifica"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Aprovação humana (L3) de outreach para conta; resposta de prospect (trigger imediato de follow-up); inatividade de 7 dias em stakeholder Tier 1 (nudge automático); handoff de Pixel com conta com alto…"
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

# Sequenciar Contato Multicanal

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sequenciar Contato Multicanal |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — Agente de Outreach e Sequenciamento SDR) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa sequenciamento multicanal personalizado para os stakeholders identificados na conta: email frio via Instantly/Apollo, LinkedIn (connection request + mensagem), e gera briefing estruturado para SDR humano fazer a abordagem via WhatsApp ou ligação. Gerencia cadências, respostas, follow-ups e sinais de engajamento (abertura, clique, resposta) para ajustar timing e canal.

## Input

- ABM Copy Package validado pelo Aegis (Critic), Account Intelligence Profile com contatos e canais preferidos, configuração de cadência (N touches, intervalos, canais), credenciais Instantly/Apollo/HubSpot Sequences

## Output

- Sequências ativas no CRM, log de todos os touches por stakeholder, taxa de abertura/resposta em tempo real, alertas de hot lead (respondeu, clicou 3x, visitou pricing page), handoff estruturado para SDR humano quando engajamento qualifica

## Trigger

Aprovação humana (L3) de outreach para conta; resposta de prospect (trigger imediato de follow-up); inatividade de 7 dias em stakeholder Tier 1 (nudge automático); handoff de Pixel com conta com alto engajamento em ads

## Knowledge base (o que o executor consulta)

- Cadencia padrao por Tier de conta, historico de respostas e taxas de engajamento por copy variant, lista de opt-outs e DNC, SLA de resposta por canal, playbook de objecoes frequentes por persona

## Action Items

1. Confirmar o gatilho e carregar a entrada (ABM Copy Package validado pelo Aegis (Critic), Account Intelligence Profile com contatos e canais preferidos, configura…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sequências ativas no CRM, log de todos os touches por stakeholder, taxa de abertura/resposta em tempo real, alertas de…) e persistir no artefato do squad.
4. Entregar ao critic Aegis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sequências ativas no CRM, log de todos os touches por stakeholder, taxa de abertura/resposta em tempo real, alertas de hot lead (respondeu, clicou 3x, visitou…
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

- **to:** Chronos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
