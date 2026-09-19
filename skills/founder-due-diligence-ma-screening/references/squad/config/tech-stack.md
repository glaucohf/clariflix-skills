# Tech stack (integrações da especificação)

- ClickUp — Gerenciamento de tasks e prova de trabalho: cada triagem e uma task com sub-tasks por agente, status tracking e entrega do artefato final linkado
- Notion / Obsidian — Knowledge base do founder (corpus de decisões, memos anteriores, teses) que alimenta o Eco (Clone Agent)
- Vector DB (Pinecone / Supabase pgvector) — Embeddings do corpus do founder e histórico de triagens anteriores para o Eco e o Columbo aprenderem com cada ciclo
- DataJud (CNJ) — Processos judiciais públicos via API para o Themis
- Receita Federal / CNPJ.info — Dados societários e CNPJ para o Argus
- LinkedIn Sales Navigator — Histórico profissional, tenure de C-level, headcount para Vox e Atlas
- Crunchbase API — Funding history, exits, investors para Fênix e Sigma
- Glassdoor / Blind (scraping) — Cultura e reviews para Vox
- BuiltWith / Wappalyzer — Stack tecnológico para Atlas
- Google News API — Cobertura de mídia para Argus e Vox
- Langfuse — Observabilidade OTEL: tracing de tokens, custo por triagem, latência por agente, task success rate por fase
- Slack — Notificações de status do pipeline ao founder (Target Profile pronto, Deep Dive completo, Memo disponível para revisão, gates L3 aguardando aprovação)
- Gmail / Email — Entrega do Investment Memo final em PDF após aprovacao L3
- INPI — Consulta de patentes e marcas registradas para Themis e Atlas
- BACEN (SCR/API) — Regularidade financeira e dados de crédito para Fenix e Themis

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
