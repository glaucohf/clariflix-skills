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
    descricao: "Pacote de outreach verificado, personalizado e rastreável por lead: (1) ICP Card vivo atualizado (ICP Cartografo) salvo no ClickUp"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "base de toda a prospecção"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Dossiê de conta estruturado (Scout Profiler) com score de confiança, fontes verificadas e ângulos de personalização"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "salvo no ClickUp e linkado ao lead no CRM"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Score de fit com breakdown auditável por dimensão (Calibre Scorer)"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "campo atualizado no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Decompõe a meta de aquisição (ex: X reuniões qualificadas por semana) em subtarefas distribuídas aos workers na sequência correta. Mantém o estado de cada lead no funil — desde a identificação no ICP…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR humano com draft completo, dossiê e score para aprovação ou rejeição com 1 clique antes de qualquer disparo."
    - "[ ] HITL: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o feedback detalhado do critic para reescritura manual."
    - "[ ] HITL: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente não envia com informação não verificada."
    - "[ ] HITL: Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para assumir a conversa — o squad nao conduz negociacao, apenas entrega o contexto completo e recua."
    - "[ ] HITL: Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do gestor comercial antes de qualquer envio."
---

# Orquestrar Pipeline do AI SDR Outbound Agentico

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do AI SDR Outbound Agentico |
| **status** | `pending` |
| **responsible_executor** | Maestro (Maestro — O Arquiteto de Pipeline) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Decompõe a meta de aquisição (ex: X reuniões qualificadas por semana) em subtarefas distribuídas aos workers na sequência correta. Mantém o estado de cada lead no funil — desde a identificação no ICP até o handoff para o closer. Decide a prioridade de processamento com base no score de fit, urgência do sinal e capacidade dos canais. Orquestra o fluxo ICP Cartografô -> Scout Profiler -> Calibre Scorer -> Cyrano Copywriter -> Sentinel Critic -> Cadence Dispatcher -> Pulse Analyst. Consolida todos os artefatos em um pacote de conta unificado e rastreável no ClickUp. Monitora os quality gates no Langfuse e escalona para HITL sempre que um gate falha ou uma ação irreversível está prestes a acontecer. Opera em L2: executa o ciclo completo de orquestração autonomamente, mas gates L3 bloqueiam o fluxo para aprovação humana antes de envios externos e ações com custo financeiro.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote de outreach verificado, personalizado e rastreável por lead: (1) ICP Card vivo atualizado (ICP Cartografo) salvo no ClickUp
- base de toda a prospecção
- (2) Dossiê de conta estruturado (Scout Profiler) com score de confiança, fontes verificadas e ângulos de personalização
- salvo no ClickUp e linkado ao lead no CRM
- (3) Score de fit com breakdown auditável por dimensão (Calibre Scorer)
- campo atualizado no CRM
- (4) Draft de mensagem aprovado pelo Sentinel com score de personalização e checklist de compliance
- versionado no ClickUp
- (5) Log de envio imutável com timestamp, canal, variação A/B e status (Cadence Dispatcher)
- activity no CRM e ClickUp
- (6) Análise de resposta com intenção estruturada, objeções mapeadas e próximo passo recomendado (Pulse Analyst)
- CRM atualizado, notificação ao SDR
- Todo o pipeline e auditável por design: cada artefato tem agente responsável, timestamp, veredicto do Sentinel e rastro do Langfuse
- O SDR humano opera os gates L3 e vê o contexto completo de cada lead em um único painel

## Trigger

Decompõe a meta de aquisição (ex: X reuniões qualificadas por semana) em subtarefas distribuídas aos workers na sequência correta. Mantém o estado de cada lead no funil — desde a identificação no ICP até o handoff para o closer. Decide a prioridade de processamento com base no score de fit, urgência do sinal e capacidade dos canais. Orquestra o fluxo ICP Cartografô -> Scout Profiler -> Calibre Scorer -> Cyrano Copywriter -> Sentinel Critic -> Cadence Dispatcher -> Pulse Analyst. Consolida todos os artefatos em um pacote de conta unificado e rastreável no ClickUp. Monitora os quality gates no Langfuse e escalona para HITL sempre que um gate falha ou uma ação irreversível está prestes a acontecer. Opera em L2: executa o ciclo completo de orquestração autonomamente, mas gates L3 bloqueiam o fluxo para aprovação humana antes de envios externos e ações com custo financeiro.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível
- fonte de verdade para estado do lead, activities, pipeline e log de outreach), Salesforce com Agentforce SDK ou Pipedrive como alternativas
- Enriquecimento e ICP: Clay (waterfall enrichment de 100+ fontes, workflows de enriquecimento em escala, intent signals), Apollo.io (275M+ contatos, emails verificados, intent data nativo, sequências), Cognism (dados europeus e brasileiros verificados)
- Intent data: LinkedIn Sales Navigator (sinais de mudança de liderança, expansão, hiring), Bombora (intent data B2B tópico), Google Alerts (menções de empresa e concorrentes)
- Email outreach: Instantly.ai ou Lemlist (warmup de domínio e sequências cold com rastreamento de abertura e click), SendGrid ou AWS SES (envio transacional para volume alto)
- LinkedIn: Phantombuster ou Expandi (automação de connection request e InMail dentro dos limites diários do LinkedIn)
- WhatsApp Business API: Gupshup, AiSensy ou QuickReply.ai
- plataformas purpose-built para o mercado brasileiro com conformidade pós-2024
- Voz AI: Vapi (<600ms latência) com Deepgram STT + Claude como LLM + ElevenLabs TTS para cold calls automatizadas em escala
- Calendário: Calendly ou Cal.com (booking automático via link em mensagem ou via conversação no WhatsApp)
- Gestão de tarefas e prova de trabalho: ClickUp (artefatos verificáveis por task
- ICP card, dossiê, draft aprovado com score, log de envio, análise de resposta) conectado ao Maestro via MCP ou webhook
- Orquestração multi-agente: LangGraph (controle fino de estado do funil, grafos de decisão por lead) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (traces OTEL por agente, quality gates dev 70% / staging 85% / prod 95% task success, dashboard de performance do squad)
- No-code complementar: n8n para automacoes de integracao entre ferramentas (pilar comum de agencias agenticas 2026)
- conecta webhooks, CRM events e notificacoes sem codigo custom
- Notificações internas: Slack ou WhatsApp do SDR humano para alertas de HITL urgentes e leads FIRE detectados

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Sentinel antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de outreach verificado, personalizado e rastreável por lead: (1) ICP Card vivo atualizado (ICP Cartografo) salvo no ClickUp
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloquei…
- [ ] Gate HITL respeitado: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para…
- [ ] Gate HITL respeitado: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR h… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o f… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente nã… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para a… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ICP Cartografo detecta shift significativo de mercado (nova objecao emergindo em >30% das respostas, queda de >20% no reply rate em 2 semanas consecutivas): al… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out ou resposta negativa agressiva: processado pelo Pulse Analyst, sequência cancelada automaticamente, CRM atualizado, notificação ao SDR para decisão sob… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** ICP Cartografo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
