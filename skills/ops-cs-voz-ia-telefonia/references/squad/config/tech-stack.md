# Tech stack (integrações da especificação)

- Aircall — plataforma de telefonia principal: webhook de chamada entrante, transferencia quente, callback scheduling, disponibilidade de filas em tempo real
- WhatsApp Business API — canal #1 no Brasil: webhook de mensagens de audio (OGG Opus), envio de audio TTS sintetizado, status de entrega de mensagem
- Deepgram Nova-2 PT-BR — ASR principal com vocabulario de dominio customizado (latencia < 300ms para streaming)
- OpenAI Whisper Large-v3 — ASR fallback para audios longos ou de qualidade muito baixa
- ElevenLabs PT-BR ou Azure Neural TTS — sintese de voz com persona da marca (latencia < 400ms)
- ClickUp (Brain2 / MCP server) — hub de tasks e prova de trabalho por interacao de voz, espelhando AIOX
- CRM: HubSpot ou Salesforce — dados de conta, tier, MRR, historico de interacoes, health score
- ERP / OMS — consulta de pedidos, status, estoque (API REST ou MCP customizado, SLA < 1.5s)
- Zendesk / Intercom — criacao de tickets de escalonamento com transcricao e contexto, KB para RAG
- Slack — notificacoes de escalonamento urgente, alertas de churn do Radar, briefings para CSMs
- Supabase / Postgres — estado de sessao dos agentes, health scores, logs de transcricoes, fila de handoffs, consentimentos LGPD
- Langfuse — observabilidade OTEL: tracing de cada step do pipeline de voz (audio -> ASR -> NER -> classificacao -> worker -> critic -> TTS), metricas de WER, latencia fim-a-fim, CSAT, deflection rate
- Claude Agent SDK / LangGraph — orquestracao multi-agente com gerenciamento de estado de sessao de voz
- Gateway de pagamento: Stripe / Pagarme / Iugu — consulta de transacoes e submissao de refund pelo Onda
- Google Calendar ou Aircall Scheduling — agendamento de callbacks pelo Hertz

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
