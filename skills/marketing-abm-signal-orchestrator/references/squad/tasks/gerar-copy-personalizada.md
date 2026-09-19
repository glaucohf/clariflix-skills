---
task: vox()
responsavel: "Vox"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Account Intelligence Profile, ICP messaging framework, brand voice guidelines, histórico de copy de alta performance por segmento, sinal de intent específico que disparou a campanha"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "ABM Copy Package: email sequences (3 variantes x 3 touches por stakeholder), LinkedIn messages, ad copy (5 variantes por formato), subject lines testadas (10 opções), call scripts para SDR, landing page copy customizada por conta"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Account Intelligence Profile validado pelo Atlas; solicitação de refresh de mensagem por baixa performance (CTR < 2%); nova persona identificada na conta"
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

# Gerar Copy Personalizada

**Task ID:** `vox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Copy Personalizada |
| **status** | `pending` |
| **responsible_executor** | Vox (Vox — Agente de Copy e Mensagem ABM) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe Account Intelligence Profile e gera assets de copy personalizados para cada stakeholder da conta: assunto e corpo de email frio (3 variantes), mensagem LinkedIn (conexão + follow-up), copy de anúncio display/social (headline + body + CTA, 5 variantes), e sequência de nurture (3 touches). Todo copy é ancorado em sinais específicos da conta (ex: mencionando o funding round ou a nova contratação de VP).

## Input

- Account Intelligence Profile, ICP messaging framework, brand voice guidelines, histórico de copy de alta performance por segmento, sinal de intent específico que disparou a campanha

## Output

- ABM Copy Package: email sequences (3 variantes x 3 touches por stakeholder), LinkedIn messages, ad copy (5 variantes por formato), subject lines testadas (10 opções), call scripts para SDR, landing page copy customizada por conta

## Trigger

Account Intelligence Profile validado pelo Atlas; solicitação de refresh de mensagem por baixa performance (CTR < 2%); nova persona identificada na conta

## Knowledge base (o que o executor consulta)

- Brand voice guidelines, ICP messaging framework por persona (Champion vs Economic Buyer vs Technical), biblioteca de copy de alta performance histórico, framework de personalização 1:1 (mencionar sinal específico da conta), playbooks de mensagem por vertical

## Action Items

1. Confirmar o gatilho e carregar a entrada (Account Intelligence Profile, ICP messaging framework, brand voice guidelines, histórico de copy de alta performance po…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (ABM Copy Package: email sequences (3 variantes x 3 touches por stakeholder), LinkedIn messages, ad copy (5 variantes po…) e persistir no artefato do squad.
4. Entregar ao critic Aegis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: ABM Copy Package: email sequences (3 variantes x 3 touches por stakeholder), LinkedIn messages, ad copy (5 variantes por formato), subject lines testadas (10 o…
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

- **to:** Pixel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
