# Tech stack (integrações da especificação)

- WhatsApp Business API via BSP purpose-built pos-proibicao Meta — Patagon AI (LATAM-first, recomendado), Leadsales ou BotPenguin como fallback. Gateway principal de entrada e saida de mensagens
- HubSpot CRM — registro automatico de leads qualificados, campos customizados de BANT (Budget, Authority, Need, Timeline), Lead Score pos-qualificacao, historico de conversa estruturado, trigger de criacao de oportunidade pos-qualificacao
- Google Calendar / Calendly — disponibilidade em tempo real para Mia agendar reunioes, criacao de eventos com dados do lead, link de videoconferencia automatico (Google Meet / Zoom)
- Clay — waterfall enrichment em tempo real por Rex (firmographic, technographic, intent signals). Opcional se cliente ja tem Clay; fallback para Apollo direto
- Apollo.io — prospecting e enriquecimento de contatos B2B como fonte primaria ou backup do Clay
- ClickUp — prova de trabalho central: task automatica por lead qualificado, dashboard de metricas do squad (taxa de qualificacao, show-rate, ROI), briefing pre-reuniao para o closer, historico de playbook versions
- Langfuse — observabilidade OTEL de todos os agents, quality gates por ambiente (dev 70% / staging 85% / prod 95% task success), rastreamento de cada conversa como trace completo, evals de qualidade de resposta de Vance
- n8n — orquestracao de webhooks e workflows de notificacao (complemento no-code): alerta de lead VIP para SDR, notificacao de no-show para reengajamento, relatorio semanal de Lilo para Slack/email
- Slack / Email — notificacoes de escalada para SDR humano (lead VIP, irritacao, objecao critica), alertas de anomalia de Lilo, relatorio semanal de performance do squad
- Meta Business Suite / BSP Dashboard — monitoramento de saude da conta WhatsApp Business (Quality Rating, Phone Number Status, Message Template Status) integrado com Kira para alertas precoces de risco de banimento

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
