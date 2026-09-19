---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem nova do cliente (texto) + histórico das últimas 5 mensagens da conversa + ID do ticket + ID do atendente ativo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON estruturado com: {intenção_primária, intenção_secundária, confiança_score, entidades_extraídas, tom_emocional, nível_urgência, mudança_de_assunto_detectada, timestamp}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Latência target: < 300ms"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de nova mensagem do cliente no helpdesk (Zendesk/Intercom event: 'ticket.updated' ou 'conversation.message.created' onde sender = customer)"
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

# Classificar Intencao Do Cliente

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Intencao Do Cliente |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Listener & Classifier de Intenção) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora cada mensagem nova na conversa em tempo real via webhook do helpdesk. Classifica a intencao primaria e secundaria do cliente com score de confianca (0-1), detecta mudanca de assunto mid-conversation, extrai entidades relevantes (numero de pedido, SKU, data, valor, nome de produto) via NER, identifica o tom emocional do cliente (neutro, frustrado, urgente, satisfeito) e o nivel de urgencia. Envia o pacote classificado ao Orchestrator Compass em < 300ms para nao criar lag perceptivel ao atendente.

## Input

- Mensagem nova do cliente (texto) + histórico das últimas 5 mensagens da conversa + ID do ticket + ID do atendente ativo

## Output

- JSON estruturado com: {intenção_primária, intenção_secundária, confiança_score, entidades_extraídas, tom_emocional, nível_urgência, mudança_de_assunto_detectada, timestamp}
- Latência target: < 300ms

## Trigger

Webhook de nova mensagem do cliente no helpdesk (Zendesk/Intercom event: 'ticket.updated' ou 'conversation.message.created' onde sender = customer)

## Knowledge base (o que o executor consulta)

- Taxonomia de intencoes do cliente (30-50 classes customizadas por verticale do cliente), modelo NER para entidades do dominio (SKUs, IDs de pedido, nomes de plano), historico das ultimas 5 mensagens da conversa para contexto de continuidade, lista de keywords de urgencia e escalonamento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Mensagem nova do cliente (texto) + histórico das últimas 5 mensagens da conversa + ID do ticket + ID do atendente ativo).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON estruturado com: {intenção_primária, intenção_secundária, confiança_score, entidades_extraídas, tom_emocional, nív…) e persistir no artefato do squad.
4. Entregar ao critic Prism; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON estruturado com: {intenção_primária, intenção_secundária, confiança_score, entidades_extraídas, tom_emocional, nível_urgência, mudança_de_assunto_detectad…
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

- **to:** Vault
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
