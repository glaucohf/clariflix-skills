# Squad de Lead Scoring Preditivo e Priorização

> Pare de adivinhar: o pipeline se reordena sozinho, colocando os deals mais quentes na frente do closer certo — antes que o concorrente ligue primeiro.

**Área:** Vendas · **TopSquad:** V3 Scoring, Roteamento & Agendamento · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Vendedores distribuem atencao uniformemente ou por feeling, gerando dois desperdícios simultâneos: esforço desperdiçado em leads frios (baixa taxa de conversão) e leads quentes que esfriam por falta de contato oportuno. Sem scoring contínuo e dinâmico, o forecast é impreciso, o ramp de novos SDRs é lento e o gestor não sabe onde intervir.

## Impacto esperado

Aumento de 25-40% na taxa de conversão SQL->Oportunidade por foco nos leads de score alto (benchmark: empresas com lead scoring maduro convertem 2x mais). Redução de 30% no ciclo de vendas por eliminação de nurture manual em leads frios. Forecast com 85%+ de acurácia ao substituir intuição por score probabilístico. ROI estimado: para um time de 5 SDRs gerando 200 leads/mês com ticket médio de R$15k, mover conversão de 8% para 12% representa R$120k/mês adicional — payback do squad em 30-60 dias de operação.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Maestro Comercial (Órion) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Scout de Sinais (Radár) | L1 · worker autônomo | `capturar-sinais-de-intencao.md` |
| `sherlock` · Sherlock | Detetive de Conta (Sherlock) | L1 · worker autônomo | `enriquecer-dados-firmograficos.md` |
| `vega` · Vega | Calculista de Score (Vega) | L0 · worker determinístico | `calcular-score-numerico.md` |
| `atlas` · Atlas | Estrategista de Prioridade (Atlas) | L2 · orquestra / decide | `priorizar-fila-de-contato.md` |
| `nexus` · Nexus | Cadenciador Inteligente (Nexus) | L3 · aprovação humana | `cadenciar-leads-multi-canal.md` |
| `oracle` · Oracle | Analista de Risco de Deal (Oracle) | L2 · orquestra / decide | `detectar-risco-deal.md` |
| `argus` · Argus | Guardião de Qualidade (Argus) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-lead-scoring-preditivo:orion` (ou instale via `npx squads add ./vendas-lead-scoring-preditivo`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-lead-scoring-preditivo-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes do disparo. SLA de aprovação: 2h.
- HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do Closer ou Gerente Comercial.
- HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos.
- HITL-4 (L3): Alerta de deal em risco alto — gestor recebe notificação e deve confirmar qual ação tomar (intervir diretamente, escalar para diretor, ajustar proposta) antes de qualquer comunicação automatizada.
- HITL-5 (L2): Ajuste manual de score por SDR — SDR pode adicionar nota qualitativa (ex: 'falei com o CEO, orçamento confirmado') que sobe o score manualmente, com registro no log de auditoria.
- HITL-6 (L1): Calibração mensal do modelo de scoring — analista de RevOps revisa os feature weights sugeridos pelo sistema e aprova ou ajusta antes do re-treino.

## KPIs

- Taxa de conversão SQL->Oportunidade: baseline vs pos-deploy (meta: +25% em 90 dias)
- Velocidade do pipeline: tempo médio de Lead->Oportunidade (meta: -30%)
- Acurácia de forecast: MAPE do forecast semanal vs fechamento real (meta: < 15%)
- Score de qualidade de mensagens Argus: media >= 8.0/10 sem degradacao
- Taxa de resposta a cadências automatizadas: benchmark por canal (email > 8%, WhatsApp > 25%)
- Lead rot prevention: % de Hot leads contactados dentro do SLA de 2h (meta: > 95%)
- Aproveitamento de pipeline: receita fechada / receita total em pipeline (meta: +15% vs baseline)
- Data completeness média dos leads: meta > 80% após enriquecimento
- Task success rate por ambiente: dev > 70%, staging > 85%, prod > 95% (Langfuse quality gates)
- ROI do squad: receita incremental atribuída / custo total do squad (meta: > 10x em 6 meses)

## Integrações

- CRM: HubSpot (MCP disponível) ou Pipedrive — source of truth para lead e deal data, destino de todos os score writes e activity logs
- WhatsApp Business API: Gupshup ou AiSensy — canal de outreach e recepção de sinais de engajamento (mensagem lida, respondida)
- Enriquecimento: Apollo.io (275M+ contatos) via API — firmográficos, contatos adicionais, tech stack
- Enriquecimento complementar: Clay — workflows de enriquecimento multi-fonte com waterfall
- Ads / Intent Signals: Facebook Lead Ads, Google Ads — webhooks de novos leads com UTMs completos
- Gestão de tarefas: ClickUp — Fila_do_Dia dos reps, proof-of-work por task, registro de artefatos verificáveis
- Comunicação interna: Slack — alertas de deals em risco, leads Hot sem contato, aprovações HITL
- Calendário: Google Calendar — disponibilidade dos reps para roteamento e agendamento
- Observabilidade: Langfuse (OTEL) — evals de qualidade dos agentes, quality gates por ambiente, traces de todas as chamadas LLM
- Orquestração: LangGraph + Claude Agent SDK — controle de estado do pipeline, workflows determinísticos
- Armazenamento de features: PostgreSQL/Supabase — Feature Store com histórico de scores e features por lead

## Entregável (prova de trabalho)

Pipeline Scorecard em tempo real (dashboard ClickUp + CRM): rank dos leads por probabilidade de fechamento, fila do dia por rep, alertas de risco de deal, forecast semanal com intervalo de confiança. Artefato verificável por task: cada lead processado gera um Score Object rastreável no Langfuse com trace completo (features usadas, peso de cada feature, score anterior vs atual, ação recomendada, canal selecionado). Briefing de Lead para cada Hot lead gerado pelo Nexus e aprovado via HITL.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM (squads.sh) — base para lógica de gestão de leads, eventos de CRM e nurture automatizado; adaptar o modelo de dados para incluir Score Object e Feature Store
- Data Quality Guardian (myclaude) — base para o Sherlock (enriquecimento e deduplicação) e para o pipeline de higiene de dados do CRM; reusar os 5 agentes de qualidade como sub-workers do Sherlock
- Skeptic Protocol (myclaude) — base para o Critic Argus; os 5 agentes de red-team/QA mapeiam diretamente para as 5 dimensões de validação de mensagens (personalização, factualidade, compliance, tom, CAN-SPAM)

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V3 · TopSquad de Scoring, Roteamento & Agendamento** — Pontua, decide o dono certo e entrega a reunião confirmada — sem mão humana no meio.

- **Missão:** A cadeia de decisão pós-qualificação: pontua o lead, decide quem o atende (território/skill/carga) e o conduz ao calendário confirmado com lembretes anti-no-show e briefing pré-reunião. Score → route → book em um fluxo só.
- **Por que consolidar:** São três elos de uma corrente única — o score define a prioridade que define o roteamento que define o agendamento. Separados, cada um relia o CRM e recalculava o estado do lead. Unificados, o mesmo modelo de priorização alimenta diretamente o booking.
- **Squads irmãos:** Lead Scoring Preditivo & Priorização, Roteamento Inteligente de Leads, Agendamento — Appointment Setting

## Estrutura

```
vendas-lead-scoring-preditivo/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
