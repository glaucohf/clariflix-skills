---
task: pulse()
responsavel: "Pulse"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição estruturada do Vox + metadados da reunião (participantes, tipo, data) + acesso à KB institucional no Notion + acesso ao ClickUp (tasks abertas por participante e projeto)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição enriquecida com anotações de contexto inline: { prior_decision_refs: [{topic, decision_date, decision_summary, kb_link}], open_tasks_by_participant: [{participant, open_count, overdue_count}], recurring_themes: [{theme, frequency, last_discussed}], unresolved_items: [{item, raised_date, meeting_ref}] }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatório de contexto: lista de temas com histórico e alertas de contradição potencial com posições anteriores"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Maestro após Vox concluir transcrição. Processo paralelo à análise inicial de Quill — Pulse entrega contexto enriquecido que Quill usa na segunda passagem de extração para garantir que de…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argos 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB — Maestro pausa o pipeline e notifica o founder com a contradição detalhada (decisão antiga vs. nova decisão). O founder confirma qual prevalece antes de Hermes atualizar a KB e criar tasks. Sem confirmação em 4h, o item fica em quarentena."
    - "[ ] HITL: ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founder com os itens em destaque para atribuição manual antes de Hermes criar as tasks. Prazo de resposta: 2h (reuniões urgentes) ou 24h (demais)."
    - "[ ] HITL: DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Proposal) — o founder deve aprovar as atualizações antes do envio. Qualquer mudança de stage ou valor estimado requer aprovação explícita via Slack (botão Aprovar/Rejeitar)."
    - "[ ] HITL: BOARD MEMO PARA ENVIO EXTERNO (L3): Hermes pode criar o draft do Board Memo no Notion automaticamente (L2), mas o envio para membros do board, investidores ou parceiros externos é sempre bloqueado até aprovação explícita do founder. Nenhum email ou comunicação sai sem revisão humana."
    - "[ ] HITL: INFORMAÇÃO SENSÍVEL FLAGUEADA (L3): Quando Argos detecta informações sensíveis na transcrição (valores de negociação, dados de saúde financeira, informações sobre demissões ou reestruturações, dados pessoais de terceiros) — o trecho é isolado e o founder decide: (a) incluir na KB com controle de acesso restrito, (b) incluir no sumário interno apenas, ou (c) excluir do registro. Sem decisão do founder, o trecho fica em quarentena."
---

# Enriquecer Contexto Transcrição

**Task ID:** `pulse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Meeting Intelligence — Decisões que Nunca se Perdem

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Contexto Transcrição |
| **status** | `pending` |
| **responsible_executor** | Pulse (Pulse — O Enriquecedor de Contexto) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em enriquecimento contextual da transcrição com memória institucional. Antes de Quill extrair decisões, Pulse injeta contexto relevante: busca na KB quais decisões anteriores existem sobre os temas da reunião, verifica quais projetos no ClickUp estão em aberto para os participantes, identifica se há compromissos não cumpridos de reuniões anteriores com as mesmas pessoas, e mapeia o histórico de posições dos participantes sobre temas recorrentes. Isso permite que Quill extraia decisões com o contexto de 'o que mudou' e 'o que ainda estava pendente', não apenas o que foi dito hoje.

## Input

- Transcrição estruturada do Vox + metadados da reunião (participantes, tipo, data) + acesso à KB institucional no Notion + acesso ao ClickUp (tasks abertas por participante e projeto)

## Output

- Transcrição enriquecida com anotações de contexto inline: { prior_decision_refs: [{topic, decision_date, decision_summary, kb_link}], open_tasks_by_participant: [{participant, open_count, overdue_count}], recurring_themes: [{theme, frequency, last_discussed}], unresolved_items: [{item, raised_date, meeting_ref}] }
- Relatório de contexto: lista de temas com histórico e alertas de contradição potencial com posições anteriores

## Trigger

Ativado por Maestro após Vox concluir transcrição. Processo paralelo à análise inicial de Quill — Pulse entrega contexto enriquecido que Quill usa na segunda passagem de extração para garantir que decisões sejam contextualizadas historicamente.

## Knowledge base (o que o executor consulta)

- KB institucional no Notion (decisões históricas indexadas no Vector DB por tema, data e participante)
- ClickUp (tasks abertas, overdue e concluídas por projeto e por pessoa)
- Histórico de reuniões processadas pelo squad (transcrições e sumários anteriores)
- Perfis dos participantes recorrentes (cargo, área, padrões de comprometimento histórico)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcrição estruturada do Vox + metadados da reunião (participantes, tipo, data) + acesso à KB institucional no Notion…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Transcrição enriquecida com anotações de contexto inline: { prior_decision_refs: [{topic, decision_date, decision_summa…) e persistir no artefato do squad.
4. Entregar ao critic Argos 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Transcrição enriquecida com anotações de contexto inline: { prior_decision_refs: [{topic, decision_date, decision_summary, kb_link}], open_tasks_by_participant…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argos 2 registrado
- [ ] Gate HITL respeitado: CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB…
- [ ] Gate HITL respeitado: ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founde…
- [ ] Gate HITL respeitado: DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Propo…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB — Maestro pausa o pi… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founder com os itens em de… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Proposal) — o founder dev… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — BOARD MEMO PARA ENVIO EXTERNO (L3): Hermes pode criar o draft do Board Memo no Notion automaticamente (L2), mas o envio para membros do board, investidores ou… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — INFORMAÇÃO SENSÍVEL FLAGUEADA (L3): Quando Argos detecta informações sensíveis na transcrição (valores de negociação, dados de saúde financeira, informações so… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — OVERDUE CRÍTICO COM ESCALADA (L2→HITL): Quando Echo identifica action item de reunião estratégica com mais de 7 dias de atraso e o assignee não respondeu a lem… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — CUSTO DE PROCESSAMENTO ACIMA DE THRESHOLD (L3): Se estimativa de custo de tokens de uma reunião longa (> 3h) superar limite configurado (default: U$2 por reuni… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Argos 2 | BLOQUEIA entrega |

## Handoff

- **to:** Quill
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
