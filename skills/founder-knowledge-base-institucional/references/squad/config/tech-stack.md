# Tech stack (integrações da especificação)

- Notion MCP — fonte primária de documentos, local de entrega de memos e briefings, armazenamento do grafo legível por humanos
- Slack MCP — ingestão de threads estratégicos exportados, entrega de alertas do Radar e digest do Chief of Staff, interface /clone para consultas ao Persona Forge
- Google Calendar / Outlook MCP — leitura de agenda pelo Chief of Staff para disparo de briefings pré-reunião e detecção de datas críticas (board, investors)
- Gmail MCP — ingestão de emails estratégicos exportados pelo SCRIBE, monitoramento de follow-ups pelo Chief of Staff
- Sembly / Fireflies API — ingestão automática de transcrições de reuniões gravadas para o SCRIBE
- ClickUp MCP — registro de tarefas e artefatos como prova de trabalho verificável, gestão de follow-ups pelo Chief of Staff
- ElevenLabs API — opcional: voz do clone para versão de áudio do Persona Forge (digital twin executivo para podcasts internos ou mensagens de voz)
- Supabase pgvector — vector store para embeddings do grafo (nós, arestas, corpus do clone), recuperação semântica de alta performance
- LangGraph / Claude Agent SDK — orquestração stateful dos workers, controle de paralelismo (SCRIBE + Cartographer + Radar em paralelo), retry logic e gerenciamento de estado do grafo
- Langfuse — observabilidade OTEL completa: tracing de cada ingestão e consulta, custo por worker, taxa de aprovação do Auditor, quality gates (dev 70% / staging 85% / prod 95% task success)
- EXA Web Search MCP — pesquisa de sinais externos pelo Radar e contextualização de mercado pelo Wargame
- Google Drive — fonte de documentos históricos (decks, board packs, docs estratégicos) para ingestão pelo SCRIBE

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
