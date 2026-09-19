# Tech stack (integrações da especificação)

- Clay — motor primário de intent data agregado de 100+ fontes, waterfall enrichment de contas, job posting tracking, technographics e sinais de funding
- Bombora / 6sense — intent data B2B por tópico específico, surge score por conta e segmento
- HubSpot CRM — campo customizado de Signal Score por conta, propriedade de ùltimo sinal detectado, webhook de stage change para atribuiçạ̃o, task automática para SDR/AE quando conta sobe para Hot
- LinkedIn Sales Navigator / LinkedIn API — company updates, mudanças de liderança, job postings críticos, atividade de contatos-alvo
- SEMrush Enterprise — monitoramento de picos de busca orgânica por keyword de problema, share of voice por segmento, menções em AI Overviews
- Crunchbase / PitchBook (via MCP ou webhook) — alertas de funding rounds, M&A, expansão geográfica
- Google Ads + Meta Ads – ativação de campanhas de retargeting disparadas por Demand Surge Playbook (via aprovação HITL)
- ClickUp – prova de trabalho: task automática por conta Hot identificada, dashboard de lead-time de antecipação, registro de playbooks disparados com status
- n8n – orquestração de workflows de monitoramento, webhooks de sinais e notificações no-code (camada complementar de automação)
- Langfuse – observabilidade OTEL de todos os agents, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de sinal
- Slack – alertas em tempo real de Hot Accounts para canal #demand-radar, notificações de Sigma BLOCKED para revisão humana urgente
- WhatsApp Business API (via Patagon AI / BotPenguin) – canal de outreach pós-aprovação Sigma para playbooks onde WhatsApp é o canal de preferência do ICP

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
