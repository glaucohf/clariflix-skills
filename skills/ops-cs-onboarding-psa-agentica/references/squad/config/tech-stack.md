# Tech stack (integrações da especificação)

- ClickUp (MCP nativo) — hub de tasks, marcos, status e prova de trabalho; espelha estrutura AIOX
- CRM (HubSpot ou Salesforce via MCP) — webhook de deal closed-won para trigger de onboarding; dados de conta e contatos
- WhatsApp Business API — notificações proativas e follow-ups de pendências do cliente
- Slack — alertas internos, notificações de risco, aprovações HITL via workflow de aprovação
- Google Drive / Notion — ingestão de SOW e documentos de kickoff via connector ou URL
- Calendário (Google Calendar / Outlook via MCP) — leitura de calls agendadas para trigger de relatório pré-reunião
- Produto SaaS do cliente (API de uso) — dados de engajamento e ativação para health score
- Supabase / Postgres — estado dos agentes, histórico de onboardings, health scores, risk matrix
- Langfuse — observabilidade OTEL, tracing de chamadas, quality gates (dev 70% / staging 85% / prod 95%)
- Email (SMTP/SendGrid) — envio de relatórios de delivery e notificações formais
- Rocketlane (referência de arquitetura PSA) — benchmark de fluxo de onboarding e estrutura de portal do cliente

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
