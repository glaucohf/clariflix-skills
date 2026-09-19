# Tech stack (integrações da especificação)

- Google Calendar / Outlook Calendar (agenda e eventos — trigger principal do Briefing Agent)
- Gmail / Outlook Email (ingestão de sinais, captura de commitments, envio de lembretes)
- HubSpot / Salesforce CRM (histórico de contas, deals, notas de relacionamento)
- ClickUp (gestão de tasks, follow-ups, prova de trabalho do squad)
- Notion / Mem.ai (knowledge base do founder, notas de reuniões, board packs)
- Sembly / Fireflies / Otter (transcrição automática de reuniões para captura de ações)
- Slack (entrega de briefs, alertas, digests e interface conversacional com o founder)
- LinkedIn (pesquisa de interlocutores para Kira e Intel)
- Brave Search / Perplexity MCP (deep research para Kira e Intel)
- Langfuse (observabilidade OTEL, tracing de tokens e custo por agente)
- Vector DB — Pinecone / Qdrant (corpus do founder para Sage, histórico de intel)
- Google Analytics / Metabase / Looker (métricas para Memo Agent e Atlas)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
