---
task: claudeOpusPipeline()
responsavel: "Claude Opus"
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
    descricao: "Relatório de ROI Por Evento: documento estruturado (PDF exportável do ClickUp + nota no CRM) gerado automaticamente 30 dias após cada evento, contendo: total de participantes processados, breakdown por score (A/B/C), taxa de contato em 48h, taxa de resposta por canal e score, SQLs gerados com ficha de qualificação, reuniões agendadas e realizadas, oportunidades abertas no CRM com valor estimado, pipeline influenciado pelo evento, custo por SQL e ROI calculado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Auditável em tempo real no ClickUp com tasks vinculadas por lead e por evento"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard de KPIs comparativo entre eventos para identificar melhores canais e temas de evento por ROI"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe a lista bruta de participantes do evento (planilha, webhook de plataforma, badge scan ou API de inscricao), executa dedup contra o CRM para identificar leads novos vs. contas existentes, decom…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vigilia antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer aprovação do closer responsável antes do primeiro envio"
    - "[ ] HITL: Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento"
    - "[ ] HITL: Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática"
    - "[ ] HITL: Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana"
    - "[ ] HITL: Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação"
---

# Orquestrar Pipeline do Reengajamento Pós-Evento e Webinar

**Task ID:** `claudeOpusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Reengajamento Pós-Evento e Webinar |
| **status** | `pending` |
| **responsible_executor** | Claude Opus (Radar — Maestro de Reengajamento (Claude Opus)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe a lista bruta de participantes do evento (planilha, webhook de plataforma, badge scan ou API de inscricao), executa dedup contra o CRM para identificar leads novos vs. contas existentes, decompoe o processamento em subtarefas por segmento de engajamento, mantém estado de cada contato no pipeline pos-evento, roteia para os Workers corretos baseado em score de engajamento e canal disponivel, monitora SLA de 48h para que 100% da lista seja contactada, consolida resultados e reporta pipeline gerado por evento ao closer responsavel. Aciona HITL para contas estrategicas (ja clientes, prospects de alto valor ja no CRM) antes de qualquer acao.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Relatório de ROI Por Evento: documento estruturado (PDF exportável do ClickUp + nota no CRM) gerado automaticamente 30 dias após cada evento, contendo: total de participantes processados, breakdown por score (A/B/C), taxa de contato em 48h, taxa de resposta por canal e score, SQLs gerados com ficha de qualificação, reuniões agendadas e realizadas, oportunidades abertas no CRM com valor estimado, pipeline influenciado pelo evento, custo por SQL e ROI calculado
- Auditável em tempo real no ClickUp com tasks vinculadas por lead e por evento
- Dashboard de KPIs comparativo entre eventos para identificar melhores canais e temas de evento por ROI

## Trigger

Recebe a lista bruta de participantes do evento (planilha, webhook de plataforma, badge scan ou API de inscricao), executa dedup contra o CRM para identificar leads novos vs. contas existentes, decompoe o processamento em subtarefas por segmento de engajamento, mantém estado de cada contato no pipeline pos-evento, roteia para os Workers corretos baseado em score de engajamento e canal disponivel, monitora SLA de 48h para que 100% da lista seja contactada, consolida resultados e reporta pipeline gerado por evento ao closer responsavel. Aciona HITL para contas estrategicas (ja clientes, prospects de alto valor ja no CRM) antes de qualquer acao.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível) / Pipedrive / Salesforce / RD Station CRM
- fonte de verdade de contatos, dedup, histórico e pipeline de oportunidades
- Plataformas de webinar: Zoom Webinar (API de participantes + engajamento), Hotmart, Eduzz, StreamYard
- fonte de metadados de engajamento pós-evento
- Plataformas de evento físico: Sympla, Eventbrite, sistemas proprietários de badge scan
- fonte de lista de participantes e dados de visita ao estande
- WhatsApp Business API: Gupshup / AiSensy / Interakt / QuickReply.ai
- canal principal de outreach pós-evento no Brasil (Score A e B)
- Email: Gmail API / Outlook API / SendGrid
- cadencias de email para todos os scores, nurture de longo prazo
- LinkedIn: LinkedIn API / Phantombuster
- outreach Score A via DM apos tentativas de WhatsApp/email sem resposta
- Enriquecimento: Clay + Apollo (275M+ contatos)
- dossiê de conta e contato para todos os leads novos
- Calendário: Google Calendar / Outlook Calendar
- agendamento e lembretes do Atlas Evento
- Observabilidade: Langfuse (OTEL)
- quality gates, evals, rastreamento de tasks por agente e por evento
- Gestão de tarefas: ClickUp
- artefatos verificáveis por task, prova de trabalho auditável, dashboard de ROI por evento
- Notificações internas: Slack / WhatsApp Business
- alertas de SQL gerado e HITL para closers e gestão
- Videoconferência: Google Meet / Zoom / Teams
- links de reunião gerados pelo Atlas Evento com pauta personalizada

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Vigilia antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de ROI Por Evento: documento estruturado (PDF exportável do ClickUp + nota no CRM) gerado automaticamente 30 dias após cada evento, contendo: total d…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vigilia registrado
- [ ] Gate HITL respeitado: Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) —…
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento
- [ ] Gate HITL respeitado: Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Lead que solicita opt-out ou demonstra irritação com o contato — intervenção humana obrigatória, registro de opt-out e revisão da cadência | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Inconsistência crítica detectada entre dados do evento e CRM (ex: lead do evento e cliente com contrato ativo cancelado) — revisão humana antes de qualquer con… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Volume de lista acima de 1.000 contatos em evento único — revisão humana da segmentação antes do disparo em massa | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Vigilia | BLOQUEIA entrega |

## Handoff

- **to:** Recon
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
