# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponivel) / Pipedrive / Salesforce — fonte de verdade de leads, contatos, deals e historico
- WhatsApp Business API: Gupshup / AiSensy / Interakt / QuickReply.ai — canal principal no Brasil, envio/recepcao de mensagens
- Voz IA: Vapi (<600ms latencia) ou Retell AI — ligacoes de qualificacao automatizadas com voz natural
- TTS: ElevenLabs — voz da marca para ligacoes do Vox
- STT: Deepgram — transcricao de calls em tempo real
- Email: Gmail API / Outlook API — cadencias de email do Eco e confirmacoes do Atlas
- Calendario: Google Calendar / Outlook Calendar — agendamento e lembretes do Atlas
- Enriquecimento: Clay + Apollo (275M+ contatos) — dados do Sherlock
- Intent Data: sinais de ads (Meta Ads, Google Ads) + plataformas de intent — gatilhos para o Argos
- Observabilidade: Langfuse (OTEL) — quality gates, evals, rastreamento de tasks por agente
- Gestao de tarefas: ClickUp — artefatos verificaveis por task, prova de trabalho auditavel
- Notificacoes internas: Slack / WhatsApp Business — alertas de lead quente e HITL para closers
- Videoconferencia: Google Meet / Zoom / Teams — links de reuniao gerados pelo Atlas

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
