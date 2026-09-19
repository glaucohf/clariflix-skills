# Tech stack (integrações da especificação)

- ERP (SAP / Omie / Conta Azul / Totvs / Netsuite) — fonte primaria de lancamentos contabeis: API de leitura para extrair transacoes, NFs, contratos, saldos de AP e AR; API de escrita para importacao de journal entries aprovados (somente apos HITL); acesso ao plano de contas
- Bancos via Open Finance / OFX / API Bancaria (Bradesco, Itau, Banco do Brasil, Nubank Business, BTG, Inter) — extrato bancario automatizado diario ou mensal; integracao via Open Finance API (BACEN) para bancos disponiveis ou exportacao OFX para os demais
- Billing Systems (Stripe / Chargebee / Vindi / Iugu / Hotmart / Eduzz) — historico de cobranças, assinaturas, mudancas de plano, descontos, estornos, webhooks de eventos de pagamento em tempo real
- ClickUp (Brain2 / Super Agents / Autopilot Agents + MCP) — hub de tasks e prova de trabalho: task por excecao HITL L3, Closing Package como task de aprovacao click-to-approve, filas de AP e AR como tasks com due date, integracao com AIOX espelhando o workflow de aprovacao
- Slack — notificacoes em tempo real: alerta de Closing Package pronto para aprovacao, exceptions de alto valor detectadas, pagamentos vencendo hoje sem aprovacao, Closing Readiness Score no canal #financeiro
- CRM (HubSpot / Salesforce / Pipedrive) — dados de conta do cliente para AR: historico de relacionamento, tier do cliente, health score, open tickets de suporte (contexto para cobranca empatetica)
- CS Platforms (ChurnZero / Custify / Chargebee / Gainsight) — health score para priorizacao de cobranca: clientes em risco de churn recebem abordagem diferente de cobranca (empatetica, com oferta de renegociacao) vs. clientes saudaveis
- WhatsApp Business API — canal de cobranca AR: envio de lembretes de vencimento e comunicacoes de cobranca na sequencia configurada pela Dunna, com templates pre-aprovados pela politica de cobranca
- Supabase / Postgres — estado do squad: Canonical Transaction Set, Exception Queue, status de cada ciclo de fechamento, historico de matches e exceptions, Closing Packages gerados e aprovados
- Langfuse — observabilidade OTEL: tracing de cada ciclo de reconciliacao (source collection -> matching -> exception classification -> investigation -> closing package -> approval), evals por tipo de match e exception, quality gates (dev 70% / staging 85% / prod 95% de precisao de matching)
- Claude Agent SDK / LangGraph — orquestracao multi-agente do ciclo de reconciliacao, state management do ciclo de fechamento, embedding similarity para matching probabilistico de descricoes de transacoes
- MCP Servers (camada de integracao universal) — ClickUp MCP, Supabase MCP para acesso padronizado; integracao com bancos via MCP customizado de Open Finance

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
