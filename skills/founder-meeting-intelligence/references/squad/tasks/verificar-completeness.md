---
task: argos()
responsavel: "Argos"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Enriched Extraction Package do Vector + transcrição original do Vox (para verificação de cobertura) + thresholds de qualidade configurados (ex: 100% de action items com owner+deadline para reuniões estratégicas) + lista de participantes e seus níveis de acesso (para controle de privacidade)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Validation Report: { completeness_score (0-100), missing_owners: [], missing_deadlines: [], ambiguous_decisions: [], potential_implicit_actions: [], privacy_flags: [], historical_contradictions_unresolved: [], verdict: 'GO' | 'NO-GO' | 'GO_WITH_WARNINGS' }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Se NO-GO: lista específica do que precisa ser reprocessado por Quill ou revisado pelo founder (HITL)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Se GO_WITH_WARNINGS: Hermes pode prosseguir mas warnings são incluídos no Meeting Intelligence Report para revisão posterior"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente por Maestro após Vector concluir enriquecimento. Gate obrigatório antes de Hermes. Se retornar NO-GO, Maestro devolve para Quill com instruções específicas de correção (máximo…"
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

# Verificar Completeness

**Task ID:** `argos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Meeting Intelligence — Decisões que Nunca se Perdem

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Completeness |
| **status** | `pending` |
| **responsible_executor** | Argos (Argos — O Crítico de Completude) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente critic/verifier responsável por validar a qualidade da extração antes de qualquer ação ser despachada por Hermes. Executa verificação em 5 dimensões: (1) COMPLETUDE DE ACTION ITEMS — todo action item tem owner nomeado, deadline explícito e contexto suficiente para execução sem perguntas adicionais; (2) CLAREZA DE DECISÕES — toda decisão tem statement inequívoco (não ambíguo), owner claro e justificativa mínima registrada; (3) CONSISTÊNCIA HISTÓRICA — contradições sinalizadas por Vector foram resolvidas (o founder foi notificado e confirmou a nova decisão substitui a anterior); (4) COBERTURA — Argos usa a transcrição original para verificar se há action items implícitos que Quill não capturou ('alguém que ficou de fazer algo' mencionado mas sem extração formal); (5) PRIVACIDADE — verifica se há informações sensíveis (dados financeiros, informações pessoais, conteúdo confidencial de negociações) que requerem controle de acesso antes de chegar à KB ou notificações. Devolve para Quill se completude < 85%.

## Input

- Enriched Extraction Package do Vector + transcrição original do Vox (para verificação de cobertura) + thresholds de qualidade configurados (ex: 100% de action items com owner+deadline para reuniões estratégicas) + lista de participantes e seus níveis de acesso (para controle de privacidade)

## Output

- Validation Report: { completeness_score (0-100), missing_owners: [], missing_deadlines: [], ambiguous_decisions: [], potential_implicit_actions: [], privacy_flags: [], historical_contradictions_unresolved: [], verdict: 'GO' | 'NO-GO' | 'GO_WITH_WARNINGS' }
- Se NO-GO: lista específica do que precisa ser reprocessado por Quill ou revisado pelo founder (HITL)
- Se GO_WITH_WARNINGS: Hermes pode prosseguir mas warnings são incluídos no Meeting Intelligence Report para revisão posterior

## Trigger

Ativado automaticamente por Maestro após Vector concluir enriquecimento. Gate obrigatório antes de Hermes. Se retornar NO-GO, Maestro devolve para Quill com instruções específicas de correção (máximo 2 reprocessamentos antes de escalar para HITL). Se GO ou GO_WITH_WARNINGS, libera Hermes para execução.

## Knowledge base (o que o executor consulta)

- Transcrição original da sessão para verificação de cobertura
- Regras de qualidade configuradas por tipo de reunião
- Lista de participantes e permissões de acesso à KB (quem pode ver o quê)
- Padrões de action items implícitos comuns (heurísticas treinadas em reuniões anteriores do cliente)
- Thresholds de privacidade e dados sensíveis do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Enriched Extraction Package do Vector + transcrição original do Vox (para verificação de cobertura) + thresholds de qua…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Validation Report: { completeness_score (0-100), missing_owners: [], missing_deadlines: [], ambiguous_decisions: [], po…) e persistir no artefato do squad.
4. Entregar ao critic Argos 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Validation Report: { completeness_score (0-100), missing_owners: [], missing_deadlines: [], ambiguous_decisions: [], potential_implicit_actions: [], privacy_fl…
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

- **to:** Argos 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
