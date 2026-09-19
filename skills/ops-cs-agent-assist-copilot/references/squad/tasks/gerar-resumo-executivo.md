---
task: memo()
responsavel: "Memo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição completa da conversa (todas as mensagens do ticket, inclusive de atendentes anteriores) + pacote_de_conta do Vault + status atual do ticket"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resumo estruturado em 2 formatos: {resumo_contexto: '5 bullets de contexto imediato para o atendente'} e {resumo_resolução: 'estrutura padrão: problema | causa | solução | followup'}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Pronto para copiar/colar no campo de nota interna ou resolução do ticket"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: (A) Ticket aberto pelo atendente com > 10 mensagens históricas — Compass dispara automaticamente; (B) Atendente clica em 'Gerar Resumo' no overlay; (C) Ticket marcado como resolvido — resumo de resol…"
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

# Gerar Resumo Executivo

**Task ID:** `memo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Resumo Executivo |
| **status** | `pending` |
| **responsible_executor** | Memo (Memo — Agente de Resumo de Ticket) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gera resumos executivos do histórico do ticket sob demanda ou automaticamente em 2 momentos: (1) quando o atendente abre um ticket com mais de 10 mensagens (resumo de contexto imediato); (2) ao final de cada atendimento (resumo de resolução para o log). O resumo de contexto cobre: problema principal, ações já tentadas, compromissos feitos, estado atual em 5 bullets. O resumo de resolução cobre: problema, causa raiz, solução aplicada, followup necessário, em formato padrão para o campo de resolução do ticket no helpdesk.

## Input

- Transcrição completa da conversa (todas as mensagens do ticket, inclusive de atendentes anteriores) + pacote_de_conta do Vault + status atual do ticket

## Output

- Resumo estruturado em 2 formatos: {resumo_contexto: '5 bullets de contexto imediato para o atendente'} e {resumo_resolução: 'estrutura padrão: problema | causa | solução | followup'}
- Pronto para copiar/colar no campo de nota interna ou resolução do ticket

## Trigger

(A) Ticket aberto pelo atendente com > 10 mensagens históricas — Compass dispara automaticamente; (B) Atendente clica em 'Gerar Resumo' no overlay; (C) Ticket marcado como resolvido — resumo de resolução gerado automaticamente para o log

## Knowledge base (o que o executor consulta)

- Transcrição completa do ticket (via API do helpdesk), template de resumo por tipo de intenção (diferente para billing vs
- onboarding vs
- suporte técnico), política de followup por tipo de resolução, exemplos de resumos de alta qualidade por categoria (few-shot)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcrição completa da conversa (todas as mensagens do ticket, inclusive de atendentes anteriores) + pacote_de_conta d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resumo estruturado em 2 formatos: {resumo_contexto: '5 bullets de contexto imediato para o atendente'} e {resumo_resolu…) e persistir no artefato do squad.
4. Entregar ao critic Prism; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resumo estruturado em 2 formatos: {resumo_contexto: '5 bullets de contexto imediato para o atendente'} e {resumo_resolução: 'estrutura padrão: problema | causa…
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

- **to:** Lumen
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
