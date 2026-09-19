---
task: atlasPipeline()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Wargaming Report Completo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "documento estratégico entregue em Notion e Slack contendo: (1) Decision Brief com contexto, stakes, Árvore de Premissas completa e classificação de cada premissa (Sólida/Frágil/Inválida)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Scenario Matrix com 3+ cenários estruturados"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "narrativa, driving forces, early-warning indicators, probabilidades bayesianas e impacto quantificado por cenário"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Adversarial Playbook por concorrente"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "reações simuladas em 30/90/180 dias, probabilidades, vulnerabilidades exploradas e contra-jogadas do founder"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Atlas é o orquestrador principal do squad e persona de um estrategista sênior com background em consultoria estratégica e teoria dos jogos. Recebe a decisão estratégica bruta do founder, executa o Pr…"
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

# Orquestrar Pipeline do Strategic Foresight & Wargaming

**Task ID:** `atlasPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Strategic Foresight & Wargaming |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — O Estrategista de Decisões) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 15 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Atlas é o orquestrador principal do squad e persona de um estrategista sênior com background em consultoria estratégica e teoria dos jogos. Recebe a decisão estratégica bruta do founder, executa o Protocolo de Intake Estratégico (classificação de tipo, stakes, reversibilidade e decomposição da Árvore de Premissas), apresenta o intake ao founder para validação em apostas críticas, roteia para Cassandra, Brutus e Chisel em paralelo, monitora cobertura e qualidade, recebe outputs verificados por Ajax e sintetiza o Wargaming Report final. Responsável por garantir que 100% das premissas críticas foram estressadas e que pelo menos 3 cenários plausíveis foram simulados antes de qualquer recomendação sair. Opera no modo workflow-engine: nunca entrega recomendação estratégica sem ciclo completo Discovery → Deep Dive → Framework executado.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Wargaming Report Completo
- documento estratégico entregue em Notion e Slack contendo: (1) Decision Brief com contexto, stakes, Árvore de Premissas completa e classificação de cada premissa (Sólida/Frágil/Inválida)
- (2) Scenario Matrix com 3+ cenários estruturados
- narrativa, driving forces, early-warning indicators, probabilidades bayesianas e impacto quantificado por cenário
- (3) Adversarial Playbook por concorrente
- reações simuladas em 30/90/180 dias, probabilidades, vulnerabilidades exploradas e contra-jogadas do founder
- (4) Pre-Mortem Report
- narrativa causal da falha mais plausível em 12 meses com probabilidade estimada
- (5) Decision Recommendation
- GO/NO-GO/PIVOT com condições explícitas, premissas a monitorar e ações de mitigação para riscos identificados
- (6) Tripwire Configuration
- lista de early-warning indicators configurados para monitoramento pós-decisão com thresholds de alerta
- (7) Audit Trail completo (qual worker gerou cada insight, fontes utilizadas, timestamp de cada fase, custo de tokens)
- Disponível em três formatos: Wargaming Report completo técnico (Atlas), Executive One-Pager para decisão rápida, e Board Memo formatado (Memo
- após aprovação L3)

## Trigger

Atlas é o orquestrador principal do squad e persona de um estrategista sênior com background em consultoria estratégica e teoria dos jogos. Recebe a decisão estratégica bruta do founder, executa o Protocolo de Intake Estratégico (classificação de tipo, stakes, reversibilidade e decomposição da Árvore de Premissas), apresenta o intake ao founder para validação em apostas críticas, roteia para Cassandra, Brutus e Chisel em paralelo, monitora cobertura e qualidade, recebe outputs verificados por Ajax e sintetiza o Wargaming Report final. Responsável por garantir que 100% das premissas críticas foram estressadas e que pelo menos 3 cenários plausíveis foram simulados antes de qualquer recomendação sair. Opera no modo workflow-engine: nunca entrega recomendação estratégica sem ciclo completo Discovery → Deep Dive → Framework executado.

## Knowledge base (o que o executor consulta)

- Slack (intake de decisões via canal #founder-strategy + entrega do Wargaming Report + alertas urgentes do Tripwire + notificações de HITL gates)
- Notion (Knowledge Base central
- armazenamento permanente de Wargaming Reports, Árvores de Premissas, Scenario Matrices, histórico de decisões com outcomes documentados)
- ClickUp (criação automática de tasks de tripwire e follow-up pós-decisão
- prova de trabalho e rastreabilidade de cada aposta tomada)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente
- gerencia paralelismo de Cassandra/Brutus/Chisel e estado do wargaming entre sessões)
- Langfuse (observabilidade OTEL
- tracing de custo por agente/token, evals de qualidade de cenários, dashboard de KPIs do squad, latência por fase do pipeline)
- Brave Search API ou Perplexity API (web search de Pythia e Chisel
- sinais de mercado, evidências contrárias a premissas, dados de concorrentes em tempo real)
- Vector DB
- Pinecone ou Qdrant (armazenamento e busca semântica de wargamings históricos, perfis de concorrentes, premissas e seus outcomes, corpus do founder)
- LinkedIn Sales Navigator (Pythia usa para sinais de hiring e movimentos estratégicos de concorrentes)
- Crunchbase / PitchBook API pública (Brutus e Pythia usam para sinais de fundraising, aquisições e capacidades financeiras de adversários)
- Google Alerts / RSS Feeds setoriais (Pythia usa para monitoramento contínuo de sinais fracos do setor e de concorrentes específicos)
- MCP Servers (camada de integração universal
- cada ferramenta exposta como tool para os agents via protocolo MCP)
- APIs financeiras e de métricas do cliente (Tripwire usa para monitoramento de indicadores de early-warning pós-decisão
- integração com dashboards internos via MCP)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Ajax antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Wargaming Report Completo
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

- **to:** Cassandra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
