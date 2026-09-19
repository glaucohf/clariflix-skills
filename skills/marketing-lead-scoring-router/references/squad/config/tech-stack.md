# Tech stack (integrações da especificação)

- HubSpot CRM — campo customizado Lead Score (0-100), Tier (Hot/Warm/Cold/Unfit), Score Breakdown (JSON), SDR Designado, Fonte Normalizada; webhook de novo contato para Scout; criação automática de deal por Vector para leads Warm+; ativação de sequences para Warm
- Meta Lead Ads API — webhook de novo lead de campanhas Facebook/Instagram Lead Ads para Scout
- Google Ads Lead Form Extensions — webhook de novo lead de formulários Google Ads para Scout
- LinkedIn Lead Gen Forms — webhook de novo lead de anúncios LinkedIn para Scout
- WhatsApp Business API (via Patagon AI ou Leadsales) — evento de novo contato iniciado para Scout; envio de mensagem de primeiro contato automatizado para leads Warm (Vector aciona)
- Clay — waterfall enrichment primary engine, ICP custom tables, intent signals de 100+ fontes (via MCP)
- Apollo.io — enriquecimento complementar de contatos e prospecting (via MCP ou API direta)
- Cognism — enriquecimento GDPR-compliant para contatos internacionais (via API)
- Apify MCP — scraping de perfil LinkedIn para validacao de cargo/empresa quando email disponıvel
- ClickUp — prova de trabalho: task automatica por lead Hot com brief completo, dashboard de KPIs em tempo real, relatorio semanal de performance, formulario de feedback dos SDRs
- Slack — alertas de lead Hot sem contato (Warning/Critical), notificação push para SDR designado, relatório diário de pipeline para Sales Lead
- n8n — orquestracao de workflows de normalizacao de leads de fontes nao-padrao e notificacoes complexas (complemento no-code para integrações customizadas)
- Langfuse — observabilidade OTEL de todos os agents, rastreamento de latência de scoring (meta < 60s), quality gates (dev 70% / staging 85% / prod 95% task success), log de todas as decisões de roteamento para auditoria
- Google Sheets / Looker Studio — dashboard executivo de KPIs (speed-to-lead, conversão por tier, volume por fonte) para CMO e Sales Lead

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
