---
task: orionPipeline()
responsavel: "ORION"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote do Digital Twin Operacional"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "conjunto de artefatos verificáveis no ClickUp e Notion: (1) Knowledge Graph do Founder v{N}"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "grafo estruturado e auditável com frameworks, princípios, decisões e vocabulário do founder, com score de completude por categoria"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) Log de Demandas Atendidas"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "histórico completo de cada pergunta recebida, modo de resposta ativado, output gerado, veredicto do SENTINEL e decisão de HITL quando aplicável"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(3) Relatório Semanal de Inteligência (VIGIL)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do Digital Twin. Recebe toda demanda direcionada ao founder (via Slack, email, WhatsApp, formulário interno ou comando direto), classifica por tipo (operacional, estratégica, cri…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio – o squad nunca envia comunicação externa autonomamente"
    - "[ ] L3: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política interna – founder aprova com opções claras antes da execução"
    - "[ ] L3: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao de pensamento antes de ser persistida no corpus canônico"
    - "[ ] L2: ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma aproximação e pode escalonar"
    - "[ ] L2: STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer caminho seja comunicado como recomendacao oficial do squad"
---

# Orquestrar Pipeline do Clône Estratégico do Founder

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Clône Estratégico do Founder |
| **status** | `pending` |
| **responsible_executor** | ORION (ÓRION — O Chief of Staff Cognitivo) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 13 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do Digital Twin. Recebe toda demanda direcionada ao founder (via Slack, email, WhatsApp, formulário interno ou comando direto), classifica por tipo (operacional, estratégica, criativa, relacional, financeira), avalia confiança do corpus para aquela classe de pergunta e roteia para o modo correto: Clone Mode (resposta direta pelo ECHO), Research Mode (ativa workers de pesquisa antes de responder), ou Escalation Mode (prepara briefing e aciona HITL). Gerencia o estado de cada demanda no ClickUp, agrega outputs dos workers, decide quando acionar o SENTINEL antes de entregar qualquer resposta externa, e alimenta o ciclo de aprendizado com cada interação validada. Também agenda e prepara reuniões do founder (agenda, pré-leitura, follow-ups) e monitora a agenda estratégica de forma proativa. Não executa nenhuma ação irreversível — seu papel é orquestrar, sintetizar e garantir que o clone seja fiel ao founder.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote do Digital Twin Operacional
- conjunto de artefatos verificáveis no ClickUp e Notion: (1) Knowledge Graph do Founder v{N}
- grafo estruturado e auditável com frameworks, princípios, decisões e vocabulário do founder, com score de completude por categoria
- (2) Log de Demandas Atendidas
- histórico completo de cada pergunta recebida, modo de resposta ativado, output gerado, veredicto do SENTINEL e decisão de HITL quando aplicável
- (3) Relatório Semanal de Inteligência (VIGIL)
- movimentos competitivos, oportunidades e alertas da semana com fontes
- (4) Relatório Mensal do Clone
- métricas de autonomia, score de fidelidade, gaps identificados e plano de melhoria do corpus para o próximo mês
- (5) Drafts de Comunicação (HERALD)
- board packs, memos e comunicados com histórico de versões e aprovações
- (6) Dashboard Langfuse
- observabilidade em tempo real de custo, latência, quality gates e taxa de aprovação do SENTINEL por tipo de demanda

## Trigger

Orquestrador central do Digital Twin. Recebe toda demanda direcionada ao founder (via Slack, email, WhatsApp, formulário interno ou comando direto), classifica por tipo (operacional, estratégica, criativa, relacional, financeira), avalia confiança do corpus para aquela classe de pergunta e roteia para o modo correto: Clone Mode (resposta direta pelo ECHO), Research Mode (ativa workers de pesquisa antes de responder), ou Escalation Mode (prepara briefing e aciona HITL). Gerencia o estado de cada demanda no ClickUp, agrega outputs dos workers, decide quando acionar o SENTINEL antes de entregar qualquer resposta externa, e alimenta o ciclo de aprendizado com cada interação validada. Também agenda e prepara reuniões do founder (agenda, pré-leitura, follow-ups) e monitora a agenda estratégica de forma proativa. Não executa nenhuma ação irreversível — seu papel é orquestrar, sintetizar e garantir que o clone seja fiel ao founder.

## Knowledge base (o que o executor consulta)

- Slack (MCP): canal principal de recepção de demandas ao squad e entrega de respostas
- inbox do ORION, notificações do VIGIL, alertas do GATE
- Gmail / Google Workspace (MCP): ingestão de emails estratégicos para o CHRONICLE, entrega de drafts do HERALD para revisão do founder, leitura de threads para contexto de demandas
- WhatsApp Business API: canal prioritário para alertas L3 do GATE e sinais CRÍTICOS do VIGIL
- founder responde APROVAR/REJEITAR diretamente no WhatsApp
- Notion: repositório primário do Knowledge Graph estruturado, storage de drafts do HERALD, documentação de decisões estratégicas
- integração via MCP ou Notion API
- Sembly / Fireflies.ai: transcrição automática de reuniões e calls do founder para ingestão pelo CHRONICLE
- fonte primária de conhecimento tácito não documentado
- Google Calendar (MCP): leitura de agenda do founder para pre-briefings do ORION, disparo do HERALD para preparação de reuniões importantes, monitoramento de compromissos estratégicos
- ClickUp: gestão de todas as tarefas do squad como prova de trabalho verificável
- cada demanda, pesquisa e comunicação gera uma task auditável com status, output e histórico de aprovações
- Supabase (pgvector): base vetorial para recuperação semântica do Knowledge Graph do founder
- busca por similaridade semântica em corpus de alta dimensão
- EXA MCP (via Docker): busca web em tempo real para o ATLAS e o VIGIL
- pesquisa profunda com fontes verificáveis
- Apífy (via Docker): scraping estruturado de concorrentes, LinkedIn, G2/Capterra para o VIGIL e ATLAS
- Langfuse (OTEL): observabilidade completa de todas as execuções
- tracing de cada resposta do ECHO, score de fidelidade pelo SENTINEL, latência por worker, custo de tokens por tipo de demanda, quality gates por ambiente (dev 70% / staging 85% / prod 95%)
- LangGraph / Claude Agent SDK: orquestração stateful do pipeline
- controle de estado de demandas complexas, paralelismo do ATLAS em swarm mode, retry logic para falhas de worker
- ElevenLabs (opcional): voz sintetizada do founder para respostas em áudio
- digital twin executivo completo para reuniões assíncronas ou conteúdo em vídeo

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic SENTINEL antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote do Digital Twin Operacional
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SENTINEL registrado
- [ ] Gate L3 respeitado: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder ante…
- [ ] Gate L3 respeitado: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou…
- [ ] Gate L3 respeitado: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuin…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma apr… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — VIGIL ao detectar sinal competitivo CRÍTICO fora do ciclo semanal: notificação imediata ao founder com proposta de contra-jogada — founder decide se ativa resp… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — CHRONICLE ao identificar gap crítico no corpus que impacta a confiabilidade do ECHO em categoria de alto volume: agenda sessão de captura de conhecimento com o… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** ECHO
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
