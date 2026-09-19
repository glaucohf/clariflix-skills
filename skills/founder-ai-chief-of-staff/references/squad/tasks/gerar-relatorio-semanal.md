---
task: vance()
responsavel: "Vance"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição de reunião (Sembly/Notion), emails com commitments, tasks existentes no ClickUp"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Detecção de padrões de linguagem de compromisso ('vou enviar', 'até sexta', 'você pode verificar')"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tasks criadas no ClickUp (dono, prazo, contexto)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Lembretes automáticos D-2, D-0 e D+1"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório semanal de follow-ups (% no prazo, abertos, atrasados, escalados)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Alerta de risco para Orion quando deadline crítico está em risco"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Fim de reunião (transcrição disponível). Email com linguagem de compromisso detectada. Check-in semanal automático (sexta 17h). Founder solicita status de um follow-up específico."
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

# Gerar Relatório Semanal

**Task ID:** `vance()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI Chief of Staff — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Relatório Semanal |
| **status** | `pending` |
| **responsible_executor** | Vance (Vance — Follow-up & Accountability Manager) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Captura ações acordadas em reuniões (via transcrição ou email), cria tasks no ClickUp com dono e prazo, monitora status e dispara lembretes escalonados. Gera relatório semanal de accountability: o que foi prometido vs entregue, gargalos e escalations para o founder.

## Input

- Transcrição de reunião (Sembly/Notion), emails com commitments, tasks existentes no ClickUp
- Detecção de padrões de linguagem de compromisso ('vou enviar', 'até sexta', 'você pode verificar')

## Output

- Tasks criadas no ClickUp (dono, prazo, contexto)
- Lembretes automáticos D-2, D-0 e D+1
- Relatório semanal de follow-ups (% no prazo, abertos, atrasados, escalados)
- Alerta de risco para Orion quando deadline crítico está em risco

## Trigger

Fim de reunião (transcrição disponível). Email com linguagem de compromisso detectada. Check-in semanal automático (sexta 17h). Founder solicita status de um follow-up específico.

## Knowledge base (o que o executor consulta)

- ClickUp (tasks, projetos, responsáveis)
- Gmail/Outlook (histórico de emails)
- Transcrições de reuniões (Sembly/Notion)
- CRM (oportunidades abertas vinculadas a follows)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcrição de reunião (Sembly/Notion), emails com commitments, tasks existentes no ClickUp).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tasks criadas no ClickUp (dono, prazo, contexto)) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tasks criadas no ClickUp (dono, prazo, contexto)
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

- **to:** Sage
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
