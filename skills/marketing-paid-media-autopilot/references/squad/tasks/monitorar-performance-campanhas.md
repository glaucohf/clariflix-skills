---
task: argos()
responsavel: "Argos"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Métricas brutas das APIs de plataforma (impressões, cliques, conversões, spend, ROAS, CPM, CTR, frequência) + Guardrails financeiros configurados (thresholds de ROAS, CPA, frequência, pacing target) + Janela de tempo de análise"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de anomalias estruturado (JSON): lista de ad sets/campanhas fora do threshold, tipo de anomalia (pacing_deviation / roas_drop / cpm_inflation / creative_fatigue), severidade (low/medium/high/critical), delta percentual vs baseline, recomendação de ação sugerida"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron job a cada 15-30 minutos (configurável). Trigger imediato se spend/hora exceder 150% do target ou ROAS cair > 30% em relação à média das últimas 4h"
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

# Monitorar Performance Campanhas

**Task ID:** `argos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Performance Campanhas |
| **status** | `pending` |
| **responsible_executor** | Argos (Argos — Performance Monitor) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de monitoramento contínuo de performance de campanhas. Executa polling das APIs de plataforma (Google Ads, Meta Ads) a cada 15-30 minutos, detecta anomalias de pacing (desvio > 5% do target diário), quedas de ROAS abaixo do threshold, inflação de CPM e fadiga de criativo (CTR decay + frequência > limite). Gera alertas estruturados para o orquestrador Orion e para o dashboard em tempo real.

## Input

- Métricas brutas das APIs de plataforma (impressões, cliques, conversões, spend, ROAS, CPM, CTR, frequência) + Guardrails financeiros configurados (thresholds de ROAS, CPA, frequência, pacing target) + Janela de tempo de análise

## Output

- Relatório de anomalias estruturado (JSON): lista de ad sets/campanhas fora do threshold, tipo de anomalia (pacing_deviation / roas_drop / cpm_inflation / creative_fatigue), severidade (low/medium/high/critical), delta percentual vs baseline, recomendação de ação sugerida

## Trigger

Cron job a cada 15-30 minutos (configurável). Trigger imediato se spend/hora exceder 150% do target ou ROAS cair > 30% em relação à média das últimas 4h

## Knowledge base (o que o executor consulta)

- Histórico de performance dos últimos 90 dias por campanha/ad set/criativo, Guardrails financeiros aprovados pelo cliente (thresholds.yaml), Benchmarks setoriais de ROAS/CAC/CPM, Curvas históricas de fadiga de criativo do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Métricas brutas das APIs de plataforma (impressões, cliques, conversões, spend, ROAS, CPM, CTR, frequência) + Guardrail…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de anomalias estruturado (JSON): lista de ad sets/campanhas fora do threshold, tipo de anomalia (pacing_devia…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de anomalias estruturado (JSON): lista de ad sets/campanhas fora do threshold, tipo de anomalia (pacing_deviation / roas_drop / cpm_inflation / creat…
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

- **to:** Midas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
