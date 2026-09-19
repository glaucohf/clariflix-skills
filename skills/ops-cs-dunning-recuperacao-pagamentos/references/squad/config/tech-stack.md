# Tech stack (integrações da especificação)

- Gateway de Pagamento: Stripe (Payment Intents, Customer Portal, Account Updater, webhooks de falha em tempo real), Asaas, Iugu, Vindi ou PagSeguro — fonte primária de eventos de falha e endpoint de retry de cobrança
- WhatsApp Business API: 360dialog, Twilio ou Meta Cloud API direta — canal #1 de recuperação no Brasil, com gestão de templates HSM aprovados e janela de conversação de 24h
- Email: SendGrid ou Amazon SES — canal de cobrança formal com rastreamento de abertura, clique e resposta
- SMS: Twilio, Zenvia ou Sinch — canal de reforço para steps críticos de última chance
- ClickUp (Brain2 / MCP server) — hub de tasks de cobranca, prova de trabalho, historico de sequencias, HITL queue e registro de outcomes, espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce — dados de conta (MRR, segmento, CSM responsável, tempo de casa, histórico de pagamentos, contatos autorizados)
- Supabase / Postgres — estado das sequências de dunning, log de mensagens enviadas, histórico de tentativas de cobrança, negociações registradas, cohorts de inadimplentes e bad debt
- Langfuse — observabilidade OTEL, tracing de cada sequência de dunning, evals de qualidade das mensagens geradas pelo Flex, quality gates dev/staging/prod, rastreamento de custo por cobrança recuperada
- Claude Agent SDK / LangGraph — orquestração do workflow de recuperação com estado persistido, retry logic e gerenciamento de eventos assíncronos (resposta de cliente pode chegar horas depois)
- Slack — notificações HITL urgentes para time financeiro (negociação acima do threshold), alertas de spike de falhas para time técnico, relatório semanal de recuperação para Head Financeiro
- Plataforma de CS (ChurnZero, Custify, Gainsight) — integração bidirecional: leitura de segmento e health score do cliente para personalizar a abordagem, escrita de eventos de dunning no timeline do cliente para o CSM ter contexto completo

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
