---
task: renato()
responsavel: "Renato"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de handoffs L3 abertos com timestamps, SLAs por urgency_level, cadeia de escalonamento humano por equipe, status de resposta em tempo real"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alertas de lembrete via Slack/email, registros de auditoria no ClickUp (quem foi notificado, quando, qual decisão tomou), relatório diário de SLA compliance (% handoffs respondidos dentro do prazo por tier de urgência)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron a cada 5 minutos para verificar handoffs abertos. Disparo imediato quando novo handoff L3 é criado. Disparo por webhook quando decisão é registrada (para fechar o ticket de monitoramento)."
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

# Monitorar Handoffs L3

**Task ID:** `renato()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Handoff Orchestrator HITL

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Handoffs L3 |
| **status** | `pending` |
| **responsible_executor** | Renato (Renato — Monitor de SLA e Escalonamento) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker determinístico que rastreia todos os handoffs L3 abertos e garante que nenhum fique sem resposta além do SLA definido por urgência. Envia lembretes progressivos (5min, 15min, 30min para críticos; 1h, 4h, 24h para normais), identifica o próximo humano na cadeia de escalonamento se o primário não respondeu, e registra todas as decisões (ou ausências de decisão) no ClickUp como prova de trabalho.

## Input

- Lista de handoffs L3 abertos com timestamps, SLAs por urgency_level, cadeia de escalonamento humano por equipe, status de resposta em tempo real

## Output

- Alertas de lembrete via Slack/email, registros de auditoria no ClickUp (quem foi notificado, quando, qual decisão tomou), relatório diário de SLA compliance (% handoffs respondidos dentro do prazo por tier de urgência)

## Trigger

Cron a cada 5 minutos para verificar handoffs abertos. Disparo imediato quando novo handoff L3 é criado. Disparo por webhook quando decisão é registrada (para fechar o ticket de monitoramento).

## Knowledge base (o que o executor consulta)

- SLAs por tipo de ação e urgência, cadeia de escalonamento humano (primário, secundário, fallback), horários de disponibilidade da equipe, histórico de tempos de resposta por responsável

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de handoffs L3 abertos com timestamps, SLAs por urgency_level, cadeia de escalonamento humano por equipe, status…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alertas de lembrete via Slack/email, registros de auditoria no ClickUp (quem foi notificado, quando, qual decisão tomou…) e persistir no artefato do squad.
4. Entregar ao critic Vitor; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alertas de lembrete via Slack/email, registros de auditoria no ClickUp (quem foi notificado, quando, qual decisão tomou), relatório diário de SLA compliance (%…
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

- **to:** Selene
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
