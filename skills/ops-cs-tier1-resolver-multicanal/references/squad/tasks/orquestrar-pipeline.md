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
    descricao: "Por ticket resolvido: Task no ClickUp com (1) transcrição completa da interação, (2) intenção classificada com confiança score, (3) worker utilizado, (4) ações de sistema executadas com IDs de referência, (5) score do Critic por dimensão, (6) status de resolução (autônomo / escalado / pendente), (7) timestamp de cada step do pipeline"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Dashboard Langfuse com: deflection rate em tempo real, CSAT agregado, distribuição de intenções, critic rejection breakdown, SLA heatmap por canal e por intenção"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe mensagem bruta do canal (chat/email/WhatsApp/voz), normaliza o texto (ASR se áudio), classifica intenção primária e secundária com confiança score, enriquece com contexto do cliente (histórico…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário"
    - "[ ] HITL: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo"
    - "[ ] HITL: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados"
    - "[ ] HITL: Terceira interação na mesma sessão sem resolução confirmada pelo cliente"
    - "[ ] HITL: Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação"
---

# Orquestrar Pipeline do Suporte Conversacional Multicanal

**Task ID:** `nexusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Suporte Conversacional Multicanal (Tier-1 Resolver)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Suporte Conversacional Multicanal |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Orchestrator de Atendimento) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe mensagem bruta do canal (chat/email/WhatsApp/voz), normaliza o texto (ASR se áudio), classifica intenção primária e secundária com confiança score, enriquece com contexto do cliente (histórico de pedidos, tier de conta, sentimento acumulado), roteia para o worker especializado correto, aguarda output, aciona o Critic antes do envio, registra prova de trabalho no ClickUp e decide escalonamento HITL quando confiança < threshold ou ação é irreversível.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Por ticket resolvido: Task no ClickUp com (1) transcrição completa da interação, (2) intenção classificada com confiança score, (3) worker utilizado, (4) ações de sistema executadas com IDs de referência, (5) score do Critic por dimensão, (6) status de resolução (autônomo / escalado / pendente), (7) timestamp de cada step do pipeline
- Dashboard Langfuse com: deflection rate em tempo real, CSAT agregado, distribuição de intenções, critic rejection breakdown, SLA heatmap por canal e por intenção

## Trigger

Recebe mensagem bruta do canal (chat/email/WhatsApp/voz), normaliza o texto (ASR se áudio), classifica intenção primária e secundária com confiança score, enriquece com contexto do cliente (histórico de pedidos, tier de conta, sentimento acumulado), roteia para o worker especializado correto, aguarda output, aciona o Critic antes do envio, registra prova de trabalho no ClickUp e decide escalonamento HITL quando confiança < threshold ou ação é irreversível.

## Knowledge base (o que o executor consulta)

- WhatsApp Business API (canal primário BR
- áudio, texto, imagem)
- Zendesk / Intercom
- helpdesk, ticket management, KB
- ClickUp (Brain2 / MCP server)
- hub de tasks e prova de trabalho espelhando AIOX
- CRM: HubSpot ou Salesforce
- dados de conta, health score, histórico
- ERP / OMS
- consulta de pedidos, status, estoque (API REST ou MCP customizado)
- Gateway de pagamento: Stripe / Pagarme / Iugu
- consulta e submissao de refund
- Logística reversa: Correios, Jadlog, Total Express
- geração de etiquetas e rastreamento
- Deepgram Nova-2 ou Whisper Large-v3
- ASR PT-BR para áudio do WhatsApp e voz
- ElevenLabs ou Azure TTS
- síntese de voz PT-BR para respostas em canal de voz
- call center e telefonia
- Slack – notificações de escalonamento, alertas de churn, briefings do Pulse
- Supabase / Postgres – estado dos agentes, health scores, logs de interações, fila de handoff
- observabilidade OTEL, evals, tracing de cada step do pipeline, quality gates
- Claude Agent SDK / LangGraph – orquestração multi-agente
- Email (SMTP/SendGrid)
- canal de suporte por email

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argus antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Por ticket resolvido: Task no ClickUp com (1) transcrição completa da interação, (2) intenção classificada com confiança score, (3) worker utilizado, (4) ações…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário
- [ ] Gate HITL respeitado: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo
- [ ] Gate HITL respeitado: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Terceira interação na mesma sessão sem resolução confirmada pelo cliente | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Menção de palavras-chave de risco: 'advogado', 'PROCON', 'Reclame Aqui', 'processo', 'imprensa', 'TV' | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Solicitacao de troca/devolucao fora do prazo de politica ou em categoria inelegivel — Volta escalona para decisao humana com contexto | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Health score do cliente cai abaixo de 45 durante a interação — Pulse dispara alerta para CSM responsável | BLOQUEIA até decisão humana |
| VETO-009 | HITL — Áudio com qualidade ASR < 0.80 de confiança — Vox marca para revisão humana antes de processar | BLOQUEIA até decisão humana |
| VETO-010 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Prism
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
