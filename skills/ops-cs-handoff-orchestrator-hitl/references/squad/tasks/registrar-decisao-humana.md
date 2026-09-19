---
task: fabio()
responsavel: "Fabio"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Decisão do humano (aprovado/rejeitado/modificado) + action_id + responsável + timestamp + modificações feitas se houver"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Registro estruturado de feedback: {action_id, decision, decision_maker, time_to_decide_min, feedback_classification_correct, feedback_reason, modification_details}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Armazenado no Supabase/Postgres"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Resumo semanal enviado para Selene"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook disparado pelo sistema de aprovação (Slack workflow, Zendesk trigger, ou interface customizada) imediatamente após decisão ser registrada."
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

# Registrar Decisão Humana

**Task ID:** `fabio()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Handoff Orchestrator HITL

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Registrar Decisão Humana |
| **status** | `pending` |
| **responsible_executor** | Fabio (Fábio — Agente de Feedback Loop) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker pos-decisão que fecha o ciclo de aprendizado. Após toda decisão humana em handoff L3, Fábio registra a decisão com contexto completo, solicita micro-feedback do responsável (30 segundos: 'Esta classificação estava correta? sim/não/parcialmente'), e alimenta o banco de dados de treinamento da matriz. Para decisões de 'não' ou 'parcialmente', coleta o motivo estruturado. Esses dados são a fonte primária para a recalibração do Selene.

## Input

- Decisão do humano (aprovado/rejeitado/modificado) + action_id + responsável + timestamp + modificações feitas se houver

## Output

- Registro estruturado de feedback: {action_id, decision, decision_maker, time_to_decide_min, feedback_classification_correct, feedback_reason, modification_details}
- Armazenado no Supabase/Postgres
- Resumo semanal enviado para Selene

## Trigger

Webhook disparado pelo sistema de aprovação (Slack workflow, Zendesk trigger, ou interface customizada) imediatamente após decisão ser registrada.

## Knowledge base (o que o executor consulta)

- Formulários de micro-feedback por tipo de ação, banco histórico de feedbacks anteriores, integração com Supabase para escrita de logs, templates de mensagem de solicitação de feedback por canal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Decisão do humano (aprovado/rejeitado/modificado) + action_id + responsável + timestamp + modificações feitas se houver).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Registro estruturado de feedback: {action_id, decision, decision_maker, time_to_decide_min, feedback_classification_cor…) e persistir no artefato do squad.
4. Entregar ao critic Vitor; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Registro estruturado de feedback: {action_id, decision, decision_maker, time_to_decide_min, feedback_classification_correct, feedback_reason, modification_deta…
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

- **to:** Vitor
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
