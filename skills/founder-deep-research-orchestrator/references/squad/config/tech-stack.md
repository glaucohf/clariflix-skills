# Tech stack (integrações da especificação)

- Slack (intake de perguntas via canal #founder-intel + entrega de briefs + alertas de Blade sobre movimentos competitivos)
- Notion (Knowledge Base central — armazenamento permanente de briefs, corpus do founder, histórico de pesquisas)
- ClickUp (criação automática de tasks de follow-up pelo Echo após cada brief — prova de trabalho e rastreabilidade)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia paralelismo dos workers e estado da sessão)
- Langfuse (observabilidade OTEL — tracing de custo por agente/token, evals de qualidade por brief, dashboard de KPIs do squad)
- Brave Search API ou Perplexity API (web search dos workers — principal fonte de dados em tempo real)
- Vector DB — Pinecone ou Qdrant (armazenamento e busca semântica do corpus do founder, briefs históricos e base de conhecimento)
- Gmail (ingestão de newsletters, relatórios e sinais estratégicos para alimentar workers via Echo/Chief of Staff)
- LinkedIn Sales Navigator (Blade usa para sinais de hiring e movimentos de concorrentes)
- Crunchbase / PitchBook API pública (Thesis usa para sinais de fundraising e múltiplos)
- MCP Servers (camada de integração universal — cada ferramenta exposta como tool para os agents via protocolo MCP)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
