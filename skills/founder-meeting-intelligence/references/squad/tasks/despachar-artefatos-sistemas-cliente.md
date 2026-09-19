---
task: hermes()
responsavel: "Hermes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Enriched Extraction Package validado por Argos (GO confirmado) + mapeamento de assignees para usuários do ClickUp/Slack + configuração de projetos-padrão por tipo de reunião + regras de notificação do cliente (quem notificar, em qual canal)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dispatch Report: { clickup_tasks_created: [{ task_id, title, assignee, due_date, url }], slack_notifications_sent: [{ channel, recipient, message_preview }], kb_entries_created: [{ notion_page_id, title, type }], crm_updates: [{ deal_id, update_type, new_value }], board_memo_draft_created: boolean, audit_trail_url: string }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Meeting Intelligence Report final gerado e salvo permanentemente"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Maestro SOMENTE após Argos retornar GO explícito na validação. É o único agente com permissão de escrita em sistemas externos (ClickUp, Notion, Slack, HubSpot). Toda ação de Hermes requer…"
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

# Despachar Artefatos Sistemas Cliente

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Meeting Intelligence — Decisões que Nunca se Perdem

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Despachar Artefatos Sistemas Cliente |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — O Despachante de Ações) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de execução e despacho: transforma o Enriched Extraction Package validado em artefatos reais nos sistemas do cliente. Executa em sequência controlada: (1) cria tasks no ClickUp com title, description, assignee, due_date, priority e link para o Meeting Intelligence Report; (2) envia notificação no Slack para cada assignee com o resumo da task e contexto; (3) alimenta a KB no Notion com o Decision Record e os Knowledge Snippets da reunião; (4) atualiza o CRM (HubSpot) se a reunião envolveu cliente ou prospect — registra next steps e atualiza stage do deal se aplicável; (5) gera o Board Memo Draft se a reunião foi classificada como 'board' ou 'estratégica nível 1'. Toda ação é logada no audit trail do Meeting Intelligence Report.

## Input

- Enriched Extraction Package validado por Argos (GO confirmado) + mapeamento de assignees para usuários do ClickUp/Slack + configuração de projetos-padrão por tipo de reunião + regras de notificação do cliente (quem notificar, em qual canal)

## Output

- Dispatch Report: { clickup_tasks_created: [{ task_id, title, assignee, due_date, url }], slack_notifications_sent: [{ channel, recipient, message_preview }], kb_entries_created: [{ notion_page_id, title, type }], crm_updates: [{ deal_id, update_type, new_value }], board_memo_draft_created: boolean, audit_trail_url: string }
- Meeting Intelligence Report final gerado e salvo permanentemente

## Trigger

Ativado por Maestro SOMENTE após Argos retornar GO explícito na validação. É o único agente com permissão de escrita em sistemas externos (ClickUp, Notion, Slack, HubSpot). Toda ação de Hermes requer confirmação de Argos como pré-condição não negociável. Ações irreversíveis (emails externos, atualizações de CRM de deals em negociação ativa) requerem HITL L3.

## Knowledge base (o que o executor consulta)

- Mapeamento de participantes da reunião para usuários do ClickUp, Slack e HubSpot
- Templates de task por tipo de reunião e projeto
- Regras de prioridade automática (ex: action items com deadline < 3 dias = Urgent)
- Templates de Board Memo do cliente
- Regras de notificação configuradas (opt-in/opt-out por participante)
- Histórico de tarefas criadas para auditoria e deduplicação

## Action Items

1. Confirmar o gatilho e carregar a entrada (Enriched Extraction Package validado por Argos (GO confirmado) + mapeamento de assignees para usuários do ClickUp/Slack…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dispatch Report: { clickup_tasks_created: [{ task_id, title, assignee, due_date, url }], slack_notifications_sent: [{ c…) e persistir no artefato do squad.
4. Entregar ao critic Argos 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dispatch Report: { clickup_tasks_created: [{ task_id, title, assignee, due_date, url }], slack_notifications_sent: [{ channel, recipient, message_preview }], k…
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

- **to:** Echo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
