---
task: vault()
responsavel: "Vault"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "ID do cliente (extraído pelo Radar do ticket) + intenção classificada (para priorizar quais dados buscar primeiro)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON 'pacote_de_conta' com: {plano, mrr, renovação_em_dias, último_nps, últimos_5_tickets_resumidos, pedidos_recentes, uso_produto_30d, notas_csm, flags_especiais, data_cliente_desde}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Latência target: < 800ms (queries em paralelo)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Orchestrator Compass imediatamente após classificação do Radar, em paralelo com outros workers"
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

# Recuperar Dados De Conta

**Task ID:** `vault()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Recuperar Dados De Conta |
| **status** | `pending` |
| **responsible_executor** | Vault (Vault — Context Fetcher de Conta) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recupera em paralelo todos os dados de contexto relevantes da conta do cliente no momento que a intenção é classificada: plano atual, MRR, data de renovação, histórico dos últimos 5 tickets (status, tipo, resolução), último NPS/CSAT registrado, uso do produto nos últimos 30 dias (logins, features ativas), dados de pedidos recentes (status, valores, transportadora), notas do CSM e flags especiais (VIP, em risco, upsell candidato). Monta o 'pacote de conta' que fundamenta qualquer sugestão contextualizada.

## Input

- ID do cliente (extraído pelo Radar do ticket) + intenção classificada (para priorizar quais dados buscar primeiro)

## Output

- JSON 'pacote_de_conta' com: {plano, mrr, renovação_em_dias, último_nps, últimos_5_tickets_resumidos, pedidos_recentes, uso_produto_30d, notas_csm, flags_especiais, data_cliente_desde}
- Latência target: < 800ms (queries em paralelo)

## Trigger

Disparado pelo Orchestrator Compass imediatamente após classificação do Radar, em paralelo com outros workers

## Knowledge base (o que o executor consulta)

- CRM (HubSpot/Salesforce): dados de conta, contato, renovação, MRR
- Helpdesk (Zendesk/Intercom): histórico de tickets dos últimos 90 dias
- ERP/OMS: pedidos e status
- CS Platform (ChurnZero/Gainsight): health score e uso do produto
- Supabase: cache de dados de conta para redução de latência

## Action Items

1. Confirmar o gatilho e carregar a entrada (ID do cliente (extraído pelo Radar do ticket) + intenção classificada (para priorizar quais dados buscar primeiro)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON 'pacote_de_conta' com: {plano, mrr, renovação_em_dias, último_nps, últimos_5_tickets_resumidos, pedidos_recentes,…) e persistir no artefato do squad.
4. Entregar ao critic Prism; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON 'pacote_de_conta' com: {plano, mrr, renovação_em_dias, último_nps, últimos_5_tickets_resumidos, pedidos_recentes, uso_produto_30d, notas_csm, flags_especi…
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

- **to:** Scribe
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
