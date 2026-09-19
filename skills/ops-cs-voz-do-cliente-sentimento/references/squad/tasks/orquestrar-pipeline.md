---
task: orionPipeline()
responsavel: "Orion"
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
    descricao: "CICLO DIÁRIO: (1) Log de ingestão no Supabase por canal"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "volume de registros, % de qualidade válida, anomalias detectadas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "prova de trabalho verificável pelo time de dados"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) Alertas em tempo real no Slack (#voc-alertas) quando temas cruzam threshold de emergência"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "com volume concreto, verbatims e sugestão de ação imediata"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(3) Dashboard Langfuse atualizado com métricas de pipeline: registros processados, distribuição de sentimento do dia, top-5 temas por volume"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion orquestra o ciclo completo de inteligencia de feedback: aciona Haruki para ingestao diaria de todos os canais, aguarda confirmacao de qualidade, dispara Yara para analise de sentimento e classi…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Cassandra antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia lembrete; sem resposta em 8h, relatório é enviado com disclaimer 'pendente de revisão humana'"
    - "[ ] HITL: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para atendimento) antes de aparecer no backlog ativo; aprovação via bot no Slack com preview da task"
    - "[ ] HITL: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefing imediato e Atlas cria task de emergência; se falso positivo, threshold é ajustado automaticamente"
    - "[ ] HITL: Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-processar histórico; impacto estimado em registros afetados e apresentado antes da aprovação"
    - "[ ] HITL: Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; indica possível drift na linguagem dos clientes ou bug na ingestão"
---

# Orquestrar Pipeline do Voz do Cliente

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Voz do Cliente |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Voice-of-Customer Orchestrator) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orion orquestra o ciclo completo de inteligencia de feedback: aciona Haruki para ingestao diaria de todos os canais, aguarda confirmacao de qualidade, dispara Yara para analise de sentimento e classificacao de temas dos novos registros, consolida os resultados no Supabase, roda deteccao de tendencias emergentes comparando volume e velocidade do periodo atual vs baseline dos 14 dias anteriores, identifica tendencias que cruzaram threshold de alerta e as encaminha para Rapid disparar alertas imediatos, e ao final de cada semana aciona Lyra para sintetizar o relatorio priorizando tendencias por score (volume x impacto x sentimento). Gerencia a fila de processamento para evitar sobrecarga em semanas com pico de volume (ex: apos release de produto ou incidente). Mantém o estado do pipeline no Supabase e recalcula baseline toda segunda-feira. Opera em modo batch (ciclo diario as 07h e ciclo semanal as 08h segunda-feira) e modo reativo (webhook de evento critico — pico de volume em < 4h).

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- CICLO DIÁRIO: (1) Log de ingestão no Supabase por canal
- volume de registros, % de qualidade válida, anomalias detectadas
- prova de trabalho verificável pelo time de dados
- (2) Alertas em tempo real no Slack (#voc-alertas) quando temas cruzam threshold de emergência
- com volume concreto, verbatims e sugestão de ação imediata
- (3) Dashboard Langfuse atualizado com métricas de pipeline: registros processados, distribuição de sentimento do dia, top-5 temas por volume
- CICLO SEMANAL: Relatório de Tendências Priorizadas
- o artefato central do squad
- entregue toda segunda-feira às 09h com: sumário executivo de 200 palavras, top-5 tendências com score de priorização, volume (menções com número absoluto e % do total), variação vs semana anterior (delta%), sentimento médio, breakdown por segmento de cliente, 3-5 verbatims representativos com canal e data citados (rastreabilidade completa), correlação com evento de produto se existir, e sugestão de ação específica por tendência
- Versão completa no Notion, versão resumida no Slack
- Tasks de ação aprovadas criadas no ClickUp com prova de trabalho rastreável (tag VOC)
- CICLO MENSAL: Relatório de impacto
- insights gerados vs ações tomadas vs variação de NPS e volume de tickets nos temas atacados
- ROI mensurável do squad

## Trigger

Orion orquestra o ciclo completo de inteligencia de feedback: aciona Haruki para ingestao diaria de todos os canais, aguarda confirmacao de qualidade, dispara Yara para analise de sentimento e classificacao de temas dos novos registros, consolida os resultados no Supabase, roda deteccao de tendencias emergentes comparando volume e velocidade do periodo atual vs baseline dos 14 dias anteriores, identifica tendencias que cruzaram threshold de alerta e as encaminha para Rapid disparar alertas imediatos, e ao final de cada semana aciona Lyra para sintetizar o relatorio priorizando tendencias por score (volume x impacto x sentimento). Gerencia a fila de processamento para evitar sobrecarga em semanas com pico de volume (ex: apos release de produto ou incidente). Mantém o estado do pipeline no Supabase e recalcula baseline toda segunda-feira. Opera em modo batch (ciclo diario as 07h e ciclo semanal as 08h segunda-feira) e modo reativo (webhook de evento critico — pico de volume em < 4h).

## Knowledge base (o que o executor consulta)

- ClickUp (Brain2 / MCP server)
- hub de tasks de ação, prova de trabalho com tags VOC, rastreabilidade de insights, espelhando arquitetura AIOX
- usado pelo Atlas para criação de tasks e pelo Orion para leitura de eventos de produto
- Zendesk ou Intercom
- fonte primária de tickets de suporte com CSAT e comentários
- volume diário normalizado pelo Haruki
- campo de tema do Yara pode ser gravado de volta como tag no ticket via API
- NPS / CSAT: Delighted, Typeform, Wootric ou SurveyMonkey
- scores e verbatims de pesquisas
- NPS é a fonte de sentimento mais estruturada e prioritária
- WhatsApp Business API
- mensagens de atendimento anônimizadas
- canal #1 de feedback informal no Brasil
- exige tratamento nativo de texto curto e linguagem informal
- Reviews públicos: G2, Capterra, Trustpilot, App Store, Google Play
- coletados semanalmente via API ou scraping
- fonte de feedback de prospects além de clientes
- destino do relatorio semanal completo em markdown com historico pesquisavel por tema e data
- canal #voc-alertas para alertas do Rapid, canal #voc-insights para relatório semanal resumido, DMs para responsáveis de tasks aprovadas pelo Atlas
- Supabase / Postgres
- banco de estado do squad: voc_raw_feedback, voc_analyzed_feedback, voc_trends_daily, voc_weekly_reports, voc_alerts, voc_actions
- histórico completo auditável
- observabilidade OTEL do pipeline, tracing de classificação do Yara, evals de qualidade dos insights do Lyra, quality gates dev/staging/prod (70/85/95% accuracy)
- Claude Agent SDK / LangGraph
- orquestração do pipeline multi-agente com gerenciamento de estado, retry logic e paralelização de ingestão de canais
- CRM: HubSpot ou Salesforce
- dados de segmento, MRR e CSM responsável por account_id para ponderação de tendências por segmento e cálculo de impacto de receita
- Jira ou Linear (opcional)
- leitura do changelog de produto para correlação de tendências com releases e incidentes no Orion
- Airtable ou Google Sheets (fallback)
- canais de feedback que não tem API estruturada podem ser ingeridos via planilha compartilhada como fonte temporária

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Cassandra antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: CICLO DIÁRIO: (1) Log de ingestão no Supabase por canal
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Cassandra registrado
- [ ] Gate HITL respeitado: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação e…
- [ ] Gate HITL respeitado: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto…
- [ ] Gate HITL respeitado: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmad…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para at… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefin… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-proce… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; in… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Publicacao de insight que menciona concorrente especifico por nome — Lyra sinaliza e o Head de CS aprova antes de distribuir para evitar vazamento de informaca… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Re-calibração de thresholds de alerta após detecção de falsos positivos recorrentes — o Rapid documenta a sugestão de ajuste e aguarda aprovação do PM ou Head… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de canal com volume insuficiente para análise estatística identificado pós-Discovery — Haruki notifica e aguarda decisão humana sobre incluir ou exclu… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Cassandra | BLOQUEIA entrega |

## Handoff

- **to:** Haruki
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
