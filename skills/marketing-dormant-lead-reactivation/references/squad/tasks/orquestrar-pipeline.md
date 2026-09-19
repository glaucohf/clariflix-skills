---
task: lazaroPipeline()
responsavel: "Lazaro"
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
    descricao: "Rodada de Reativacao Verificavel e Auditavel: (1) Mapa de Base Dormentes"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "segmentacao completa por archetype, cluster e prioridade (Arqueologa + Oraculo Scorer) exportado como planilha e salvo no ClickUp, linkado ao CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Ficha de Sinais Novos por lead processado (Radar) com mudancas detectadas, fontes verificadas e angulo de reativacao"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "salva no ClickUp e dados atualizados no CRM"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Pack de Reativacao aprovado por lead: drafts A/B por toque da sequencia com checklist do critic Atena preenchido, score de qualidade e compliance confirmado"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "versionado no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestra o ciclo completo de reativacao da base dormentes: ingere a lista de leads dormentes do CRM, decompoe em clusters acionaveis, distribui para os workers na sequencia correta (Arqueologa -> Ra…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Atena antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao."
    - "[ ] HITL: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado."
    - "[ ] HITL: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio."
    - "[ ] HITL: Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa."
    - "[ ] HITL: Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática."
---

# Orquestrar Pipeline do Dormant Lead Reactivation

**Task ID:** `lazaroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Dormant Lead Reactivation |
| **status** | `pending` |
| **responsible_executor** | Lazaro (Lazaro — O Ressuscitador de Pipeline) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestra o ciclo completo de reativacao da base dormentes: ingere a lista de leads dormentes do CRM, decompoe em clusters acionaveis, distribui para os workers na sequencia correta (Arqueologa -> Radar -> Oraculo Scorer -> Lazaro Writer -> Atena -> Charon Dispatcher -> Echo Analyst), mantem o estado de reativacao de cada lead (dormente -> em sequencia -> reativado -> oportunidade reaberta -> descartado com dignidade), e consolida os artefatos de cada rodada em relatorio executivo de ROI da reativacao. Decide quais leads entram em qual trilha de reativacao com base nos clusters definidos no Deep Dive. Monitora os quality gates no Langfuse e bloqueia o fluxo para HITL sempre que uma acao irreversivel esta prestes a acontecer ou um gate falha. Opera em L2: executa o ciclo de orquestracao autonomamente por cluster e rodada, mas gates L3 (envios para leads estrategicos, aprovacoes de copy sensivel) bloqueiam o fluxo para aprovacao humana.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Rodada de Reativacao Verificavel e Auditavel: (1) Mapa de Base Dormentes
- segmentacao completa por archetype, cluster e prioridade (Arqueologa + Oraculo Scorer) exportado como planilha e salvo no ClickUp, linkado ao CRM
- (2) Ficha de Sinais Novos por lead processado (Radar) com mudancas detectadas, fontes verificadas e angulo de reativacao
- salva no ClickUp e dados atualizados no CRM
- (3) Pack de Reativacao aprovado por lead: drafts A/B por toque da sequencia com checklist do critic Atena preenchido, score de qualidade e compliance confirmado
- versionado no ClickUp
- (4) Log de Envio imutavel (Charon Dispatcher): timestamp, canal, variacao A/B, status de cada mensagem com rastreamento de abertura e click
- activity no CRM e ClickUp
- (5) Analise de Resposta estruturada (Echo Analyst): categoria de reativacao, objecao detectada, coaching note para o vendedor, proximo passo recomendado
- CRM atualizado, notificacao ao vendedor
- (6) Relatorio Executivo de ROI da Rodada: leads processados, taxa de reativacao por trilha e archetype, pipeline reaberto em R$, custo por lead reativado vs CAC original, variacoes A/B vencedoras, recomendacoes para proxima rodada
- entregue ao gestor via ClickUp e Slack/email
- Todo o pipeline e auditavel por design: cada artefato tem agente responsavel, timestamp, veredicto do critic e rastro no Langfuse
- O gestor ve o ROI completo de cada centavo do CAC que foi resgatado

## Trigger

Orquestra o ciclo completo de reativacao da base dormentes: ingere a lista de leads dormentes do CRM, decompoe em clusters acionaveis, distribui para os workers na sequencia correta (Arqueologa -> Radar -> Oraculo Scorer -> Lazaro Writer -> Atena -> Charon Dispatcher -> Echo Analyst), mantem o estado de reativacao de cada lead (dormente -> em sequencia -> reativado -> oportunidade reaberta -> descartado com dignidade), e consolida os artefatos de cada rodada em relatorio executivo de ROI da reativacao. Decide quais leads entram em qual trilha de reativacao com base nos clusters definidos no Deep Dive. Monitora os quality gates no Langfuse e bloqueia o fluxo para HITL sempre que uma acao irreversivel esta prestes a acontecer ou um gate falha. Opera em L2: executa o ciclo de orquestracao autonomamente por cluster e rodada, mas gates L3 (envios para leads estrategicos, aprovacoes de copy sensivel) bloqueiam o fluxo para aprovacao humana.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível
- fonte de verdade para o estado de cada lead dormente, activities, histórico de interações, campo de score de reativação, pipeline de oportunidades reativadas), Salesforce com Agentforce SDK ou Pipedrive como alternativas
- Enriquecimento e sinais novos: Clay (waterfall de 100+ fontes para atualização de dados, intent signals, sinais de mudança de empresa e headcount), Apollo.io (verificação de email atual, cargo atual, sinais de mudança de emprego), LinkedIn Sales Navigator (mudanças de cargo, promoções, expansões de headcount)
- Validação de email: NeverBounce ou ZeroBounce integrados via Clay waterfall para verificação antes de qualquer envio
- bounce em reativação e mais custoso que em cold (queima relação pre-existente)
- Email reativação: Instantly.ai ou Lemlist (sequências com rastreamento de abertura e click, warmup de domínio para proteger reputação), SendGrid ou AWS SES para volume alto
- WhatsApp Business API: plataformas purpose-built para mercado brasileiro
- Gupshup, AiSensy ou QuickReply.ai (conformidade pós-restricoes Meta 2024, templates pré-aprovados para reativação B2B)
- LinkedIn outreach: Sales Navigator para verificação de dados + Phantombuster ou Expandi para automação controlada de InMails dentro dos limites diários
- Calendário para booking: Calendly ou Cal.com integrado ao Charon Dispatcher para envio automático de link de agendamento quando lead responde positivamente, sem intervenção humana no booking
- Gestão de tasks e artefatos: ClickUp (prova de trabalho verificável por rodada de reativação
- ficha de arqueologia, ficha de sinais, score com breakdown, draft aprovado com checklist do crític, log de envio, análise de resposta) conectado ao Lázaro via MCP ou webhook
- Orquestração multi-agente: LangGraph para controle de estado do funil de reativação por lead (grafos de decisão: dormente -> em sequência -> reativado -> oportunidade -> fechado/arquivado) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (traces OTEL por agente, quality gates dev 70% / staging 85% / prod 95%, dashboard de reativação com KPIs em tempo real, alertas de anomalia quando taxa de bounce ou opt-out sobe acima do threshold)
- Notificações internas: Slack ou WhatsApp do vendedor/gestor para alertas de HITL urgentes, leads RESSUSCITADOS detectados e relatório semanal de ROI de reativação
- No-code complementar: n8n para automações de integração
- webhook de resposta de email para Echo Analyst, cron de batch semanal de novos dormentes, sync de score de reativação para CRM custom fields sem código

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Atena antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Rodada de Reativacao Verificavel e Auditavel: (1) Mapa de Base Dormentes
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Atena registrado
- [ ] Gate HITL respeitado: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configura…
- [ ] Gate HITL respeitado: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança…
- [ ] Gate HITL respeitado: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrig…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovaç… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que di… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Sinais de oportunidade detectados em lead que estava em ARQUIVO (score < 40): Radar detecta mudança significativa (investimento, mudança de decisor, sinal de i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Relatório semanal de performance: Echo Analyst gera relatório de taxa de reativação por trilha e archetype entregue ao gestor todo friday — ponto de HITL estru… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Opt-out recebido: processamento automático cancela a sequência e atualiza o CRM, mas a decisão de blacklist permanente (nunca mais contatar) é sempre humana —… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Atena | BLOQUEIA entrega |

## Handoff

- **to:** Arqueologa
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
