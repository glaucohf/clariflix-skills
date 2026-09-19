# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível — fonte de verdade para estado do lead, activities, pipeline e log de outreach), Salesforce com Agentforce SDK ou Pipedrive como alternativas
- Enriquecimento e ICP: Clay (waterfall enrichment de 100+ fontes, workflows de enriquecimento em escala, intent signals), Apollo.io (275M+ contatos, emails verificados, intent data nativo, sequências), Cognism (dados europeus e brasileiros verificados)
- Intent data: LinkedIn Sales Navigator (sinais de mudança de liderança, expansão, hiring), Bombora (intent data B2B tópico), Google Alerts (menções de empresa e concorrentes)
- Email outreach: Instantly.ai ou Lemlist (warmup de domínio e sequências cold com rastreamento de abertura e click), SendGrid ou AWS SES (envio transacional para volume alto)
- LinkedIn: Phantombuster ou Expandi (automação de connection request e InMail dentro dos limites diários do LinkedIn)
- WhatsApp Business API: Gupshup, AiSensy ou QuickReply.ai — plataformas purpose-built para o mercado brasileiro com conformidade pós-2024
- Voz AI: Vapi (<600ms latência) com Deepgram STT + Claude como LLM + ElevenLabs TTS para cold calls automatizadas em escala
- Calendário: Calendly ou Cal.com (booking automático via link em mensagem ou via conversação no WhatsApp)
- Gestão de tarefas e prova de trabalho: ClickUp (artefatos verificáveis por task — ICP card, dossiê, draft aprovado com score, log de envio, análise de resposta) conectado ao Maestro via MCP ou webhook
- Orquestração multi-agente: LangGraph (controle fino de estado do funil, grafos de decisão por lead) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (traces OTEL por agente, quality gates dev 70% / staging 85% / prod 95% task success, dashboard de performance do squad)
- No-code complementar: n8n para automacoes de integracao entre ferramentas (pilar comum de agencias agenticas 2026) — conecta webhooks, CRM events e notificacoes sem codigo custom
- Notificações internas: Slack ou WhatsApp do SDR humano para alertas de HITL urgentes e leads FIRE detectados

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
