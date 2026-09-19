---
task: sage()
responsavel: "Sage"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Signal Feed histórico de Pulse (últimos 90 dias), status de oportunidades no CRM com origem rastreada, playbooks disparados por Nexus com resultado, dados de campanha de ads (CTR, conversão, CPL por segmento de sinal), feedback qualitativo do time de vendas sobre qualidade das contas Hot"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dashboard semanal de Demand Sensing (lead-time médio, win-rate por tipo de sinal, pipeline atribuído ao radar), ROI Report por categoria de sinal (qual converte mais, qual tem melhor CAC), Anomaly Alert quando métrica crítica desvia > 20% da média móvel, Recalibration Flag quando baseline de sinal precisa de ajuste, relatório mensal de antecipação (quantas semanas antes o time chegou vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "quando o deal foi fechado)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo semanal automático de consolidação; deal fechado no CRM com origem em conta sinalizada (trigger de atribuição); anomalia detectada em métrica de funil; Radar solicita análise de performance de…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sigma 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)"
    - "[ ] HITL: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)"
    - "[ ] HITL: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)"
    - "[ ] HITL: Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)"
    - "[ ] HITL: Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)"
---

# Calcular ROI Sinal

**Task ID:** `sage()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular ROI Sinal |
| **status** | `pending` |
| **responsible_executor** | Sage (Sage — Analytics & Attribution Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Consolida a performance do radar e atribui pipeline ao sinal que originou cada oportunidade. Calcula o ROI por categoria de sinal (qual tipo de sinal converte mais em oportunidade e receita), detecta anomalias no funil (ex: funding playbook está gerando meetings mas não oportunidades — sinal de problema de qualificação), e produz o dashboard semanal com as métricas de antecipação. Responsável por detectar quando o baseline de ruído de uma categoria de sinal precisa ser recalibrado (sinal que antes era Hot agora é commodity).

## Input

- Signal Feed histórico de Pulse (últimos 90 dias), status de oportunidades no CRM com origem rastreada, playbooks disparados por Nexus com resultado, dados de campanha de ads (CTR, conversão, CPL por segmento de sinal), feedback qualitativo do time de vendas sobre qualidade das contas Hot

## Output

- Dashboard semanal de Demand Sensing (lead-time médio, win-rate por tipo de sinal, pipeline atribuído ao radar), ROI Report por categoria de sinal (qual converte mais, qual tem melhor CAC), Anomaly Alert quando métrica crítica desvia > 20% da média móvel, Recalibration Flag quando baseline de sinal precisa de ajuste, relatório mensal de antecipação (quantas semanas antes o time chegou vs
- quando o deal foi fechado)

## Trigger

Ciclo semanal automático de consolidação; deal fechado no CRM com origem em conta sinalizada (trigger de atribuição); anomalia detectada em métrica de funil; Radar solicita análise de performance de categoria específica; revisão mensal de calibração de thresholds

## Knowledge base (o que o executor consulta)

- Histórico completo de sinais detectados com timestamps, dados de CRM com stage, origem e resultado de todas as oportunidades, mapping de playbooks disparados por conta e resultado, benchmark de win-rate por tipo de sinal (construído ao longo do tempo), modelos de atribuição multi-touch para separar contribuição do sinal de outros touchpoints

## Action Items

1. Confirmar o gatilho e carregar a entrada (Signal Feed histórico de Pulse (últimos 90 dias), status de oportunidades no CRM com origem rastreada, playbooks dispar…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dashboard semanal de Demand Sensing (lead-time médio, win-rate por tipo de sinal, pipeline atribuído ao radar), ROI Rep…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dashboard semanal de Demand Sensing (lead-time médio, win-rate por tipo de sinal, pipeline atribuído ao radar), ROI Report por categoria de sinal (qual convert…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sigma 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o…
- [ ] Gate HITL respeitado: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cad…
- [ ] Gate HITL respeitado: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squ… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprova… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3) | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Bolt
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
