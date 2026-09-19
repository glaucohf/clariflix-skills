---
task: workerDeLeadScoring()
responsavel: "Worker de Lead Scoring"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê enriquecido do Argos + eventos comportamentais do lead (CRM/analytics): {páginas_visitadas[], formulários_preenchidos[], emails_abertos[], anúncios_clicados[], histórico_interações[]}"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score estruturado: {score_total: 0-100, tier: HOT|WARM|COLD, breakdown: {fit, intenção, urgência, relação}, justificativa_textual, próxima_acão_sugerida}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro após Argos retornar dossiê; re-score automático quando novo evento comportamental é registrado (email aberto, página visitada, WhatsApp respondido)"
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

# Calcular Score Lead

**Task ID:** `workerDeLeadScoring()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Score Lead |
| **status** | `pending` |
| **responsible_executor** | Worker de Lead Scoring (Oracle (Worker de Lead Scoring)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o dossiê enriquecido e o histórico comportamental do lead (páginas visitadas, emails abertos, formulário preenchido, anúncio clicado) e calcula score composto em 4 dimensões: Fit (perfil ideal x perfil real), Intenção (sinais comportamentais recentes), Urgência (timing, verba, prazo declarado) e Relação (origem indicação/evento/inbound frio). Retorna score 0-100 com breakdown por dimensão e tier (HOT/WARM/COLD) para o Maestro priorizar a fila.

## Input

- Dossiê enriquecido do Argos + eventos comportamentais do lead (CRM/analytics): {páginas_visitadas[], formulários_preenchidos[], emails_abertos[], anúncios_clicados[], histórico_interações[]}

## Output

- Score estruturado: {score_total: 0-100, tier: HOT|WARM|COLD, breakdown: {fit, intenção, urgência, relação}, justificativa_textual, próxima_acão_sugerida}

## Trigger

Acionado pelo Maestro após Argos retornar dossiê; re-score automático quando novo evento comportamental é registrado (email aberto, página visitada, WhatsApp respondido)

## Knowledge base (o que o executor consulta)

- Modelo de scoring calibrado com histórico de conversão do cliente (leads convertidos x não convertidos por perfil), critérios BANT/MEDDIC adaptados ao negócio, pesos por canal de origem, benchmarks de score por setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossiê enriquecido do Argos + eventos comportamentais do lead (CRM/analytics): {páginas_visitadas[], formulários_preenc…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score estruturado: {score_total: 0-100, tier: HOT|WARM|COLD, breakdown: {fit, intenção, urgência, relação}, justificati…) e persistir no artefato do squad.
4. Entregar ao critic Veredito 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score estruturado: {score_total: 0-100, tier: HOT|WARM|COLD, breakdown: {fit, intenção, urgência, relação}, justificativa_textual, próxima_acão_sugerida}
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
