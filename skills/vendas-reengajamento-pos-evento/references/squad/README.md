# Squad de Reengajamento Pós-Evento e Webinar

> Transforma lista fria de evento em pipeline quente em 48 horas — antes que o concorrente perceba que você estava no mesmo stand.

**Área:** Vendas · **TopSquad:** V4 Nurture, Follow-up & Reativação · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Listas de participantes de webinars, feiras e eventos esfriam em 72 horas. O follow-up manual e lento, genérico ('foi um prazer te conhecer') e não escala: um SDR humano consegue processar 20-30 contatos/dia com qualidade; uma feira gera 200-500 leads. Sem segmentação automática por sinal de engajamento (ficou até o final? fez pergunta? visitou o estande? assistiu ao replay?) e sem personalização baseada no contexto do evento, o ROI de marketing de evento nunca aparece no pipeline. O squad processa toda a lista em até 48h pós-evento, segmenta por grau de engajamento, enriquece cada contato com dossiê de conta, dispara sequências hiperpersonalizadas por canal, qualifica automaticamente os responsivos e entrega apenas SQLs aquecidos para o closer.

## Impacto esperado

Empresas com ticket médio de R$10-50k que participam de 4-8 eventos/ano investem R$50-200k em estandes, patrocínios e produção sem converter a lista em pipeline sistematicamente. ROI estimado: squad aumenta taxa de conversão lista->SQL de 2-5% (manual/generico) para 15-25% (automatizado/hiperpersonalizado) — multiplicador de 4-5x no pipeline gerado por evento. Para uma empresa que gera 300 leads por evento com ticket médio R$20k e taxa de fechamento de 20%: (300 leads x 20% SQL x 20% fechamento x R$20k) = R$240k de receita por evento usando o squad, vs. R$60k na média manual. Payback do squad em 1 evento. Benefícios secundários: redução de 70% no tempo de SDR para follow-up pós-evento, 100% dos leads contactados nas primeiras 48h (vs. <30% no modelo manual), dados de evento integrados ao CRM para análise de ROI por canal de evento.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `claude-opus` · Claude Opus | Radar — Maestro de Reengajamento (Claude Opus) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `recon` · Recon | Recon — Worker de Ingestão e Segmentação de Lista | L1 · worker autônomo | `processar-lista-de-participantes.md` |
| `sherlock-evento` · Sherlock Évento | Sherlock Évento — Worker de Enriquecimento de Conta | L1 · worker autônomo | `enriquecer-dossie-contato.md` |
| `alta-intencao` · Alta Intenção | Cypher — Worker de Outreach Score A (Alta Intencao) | L3 · aprovação humana | `agendar-reuniao-demo.md` |
| `engajamento-medio` · Engajamento Médio | Nova — Worker de Outreach Score B (Engajamento Médio) | L2 · orquestra / decide | `enviar-mensagem-adicional.md` |
| `argos-evento` · Argos Evento | Argos Evento — Worker de Qualificação Pós-Resposta | L2 · orquestra / decide | `conduzir-qualificacao-conversacional.md` |
| `eco-evento` · Eco Evento | Eco Evento — Worker de Nurture Pos-Evento de Longo Prazo | L2 · orquestra / decide | `gerenciar-leads-baixo-engajamento.md` |
| `atlas-evento` · Atlas Evento | Atlas Evento — Worker de Agendamento Contextualizado | L2 · orquestra / decide | `agendar-reuniao-contextualizada.md` |
| `vigilia` · Vigilia | Vigília — Critic de Mensagem, Personalização e Compliance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-reengajamento-pos-evento:claude-opus` (ou instale via `npx squads add ./vendas-reengajamento-pos-evento`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-reengajamento-pos-evento-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer aprovação do closer responsável antes do primeiro envio
- Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento
- Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática
- Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana
- Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação
- Lead que solicita opt-out ou demonstra irritação com o contato — intervenção humana obrigatória, registro de opt-out e revisão da cadência
- Inconsistência crítica detectada entre dados do evento e CRM (ex: lead do evento e cliente com contrato ativo cancelado) — revisão humana antes de qualquer contato
- Volume de lista acima de 1.000 contatos em evento único — revisão humana da segmentação antes do disparo em massa

## KPIs

- Cobertura de lista: % de participantes do evento contactados em até 48h (meta: 100% em 48h vs. <30% manual)
- Taxa de conversão lista->SQL: benchmark atual vs. pós-squad (meta: 15-25% vs. 2-5% manual — multiplicador 4-5x)
- Tempo de primeiro contato pós-evento: meta < 2h para Score A, < 6h para Score B, < 24h para Score C
- Taxa de resposta por score: Score A meta >35%, Score B meta >15%, Score C meta >5%
- Taxa de agendamento de reunião: % de SQLs que chegam a reunião confirmada (meta: >50% dos SQLs)
- Show rate: % de reuniões que efetivamente ocorrem (meta: >80% com lembretes contextualizados do Atlas Evento)
- Taxa de reativação de nurture: % de leads Score C/B-inativo que se reativam na sequência de 4-8 semanas (meta: >8%)
- ROI por evento: pipeline gerado (R$) / investimento total no evento incluindo squad (meta: ROI >3x em 90 dias)
- Task success rate no Langfuse: dev 70% / staging 85% / prod 95%
- Taxa de compliance Vigília: % de mensagens aprovadas sem intervenção HITL (meta: >90% aprovação automática)
- Custo por SQL gerado de evento: total do squad / SQLs gerados por evento (meta: redução de 60% vs. SDR manual)

## Integrações

- CRM: HubSpot (MCP disponível) / Pipedrive / Salesforce / RD Station CRM — fonte de verdade de contatos, dedup, histórico e pipeline de oportunidades
- Plataformas de webinar: Zoom Webinar (API de participantes + engajamento), Hotmart, Eduzz, StreamYard — fonte de metadados de engajamento pós-evento
- Plataformas de evento físico: Sympla, Eventbrite, sistemas proprietários de badge scan — fonte de lista de participantes e dados de visita ao estande
- WhatsApp Business API: Gupshup / AiSensy / Interakt / QuickReply.ai — canal principal de outreach pós-evento no Brasil (Score A e B)
- Email: Gmail API / Outlook API / SendGrid — cadencias de email para todos os scores, nurture de longo prazo
- LinkedIn: LinkedIn API / Phantombuster — outreach Score A via DM apos tentativas de WhatsApp/email sem resposta
- Enriquecimento: Clay + Apollo (275M+ contatos) — dossiê de conta e contato para todos os leads novos
- Calendário: Google Calendar / Outlook Calendar — agendamento e lembretes do Atlas Evento
- Observabilidade: Langfuse (OTEL) — quality gates, evals, rastreamento de tasks por agente e por evento
- Gestão de tarefas: ClickUp — artefatos verificáveis por task, prova de trabalho auditável, dashboard de ROI por evento
- Notificações internas: Slack / WhatsApp Business — alertas de SQL gerado e HITL para closers e gestão
- Videoconferência: Google Meet / Zoom / Teams — links de reunião gerados pelo Atlas Evento com pauta personalizada

## Entregável (prova de trabalho)

Relatório de ROI Por Evento: documento estruturado (PDF exportável do ClickUp + nota no CRM) gerado automaticamente 30 dias após cada evento, contendo: total de participantes processados, breakdown por score (A/B/C), taxa de contato em 48h, taxa de resposta por canal e score, SQLs gerados com ficha de qualificação, reuniões agendadas e realizadas, oportunidades abertas no CRM com valor estimado, pipeline influenciado pelo evento, custo por SQL e ROI calculado. Auditável em tempo real no ClickUp com tasks vinculadas por lead e por evento. Dashboard de KPIs comparativo entre eventos para identificar melhores canais e temas de evento por ROI.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM (squads.sh) — base para gestão de leads, integração conversacional com CRM e lógica de segmentação; já tem estrutura de recepção de leads e roteamento que acelera a construção do Orchestrator Radar e do Recon
- Skeptic Protocol (5 agentes de red-team/QA, myclaude) — base direta para o Critic Vigília; lógica de verificação adversarial, validação de claims e compliance antes de ações externas se encaixa exatamente no papel de verificação pós-segmentação do squad
- Data Quality Guardian (5 agentes de qualidade de dados, squads.sh) — base para o Sherlock Evento e o Recon; já implementa dedup, normalização de campos e enriquecimento de dados que são o core do processamento inicial da lista de evento

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V4 · TopSquad de Nurture, Follow-up & Reativação** — Nenhum lead morto: reaquece deals parados, leads frios e públicos pós-evento.

- **Missão:** O squad da memória longa do funil: detecta qualquer lead/deal que esfriou — sem resposta, estagnado no pipeline ou inerte após um evento/webinar — e dispara a cadência de reaquecimento certa para o motivo certo.
- **Por que consolidar:** Os três faziam a mesma coisa — reaquecer quem parou de avançar — variando só o gatilho (silêncio, deal estagnado, fim de evento). Compartilham biblioteca de cadências, lógica de decaimento e regra de "quando desistir". Um squad só evita três motores de cadência concorrendo pelo mesmo lead.
- **Squads irmãos:** Follow-up, Nurture e Reativação, Recuperação de Oportunidades Estagnadas, Reengajamento Pós-Evento e Webinar

## Estrutura

```
vendas-reengajamento-pos-evento/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
