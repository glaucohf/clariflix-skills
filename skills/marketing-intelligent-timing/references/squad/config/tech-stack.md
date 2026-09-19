# Tech stack (integrações da especificação)

- HubSpot CRM — leitura de historico de engajamento por contato, escrita de Timing Profile como propriedade customizada por lead, webhooks de eventos de abertura/clique/resposta, sincronizacao de opt-out list em tempo real
- Instantly.ai — plataforma de cold email outreach: leitura de metricas de engajamento por sequencia e por toque, escrita de agendamentos otimizados via API, sincronizacao de blacklist e bounce list
- LinkedIn Sales Navigator — leitura de eventos de visualizacao de perfil e interacoes, agendamento de InMails via API no horario otimizado
- WhatsApp Business API (via Patagon AI ou BotPenguin) — envio de mensagens de outreach e follow-up no horario calculado por Helios, leitura de status de leitura (double-check azul) como sinal de engajamento para Sirius
- ClickUp — prova de trabalho: task automatica por ciclo de schedule gerado, dashboard de KPIs de timing (open rate, reply rate, uplift vs. baseline, Channel Health Score por canal), alertas de anomalia como tasks de alta prioridade
- Langfuse — observabilidade OTEL de todos os agents, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latencia do pipeline de agendamento, evals de qualidade do modelo de timing
- n8n — orquestracao dos workflows de webhooks de engajamento, filas de retry de envio, sincronizacao de opt-out entre plataformas e notificacoes para o time (complemento no-code para integracao entre sistemas)
- Google Sheets / Looker Studio — dashboard executivo de Uplift Report mensal para apresentacao ao board (Lumina output renderizado em visualizacao acessivel sem acesso ao sistema)
- Mailchimp / ActiveCampaign (opcional) — integracao para squads que usam email marketing em adicao ao cold outreach, leitura de metricas de campanha nurture para incluir no modelo de Sirius

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
