# Squad de Triagem, Roteamento e Priorização de Tickets

> Ticket certo, fila certa, no primeiro toque — zero reassignment, SLA intacto.

**Área:** Operações & CS · **TopSquad:** O1 Atendimento & Suporte Conversacional · **Prioridade:** must‑have · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Tickets chegam sem classificação semântica, são roteados manualmente por triadores sobrecarregados e priorizados por FIFO (ordem de chegada) em vez de impacto de negócio. Resultado: misrouting de 35-60% dos tickets, reassignments que consomem 40% do tempo do agente humano, SLA violado em casos críticos que chegam tarde demais à fila certa. O squad classifica intenção + urgência + impacto em menos de 30 segundos por ticket, aplica taxonomia estruturada no ClickUp e despacha para o agente/fila corretos no primeiro toque.

## Impacto esperado

Redução de reassignments de ~40% para <5% (estimativa baseada em benchmarks de Zendesk/Intercom 2024); tempo médio até primeira resposta qualificada cai de 4-8h para <15min; SLA compliance em tickets críticos sobe de ~60% para >95%; liberação de 2-4 FTEs de triagem manual para trabalho de alto valor. ROI estimado: para equipes de 10+ agentes, payback em 60-90 dias considerando custo de token Sonnet (~$0.003 por ticket classificado) vs. custo de triagem humana (~R$1,50-3,00/ticket). Volume de 500 tickets/dia = economia de R$22-45k/mês em triagem.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `triador-mor` · Triador-Mor | Triador-Mor (persona: Viktor, chefe de triagem sênior com 10 anos em NOC/CS) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `lara` · Lara | Lara — Classificadora de Intenção | L1 · worker autônomo | `classificar-intencao.md` |
| `dante` · Dante | Dante — Árbitro de Prioridade | L1 · worker autônomo | `classificar-prioridade-ticket.md` |
| `enzo` · Enzo | Enzo — Despachante de Fila | L2 · orquestra / decide | `selecionar-fila-destino.md` |
| `bela` · Bela | Bela — Contextualista de Conta | L1 · worker autônomo | `enriquecer-contexto-cliente.md` |
| `rex` · Rex | Rex — Detector de Duplicatas e Agrupamento | L2 · orquestra / decide | `detectar-e-agrupar-duplicatas.md` |
| `faq-l0` · FAQ/L0 | Nina — Respondente de Auto-Resolução (FAQ/L0) | L3 · aprovação humana | `autoresponder-consultas.md` |
| `auditor-de-roteamento` · Auditor de Roteamento | Auditor de Roteamento — Sócrates | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-triagem-roteamento-priorizacao:triador-mor` (ou instale via `npx squads add ./ops-cs-triagem-roteamento-priorizacao`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-triagem-roteamento-priorizacao-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Confiança de classificação < 0.75 (Lara sinalizou ambiguidade): humano revisa intenção antes do roteamento prosseguir
- Ticket P1 criado: notificação imediata para supervisor via Slack com justificativa do score, supervisor confirma ou rebaixa prioridade em até 5min
- Intenção de churn/cancelamento detectada (intent_l1=churn): roteamento bloqueado automaticamente até CS Manager aprovar estratégia de resposta (L3 por risco de perda de receita)
- Rex detecta surto (SURGE): incident manager humano é notificado e confirma se é incidente real antes de agrupar tickets — evita falso positivo que agruparia tickets distintos
- Nina tentou auto-resolução mas confidence < 0.90: agente humano recebe ticket com contexto da tentativa e decide a resposta final
- Novo tipo de intenção detectado (não mapeado na taxonomia): Triador-Mor para o fluxo e aciona ops lead para expandir a taxonomia antes de processar o lote
- Auditoria do Sócrates aponta drift de acurácia < 85%: revisão semanal obrigatória com ops lead para recalibrar pesos da matriz de roteamento

## KPIs

- % de roteamento correto no primeiro toque (target: >95%, baseline estimado 60-65%)
- Taxa de reassignment após triagem automática (target: <5%, baseline ~35-40%)
- Tempo médio até atribuição qualificada — ticket entra até agente certo ter o ticket (target: <2min, baseline 4-8h com triagem manual)
- SLA compliance em tickets P1/P2 (target: >98%, baseline ~60%)
- Taxa de auto-resolução pelo Nina (target: 20-30% do volume de FAQ/L0, 0% de falsos positivos)
- Acurácia de classificação de intenção (target: >90%, medido pelo Sócrates em amostragem diária)
- Tickets agrupados como surto vs. processados individualmente (eficiência do Rex em eventos de incidente)
- Custo por ticket triado (tokens + infra, target: <R$0,05 por ticket para volume acima de 200/dia)

## Integrações

- ClickUp (Brain2 / Autopilot Agents + API): hub central de tickets, aplicação de tags, setagem de assignee/fila/SLA deadline, campo de routing_justification, dashboard de métricas
- WhatsApp Business API: canal de entrada de tickets (mensagens de texto + transcrição de áudios via ASR PT-BR)
- HubSpot / Salesforce CRM: busca de tier de cliente, ARR, health score, histórico de interações para Bela e Dante
- ChurnZero / Custify: health score, eventos de uso, risco de churn para cálculo de prioridade pelo Dante
- Zendesk / Intercom: sistemas de helpdesk alternativos de entrada de tickets (via webhooks ou MCP server)
- Slack: notificações de tickets P1 para supervisores, alertas de surto para incident manager, alertas de drift de acurácia para ops lead
- Langfuse: observabilidade OTEL completa de cada classificação (latência, confidence scores, tokens, quality gates por ambiente)
- Supabase / Postgres: estado persistente do squad (taxonomia viva, matriz de roteamento, histórico de classificações para auditoria do Sócrates, cache de embeddings do Rex)
- MCP Servers (camada de integração universal): MCP ClickUp, MCP CRM, MCP helpdesk — abstraem chamadas de API para os workers

## Entregável (prova de trabalho)

Ticket com taxonomia completa no ClickUp: tags de intent_l1, intent_l2, priority_tier (P1-P4), canal, produto/módulo, cliente_tier + assignee/fila de destino setados + sla_deadline definido + campo routing_justification preenchido com texto legível ('Cliente Enterprise P1 — Bug crítico em módulo de pagamentos com impacto em 47 usuários, risco de churn alto — roteado para Fila Suporte Técnico L2, SLA 2h') + briefing de conta da Bela anexado. Este é o artefato verificável (prova de trabalho) auditável pelo Sócrates e pelo ops lead.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Incident Response Squad (5 ag) — base direta para o módulo de detecção de surto do Rex e lógica de agrupamento de tickets em incidentes; reutilizar o padrão de correlação de alertas e escalação
- Data Quality Guardian (5 ag) — padrão de validação contínua e auditoria de amostragem que o Sócrates usa; reutilizar a arquitetura de critic com threshold de qualidade e alertas de drift
- Skeptic Protocol (5 ag) — arquitetura de red-team/QA que inspira o papel do Sócrates; reutilizar o padrão de verificação adversarial pré-despacho e o loop de feedback para recalibração

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O1 · TopSquad de Atendimento & Suporte Conversacional** — Resolve, tria, escala e assiste — toda a linha de frente em um cérebro só.

- **Missão:** A linha de frente inteira: resolve o Tier-1 em texto e voz (PT-BR), tria e prioriza tickets, decide quando escalar para humano (handoff) e assiste o agente humano quando ele assume. Um único cérebro de atendimento, multicanal.
- **Por que consolidar:** Os cinco vivem na mesma conversa do cliente — só atuam em momentos diferentes (resolver, triar, escalar, assistir). Mantê-los separados quebrava o contexto a cada passagem de bastão. Unidos, a conversa flui do bot ao humano e de volta sem reiniciar, com triagem e copiloto compartilhando o mesmo estado.
- **Squads irmãos:** Suporte Conversacional Multicanal (Tier-1), Voz-IA para Atendimento Telefônico (PT-BR), Triagem, Roteamento e Priorização de Tickets, Handoff Orchestrator HITL, Copiloto do Agente Humano

## Estrutura

```
ops-cs-triagem-roteamento-priorizacao/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
