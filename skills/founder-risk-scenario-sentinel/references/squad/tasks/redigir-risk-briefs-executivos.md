---
task: cipher()
responsavel: "Cipher"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Risk & Scenario Brief verificado por Argos + Expert Lens de Oráculo (quando disponível) + audiência-alvo do documento (founder/board/investidores/time interno) + nível de detalhe configurado (executivo sintetizado / técnico completo) + tom do founder (configurado no onboarding"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "direto/consultivo/formal) + restrições de confidencialidade (quais riscos podem ser comunicados a qual audiência)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Executive Risk Communication: { document_type (Founder_Brief/Board_Update/Team_Alert), target_audience, risk_summary_headline (1 frase), top_3_risks_ranked (com materialidade, urgência e janela de resposta), scenario_outlook (Adaptativo/Disruptivo/Bloqueio"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "probabilidade e horizonte), recommended_actions (3 ações com owner e prazo), monitoring_status (o que o Sentinel está vigiando), source_trail (lista de fontes primárias) }"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Todo documento salvo em Notion como draft antes de qualquer envio"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Founder Brief entregue em Slack imediatamente após validação de Argos"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Board/Investor Updates e Team Alerts: L3 obrigatório antes de qualquer envio"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Nexus após Risk & Scenario Brief validado por Argos no ciclo regular. Ativado em modo emergencial por Nexus quando Vela dispara alerta Crítico (Cipher produz Emergency Brief em 30 minutos…"
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

# Redigir Risk Briefs Executivos

**Task ID:** `cipher()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Redigir Risk Briefs Executivos |
| **status** | `pending` |
| **responsible_executor** | Cipher (Cipher — O Redator de Risk Briefs Executivos) |
| **execution_type** | `Hybrid` |
| **input** | 2 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em transformar o mapa técnico de riscos e cenários em comunicações executivas acionáveis calibradas por audiência. Cipher recebe o Risk & Scenario Brief sintetizado por Nexus e produz três formatos distintos: (1) FOUNDER BRIEF — alerta de 1 página com mapa de riscos priorizados, janelas de resposta e 3 ações concretas com prazo e owner; (2) BOARD/INVESTOR RISK UPDATE — memo trimestral com narrativa de riscos relevantes para conselheiros e investidores, com mapeamento de como a gestão está respondendo proativamente (demonstra governança); (3) TEAM ALERT — comunicado interno simplificado para C-level / gerentes afetados contendo apenas o que é acionável para cada área sem expor análise estratégica confidencial. Todo documento gerado por Cipher é 100% source-grounded: cada claim tem link para fonte primária ou referência ao risco ID no Risk Register. NUNCA gera recomendações que excedam o escopo do Risk Brief verificado por Argos.

## Input

- Risk & Scenario Brief verificado por Argos + Expert Lens de Oráculo (quando disponível) + audiência-alvo do documento (founder/board/investidores/time interno) + nível de detalhe configurado (executivo sintetizado / técnico completo) + tom do founder (configurado no onboarding
- direto/consultivo/formal) + restrições de confidencialidade (quais riscos podem ser comunicados a qual audiência)

## Output

- Executive Risk Communication: { document_type (Founder_Brief/Board_Update/Team_Alert), target_audience, risk_summary_headline (1 frase), top_3_risks_ranked (com materialidade, urgência e janela de resposta), scenario_outlook (Adaptativo/Disruptivo/Bloqueio
- probabilidade e horizonte), recommended_actions (3 ações com owner e prazo), monitoring_status (o que o Sentinel está vigiando), source_trail (lista de fontes primárias) }
- Todo documento salvo em Notion como draft antes de qualquer envio
- Founder Brief entregue em Slack imediatamente após validação de Argos
- Board/Investor Updates e Team Alerts: L3 obrigatório antes de qualquer envio

## Trigger

Ativado por Nexus após Risk & Scenario Brief validado por Argos no ciclo regular. Ativado em modo emergencial por Nexus quando Vela dispara alerta Crítico (Cipher produz Emergency Brief em 30 minutos). Ativado diretamente pelo founder via '/risk-brief [audiência] [tom]' para brief ad hoc. BLOQUEADO para envio externo (board, investidores, parceiros) sem aprovação L3 explícita do founder.

## Knowledge base (o que o executor consulta)

- Templates de Risk Brief aprovados pelo founder por audiência (configurados no onboarding)
- Corpus de comunicações anteriores do founder (estilo, vocabulário, nível de detalhe por audiência)
- Histórico de Risk Briefs anteriores para manter consistência de narrativa e mostrar evolução do mapa de riscos ao longo do tempo
- Restrições de confidencialidade configuradas (quais riscos são internos vs
- comunicáveis externamente)
- Risk Register completo para rastreabilidade de claims

## Action Items

1. Confirmar o gatilho e carregar a entrada (Risk & Scenario Brief verificado por Argos + Expert Lens de Oráculo (quando disponível) + audiência-alvo do documento (…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Executive Risk Communication: { document_type (Founder_Brief/Board_Update/Team_Alert), target_audience, risk_summary_he…) e persistir no artefato do squad.
4. Entregar ao critic Argos; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Executive Risk Communication: { document_type (Founder_Brief/Board_Update/Team_Alert), target_audience, risk_summary_headline (1 frase), top_3_risks_ranked (co…
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

- **to:** Argos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
