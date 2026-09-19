---
task: orionPipeline()
responsavel: "Orion"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Signal-to-Meeting Dossie: para cada lead abordado, um artefato verificável no ClickUp contendo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(1) Signal Card (tipo de sinal, timestamp, score de urgência, fonte), (2) Lead Dossie completo (Sherlock), (3) Message Package aprovado pelo Argus com score de personalização, (4) Execution Log da cadência com timestamps de cada toque, (5) Classification Card da resposta (se houver), (6) CRM Update Confirmation com link para o deal/contato"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard consolidado no ClickUp com métricas do squad em tempo real e relatório executivo semanal automático"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe sinais do LinkedIn e eventos de CRM, decompose em subtarefas, roteia para workers especializados, mantem estado do lead no funil, gerencia filas de aprovacao HITL, consolida artefatos e garant…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório."
    - "[ ] HITL: Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada."
    - "[ ] HITL: Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente."
    - "[ ] HITL: Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana."
    - "[ ] HITL: Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração."
---

# Orquestrar Pipeline do Social Selling e Inbound LinkedIn

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Social Selling e Inbound LinkedIn |
| **status** | `pending` |
| **responsible_executor** | Orion (Maestro Comercial (Órion)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe sinais do LinkedIn e eventos de CRM, decompose em subtarefas, roteia para workers especializados, mantem estado do lead no funil, gerencia filas de aprovacao HITL, consolida artefatos e garante que nenhuma janela de timing seja perdida. Opera como cerebro central do loop signal-to-meeting.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Signal-to-Meeting Dossie: para cada lead abordado, um artefato verificável no ClickUp contendo
- (1) Signal Card (tipo de sinal, timestamp, score de urgência, fonte), (2) Lead Dossie completo (Sherlock), (3) Message Package aprovado pelo Argus com score de personalização, (4) Execution Log da cadência com timestamps de cada toque, (5) Classification Card da resposta (se houver), (6) CRM Update Confirmation com link para o deal/contato
- Dashboard consolidado no ClickUp com métricas do squad em tempo real e relatório executivo semanal automático

## Trigger

Recebe sinais do LinkedIn e eventos de CRM, decompose em subtarefas, roteia para workers especializados, mantem estado do lead no funil, gerencia filas de aprovacao HITL, consolida artefatos e garante que nenhuma janela de timing seja perdida. Opera como cerebro central do loop signal-to-meeting.

## Knowledge base (o que o executor consulta)

- LinkedIn Sales Navigator
- fonte primária de sinais e canal de outreach (via automação com limites de segurança para não violar ToS)
- Apollo.io
- enriquecimento de contatos (email, cargo, empresa), alertas de mudança de cargo, base de 275M+ contatos
- enriquecimento avançado e workflows de pesquisa de conta (waterfall de provedores de dados)
- HubSpot CRM (MCP disponível)
- CRM primário: criação de deals, atualização de contatos, registro de atividades, pipeline stages
- Pipedrive
- alternativa de CRM para clientes que usam Pipedrive (mesmo contrato de integração)
- gestão de tarefas do squad, prova de trabalho verificável por lead, dashboard de KPIs, filas de aprovação HITL
- Gmail/Outlook
- canal secundário de outreach quando email disponível (via Apollo enriquecimento)
- Slack/WhatsApp Business
- notificações HITL em tempo real para SDRs e closers (alerts HOT, aprovações tier-1)
- observabilidade OTEL, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de custo por lead
- n8n / Make
- orquestracao de webhooks e automacoes de suporte (alternativa leve para integrações pontuais)
- Calendly / Google Calendar
- agendamento automático quando lead classifica como HOT e aceita reunião

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argus 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Signal-to-Meeting Dossie: para cada lead abordado, um artefato verificável no ClickUp contendo
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus 2 registrado
- [ ] Gate HITL respeitado: Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório.
- [ ] Gate HITL respeitado: Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada.
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório. | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana. | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Primeiro envio de cadência para um novo segmento/persona não testado anteriormente: SDR revisa amostra de 5 mensagens antes de liberar automação plena. | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Lead responde mencionando nome de concorrente ou fazendo pergunta técnica complexa: desvia para SDR humano com contexto completo da conversa. | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Argus 2 | BLOQUEIA entrega |

## Handoff

- **to:** Scout
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
