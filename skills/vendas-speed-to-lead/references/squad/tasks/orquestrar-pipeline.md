---
task: claudeOpusPipeline()
responsavel: "Claude Opus"
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
    descricao: "Dossie de Lead Completo por Contato: documento estruturado (JSON + nota no CRM) contendo timestamp de cada etapa (primeiro contato, enriquecimento, qualificacao, agendamento), scorecard BANT preenchido, score de ICP, transcricao/sumario das interacoes por canal, proximo passo recomendado e closer responsavel"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Auditavel em tempo real no ClickUp com tasks vinculadas por lead"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard de KPIs atualizado em tempo real com metricas de velocidade, volume e conversao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe todo sinal de inbound (formulario preenchido, mensagem recebida, chamada entrante, click em ad), decompoe em subtarefas, mantém estado do funil no CRM, roteia para o Worker correto baseado em…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead"
    - "[ ] HITL: Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto"
    - "[ ] HITL: Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio"
    - "[ ] HITL: Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel"
    - "[ ] HITL: Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano"
---

# Orquestrar Pipeline do Speed-to-Lead

**Task ID:** `claudeOpusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Speed-to-Lead |
| **status** | `pending` |
| **responsible_executor** | Claude Opus (Maestro Comercial (Claude Opus)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe todo sinal de inbound (formulario preenchido, mensagem recebida, chamada entrante, click em ad), decompoe em subtarefas, mantém estado do funil no CRM, roteia para o Worker correto baseado em canal e contexto, consolida resultados, aciona HITL quando criterio L3 é atingido, monitora SLA de 60 segundos e escala em caso de falha.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Dossie de Lead Completo por Contato: documento estruturado (JSON + nota no CRM) contendo timestamp de cada etapa (primeiro contato, enriquecimento, qualificacao, agendamento), scorecard BANT preenchido, score de ICP, transcricao/sumario das interacoes por canal, proximo passo recomendado e closer responsavel
- Auditavel em tempo real no ClickUp com tasks vinculadas por lead
- Dashboard de KPIs atualizado em tempo real com metricas de velocidade, volume e conversao

## Trigger

Recebe todo sinal de inbound (formulario preenchido, mensagem recebida, chamada entrante, click em ad), decompoe em subtarefas, mantém estado do funil no CRM, roteia para o Worker correto baseado em canal e contexto, consolida resultados, aciona HITL quando criterio L3 é atingido, monitora SLA de 60 segundos e escala em caso de falha.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponivel) / Pipedrive / Salesforce
- fonte de verdade de leads, contatos, deals e historico
- WhatsApp Business API: Gupshup / AiSensy / Interakt / QuickReply.ai
- canal principal no Brasil, envio/recepcao de mensagens
- Voz IA: Vapi (<600ms latencia) ou Retell AI
- ligacoes de qualificacao automatizadas com voz natural
- TTS: ElevenLabs
- voz da marca para ligacoes do Vox
- STT: Deepgram
- transcricao de calls em tempo real
- Email: Gmail API / Outlook API
- cadencias de email do Eco e confirmacoes do Atlas
- Calendario: Google Calendar / Outlook Calendar
- agendamento e lembretes do Atlas
- Enriquecimento: Clay + Apollo (275M+ contatos)
- dados do Sherlock
- Intent Data: sinais de ads (Meta Ads, Google Ads) + plataformas de intent
- gatilhos para o Argos
- Observabilidade: Langfuse (OTEL)
- quality gates, evals, rastreamento de tasks por agente
- Gestao de tarefas: ClickUp
- artefatos verificaveis por task, prova de trabalho auditavel
- Notificacoes internas: Slack / WhatsApp Business
- alertas de lead quente e HITL para closers
- Videoconferencia: Google Meet / Zoom / Teams
- links de reuniao gerados pelo Atlas

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Sentinel antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossie de Lead Completo por Contato: documento estruturado (JSON + nota no CRM) contendo timestamp de cada etapa (primeiro contato, enriquecimento, qualificaca…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead
- [ ] Gate HITL respeitado: Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Reagendamento apos segundo no-show — Atlas escala para closer decidir se continua ou descarta lead | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Lead demonstra sinal negativo forte (reclamacao de contato excessivo, solicitacao de opt-out) — intervencao humana obrigatoria e imediata | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Flash
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
