---
task: farol()
responsavel: "Farol"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stream de eventos do CRM (aceites, registros de contato, atualizações de status) + configurações de SLA por tier de lead"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ações de escalonamento: {lead_id, status_sla, tempo_decorrido, ação_tomada: RE-ROTEAMENTO|ALERTA_GESTOR|ESCALA_GERENTE, timestamp}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "dashboard de SLA compliance atualizado em tempo real"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron a cada 60 segundos verificando todos os leads ativos sem primeiro contato confirmado; também dispara em eventos de lead criado/atribuído"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Veredito 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro deploy; em produção, amostras aleatórias (10%) passam por revisão humana"
    - "[ ] L3: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratamento especial"
    - "[ ] L3: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente"
    - "[ ] L3: Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interface de configuração, com log de auditoria"
    - "[ ] L3: Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor designado"
---

# Monitorar Primeiro Contato

**Task ID:** `farol()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Primeiro Contato |
| **status** | `pending` |
| **responsible_executor** | Farol (Farol (Worker de Monitor de SLA e Re-roteamento)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora em tempo real todos os leads no pipeline que ainda não tiveram primeiro contato confirmado. Para cada lead, acompanha: tempo desde atribuição, status de aceite do vendedor, confirmação de primeiro contato (ligação/WhatsApp registrado no CRM). Dispara alertas escalonados: 3 min sem aceite = re-roteia automaticamente; 10 min sem primeiro contato = alerta ao gestor; 30 min = escala para o gerente de vendas com contexto completo. Gera dashboard em tempo real de SLA compliance.

## Input

- Stream de eventos do CRM (aceites, registros de contato, atualizações de status) + configurações de SLA por tier de lead

## Output

- Ações de escalonamento: {lead_id, status_sla, tempo_decorrido, ação_tomada: RE-ROTEAMENTO|ALERTA_GESTOR|ESCALA_GERENTE, timestamp}
- dashboard de SLA compliance atualizado em tempo real

## Trigger

Cron a cada 60 segundos verificando todos os leads ativos sem primeiro contato confirmado; também dispara em eventos de lead criado/atribuído

## Knowledge base (o que o executor consulta)

- SLAs definidos por tier (HOT: 2min aceite / 5min primeiro contato
- WARM: 5min / 15min
- COLD: 30min / 2h), histórico de SLA compliance por vendedor, árvore de escalonamento (vendedor -> gestor -> gerente), templates de alerta por nível de escalonamento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stream de eventos do CRM (aceites, registros de contato, atualizações de status) + configurações de SLA por tier de lead).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ações de escalonamento: {lead_id, status_sla, tempo_decorrido, ação_tomada: RE-ROTEAMENTO|ALERTA_GESTOR|ESCALA_GERENTE,…) e persistir no artefato do squad.
4. Entregar ao critic Veredito 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ações de escalonamento: {lead_id, status_sla, tempo_decorrido, ação_tomada: RE-ROTEAMENTO|ALERTA_GESTOR|ESCALA_GERENTE, timestamp}
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Veredito 2 registrado
- [ ] Gate L3 respeitado: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização an…
- [ ] Gate L3 respeitado: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurtu…
- [ ] Gate L3 respeitado: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro depl… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratame… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interfac… | BLOQUEIA até decisão humana |
| VETO-005 | L3 — Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor desi… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão humana semanal do relatório de auditoria do Veredito para identificar vieses sistemáticos e calibrar o modelo de scoring | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Veredito 2 | BLOQUEIA entrega |

## Handoff

- **to:** Veredito 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
