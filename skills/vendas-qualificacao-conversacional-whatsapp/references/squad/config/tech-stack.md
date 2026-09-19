# Tech stack (integrações da especificação)

- WhatsApp Business API via Gupshup ou AiSensy (envio/recepção de mensagens, webhooks de status)
- HubSpot CRM via MCP HubSpot oficial (leitura e escrita de contatos, deals, propriedades customizadas, activities)
- Google Calendar ou Calendly API (disponibilidade de closers, criação de eventos, webhooks de cancelamento)
- Meta Ads Lead Ads (webhook de novo lead -> N8N -> Orchestrator)
- Apollo.io ou Clay (enriquecimento de dados B2B: empresa, cargo, contato)
- N8N como middleware de webhook (recebe sinais de múltiplas fontes e normaliza payload para o Orchestrator)
- ClickUp (artefatos verificáveis por task: scorecards, conversation logs, relatórios de higiene e intelligence)
- Langfuse OTEL (observabilidade de todas as chamadas LLM: latência, tokens, task success rate por agente, evals customizados)
- LangGraph (orquestração do grafo de agentes com estado persistente por lead_id)
- Claude API — Opus 4 para Orchestrator e Critic; Sonnet 4 para workers (balanço custo/performance)
- Píxel de site do cliente (sinais de reativação para o Lázaro via webhook de evento personalizado)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
