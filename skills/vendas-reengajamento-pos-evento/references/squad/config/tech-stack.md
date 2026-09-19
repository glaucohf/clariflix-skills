# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível) / Pipedrive / Salesforce / RD Station CRM — fonte de verdade de contatos, dedup, histórico e pipeline de oportunidades
- Plataformas de webinar: Zoom Webinar (API de participantes + engajamento), Hotmart, Eduzz, StreamYard — fonte de metadados de engajamento pós-evento
- Plataformas de evento físico: Sympla, Eventbrite, sistemas proprietários de badge scan — fonte de lista de participantes e dados de visita ao estande
- WhatsApp Business API: Gupshup / AiSensy / Interakt / QuickReply.ai — canal principal de outreach pós-evento no Brasil (Score A e B)
- Email: Gmail API / Outlook API / SendGrid — cadencias de email para todos os scores, nurture de longo prazo
- LinkedIn: LinkedIn API / Phantombuster — outreach Score A via DM apos tentativas de WhatsApp/email sem resposta
- Enriquecimento: Clay + Apollo (275M+ contatos) — dossiê de conta e contato para todos os leads novos
- Calendário: Google Calendar / Outlook Calendar — agendamento e lembretes do Atlas Evento
- Observabilidade: Langfuse (OTEL) — quality gates, evals, rastreamento de tasks por agente e por evento
- Gestão de tarefas: ClickUp — artefatos verificáveis por task, prova de trabalho auditável, dashboard de ROI por evento
- Notificações internas: Slack / WhatsApp Business — alertas de SQL gerado e HITL para closers e gestão
- Videoconferência: Google Meet / Zoom / Teams — links de reunião gerados pelo Atlas Evento com pauta personalizada

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
