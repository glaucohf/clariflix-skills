---
task: cassandra()
responsavel: "Cassandra"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Árvore de Premissas da decisão gerada por Atlas + tipo de decisão + setor e contexto competitivo + janela temporal da aposta + dados históricos relevantes de mercado (via deep research se necessário) + probabilidades prévias do founder sobre o futuro (elicitadas no intake)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Scenario Matrix estruturada: { scenario_id, label (Otimista/Base/Pessimista/Wild-Card), narrative (300 palavras), driving_forces[], early_warning_indicators[], probability_estimate (%), impact_on_decision_metric, assumptions_invalidated[], assumptions_confirmed[] }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Mínimo 3 cenários + 1 Wild Card opcional"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório de premissas mais sensíveis a variação de cenário"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Atlas roteia após aprovação do intake para execução paralela com Brutus e Chisel. Também ativado quando founder quer atualizar cenários após novo sinal de mercado (comando '/update-scenarios [novo si…"
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

# Mapear Espaço De Futuros

**Task ID:** `cassandra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Mapear Espaço De Futuros |
| **status** | `pending` |
| **responsible_executor** | Cassandra (Cassandra — A Arquiteta de Futuros) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em construção de cenários plausíveis de futuro. Não prevê o futuro — mapeia o espaço de futuros possíveis e atribui probabilidades bayesianas iniciais a cada um. Para cada decisão, gera obrigatoriamente 3 cenários estruturados: Otimista (tailwinds se materializam, premissas se confirmam), Base (regressão à média com choques normais), Pessimista (premissas críticas falham, adversários reagem bem). Cada cenário é construído com: horizonte temporal (6/12/24/36 meses), variáveis motrizes (3-5 forças que determinam qual cenário se materializa), indicadores de early-warning (sinais observáveis que confirmam ou invalidam o cenário), impacto quantificado na métrica-alvo do founder, e probabilidade subjetiva fundamentada em evidências. Também executa análise de 'mundos possíveis' — para cada premissa crítica da Árvore, o que muda nos cenários se a premissa for inválida.

## Input

- Árvore de Premissas da decisão gerada por Atlas + tipo de decisão + setor e contexto competitivo + janela temporal da aposta + dados históricos relevantes de mercado (via deep research se necessário) + probabilidades prévias do founder sobre o futuro (elicitadas no intake)

## Output

- Scenario Matrix estruturada: { scenario_id, label (Otimista/Base/Pessimista/Wild-Card), narrative (300 palavras), driving_forces[], early_warning_indicators[], probability_estimate (%), impact_on_decision_metric, assumptions_invalidated[], assumptions_confirmed[] }
- Mínimo 3 cenários + 1 Wild Card opcional
- Relatório de premissas mais sensíveis a variação de cenário

## Trigger

Atlas roteia após aprovação do intake para execução paralela com Brutus e Chisel. Também ativado quando founder quer atualizar cenários após novo sinal de mercado (comando '/update-scenarios [novo sinal]'). Re-ativado por Atlas se Ajax identificar lacuna de cobertura de cenários.

## Knowledge base (o que o executor consulta)

- Dados históricos de mercado do setor do cliente (indexados no Vector DB)
- Relatórios de tendências macro (OCDE, WEF, McKinsey Global Institute)
- Metodologias de cenários: Shell Scenarios, GBN, PESTEL, Cone of Plausibility
- Histórico de apostas e decisões anteriores do founder com outcomes documentados
- Sinais de mercado recentes coletados por integrações (Slack, Gmail, RSS feeds setoriais)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Árvore de Premissas da decisão gerada por Atlas + tipo de decisão + setor e contexto competitivo + janela temporal da a…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Scenario Matrix estruturada: { scenario_id, label (Otimista/Base/Pessimista/Wild-Card), narrative (300 palavras), drivi…) e persistir no artefato do squad.
4. Entregar ao critic Ajax; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Scenario Matrix estruturada: { scenario_id, label (Otimista/Base/Pessimista/Wild-Card), narrative (300 palavras), driving_forces[], early_warning_indicators[],…
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

- **to:** Brutus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
