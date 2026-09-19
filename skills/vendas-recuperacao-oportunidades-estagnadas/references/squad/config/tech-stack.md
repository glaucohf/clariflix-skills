# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce — fonte de verdade de deals e histórico
- WhatsApp Business API: Gupshup, AiSensy ou Interakt — canal principal de recuperação no Brasil
- Email: SMTP/SendGrid ou sequenciador (Apollo, Instantly) — cadências de nurture e follow-up
- LinkedIn Sales Navigator — enriquecimento de contexto e outreach via Escavador
- Voz: Vapi (<600ms latência) ou Retell AI + ElevenLabs TTS — recuperação via ligação para deals de alto valor
- Enriquecimento: Clay ou Apollo (275M+ contatos) — Escavador busca sinais externos
- E-commerce/Carrinho: Shopify, WooCommerce, Hotmart — webhooks de abandono de carrinho
- ClickUp — gestão de tarefas, prova de trabalho, artefatos verificáveis por deal
- Langfuse (OTEL) — observabilidade, evals e quality gates (dev 70% / staging 85% / prod 95%)
- Google Calendar / Calendly — booking de reuniões de reativação pelo Worker de Agendamento (quando integrado)
- Slack / Teams — alertas de resposta e HITL gates para comerciais humanos

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
