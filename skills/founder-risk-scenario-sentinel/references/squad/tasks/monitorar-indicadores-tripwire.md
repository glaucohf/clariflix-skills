---
task: vela()
responsavel: "Vela"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Risk Scenario Matrix de Chronos com early-warning indicators por cenário + Risk Register do founder com status de cada risco (Monitorando/Ativo/Materializado) + thresholds de alerta configurados por risco (definidos no Review Gate com o founder) + integrações com fontes de dados dos indicadores (feeds do DOU, APIs de câmbio/Selic, Google Alerts configurados, RSS de agências reguladoras)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Configuração inicial: mapa de founder aprovado no onboarding com todos os risks, indicadores e thresholds"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alert Feed estruturado: { alert_id, risk_id, risk_name, indicator_name, current_value, threshold_value, gap_percentage, alert_level (Informativo/Atencao/Critico), evidence_url, summary_plain_language (100 palavras), recommended_immediate_action, triggers_new_deep_dive (boolean) }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Dashboard de Risk Register com status de todos os riscos ativos"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório mensal de performance de monitoramento: quantos alertas gerados, quantos se materializaram, acurácia de early-warning por tipo de risco"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Alertas Críticos entregues via Slack com menção direta ao founder"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Configurada automaticamente por Nexus ao final de cada Risk & Scenario Brief aceito pelo founder. Crons escalonados por frequência de indicador: diário (câmbio, Selic, Google Alerts), semanal (pipeli…"
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

# Monitorar Indicadores Tripwire

**Task ID:** `vela()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Indicadores Tripwire |
| **status** | `pending` |
| **responsible_executor** | Vela (Vela — A Guardiã de Tripwires) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de monitoramento contínuo pós-identificação de risco. Após o founder receber o Risk & Scenario Brief e decidir como lidar com cada risco (monitorar, adaptar, ignorar, escalonar), Vela configura os tripwires — indicadores de early-warning específicos para cada risco ativo no Risk Register do founder. Opera em modo contínuo e escalonado: verifica diariamente os sinais de alta frequência, semanalmente os sinais de frequência média, e quinzenalmente os sinais de baixa frequência. Quando um indicador cruza o threshold configurado (ex: proposta regulatória X avança de consulta pública para votação em comissão, câmbio cruza R$5,80, governo anuncia mudança em política setorial), Vela aciona alerta escalonado: Informativo (sinal observado, fora do range normal), Atenção (tendência de materialização acelera), Crítico (risco em materialização — janela de resposta ativa). Para alertas Críticos, Vela dispara Nexus automaticamente para novo ciclo Deep Dive emergencial. Vela é também o sistema de aprendizado do squad: documenta todos os riscos com status de materialização e alimenta a calibração de probabilidades de Chronos.

## Input

- Risk Scenario Matrix de Chronos com early-warning indicators por cenário + Risk Register do founder com status de cada risco (Monitorando/Ativo/Materializado) + thresholds de alerta configurados por risco (definidos no Review Gate com o founder) + integrações com fontes de dados dos indicadores (feeds do DOU, APIs de câmbio/Selic, Google Alerts configurados, RSS de agências reguladoras)
- Configuração inicial: mapa de founder aprovado no onboarding com todos os risks, indicadores e thresholds

## Output

- Alert Feed estruturado: { alert_id, risk_id, risk_name, indicator_name, current_value, threshold_value, gap_percentage, alert_level (Informativo/Atencao/Critico), evidence_url, summary_plain_language (100 palavras), recommended_immediate_action, triggers_new_deep_dive (boolean) }
- Dashboard de Risk Register com status de todos os riscos ativos
- Relatório mensal de performance de monitoramento: quantos alertas gerados, quantos se materializaram, acurácia de early-warning por tipo de risco
- Alertas Críticos entregues via Slack com menção direta ao founder

## Trigger

Configurada automaticamente por Nexus ao final de cada Risk & Scenario Brief aceito pelo founder. Crons escalonados por frequência de indicador: diário (câmbio, Selic, Google Alerts), semanal (pipeline regulatório, movimentos políticos), quinzenal (sinais geopolíticos de médio prazo). Dispara Nexus automaticamente quando alert_level = Crítico. Dispara HITL Gate L3 quando risco Crítico em materialização exige resposta com impacto financeiro ou operacional do founder.

## Knowledge base (o que o executor consulta)

- Risk Register completo do cliente com histórico de todos os riscos identificados, seus thresholds e status de materialização
- Configurações de early-warning indicators por categoria de risco (mapa de quais sinais observáveis precedem materializações históricas)
- Histórico de performance de alertas anteriores (para calibração de thresholds
- evitar ruído excessivo ou lacunas)
- Feeds em tempo real: API do BACEN (Selic, câmbio), sistemas de acompanhamento do DOU e portais de agências reguladoras, Google Alerts configurados com termos setoriais críticos, LinkedIn e Crunchbase para sinais de concorrentes correlacionados a riscos regulatórios

## Action Items

1. Confirmar o gatilho e carregar a entrada (Risk Scenario Matrix de Chronos com early-warning indicators por cenário + Risk Register do founder com status de cada…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alert Feed estruturado: { alert_id, risk_id, risk_name, indicator_name, current_value, threshold_value, gap_percentage,…) e persistir no artefato do squad.
4. Entregar ao critic Argos; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alert Feed estruturado: { alert_id, risk_id, risk_name, indicator_name, current_value, threshold_value, gap_percentage, alert_level (Informativo/Atencao/Critic…
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

- **to:** Oráculo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
