---
task: atlas()
responsavel: "Atlas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Intent Signal Alert, Account Universé Map, ICP définition doc, crédenciais Clay/Apollo/Cognism"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Account Intelligence Profile: empresa (tech stack, financiamento, headcount, notícias recentes), buying committee (nome, cargo, LinkedIn, email, telefone, histórico de interações CRM), ICP score 0-100, recommended messaging angle, next best action por stakeholder"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Intent Signal Alert de Radar com intensidade >= 6; solicitação manual do Nexus para conta específica; scheduled refresh semanal para contas Tier 1 ativas"
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

# Enriquecer Conta Icp

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Conta Icp |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Agente de Enriquecimento e ICP Profiler) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Ao receber um Intent Signal Alert, executa cascata de enriquecimento da conta via Clay waterfall (100+ fontes: LinkedIn, Crunchbase, BuiltWith, Apollo, Cognism, web scraping). Mapeia buying committee completo (Champion, Economic Buyer, Technical Evaluator, Blocker), escora fit de ICP em 5 dimensões (setor, porte, maturidade tecnológica, budget signals, timing), e gera Account Intelligence Profile pronto para personalização.

## Input

- Intent Signal Alert, Account Universé Map, ICP définition doc, crédenciais Clay/Apollo/Cognism

## Output

- Account Intelligence Profile: empresa (tech stack, financiamento, headcount, notícias recentes), buying committee (nome, cargo, LinkedIn, email, telefone, histórico de interações CRM), ICP score 0-100, recommended messaging angle, next best action por stakeholder

## Trigger

Intent Signal Alert de Radar com intensidade >= 6; solicitação manual do Nexus para conta específica; scheduled refresh semanal para contas Tier 1 ativas

## Knowledge base (o que o executor consulta)

- ICP definition doc com critérios de fit, mapeamento de personas por vertical, histórico de enriquecimentos anteriores, templates de Account Intelligence Profile, scoring rubric por dimensão

## Action Items

1. Confirmar o gatilho e carregar a entrada (Intent Signal Alert, Account Universé Map, ICP définition doc, crédenciais Clay/Apollo/Cognism).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Account Intelligence Profile: empresa (tech stack, financiamento, headcount, notícias recentes), buying committee (nome…) e persistir no artefato do squad.
4. Entregar ao critic Aegis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Account Intelligence Profile: empresa (tech stack, financiamento, headcount, notícias recentes), buying committee (nome, cargo, LinkedIn, email, telefone, hist…
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

- **to:** Vox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
