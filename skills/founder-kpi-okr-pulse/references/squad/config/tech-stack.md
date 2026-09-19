# Tech stack (integrações da especificação)

- HubSpot / Salesforce (CRM — pipeline de vendas, MRR, churn, NPS, métricas de CS via MCP)
- Stripe / Conta Azul / Omie (financeiro — receita, MRR, ARR, inadimplência, unit economics via MCP ou API)
- Google Analytics 4 / Mixpanel / Amplitude (produto/analytics — DAU, MAU, activation, retention, engagement via MCP)
- Meta Ads / Google Ads (mídia paga — CPL, CAC, ROAS, impressões, conversões via MCP ou API)
- Google Sheets / Airtable (planilhas operacionais — KPIs que ainda não têm sistema dedicado, coletados via MCP)
- ClickUp (OKRs source-of-truth + criação automática de tasks de recomendação + prova de trabalho do squad)
- Notion (Knowledge Base — armazenamento permanente do Pulse Report, OKRs, histórico de diagnósticos e playbook de alavancas)
- Slack (entrega do Pulse semanal via canal privado #founder-pulse + alertas de desvio crítico em tempo real)
- WhatsApp Business API (versão ultra-curta do Pulse em 5 bullets via Sigma — opcional, para founders mobile-first)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia ciclo semanal e queries ad-hoc)
- Langfuse (observabilidade OTEL — tracing de custo por agente/token, evals de qualidade do diagnóstico, dashboard de KPIs do squad)
- Vector DB — Pinecone ou Qdrant (histórico de KPIs, corpus do founder para Sigma, playbook de alavancas, heurísticas de Véra)
- MCP Servers (camada de integração universal — cada sistema exposto como tool para Pulsar via protocolo MCP)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
