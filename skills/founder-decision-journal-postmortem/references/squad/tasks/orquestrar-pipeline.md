---
task: verdictPipeline()
responsavel: "VERDICT"
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
    descricao: "Pacote do Decision Intelligence System"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "conjunto de artefatos verificaveis e auditaveis: (1) Decision Journal Ativo no Notion"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "database estruturado com todas as entries, premissas declaradas com timestamp imutavel, Red-Team Reports vinculados, status de cada decisao no ciclo, postmortems associados e links para evidencias de resultado"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) Calibration Corpus do Founder"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "banco de premissas testadas com historico de acerto/erro, nivel de confianca calibrado por contexto e referencia ao postmortem de origem"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "cada entrada e dado de treino de alta qualidade para o clone"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do squad. Recebe sinais de decisao de multiplos canais (Slack, WhatsApp, ClickUp, calendario, formulario manual), classifica por tipo e impacto, e gerencia o estado de cada decis…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic MIRROR antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder antes de ser persistida — o clone nunca evolui seus principios nucleares sem consentimento explicito do dono do conhecimento"
    - "[ ] L3: ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirmacao do founder de que quer registrar — nenhum trigger automatico substitui a intencao explicita para eventos deste nivel"
    - "[ ] L3: SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu prosseguir, ou que discorda do SKEPTIC com justificativa registrada — garante accountability do processo, nao apenas do resultado"
    - "[ ] L2: ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao capturou antes do relatorio ser finalizado e enviado ao CALIBRADOR"
    - "[ ] L2: CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima custo de integracao — recomendamos adicionar gate obrigatorio de validacao tecnica antes de fechar contratos acima de R$X'): founder aprova ou rejeita a mudanca de processo antes de ser codificada"
---

# Orquestrar Pipeline do Decision Journal & Postmortem

**Task ID:** `verdictPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Decision Journal & Postmortem |
| **status** | `pending` |
| **responsible_executor** | VERDICT (VERDICT — O Arquivista-Mor de Decisoes) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do squad. Recebe sinais de decisao de multiplos canais (Slack, WhatsApp, ClickUp, calendario, formulario manual), classifica por tipo e impacto, e gerencia o estado de cada decisao ao longo de seu ciclo de vida completo: Captura → Registro → Monitoramento → Postmortem → Calibracao. Mantem o pipeline de decisoes abertas (aguardando postmortem) organizado por janela de revisao. Roteia demandas para os workers corretos: ARCHIVIST para captura, SKEPTIC para red-team, SCOUT para pesquisa de benchmarks, RADAR para monitoramento de premissas, ORACLE para analise de postmortem, CALIBRADOR para atualizacao do clone. Tambem detecta decisoes relevantes que NAO foram capturadas (via monitoramento de Slack, email, ClickUp) e aciona o ARCHIVIST para captura retroativa. Nunca toma a decisao pelo founder — apenas garante que o processo de registro e revisao aconteca de forma sistematica. Gera o dashboard semanal de status: decisoes abertas, postmortems pendentes, score de calibracao atual.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote do Decision Intelligence System
- conjunto de artefatos verificaveis e auditaveis: (1) Decision Journal Ativo no Notion
- database estruturado com todas as entries, premissas declaradas com timestamp imutavel, Red-Team Reports vinculados, status de cada decisao no ciclo, postmortems associados e links para evidencias de resultado
- (2) Calibration Corpus do Founder
- banco de premissas testadas com historico de acerto/erro, nivel de confianca calibrado por contexto e referencia ao postmortem de origem
- cada entrada e dado de treino de alta qualidade para o clone
- (3) Calibration Brief Mensal
- relatorio executivo de 1 pagina: score de calibracao do mes por categoria de decisao, top 3 aprendizados com implicacoes acionaveis, evolucao do julgamento vs historico, vieses mais ativos e plano de melhoria
- (4) Dashboard de Cobertura no ClickUp
- tasks por decisao com pipeline visual: Capturada / Red-Team / Monitorando / Postmortem Pendente / Calibracao Aplicada, com SLA de cada etapa e historico de outputs por agente
- (5) Relatorio de Integridade Semanal (SENTINEL-DJ)
- taxa de cobertura, decisoes nao capturadas identificadas, violacoes de imutabilidade, score de qualidade das entries
- (6) Painel Langfuse
- observabilidade em tempo real de custo por ciclo de decisao, latencia por agente, quality gates e score do MIRROR por tipo de postmortem

## Trigger

Orquestrador central do squad. Recebe sinais de decisao de multiplos canais (Slack, WhatsApp, ClickUp, calendario, formulario manual), classifica por tipo e impacto, e gerencia o estado de cada decisao ao longo de seu ciclo de vida completo: Captura → Registro → Monitoramento → Postmortem → Calibracao. Mantem o pipeline de decisoes abertas (aguardando postmortem) organizado por janela de revisao. Roteia demandas para os workers corretos: ARCHIVIST para captura, SKEPTIC para red-team, SCOUT para pesquisa de benchmarks, RADAR para monitoramento de premissas, ORACLE para analise de postmortem, CALIBRADOR para atualizacao do clone. Tambem detecta decisoes relevantes que NAO foram capturadas (via monitoramento de Slack, email, ClickUp) e aciona o ARCHIVIST para captura retroativa. Nunca toma a decisao pelo founder — apenas garante que o processo de registro e revisao aconteca de forma sistematica. Gera o dashboard semanal de status: decisoes abertas, postmortems pendentes, score de calibracao atual.

## Knowledge base (o que o executor consulta)

- Slack (MCP): canal principal de captura conversacional pelo ARCHIVIST, entrega de Red-Team Reports pelo SKEPTIC, alertas do RADAR, notificacoes de postmortem pendente
- inbox central do VERDICT para o squad
- WhatsApp Business API: canal de alta urgencia para alertas L3 do SENTINEL-DJ (violacao de imutabilidade), sinais CRITICOS do RADAR, e aprovacoes do CALIBRADOR para atualizacoes de corpus
- founder responde APROVAR/REJEITAR diretamente
- Notion (MCP): repositorio primario do Decision Journal
- database estruturado com todas as entries, postmortems vinculados, Calibration Corpus e Calibration Briefs mensais
- Schema rigido com campos imutaveis (pre-resultado) e campos de postmortem separados
- ClickUp (MCP): prova de trabalho verificavel
- cada decisao e uma task com status (Capturada / Red-Team Feito / Monitorando / Postmortem Pendente / Calibracao Aplicada / Concluida), subtasks por agente, historico de outputs e timestamps de cada etapa do ciclo
- Gmail / Google Workspace (MCP): monitoramento de emails estrategicos pelo RADAR (sinais de resultado de decisoes abertas), ingestao de documentos e comunicacoes para o ARCHIVIST em decisoes identificadas via email
- HubSpot / CRM (MCP): fonte de metricas de resultado para decisoes relacionadas a vendas, pipeline, contratacoes de vendas e expansao de contas
- RADAR conecta resultados de CRM a premissas abertas do journal
- EXA MCP (via Docker): busca web em tempo real para o SCOUT (base rates, benchmarks) e o RADAR (sinais externos de premissas de mercado)
- toda afirmacao vem com citacao de fonte
- Apify (via Docker): scraping de relatorios setoriais, benchmarks de VCs, estudos de caso e publicacoes de mercado para o SCOUT
- fontes estruturadas para base rates de premissas
- Langfuse (OTEL): observabilidade completa
- tracing de cada ciclo de decisao (captura → red-team → monitoramento → postmortem → calibracao), score de qualidade do MIRROR por etapa, custo de tokens por tipo de decisao, latencia de cada worker, quality gates por ambiente (dev 70% / staging 85% / prod 95% task success)
- LangGraph / Claude Agent SDK: orquestracao stateful do pipeline de decisao
- controle de estado por decision ID ao longo de meses (uma decisao pode estar em monitoramento por 180 dias), paralelismo do SKEPTIC + SCOUT para red-team, retry logic para falhas de captura
- Supabase (pgvector): base vetorial para busca semantica de decisoes analogas
- quando o ORACLE analisa um postmortem, busca os 5 casos mais similares do historico para analise de padroes
- tambem para o SKEPTIC identificar decisoes passadas com premissas similares e seus outcomes

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic MIRROR antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote do Decision Intelligence System
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic MIRROR registrado
- [ ] Gate L3 respeitado: CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao ex…
- [ ] Gate L3 respeitado: ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e…
- [ ] Gate L3 respeitado: SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar q…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder a… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirm… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima cus… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — RADAR ao detectar sinal de refutacao FORTE de premissa critica em decisao de alto impacto ANTES da janela de postmortem: notificacao imediata ao founder com su… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — Configuracao inicial de thresholds (Discovery): founder define pessoalmente os criterios de disparo automatico, as janelas de revisao por tipo de decisao e o n… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic MIRROR | BLOQUEIA entrega |

## Handoff

- **to:** ARCHIVIST
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
