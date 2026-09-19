# Tech stack (integrações da especificação)

- Zendesk / Intercom — fonte primária de tickets sem match KB, webhooks de feedback de resolução do Tier-1, tags de intenção
- ClickUp — task por artigo (prova de trabalho), status do pipeline (Gap Identified -> Draft -> QA -> HITL -> Published -> Monitored), integracao com AIOX
- Confluence / Notion / GitBook / Freshdesk KB — destino de publicação dos artigos (configurável por cliente), API de CRUD de artigos
- Supabase / Postgres — estado do pipeline (gap_id, artigo_id, versão, scores, status), vetorização da KB (pgvector), log de aprovações HITL
- Slack — notificações de HITL pendente, alertas de artigo em estado CRÍTICO (Petra), resumo semanal do Impact Report para canal #kb-updates
- OpenAI Embeddings / Anthropic Claude — geração de embeddings da KB para similarity search, geração de drafts (Vera), fact-check (Lex)
- Langfuse — tracing de cada ciclo de produção (gap -> draft -> revisões -> publicação), evals automatizados por dimensão, quality gates (dev 70% / staging 85% / prod 95% task success)
- Tier-1 Resolver (squad interno) — recebe atualizações da KB via webhook pós-publicação, envia sinal KB_NÃO_RESOLVEU para Petra

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
