# Tech stack (integrações da especificação)

- Crunchbase / PitchBook dados públicos (mapeamento de portfólios de VCs e histórico de investimentos para o Vega)
- LinkedIn API / Sales Navigator (warm intro path mapping, perfis de GPs e managing partners para o Vega e Mnemo)
- EXA / Perplexity MCP (pesquisa em tempo real de atividade de investidores, teses publicadas, notícias de mercado)
- Gmail / Outlook MCP (histórico de comunicações com investidores para o Mnemo, envio controlado via Gate)
- Google Drive / Notion (repositório do data room, versionamento de documentos pelo Atlas)
- Dealroom / Captable.io / Carta (cap table atualizado, documentos de rodadas anteriores para o Atlas)
- Stripe / QuickBooks / Conta Azul (dados financeiros reais para o financial model e métricas do Atlas)
- HubSpot / Salesforce CRM (cohort de clientes, churn, expansão, CAC — métricas de tração para Atlas e Brutus)
- Mixpanel / Amplitude / PostHog (métricas de produto, DAU/MAU, NPS, engagement para o data room)
- ClickUp (Roadshow Tracker — pipeline de captação, tasks, follow-ups, audit trail de toda a operação)
- Sembly / Fireflies / Otter.ai (transcrições automáticas de meetings com investidores para o Mnemo)
- Langfuse (observabilidade OTEL — tracing de tokens, custo por agente, task success rate por pipeline)
- Vector DB — Pinecone / Qdrant (Knowledge Graph do Mnemo, corpus de Intelligence Briefs do Vega, histórico de narrativas)
- Slack (interface conversacional do founder com o Orion — recebe alertas, approva mensagens, consulta status do roadshow)
- DocSend / Docsend-compatible viewer (rastreamento de visualização do data room — quem abriu, quanto tempo em cada seção)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
