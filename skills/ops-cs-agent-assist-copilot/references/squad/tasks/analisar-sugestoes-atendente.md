---
task: echo()
responsavel: "Echo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Log de cada sugestão: {sugestão_id, tipo (macro/rag/free), intenção, texto_sugestão, ação_do_atendente (accepted/edited/rejected/ignored), texto_editado_se_aplicável, ticket_id, atendente_id, timestamp}"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Log persistido no Supabase por sugestão"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Dashboard Langfuse com: adoption_rate por intenção, rejection_rate por macro, top edições mais frequentes (indica lacunas), AHT antes e depois por atendente"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório semanal no Slack com: top 5 sugestões mais aceitas, top 5 mais rejeitadas com análise de causa, recomendações de atualização de KB/macros"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento de feedback do overlay (atendente clica em aceitar/rejeitar/ignorar) via webhook; job semanal para relatório agregado (cron segunda-feira 8h)"
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

# Analisar Sugestões Atendente

**Task ID:** `echo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Sugestões Atendente |
| **status** | `pending` |
| **responsible_executor** | Echo (Echo — Agente de Feedback & Aprendizado Contínuo) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Registra e analisa cada sugestão exibida ao atendente e o que aconteceu com ela: aceita integralmente, aceita com edição, rejeitada (e qual foi a resposta manual do atendente), ignorada. Agrega feedback por intenção, por atendente, por macro e por período. Detecta padrões: sugestões consistentemente rejeitadas indicam prompt desatualizado ou macro errada; sugestões consistentemente editadas indicam personalização insuficiente. Gera relatório semanal de qualidade das sugestões e alimenta o ciclo de melhoria (atualiza KB, refina prompts, atualiza ground-truth).

## Input

- Log de cada sugestão: {sugestão_id, tipo (macro/rag/free), intenção, texto_sugestão, ação_do_atendente (accepted/edited/rejected/ignored), texto_editado_se_aplicável, ticket_id, atendente_id, timestamp}

## Output

- Log persistido no Supabase por sugestão
- Dashboard Langfuse com: adoption_rate por intenção, rejection_rate por macro, top edições mais frequentes (indica lacunas), AHT antes e depois por atendente
- Relatório semanal no Slack com: top 5 sugestões mais aceitas, top 5 mais rejeitadas com análise de causa, recomendações de atualização de KB/macros

## Trigger

Evento de feedback do overlay (atendente clica em aceitar/rejeitar/ignorar) via webhook; job semanal para relatório agregado (cron segunda-feira 8h)

## Knowledge base (o que o executor consulta)

- Log historico de sugestoes e feedbacks no Supabase, benchmark de adoption rate por intencao (meta >= 55%), modelos de macros atuais e suas versoes, catalogo de ground-truth com data de ultima atualizacao

## Action Items

1. Confirmar o gatilho e carregar a entrada (Log de cada sugestão: {sugestão_id, tipo (macro/rag/free), intenção, texto_sugestão, ação_do_atendente (accepted/edited…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Log persistido no Supabase por sugestão) e persistir no artefato do squad.
4. Entregar ao critic Prism; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Log persistido no Supabase por sugestão
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

- **to:** Shield
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
