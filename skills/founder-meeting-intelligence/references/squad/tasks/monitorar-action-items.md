---
task: echo()
responsavel: "Echo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de tasks criadas por Hermes (IDs do ClickUp) + calendário do founder (Google Calendar/Outlook) para identificar reuniões de follow-up programadas + configuração de SLAs por tipo de task (ex: estratégicas = 7 dias, operacionais = 3 dias) + preferências de notificação do founder"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alertas de deadline em risco (Slack DM para owner + notificação para founder se crítico)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Weekly Commitment Report (quem cumpriu o quê, quem está em atraso, tendências)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Pre-Meeting Brief para reuniões recorrentes (última reunião → o que ficou → sugestão de pauta)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Accountability Dashboard atualizado no Notion com métricas de cumprimento por participante e projeto"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por cron diário (07h30 no fuso do cliente) para verificar status de tasks criadas. Ativado 48h antes de deadline de qualquer task criada pelo squad. Ativado automaticamente 2h antes de reuniõ…"
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

# Monitorar Action Items

**Task ID:** `echo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Meeting Intelligence — Decisões que Nunca se Perdem

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Action Items |
| **status** | `pending` |
| **responsible_executor** | Echo (Echo — O Guardião de Follow-Up) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de acompanhamento e accountability pós-reunião. Monitora o ciclo de vida das action items criadas por Hermes: verifica no ClickUp se tasks foram iniciadas, envia lembretes proativos 48h antes do deadline, escalona ao founder tasks em risco de atraso, e gera o Weekly Commitment Report — um painel de comprometimentos por participante (taxa de cumprimento, overdue, tendências). Na véspera de reuniões recorrentes (1:1s, weeklies), Echo prepara automaticamente o Pre-Meeting Brief: o que foi decidido na última reunião, o que foi cumprido, o que está pendente, e os tópicos sugeridos para pauta baseados em items em aberto.

## Input

- Lista de tasks criadas por Hermes (IDs do ClickUp) + calendário do founder (Google Calendar/Outlook) para identificar reuniões de follow-up programadas + configuração de SLAs por tipo de task (ex: estratégicas = 7 dias, operacionais = 3 dias) + preferências de notificação do founder

## Output

- Alertas de deadline em risco (Slack DM para owner + notificação para founder se crítico)
- Weekly Commitment Report (quem cumpriu o quê, quem está em atraso, tendências)
- Pre-Meeting Brief para reuniões recorrentes (última reunião → o que ficou → sugestão de pauta)
- Accountability Dashboard atualizado no Notion com métricas de cumprimento por participante e projeto

## Trigger

Ativado por cron diário (07h30 no fuso do cliente) para verificar status de tasks criadas. Ativado 48h antes de deadline de qualquer task criada pelo squad. Ativado automaticamente 2h antes de reuniões recorrentes identificadas no calendário do founder. Ativado manualmente pelo founder via '/echo status [pessoa ou projeto]' para relatório pontual.

## Knowledge base (o que o executor consulta)

- ClickUp API (leitura de status de tasks criadas pelo squad)
- Google Calendar / Outlook API (identificação de reuniões recorrentes e próximos encontros com os mesmos participantes)
- Histórico de taxa de cumprimento por participante (para calibrar urgência dos alertas)
- Regras de SLA por tipo de task e projeto
- Perfil de preferências do founder (como quer receber alertas, thresholds de escalada)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de tasks criadas por Hermes (IDs do ClickUp) + calendário do founder (Google Calendar/Outlook) para identificar r…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alertas de deadline em risco (Slack DM para owner + notificação para founder se crítico)) e persistir no artefato do squad.
4. Entregar ao critic Argos 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alertas de deadline em risco (Slack DM para owner + notificação para founder se crítico)
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

- **to:** Argos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
