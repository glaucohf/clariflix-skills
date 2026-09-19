---
task: chronos()
responsavel: "Chronos"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Regulatory Risk Reports de Lexis (riscos identificados no ciclo) + Macro-Geo Risk Reports de Gaia (riscos identificados no ciclo) + perfil do modelo de negócio do cliente (linhas de produto, estrutura de receita, % de receita por segmento/mercado) + histórico de cenários anteriores do cliente com outcomes documentados (para calibração de probabilidades)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Modo on-demand: conjunto específico de riscos para simular por pedido do founder"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Risk Scenario Matrix estruturada: { scenario_id, scenario_label (Adaptativo/Disruptivo/Bloqueio_Total), trigger_risks (IDs de Lexis e Gaia que geram este cenário), narrative_plain_language (300 palavras em português executivo), probability_estimate (%), materialization_horizon (dias), revenue_impact_range_BRL, ebitda_impact_range_BRL, capital_at_risk_BRL, response_window_days, adaptation_cost_estimate_BRL, founder_actions_by_scenario (3-5 ações com owner e prazo), second_order_risks[] }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Cross-risk analysis identificando combinações de riscos que criam cenários de segunda ordem"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Recomendação de qual cenário deve ser tratado como cenário-base para planejamento"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Nexus após receber outputs de Lexis e Gaia no ciclo semanal/quinzenal. Ativado por Nexus no Pre-Decision Risk Scan quando founder está prestes a tomar decisão estratégica específica. Re-a…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argos antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao founder quando o risco é classificado como Crítico (impacto estimado > R$200k ou impacto em licença/operação). O founder valida o escopo da investigação, confirma as agências e mercados a investigar, e aprova o nível de profundidade (scan rápido vs. deep dive). Para riscos Médios e Baixos, Nexus opera de forma autônoma sem gate obrigatório."
    - "[ ] HITL: RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da janela de resposta), o squad pausa toda recomendação de ação com impacto financeiro ou operacional e escalona para o founder com urgência máxima. O founder recebe: (a) o Evidence Report do Argos com fontes primárias que confirmam a materialização, (b) os cenários ativos de Chronos com janelas de resposta restantes, (c) as 3 ações prioritárias de Cipher. O founder deve responder com decisão explícita antes de qualquer ação ser executada."
    - "[ ] HITL: PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi invalidada por nova evidência (ex: a norma que estava em consulta pública foi arquivada, alterando radicalmente o cenário regulatório), o squad notifica o founder com o impacto na matrix de cenários antes de atualizar o Risk Register. O founder confirma a revisão ou solicita novo ciclo de análise."
    - "[ ] HITL: BOARD/INVESTOR RISK UPDATE E COMUNICAÇÕES EXTERNAS (L3): Cipher nunca envia qualquer documento para audiência externa (board, conselheiros, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento produzido para audiência externa vai primeiro para Notion como draft com notificação Slack ao founder. Apenas após founder aprovar explicitamente (clique no botão 'Aprovar para envio' ou mensagem de aprovação no Slack) o envio é autorizado. Este gate é inviolável."
    - "[ ] HITL: CONFIGURAÇÃO DO ORÁCULO E CORPUS DO FOUNDER (L2): A configuração inicial do corpus do Oráculo (quais documentos, transcrições e decisões do founder são ingeridas) requer aprovação explícita item a item pelo founder. O founder define o que entra no corpus (controle de privacidade sobre decisões sensíveis) e o que fica fora. Atualizações mensais automáticas do corpus precisam de revisão semestral do founder para remoção de decisões desatualizadas."
---

# Analisar Riscos Estratégicos

**Task ID:** `chronos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Riscos Estratégicos |
| **status** | `pending` |
| **responsible_executor** | Chronos (Chronos — O Arquiteto de Cenários de Risco) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em transformar os sinais brutos de Lexis e Gaia em cenários estruturados de impacto para o negócio específico do founder. Chronos é o elo entre a inteligência de risco e a decisão estratégica: traduz 'houve mudança regulatória X e sinal macro Y' em 'para o seu negócio, existem três futuros possíveis nos próximos 6 meses, com estas probabilidades, estes impactos em receita e operação, e estas janelas de resposta'. Opera exclusivamente com três cenários por ciclo: ADAPTATIVO (o ambiente muda mas o negócio consegue se adaptar dentro da janela disponível com custo conhecido), DISRUPTIVO (a mudança exige pivô significativo no modelo de negócio — produto, pricing, canal ou regulatório), BLOQUEIO TOTAL (a materialização do risco inviabiliza a linha de produto ou mercado específico). Para cada cenário: probabilidade bayesiana inicial, horizonte de materialização, impacto quantificado em receita/EBITDA/capital, janela de resposta disponível antes de fechamento de opção, custo de adaptação estimado, e 3-5 ações concretas do founder para cada cenário. Chronos também identifica os 'cruzamentos de risco' — quando dois sinais independentes de Lexis e Gaia se combinam e criam um risco de segunda ordem não óbvio.

## Input

- Regulatory Risk Reports de Lexis (riscos identificados no ciclo) + Macro-Geo Risk Reports de Gaia (riscos identificados no ciclo) + perfil do modelo de negócio do cliente (linhas de produto, estrutura de receita, % de receita por segmento/mercado) + histórico de cenários anteriores do cliente com outcomes documentados (para calibração de probabilidades)
- Modo on-demand: conjunto específico de riscos para simular por pedido do founder

## Output

- Risk Scenario Matrix estruturada: { scenario_id, scenario_label (Adaptativo/Disruptivo/Bloqueio_Total), trigger_risks (IDs de Lexis e Gaia que geram este cenário), narrative_plain_language (300 palavras em português executivo), probability_estimate (%), materialization_horizon (dias), revenue_impact_range_BRL, ebitda_impact_range_BRL, capital_at_risk_BRL, response_window_days, adaptation_cost_estimate_BRL, founder_actions_by_scenario (3-5 ações com owner e prazo), second_order_risks[] }
- Cross-risk analysis identificando combinações de riscos que criam cenários de segunda ordem
- Recomendação de qual cenário deve ser tratado como cenário-base para planejamento

## Trigger

Ativado por Nexus após receber outputs de Lexis e Gaia no ciclo semanal/quinzenal. Ativado por Nexus no Pre-Decision Risk Scan quando founder está prestes a tomar decisão estratégica específica. Re-ativado quando Vela (Alert & Tripwire) sinaliza que um indicador de early-warning cruzou o threshold — Chronos recalcula probabilidades dos cenários com base no novo sinal. Ativado diretamente pelo founder via '/risk-scenarios [conjunto de riscos]' para simulação ad hoc.

## Knowledge base (o que o executor consulta)

- Perfil financeiro detalhado do modelo de negócio do cliente (P&L simplificado, principais drivers de receita e custo, alavancagem operacional e financeira)
- Histórico de cenários gerados para o cliente com outcomes reais (para calibração bayesiana progressiva)
- Metodologias de construção de cenários aplicadas a contextos de risco: PESTEL, STEEP, análise de sensibilidade, Monte Carlo simplificado
- Risk Registers históricos do cliente com materialização ou não de riscos anteriores
- Benchmarks setoriais de impacto de eventos regulatórios e macro similares em empresas comparáveis

## Action Items

1. Confirmar o gatilho e carregar a entrada (Regulatory Risk Reports de Lexis (riscos identificados no ciclo) + Macro-Geo Risk Reports de Gaia (riscos identificados…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Risk Scenario Matrix estruturada: { scenario_id, scenario_label (Adaptativo/Disruptivo/Bloqueio_Total), trigger_risks (…) e persistir no artefato do squad.
4. Entregar ao critic Argos; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Risk Scenario Matrix estruturada: { scenario_id, scenario_label (Adaptativo/Disruptivo/Bloqueio_Total), trigger_risks (IDs de Lexis e Gaia que geram este cenár…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argos registrado
- [ ] Gate HITL respeitado: INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao foun…
- [ ] Gate HITL respeitado: RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da…
- [ ] Gate HITL respeitado: PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi i…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao founder quando o risco é… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da janela de resposta),… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi invalidada por nova e… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — BOARD/INVESTOR RISK UPDATE E COMUNICAÇÕES EXTERNAS (L3): Cipher nunca envia qualquer documento para audiência externa (board, conselheiros, investidores, parce… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — CONFIGURAÇÃO DO ORÁCULO E CORPUS DO FOUNDER (L2): A configuração inicial do corpus do Oráculo (quais documentos, transcrições e decisões do founder são ingerid… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — AJUSTE DE THRESHOLDS DE ALERTA (L2): Os thresholds de early-warning de Vela (o que configura Informativo vs. Atenção vs. Crítico para cada indicador) são confi… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argos | BLOQUEIA entrega |

## Handoff

- **to:** Vela
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
