---
task: veredito()
responsavel: "Veredito"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pacote completo de decisão do Maestro: {lead_dossiê, score_oracle, lista_atlas_ranqueada, vendedor_designado, justificativa_roteamento, mensagem_apresentação}"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredicto: {status: APROVADO|BLOQUEADO|REVISÃO_HUMANA, confiança: 0-100, problemas_detectados[], sugestão_alternativa?, flag_vies_sistemico: bool}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado automaticamente pelo Maestro em TODA decisão de roteamento antes da execução; também acionado manualmente pelo gestor para auditoria spot-check"
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

# Verificar Roteamento

**Task ID:** `veredito()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Roteamento |
| **status** | `pending` |
| **responsible_executor** | Veredito (Veredito (Critic / Verifier de Roteamento)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Áuditor independente que valida cada decisão de roteamento do Maestro ANTES do Hermes notificar. Verifica: (1) o scoring do Oracle está consistente com o perfil do lead, (2) o vendedor designado tem capacidade real e não viola regras de território/especialidade, (3) a mensagem de apresentação está personalizada e sem erros, (4) não há viéses sistemáticos (ex: sempre rotear leads HOT para o mesmo vendedor). Retorna APROVADO ou BLOQUEADO com justificativa. Também gera relatório semanal de auditoria de roteamentos.

## Input

- Pacote completo de decisão do Maestro: {lead_dossiê, score_oracle, lista_atlas_ranqueada, vendedor_designado, justificativa_roteamento, mensagem_apresentação}

## Output

- Veredicto: {status: APROVADO|BLOQUEADO|REVISÃO_HUMANA, confiança: 0-100, problemas_detectados[], sugestão_alternativa?, flag_vies_sistemico: bool}

## Trigger

Acionado automaticamente pelo Maestro em TODA decisão de roteamento antes da execução; também acionado manualmente pelo gestor para auditoria spot-check

## Knowledge base (o que o executor consulta)

- Playbook de Regras de Roteamento v1 (matriz score x território x especialidade), histórico de roteamentos anteriores e outcomes (converteu/não converteu), limites de capacidade por vendedor, política anti-vies (distribuição máxima por vendedor por período), critérios de compliance e LGPD para comunicação de leads

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pacote completo de decisão do Maestro: {lead_dossiê, score_oracle, lista_atlas_ranqueada, vendedor_designado, justifica…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Veredicto: {status: APROVADO|BLOQUEADO|REVISÃO_HUMANA, confiança: 0-100, problemas_detectados[], sugestão_alternativa?,…) e persistir no artefato do squad.
4. Entregar ao critic Veredito 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredicto: {status: APROVADO|BLOQUEADO|REVISÃO_HUMANA, confiança: 0-100, problemas_detectados[], sugestão_alternativa?, flag_vies_sistemico: bool}
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

- **to:** Farol
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
