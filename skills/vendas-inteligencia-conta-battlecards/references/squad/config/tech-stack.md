# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível) ou Pipedrive — leitura de histórico e escrita de atualizações via MEMÓRIA
- Calendário: Google Calendar ou Outlook (MCP) — leitura de reuniões agendadas para disparo automático do pipeline
- LinkedIn: Clay ou Apollo para enriquecimento de perfis de stakeholders (IRIS)
- Dados de empresa: Apollo.io (275M+ contatos e firmografia), Clearbit Enrichment (SCOUT)
- Stack tecnológica: BuiltWith API ou Wappalyzer (SCOUT — detecção de tecnologias do prospect)
- Notícias e sinais: Google News API, RSS feeds setoriais (SCOUT e ORACLE)
- ClickUp: gestão de tarefas e armazenamento de artefatos como prova de trabalho verificável (HERALD)
- Slack: notificação push do dossiê finalizado ao vendedor (HERALD)
- WhatsApp Business API: entrega alternativa do resumo executivo para vendedores mobile-first (HERALD)
- Observabilidade: Langfuse (OTEL) — rastreamento de cada execução, latência por worker, taxa de aprovação do SENTINEL, quality gates por ambiente
- Orquestração: LangGraph ou Claude Agent SDK — controle de estado do pipeline, paralelismo dos workers, retry logic
- Armazenamento de battlecards: base vetorial (Supabase pgvector ou Pinecone) para recuperação semântica de battlecards análogos

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
