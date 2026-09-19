# Tech stack (integrações da especificação)

- Slack (MCP): canal principal de recepção de demandas ao squad e entrega de respostas — inbox do ORION, notificações do VIGIL, alertas do GATE
- Gmail / Google Workspace (MCP): ingestão de emails estratégicos para o CHRONICLE, entrega de drafts do HERALD para revisão do founder, leitura de threads para contexto de demandas
- WhatsApp Business API: canal prioritário para alertas L3 do GATE e sinais CRÍTICOS do VIGIL — founder responde APROVAR/REJEITAR diretamente no WhatsApp
- Notion: repositório primário do Knowledge Graph estruturado, storage de drafts do HERALD, documentação de decisões estratégicas — integração via MCP ou Notion API
- Sembly / Fireflies.ai: transcrição automática de reuniões e calls do founder para ingestão pelo CHRONICLE — fonte primária de conhecimento tácito não documentado
- Google Calendar (MCP): leitura de agenda do founder para pre-briefings do ORION, disparo do HERALD para preparação de reuniões importantes, monitoramento de compromissos estratégicos
- ClickUp: gestão de todas as tarefas do squad como prova de trabalho verificável — cada demanda, pesquisa e comunicação gera uma task auditável com status, output e histórico de aprovações
- Supabase (pgvector): base vetorial para recuperação semântica do Knowledge Graph do founder — busca por similaridade semântica em corpus de alta dimensão
- EXA MCP (via Docker): busca web em tempo real para o ATLAS e o VIGIL — pesquisa profunda com fontes verificáveis
- Apífy (via Docker): scraping estruturado de concorrentes, LinkedIn, G2/Capterra para o VIGIL e ATLAS
- Langfuse (OTEL): observabilidade completa de todas as execuções — tracing de cada resposta do ECHO, score de fidelidade pelo SENTINEL, latência por worker, custo de tokens por tipo de demanda, quality gates por ambiente (dev 70% / staging 85% / prod 95%)
- LangGraph / Claude Agent SDK: orquestração stateful do pipeline — controle de estado de demandas complexas, paralelismo do ATLAS em swarm mode, retry logic para falhas de worker
- ElevenLabs (opcional): voz sintetizada do founder para respostas em áudio — digital twin executivo completo para reuniões assíncronas ou conteúdo em vídeo

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
