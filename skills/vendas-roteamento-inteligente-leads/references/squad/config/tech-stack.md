# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP HubSpot disponível) ou Pipedrive/Salesforce via API — leitura e escrita de leads, contatos, deals, atividades
- WhatsApp Business API: Gupshup ou AiSensy (crítico Brasil) — notificação de vendedores e mensagem de apresentação ao lead
- Calendário: Google Calendar e/ou Microsoft Outlook via MCP — consulta de disponibilidade em tempo real para Atlas
- Enriquecimento: Clay (principal) + Apollo.io (275M+ contatos) — enriquecimento automático pelo Argos
- Comunicação interna: Slack — alertas do Farol e notificações do Hermes para vendedores
- Gestão de tarefas/prova de trabalho: ClickUp — cada roteamento gera task com artefato verificável (card de lead + decisão documentada)
- Observabilidade: Langfuse (OTEL) — rastreamento de todas as decisões de roteamento, latência por agente, quality gates
- Ads/Sinais de intenção: Meta Ads + Google Ads (UTM params) — contexto de origem do lead para scoring de intenção do Oracle
- Orquestração: LangGraph (controle fino de estado do funil) + Claude Agent SDK (Maestro como Ópus lead, workers como Sonnet)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
