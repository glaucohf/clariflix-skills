# AI Chief of Staff — Founder Office

> Seu segundo cérebro estratégico: nunca mais entre em reunião sem preparo, nunca mais perca um follow-up.

**Área:** Founder Office · **TopSquad:** F1 Chief of Staff & Clone do Founder · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

O founder gasta 8–15h/semana em prep de reuniões, triagem de contexto, cobrança de follow-ups e síntese de informações dispersas — tempo que deveria estar em decisões de alta alavancagem. Sem um Chief of Staff dedicado, objeções são antecipadas tarde, deals esfriam por falta de follow-up, e o strategic thinking fica sequestrado pelo operacional.

## Impacto esperado

Economia estimada de 8–12h/semana do founder (ROI direto se hora do founder vale R$1.000–5.000 = R$32k–240k/mês em tempo recuperado). % de reuniões com brief automatizado: meta 90% em 30 dias. Taxa de follow-ups concluídos no prazo: de ~40% manual para 85%+ automatizado. Redução de ciclo de decisão estratégica de dias para horas com deep research on-demand.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Strategic Chief of Staff | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `briefing` · Briefing | Briefing — Prep de Reunião | L2 · orquestra / decide | `preparar-briefing-de-reuniao.md` |
| `kira` · Kira | Kira — Deep Research Worker | L1 · worker autônomo | `sintetizar-fontes-abertas.md` |
| `vance` · Vance | Vance — Follow-up & Accountability Manager | L2 · orquestra / decide | `gerar-relatorio-semanal.md` |
| `sage` · Sage | Sage — Founder Clone Agent | L1 · worker autônomo | `validar-output-estrategico.md` |
| `intel` · Intel | Intel — Competitive Intelligence Monitor | L2 · orquestra / decide | `monitorar-inteligencia-competitiva.md` |
| `atlas` · Atlas | Atlas — Priority & Focus Aligner | L2 · orquestra / decide | `gerar-plano-da-semana.md` |
| `memo` · Memo | Memo — Board & Investor Communications | L3 · aprovação humana | `gerar-drafts-de-updates.md` |
| `skeptic` · Skeptic | Skeptic — Verifier & Hallucination Guard | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-ai-chief-of-staff:orion` (ou instale via `npx squads add ./founder-ai-chief-of-staff`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-ai-chief-of-staff-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design
- Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas)
- Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado
- Aprovação de escalation quando follow-up crítico está atrasado e envolve terceiros externos
- Validação do Founder Clone Agent antes de qualquer resposta ser enviada em nome do founder
- Configuração inicial do corpus do Sage (founder revisa e aprova quais comunicações entram no corpus de clonagem)

## KPIs

- Horas/semana economizadas do founder (baseline manual vs pós-squad) — meta: -8h/semana em 30 dias
- % de reuniões com brief automatizado entregue >1h antes — meta: 90% em 30 dias
- Taxa de follow-ups concluídos no prazo — meta: de ~40% para 85%+ em 60 dias
- Tempo médio de geração de meeting brief — meta: <15 minutos end-to-end
- Score de satisfação do founder com briefs (1–5 por reunião) — meta: >=4.2
- % de board/investor memos aprovados sem revisão estrutural — meta: 80% em 90 dias
- Hallucination rate nos outputs (Skeptic score <75%) — meta: <5% de artefatos bloqueados
- NPS interno do squad (founder avalia mensalmente) — meta: >=8
- Task success rate no Langfuse — meta: dev 70% / staging 85% / prod 95%

## Integrações

- Google Calendar / Outlook Calendar (agenda e eventos — trigger principal do Briefing Agent)
- Gmail / Outlook Email (ingestão de sinais, captura de commitments, envio de lembretes)
- HubSpot / Salesforce CRM (histórico de contas, deals, notas de relacionamento)
- ClickUp (gestão de tasks, follow-ups, prova de trabalho do squad)
- Notion / Mem.ai (knowledge base do founder, notas de reuniões, board packs)
- Sembly / Fireflies / Otter (transcrição automática de reuniões para captura de ações)
- Slack (entrega de briefs, alertas, digests e interface conversacional com o founder)
- LinkedIn (pesquisa de interlocutores para Kira e Intel)
- Brave Search / Perplexity MCP (deep research para Kira e Intel)
- Langfuse (observabilidade OTEL, tracing de tokens e custo por agente)
- Vector DB — Pinecone / Qdrant (corpus do founder para Sage, histórico de intel)
- Google Analytics / Metabase / Looker (métricas para Memo Agent e Atlas)

## Entregável (prova de trabalho)

Chief of Staff Weekly Pack (artefato semanal verificável): (1) Plano da Semana com top 3 prioridades e blocos de foco, (2) Meeting Briefs gerados na semana com score de qualidade, (3) Dashboard de follow-ups (prometido vs entregue, % no prazo, escalations), (4) Intel Digest semanal com movimentos de mercado relevantes, (5) Retrospectiva de foco (onde o tempo foi vs onde deveria ter ido). Tudo rastreável no ClickUp e auditável no Langfuse.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base para o pipeline de deep research do Kira e o modelo de síntese estratégica do Orion
- Genius Athena Strange (5 agentes, decisão sob incerteza) — base para o módulo de antecipação de objeções e wargaming do Skeptic
- Cognitive Fusion Lab (clone cognitivo) — base para a arquitetura do Sage (Founder Clone Agent), corpus ingestion e lógica de replicação de raciocínio

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F1 · TopSquad de Chief of Staff & Clone do Founder** — O braço executivo: agenda, reuniões, memória institucional e um twin que decide no estilo do founder.

- **Missão:** A extensão operacional do founder: gere agenda e prioridades (chief of staff), captura e processa reuniões (meeting intelligence), mantém a memória institucional e opera o digital twin que rascunha decisões/respostas no estilo e nos valores do founder.
- **Por que consolidar:** Os quatro compartilham o ativo mais raro — o contexto do founder. O clone só funciona com a memória institucional; o chief of staff age sobre as decisões das reuniões; meeting intelligence abastece a memória. Separados, cada um reconstruía o contexto do founder do zero. Unidos, há um único cérebro do founder.
- **Squads irmãos:** AI Chief of Staff, Meeting Intelligence, Clone Estratégico do Founder (Digital Twin), Knowledge Base Institucional do Founder

## Estrutura

```
founder-ai-chief-of-staff/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
