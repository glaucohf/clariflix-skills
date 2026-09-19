# Tech stack (integrações da especificação)

- ClickUp (Brain2 / MCP server) — hub central de tasks do pacote de renovacao, checklist de preparacao de QBR, prova de trabalho do squad e monitoramento de ativacao; espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce — fonte primaria de datas de renovacao, historico de expansao, MRR, atividades do CSM, notas de QBR, executive sponsor, pipeline de renovacao e decisoes comerciais
- Plataforma de produto: Mixpanel, Amplitude, Segment ou analytics nativo — eventos de uso por conta, DAU/MAU, feature adoption, usuarios ativos vs licencas, sessoes por usuario
- CS Platforms: Gainsight, ChurnZero, Custify, Velaris ou Chargebee — health scores existentes, historico de QBRs gerenciados na plataforma, alertas de renovacao e dados de health ja calculados (integracao bidirecional: leitura e escrita de scores)
- Google Workspace (Google Slides + Google Drive) ou Microsoft 365 (PowerPoint + SharePoint) — geracao e armazenamento de decks de QBR via API; webhook de deteccao de edicao pos-geracao
- Helpdesk: Zendesk ou Intercom — volume de tickets recentes por conta, CSAT, categorias de problema, resolucoes documentadas para o brief
- NPS / CSAT: Delighted, Typeform, Wootric ou nativo da CS platform — scores e verbatims para o brief de sentimento
- Call Recording: Gong, Chorus ou Zoom AI (nativo do CRM) — transcricoes de chamadas de QBR anteriores para o Memory e para o Briefer enriquecer o contexto relacional
- Slack — notificacoes ao CSM (brief pronto, deck gerado, renovacao critica), manager (escalacoes, tasks nao abertas) e Head de CS (relatorio semanal de cobertura e NRR tracking)
- Supabase / Postgres — estado dos agentes, Account Memory, Renewal Readiness Score historico, Expansion Signal Reports, log de tasks criadas e outcomes de renovacao
- Langfuse — observabilidade OTEL, tracing do pipeline de geracao de briefs, evals de qualidade de artefatos, quality gates dev/staging/prod, dashboard de NRR e cobertura de renovacoes
- Claude Agent SDK / LangGraph — orquestracao do pipeline multi-agente com gerenciamento de estado, filas de prioridade e retry logic
- Email / SMTP — relatorio semanal de cobertura de renovacoes para Head de CS e resumo mensal de NRR impact para stakeholders

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
