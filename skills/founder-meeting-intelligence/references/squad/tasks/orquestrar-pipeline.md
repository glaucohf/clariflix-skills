---
task: maestroPipeline()
responsavel: "Maestro"
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
    descricao: "Meeting Intelligence Report"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "documento estruturado gerado por reunião, salvo permanentemente na KB (Notion) e enviado ao founder via Slack"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Contém: (1) Executive Summary com 5 bullets (decisões, ações, insights chave, próximos passos, riscos identificados)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) Decision Log"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "tabela de todas as decisões formais com statement, owner, rationale, alternativas rejeitadas e link para contexto histórico na KB"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(3) Action Items com formato pronto para ClickUp (título, assignee, deadline, prioridade, contexto executável) e link para task criada"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro é o orquestrador central do squad. Recebe o intake de reunião (áudio, vídeo, transcrição ou link), executa o protocolo de classificação (tipo, participantes, contexto, prioridade), orquestra…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argos 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB — Maestro pausa o pipeline e notifica o founder com a contradição detalhada (decisão antiga vs. nova decisão). O founder confirma qual prevalece antes de Hermes atualizar a KB e criar tasks. Sem confirmação em 4h, o item fica em quarentena."
    - "[ ] HITL: ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founder com os itens em destaque para atribuição manual antes de Hermes criar as tasks. Prazo de resposta: 2h (reuniões urgentes) ou 24h (demais)."
    - "[ ] HITL: DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Proposal) — o founder deve aprovar as atualizações antes do envio. Qualquer mudança de stage ou valor estimado requer aprovação explícita via Slack (botão Aprovar/Rejeitar)."
    - "[ ] HITL: BOARD MEMO PARA ENVIO EXTERNO (L3): Hermes pode criar o draft do Board Memo no Notion automaticamente (L2), mas o envio para membros do board, investidores ou parceiros externos é sempre bloqueado até aprovação explícita do founder. Nenhum email ou comunicação sai sem revisão humana."
    - "[ ] HITL: INFORMAÇÃO SENSÍVEL FLAGUEADA (L3): Quando Argos detecta informações sensíveis na transcrição (valores de negociação, dados de saúde financeira, informações sobre demissões ou reestruturações, dados pessoais de terceiros) — o trecho é isolado e o founder decide: (a) incluir na KB com controle de acesso restrito, (b) incluir no sumário interno apenas, ou (c) excluir do registro. Sem decisão do founder, o trecho fica em quarentena."
---

# Orquestrar Pipeline do Meeting Intelligence

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Meeting Intelligence — Decisões que Nunca se Perdem

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Meeting Intelligence |
| **status** | `pending` |
| **responsible_executor** | Maestro (Maestro — O Diretor de Orquestra Institucional) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Maestro é o orquestrador central do squad. Recebe o intake de reunião (áudio, vídeo, transcrição ou link), executa o protocolo de classificação (tipo, participantes, contexto, prioridade), orquestra os agentes workers em sequência otimizada — Vox para transcrição, Pulse para enriquecimento contextual, Quill para extração multi-dimensional, Vector para conexão com KB, Argos para validação crítica, e Hermes para despacho das ações. Monitora qualidade em cada etapa: se cobertura de action items com owner+deadline < 90%, devolve para Quill antes de prosseguir. Responsável pelo Meeting Intelligence Report final e pelo SLA de processamento (< 10 min para reuniões de até 60 min). Mantém o Memory Layer do squad atualizado com padrões de comprometimento e histórico de decisões por tema.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Meeting Intelligence Report
- documento estruturado gerado por reunião, salvo permanentemente na KB (Notion) e enviado ao founder via Slack
- Contém: (1) Executive Summary com 5 bullets (decisões, ações, insights chave, próximos passos, riscos identificados)
- (2) Decision Log
- tabela de todas as decisões formais com statement, owner, rationale, alternativas rejeitadas e link para contexto histórico na KB
- (3) Action Items com formato pronto para ClickUp (título, assignee, deadline, prioridade, contexto executável) e link para task criada
- (4) Strategic Insights
- Knowledge Snippets para alimentar KB institucional com frameworks, hipóteses e conhecimento tácito extraído
- (5) Consistency Report
- lista de alinhamentos e contradições com decisões históricas
- (6) Audit Trail completo (quais agentes processaram, timestamps, custo de tokens, versão do report)
- (7) Link permanente para transcrição original
- Para reuniões classificadas como 'board' ou 'estratégica nível 1': Board Memo Draft adicional (executive one-pager para compartilhamento com stakeholders após aprovação do founder)
- Toda ação executada por Hermes é rastreada com ID de task no ClickUp como prova de trabalho auditável

## Trigger

Maestro é o orquestrador central do squad. Recebe o intake de reunião (áudio, vídeo, transcrição ou link), executa o protocolo de classificação (tipo, participantes, contexto, prioridade), orquestra os agentes workers em sequência otimizada — Vox para transcrição, Pulse para enriquecimento contextual, Quill para extração multi-dimensional, Vector para conexão com KB, Argos para validação crítica, e Hermes para despacho das ações. Monitora qualidade em cada etapa: se cobertura de action items com owner+deadline < 90%, devolve para Quill antes de prosseguir. Responsável pelo Meeting Intelligence Report final e pelo SLA de processamento (< 10 min para reuniões de até 60 min). Mantém o Memory Layer do squad atualizado com padrões de comprometimento e histórico de decisões por tema.

## Knowledge base (o que o executor consulta)

- Google Meet / Zoom / Microsoft Teams (captura de gravações automática via webhooks ou API
- intake direto de reuniões gravadas)
- Google Calendar / Outlook Calendar (enriquecimento de metadados
- participantes, recorrência, tipo de reunião
- trigger automático por evento de calendário com gravação)
- ClickUp (criação de tasks com owner, deadline, prioridade e contexto
- core output do squad
- leitura de tasks existentes para deduplicação e follow-up)
- Notion (KB institucional
- armazenamento permanente de Decision Records, Knowledge Snippets e Meeting Intelligence Reports
- busca semântica via Vector DB)
- Slack (intake de reuniões via upload/link no canal #meetings-intel + entrega de sumários + notificações de action items + alertas de deadline + confirmações HITL)
- HubSpot (atualização de deals e contatos quando reunião envolve cliente/prospect
- next steps, mudança de stage, notas de reunião)
- Claude Agent SDK + LangGraph (orquestração stateful do pipeline multi-agente
- gerencia sequência Vox→Pulse→Quill→Vector→Argos→Hermes e estado da sessão por reunião)
- Langfuse (observabilidade OTEL
- tracing completo por reunião, custo por agente/token, eval de qualidade de extração, dashboard de KPIs do squad)
- Whisper API / AssemblyAI (transcrição de áudio com diarização de alta qualidade
- Vox usa como motor de transcrição com fallback entre providers)
- Vector DB
- Pinecone ou Qdrant (armazenamento e busca semântica de decisões históricas, sumários e conhecimento tácito do founder)
- Gmail / Email SMTP (notificações de action items para participantes externos
- envio de Meeting Intelligence Report para stakeholders aprovados)
- MCP Servers (camada de integração universal
- ClickUp MCP, Notion MCP, Slack MCP, Google Calendar MCP expostos como tools para os agents)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argos 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Meeting Intelligence Report
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argos 2 registrado
- [ ] Gate HITL respeitado: CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB…
- [ ] Gate HITL respeitado: ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founde…
- [ ] Gate HITL respeitado: DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Propo…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB — Maestro pausa o pi… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founder com os itens em de… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Proposal) — o founder dev… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — BOARD MEMO PARA ENVIO EXTERNO (L3): Hermes pode criar o draft do Board Memo no Notion automaticamente (L2), mas o envio para membros do board, investidores ou… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — INFORMAÇÃO SENSÍVEL FLAGUEADA (L3): Quando Argos detecta informações sensíveis na transcrição (valores de negociação, dados de saúde financeira, informações so… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — OVERDUE CRÍTICO COM ESCALADA (L2→HITL): Quando Echo identifica action item de reunião estratégica com mais de 7 dias de atraso e o assignee não respondeu a lem… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — CUSTO DE PROCESSAMENTO ACIMA DE THRESHOLD (L3): Se estimativa de custo de tokens de uma reunião longa (> 3h) superar limite configurado (default: U$2 por reuni… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Argos 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
