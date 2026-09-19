---
task: enriquecedorDeContaELead()
responsavel: "Enriquecedor de Conta e Lead"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Registro CRM com mapa de campos nulos ou desatualizados (>90 dias sem update)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Lista de campos prioritários definida no onboarding"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Patch de enriquecimento: { contact_id, enriched_fields: [ { field, old_value, new_value, source, confidence, timestamp } ] }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Gravado no CRM como nota de atividade + artefato no ClickUp"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Custo de API estimado por registro incluído no log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Apos Geminî processar registro (novos lêads); mudançâ de estagio do deal (MQL → SQL dispara re-enriquecimento); varredurâ mensal de registros sem enriquecimento nos últimos 60 dias."
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

# Consultar Fontes Confiança

**Task ID:** `enriquecedorDeContaELead()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Consultar Fontes Confiança |
| **status** | `pending` |
| **responsible_executor** | Enriquecedor de Conta e Lead (Atlas (Enriquecedor de Conta e Lead)) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Para cada registro com campos criticos nulos (cargo, empresa, setor, tamanho, LinkedIn URL, telefone, receita estimada, tecnologias usadas), consulta APIs de enriquecimento em cascata: Apollo (contatos B2B) → Clay (waterfall de multiplas fontes) → Clearbit (dados de empresa). Prioriza campo mais recente com maior confidence. Nao sobrescreve campos ja preenchidos manualmente pelo humano (campo tem flag 'human_edited = true').

## Input

- Registro CRM com mapa de campos nulos ou desatualizados (>90 dias sem update)
- Lista de campos prioritários definida no onboarding

## Output

- Patch de enriquecimento: { contact_id, enriched_fields: [ { field, old_value, new_value, source, confidence, timestamp } ] }
- Gravado no CRM como nota de atividade + artefato no ClickUp
- Custo de API estimado por registro incluído no log

## Trigger

Apos Geminî processar registro (novos lêads); mudançâ de estagio do deal (MQL → SQL dispara re-enriquecimento); varredurâ mensal de registros sem enriquecimento nos últimos 60 dias.

## Knowledge base (o que o executor consulta)

- Credenciais e limites de rate das APIs (Apollo, Clay, Clearbit)
- Mapa de campos CRM → campos API (schema de tradução)
- ICP do cliente (setores, cargos, tamanhos de empresa alvo) para priorizar enriquecimento
- Custo por lookup por provedor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Registro CRM com mapa de campos nulos ou desatualizados (>90 dias sem update)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Patch de enriquecimento: { contact_id, enriched_fields: [ { field, old_value, new_value, source, confidence, timestamp…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Patch de enriquecimento: { contact_id, enriched_fields: [ { field, old_value, new_value, source, confidence, timestamp } ] }
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

- **to:** Sincronizador de Fontes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
