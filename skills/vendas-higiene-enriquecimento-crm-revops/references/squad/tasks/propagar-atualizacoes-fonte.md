---
task: sincronizadorDeFontes()
responsavel: "Sincronizador de Fontes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de atualização de registro no CRM (webhook) com delta de campos alterados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Log de sincronizacao: { contact_id, sync_targets: [ { system, field, old_value, new_value, status: synced|failed|skipped, timestamp } ] }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alertas de falha enviados ao Slack do time de RevOps"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de update no CRM (campo crítico alterado); agendamento diário 06h para sync incremental; trigger manual por operador RevOps."
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

# Propagar Atualizações Fonte

**Task ID:** `sincronizadorDeFontes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Propagar Atualizações Fonte |
| **status** | `pending` |
| **responsible_executor** | Sincronizador de Fontes (Hermes (Sincronizador de Fontes)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mantem consistencia entre CRM (source of truth) e ferramentas downstream: plataforma de email (ActiveCampaign/Mailchimp), WhatsApp (API Business), ClickUp (tasks de follow-up), e planilhas de SDR. Detecta divergencias por campo (ex: telefone atualizado no CRM mas nao na plataforma de WhatsApp) e propaga atualizacoes. Registra log de sync com timestamp e delta.

## Input

- Evento de atualização de registro no CRM (webhook) com delta de campos alterados

## Output

- Log de sincronizacao: { contact_id, sync_targets: [ { system, field, old_value, new_value, status: synced|failed|skipped, timestamp } ] }
- Alertas de falha enviados ao Slack do time de RevOps

## Trigger

Webhook de update no CRM (campo crítico alterado); agendamento diário 06h para sync incremental; trigger manual por operador RevOps.

## Knowledge base (o que o executor consulta)

- Mapa de integração: CRM → sistemas downstream com campo-a-campo mapping
- Credenciais de API de cada sistema
- Regras de sync (bidirecional vs unidirecional por sistema)
- Lista de campos críticos que exigem sync imediato vs batch

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de atualização de registro no CRM (webhook) com delta de campos alterados).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Log de sincronizacao: { contact_id, sync_targets: [ { system, field, old_value, new_value, status: synced|failed|skippe…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Log de sincronizacao: { contact_id, sync_targets: [ { system, field, old_value, new_value, status: synced|failed|skipped, timestamp } ] }
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

- **to:** Pythia
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
