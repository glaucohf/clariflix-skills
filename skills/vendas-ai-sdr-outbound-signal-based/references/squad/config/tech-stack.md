# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível), Pipedrive ou Salesforce — fonte de verdade para estado do lead e log de atividades
- Enriquecimento de dados: Clay (enriquecimento em escala via workflows), Apollo.io (275M+ contatos, intent data, sequências)
- Email: SendGrid ou AWS SES (envio transacional), Instantly.ai ou Lemlist (warmup de domínio e sequências cold)
- WhatsApp Business API: Gupshup, AiSensy ou QuickReply.ai (crítico para o mercado brasileiro)
- LinkedIn: Phantombuster ou Expandi (automação de InMail/connection request dentro dos limites)
- Voz AI: Vapi (<600ms latência) com Deepgram STT + Claude/GPT LLM + ElevenLabs TTS para cold calls automatizadas
- Calendário: Calendly ou Cal.com (booking automático via link ou conversacional)
- Intent data e sinais: LinkedIn Sales Navigator, Bombora (intent data B2B), Google Alerts (menções de empresa)
- Gestão de tarefas e prova de trabalho: ClickUp (artefatos verificáveis por task — dossiê, draft aprovado, log de envio)
- Orquestração: LangGraph (controle fino de estado do funil) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (OTEL) para quality gates dev 70% / staging 85% / prod 95% task success
- Notificações internas: Slack ou WhatsApp do SDR humano para alertas de HITL e leads HOT

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
