---
task: dora()
responsavel: "Dora"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Briefing de Decisão + action classification JSON + horário atual + disponibilidade da equipe (calendário/status Slack) + regras de roteamento configuradas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Rota de entrega: {primary_recipient, channel, backup_recipient, escalation_chain[], delivery_timestamp, notification_sent: bool}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Log registrado no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Dispara imediatamente após Beatriz completar o Briefing de Decisão. Também dispara quando Renato identifica SLA expirado e precisa re-rotear para nível superior."
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

# Determinar Canal Enviado

**Task ID:** `dora()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Handoff Orchestrator HITL

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Determinar Canal Enviado |
| **status** | `pending` |
| **responsible_executor** | Dora (Dora — Roteadora de Canal e Responsável) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker operacional que determina PARA QUEM e POR QUAL CANAL o handoff L3 deve ser enviado. Aplica regras de negocio: tipo de acao define equipe responsavel, valor financeiro define nivel hierarquico, horario define canal (Slack em horario comercial, SMS/ligacao para P0 fora do horario), disponibilidade do responsavel define fallback. Garante que o briefing do Beatriz chegue na pessoa certa pelo canal certo.

## Input

- Briefing de Decisão + action classification JSON + horário atual + disponibilidade da equipe (calendário/status Slack) + regras de roteamento configuradas

## Output

- Rota de entrega: {primary_recipient, channel, backup_recipient, escalation_chain[], delivery_timestamp, notification_sent: bool}
- Log registrado no ClickUp

## Trigger

Dispara imediatamente após Beatriz completar o Briefing de Decisão. Também dispara quando Renato identifica SLA expirado e precisa re-rotear para nível superior.

## Knowledge base (o que o executor consulta)

- Organograma da equipe de operações e CS do cliente, regras de roteamento por tipo de ação e valor, calendários e status de disponibilidade, integração com Slack presence API, política de escalação fora do horário comercial

## Action Items

1. Confirmar o gatilho e carregar a entrada (Briefing de Decisão + action classification JSON + horário atual + disponibilidade da equipe (calendário/status Slack)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Rota de entrega: {primary_recipient, channel, backup_recipient, escalation_chain[], delivery_timestamp, notification_se…) e persistir no artefato do squad.
4. Entregar ao critic Vitor; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Rota de entrega: {primary_recipient, channel, backup_recipient, escalation_chain[], delivery_timestamp, notification_sent: bool}
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

- **to:** Fabio
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
