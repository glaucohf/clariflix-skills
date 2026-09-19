---
task: gaia()
responsavel: "Gaia"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Perfil do modelo de negócio do cliente (estrutura de receita, principais fornecedores e suas origens geográficas, mercados de atuação e expansão, estrutura de capital e exposição cambial) + lista de países e regiões estratégicos para o negócio + thresholds de materialidade configurados pelo founder (ex: variação de câmbio > X% é material, Selic acima de Y% impacta CAC)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Modo on-demand: pergunta específica do founder sobre evento macro ou geopolítico específico"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Macro-Geo Risk Report estruturado: { risk_id, risk_category (Macro_Domestico/Macro_Internacional/Geopolitico_Estrategico), event_description, geographic_scope, probability_30d/90d/180d (%), estimated_financial_impact_BRL_range, business_areas_affected[], sensitivity_analysis (como o impacto varia com a intensidade do evento), early_warning_indicators (3-5 sinais observáveis que indicam que o risco está se materializando), recommended_hedge_or_adaptation[], urgency_flag }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Digest quinzenal consolidado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alertas imediatos para eventos com probability_30d >= 60% e impacto estimado > R$100k"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron quinzenal para varredura de sinais macro e geopolíticos. Cron semanal para monitoramento de indicadores de alta frequência (câmbio, Selic, spreads de crédito, VIX equivalente BR). Ativado por Ne…"
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

# Estimar Impacto Financeiro

**Task ID:** `gaia()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Estimar Impacto Financeiro |
| **status** | `pending` |
| **responsible_executor** | Gaia (Gaia — O Radar Macro-Geopolítico) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em inteligência macroeconômica e geopolítica aplicada ao modelo de negócio do founder. Gaia não produz análise de conjuntura genérica — produz mapa de impacto específico: 'o que este movimento macro/geopolítico significa para o seu modelo de receita, seus fornecedores e sua estrutura de capital?'. Opera em três camadas simultâneas: (1) MACRO DOMÉSTICO — monitoramento de Selic, câmbio, inflação, crédito, ciclos eleitorais e policy shifts com impacto direto em custo de capital, poder de compra do cliente-alvo e ambiente regulatório (governos mudam regulação); (2) MACRO INTERNACIONAL — reconfiguração de cadeias de suprimentos, tarifas comerciais, sanções econômicas, fluxos de capital e FDI que afetam fornecedores ou mercados de expansão do cliente; (3) GEOPOLÍTICA ESTRATÉGICA — tensões que afetam infra de tecnologia (cloud, semicondutores, dados), acordos comerciais em negociação com impacto setorial, riscos de soberania de dados, movimentos de nearshoring/friendshoring que criam ou destroem vantagens competitivas regionais. Para cada vetor, Gaia estima a probabilidade de materialização em 3 horizontes (30/90/180 dias) e calcula o impacto financeiro estimado no modelo do cliente com cálculo de sensibilidade.

## Input

- Perfil do modelo de negócio do cliente (estrutura de receita, principais fornecedores e suas origens geográficas, mercados de atuação e expansão, estrutura de capital e exposição cambial) + lista de países e regiões estratégicos para o negócio + thresholds de materialidade configurados pelo founder (ex: variação de câmbio > X% é material, Selic acima de Y% impacta CAC)
- Modo on-demand: pergunta específica do founder sobre evento macro ou geopolítico específico

## Output

- Macro-Geo Risk Report estruturado: { risk_id, risk_category (Macro_Domestico/Macro_Internacional/Geopolitico_Estrategico), event_description, geographic_scope, probability_30d/90d/180d (%), estimated_financial_impact_BRL_range, business_areas_affected[], sensitivity_analysis (como o impacto varia com a intensidade do evento), early_warning_indicators (3-5 sinais observáveis que indicam que o risco está se materializando), recommended_hedge_or_adaptation[], urgency_flag }
- Digest quinzenal consolidado
- Alertas imediatos para eventos com probability_30d >= 60% e impacto estimado > R$100k

## Trigger

Cron quinzenal para varredura de sinais macro e geopolíticos. Cron semanal para monitoramento de indicadores de alta frequência (câmbio, Selic, spreads de crédito, VIX equivalente BR). Ativado por Nexus no Deep Dive quando founder submete input com tema macro ou geopolítico. Ativado por Nexus quando Lexis identifica mudança regulatória possivelmente motivada por pressão política ou macroeconômica (sinais correlacionados). Ativado diretamente pelo founder via '/risk-macro [evento ou pergunta]'.

## Knowledge base (o que o executor consulta)

- Perfil detalhado do modelo de negócio do cliente com mapa de exposição (configurado no onboarding): principais fornecedores e origens geográficas, estrutura de custo e % expostos a câmbio/juros, mercados de receita e sua correlação com ciclo econômico, estrutura de capital e covenants relevantes
- Histórico macroeconômico dos últimos 5 anos do Brasil com correlação com desempenho setorial
- Calendário de eventos macro (reuniões do COPOM, divulgações de IPCA, reuniões do Fed, eleições relevantes nos próximos 18 meses)
- Fontes primárias: BACEN, IBGE, FMI, BIS, relatórios do Tesouro Nacional, publicações de think tanks geopolíticos (CEBRI, CFR, ECFR, Chatham House)
- Mapa de correlação histórica entre eventos geopolíticos e impactos setoriais do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Perfil do modelo de negócio do cliente (estrutura de receita, principais fornecedores e suas origens geográficas, merca…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Macro-Geo Risk Report estruturado: { risk_id, risk_category (Macro_Domestico/Macro_Internacional/Geopolitico_Estrategic…) e persistir no artefato do squad.
4. Entregar ao critic Argos; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Macro-Geo Risk Report estruturado: { risk_id, risk_category (Macro_Domestico/Macro_Internacional/Geopolitico_Estrategico), event_description, geographic_scope,…
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

- **to:** Chronos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
