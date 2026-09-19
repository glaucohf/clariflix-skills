---
task: beatriz()
responsavel: "Beatriz"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "action_id + classification JSON do Cassio + histórico completo da interação + dados do cliente (CRM, ClickUp, plataforma CS) + políticas relevantes"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Briefing de Decisão estruturado: {summary_2_lines, client_context, action_requested, options_with_impact[], agent_recommendation, urgency_level, sla_deadline, approval_link, rejection_link, escalation_link}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Entregue via Slack (canal #hitl-approvals), email ou interface do helpdesk"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Dispara imediatamente apos Cassio classificar acao como L3. Tambem dispara em re-escalonamentos quando o primeiro humano nao respondeu dentro do SLA."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vitor antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de qualquer execução, sem exceção."
    - "[ ] HITL: L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cláusula contratual, bloqueio/banimento de usuário."
    - "[ ] HITL: L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que mencione termos legais ou rescisão."
    - "[ ] HITL: L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, respostas à imprensa."
    - "[ ] HITL: Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operações."
---

# Empacotar Contexto

**Task ID:** `beatriz()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Handoff Orchestrator HITL

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Empacotar Contexto |
| **status** | `pending` |
| **responsible_executor** | Beatriz (Beatriz — Empacotadora de Contexto) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em preparar o pacote de contexto que o humano recebe quando uma ação é classificada L3. Seu trabalho é garantir que o humano consiga decidir em menos de 30 segundos sem precisar abrir nenhum outro sistema. Gera o Briefing de Decisão: resumo da situação, histórico relevante do cliente, opções disponíveis com pros/contras, recomendação do agente, impacto de cada opção, e botões de ação direta (Aprovar / Rejeitar / Modificar).

## Input

- action_id + classification JSON do Cassio + histórico completo da interação + dados do cliente (CRM, ClickUp, plataforma CS) + políticas relevantes

## Output

- Briefing de Decisão estruturado: {summary_2_lines, client_context, action_requested, options_with_impact[], agent_recommendation, urgency_level, sla_deadline, approval_link, rejection_link, escalation_link}
- Entregue via Slack (canal #hitl-approvals), email ou interface do helpdesk

## Trigger

Dispara imediatamente apos Cassio classificar acao como L3. Tambem dispara em re-escalonamentos quando o primeiro humano nao respondeu dentro do SLA.

## Knowledge base (o que o executor consulta)

- Templates de briefing por tipo de ação (reembolso, cancelamento, alteração contratual, acesso a dados, crédito), histórico de decisões anteriores similares, perfil completo do cliente (LTV, ticket médio, NPS, número de reclamações abertas, status de saúde CS), políticas e limites de negociação

## Action Items

1. Confirmar o gatilho e carregar a entrada (action_id + classification JSON do Cassio + histórico completo da interação + dados do cliente (CRM, ClickUp, plataform…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Briefing de Decisão estruturado: {summary_2_lines, client_context, action_requested, options_with_impact[], agent_recom…) e persistir no artefato do squad.
4. Entregar ao critic Vitor; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Briefing de Decisão estruturado: {summary_2_lines, client_context, action_requested, options_with_impact[], agent_recommendation, urgency_level, sla_deadline,…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vitor registrado
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — hum…
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assin…
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qual…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cl… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, r… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operaçõe… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão humana quinzenal do Relatório de Auditoria do Vitor: supervisor CS assina o score de qualidade e valida as correções propostas. | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Gate humano na primeira semana pos-implantacao: humano revisa 100% das classificacoes (nao apenas L3) para construir confianca na matriz antes de operar em mod… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Vitor | BLOQUEIA entrega |

## Handoff

- **to:** Renato
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
