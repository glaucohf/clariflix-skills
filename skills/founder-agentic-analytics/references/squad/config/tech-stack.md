# Tech stack (integrações da especificação)

- WrenAI ou equivalente open-source (camada semântica governada, contexto semântico sobre SQL, suporte a 20+ fontes)
- PostgreSQL / MySQL / BigQuery / Snowflake (banco de dados transacional ou warehouse da empresa)
- HubSpot ou Salesforce CRM (métricas de pipeline, conversão, receita por fonte)
- Stripe / Conta Azul / Omie (métricas financeiras: MRR, churn, LTV, inadimplência)
- Google Ads / Meta Ads (CAC por canal, ROAS, CPC, impressões)
- Google Sheets / Notion (fontes de dados semi-estruturadas do founder)
- ClickUp (registro de decisões, audit trail, follow-ups do Clio)
- Slack (entrega de alertas críticos da Cassandra, interface conversacional opcional)
- Langfuse (observabilidade OTEL: rastreamento de cada query, custo de tokens, latência, acurácia)
- Claude Agent SDK + LangGraph (orquestração stateful das sessões analíticas multi-turno)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
