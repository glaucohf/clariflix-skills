# Tech stack (integrações da especificação)

- Plataformas de voz/vídeo: Vapi (webhook pós-call com link de gravação), Retell AI, Zoom (webhook recording.completed), Google Meet (Drive API para gravações), Gupshup/AiSensy para calls gravadas via WhatsApp Business
- STT (Speech-to-Text): Deepgram (latência < 1min/hora de áudio, diarização de speakers, vocabulário customizado) ou AssemblyAI como fallback
- CRM: HubSpot (MCP disponível nativamente) ou Pipedrive — gravação de insights, sinais de risco, score de call, próximo passo como campos customizados no deal e na timeline
- Gestão de tarefas: ClickUp — Coaching Card como task atribuída ao vendedor com link para o trecho da call, proof-of-work verificável por task, Plano de Role-Play semanal como task coletiva
- Comunicação: WhatsApp Business API (Gupshup ou AiSensy) para entrega do coaching card ao vendedor e alertas de risco ao gestor; Slack para integração com times que usam Slack como hub
- Armazenamento de artefatos: Supabase (PostgreSQL) — Transcript Objects, Call Analysis Objects, Call Score Objects, histórico de coaching por vendedor, Feature Store de objeções
- Documentação de coaching: Notion — Coaching Cards formatados, Biblioteca de Counter-Scripts, Plano de Desenvolvimento Individual por vendedor, Briefing Semanal do Gestor
- Observabilidade/Evals: Langfuse (OTEL) — traces de todas as chamadas LLM (análise + coaching), quality gates por ambiente (dev 70% / staging 85% / prod 95%), evals de qualidade do coaching card (rastreabilidade, especificidade, tom)
- Orquestração: LangGraph + Claude Agent SDK — controle de estado do pipeline de análise, workflows determinísticos de sequenciamento (transcrição -> análise -> scoring -> coaching), re-tentativas automáticas em falha
- Armazenamento de áudio: AWS S3 ou Google Cloud Storage — arquivos de áudio/vídeo das calls com retenção configurável (90 dias default, 365 dias para deals fechados)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
