---
task: sage()
responsavel: "Sage"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pergunta estratégica, rascunho de email/memo, output de outro agente para validação de alinhamento"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Contexto de quem está perguntando e qual é o objetivo da comunicação"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta em voz do founder (texto), email redigido pronto para revisão final, score de alinhamento estratégico (0–10) com justificativa para outputs de outros agentes"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Marcação de pontos divergentes do pensamento do founder"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Validação de brief antes de entrega ao founder. Founder solicita rascunho de email/mensagem. Pergunta ad-hoc que exige resposta 'no meu estilo'. Decisão de baixo impacto que pode ser delegada ao clon…"
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

# Validar Output Estratégico

**Task ID:** `sage()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI Chief of Staff — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validar Output Estratégico |
| **status** | `pending` |
| **responsible_executor** | Sage (Sage — Founder Clone Agent) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Replica a lógica de raciocínio, frameworks preferidos e tom de comunicação do founder. Responde perguntas estratégicas 'como o founder responderia', redige emails em voz do founder, e valida se outputs dos outros agentes estão alinhados ao pensamento estratégico do founder antes de chegarem a ele.

## Input

- Pergunta estratégica, rascunho de email/memo, output de outro agente para validação de alinhamento
- Contexto de quem está perguntando e qual é o objetivo da comunicação

## Output

- Resposta em voz do founder (texto), email redigido pronto para revisão final, score de alinhamento estratégico (0–10) com justificativa para outputs de outros agentes
- Marcação de pontos divergentes do pensamento do founder

## Trigger

Validação de brief antes de entrega ao founder. Founder solicita rascunho de email/mensagem. Pergunta ad-hoc que exige resposta 'no meu estilo'. Decisão de baixo impacto que pode ser delegada ao clone.

## Knowledge base (o que o executor consulta)

- Corpus de comunicações passadas do founder (emails, Notion, transcrições)
- Frameworks e modelos mentais documentados
- Decisões históricas e raciocínios registrados
- Biblioteca de templates aprovados pelo founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pergunta estratégica, rascunho de email/memo, output de outro agente para validação de alinhamento).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resposta em voz do founder (texto), email redigido pronto para revisão final, score de alinhamento estratégico (0–10) c…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta em voz do founder (texto), email redigido pronto para revisão final, score de alinhamento estratégico (0–10) com justificativa para outputs de outros…
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

- **to:** Intel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
