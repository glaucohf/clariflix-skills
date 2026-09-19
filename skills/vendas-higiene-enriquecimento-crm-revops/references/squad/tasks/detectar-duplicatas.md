---
task: detectorDeDuplicatas()
responsavel: "Detector de Duplicatas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Registro novo validado por Argos + slice da base CRM (5000 registros mais recentes ou segmento por empresa/dominío)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lista de clusters: [ { master_id, duplicate_ids[], confidence, merge_fields: { field, master_value, duplicate_value, recommended } } ]"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Duplicatas L1 marcadas para merge automático"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Duplicatas L2 enviadas para HITL queue"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Apos Argos validar novo registro; varredura agendada semanal (domingo 02h) em toda a base."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)"
    - "[ ] HITL: Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)"
    - "[ ] HITL: Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)"
    - "[ ] HITL: Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal)"
    - "[ ] HITL: Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente)"
---

# Detectar Duplicatas

**Task ID:** `detectorDeDuplicatas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Duplicatas |
| **status** | `pending` |
| **responsible_executor** | Detector de Duplicatas (Gemini (Detector de Duplicatas)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Roda fuzzy matching em novos registros contra base existente. Usa algoritmo multi-campo: email (exato, peso 0.5) + nome normalizado (Levenshtein, peso 0.25) + telefone normalizado (peso 0.15) + CNPJ (exato, peso 0.10). Gera clusters de duplicatas com score de confianca. Score >0.90 = merge automatico (L1). Score 0.75-0.89 = propoe merge com justificativa (L2). Score <0.75 = ignora.

## Input

- Registro novo validado por Argos + slice da base CRM (5000 registros mais recentes ou segmento por empresa/dominío)

## Output

- Lista de clusters: [ { master_id, duplicate_ids[], confidence, merge_fields: { field, master_value, duplicate_value, recommended } } ]
- Duplicatas L1 marcadas para merge automático
- Duplicatas L2 enviadas para HITL queue

## Trigger

Apos Argos validar novo registro; varredura agendada semanal (domingo 02h) em toda a base.

## Knowledge base (o que o executor consulta)

- Algoritmos de fuzzy matching (Levenshtein, Jaro-Winkler)
- Regras de golden record do cliente (qual fonte tem prioridade por campo)
- Histórico de merges anteriores para aprendizado de falsos positivos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Registro novo validado por Argos + slice da base CRM (5000 registros mais recentes ou segmento por empresa/dominío)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lista de clusters: [ { master_id, duplicate_ids[], confidence, merge_fields: { field, master_value, duplicate_value, re…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lista de clusters: [ { master_id, duplicate_ids[], confidence, merge_fields: { field, master_value, duplicate_value, recommended } } ]
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)
- [ ] Gate HITL respeitado: Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)
- [ ] Gate HITL respeitado: Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez) | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de integração de nova fonte de dados ao pipeline (ex: adicionar novo formulário ou importação de lista de parceiro) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Enriquecedor de Conta e Lead
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
