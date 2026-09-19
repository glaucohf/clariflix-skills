---
task: briefing()
responsavel: "Briefing"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de calendário (título, participantes, descrição), dados do CRM (conta, deals), histórico de emails/notas da conta, perfil público do interlocutor (LinkedIn, news)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Meeting Brief PDF/Notion (1 página): contexto, objetivo, perguntas sugeridas, objeções prováveis, próximo passo recomendado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Entregue 2h antes da reunião via Slack/email"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento de calendário detectado com 24h de antecedência. Também acionado manualmente via comando '/brief @pessoa' no Slack."
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

# Preparar Briefing De Reunião

**Task ID:** `briefing()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI Chief of Staff — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Preparar Briefing De Reunião |
| **status** | `pending` |
| **responsible_executor** | Briefing (Briefing — Prep de Reunião) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gera o meeting brief completo (1 página) para cada reunião do founder: quem é o interlocutor, histórico do relacionamento, últimas interações no CRM, contexto da empresa/setor, objetivo da reunião, 3 perguntas de alto impacto e 2 riscos/objeções prováveis.

## Input

- Evento de calendário (título, participantes, descrição), dados do CRM (conta, deals), histórico de emails/notas da conta, perfil público do interlocutor (LinkedIn, news)

## Output

- Meeting Brief PDF/Notion (1 página): contexto, objetivo, perguntas sugeridas, objeções prováveis, próximo passo recomendado
- Entregue 2h antes da reunião via Slack/email

## Trigger

Evento de calendário detectado com 24h de antecedência. Também acionado manualmente via comando '/brief @pessoa' no Slack.

## Knowledge base (o que o executor consulta)

- CRM (HubSpot/Salesforce): histórico de deals, notas, emails
- Notion/Mem.ai: notas de reuniões anteriores
- Google Calendar: agenda e metadados
- Banco de perfis de interlocutores
- Corpus de frameworks estratégicos do founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de calendário (título, participantes, descrição), dados do CRM (conta, deals), histórico de emails/notas da cont…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Meeting Brief PDF/Notion (1 página): contexto, objetivo, perguntas sugeridas, objeções prováveis, próximo passo recomen…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Meeting Brief PDF/Notion (1 página): contexto, objetivo, perguntas sugeridas, objeções prováveis, próximo passo recomendado
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

- **to:** Kira
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
