---
task: workerDeEnriquecimento()
responsavel: "Worker de Enriquecimento"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead bruto: {nome?, email?, telefone?, empresa?, canal_origem, utm_params, timestamp_entrada}"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê JSON enriquecido: {cargo, empresa, setor, tamanho_empresa, localização, linkedin_url, sinais_intenção[], duplicata_detectada: bool, confiança_enriquecimento: 0-100}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo lead criado em qualquer canal de entrada (webhook CRM, formulário, WhatsApp, ads); também acionado em re-enriquecimento periódico de leads frios (cron semanal)"
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

# Retornar Dossiê Estruturado

**Task ID:** `workerDeEnriquecimento()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Retornar Dossiê Estruturado |
| **status** | `pending` |
| **responsible_executor** | Worker de Enriquecimento (Argos (Worker de Enriquecimento)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o lead bruto (nome, email, telefone, empresa ou apenas número de WhatsApp) e executa enriquecimento automático via Clay/Apollo/Clearbit para completar campos críticos: cargo, tamanho de empresa, setor, localização, presença LinkedIn, sinais de intenção recentes. Detecta duplicatas no CRM antes de criar registro. Retorna dossiê estruturado para o Maestro em <30 segundos.

## Input

- Lead bruto: {nome?, email?, telefone?, empresa?, canal_origem, utm_params, timestamp_entrada}

## Output

- Dossiê JSON enriquecido: {cargo, empresa, setor, tamanho_empresa, localização, linkedin_url, sinais_intenção[], duplicata_detectada: bool, confiança_enriquecimento: 0-100}

## Trigger

Novo lead criado em qualquer canal de entrada (webhook CRM, formulário, WhatsApp, ads); também acionado em re-enriquecimento periódico de leads frios (cron semanal)

## Knowledge base (o que o executor consulta)

- Base de dados Clay/Apollo (275M+ contatos), histórico de enriquecimentos anteriores para calibrar confiança, regras de dedup do CRM (campos-chave para identificação de duplicata), mapeamento de setores/territórios do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead bruto: {nome?, email?, telefone?, empresa?, canal_origem, utm_params, timestamp_entrada}).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossiê JSON enriquecido: {cargo, empresa, setor, tamanho_empresa, localização, linkedin_url, sinais_intenção[], duplica…) e persistir no artefato do squad.
4. Entregar ao critic Veredito 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossiê JSON enriquecido: {cargo, empresa, setor, tamanho_empresa, localização, linkedin_url, sinais_intenção[], duplicata_detectada: bool, confiança_enriquecim…
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

- **to:** Worker de Lead Scoring
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
