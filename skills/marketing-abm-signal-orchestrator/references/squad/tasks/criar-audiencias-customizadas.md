---
task: pixel()
responsavel: "Pixel"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "ABM Copy Package (assets de ad copy), lista de contas ativas com stakeholders (emails, domínios, LinkedIn URLs para custom audiences), budget aprovado por conta Tier, assets criativos da fábrica UGC, configuração de plataformas (Meta Business, Google Ads, LinkedIn Campaign Manager)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Campanhas ativas nas plataformas configuradas, relatório de impressões/cliques/engajamento por conta, alertas de conta com engajamento elevado (sinal de intent reforço), sugestão de reallocation de budget"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Aprovação humana (L3) de campanha ABM para conta específica; alerta de engajamento elevado em conta Tier 1 (reforço de bid); fim de ciclo mensal (revisão de budget)"
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

# Criar Audiências Customizadas

**Task ID:** `pixel()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Criar Audiências Customizadas |
| **status** | `pending` |
| **responsible_executor** | Pixel (Pixel — Agente de Ads e Media Programática) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Configura e gerencia campanhas de anuncio direcionadas especificamente para as contas-alvo ativadas (Account-Based Advertising). Cria audiencias customizadas no Meta/Google/LinkedIn baseadas na lista de contas e stakeholders, faz bid/budget pacing, rota creativos por fase do funil (awareness vs consideracao vs decisao), e otimiza baseado em sinal de engajamento da conta.

## Input

- ABM Copy Package (assets de ad copy), lista de contas ativas com stakeholders (emails, domínios, LinkedIn URLs para custom audiences), budget aprovado por conta Tier, assets criativos da fábrica UGC, configuração de plataformas (Meta Business, Google Ads, LinkedIn Campaign Manager)

## Output

- Campanhas ativas nas plataformas configuradas, relatório de impressões/cliques/engajamento por conta, alertas de conta com engajamento elevado (sinal de intent reforço), sugestão de reallocation de budget

## Trigger

Aprovação humana (L3) de campanha ABM para conta específica; alerta de engajamento elevado em conta Tier 1 (reforço de bid); fim de ciclo mensal (revisão de budget)

## Knowledge base (o que o executor consulta)

- Budget caps por conta e Tier, histórico de performance de campanhas ABM anteriores, negative keyword lists, audiências salvas por segmento, benchmarks de CTR/CPL por vertical e formato

## Action Items

1. Confirmar o gatilho e carregar a entrada (ABM Copy Package (assets de ad copy), lista de contas ativas com stakeholders (emails, domínios, LinkedIn URLs para cus…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Campanhas ativas nas plataformas configuradas, relatório de impressões/cliques/engajamento por conta, alertas de conta…) e persistir no artefato do squad.
4. Entregar ao critic Aegis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Campanhas ativas nas plataformas configuradas, relatório de impressões/cliques/engajamento por conta, alertas de conta com engajamento elevado (sinal de intent…
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

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
