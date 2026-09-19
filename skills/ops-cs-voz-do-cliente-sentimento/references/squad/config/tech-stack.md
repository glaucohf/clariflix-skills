# Tech stack (integrações da especificação)

- ClickUp (Brain2 / MCP server) — hub de tasks de ação, prova de trabalho com tags VOC, rastreabilidade de insights, espelhando arquitetura AIOX; usado pelo Atlas para criação de tasks e pelo Orion para leitura de eventos de produto
- Zendesk ou Intercom — fonte primária de tickets de suporte com CSAT e comentários; volume diário normalizado pelo Haruki; campo de tema do Yara pode ser gravado de volta como tag no ticket via API
- NPS / CSAT: Delighted, Typeform, Wootric ou SurveyMonkey — scores e verbatims de pesquisas; NPS é a fonte de sentimento mais estruturada e prioritária
- WhatsApp Business API — mensagens de atendimento anônimizadas; canal #1 de feedback informal no Brasil; exige tratamento nativo de texto curto e linguagem informal
- Reviews públicos: G2, Capterra, Trustpilot, App Store, Google Play — coletados semanalmente via API ou scraping; fonte de feedback de prospects além de clientes
- Notion — destino do relatorio semanal completo em markdown com historico pesquisavel por tema e data
- Slack — canal #voc-alertas para alertas do Rapid, canal #voc-insights para relatório semanal resumido, DMs para responsáveis de tasks aprovadas pelo Atlas
- Supabase / Postgres — banco de estado do squad: voc_raw_feedback, voc_analyzed_feedback, voc_trends_daily, voc_weekly_reports, voc_alerts, voc_actions; histórico completo auditável
- Langfuse — observabilidade OTEL do pipeline, tracing de classificação do Yara, evals de qualidade dos insights do Lyra, quality gates dev/staging/prod (70/85/95% accuracy)
- Claude Agent SDK / LangGraph — orquestração do pipeline multi-agente com gerenciamento de estado, retry logic e paralelização de ingestão de canais
- CRM: HubSpot ou Salesforce — dados de segmento, MRR e CSM responsável por account_id para ponderação de tendências por segmento e cálculo de impacto de receita
- Jira ou Linear (opcional) — leitura do changelog de produto para correlação de tendências com releases e incidentes no Orion
- Airtable ou Google Sheets (fallback) — canais de feedback que não tem API estruturada podem ser ingeridos via planilha compartilhada como fonte temporária

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
