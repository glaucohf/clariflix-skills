---
task: geradorDeGoldenRecord()
responsavel: "Gerador de Golden Record"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Cluster de duplicatas aprovado para merge (pelo humano se L2, automático se L1) com regras de golden record"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Golden record consolidado no CRM com: todos os campos do master atualizados, histórico completo preservado, nota de merge com diff detalhado, e registro de auditoria imutável"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato de merge gravado no ClickUp com aprovador e timestamp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Aprovação de merge pelo humano na fila HITL; merge automático L1 após score >0.90 no Gemini; solicitação manual de merge pelo operador RevOps."
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

# Gerar Golden Record

**Task ID:** `geradorDeGoldenRecord()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Golden Record |
| **status** | `pending` |
| **responsible_executor** | Gerador de Golden Record (Midas (Gerador de Golden Record)) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Ápos deduplicação aprovada (automática L1 ou HITL L2), executa o merge definitivo: consolida campos pelo playbook de regras (mais recente, mais completo, fonte prioritária), preserva histórico de atividades de ambos os registros, transfere deals/tasks/notas para o master record, marca duplicata como 'merged' (não deleta para audit trail). Gera diff legível do que mudou.

## Input

- Cluster de duplicatas aprovado para merge (pelo humano se L2, automático se L1) com regras de golden record

## Output

- Golden record consolidado no CRM com: todos os campos do master atualizados, histórico completo preservado, nota de merge com diff detalhado, e registro de auditoria imutável
- Artefato de merge gravado no ClickUp com aprovador e timestamp

## Trigger

Aprovação de merge pelo humano na fila HITL; merge automático L1 após score >0.90 no Gemini; solicitação manual de merge pelo operador RevOps.

## Knowledge base (o que o executor consulta)

- Playbook de regras de golden record do cliente (fonte prioritária por campo, campo mais recente vs mais completo)
- Esquema de campos do CRM para saber quais campos são mergeáveis vs substituíveis
- Log de merges anteriores para auditoria

## Action Items

1. Confirmar o gatilho e carregar a entrada (Cluster de duplicatas aprovado para merge (pelo humano se L2, automático se L1) com regras de golden record).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Golden record consolidado no CRM com: todos os campos do master atualizados, histórico completo preservado, nota de mer…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Golden record consolidado no CRM com: todos os campos do master atualizados, histórico completo preservado, nota de merge com diff detalhado, e registro de aud…
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

- **to:** Sentinel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
