# Tech stack (integrações da especificação)

- HubSpot CRM — campo customizado ICP Fit Score por lead/empresa, propriedades de segmento e sinais, webhook de novo lead para trigger de enriquecimento
- Clay — waterfall enrichment primary engine, ICP custom tables, intent signals agregados de 100+ fontes
- Apollo.io — prospecting consolidado, enriquecimento de contatos, dados de seniority e titulo
- Cognism — enriquecimento complementar com foco em compliance GDPR para mercados internacionais
- ClickUp — prova de trabalho: task automática por ciclo de enriquecimento, dashboard de ICP Score médio da pipeline, alertas de desvio de ICP
- LinkedIn Sales Navigator — sinais de atividade de contatos, mudanças de emprego, company updates
- Bombora / 6sense — intent data B2B por tópico e segmento
- n8n — orquestração de workflows de enriquecimento e notificações (complemento no-code)
- Langfuse — observabilidade OTEL de todos os agents, quality gates (dev 70% / staging 85% / prod 95% task success)
- Slack / Email — alertas de Hot Accounts (intent score > 70) e notificações de nova versão de ICP publicada

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
