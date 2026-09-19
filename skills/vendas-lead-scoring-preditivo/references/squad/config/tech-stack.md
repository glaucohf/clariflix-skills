# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível) ou Pipedrive — source of truth para lead e deal data, destino de todos os score writes e activity logs
- WhatsApp Business API: Gupshup ou AiSensy — canal de outreach e recepção de sinais de engajamento (mensagem lida, respondida)
- Enriquecimento: Apollo.io (275M+ contatos) via API — firmográficos, contatos adicionais, tech stack
- Enriquecimento complementar: Clay — workflows de enriquecimento multi-fonte com waterfall
- Ads / Intent Signals: Facebook Lead Ads, Google Ads — webhooks de novos leads com UTMs completos
- Gestão de tarefas: ClickUp — Fila_do_Dia dos reps, proof-of-work por task, registro de artefatos verificáveis
- Comunicação interna: Slack — alertas de deals em risco, leads Hot sem contato, aprovações HITL
- Calendário: Google Calendar — disponibilidade dos reps para roteamento e agendamento
- Observabilidade: Langfuse (OTEL) — evals de qualidade dos agentes, quality gates por ambiente, traces de todas as chamadas LLM
- Orquestração: LangGraph + Claude Agent SDK — controle de estado do pipeline, workflows determinísticos
- Armazenamento de features: PostgreSQL/Supabase — Feature Store com histórico de scores e features por lead

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
