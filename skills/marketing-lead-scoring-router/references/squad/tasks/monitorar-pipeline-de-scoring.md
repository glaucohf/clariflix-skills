---
task: pulse()
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Log de roteamentos do Vector (timestamp, tier, SDR designado), CRM activity feed (primeiro contato registrado pelo SDR), métricas de conversão do CRM por tier (semanal), health status dos webhooks de entrada do Scout, threshold de SLA por tier configurados, baseline histórico de distribuição de scores e taxas de conversão"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dashboard de KPIs em tempo real no ClickUp: speed-to-lead por fonte e por tier, % de leads órfãos, taxa de conversão corrente vs baseline por tier, distribuição de scores (histograma), health dos webhooks"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alertas escalonados: Warning para Orion quando SLA em risco, Critical para SDR Manager via Slack quando SLA violado, Escalation para HITL quando lead Hot sem contato em > 30 minutos"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório semanal de performance do modelo com recomendações de ajuste de pesos para Critique"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job de monitoramento a cada 5 minutos (cron); lead Hot registrado no Vector sem primeiro contato no CRM apos 15 minutos; desvio de distribuição de scores > 20% vs média histórica dos últimos 30 dias;…"
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

# Monitorar Pipeline De Scoring

**Task ID:** `pulse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Lead Scoring & Router

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Pipeline De Scoring |
| **status** | `pending` |
| **responsible_executor** | Pulse (Pulse — Pipeline Monitor & Anomaly Detector) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitor contínuo do pipeline de scoring e roteamento. Rastreia em tempo real: leads órfãos (score calculado mas sem roteamento em > 10 minutos), leads Hot sem primeiro contato do SDR em > 15 minutos, taxa de conversão por tier comparada ao baseline histórico, desvio de distribuição de scores (se o modelo está enviando mais ou menos leads para Hot do que a média histórica indica drift), e health dos webhooks de entrada (fonte sem novo lead em > 24h pode ser webhook quebrado). Gera alertas escalonados: Warning (SLA em risco) -> Critical (SLA violado) -> Escalation (intervenção humana necessária). Alimenta o dashboard de KPIs do squad no ClickUp.

## Input

- Log de roteamentos do Vector (timestamp, tier, SDR designado), CRM activity feed (primeiro contato registrado pelo SDR), métricas de conversão do CRM por tier (semanal), health status dos webhooks de entrada do Scout, threshold de SLA por tier configurados, baseline histórico de distribuição de scores e taxas de conversão

## Output

- Dashboard de KPIs em tempo real no ClickUp: speed-to-lead por fonte e por tier, % de leads órfãos, taxa de conversão corrente vs baseline por tier, distribuição de scores (histograma), health dos webhooks
- Alertas escalonados: Warning para Orion quando SLA em risco, Critical para SDR Manager via Slack quando SLA violado, Escalation para HITL quando lead Hot sem contato em > 30 minutos
- Relatório semanal de performance do modelo com recomendações de ajuste de pesos para Critique

## Trigger

Job de monitoramento a cada 5 minutos (cron); lead Hot registrado no Vector sem primeiro contato no CRM apos 15 minutos; desvio de distribuição de scores > 20% vs média histórica dos últimos 30 dias; webhook de fonte sem evento em > 24h; solicitação de relatório semanal automático toda segunda-feira 8h

## Knowledge base (o que o executor consulta)

- SLAs por tier (Hot < 5min para roteamento, < 15min para primeiro contato
- Warm < 2h
- Cold < 24h), baseline historico de metricas por tier, mapeamento de SDRs e canais de notificacao (Slack handle, WhatsApp), regras de escalada (quem notificar e quando), historico de anomalias anteriores para context de alertas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Log de roteamentos do Vector (timestamp, tier, SDR designado), CRM activity feed (primeiro contato registrado pelo SDR)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dashboard de KPIs em tempo real no ClickUp: speed-to-lead por fonte e por tier, % de leads órfãos, taxa de conversão co…) e persistir no artefato do squad.
4. Entregar ao critic Critique 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dashboard de KPIs em tempo real no ClickUp: speed-to-lead por fonte e por tier, % de leads órfãos, taxa de conversão corrente vs baseline por tier, distribuiçã…
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

- **to:** Critique
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
