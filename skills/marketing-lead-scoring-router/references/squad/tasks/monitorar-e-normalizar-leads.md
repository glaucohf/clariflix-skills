---
task: scout()
responsavel: "Scout"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Webhooks de formulários (HubSpot Forms, Typeform, RDStation), Meta Lead Ads webhook, Google Ads Lead Form webhook, LinkedIn Lead Gen Forms webhook, WhatsApp Business API eventos de novo contato, importações manuais CSV via ClickUp task, CRM de novos contatos criados por SDR"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead normalizado em schema padrão (JSON estruturado com todos os campos disponíveis preenchidos e campos ausentes marcados como null), flag de deduplicação (novo vs existente vs possível duplicata), fonte e timestamp de entrada, UTMs completas quando disponíveis, enfileiramento no pipeline Orion via event"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de nova submissão de formulário; evento de novo lead em Meta/Google/LinkedIn Ads; novo contato no WhatsApp Business; importação manual acionada via ClickUp; cron de varredura de novos contato…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Critique 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o threshold de 75 é ajustável) e validar a Routing Matrix antes de ativar em produção (L3)"
    - "[ ] HITL: Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads (L3)"
    - "[ ] HITL: Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique deve ser aprovada pelo Sales Lead antes de Orion aplicar em produção (L3)"
    - "[ ] HITL: Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerteza (L3)"
    - "[ ] HITL: Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3)"
---

# Monitorar E Normalizar Leads

**Task ID:** `scout()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Lead Scoring & Router

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar E Normalizar Leads |
| **status** | `pending` |
| **responsible_executor** | Scout (Scout — Lead Intake & Source Mapper) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Porta de entrada de todos os leads. Scout monitora e normaliza leads provenientes de fontes heterogeneas (formularios web via webhook, Meta/Google Ads via Lead Ads API, WhatsApp Business API, LinkedIn Lead Gen Forms, eventos/planilhas importadas manualmente, indicacoes via CRM). Para cada lead recebido, extrai os campos brutos disponıveis, normaliza para o schema padrao do squad (nome, email, telefone, empresa, cargo, fonte, UTMs, timestamp), deduplica contra o CRM (evita reprocessar lead existente) e enfileira para enriquecimento. Scout e a unica interface com fontes externas de entrada — nenhum outro agente consome webhooks diretamente.

## Input

- Webhooks de formulários (HubSpot Forms, Typeform, RDStation), Meta Lead Ads webhook, Google Ads Lead Form webhook, LinkedIn Lead Gen Forms webhook, WhatsApp Business API eventos de novo contato, importações manuais CSV via ClickUp task, CRM de novos contatos criados por SDR

## Output

- Lead normalizado em schema padrão (JSON estruturado com todos os campos disponíveis preenchidos e campos ausentes marcados como null), flag de deduplicação (novo vs existente vs possível duplicata), fonte e timestamp de entrada, UTMs completas quando disponíveis, enfileiramento no pipeline Orion via event

## Trigger

Webhook de nova submissão de formulário; evento de novo lead em Meta/Google/LinkedIn Ads; novo contato no WhatsApp Business; importação manual acionada via ClickUp; cron de varredura de novos contatos no CRM a cada 15 minutos

## Knowledge base (o que o executor consulta)

- Schema padrao de lead do squad (mapeamento de campos por fonte), regras de deduplicacao (email como primary key, fallback para telefone + nome), lista de fontes ativas e seus endpoints de webhook, UTM taxonomy da empresa, regras de exclusao (emails corporativos de domınios blacklistados, leads sem empresa para B2B)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Webhooks de formulários (HubSpot Forms, Typeform, RDStation), Meta Lead Ads webhook, Google Ads Lead Form webhook, Link…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead normalizado em schema padrão (JSON estruturado com todos os campos disponíveis preenchidos e campos ausentes marca…) e persistir no artefato do squad.
4. Entregar ao critic Critique 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead normalizado em schema padrão (JSON estruturado com todos os campos disponíveis preenchidos e campos ausentes marcados como null), flag de deduplicação (no…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Critique 2 registrado
- [ ] Gate HITL respeitado: Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa…
- [ ] Gate HITL respeitado: Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de p…
- [ ] Gate HITL respeitado: Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) prop…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique de… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerte… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Desvio crítico de performance detectado por Critique — quando Precision@Hot cai abaixo de 40% ou Recall cai abaixo de 50%, o squad entra em modo de revisão e n… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Ativação de nova fonte de leads (novo canal, novo formulário) — Scout não ativa fonte nova automaticamente, requer validação do schema de campos e regras de no… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Ajuste de capacidade de SDR na Routing Matrix — quando SDR entra em ferias ou saı da empresa, Vector nao rebalanceia automaticamente sem confirmacao do Sales L… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Critique 2 | BLOQUEIA entrega |

## Handoff

- **to:** Apex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
