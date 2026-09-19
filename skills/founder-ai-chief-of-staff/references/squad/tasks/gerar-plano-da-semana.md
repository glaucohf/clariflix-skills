---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "OKRs do quarter (Notion/ClickUp)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Agenda da semana (Google Calendar)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Status de deals no CRM"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Tasks abertas e atrasadas (ClickUp)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Tempo gasto por categoria (Calendar analytics)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Inputs do founder sobre mudanças de prioridade"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Plano Semanal (segunda 8h): top 3 prioridades, blocos de foco sugeridos no calendário, itens a delegar ou recusar"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Retrospectiva Semanal (sexta 17h): heatmap de onde o tempo foi, score de foco (0–10), recomendação para próxima semana"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alerta de desvio quando agenda foge das prioridades declaradas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Schedule semanal (segunda 8h e sexta 17h). Detecção de reunião fora das prioridades declaradas. OKR check-in mensal. Founder solicita revisão de prioridades."
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

# Gerar Plano Da Semana

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI Chief of Staff — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Plano Da Semana |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Priority & Focus Aligner) |
| **execution_type** | `Agent` |
| **input** | 6 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mantém o mapa semanal de prioridades do founder atualizado, alinhado com OKRs e com o que tem maior alavancagem. Toda segunda-feira gera o 'Plano da Semana' com os 3 temas de foco e bloqueia tempo no calendário. Toda sexta, gera retrospectiva: o que foi feito vs planejado, onde o tempo foi para, qual o score de foco.

## Input

- OKRs do quarter (Notion/ClickUp)
- Agenda da semana (Google Calendar)
- Status de deals no CRM
- Tasks abertas e atrasadas (ClickUp)
- Tempo gasto por categoria (Calendar analytics)
- Inputs do founder sobre mudanças de prioridade

## Output

- Plano Semanal (segunda 8h): top 3 prioridades, blocos de foco sugeridos no calendário, itens a delegar ou recusar
- Retrospectiva Semanal (sexta 17h): heatmap de onde o tempo foi, score de foco (0–10), recomendação para próxima semana
- Alerta de desvio quando agenda foge das prioridades declaradas

## Trigger

Schedule semanal (segunda 8h e sexta 17h). Detecção de reunião fora das prioridades declaradas. OKR check-in mensal. Founder solicita revisão de prioridades.

## Knowledge base (o que o executor consulta)

- OKRs e metas do founder (Notion/ClickUp)
- Google Calendar (histórico e projeção)
- CRM (pipeline e deals críticos)
- ClickUp (backlog e tasks)
- Histórico de retrospectivas anteriores

## Action Items

1. Confirmar o gatilho e carregar a entrada (OKRs do quarter (Notion/ClickUp)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Plano Semanal (segunda 8h): top 3 prioridades, blocos de foco sugeridos no calendário, itens a delegar ou recusar) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Plano Semanal (segunda 8h): top 3 prioridades, blocos de foco sugeridos no calendário, itens a delegar ou recusar
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

- **to:** Memo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
