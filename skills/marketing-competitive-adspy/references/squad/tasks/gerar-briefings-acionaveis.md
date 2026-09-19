---
task: nexus()
responsavel: "Nexus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Burst Alert de Falcon (campanha nova de concorrente detectada), Pricing Change Alert de Prism (mudança de preço detectada), Category Trend Alert de Volta (convergência de ângulos/formatos/oferta), Ad Intelligence Cards de Cipher (winning ads identificados), itens novos do swipe file de Echo prontos para uso, contexto de campanhas próprias em andamento para calibrar prioridade de reação"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Competitive Brief formatado (o que aconteceu + hipótese + janela de reação + ação sugerida), task no ClickUp criada para o responsável com prioridade e prazo definidos, notificação no Slack no canal #competitive-intel com resumo executivo (3 bullets: o que mudou, por que importa, ação recomendada), Briefing de Criativo em caso de reação urgente (hook sugerido + ângulo recomendado do swipe file + formato prioritário + CTA), todo output pendente gate de Sigma antes de ser entregue ao time"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Qualquer alerta crítico de Falcon (burst de Tier 1), Prism (mudança de preço) ou Volta (Category Trend Alert); Orion eleva prioridade de movimento competitivo para reação imediata; lançamento identif…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sigma 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente e critérios de alerta antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação)"
    - "[ ] HITL: Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fazem sentido para o contexto do setor antes do squad entrar em produção completa (L3, calibração crítica de taxonomia)"
    - "[ ] HITL: Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e decidir sobre reação antes de qualquer briefing ser disparado ao time (L3, irreversível — reação de preço e decisão estratégica)"
    - "[ ] HITL: Aprovação de Category Trend Alert — quando Volta detecta convergência de 3+ concorrentes, o CMO deve validar a hipótese estratégica antes de escalar como diretriz de campanha (L3, decisão estratégica de posicionamento)"
    - "[ ] HITL: Revisão de Competitive Brief de reação urgente — qualquer briefing com prazo de reação de 4h (mudança de Tier 1) deve ser revisado por Head de Marketing antes de ser entregue ao time de criativo (L3, velocidade não elimina o gate humano em movimentos críticos)"
---

# Gerar Briefings Acionáveis

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Briefings Acionáveis |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Alert Dispatcher & Briefing Generator) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Interface entre inteligência detectada e ação do time de marketing. Responsável por transformar alertas de Falcon, Prism e Volta em briefings acionáveis que o time consegue executar sem precisar interpretar dados brutos. Para cada alerta de movimento crítico: (1) Monta o Competitive Brief — o que aconteceu, qual concorrente, qual o movimento específico, qual a hipótese de por que estão fazendo isso, e qual a janela de reação recomendada; (2) Sugere a resposta tática — novo ângulo de teste baseado no swipe file de Echo, ajuste de posicionamento baseado em Prism, criativo de reação específico; (3) Prioriza a resposta — urgência em 4h (mudança de preço de Tier 1), urgência em 24h (novo ângulo escalando), urgência em 72h (tendência de categoria detectada por Volta); (4) Cria tasks automáticas no ClickUp para o time responsável com contexto completo. Nunca envia briefing externo sem aprovação de Sigma.

## Input

- Burst Alert de Falcon (campanha nova de concorrente detectada), Pricing Change Alert de Prism (mudança de preço detectada), Category Trend Alert de Volta (convergência de ângulos/formatos/oferta), Ad Intelligence Cards de Cipher (winning ads identificados), itens novos do swipe file de Echo prontos para uso, contexto de campanhas próprias em andamento para calibrar prioridade de reação

## Output

- Competitive Brief formatado (o que aconteceu + hipótese + janela de reação + ação sugerida), task no ClickUp criada para o responsável com prioridade e prazo definidos, notificação no Slack no canal #competitive-intel com resumo executivo (3 bullets: o que mudou, por que importa, ação recomendada), Briefing de Criativo em caso de reação urgente (hook sugerido + ângulo recomendado do swipe file + formato prioritário + CTA), todo output pendente gate de Sigma antes de ser entregue ao time

## Trigger

Qualquer alerta crítico de Falcon (burst de Tier 1), Prism (mudança de preço) ou Volta (Category Trend Alert); Orion eleva prioridade de movimento competitivo para reação imediata; lançamento identificado de produto ou oferta nova de concorrente Tier 1; CMO solicita briefing competitivo para reunião de planejamento; ciclo semanal de consolidação de movimentos para Competitive Week Review

## Knowledge base (o que o executor consulta)

- Calendário de campanhas e lançamentos próprios da empresa (para calibrar prioridade e conflito de timing de reação), swipe file completo e atualizado de Echo (para sugestão de ângulo na reação), histórico de briefings anteriores com resultado (o que o time executou e qual foi a performance), mapeamento de responsáveis no time de marketing por tipo de reação (quem cuida de ads, quem cuida de landing page, quem cuida de conteúdo orgânico), regras de frequência de alerta por canal (evitar fadiga de notificação)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Burst Alert de Falcon (campanha nova de concorrente detectada), Pricing Change Alert de Prism (mudança de preço detecta…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Competitive Brief formatado (o que aconteceu + hipótese + janela de reação + ação sugerida), task no ClickUp criada par…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Competitive Brief formatado (o que aconteceu + hipótese + janela de reação + ação sugerida), task no ClickUp criada para o responsável com prioridade e prazo d…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sigma 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente…
- [ ] Gate HITL respeitado: Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fa…
- [ ] Gate HITL respeitado: Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente e critérios de aler… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fazem sentido para o c… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e decidir sobre reação a… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação de Category Trend Alert — quando Volta detecta convergência de 3+ concorrentes, o CMO deve validar a hipótese estratégica antes de escalar como diret… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de Competitive Brief de reação urgente — qualquer briefing com prazo de reação de 4h (mudança de Tier 1) deve ser revisado por Head de Marketing antes… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de itens do swipe file antes de publicação no ClickUp — revisão quinzenal pelo Head de Marketing dos itens aprovados por Sigma para garantir alinhame… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisão mensal do Competitive Intelligence Baseline — CMO e Head de Vendas revisam com Orion quais concorrentes devem subir ou descer de tier, se novos concorr… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Quando Sigma retorna BLOCKED em gate de compliance (risco de plágio ou evidência muito fraca) — revisão humana obrigatória antes de reprocessar o item ou desca… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Sigma
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
