---
task: tripwire()
responsavel: "Tripwire"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Early-warning indicators do Scenario Matrix de Cassandra + premissas críticas classificadas pelo Chisel + decisão tomada pelo founder com cenário escolhido + thresholds de alerta configurados (quanto desvio do indicador dispara alertas de cada nível) + integrações com fontes de dados dos indicadores"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dashboard de monitoramento de decisão: { decision_id, chosen_scenario, indicator_name, current_value, expected_range, status (On-Track/Diverging/Off-Track), last_updated }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alertas escalonados: Informativo (sinal fora do range esperado), Atenção (tendência de divergência), Crítico (cenário claramente divergindo"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "recomenda revisão da decisão)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Relatório mensal de calibração: quais cenários se materializaram vs"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "previstos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Configurado automaticamente por Atlas ao final de cada Wargaming concluído com decisão tomada. Cron configurável por tipo de indicador (diário para sinais de mercado, semanal para macro, mensal para…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Ajax antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificação de stakes, estimativa de custo de tokens). Para decisões classificadas como Alto (R$100k-500k) ou Crítico (R$500k+), aprovação explícita do founder é obrigatória antes de disparar workers. Inclui confirmação do escopo, dos concorrentes a simular e do nível de profundidade desejado."
    - "[ ] HITL: PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e founder recebe notificação urgente com evidências contrárias. O founder deve decidir: (a) revisar a tese antes de prosseguir, (b) validar a premissa com dado adicional, ou (c) aceitar o risco explicitamente e autorizar o prosseguimento. Sem aprovação explícita, Atlas não gera recomendação de GO."
    - "[ ] HITL: PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloqueia automaticamente a recomendação de GO e escalona para o founder. O relatório apresenta: narrativa do caminho de falha, premissas que o geram e opções de mitigação. O founder deve responder com ação concreta (mitigar, aceitar, desistir) antes de qualquer recomendação final."
    - "[ ] HITL: BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento gerado vai primeiro para Notion como draft. Somente após founder marcar como aprovado o envio é permitido. Este gate é inviolável e não pode ser desabilitado."
    - "[ ] HITL: WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades financeiras ou decisões internas), o output é marcado como confidencial e apresentado ao founder antes de ser incluído em qualquer documento compartilhável. Dados de origem não-verificada são explicitamente rotulados."
---

# Monitorar Indicadores De Alerta

**Task ID:** `tripwire()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Indicadores De Alerta |
| **status** | `pending` |
| **responsible_executor** | Tripwire (Tripwire — O Guardião de Alertas) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de monitoramento pós-decisão: após o founder tomar uma decisão estratégica com base no Wargaming Report, Tripwire configura e monitora os indicadores de early-warning definidos por Cassandra nos cenários. Opera em modo contínuo: verifica periodicamente se os sinais observáveis estão confirmando o cenário escolhido ou apontando para divergência. Quando sinal de divergência detectado, aciona alerta escalonado: primeiro notificação informativa, depois alerta de revisão, depois HITL gate para reavaliação da decisão. Também monitora os tripwires de premissas — quando premissa anteriormente Sólida começa a mostrar sinais de fragilização, alerta antes que vire Inválida. É o mecanismo de aprendizado do squad: documenta quais cenários se materializaram e calibra probabilidades futuras.

## Input

- Early-warning indicators do Scenario Matrix de Cassandra + premissas críticas classificadas pelo Chisel + decisão tomada pelo founder com cenário escolhido + thresholds de alerta configurados (quanto desvio do indicador dispara alertas de cada nível) + integrações com fontes de dados dos indicadores

## Output

- Dashboard de monitoramento de decisão: { decision_id, chosen_scenario, indicator_name, current_value, expected_range, status (On-Track/Diverging/Off-Track), last_updated }
- Alertas escalonados: Informativo (sinal fora do range esperado), Atenção (tendência de divergência), Crítico (cenário claramente divergindo
- recomenda revisão da decisão)
- Relatório mensal de calibração: quais cenários se materializaram vs
- previstos

## Trigger

Configurado automaticamente por Atlas ao final de cada Wargaming concluído com decisão tomada. Cron configurável por tipo de indicador (diário para sinais de mercado, semanal para macro, mensal para regulatório). Disparado manualmente pelo founder via '/check-tripwires [decisão_id]'.

## Knowledge base (o que o executor consulta)

- Wargaming Reports históricos com cenários, premissas e indicadores definidos
- Dados em tempo real dos indicadores via integrações configuradas (APIs financeiras, Google Alerts, dashboards de métricas do cliente)
- Histórico de materializações passadas para calibração bayesiana
- Threshold configurations por decisão e por founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Early-warning indicators do Scenario Matrix de Cassandra + premissas críticas classificadas pelo Chisel + decisão tomad…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dashboard de monitoramento de decisão: { decision_id, chosen_scenario, indicator_name, current_value, expected_range, s…) e persistir no artefato do squad.
4. Entregar ao critic Ajax; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dashboard de monitoramento de decisão: { decision_id, chosen_scenario, indicator_name, current_value, expected_range, status (On-Track/Diverging/Off-Track), la…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Ajax registrado
- [ ] Gate HITL respeitado: INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Pr…
- [ ] Gate HITL respeitado: PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o war…
- [ ] Gate HITL respeitado: PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificaç… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e found… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloque… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades fi… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — DECISÃO DE MONITORAMENTO CONTÍNUO (L2): Após wargaming concluído, Atlas apresenta lista de tripwires sugeridos para aprovação do founder antes de ativar Tripwi… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Ajax | BLOQUEIA entrega |

## Handoff

- **to:** Ajax
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
