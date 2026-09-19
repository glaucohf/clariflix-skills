# Tech stack (integrações da especificação)

- Vapi ou Rétell AI (plataforma de agente de voz sub-600ms)
- Deepgram (STT — Speech-to-Text de baixa latência)
- ElevenLabs (TTS — Text-to-Speech com voz personalizada)
- HubSpot CRM (MCP disponível — leitura e escrita de leads, deals, activities)
- Google Calendar ou Outlook (agendamento e gestão de disponibilidade do closer)
- WhatsApp Business API via Gupshup ou AiSensy (confirmações, lembretes, nurture)
- Apollo.io (enriquecimento de leads — 275M+ contatos)
- Clay (enriquecimento dinâmico e waterfall de dados)
- ClickUp (gestão de tarefas e artefatos verificáveis por story)
- Langfuse (observabilidade OTEL, evals e quality gates por fase)
- LangGraph (orquestração do grafo de estados conversacional do Vox Agent)
- Twilio ou Vonage (gateway de telefonia para discagem programática)
- Google Sheets ou Airtable (lista de prospectos e relatórios para clientes sem CRM robusto)
- Slack ou Teams (notificações de leads qualificados e alertas de HITL para gestor comercial)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
