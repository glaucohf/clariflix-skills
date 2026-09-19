# Tech stack (integrações da especificação)

- ClickUp (Brain2/Autopilot Agents) — hub de tasks, prova de trabalho, registro de cada decisão de handoff como task com checklist, espelho do AIOX
- Claude Agent SDK + LangGraph — orquestração multi-agente, grafo de decisão do Hieronimus, estados de handoff
- Langfuse — observabilidade OTEL completa, tracing de cada classificação, dashboard de KPIs, quality gates (dev 70% / staging 85% / prod 95%)
- Supabase/Postgres — estado persistente dos handoffs abertos, log de decisões, banco de treinamento da matriz, histórico de feedbacks
- Slack (Webhooks + Workflow Builder) — canal #hitl-approvals para briefings L3, botões de ação direta (Aprovar/Rejeitar/Modificar), lembretes de SLA
- Zendesk / Intercom — webhook de interceptação de ações antes da execução, registro de decisões em tickets, integração com filas de atendimento
- WhatsApp Business API — interceptação de ações de alto risco iniciadas em atendimentos via WhatsApp antes do envio
- HubSpot / Salesforce — contexto do cliente (LTV, tier, histórico de contratos, health score) para enriquecer classificação de criticidade
- MCP Servers (camada universal) — ClickUp MCP, CRM MCP, helpdesk MCP para acesso unificado sem hardcode de API keys

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
