---
task: atlas()
responsavel: "Atlas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados brutos de plataformas (Google Ads API, Meta Ads API): spend, impressões, cliques, conversões rastreadas + Dados de CRM (HubSpot/Salesforce): leads, oportunidades, deals fechados com source/campaign attribution + Dados de pixel/conversão offline + Janela de atribuição configurada (7d click / 1d view ou customizada)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dashboard de performance consolidado (CAC por canal, ROAS por campanha/ad set/criativo, % de budget em criativos performantes, desvio de pacing acumulado, CPL por etapa de funil), Relatório diário estruturado (PDF + JSON) para o orquestrador e cliente, Alertas de anomalia de atribuição (ex: conversões caindo sem queda de cliques = problema de pixel), Dados de closed-loop attribution para calibrar decisões do Midas e Prism"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Relatório diário automático as 08h (D-1 completo). Relatório semanal toda segunda-feira as 07h (semana anterior). Trigger em tempo real quando o orquestrador solicita contexto de atribuição para deci…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de ROAS para escala, orçamento máximo em risco por ciclo) — sem essa aprovação o squad não opera"
    - "[ ] HITL: Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget total ou pausar campanha inteira) requer aprovação explícita via Slack/WhatsApp antes de execução pelo Midas"
    - "[ ] HITL: Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos de mensagem sem histórico) requer aprovação humana — irreversível em termos de impressão inicial"
    - "[ ] HITL: Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de threshold) requerem OK do gestor antes de ativação automática"
    - "[ ] HITL: Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com os guardrails mais recentes aprovados"
---

# Consolidar Dados De Performance

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Consolidar Dados De Performance |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Attribution & Analytics Agent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de consolidação de performance cross-channel e atribuição de pipeline. Agrega dados de todas as plataformas de mídia (Google Ads, Meta Ads) com dados de CRM (leads gerados, oportunidades abertas, deals fechados) para calcular CAC real, ROAS de pipeline (não só de conversão imediata) e LTV por canal/campanha/criativo. Detecta anomalias de atribuição e gaps de rastreamento. Gera o relatório de performance consolidado diário e semanal.

## Input

- Dados brutos de plataformas (Google Ads API, Meta Ads API): spend, impressões, cliques, conversões rastreadas + Dados de CRM (HubSpot/Salesforce): leads, oportunidades, deals fechados com source/campaign attribution + Dados de pixel/conversão offline + Janela de atribuição configurada (7d click / 1d view ou customizada)

## Output

- Dashboard de performance consolidado (CAC por canal, ROAS por campanha/ad set/criativo, % de budget em criativos performantes, desvio de pacing acumulado, CPL por etapa de funil), Relatório diário estruturado (PDF + JSON) para o orquestrador e cliente, Alertas de anomalia de atribuição (ex: conversões caindo sem queda de cliques = problema de pixel), Dados de closed-loop attribution para calibrar decisões do Midas e Prism

## Trigger

Relatório diário automático as 08h (D-1 completo). Relatório semanal toda segunda-feira as 07h (semana anterior). Trigger em tempo real quando o orquestrador solicita contexto de atribuição para decisão de realocação

## Knowledge base (o que o executor consulta)

- Estrutura completa de campanhas por plataforma (hierarquia: campanha > ad set > ad), Mapeamento de UTMs e parâmetros de rastreamento, Janelas de atribuição configuradas por plataforma, Dados históricos de funil (taxa de conversão lead-para-oportunidade, oportunidade-para-deal por canal), Benchmarks de CAC/ROAS setoriais, Modelo de LTV do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados brutos de plataformas (Google Ads API, Meta Ads API): spend, impressões, cliques, conversões rastreadas + Dados d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dashboard de performance consolidado (CAC por canal, ROAS por campanha/ad set/criativo, % de budget em criativos perfor…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dashboard de performance consolidado (CAC por canal, ROAS por campanha/ad set/criativo, % de budget em criativos performantes, desvio de pacing acumulado, CPL…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis 2 registrado
- [ ] Gate HITL respeitado: Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA…
- [ ] Gate HITL respeitado: Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: move…
- [ ] Gate HITL respeitado: Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos forma…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget to… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de thresh… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com o… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Onboarding de nova plataforma ou canal: qualquer expansão para nova plataforma de mídia (ex: adicionar TikTok Ads, Pinterest Ads, CTV) requer aprovação e confi… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Bloqueio por anomalia crítica: se Argos detectar anomalia CRITICAL (ex: ROAS caiu > 50% em 1h ou spend disparou 300% acima do target), o squad pausa todas as a… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Aegis 2 | BLOQUEIA entrega |

## Handoff

- **to:** Sentinel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
