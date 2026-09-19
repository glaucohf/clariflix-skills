# Tech stack (integrações da especificação)

- CRM: HubSpot (MCP disponível) ou Pipedrive — leitura de contexto do deal e prospect em tempo real pelo MAESTRO; escrita de resultados e atualização de battlecards pelo ARQUIVO (L3 gate)
- WhatsApp Business API (Gupshup, AiSensy, ou QuickReply.ai) — canal primário de acionamento do squad por SDRs e closers no Brasil; entrega de resposta como mensagem rápida copiável
- Interface de call em tempo real: integração com Vapi ou Retell AI para captura de transcrição ao vivo; widget de overlay na tela do vendedor durante a call com resposta em < 15 segundos
- STT em tempo real: Deepgram para transcrição da fala do prospect durante calls, alimentando o MAESTRO com o texto da objeção antes mesmo do vendedor digitar
- Conversation Intelligence: Gong ou Chorus — analise pos-call para identificar objecoes que ocorreram e se foram superadas; dados alimentam ARQUIVO para aprendizado continuo
- ClickUp: registro de cada interação de objection handling como tarefa/artefato verificável com resultado; prova de trabalho do squad por deal
- Slack: notificações de HITL para supervisores (aprovação de desconto, nova objeção detectada); relatório semanal de padrões de objeção para liderança de vendas
- Base vetorial: Supabase pgvector ou Pinecone — armazenamento e busca semântica da base de battlecards, respostas históricas e casos de uso para recuperação em < 3 segundos
- Observabilidade: Langfuse (OTEL) — rastreamento de latência por worker, taxa de aprovação do ARGUS, taxa de uso pelo vendedor (resposta entregue vs resposta efetivamente usada), quality gates dev 70% / staging 85% / prod 95%
- Orquestração: LangGraph ou Claude Agent SDK — controle de estado por sessão de call, paralelismo dos workers de recuperação (battlecard + contexto), retry logic com fallback para resposta genérica se SLA estourar

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
