---
task: atlas()
responsavel: "Atlas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Criterios de roteamento do Maestro: {território_requerido, especialidade_requerida, tier_do_lead, horário_entrada}"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lista ranqueada de vendedores: [{vendedor_id, nome, score_adequacao: 0-100, slots_disponíveis_proximas_2h, carteira_atual/capacidade_maxima, taxa_conversao_segmento, status_atual}] ordenada por score_adequacao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro em toda decisão de roteamento; também atualiza cache de disponibilidade a cada 5 minutos via cron para redução de latência"
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

# Consultar Capacidade Vendedores

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Consultar Capacidade Vendedores |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas (Worker de Disponibilidade e Capacidade)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Consulta em tempo real à capacidade de cada vendedor elegível: agenda do Google Calendar/Outlook (slots livres próximas 2h), carteira atual (leads em andamento vs limite de capacidade), status declarado (disponível/em call/ausente/férias), performance recente (taxa de conversão dos últimos 30 dias por segmento). Retorna lista ranqueada de vendedores elegíveis com score de adequação para o Maestro tomar a decisão de roteamento.

## Input

- Criterios de roteamento do Maestro: {território_requerido, especialidade_requerida, tier_do_lead, horário_entrada}

## Output

- Lista ranqueada de vendedores: [{vendedor_id, nome, score_adequacao: 0-100, slots_disponíveis_proximas_2h, carteira_atual/capacidade_maxima, taxa_conversao_segmento, status_atual}] ordenada por score_adequacao

## Trigger

Acionado pelo Maestro em toda decisão de roteamento; também atualiza cache de disponibilidade a cada 5 minutos via cron para redução de latência

## Knowledge base (o que o executor consulta)

- Estrutura da equipe de vendas (territórios, especialidades, limites de carteira por vendedor), calendário integrado (Google Calendar/Outlook via MCP), histórico de performance por vendedor e segmento, regras de exceção (vendedor não atende determinado setor/tamanho)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Criterios de roteamento do Maestro: {território_requerido, especialidade_requerida, tier_do_lead, horário_entrada}).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lista ranqueada de vendedores: [{vendedor_id, nome, score_adequacao: 0-100, slots_disponíveis_proximas_2h, carteira_atu…) e persistir no artefato do squad.
4. Entregar ao critic Veredito 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lista ranqueada de vendedores: [{vendedor_id, nome, score_adequacao: 0-100, slots_disponíveis_proximas_2h, carteira_atual/capacidade_maxima, taxa_conversao_seg…
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

- **to:** Worker de Notificação e Aceite
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
