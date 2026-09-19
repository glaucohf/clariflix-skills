---
task: sentinel()
responsavel: "Sentinel"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados de Google Trends API (palavras-chave do negocio e concorrentes) + Meta Ads Library (monitoramento de criativos de concorrentes) + Google Search Console (impressoes/cliques organicos como proxy de demanda) + Calendario de eventos sazonais do cliente (promocoes, datas comemorativas, lancamentos) + Historico de performance por periodo sazonal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório semanal de inteligência de mercado (tendências de demanda, movimentos de concorrentes, oportunidades de escala identificadas), Alertas de oportunidade (ex: concorrente pausou campanhas = janela de escala com menor CPC), Recomendações de ajuste de budget proativo para próximos 7 dias com justificativa de sinal, Dados de contexto para o orquestrador Orion"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Varredura diária automática as 07h. Alertas em tempo real se variação de tendência > 20% em 24h para keywords prioritárias ou se concorrente direto lançar nova campanha detectada"
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

# Monitorar Sinais De Mercado

**Task ID:** `sentinel()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais De Mercado |
| **status** | `pending` |
| **responsible_executor** | Sentinel (Sentinel — Signal & Intent Monitor) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de monitoramento de sinais de mercado e intenção de compra. Monitora tendências de busca (Google Trends, Search Console), mudanças no landscape competitivo (novos ads de concorrentes via biblioteca de anúncios), sazonalidade de demanda e sinais de intent em tempo real. Alimenta o orquestrador com contexto de mercado para decisões de escala proativa (ex: aumentar budget quando sinal de demanda aumenta antes de evento sazonal).

## Input

- Dados de Google Trends API (palavras-chave do negocio e concorrentes) + Meta Ads Library (monitoramento de criativos de concorrentes) + Google Search Console (impressoes/cliques organicos como proxy de demanda) + Calendario de eventos sazonais do cliente (promocoes, datas comemorativas, lancamentos) + Historico de performance por periodo sazonal

## Output

- Relatório semanal de inteligência de mercado (tendências de demanda, movimentos de concorrentes, oportunidades de escala identificadas), Alertas de oportunidade (ex: concorrente pausou campanhas = janela de escala com menor CPC), Recomendações de ajuste de budget proativo para próximos 7 dias com justificativa de sinal, Dados de contexto para o orquestrador Orion

## Trigger

Varredura diária automática as 07h. Alertas em tempo real se variação de tendência > 20% em 24h para keywords prioritárias ou se concorrente direto lançar nova campanha detectada

## Knowledge base (o que o executor consulta)

- Lista de keywords prioritárias do negócio e concorrentes, Calendário de sazonalidade histórica com impacto em ROAS/CAC, Perfis de concorrentes diretos monitorados, Histórico de performance por contexto de mercado, ICP e mercado-alvo para filtro de relevância de sinais

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados de Google Trends API (palavras-chave do negocio e concorrentes) + Meta Ads Library (monitoramento de criativos de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório semanal de inteligência de mercado (tendências de demanda, movimentos de concorrentes, oportunidades de escal…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório semanal de inteligência de mercado (tendências de demanda, movimentos de concorrentes, oportunidades de escala identificadas), Alertas de oportunidad…
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

- **to:** Aegis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
