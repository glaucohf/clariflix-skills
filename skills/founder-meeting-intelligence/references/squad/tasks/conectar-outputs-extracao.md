---
task: vector()
responsavel: "Vector"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Structured Extraction Package do Quill + acesso ao Vector DB da KB institucional + acesso à API do ClickUp (tasks existentes) + acesso ao Notion (documentos e decisões históricas)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Enriched Extraction Package: cada decision e action_item recebe { kb_conflicts: [], kb_alignments: [], prior_meeting_refs: [], existing_clickup_task_id (se duplicata detectada), related_documents: [] }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatório de consistência: { new_decisions: N, contradictions_flagged: N, pending_items_resolved: N, duplicates_prevented: N }"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Maestro após Quill concluir extração. Processo de enriquecimento e verificação antes da validação crítica de Argos. Também ativado proativamente quando founder faz pergunta direta sobre h…"
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

# Conectar Outputs Extração

**Task ID:** `vector()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Meeting Intelligence — Decisões que Nunca se Perdem

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Conectar Outputs Extração |
| **status** | `pending` |
| **responsible_executor** | Vector (Vector — O Conector da KB) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em conectar os outputs de extração de Quill com a base de conhecimento institucional. Executa três operações: (1) VERIFICAÇÃO DE CONSISTÊNCIA — compara cada decisão extraída com decisões históricas na KB: sinaliza se contradiz algo decidido anteriormente, se está alinhada com princípios estratégicos documentados, ou se retoma tema que ficou pendente; (2) DEDUPLICAÇÃO — identifica se action items gerados já existem como tasks no ClickUp (evita duplicatas); (3) ENRIQUECIMENTO DE LINKS — adiciona links para documentos relevantes na KB, epics relacionados no ClickUp, e reuniões anteriores sobre o mesmo tema. Output alimenta Argos para validação e depois Hermes para despacho.

## Input

- Structured Extraction Package do Quill + acesso ao Vector DB da KB institucional + acesso à API do ClickUp (tasks existentes) + acesso ao Notion (documentos e decisões históricas)

## Output

- Enriched Extraction Package: cada decision e action_item recebe { kb_conflicts: [], kb_alignments: [], prior_meeting_refs: [], existing_clickup_task_id (se duplicata detectada), related_documents: [] }
- Relatório de consistência: { new_decisions: N, contradictions_flagged: N, pending_items_resolved: N, duplicates_prevented: N }

## Trigger

Ativado por Maestro após Quill concluir extração. Processo de enriquecimento e verificação antes da validação crítica de Argos. Também ativado proativamente quando founder faz pergunta direta sobre histórico de decisões — ex: '/quando decidimos sobre [tema]?'

## Knowledge base (o que o executor consulta)

- Vector DB com todas as decisões históricas indexadas semanticamente (Pinecone ou Qdrant)
- API do ClickUp com access token configurado (acesso read para verificação de duplicatas)
- Notion API para busca semântica em documentos estratégicos
- Índice de reuniões processadas pelo squad (data, participantes, temas-chave, link para sumário)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Structured Extraction Package do Quill + acesso ao Vector DB da KB institucional + acesso à API do ClickUp (tasks exist…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Enriched Extraction Package: cada decision e action_item recebe { kb_conflicts: [], kb_alignments: [], prior_meeting_re…) e persistir no artefato do squad.
4. Entregar ao critic Argos 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Enriched Extraction Package: cada decision e action_item recebe { kb_conflicts: [], kb_alignments: [], prior_meeting_refs: [], existing_clickup_task_id (se dup…
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

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
