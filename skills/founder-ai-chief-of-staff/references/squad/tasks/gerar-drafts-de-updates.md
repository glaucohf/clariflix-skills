---
task: memo()
responsavel: "Memo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados de métricas (dashboard financeiro, CRM, produto)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Agenda do board/investor meeting"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Notas de reuniões anteriores"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "OKRs e status do quarter"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Input do founder sobre narrativa e contexto político"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Draft de board pack (Notion/PDF): sumário executivo, highlights do período, métricas-chave com commentary, desafios e plano, próximos passos"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Pronto para revisão final do founder antes de qualquer envio"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: 30 dias antes de board meeting. Investor solicita update. Founder aciona manualmente para deal memo ou strategic update. Milestone relevante atingido (rodada, produto, expansão)."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Skeptic antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design"
    - "[ ] HITL: Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas)"
    - "[ ] HITL: Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado"
    - "[ ] HITL: Aprovação de escalation quando follow-up crítico está atrasado e envolve terceiros externos"
    - "[ ] HITL: Validação do Founder Clone Agent antes de qualquer resposta ser enviada em nome do founder"
---

# Gerar Drafts De Updates

**Task ID:** `memo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI Chief of Staff — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Drafts De Updates |
| **status** | `pending` |
| **responsible_executor** | Memo (Memo — Board & Investor Communications) |
| **execution_type** | `Hybrid` |
| **input** | 5 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Coleta sinais de performance (métricas, pipeline, hiring, produto) e gera drafts de board updates, memos de investor e executive summaries. Garante que cada afirmação é rastreável a uma fonte verificada. Nunca envia — entrega rascunho para revisão e aprovação do founder (L3).

## Input

- Dados de métricas (dashboard financeiro, CRM, produto)
- Agenda do board/investor meeting
- Notas de reuniões anteriores
- OKRs e status do quarter
- Input do founder sobre narrativa e contexto político

## Output

- Draft de board pack (Notion/PDF): sumário executivo, highlights do período, métricas-chave com commentary, desafios e plano, próximos passos
- Pronto para revisão final do founder antes de qualquer envio

## Trigger

30 dias antes de board meeting. Investor solicita update. Founder aciona manualmente para deal memo ou strategic update. Milestone relevante atingido (rodada, produto, expansão).

## Knowledge base (o que o executor consulta)

- Dashboards financeiros (receita, burn, CAC, LTV)
- CRM (pipeline, churns, expansões)
- Produto (roadmap, launches, NPS)
- Hiring tracker
- Histórico de board packs anteriores
- Templates aprovados de comunicação com investidores

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados de métricas (dashboard financeiro, CRM, produto)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Draft de board pack (Notion/PDF): sumário executivo, highlights do período, métricas-chave com commentary, desafios e p…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Draft de board pack (Notion/PDF): sumário executivo, highlights do período, métricas-chave com commentary, desafios e plano, próximos passos
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Skeptic registrado
- [ ] Gate HITL respeitado: Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design
- [ ] Gate HITL respeitado: Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas)
- [ ] Gate HITL respeitado: Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação de escalation quando follow-up crítico está atrasado e envolve terceiros externos | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Founder Clone Agent antes de qualquer resposta ser enviada em nome do founder | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Configuração inicial do corpus do Sage (founder revisa e aprova quais comunicações entram no corpus de clonagem) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Skeptic | BLOQUEIA entrega |

## Handoff

- **to:** Skeptic
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
