---
task: cassandra()
responsavel: "Cassandra"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Eventos de email bounce (webhook do ESP), mudanças de cargo (Clay/Apollo alerts), visitas ao site (HubSpot tracking), histórico de engajamento no CRM"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Fila de alertas classificados: { contact_id, signal_type: rotting|intent_high|intent_medium, signal_source, recommended_action, urgency: high|medium|low }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Integrado ao ClickUp como tasks com prioridade"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Registros podres marcados para HITL de exclusão"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de email bounce; agendamento diário de verificação de mudanças de cargo via API; threshold de inatividade (lead sem engajamento >180 dias)."
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

# Detectar Sinais De Intencao

**Task ID:** `cassandra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Sinais De Intencao |
| **status** | `pending` |
| **responsible_executor** | Cassandra (Cassandra (Detectora de Sinais de Intenção e Rotting)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora sinais de degradacao de dados (emails bouncing, telefones inexistentes, empresa fechada/adquirida) e sinais de intencao de compra (visita ao site, abertura de email, mudanca de cargo no LinkedIn). Gera alertas de 'registro podre' para remocao ou re-validacao. Gera alertas de 'lead quente' para priorizacao pelo squad de outreach downstream.

## Input

- Eventos de email bounce (webhook do ESP), mudanças de cargo (Clay/Apollo alerts), visitas ao site (HubSpot tracking), histórico de engajamento no CRM

## Output

- Fila de alertas classificados: { contact_id, signal_type: rotting|intent_high|intent_medium, signal_source, recommended_action, urgency: high|medium|low }
- Integrado ao ClickUp como tasks com prioridade
- Registros podres marcados para HITL de exclusão

## Trigger

Webhook de email bounce; agendamento diário de verificação de mudanças de cargo via API; threshold de inatividade (lead sem engajamento >180 dias).

## Knowledge base (o que o executor consulta)

- Regras de classificação de bounce (hard vs soft)
- Sinais de intenção definidos pelo cliente (lista de páginas de alto valor no site, sequências de abertura de email)
- Limiar de rotting por estágio do funil (SQL inativo >30 dias = alerta, MQL inativo >90 dias = alerta)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Eventos de email bounce (webhook do ESP), mudanças de cargo (Clay/Apollo alerts), visitas ao site (HubSpot tracking), h…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Fila de alertas classificados: { contact_id, signal_type: rotting|intent_high|intent_medium, signal_source, recommended…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Fila de alertas classificados: { contact_id, signal_type: rotting|intent_high|intent_medium, signal_source, recommended_action, urgency: high|medium|low }
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

- **to:** Gerador de Golden Record
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
