# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce — source of truth de contatos e companies
- Enriquecimento: Apollo.io (275M+ contatos B2B), Clay (waterfall multi-source), Clearbit (dados de empresa)
- Email validation: ZeroBounce ou NeverBounce (verificação de MX record e caixa ativa)
- WhatsApp Business API: sync de numero validado e opt-in status
- Plataforma de email (ActiveCampaign / Mailchimp / RD Station): sync de contatos e status de bounce
- ClickUp: artefatos verificáveis por task, fila HITL, dashboard de qualidade de CRM
- Langfuse (OTEL): observabilidade de cada agente, quality gates dev 70% / staging 85% / prod 95%
- Slack: alertas de anomalia, fila HITL para aprovação de merges
- LangGraph: orquestração do pipeline com estado persistente entre etapas
- N8N (opcional): webhook receiver para fontes de entrada não-nativas (ex: formulário do site, planilha do SDR)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
