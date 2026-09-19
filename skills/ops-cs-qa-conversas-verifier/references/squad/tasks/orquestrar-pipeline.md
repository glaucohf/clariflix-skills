---
task: kronosPipeline()
responsavel: "KRONOS"
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
    descricao: "Scorecard de Qualidade por Conversa"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "artefato verificável entregue para 100% das conversas auditadas: score total de 0-100 + score por eixo (Compliance/Tom/Precisão/Resolução) + veredicto (VERDE/AMARELO/VERMELHO) + lista de violações com trecho exato citado + ação recomendada"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para conversas AMARELAS e VERMELHAS: task automática no ClickUp com evidência, responsável, prazo e prioridade"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "prova de trabalho rastreável do squad"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Relatório consolidado semanal entregue ao gestor via Slack: distribuição de scores, top violações da semana, agentes que mais melhoraram e que mais precisam de atenção, evolução da taxa de violação por eixo vs semana anterior"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Dashboard de qualidade em tempo real (ClickUp ou Supabase-backed) com métricas de produção do squad (volume auditado, taxa de cobertura, custo por auditoria) e métricas de impacto (taxa de violação trend, FCR, churn risk conversas)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do squad de QA. Gerencia a fila de conversas priorizadas, despacha cada conversa aos quatro workers de auditoria em paralelo, coleta os scores parciais, aplica a fórmula de ponde…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic VERITAS-SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HERALD cria a task — o gestor recebe o alerta e decide se escala para ação disciplinar ou coaching"
    - "[ ] L3: Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do envio; nenhum alerta crítico é enviado sem revisão de falso positivo"
    - "[ ] L3: Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara a proposta de mudança, gestor responsável aprova via ClickUp task antes de entrar em produção — nunca modificação autônoma da rubrica"
    - "[ ] L3: Ações que afetam o agente humano diretamente (notificação formal de violação, registro em prontuário de RH, bloqueio de acesso): o squad gera a evidência e a recomendação, mas a ação sobre pessoas exige aprovação humana obrigatória"
    - "[ ] L2: Conversas de clientes VIP (acima de threshold configurado de valor anual) ou conversas envolvendo processos juridicos ou ameacas: KRONOS pausa o pipeline automatico e notifica o gestor para revisar manualmente antes de qualquer acao do squad"
---

# Orquestrar Pipeline do QÁ de Conversas 100%

**Task ID:** `kronosPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do QÁ de Conversas 100% |
| **status** | `pending` |
| **responsible_executor** | KRONOS (KRONOS — O Crônista de Qualidade) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do squad de QA. Gerencia a fila de conversas priorizadas, despacha cada conversa aos quatro workers de auditoria em paralelo, coleta os scores parciais, aplica a fórmula de ponderação por contexto do cliente (rubrica configurada no onboarding), calcula o score compósito e determina o veredicto final (VERDE / AMARELO / VERMELHO). Coordena o fluxo entre o VERITAS-SENTINEL para revisão de falso positivo em casos críticos, delega a criação de tasks no ClickUp e alertas ao HERALD, e mantém o estado de processamento de cada conversa (idempotência: não reprocessa conversa já auditada, permite retry em caso de falha de worker). Produz o agregado de métricas por ciclo para o dashboard de qualidade. Não executa nenhuma análise de conteúdo diretamente — e o maestro do pipeline, não um revisor.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Scorecard de Qualidade por Conversa
- artefato verificável entregue para 100% das conversas auditadas: score total de 0-100 + score por eixo (Compliance/Tom/Precisão/Resolução) + veredicto (VERDE/AMARELO/VERMELHO) + lista de violações com trecho exato citado + ação recomendada
- Para conversas AMARELAS e VERMELHAS: task automática no ClickUp com evidência, responsável, prazo e prioridade
- prova de trabalho rastreável do squad
- Relatório consolidado semanal entregue ao gestor via Slack: distribuição de scores, top violações da semana, agentes que mais melhoraram e que mais precisam de atenção, evolução da taxa de violação por eixo vs semana anterior
- Dashboard de qualidade em tempo real (ClickUp ou Supabase-backed) com métricas de produção do squad (volume auditado, taxa de cobertura, custo por auditoria) e métricas de impacto (taxa de violação trend, FCR, churn risk conversas)

## Trigger

Orquestrador central do squad de QA. Gerencia a fila de conversas priorizadas, despacha cada conversa aos quatro workers de auditoria em paralelo, coleta os scores parciais, aplica a fórmula de ponderação por contexto do cliente (rubrica configurada no onboarding), calcula o score compósito e determina o veredicto final (VERDE / AMARELO / VERMELHO). Coordena o fluxo entre o VERITAS-SENTINEL para revisão de falso positivo em casos críticos, delega a criação de tasks no ClickUp e alertas ao HERALD, e mantém o estado de processamento de cada conversa (idempotência: não reprocessa conversa já auditada, permite retry em caso de falha de worker). Produz o agregado de métricas por ciclo para o dashboard de qualidade. Não executa nenhuma análise de conteúdo diretamente — e o maestro do pipeline, não um revisor.

## Knowledge base (o que o executor consulta)

- Zendesk / Intercom (Fin) / Freshdesk
- helpdesks primarios para ingestao de tickets
- webhook ou polling via MCP para receber conversas encerradas em tempo quasi-real
- leitura de metadados de ticket (agente, categoria, resolucao) para contexto do NEXUS
- WhatsApp Business API (Gupshup, AiSensy, Twilio)
- canal #1 no Brasil
- ingestão de conversas completas incluindo áudio transcrito via Deepgram/Whisper para audit trail completo
- Gong / Chorus / NICE
- conversation intelligence para calls de voz
- transcrições automáticas alimentam VERITAS e ARIA
- dados de sentimento pré-processados reduzem latência do squad
- ClickUp (MCP disponível / Brain2 / Super Agents)
- hub de tasks de coaching e correção
- cada violação vira uma task rastreável com evidência citada, responsável, prazo e status
- dashboard de qualidade agregado no ClickUp
- prova de trabalho do squad
- canal de alertas críticos para gestores (violações VERMELHAS confirmadas pelo SENTINEL)
- relatório semanal de tendências de qualidade
- notificações de HITL para aprovação de mudanças de rubrica
- HubSpot / Salesforce (MCP disponivel)
- leitura de perfil de cliente (tier, valor, historico) para contextualizacao de prioridade na fila e ponderacao de score
- dados de churn historico para calibrar flag de risco do ARIA
- ChurnZero / Custify / Velaris
- CS platforms para leitura de health score do cliente
- conversas de clientes com health score baixo recebem prioridade de auditoria e peso maior no flag de risco de churn
- Supabase / Postgres
- estado persistente do squad: fila de processamento, scorecards históricos, rubrica ativa, log de contestações, métricas de produção
- pgvector para busca semântica na base de conhecimento do VERITAS
- Langfuse (OTEL)
- observabilidade completa: tracing por conversa (latência por worker, custo por auditoria, tokens consumidos), quality gates (dev 70% / staging 85% / prod 95% de precisão de detecção validada contra set de conversas anotadas), dashboard de drift de qualidade do squad
- Claude Agent SDK / LangGraph
- orquestração do pipeline multi-agente
- paralelismo dos 4 workers de auditoria (LEXIS, ARIA, VERITAS, NEXUS rodando simultaneamente por conversa)
- retry logic com fallback
- controle de estado de processamento por batch
- Deepgram / Whisper
- ASR para transcrição de áudios do WhatsApp e chamadas de voz não processadas por Gong/Chorus
- PT-BR como língua primária com fallback para ES e EN

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic VERITAS-SENTINEL antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Scorecard de Qualidade por Conversa
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic VERITAS-SENTINEL registrado
- [ ] Gate L3 respeitado: Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HER…
- [ ] Gate L3 respeitado: Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do…
- [ ] Gate L3 respeitado: Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HERALD cria a task — o… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do envio; nenhum alerta… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara a proposta de mudan… | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Ações que afetam o agente humano diretamente (notificação formal de violação, registro em prontuário de RH, bloqueio de acesso): o squad gera a evidência e a r… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Conversas de clientes VIP (acima de threshold configurado de valor anual) ou conversas envolvendo processos juridicos ou ameacas: KRONOS pausa o pipeline autom… | BLOQUEIA até decisão humana |
| VETO-006 | L2 — Contestação de scorecard pelo agente auditado: CALIBRA recebe a contestação, analisa e gera recomendação (confirmar ou reverter veredicto), mas a decisão final… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — Calibragem inicial da rubrica no onboarding: os pesos dos eixos, os thresholds de VERDE/AMARELO/VERMELHO e a lista inicial de termos proibidos são definidos pe… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic VERITAS-SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** LEXIS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
