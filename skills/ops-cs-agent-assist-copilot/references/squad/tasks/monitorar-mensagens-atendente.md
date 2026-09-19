---
task: shield()
responsavel: "Shield"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Rascunho da resposta do atendente (capturado via hook no campo de texto do helpdesk) + regras de compliance carregadas + contexto do ticket (plano do cliente, políticas aplicáveis)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alerta inline com: {tipo_risco (policy_violation | lgpd | linguagem | confidencial), severidade (info | warning | blocker), descrição_do_problema, sugestão_de_correção}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Severidade 'blocker' (violação de LGPD): adiciona pop-up de confirmação obrigatória antes do envio"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Registro de todo alerta no Langfuse para auditoria"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Hook em tempo real no campo de composição do helpdesk (debounce 800ms após última tecla digitada pelo atendente); acionado apenas para mensagens do atendente, nunca do cliente"
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

# Monitorar Mensagens Atendente

**Task ID:** `shield()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Mensagens Atendente |
| **status** | `pending` |
| **responsible_executor** | Shield (Shield — Agente de Alerta de Risco & Compliance) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora cada mensagem do atendente (não do cliente) antes do envio para detectar riscos em tempo real: promessas fora da política (prazo de devolução errado, desconto não autorizado, comprometimento jurídico não permitido), exposição de dados de outros clientes, linguagem inadequada (agressiva, discriminatória, informal demais para o contexto), menção de informações confidenciais da empresa. Exibe alerta inline no momento da digitação, antes do atendente enviar. Não bloqueia o envio (L1), apenas alerta — exceto violações de LGPD que são L3 e requerem confirmação explícita.

## Input

- Rascunho da resposta do atendente (capturado via hook no campo de texto do helpdesk) + regras de compliance carregadas + contexto do ticket (plano do cliente, políticas aplicáveis)

## Output

- Alerta inline com: {tipo_risco (policy_violation | lgpd | linguagem | confidencial), severidade (info | warning | blocker), descrição_do_problema, sugestão_de_correção}
- Severidade 'blocker' (violação de LGPD): adiciona pop-up de confirmação obrigatória antes do envio
- Registro de todo alerta no Langfuse para auditoria

## Trigger

Hook em tempo real no campo de composição do helpdesk (debounce 800ms após última tecla digitada pelo atendente); acionado apenas para mensagens do atendente, nunca do cliente

## Knowledge base (o que o executor consulta)

- Rulebook de compliance e políticas (devolução, reembolso, SLA, descontos autorizados, termos proibidos), regulamentação LGPD aplicável ao setor do cliente, lista de informações confidenciais da empresa, glossário de linguagem inadequada por contexto (formal, semi-formal, B2C, B2B), histórico de violações anteriores para aprendizado de padrões

## Action Items

1. Confirmar o gatilho e carregar a entrada (Rascunho da resposta do atendente (capturado via hook no campo de texto do helpdesk) + regras de compliance carregadas…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alerta inline com: {tipo_risco (policy_violation | lgpd | linguagem | confidencial), severidade (info | warning | block…) e persistir no artefato do squad.
4. Entregar ao critic Prism; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alerta inline com: {tipo_risco (policy_violation | lgpd | linguagem | confidencial), severidade (info | warning | blocker), descrição_do_problema, sugestão_de_…
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

- **to:** Prism
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
