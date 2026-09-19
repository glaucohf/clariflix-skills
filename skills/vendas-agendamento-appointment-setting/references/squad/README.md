# Squad de Agendamento — Appointment Setting

> Do lead ao calendário confirmado: zero atrito, zero no-show, zero slot perdido.

**Área:** Vendas · **TopSquad:** V3 Scoring, Roteamento & Agendamento · **Prioridade:** must‑have · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Reuniões não marcadas e no-shows derrubam o funil. Coordenar agenda manualmente entre lead e vendedor gera atrito, perda de slots e taxa alta de faltas sem lembretes e reagendamento automáticos. O squad elimina o gargalo humano no meio do funil: conduz o lead ao booking, integra calendário, confirma, lembra e reagenda sem intervenção manual — transformando sinais de intenção em reuniões realizadas.

## Impacto esperado

Redução de 60-80% no tempo médio de lead-to-booked (de dias para minutos). Taxa de no-show cai de 30-45% para abaixo de 10% com sequência automática de lembretes multicanal. Recuperação de 25-35% dos leads que seriam descartados por falta de follow-up. ROI estimado: para um funil de 200 leads/mês com ticket médio de R$15k e taxa de fechamento de 20%, recuperar 30 reuniões adicionais/mês representa R$900k de pipeline incremental. Payback do squad em menos de 30 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Maestro — Orquestrador de Agendamento | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Rádar — Worker de Qualificação Conversacional | L1 · worker autônomo | `qualificar-lead-conversacionalmente.md` |
| `slot` · Slot | Slot — Worker de Agendamento e Booking | L2 · orquestra / decide | `criar-evento.md` |
| `vigil` · Vigil | Vigil — Worker de Confirmação e Lembrete | L2 · orquestra / decide | `enviar-lembretes-agendados.md` |
| `bounce` · Bounce | Bounce – Worker de Reagendamento e Recuperação | L2 · orquestra / decide | `reagendar-oportunidades-perdidas.md` |
| `intell` · Intell | Intell — Worker de Enriquecimento pré-Reunião | L2 · orquestra / decide | `enriquecer-dossie-lead.md` |
| `pulse` · Pulse | Pulse — Worker de Lead Scoring e Priorização | L1 · worker autônomo | `priorizar-leads.md` |
| `sentinela` · Sentinela | Sentinela — Critic e Verifier de Mensagens e Compliance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-agendamento-appointment-setting:maestro` (ou instale via `npx squads add ./vendas-agendamento-appointment-setting`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-agendamento-appointment-setting-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 – Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar abordagem e personalização antes do envio.
- L3 – Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial fora da política padrão).
- L3 – Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nova tentativa.
- L2 – Notificação ao closer/SDR quando lead muda de COLD para HOT (score sobe 30+ pontos em 24h) para decisão de abordar manualmente em vez de deixar o squad rodar sozinho.
- L2 — Alerta ao gerente de vendas quando taxa de no-show da semana ultrapassar threshold configurado (ex: >20%) — indica problema sistêmico que requer revisão de ICP ou abordagem.
- L1 — Revisão humana do briefing pre-reunião antes do envio ao closer, opcional mas recomendado nas primeiras 2 semanas de operação do squad para calibragem.

## KPIs

- Lead-to-Booked Rate: % de leads qualificados que chegam ao agendamento confirmado (meta: >40%, benchmark atual típico: 15-25%)
- Time-to-Book: tempo médio do primeiro contato até o booking confirmado (meta: <4h, hoje tipicamente dias)
- No-Show Rate: % de reuniões agendadas que não acontecem (meta: <10%, benchmark: 25-40%)
- Reschedule Recovery Rate: % de no-shows recuperados via reagendamento automático (meta: >30%)
- Confirmation Rate: % de leads que confirmam presença antes da reunião (meta: >85%)
- Briefing Delivery Rate: % de reuniões confirmadas que o closer recebe briefing com >1h de antecedência (meta: 100%)
- Slot Utilization: % de slots de calendário do closer preenchidos por semana (meta: >80% da capacidade configurada)
- Task Success Rate por ambiente: dev 70% / staging 85% / prod 95% (quality gates Langfuse)
- Custo por reunião agendada: tokens + custo de API / número de reuniões realizadas (meta: <R$15/reunião)

## Integrações

- CRM: HubSpot (MCP nativo disponível) ou Pipedrive ou Salesforce — fonte de verdade de leads, deals e histórico
- Calendário: Google Calendar API ou Microsoft Outlook/Graph API — leitura de disponibilidade e criação de eventos
- Agendamento: Calendly API (alternativa ao calendário direto, mais simples para B2C)
- WhatsApp Business API: Gupshup, AiSensy ou Interakt — canal principal de comunicação no Brasil
- Email: SMTP transacional (SendGrid, Resend) ou Gmail API para lembretes e confirmações por email
- Videochamada: Google Meet API ou Zoom API — geração de link único por reunião
- Enriquecimento: Apollo.io API (275M+ contatos) ou Clay — dados firmográficos e de contato
- Observabilidade: Langfuse (OTEL) — rastreamento de todas as tarefas, evals e quality gates
- Gestão de Tarefas: ClickUp — prova de trabalho por task, artefatos verificáveis
- Notificações Internas: Slack webhook ou email — alertas de no-show, leads quentes, aprovações L3
- Voz (opcional avançado): Vapi ou Retell AI — ligação automática de lembrete ou confirmação por voz

## Entregável (prova de trabalho)

Booking Confirmation Package — artefato verificavel gerado para cada reuniao realizada, contendo: booking_confirmation.json (dados do evento), reminder_log.json (historico de lembretes enviados), pre_meeting_brief.md (dossie do lead para o closer), lead_priority_queue.json (snapshot do score no momento do agendamento), e validation_log.json do Sentinela (prova de que todas as mensagens passaram pelo critic). Disponivel no CRM e no ClickUp como task concluida com todos os artefatos anexados.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM — base para gestão de leads e integração com CRM, adaptável como camada de estado do funil e histórico de interações do Maestro
- Flywheel Core (4 agentes autônomos) — arquitetura de agentes em loop contínuo, reutilizável como base do ciclo de lembrete-confirmação-reagendamento do Vigil e Bounce
- Data Quality Guardian (5 agentes) — base para o Sentinela validar qualidade dos dados antes de cada envio externo, evitando mensagens com variáveis não substituídas ou dados incorretos

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V3 · TopSquad de Scoring, Roteamento & Agendamento** — Pontua, decide o dono certo e entrega a reunião confirmada — sem mão humana no meio.

- **Missão:** A cadeia de decisão pós-qualificação: pontua o lead, decide quem o atende (território/skill/carga) e o conduz ao calendário confirmado com lembretes anti-no-show e briefing pré-reunião. Score → route → book em um fluxo só.
- **Por que consolidar:** São três elos de uma corrente única — o score define a prioridade que define o roteamento que define o agendamento. Separados, cada um relia o CRM e recalculava o estado do lead. Unificados, o mesmo modelo de priorização alimenta diretamente o booking.
- **Squads irmãos:** Lead Scoring Preditivo & Priorização, Roteamento Inteligente de Leads, Agendamento — Appointment Setting

## Estrutura

```
vendas-agendamento-appointment-setting/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
