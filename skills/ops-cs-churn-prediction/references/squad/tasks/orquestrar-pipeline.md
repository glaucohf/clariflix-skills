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
    descricao: "Por ciclo diario: (1) Dashboard Langfuse atualizado com health scores de toda a base, distribuicao por faixa de risco, trending de deterioracao e mapa de calor por CSM/segmento"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Tasks no ClickUp para cada conta em risco CRITICO e ALTO com brief completo, sinais que compoem o score com valores concretos, next-best-action prioritaria com taxa de sucesso historica, acoes alternativas rankeadas e script de abertura sugerido"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Registro no Supabase de cada score calculado com breakdown por dimensao, sinais de entrada utilizados, timestamp e versao do modelo"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "prova de trabalho auditavel e rastreavel"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Por semana: relatorio de saude da base (distribuicao de scores, saves confirmados, MRR protegido, padroes sistemicos detectados) entregue no Slack do Head de CS"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Por save confirmado: medicao de impacto (variacao do health score pre/pos-intervencao, MRR protegido) registrada no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestra o ciclo diario de analise de churn: aciona o Sensor Vega para ingestao de sinais, recebe os dados normalizados de todas as contas monitoradas, calcula ou delega o calculo do health score co…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica"
    - "[ ] HITL: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato"
    - "[ ] HITL: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados"
    - "[ ] HITL: Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch"
    - "[ ] HITL: Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar"
---

# Orquestrar Pipeline do Predição e Prevenção de Churn

**Task ID:** `nexusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Predição e Prevenção de Churn |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Analista de Churn Orchestrator) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestra o ciclo diario de analise de churn: aciona o Sensor Vega para ingestao de sinais, recebe os dados normalizados de todas as contas monitoradas, calcula ou delega o calculo do health score composto, prioriza a fila de contas em risco critico por urgencia e MRR em risco, aciona o Gerador de Brief Mira para as top-N contas, valida com o Critic Argus, e comanda o Agente de Ativacao Spark para criacao de tasks no ClickUp. Em modo batch diario (6h da manha) e modo reativo (webhook de evento critico em tempo real). Mantém historico de scores no Supabase e detecta tendencias de deterioracao acelerada que requerem intervencao imediata.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Por ciclo diario: (1) Dashboard Langfuse atualizado com health scores de toda a base, distribuicao por faixa de risco, trending de deterioracao e mapa de calor por CSM/segmento
- (2) Tasks no ClickUp para cada conta em risco CRITICO e ALTO com brief completo, sinais que compoem o score com valores concretos, next-best-action prioritaria com taxa de sucesso historica, acoes alternativas rankeadas e script de abertura sugerido
- (3) Registro no Supabase de cada score calculado com breakdown por dimensao, sinais de entrada utilizados, timestamp e versao do modelo
- prova de trabalho auditavel e rastreavel
- Por semana: relatorio de saude da base (distribuicao de scores, saves confirmados, MRR protegido, padroes sistemicos detectados) entregue no Slack do Head de CS
- Por save confirmado: medicao de impacto (variacao do health score pre/pos-intervencao, MRR protegido) registrada no CRM

## Trigger

Orquestra o ciclo diario de analise de churn: aciona o Sensor Vega para ingestao de sinais, recebe os dados normalizados de todas as contas monitoradas, calcula ou delega o calculo do health score composto, prioriza a fila de contas em risco critico por urgencia e MRR em risco, aciona o Gerador de Brief Mira para as top-N contas, valida com o Critic Argus, e comanda o Agente de Ativacao Spark para criacao de tasks no ClickUp. Em modo batch diario (6h da manha) e modo reativo (webhook de evento critico em tempo real). Mantém historico de scores no Supabase e detecta tendencias de deterioracao acelerada que requerem intervencao imediata.

## Knowledge base (o que o executor consulta)

- ClickUp (Brain2 / MCP server)
- hub de tasks de retenção, prova de trabalho, prioridade e prazos automáticos, espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce
- fonte de dados de Account, Contract, MRR, CSM, histórico de interações, QBRs e pipeline de renovação
- Plataforma de produto: Mixpanel, Amplitude ou Segment
- eventos de uso, DAU/MAU, feature adoption, sessões por conta
- Helpdesk: Zendesk ou Intercom
- volume de tickets, CSAT, categorias, transcrições e histórico de suporte por conta
- NPS / CSAT: Delighted, Typeform ou Wootric
- scores e verbatims de pesquisas de satisfação
- CS Platforms: ChurnZero, Custify, Gainsight, ou Velaris
- plataformas especializadas de health scoring (integração bidirecional: leitura de dados + escrita de scores calculados)
- notificações em tempo real para CSM (alerta de churn), manager (escalonamento) e Head de CS (relatório semanal e padrões sistêmicos)
- Supabase / Postgres
- estado dos agentes, armazenamento de health scores históricos, sinais normalizados, log de tasks e outcomes
- observabilidade OTEL, tracing do pipeline de cálculo de score, evals de qualidade dos briefs, quality gates dev/staging/prod
- Claude Agent SDK / LangGraph
- orquestração do pipeline multi-agente com gerenciamento de estado e retry logic
- Email / SMTP
- envio de relatório semanal de saúde da base para Head de CS e stakeholders
- News/alerts API (NewsAPI, Google Alerts webhook)
- detecção de mudanças organizacionais em contas monitoradas (M&A, redução de headcount, mudança de liderança)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argus antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Por ciclo diario: (1) Dashboard Langfuse atualizado com health scores de toda a base, distribuicao por faixa de risco, trending de deterioracao e mapa de calor…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cri…
- [ ] Gate HITL respeitado: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de…
- [ ] Gate HITL respeitado: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguarda… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualque… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analis… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo b… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de rela… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Vega
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
