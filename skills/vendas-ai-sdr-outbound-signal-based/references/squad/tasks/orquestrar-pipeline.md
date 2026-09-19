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
    descricao: "Pacote de outreach verificado e rastreável por lead: (1) Dossiê de conta estruturado (Sherlock) salvo no ClickUp e CRM, (2) Draft de mensagem aprovado pelo Argus com score de personalização e checklist de compliance, (3) Log de envio com timestamp e canal no CRM e ClickUp, (4) Score de lead atualizado com breakdown (Magnus), (5) Análise de resposta com intenção e próxima ação sugerida (Lumen)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Todo o pipeline é auditável: cada artefato tem prova de trabalho com agente responsável, timestamp e veredicto do critic"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe o sinal bruto (webhook, evento de CRM, trigger de intent data), decompoe em subtarefas, roteia para os workers corretos na sequencia correta, mantem estado do lead no funil, consolida os outpu…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo."
    - "[ ] HITL: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial."
    - "[ ] HITL: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual."
    - "[ ] HITL: Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo."
    - "[ ] HITL: Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach."
---

# Orquestrar Pipeline do AI SDR Outbound Signal-Based

**Task ID:** `nexusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do AI SDR Outbound Signal-Based |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — O Maestro Comercial) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o sinal bruto (webhook, evento de CRM, trigger de intent data), decompoe em subtarefas, roteia para os workers corretos na sequencia correta, mantem estado do lead no funil, consolida os outputs em um artefato de conta unificado e decide se escalona para HITL ou dispara o outreach. Opera em L2: propoe e executa a sequencia de trabalho, mas gates L3 param o fluxo para aprovacao humana antes de acoes irreversiveis.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote de outreach verificado e rastreável por lead: (1) Dossiê de conta estruturado (Sherlock) salvo no ClickUp e CRM, (2) Draft de mensagem aprovado pelo Argus com score de personalização e checklist de compliance, (3) Log de envio com timestamp e canal no CRM e ClickUp, (4) Score de lead atualizado com breakdown (Magnus), (5) Análise de resposta com intenção e próxima ação sugerida (Lumen)
- Todo o pipeline é auditável: cada artefato tem prova de trabalho com agente responsável, timestamp e veredicto do critic

## Trigger

Recebe o sinal bruto (webhook, evento de CRM, trigger de intent data), decompoe em subtarefas, roteia para os workers corretos na sequencia correta, mantem estado do lead no funil, consolida os outputs em um artefato de conta unificado e decide se escalona para HITL ou dispara o outreach. Opera em L2: propoe e executa a sequencia de trabalho, mas gates L3 param o fluxo para aprovacao humana antes de acoes irreversiveis.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível), Pipedrive ou Salesforce
- fonte de verdade para estado do lead e log de atividades
- Enriquecimento de dados: Clay (enriquecimento em escala via workflows), Apollo.io (275M+ contatos, intent data, sequências)
- Email: SendGrid ou AWS SES (envio transacional), Instantly.ai ou Lemlist (warmup de domínio e sequências cold)
- WhatsApp Business API: Gupshup, AiSensy ou QuickReply.ai (crítico para o mercado brasileiro)
- LinkedIn: Phantombuster ou Expandi (automação de InMail/connection request dentro dos limites)
- Voz AI: Vapi (<600ms latência) com Deepgram STT + Claude/GPT LLM + ElevenLabs TTS para cold calls automatizadas
- Calendário: Calendly ou Cal.com (booking automático via link ou conversacional)
- Intent data e sinais: LinkedIn Sales Navigator, Bombora (intent data B2B), Google Alerts (menções de empresa)
- Gestão de tarefas e prova de trabalho: ClickUp (artefatos verificáveis por task
- dossiê, draft aprovado, log de envio)
- Orquestração: LangGraph (controle fino de estado do funil) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (OTEL) para quality gates dev 70% / staging 85% / prod 95% task success
- Notificações internas: Slack ou WhatsApp do SDR humano para alertas de HITL e leads HOT

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argus antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de outreach verificado e rastreável por lead: (1) Dossiê de conta estruturado (Sherlock) salvo no ClickUp e CRM, (2) Draft de mensagem aprovado pelo Arg…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossi…
- [ ] Gate HITL respeitado: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do…
- [ ] Gate HITL respeitado: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação ant… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Unsubscribe ou resposta negativa agressiva: processado pelo Lumen, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
