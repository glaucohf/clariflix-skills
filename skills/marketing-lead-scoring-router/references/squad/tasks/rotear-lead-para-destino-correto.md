---
task: vector()
responsavel: "Vector"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Score Card completo do Apex (score, tier, reasoning, confidence), lead enriquecido do Iris, Routing Matrix configurada (regras de atribuição de SDR por território/vertical/carga atual), templates de brief por tier e por fonte de origem, disponibilidade atual dos SDRs (via CRM ou calendário integrado), limites de capacidade por SDR"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Roteamento executado com prova de trabalho: CRM deal/contact atualizado com score, tier, fonte e timestamp, task no ClickUp criada para SDR com brief completo (empresa, score breakdown, sinal de intent, próximos passos sugeridos), sequência automática ativada no HubSpot para tier 2 (email + WhatsApp), notificação push para SDR designado (Slack + WhatsApp) para leads Hot, registro de roteamento no log centralizado (para auditoria e análise de Pulse), tempo de roteamento registrado (speed-to-route para KPI)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Score Card gerado pelo Apex com tier definido (trigger primário); re-score de lead Warm que subiu para Hot (re-roteamento imediato); lead órfão detectado pelo Pulse (sem atividade em 48h — re-roteia…"
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

# Rotear Lead Para Destino Correto

**Task ID:** `vector()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Lead Scoring & Router

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Rotear Lead Para Destino Correto |
| **status** | `pending` |
| **responsible_executor** | Vector (Vector — Intelligent Router Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa o roteamento do lead para o destino correto baseado no Score Composto, tier, fonte de origem e disponibilidade dos canais de destino. Routing Matrix: Tier Hot (>= 75) -> SDR humano designado por território/vertical em < 5 minutos com brief completo no CRM + task urgente no ClickUp + notificação Slack/WhatsApp para o SDR. Tier Warm (50-74) -> sequência automática de email/WhatsApp com personalização baseada no score (templates diferentes por faixa de score) + CRM deal criado em estágio Prospecting. Tier Cold (30-49) -> fluxo de nurture de longo prazo (email + retargeting) + tag no CRM para remarketing. Tier Unfit (< 30) -> CRM contact criado com tag Unfit, excluído de listas ativas mas mantido para referência. Vector nunca envia mensagem diretamente — cria as tasks e aciona os sistemas (CRM deal, ClickUp task, HubSpot sequence) que executam o contato.

## Input

- Score Card completo do Apex (score, tier, reasoning, confidence), lead enriquecido do Iris, Routing Matrix configurada (regras de atribuição de SDR por território/vertical/carga atual), templates de brief por tier e por fonte de origem, disponibilidade atual dos SDRs (via CRM ou calendário integrado), limites de capacidade por SDR

## Output

- Roteamento executado com prova de trabalho: CRM deal/contact atualizado com score, tier, fonte e timestamp, task no ClickUp criada para SDR com brief completo (empresa, score breakdown, sinal de intent, próximos passos sugeridos), sequência automática ativada no HubSpot para tier 2 (email + WhatsApp), notificação push para SDR designado (Slack + WhatsApp) para leads Hot, registro de roteamento no log centralizado (para auditoria e análise de Pulse), tempo de roteamento registrado (speed-to-route para KPI)

## Trigger

Score Card gerado pelo Apex com tier definido (trigger primário); re-score de lead Warm que subiu para Hot (re-roteamento imediato); lead órfão detectado pelo Pulse (sem atividade em 48h — re-roteia ou escala); alteração de disponibilidade de SDR (re-balanceia leads em fila); solicitação manual de re-roteamento via ClickUp

## Knowledge base (o que o executor consulta)

- Routing Matrix completa (regras de atribuição por tier + território + vertical + carga de SDR), capacidade máxima de leads por SDR por semana, templates de brief por tier e por fonte de origem (brief diferente para lead de webinar vs lead de ads vs lead de indicação), regras de SLA por tier (Hot: < 5min, Warm: < 2h, Cold: < 24h), histórico de performance de conversão por SDR (para roteamento inteligente baseado em match SDR x perfil de lead)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Score Card completo do Apex (score, tier, reasoning, confidence), lead enriquecido do Iris, Routing Matrix configurada…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Roteamento executado com prova de trabalho: CRM deal/contact atualizado com score, tier, fonte e timestamp, task no Cli…) e persistir no artefato do squad.
4. Entregar ao critic Critique 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Roteamento executado com prova de trabalho: CRM deal/contact atualizado com score, tier, fonte e timestamp, task no ClickUp criada para SDR com brief completo…
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

- **to:** Pulse
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
