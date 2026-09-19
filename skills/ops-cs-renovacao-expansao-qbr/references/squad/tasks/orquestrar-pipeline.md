---
task: maestroPipeline()
responsavel: "Maestro"
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
    descricao: "Por conta em janela de renovacao: (1) QBR Brief completo em markdown (max 600 palavras) com Resumo de Valor do Trimestre, Metricas de Adocao com comparativo, Marcos Entregues, Status de Comprometimentos Anteriores, Pontos de Tensao baseados em sentimento e Agenda Proposta de QBR"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "armazenado no Supabase e na task ClickUp como prova de trabalho auditavel"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Deck de QBR gerado automaticamente via API (Google Slides ou PowerPoint) com os dados do brief, salvo no Google Drive na pasta do CSM, link direto na task ClickUp"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Renewal Package com Renewal Readiness Score interpretado, Top-5 Evidencias de ROI em linguagem do decisor, e Proposta de Expansao qualificada (se aplicavel) com sinais que a embasam"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(4) Pacote de tarefas no ClickUp: task principal de renovacao/QBR com todas as subtasks, prazos calculados e checklists de preparacao"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "prova de trabalho completa do squad rastreavel por conta, CSM e data"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestra o ciclo diario e por eventos de preparacao de renovacao e expansao. Executa o pipeline completo em modo batch diario (05h30): aciona o Radar para identificar contas em janela de renovacao e…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Verity antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de expansao com status 'Aguardando Aprovacao do CSM/Manager' antes de incluir a proposta no deck final para o cliente"
    - "[ ] HITL: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CSM (deck e gerado, nunca enviado automaticamente ao cliente)"
    - "[ ] HITL: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar qualquer contato de renovacao"
    - "[ ] HITL: Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de entrada antes de reprocessar"
    - "[ ] HITL: Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer alinhamento com equipe comercial (AE ou CSM sênior) antes de abordar o cliente"
---

# Orquestrar Pipeline do Renovacao, Expansao e QBR Automatizado

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Renovacao, Expansao e QBR Automatizado |
| **status** | `pending` |
| **responsible_executor** | Maestro (Maestro — Orchestrator de Renovacao e Expansao) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestra o ciclo diario e por eventos de preparacao de renovacao e expansao. Executa o pipeline completo em modo batch diario (05h30): aciona o Radar para identificar contas em janela de renovacao e com sinais de expansao, recebe o mapa de prioridades do dia, aciona o Compass para calcular Renewal Readiness Score das contas prioritarias, aciona o Scout para analise de expansao paralela, e delega a geracao de brief ao Briefer para cada conta relevante. Em modo evento: reage a webhooks de renovacao proxima (< 30 dias, nao detectada antes) e a sinais de expansao criticos (aumento de usuarios acima de threshold em 24h, solicitacao de feature premium via ticket). Controla a fila de producao de briefs por prioridade (MRR da conta x proximidade da renovacao x Renewal Readiness Score) para evitar sobrecarga em dias com multiplas renovacoes simultaneas. Mantém estado de pipeline de renovacao no Supabase e garante que cada conta tenha seu brief pronto pelo menos 30 dias antes da data-chave.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Por conta em janela de renovacao: (1) QBR Brief completo em markdown (max 600 palavras) com Resumo de Valor do Trimestre, Metricas de Adocao com comparativo, Marcos Entregues, Status de Comprometimentos Anteriores, Pontos de Tensao baseados em sentimento e Agenda Proposta de QBR
- armazenado no Supabase e na task ClickUp como prova de trabalho auditavel
- (2) Deck de QBR gerado automaticamente via API (Google Slides ou PowerPoint) com os dados do brief, salvo no Google Drive na pasta do CSM, link direto na task ClickUp
- (3) Renewal Package com Renewal Readiness Score interpretado, Top-5 Evidencias de ROI em linguagem do decisor, e Proposta de Expansao qualificada (se aplicavel) com sinais que a embasam
- (4) Pacote de tarefas no ClickUp: task principal de renovacao/QBR com todas as subtasks, prazos calculados e checklists de preparacao
- prova de trabalho completa do squad rastreavel por conta, CSM e data
- Por semana: relatorio de cobertura de renovacoes (% de renovacoes nos proximos 30 dias com pacote pronto) e pipeline de expansao identificado (numero de oportunidades e ARR total)
- Por mes: relatorio de NRR impact com MRR protegido em renovacoes e MRR incremental de expansoes atribuiveis ao squad

## Trigger

Orquestra o ciclo diario e por eventos de preparacao de renovacao e expansao. Executa o pipeline completo em modo batch diario (05h30): aciona o Radar para identificar contas em janela de renovacao e com sinais de expansao, recebe o mapa de prioridades do dia, aciona o Compass para calcular Renewal Readiness Score das contas prioritarias, aciona o Scout para analise de expansao paralela, e delega a geracao de brief ao Briefer para cada conta relevante. Em modo evento: reage a webhooks de renovacao proxima (< 30 dias, nao detectada antes) e a sinais de expansao criticos (aumento de usuarios acima de threshold em 24h, solicitacao de feature premium via ticket). Controla a fila de producao de briefs por prioridade (MRR da conta x proximidade da renovacao x Renewal Readiness Score) para evitar sobrecarga em dias com multiplas renovacoes simultaneas. Mantém estado de pipeline de renovacao no Supabase e garante que cada conta tenha seu brief pronto pelo menos 30 dias antes da data-chave.

## Knowledge base (o que o executor consulta)

- ClickUp (Brain2 / MCP server)
- hub central de tasks do pacote de renovacao, checklist de preparacao de QBR, prova de trabalho do squad e monitoramento de ativacao
- espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce
- fonte primaria de datas de renovacao, historico de expansao, MRR, atividades do CSM, notas de QBR, executive sponsor, pipeline de renovacao e decisoes comerciais
- Plataforma de produto: Mixpanel, Amplitude, Segment ou analytics nativo
- eventos de uso por conta, DAU/MAU, feature adoption, usuarios ativos vs licencas, sessoes por usuario
- CS Platforms: Gainsight, ChurnZero, Custify, Velaris ou Chargebee
- health scores existentes, historico de QBRs gerenciados na plataforma, alertas de renovacao e dados de health ja calculados (integracao bidirecional: leitura e escrita de scores)
- Google Workspace (Google Slides + Google Drive) ou Microsoft 365 (PowerPoint + SharePoint)
- geracao e armazenamento de decks de QBR via API
- webhook de deteccao de edicao pos-geracao
- Helpdesk: Zendesk ou Intercom
- volume de tickets recentes por conta, CSAT, categorias de problema, resolucoes documentadas para o brief
- NPS / CSAT: Delighted, Typeform, Wootric ou nativo da CS platform
- scores e verbatims para o brief de sentimento
- Call Recording: Gong, Chorus ou Zoom AI (nativo do CRM)
- transcricoes de chamadas de QBR anteriores para o Memory e para o Briefer enriquecer o contexto relacional
- notificacoes ao CSM (brief pronto, deck gerado, renovacao critica), manager (escalacoes, tasks nao abertas) e Head de CS (relatorio semanal de cobertura e NRR tracking)
- Supabase / Postgres
- estado dos agentes, Account Memory, Renewal Readiness Score historico, Expansion Signal Reports, log de tasks criadas e outcomes de renovacao
- observabilidade OTEL, tracing do pipeline de geracao de briefs, evals de qualidade de artefatos, quality gates dev/staging/prod, dashboard de NRR e cobertura de renovacoes
- Claude Agent SDK / LangGraph
- orquestracao do pipeline multi-agente com gerenciamento de estado, filas de prioridade e retry logic
- Email / SMTP
- relatorio semanal de cobertura de renovacoes para Head de CS e resumo mensal de NRR impact para stakeholders

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Verity antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Por conta em janela de renovacao: (1) QBR Brief completo em markdown (max 600 palavras) com Resumo de Valor do Trimestre, Metricas de Adocao com comparativo, M…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Verity registrado
- [ ] Gate HITL respeitado: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pu…
- [ ] Gate HITL respeitado: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e…
- [ ] Gate HITL respeitado: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS a…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CS… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de ent… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer ali… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Comprometimento pendente do fornecedor detectado pelo Memory como nao entregue no periodo anterior — brief inclui o item mas Pulse cria subtask de 'Resolucao d… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Conta com Renewal Readiness Score CRITICO (< 50) e renovacao em < 30 dias — escalacao imediata para Head de CS e Account Executive senior com brief de situacao… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de Memory indicando que CSM fez edicao significativa no deck (> 30% do conteudo alterado) — Maestro abre HITL para CSM documentar o motivo da edicao e… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Verity | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
