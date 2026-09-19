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
    descricao: "Corpus Institucional Vivo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "conjunto de artefatos verificáveis entregues pelo squad: (1) Grafo de Conhecimento Estruturado (Notion + vector store): taxonomia completa com nós, arestas, fontes e nível de confiança por claim"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "consultável por qualquer membro autorizado do time"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) Clone Estratégico Ativo (Persona Forge): interface /clone no Slack que responde perguntas estratégicas com a lógica do founder, com citação de fonte e nível de confiança"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Memo Engine Configurado (Scrivener): capacidade de gerar board packs e investor updates em < 4h com rastreabilidade total ao grafo"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(4) Intelligence Feed Ativo (Radar): alertas contextualizados de movimentos competitivos e de mercado conectados ao grafo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do squad. Recebe intencoes estrategicas (perguntas, pedidos de memo, alertas de sinal externo, sessoes de ingestao) e as decompoe em tarefas roteadas para os workers corretos. Ge…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic AUDITOR antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automaticamente — pausa e apresenta ao founder os dois claims com contexto (data, situacao) para ele determinar qual e a posicao atual e por que evoluiu. Irreversivel porque altera permanentemente o grafo canônico."
    - "[ ] L3: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída para fora da empresa exige leitura e aprovação explícita do founder. O clone fala pela empresa — erro de representação e irreversível reputacionalmente."
    - "[ ] L3: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com anotações de contexto por seção para facilitar a revisão, mas o envio nunca é automático."
    - "[ ] L2: Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para reunião'. O founder decide o que fazer com o sinal, não o squad."
    - "[ ] L2: Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao ha ingestao forçada — o founder controla o ritmo de captura do proprio conhecimento."
---

# Orquestrar Pipeline do Knowledge Base Institucional do Founder

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Knowledge Base Institucional do Founder |
| **status** | `pending` |
| **responsible_executor** | ORION (ORION — O Guardião do Segundo Cerebro) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do squad. Recebe intencoes estrategicas (perguntas, pedidos de memo, alertas de sinal externo, sessoes de ingestao) e as decompoe em tarefas roteadas para os workers corretos. Gerencia o estado do grafo de conhecimento, prioriza ingestao por lacunas criticas identificadas no Discovery, decide quando acionar o clone vs o Memo Engine vs o Radar, e garante que nenhum output saia sem verificacao do Auditor. Nao executa ingestao nem escrita diretamente — seu trabalho e manter a coerencia e completude do corpus institucional e garantir que o founder seja interrompido apenas para validacoes de altissimo valor (L3). Opera em modo proativo: identifica lacunas no grafo, agenda sessoes de captura e alerta sobre topicos criticos ainda nao estruturados.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Corpus Institucional Vivo
- conjunto de artefatos verificáveis entregues pelo squad: (1) Grafo de Conhecimento Estruturado (Notion + vector store): taxonomia completa com nós, arestas, fontes e nível de confiança por claim
- consultável por qualquer membro autorizado do time
- (2) Clone Estratégico Ativo (Persona Forge): interface /clone no Slack que responde perguntas estratégicas com a lógica do founder, com citação de fonte e nível de confiança
- (3) Memo Engine Configurado (Scrivener): capacidade de gerar board packs e investor updates em < 4h com rastreabilidade total ao grafo
- (4) Intelligence Feed Ativo (Radar): alertas contextualizados de movimentos competitivos e de mercado conectados ao grafo
- (5) Relatório de Cobertura Mensal: dashboard no ClickUp mostrando % de tópicos cobertos, taxa de reuso, interrupções evitadas e valor estimado de tempo do founder liberado
- Prova de trabalho: toda consulta, ingestão e memo registrado no Langfuse com trace completo e no ClickUp com artefato verificável

## Trigger

Orquestrador central do squad. Recebe intencoes estrategicas (perguntas, pedidos de memo, alertas de sinal externo, sessoes de ingestao) e as decompoe em tarefas roteadas para os workers corretos. Gerencia o estado do grafo de conhecimento, prioriza ingestao por lacunas criticas identificadas no Discovery, decide quando acionar o clone vs o Memo Engine vs o Radar, e garante que nenhum output saia sem verificacao do Auditor. Nao executa ingestao nem escrita diretamente — seu trabalho e manter a coerencia e completude do corpus institucional e garantir que o founder seja interrompido apenas para validacoes de altissimo valor (L3). Opera em modo proativo: identifica lacunas no grafo, agenda sessoes de captura e alerta sobre topicos criticos ainda nao estruturados.

## Knowledge base (o que o executor consulta)

- Notion MCP
- fonte primária de documentos, local de entrega de memos e briefings, armazenamento do grafo legível por humanos
- Slack MCP
- ingestão de threads estratégicos exportados, entrega de alertas do Radar e digest do Chief of Staff, interface /clone para consultas ao Persona Forge
- Google Calendar / Outlook MCP
- leitura de agenda pelo Chief of Staff para disparo de briefings pré-reunião e detecção de datas críticas (board, investors)
- Gmail MCP
- ingestão de emails estratégicos exportados pelo SCRIBE, monitoramento de follow-ups pelo Chief of Staff
- Sembly / Fireflies API
- ingestão automática de transcrições de reuniões gravadas para o SCRIBE
- ClickUp MCP
- registro de tarefas e artefatos como prova de trabalho verificável, gestão de follow-ups pelo Chief of Staff
- ElevenLabs API
- opcional: voz do clone para versão de áudio do Persona Forge (digital twin executivo para podcasts internos ou mensagens de voz)
- Supabase pgvector
- vector store para embeddings do grafo (nós, arestas, corpus do clone), recuperação semântica de alta performance
- LangGraph / Claude Agent SDK
- orquestração stateful dos workers, controle de paralelismo (SCRIBE + Cartographer + Radar em paralelo), retry logic e gerenciamento de estado do grafo
- observabilidade OTEL completa: tracing de cada ingestão e consulta, custo por worker, taxa de aprovação do Auditor, quality gates (dev 70% / staging 85% / prod 95% task success)
- EXA Web Search MCP
- pesquisa de sinais externos pelo Radar e contextualização de mercado pelo Wargame
- Google Drive
- fonte de documentos históricos (decks, board packs, docs estratégicos) para ingestão pelo SCRIBE

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic AUDITOR antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Corpus Institucional Vivo
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic AUDITOR registrado
- [ ] Gate L3 respeitado: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o graf…
- [ ] Gate L3 respeitado: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, m…
- [ ] Gate L3 respeitado: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scriv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automat… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída pa… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com ano… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao h… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão do mapa de lacunas gerado no Discovery: antes de priorizar quais tópicos capturar, o founder valida se a taxonomia e as lacunas identificadas fazem sen… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic AUDITOR | BLOQUEIA entrega |

## Handoff

- **to:** SCRIBE
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
