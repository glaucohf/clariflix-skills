---
task: lumen()
responsavel: "Lumen"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pacote_de_conta do Vault + intenção classificada + sentimento e urgência do Radar + SLA atual do ticket (tempo aberto vs"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "SLA contratado) + histórico de resolução de intenções similares"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "0-2 sugestões de próximo passo com: {tipo_acão (internal_ticket | retenção_offer | upsell_hint | sla_alert | escalate_csm | kb_gap), descrição_curta, justificativa_em_1_frase, urgência (info | warning | alert)}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Exibidas no overlay como cards secundários abaixo da sugestão de resposta"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado após Scribe concluir a sugestão de resposta; executa em paralelo ao Critic para não adicionar latência ao caminho crítico"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Prism antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar conscientemente ou corrigir"
    - "[ ] HITL: Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — responda manualmente'"
    - "[ ] HITL: Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico"
    - "[ ] HITL: Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromisso"
    - "[ ] HITL: Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente"
---

# Sugerir Próximo Passo

**Task ID:** `lumen()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sugerir Próximo Passo |
| **status** | `pending` |
| **responsible_executor** | Lumen (Lumen — Agente de Sugestão de Próximo Passo) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Além de sugerir a resposta, Lumen analisa o contexto da conta e da conversa para recomendar a ação além da resposta textual: sugerir abertura de ticket interno de engenharia, recomendar oferta de retenção proativa, propor upsell contextual (cliente perguntou sobre feature que existe no plano superior), alertar que o SLA do ticket está em risco de vencer, ou recomendar que o atendente escalone para o CSM responsável. Funciona como um 'coach' silencioso que ve o que o atendente pode estar perdendo.

## Input

- Pacote_de_conta do Vault + intenção classificada + sentimento e urgência do Radar + SLA atual do ticket (tempo aberto vs
- SLA contratado) + histórico de resolução de intenções similares

## Output

- 0-2 sugestões de próximo passo com: {tipo_acão (internal_ticket | retenção_offer | upsell_hint | sla_alert | escalate_csm | kb_gap), descrição_curta, justificativa_em_1_frase, urgência (info | warning | alert)}
- Exibidas no overlay como cards secundários abaixo da sugestão de resposta

## Trigger

Disparado após Scribe concluir a sugestão de resposta; executa em paralelo ao Critic para não adicionar latência ao caminho crítico

## Knowledge base (o que o executor consulta)

- SLA por tier de cliente e tipo de ticket, playbooks de retenção (quando oferecer e qual oferta por perfil de risco), catálogo de features por plano (para identificar oportunidades de upsell), histórico de resolução por intenção (benchmark de tempo e ações típicas), alertas de health score do ChurnZero/Gainsight

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pacote_de_conta do Vault + intenção classificada + sentimento e urgência do Radar + SLA atual do ticket (tempo aberto vs).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (0-2 sugestões de próximo passo com: {tipo_acão (internal_ticket | retenção_offer | upsell_hint | sla_alert | escalate_c…) e persistir no artefato do squad.
4. Entregar ao critic Prism; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: 0-2 sugestões de próximo passo com: {tipo_acão (internal_ticket | retenção_offer | upsell_hint | sla_alert | escalate_csm | kb_gap), descrição_curta, justifica…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Prism registrado
- [ ] Gate HITL respeitado: Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atenden…
- [ ] Gate HITL respeitado: Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'int…
- [ ] Gate HITL respeitado: Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso esp…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar co… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — resp… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromis… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Vault retorna flag 'cliente_em_risco_de_churn' (health score < 50): todas as sugestões do Scribe são marcadas com indicador visual e Lumen adiciona sugestão de… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Echo detecta que uma macro tem rejection_rate > 60% por 7 dias consecutivos: dispara alerta para gestor de CS no Slack pedindo revisão manual da macro antes de… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Shield detecta promessa de desconto ou benefício financeiro no rascunho do atendente: alerta de policy_violation com valor exato do limite autorizado e botão d… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Prism | BLOQUEIA entrega |

## Handoff

- **to:** Echo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
