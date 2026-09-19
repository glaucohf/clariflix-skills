# Tech stack (integrações da especificação)

- LinkedIn (scraping via Apify Actor) — monitoramento diário de Company Pages dos concorrentes (headcount, job postings), perfis de fundadores e C-level para sinais de estratégia pública, detecção de mudanças de descrição de empresa que sinalizam reposicionamento
- Crunchbase (API ou scraping) — monitoramento de rodadas de investimento, aquisições, novas parcerias e mudanças de liderança dos concorrentes Tier 1 e Tier 2
- Product Hunt — alertas de novos launches de concorrentes ou de startups emergentes no mesmo espaço competitivo
- G2 / Capterra / Reclame Aqui (scraping via Apify) — monitoramento de novas reviews de concorrentes com extração de sentimento e temas críticos (pontos fracos exploráveis)
- ClickUp — prova de trabalho central: tasks de alertas com prioridade e janela de ação, Counter-Play Briefs anexados, Competitive Intelligence Baseline como documento de referência, dashboard de cobertura de concorrentes e SLA de detecção
- Slack — canal #competitive-intel para Competitive Flash Cards em tempo real, Competitive Intel Weekly Briefing toda sexta-feira, notificações de gate BLOCKED de Veritas para revisão humana urgente
- Notion — repositório dos Competitive Landscape Reports mensais, Board Intelligence Packs, Movement Profiles atualizados e Corpus do Founder estruturado como knowledge base do squad
- n8n — orquestração de workflows de varredura, webhooks de detecção de mudança em páginas monitoradas (diff de páginas de preço), agendamento de crons por frequência e tier, roteamento de sinais entre agentes
- Apify (via MCP Docker) — scraping estruturado de páginas de preço (diff automático), job postings de LinkedIn, reviews de G2/Capterra, conteúdo de blogs de concorrentes, perfis públicos de fundadores
- Langfuse — observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de sinal (SLA de detecção vs. alerta), evals de acurácia de classificação de Lynx e de qualidade de hipóteses de Ares, custo por alerta gerado
- HubSpot CRM (opcional) — campo Competitive Threat Level nos deals ativos, context cards de concorrentes em oportunidades em negociação, alerta automático para SDRs/AEs quando Hermes detecta mudança de preço de concorrente com deals em andamento
- EXÁ (via MCP Docker) — web search para contexto adicional de sinais de menor confiança, pesquisa de background de concorrentes emergentes detectados por Hawk, busca de cobertura de mídia de eventos competitivos relevantes
- Google Alerts / RSS Aggregator — camada complementar de monitoramento de menções públicas de concorrentes em mídia, redução de latência para eventos de alta visibilidade (funding announcements, lançamentos com cobertura de imprensa)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
