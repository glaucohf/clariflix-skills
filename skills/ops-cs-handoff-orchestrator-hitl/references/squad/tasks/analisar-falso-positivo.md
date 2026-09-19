---
task: selene()
responsavel: "Selene"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Log completo de decisões dos últimos 7/30/90 dias (action_id, tier_atribuído, decisão_humana, tempo_de_resposta, outcome_pos_decisão), feedback de incidentes, NPS correlacionado com tipo de ação"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio de Deriva da Matriz: {actions_to_downgrade[], actions_to_upgrade[], confidence_per_change, evidence_samples[], estimated_impact_on_handoff_volume, proposed_matrix_delta}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Salvo no ClickUp como task com checklist de aprovacao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron semanal (domingo 22h). Disparo imediato quando taxa de falso-positivo ultrapassa 15% em qualquer categoria no período de 48h. Disparo manual via comando do supervisor CS."
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

# Analisar Falso Positivo

**Task ID:** `selene()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Handoff Orchestrator HITL

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Falso Positivo |
| **status** | `pending` |
| **responsible_executor** | Selene (Selêne — Analista de Padrão de Falso Positivo) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker analítico que roda semanalmente (ou on-demand) para detectar deriva na matriz de classificação: identifica ações que foram escaladas para L3 mas o humano sempre aprova sem modificação (candidatos a L2), e ações que rodaram em L2 mas geraram reclamações ou rollbacks (candidatos a L3). Gera proposta de recalibração da matriz com evidências estatísticas para revisão do Critic Vítor e aprovação humana.

## Input

- Log completo de decisões dos últimos 7/30/90 dias (action_id, tier_atribuído, decisão_humana, tempo_de_resposta, outcome_pos_decisão), feedback de incidentes, NPS correlacionado com tipo de ação

## Output

- Relatorio de Deriva da Matriz: {actions_to_downgrade[], actions_to_upgrade[], confidence_per_change, evidence_samples[], estimated_impact_on_handoff_volume, proposed_matrix_delta}
- Salvo no ClickUp como task com checklist de aprovacao

## Trigger

Cron semanal (domingo 22h). Disparo imediato quando taxa de falso-positivo ultrapassa 15% em qualquer categoria no período de 48h. Disparo manual via comando do supervisor CS.

## Knowledge base (o que o executor consulta)

- Histórico completo de classificações e outcomes, benchmarks de taxa aceitável por tipo de ação, políticas de negócio que não podem ser relaxadas (compliance hard-rules), feedback qualitativo dos humanos que recebem handoffs

## Action Items

1. Confirmar o gatilho e carregar a entrada (Log completo de decisões dos últimos 7/30/90 dias (action_id, tier_atribuído, decisão_humana, tempo_de_resposta, outcom…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio de Deriva da Matriz: {actions_to_downgrade[], actions_to_upgrade[], confidence_per_change, evidence_samples[]…) e persistir no artefato do squad.
4. Entregar ao critic Vitor; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio de Deriva da Matriz: {actions_to_downgrade[], actions_to_upgrade[], confidence_per_change, evidence_samples[], estimated_impact_on_handoff_volume, pr…
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

- **to:** Dora
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
