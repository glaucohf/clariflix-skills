---
task: quill()
responsavel: "Quill"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição enriquecida do Pulse + contexto de tipo de reunião (estratégica/operacional/comercial/board/1:1) + regras de extração configuradas (ex: reuniões de board requerem extração mais formal) + templates de Decision Record e Task Card do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Structured Extraction Package: { decisions: [{ id, statement, owner, rationale, alternatives_rejected, confidence_level, timestamp_ref, speaker_ref }], action_items: [{ id, task_title, assignee, deadline, priority, context_brief, dependencies, clickup_project_ref }], strategic_insights: [{ category, insight, source_quote, timestamp_ref, relevance_score }], tacit_knowledge: [{ framework_name, application_context, founder_quote, timestamp_ref }] }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Completeness score por dimensão (0-100%)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Maestro após Pulse entregar contexto enriquecido. Executa extração em paralelo nas 4 dimensões para otimizar tempo. Reprocessado pelo Maestro se Argos retornar action items sem owner/dead…"
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

# Extrair Decisões

**Task ID:** `quill()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Meeting Intelligence — Decisões que Nunca se Perdem

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Extrair Decisões |
| **status** | `pending` |
| **responsible_executor** | Quill (Quill — O Extrator Estruturado) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de extração multi-dimensional: o coração analítico do squad. Processa a transcrição enriquecida e extrai em paralelo quatro dimensões críticas. (1) DECISÕES: o que foi formalmente decidido, quem decidiu, qual era a alternativa descartada e qual foi a justificativa — formato Decision Record. (2) ACTION ITEMS: quem se comprometeu a fazer o quê, até quando, com qual nível de prioridade e quais dependências — formato Task Card compatível com ClickUp. (3) CONTEXTO ESTRATÉGICO: insights de mercado, riscos mencionados, oportunidades identificadas, benchmarks citados, hipóteses levantadas — formato Knowledge Snippet para KB. (4) CONHECIMENTO TÁCITO: frameworks que o founder usou, princípios que guiaram decisões, analogias e heurísticas mencionadas — matéria-prima para o Founder Clone Agent de outros squads.

## Input

- Transcrição enriquecida do Pulse + contexto de tipo de reunião (estratégica/operacional/comercial/board/1:1) + regras de extração configuradas (ex: reuniões de board requerem extração mais formal) + templates de Decision Record e Task Card do cliente

## Output

- Structured Extraction Package: { decisions: [{ id, statement, owner, rationale, alternatives_rejected, confidence_level, timestamp_ref, speaker_ref }], action_items: [{ id, task_title, assignee, deadline, priority, context_brief, dependencies, clickup_project_ref }], strategic_insights: [{ category, insight, source_quote, timestamp_ref, relevance_score }], tacit_knowledge: [{ framework_name, application_context, founder_quote, timestamp_ref }] }
- Completeness score por dimensão (0-100%)

## Trigger

Ativado por Maestro após Pulse entregar contexto enriquecido. Executa extração em paralelo nas 4 dimensões para otimizar tempo. Reprocessado pelo Maestro se Argos retornar action items sem owner/deadline ou decisões sem contexto suficiente.

## Knowledge base (o que o executor consulta)

- Templates de Decision Record e Task Card configurados para o cliente
- Regras de classificação de prioridade (ex: o que é urgente vs
- importante para aquele cliente)
- Glossário de termos e projetos internos do cliente para mapear referências ambíguas corretamente
- Exemplos de extrações anteriores aprovadas pelo founder (few-shot learning para calibrar o padrão de qualidade)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcrição enriquecida do Pulse + contexto de tipo de reunião (estratégica/operacional/comercial/board/1:1) + regras d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Structured Extraction Package: { decisions: [{ id, statement, owner, rationale, alternatives_rejected, confidence_level…) e persistir no artefato do squad.
4. Entregar ao critic Argos 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Structured Extraction Package: { decisions: [{ id, statement, owner, rationale, alternatives_rejected, confidence_level, timestamp_ref, speaker_ref }], action_…
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

- **to:** Vector
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
