# Tech stack (integrações da especificação)

- Zendesk / Intercom (Fin) / Freshdesk — helpdesks primarios para ingestao de tickets; webhook ou polling via MCP para receber conversas encerradas em tempo quasi-real; leitura de metadados de ticket (agente, categoria, resolucao) para contexto do NEXUS
- WhatsApp Business API (Gupshup, AiSensy, Twilio) — canal #1 no Brasil; ingestão de conversas completas incluindo áudio transcrito via Deepgram/Whisper para audit trail completo
- Gong / Chorus / NICE — conversation intelligence para calls de voz; transcrições automáticas alimentam VERITAS e ARIA; dados de sentimento pré-processados reduzem latência do squad
- ClickUp (MCP disponível / Brain2 / Super Agents) — hub de tasks de coaching e correção; cada violação vira uma task rastreável com evidência citada, responsável, prazo e status; dashboard de qualidade agregado no ClickUp; prova de trabalho do squad
- Slack — canal de alertas críticos para gestores (violações VERMELHAS confirmadas pelo SENTINEL); relatório semanal de tendências de qualidade; notificações de HITL para aprovação de mudanças de rubrica
- HubSpot / Salesforce (MCP disponivel) — leitura de perfil de cliente (tier, valor, historico) para contextualizacao de prioridade na fila e ponderacao de score; dados de churn historico para calibrar flag de risco do ARIA
- ChurnZero / Custify / Velaris — CS platforms para leitura de health score do cliente; conversas de clientes com health score baixo recebem prioridade de auditoria e peso maior no flag de risco de churn
- Supabase / Postgres — estado persistente do squad: fila de processamento, scorecards históricos, rubrica ativa, log de contestações, métricas de produção; pgvector para busca semântica na base de conhecimento do VERITAS
- Langfuse (OTEL) — observabilidade completa: tracing por conversa (latência por worker, custo por auditoria, tokens consumidos), quality gates (dev 70% / staging 85% / prod 95% de precisão de detecção validada contra set de conversas anotadas), dashboard de drift de qualidade do squad
- Claude Agent SDK / LangGraph — orquestração do pipeline multi-agente; paralelismo dos 4 workers de auditoria (LEXIS, ARIA, VERITAS, NEXUS rodando simultaneamente por conversa); retry logic com fallback; controle de estado de processamento por batch
- Deepgram / Whisper — ASR para transcrição de áudios do WhatsApp e chamadas de voz não processadas por Gong/Chorus; PT-BR como língua primária com fallback para ES e EN

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
