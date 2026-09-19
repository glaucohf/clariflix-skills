# Squad de Suporte Conversacional Multicanal (Tier-1 Resolver)

> Resolve 70% dos tickets de suporte sem toque humano — em menos de 90 segundos, em qualquer canal.

**Área:** Operações & CS · **TopSquad:** O1 Atendimento & Suporte Conversacional · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

60-80% dos tickets sao repetitivos (status de pedido, FAQ, troca, refund, billing): consomem o time humano inteiro, estouraram SLA e geram fila cronica. O squad resolve esses tickets de forma autonoma com orchestrator Opus roteando intencao para workers Sonnet especializados por dominio, com critic QA validando tom, compliance e alucinacao antes de qualquer envio externo.

## Impacto esperado

Deflection rate target: 65-75% dos tickets Tier-1 resolvidos sem intervenção humana. Redução de 50-60% no custo por ticket (de R$18-35 para R$4-8). CSAT pós-resolução automática: meta >= 4.2/5. Tempo de primeira resposta: de 4-8h para < 90 segundos. SLA compliance rate: de 60-70% para > 95%. Para uma operação com 3.000 tickets/mês, ROI estimado: R$35-55k/mês em custo evitado + redução de 2-3 headcounts de atendimento Tier-1.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · Nexus | Nexus — Orchestrator de Atendimento | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `prism` · Prism | Prism — Worker de Status & Logística | L2 · orquestra / decide | `consultar-status-de-pedido.md` |
| `volta` · Volta | Volta — Worker de Troca & Devolução | L3 · aprovação humana | `processar-troca-e-devolucao.md` |
| `flux` · Flux | Flux — Worker de Refund & Billing | L3 · aprovação humana | `processar-refund-e-cobranca.md` |
| `sage` · Sage | Sage — Worker de FAQ & KB | L1 · worker autônomo | `responder-perguntas-frequentes.md` |
| `vox` · Vox | Vox — Agente de Voz & Áudio | L2 · orquestra / decide | `processar-audio-voz.md` |
| `hermes` · Hermes | Hermes — Agente de Handoff & Escalonamento HITL | L2 · orquestra / decide | `gerenciar-escalonamento.md` |
| `pulse` · Pulse | Pulse — Agente de Health Score & Churn Signal | L2 · orquestra / decide | `monitorar-sinais-de-churn.md` |
| `argus` · Argus | Argus — Critic de Qualidade & Compliance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-tier1-resolver-multicanal:nexus` (ou instale via `npx squads add ./ops-cs-tier1-resolver-multicanal`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-tier1-resolver-multicanal-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário
- Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo
- Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados
- Terceira interação na mesma sessão sem resolução confirmada pelo cliente
- Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação
- Menção de palavras-chave de risco: 'advogado', 'PROCON', 'Reclame Aqui', 'processo', 'imprensa', 'TV'
- Solicitacao de troca/devolucao fora do prazo de politica ou em categoria inelegivel — Volta escalona para decisao humana com contexto
- Health score do cliente cai abaixo de 45 durante a interação — Pulse dispara alerta para CSM responsável
- Áudio com qualidade ASR < 0.80 de confiança — Vox marca para revisão humana antes de processar

## KPIs

- Deflection Rate: % de tickets Tier-1 resolvidos autonomamente sem toque humano (meta: >= 65%)
- CSAT pós-resolução automática: pesquisa de 1 pergunta pós-chat (meta: >= 4.2 / 5.0)
- Tempo de Primeira Resposta (FRT): tempo entre abertura e primeira resposta do sistema (meta: < 90 segundos em 95% dos casos)
- SLA Compliance Rate: % de tickets respondidos dentro do SLA contratado (meta: > 95%)
- Taxa de Escalonamento Desnecessária: % de tickets escalados que o humano resolveu igual ao que o agente teria feito (meta: < 10%)
- Custo por Ticket Automatizado: custo total de tokens + infra / numero de tickets resolvidos (meta: < R$0.80 por ticket)
- Critic Rejection Rate: % de respostas rejeitadas pelo Argus antes do envio (meta: < 8% — indica qualidade dos workers)
- Churn Prevented Rate: % de clientes com health score < 60 que não churnam após intervenção do Pulse (meta: > 40%)
- Containment Rate por Intencao: deflection separado por categoria (status/refund/troca/faq) para identificar gaps
- Hallucination Rate no Critic: % de respostas com flag de alucinação detectada (meta: < 2%)

## Integrações

- WhatsApp Business API (canal primário BR — áudio, texto, imagem)
- Zendesk / Intercom — helpdesk, ticket management, KB
- ClickUp (Brain2 / MCP server) — hub de tasks e prova de trabalho espelhando AIOX
- CRM: HubSpot ou Salesforce — dados de conta, health score, histórico
- ERP / OMS — consulta de pedidos, status, estoque (API REST ou MCP customizado)
- Gateway de pagamento: Stripe / Pagarme / Iugu — consulta e submissao de refund
- Logística reversa: Correios, Jadlog, Total Express — geração de etiquetas e rastreamento
- Deepgram Nova-2 ou Whisper Large-v3 — ASR PT-BR para áudio do WhatsApp e voz
- ElevenLabs ou Azure TTS — síntese de voz PT-BR para respostas em canal de voz
- Aircall — call center e telefonia
- Slack – notificações de escalonamento, alertas de churn, briefings do Pulse
- Supabase / Postgres – estado dos agentes, health scores, logs de interações, fila de handoff
- Langfuse — observabilidade OTEL, evals, tracing de cada step do pipeline, quality gates
- Claude Agent SDK / LangGraph – orquestração multi-agente
- Email (SMTP/SendGrid) — canal de suporte por email

## Entregável (prova de trabalho)

Por ticket resolvido: Task no ClickUp com (1) transcrição completa da interação, (2) intenção classificada com confiança score, (3) worker utilizado, (4) ações de sistema executadas com IDs de referência, (5) score do Critic por dimensão, (6) status de resolução (autônomo / escalado / pendente), (7) timestamp de cada step do pipeline. Dashboard Langfuse com: deflection rate em tempo real, CSAT agregado, distribuição de intenções, critic rejection breakdown, SLA heatmap por canal e por intenção.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 ag, red-team/QA) – base para o Critic Argus: lógica de adversarial review, rubrica de validação e rejeição com feedback estruturado
- Incident Response Squad (5 ag) — base para o Agente Hermes de Handoff: logica de escalonamento, triagem por criticidade e notificacao multicanal
- Data Quality Guardian (5 ag, qualidade de dados) — base para o Pulse Health Score: deteccao de anomalia em streams de dados de comportamento e geracão de alertas com contexto

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O1 · TopSquad de Atendimento & Suporte Conversacional** — Resolve, tria, escala e assiste — toda a linha de frente em um cérebro só.

- **Missão:** A linha de frente inteira: resolve o Tier-1 em texto e voz (PT-BR), tria e prioriza tickets, decide quando escalar para humano (handoff) e assiste o agente humano quando ele assume. Um único cérebro de atendimento, multicanal.
- **Por que consolidar:** Os cinco vivem na mesma conversa do cliente — só atuam em momentos diferentes (resolver, triar, escalar, assistir). Mantê-los separados quebrava o contexto a cada passagem de bastão. Unidos, a conversa flui do bot ao humano e de volta sem reiniciar, com triagem e copiloto compartilhando o mesmo estado.
- **Squads irmãos:** Suporte Conversacional Multicanal (Tier-1), Voz-IA para Atendimento Telefônico (PT-BR), Triagem, Roteamento e Priorização de Tickets, Handoff Orchestrator HITL, Copiloto do Agente Humano

## Estrutura

```
ops-cs-tier1-resolver-multicanal/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
