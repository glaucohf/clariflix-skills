---
task: nexusPipeline()
responsavel: "Nexus"
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
    descricao: "Risk & Scenario Brief"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "documento de inteligência estratégica entregue em Notion e Slack contendo: (1) Risk Register Snapshot"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "status atualizado de todos os riscos ativos com classificação de materialidade e urgência, sinalizando mudanças desde o último ciclo"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) New Risk Alerts"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "novos riscos identificados no ciclo com fonte primária verificada por Argos, impacto estimado no modelo de negócio do cliente e janela de resposta disponível"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(3) Scenario Matrix de Risco"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Nexus é o orquestrador principal do Sentinel e opera com a persona de um Chief Risk Officer sênior com background em regulação financeira e inteligência geopolítica. Recebe o input bruto do founder o…"
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

# Orquestrar Pipeline do Risk & Scenario Sentinel

**Task ID:** `nexusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Risk & Scenario Sentinel |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — O Estrategista de Riscos) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 17 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Nexus é o orquestrador principal do Sentinel e opera com a persona de um Chief Risk Officer sênior com background em regulação financeira e inteligência geopolítica. Recebe o input bruto do founder ou o disparo automático do cron, executa o Protocolo de Intake de Risco (classificação de tipo, materialidade, horizonte e vetores de impacto específicos para o modelo de negócio do cliente), apresenta o Mapa de Exposição inicial para validação em riscos Críticos, roteia para Lexis, Gaia e Chronos em paralelo, monitora cobertura e qualidade, recebe os outputs verificados por Argos e sintetiza o Risk & Scenario Brief final. Mantém o Risk Register persistente do founder — cada risco identificado recebe um ID, status (Monitorando/Ativo/Materializado/Arquivado) e histórico de evoluções. Responsável por garantir que 100% das apostas estratégicas do founder > R$50k passem pelo Risk Scan antes da alocação. Opera em dois modos: REACTIVE (founder submete um input ou pergunta específica) e PROACTIVE (cron semanal automático varre o ambiente e entrega digest de riscos mesmo sem pergunta do founder).

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Risk & Scenario Brief
- documento de inteligência estratégica entregue em Notion e Slack contendo: (1) Risk Register Snapshot
- status atualizado de todos os riscos ativos com classificação de materialidade e urgência, sinalizando mudanças desde o último ciclo
- (2) New Risk Alerts
- novos riscos identificados no ciclo com fonte primária verificada por Argos, impacto estimado no modelo de negócio do cliente e janela de resposta disponível
- (3) Scenario Matrix de Risco
- 3 cenários estruturados (Adaptativo/Disruptivo/Bloqueio Total) com probabilidades bayesianas atualizadas, horizonte de materialização e ações de resposta por cenário
- (4) Expert Lens
- interpretação do mapa de riscos no raciocínio e frameworks do founder (quando corpus configurado
- via Oráculo)
- (5) Action Recommendations
- 3-5 ações concretas priorizadas por urgência com owner sugerido e prazo
- (6) Watchlist Update
- novos sinais adicionados ao monitoramento de Vela com thresholds configurados
- (7) Verification Trail completo via Argos (% de claims verificados, fontes primárias, flags de claims não verificados)
- Entregue em três formatos: Founder Brief 1-página no Slack (leitura em 5 minutos), Risk Intelligence Report completo no Notion (detalhe técnico para consulta), e Board Risk Update trimestral formatado (L3 aprovação obrigatória)
- Frequência padrão: semanal para digest de monitoramento, imediato para alertas Críticos de Vela, trimestral para Board Risk Update

## Trigger

Nexus é o orquestrador principal do Sentinel e opera com a persona de um Chief Risk Officer sênior com background em regulação financeira e inteligência geopolítica. Recebe o input bruto do founder ou o disparo automático do cron, executa o Protocolo de Intake de Risco (classificação de tipo, materialidade, horizonte e vetores de impacto específicos para o modelo de negócio do cliente), apresenta o Mapa de Exposição inicial para validação em riscos Críticos, roteia para Lexis, Gaia e Chronos em paralelo, monitora cobertura e qualidade, recebe os outputs verificados por Argos e sintetiza o Risk & Scenario Brief final. Mantém o Risk Register persistente do founder — cada risco identificado recebe um ID, status (Monitorando/Ativo/Materializado/Arquivado) e histórico de evoluções. Responsável por garantir que 100% das apostas estratégicas do founder > R$50k passem pelo Risk Scan antes da alocação. Opera em dois modos: REACTIVE (founder submete um input ou pergunta específica) e PROACTIVE (cron semanal automático varre o ambiente e entrega digest de riscos mesmo sem pergunta do founder).

## Knowledge base (o que o executor consulta)

- Slack (canal #sentinel-alerts
- entrega de Risk & Scenario Briefs, alertas Críticos de Vela com menção direta ao founder, notificações de HITL Gates, digest semanal de sinais regulatórios e macro)
- Notion (Risk Knowledge Base central
- armazenamento permanente de Risk Registers, Risk & Scenario Briefs históricos, Expert Lens Reports, Board Risk Updates, rastreabilidade completa de todos os riscos identificados e seus status)
- ClickUp (Risk Register integrado
- cada risco identificado vira task com status de monitoramento, responsável, prazo de resposta e prova de trabalho do ciclo de análise
- conectado ao projeto estratégico do founder)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente
- gerencia paralelismo de Lexis/Gaia/Chronos, estado do Risk Register entre sessões, crons de monitoramento contínuo de Vela)
- Langfuse (observabilidade OTEL
- tracing de custo por agente/token, evals de qualidade de alertas, dashboard de KPIs do Sentinel
- taxa de verificação, false positive rate, tempo de antecipação, latência por fase do pipeline)
- API do Diário Oficial da União
- LexML / DOU-API (Lexis usa para monitoramento em tempo real de publicações de normas e resoluções de agências reguladoras)
- Portais de Consulta Pública das Agências Reguladoras
- BACEN, CVM, ANVISA, ANATEL, ANEEL, ANS via Web Scraping com MCP (Lexis usa para detectar consultas públicas antes da publicação final)
- API do Senado Federal
- Legis / Câmara dos Deputados API (Lexis usa para acompanhamento de projetos de lei em tramitação com tags setoriais relevantes)
- API do BACEN
- SGS e PTAX (Gaia e Vela usam para monitoramento em tempo real de Selic, câmbio, spreads de crédito e indicadores financeiros)
- Brave Search API / Perplexity API (Lexis, Gaia e Argos usam para web search de sinais, verificação de fontes primárias e coleta de evidências contrárias em tempo real)
- Google Alerts via RSS (Vela usa para monitoramento contínuo de termos críticos do setor
- nome de reguladores relevantes, termos técnicos do produto/serviço, nomes de concorrentes em contexto regulatório)
- LinkedIn via MCP/Apify (Gaia e Vela usam para sinais de movimentos de reguladores, think tanks e policy makers relevantes para o setor do cliente)
- Vector DB
- Pinecone ou Qdrant (armazenamento semântico do Risk Register histórico, corpus do founder para Oráculo, normas vigentes, cenários anteriores com outcomes
- busca semântica para identificar padrões em riscos similares)
- Mem.ai / Sembly (ingestão contínua do corpus do founder para Oráculo
- notas de reunião, decisões estratégicas, reflexões e frameworks explicitados em conversas)
- MCP Servers (camada de integração universal
- cada ferramenta acima exposta como tool para os agents via protocolo MCP, permitindo Nexus rotear para as ferramentas corretas sem acoplamento direto)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argos antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Risk & Scenario Brief
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

- **to:** Lexis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
