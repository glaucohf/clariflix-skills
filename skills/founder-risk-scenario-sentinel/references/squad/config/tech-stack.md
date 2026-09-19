# Tech stack (integrações da especificação)

- Slack (canal #sentinel-alerts — entrega de Risk & Scenario Briefs, alertas Críticos de Vela com menção direta ao founder, notificações de HITL Gates, digest semanal de sinais regulatórios e macro)
- Notion (Risk Knowledge Base central — armazenamento permanente de Risk Registers, Risk & Scenario Briefs históricos, Expert Lens Reports, Board Risk Updates, rastreabilidade completa de todos os riscos identificados e seus status)
- ClickUp (Risk Register integrado — cada risco identificado vira task com status de monitoramento, responsável, prazo de resposta e prova de trabalho do ciclo de análise; conectado ao projeto estratégico do founder)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia paralelismo de Lexis/Gaia/Chronos, estado do Risk Register entre sessões, crons de monitoramento contínuo de Vela)
- Langfuse (observabilidade OTEL — tracing de custo por agente/token, evals de qualidade de alertas, dashboard de KPIs do Sentinel — taxa de verificação, false positive rate, tempo de antecipação, latência por fase do pipeline)
- API do Diário Oficial da União — LexML / DOU-API (Lexis usa para monitoramento em tempo real de publicações de normas e resoluções de agências reguladoras)
- Portais de Consulta Pública das Agências Reguladoras — BACEN, CVM, ANVISA, ANATEL, ANEEL, ANS via Web Scraping com MCP (Lexis usa para detectar consultas públicas antes da publicação final)
- API do Senado Federal — Legis / Câmara dos Deputados API (Lexis usa para acompanhamento de projetos de lei em tramitação com tags setoriais relevantes)
- API do BACEN — SGS e PTAX (Gaia e Vela usam para monitoramento em tempo real de Selic, câmbio, spreads de crédito e indicadores financeiros)
- Brave Search API / Perplexity API (Lexis, Gaia e Argos usam para web search de sinais, verificação de fontes primárias e coleta de evidências contrárias em tempo real)
- Google Alerts via RSS (Vela usa para monitoramento contínuo de termos críticos do setor — nome de reguladores relevantes, termos técnicos do produto/serviço, nomes de concorrentes em contexto regulatório)
- LinkedIn via MCP/Apify (Gaia e Vela usam para sinais de movimentos de reguladores, think tanks e policy makers relevantes para o setor do cliente)
- Vector DB — Pinecone ou Qdrant (armazenamento semântico do Risk Register histórico, corpus do founder para Oráculo, normas vigentes, cenários anteriores com outcomes — busca semântica para identificar padrões em riscos similares)
- Mem.ai / Sembly (ingestão contínua do corpus do founder para Oráculo — notas de reunião, decisões estratégicas, reflexões e frameworks explicitados em conversas)
- MCP Servers (camada de integração universal — cada ferramenta acima exposta como tool para os agents via protocolo MCP, permitindo Nexus rotear para as ferramentas corretas sem acoplamento direto)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
