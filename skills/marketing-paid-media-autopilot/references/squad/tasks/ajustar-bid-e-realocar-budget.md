---
task: midas()
responsavel: "Midas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de anomalias do Argos + Decisão de ação do orquestrador Orion (tipo de ajuste, magnitude, campanha/ad set alvo) + Guardrails de banda (% máximo de realocação por ciclo, teto de CPA, floor de ROAS para escala) + Saldo de budget disponível por campanha"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Confirmação de execução das ações (API response + timestamp), Log de mudanças (antes/depois por métrica), Artefato ClickUp task atualizado com prova de trabalho, Alerta Slack/WhatsApp para humano se ação for L3 (aguarda aprovação antes de executar)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo orquestrador Orion após validação do relatório do Argos. Para ações L3: aguarda aprovação explícita do humano responsável via canal configurado (Slack/WhatsApp) antes de qualquer execuç…"
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

# Ajustar Bid E Realocar Budget

**Task ID:** `midas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Ajustar Bid E Realocar Budget |
| **status** | `pending` |
| **responsible_executor** | Midas (Midas — Bid & Budget Optimizer) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de execução de ajustes de bid strategy e realocação de budget dentro das bandas de autonomia pre-aprovadas (L2: realoca até X% do budget sem aprovação; L3: realocações acima do teto ou mudanças de estrutura de campanha requerem gate humano). Executa via API as ações aprovadas pelo orquestrador Orion. Registra toda ação no ClickUp como prova de trabalho auditável.

## Input

- Relatório de anomalias do Argos + Decisão de ação do orquestrador Orion (tipo de ajuste, magnitude, campanha/ad set alvo) + Guardrails de banda (% máximo de realocação por ciclo, teto de CPA, floor de ROAS para escala) + Saldo de budget disponível por campanha

## Output

- Confirmação de execução das ações (API response + timestamp), Log de mudanças (antes/depois por métrica), Artefato ClickUp task atualizado com prova de trabalho, Alerta Slack/WhatsApp para humano se ação for L3 (aguarda aprovação antes de executar)

## Trigger

Acionado pelo orquestrador Orion após validação do relatório do Argos. Para ações L3: aguarda aprovação explícita do humano responsável via canal configurado (Slack/WhatsApp) antes de qualquer execução

## Knowledge base (o que o executor consulta)

- Guardrails financeiros e bandas de autonomia aprovados, Histórico de ajustes anteriores e seus impactos (closed-loop learning), Regras de bid strategy por objetivo de campanha (max conversions, target CPA, target ROAS), Limites de API por plataforma (rate limits, políticas de mudança mínima)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Relatório de anomalias do Argos + Decisão de ação do orquestrador Orion (tipo de ajuste, magnitude, campanha/ad set alv…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Confirmação de execução das ações (API response + timestamp), Log de mudanças (antes/depois por métrica), Artefato Clic…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Confirmação de execução das ações (API response + timestamp), Log de mudanças (antes/depois por métrica), Artefato ClickUp task atualizado com prova de trabalh…
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

- **to:** Prism
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
