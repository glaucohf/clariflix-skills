---
task: workerDeNotificacaoEAceite()
responsavel: "Worker de Notificação e Aceite"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Decisão de roteamento do Maestro: {lead_id, vendedor_designado, justificativa_roteamento, card_lead, mensagem_apresentação_sugerida, sla_aceite_minutos}"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Confirmação de entrega: {notificacao_vendedor_enviada: bool, timestamp_notificacao, aceite_recebido: bool, timestamp_aceite, mensagem_apresentação_enviada_ao_lead: bool, re_roteamento_necessário: bool}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro imediatamente após decisão de roteamento; também acionado pelo timer de SLA para re-roteamento"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Veredito 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro deploy; em produção, amostras aleatórias (10%) passam por revisão humana"
    - "[ ] L3: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratamento especial"
    - "[ ] L3: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente"
    - "[ ] L3: Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interface de configuração, com log de auditoria"
    - "[ ] L3: Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor designado"
---

# Notificar Vendedor Lead

**Task ID:** `workerDeNotificacaoEAceite()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Notificar Vendedor Lead |
| **status** | `pending` |
| **responsible_executor** | Worker de Notificação e Aceite (Hermes (Worker de Notificação e Aceite)) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa a atribuicao decidida pelo Maestro: notifica o vendedor designado via WhatsApp e/ou Slack com o card do lead (nome, empresa, score, resumo do dossie, link direto no CRM), registra o roteamento no CRM, inicia timer de SLA de aceite (padrao: 3 minutos). Se SLA vencer sem aceite, sinaliza ao Maestro para re-roteamento. Se aceito, atualiza status no CRM e notifica o lead com mensagem de apresentacao personalizada do vendedor.

## Input

- Decisão de roteamento do Maestro: {lead_id, vendedor_designado, justificativa_roteamento, card_lead, mensagem_apresentação_sugerida, sla_aceite_minutos}

## Output

- Confirmação de entrega: {notificacao_vendedor_enviada: bool, timestamp_notificacao, aceite_recebido: bool, timestamp_aceite, mensagem_apresentação_enviada_ao_lead: bool, re_roteamento_necessário: bool}

## Trigger

Acionado pelo Maestro imediatamente após decisão de roteamento; também acionado pelo timer de SLA para re-roteamento

## Knowledge base (o que o executor consulta)

- Templates de card de lead por tier (HOT/WARM/COLD), templates de mensagem de apresentação por especialidade/segmento, configurações de SLA por tier (HOT=2min, WARM=5min, COLD=30min), canais preferidos por vendedor (WhatsApp vs Slack vs email)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Decisão de roteamento do Maestro: {lead_id, vendedor_designado, justificativa_roteamento, card_lead, mensagem_apresenta…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Confirmação de entrega: {notificacao_vendedor_enviada: bool, timestamp_notificacao, aceite_recebido: bool, timestamp_ac…) e persistir no artefato do squad.
4. Entregar ao critic Veredito 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Confirmação de entrega: {notificacao_vendedor_enviada: bool, timestamp_notificacao, aceite_recebido: bool, timestamp_aceite, mensagem_apresentação_enviada_ao_l…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Veredito 2 registrado
- [ ] Gate L3 respeitado: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização an…
- [ ] Gate L3 respeitado: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurtu…
- [ ] Gate L3 respeitado: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro depl… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratame… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interfac… | BLOQUEIA até decisão humana |
| VETO-005 | L3 — Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor desi… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão humana semanal do relatório de auditoria do Veredito para identificar vieses sistemáticos e calibrar o modelo de scoring | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Veredito 2 | BLOQUEIA entrega |

## Handoff

- **to:** Worker de Higiene de CRM
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
