# ABM Signal Orchestrator

> Cada sinal de intent em conta estrategica vira campanha coordenada antes que o concorrente responda.

**Área:** Marketing · **TopSquad:** M1 Demand Gen & ABM Orchestration · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Contas estrategicas recebem abordagem generica e descoordenada entre marketing e vendas, desperdicando momentum de intent. O squad detecta sinais de compra em tempo real (job postings, funding rounds, tech stack changes, engajamento com conteudo), enriquece o contexto da conta, e dispara orchestracao ABM multicanal personalizada — ads, outreach, conteudo e ativacao de vendas — de forma sincronizada e mensuravel.

## Impacto esperado

Penetração em contas-alvo sobe de ~12% para ~35% em 90 dias. Pipeline ABM gerado aumenta 3-5x vs abordagem genérica. Engajamento multi-stakeholder (2+ contatos por conta) reduz ciclo de vendas em 25-40%. ROI estimado: para consultoria Lendar a R$15k/squad, cliente target gera R$150k-500k em pipeline incremental no primeiro trimestre — payback em semanas.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · Nexus | Nexus — Orquestrador ABM | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Radar — Agente de Sinais de Intent | L1 · worker autônomo | `monitorar-sinais-de-intent.md` |
| `atlas` · Atlas | Atlas — Agente de Enriquecimento e ICP Profiler | L1 · worker autônomo | `enriquecer-conta-icp.md` |
| `vox` · Vox | Vox — Agente de Copy e Mensagem ABM | L2 · orquestra / decide | `gerar-copy-personalizada.md` |
| `pixel` · Pixel | Pixel — Agente de Ads e Media Programática | L3 · aprovação humana | `criar-audiencias-customizadas.md` |
| `hermes` · Hermes | Hermes — Agente de Outreach e Sequenciamento SDR | L3 · aprovação humana | `sequenciar-contato-multicanal.md` |
| `chronos` · Chronos | Chronos — Agente de Timing e Orquestração de Canais | L2 · orquestra / decide | `orquestrar-canais-de-mensagens.md` |
| `prism` · Prism | Prism — Agente de Analytics e Atribuição ABM | L1 · worker autônomo | `consolidar-sinais-engajamento-conta.md` |
| `aegis` · Aegis | Aégis — Verificador de Qualidade e Compliance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-abm-signal-orchestrator:nexus` (ou instale via `npx squads add ./marketing-abm-signal-orchestrator`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-abm-signal-orchestrator-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plataformas de ads
- L3 — Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad
- L3 — Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio
- L2 — Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha completa
- L2 — Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana sobre próximos passos
- L1 — Curadoria do Account Universe Map: adicionar/remover contas do universo ABM e ajustar Tiers requer input estratégico humano (revisão quinzenal)

## KPIs

- Penetração em contas-alvo: % de contas Tier 1 com pelo menos 2 stakeholders engajados (meta: subir de ~12% para ~35% em 90 dias)
- Pipeline ABM gerado: R$ em oportunidades abertas no CRM atribuídas ao programa ABM (meta: 3-5x vs baseline sem ABM)
- Engajamento multi-stakeholder: media de contatos engajados por conta Tier 1 (meta: >= 2.5 por conta)
- Tempo de resposta a sinal de intent: de detecção do sinal até primeiro toque personalizado (meta: < 4 horas para Tier 1)
- Taxa de abertura de email ABM: benchmark > 35% (vs 20% de campanha generica)
- Taxa de resposta positiva de outreach: benchmark > 8% (vs 2% de cold outreach gênerico)
- Reuniões agendadas por conta Tier 1: meta >= 1 meeting/conta nos primeiros 60 dias de ativação
- Task Success Rate no Langfuse: >= 85% em staging, >= 95% em produção

## Integrações

- HubSpot CRM — fonte de verdade de contas, contatos, deals e histórico de interações; receptor de todos os touches e atualizações de engajamento
- Clay — waterfall enrichment com 100+ fontes para Account Intelligence Profile; source primária de sinais de intent via Clay Intelligence
- Apollo.io — prospecting, enriquecimento de contatos, sequenciamento de email frio via Apollo Sequences
- Instantly — cold email infrastructure com alta deliverabilidade, rotação de caixas de entrada, warmup automático
- LinkedIn (via API/Phantombuster) — connection requests, messages, monitoramento de atividade de stakeholders
- Meta Business Manager — campanhas de Account-Based Advertising com custom audiences por conta
- Google Ads — campanhas RLSA e Customer Match para contas-alvo
- LinkedIn Campaign Manager — Matched Audiences por empresa e lista de contatos
- WhatsApp Business API (via Patagon AI ou Leadsales) — canal de outreach para stakeholders qualificados, pós-proibição Meta de chatbots gênericos
- ClickUp — camada de prova-de-trabalho: cada campanha ABM criada vira task com artefatos verificáveis, checklists e histórico de aprovações HITL
- Langfuse — observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95%), rastreamento de custo por campanha ABM
- Bombora / G2 / TechTarget — sinais de intent third-party por topico e categoria de produto
- Clearbit / Crunchbase — funding signals, hiring signals, tech stack changes para enriquecimento do Radar

## Entregável (prova de trabalho)

ABM Campaign Package por conta ativada — artefato verificavel no ClickUp contendo: Account Intelligence Profile (buying committee mapeado, ICP score, sinais detectados), ABM Copy Package aprovado pelo Aegis (email sequences, LinkedIn messages, ad copy, call script), cronograma de touches aprovado pelo Chronos, campanhas ativas nas plataformas de ads, sequencias ativas no CRM, e Account Engagement Dashboard com tracking em tempo real. Cada campanha e uma task no ClickUp com checklist de aprovacoes HITL, historico de versoes de copy e metricas de performance linkadas.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 ag, red-team/QA) — base direta para o agente Aegis (Crític/Verifier): a lógica de red-team e verificação adversarial do Skeptic Protocol mapeia diretamente para os 5 gates de qualidade do Aegis (brand voice, personalização, compliance, coerência, copy score)
- Athenaeum (11 ag, inteligencia estrategica) — acelera a fase Discovery e Deep Dive do squad: os agentes de pesquisa e sintese do Athenaeum podem alimentar o Atlas (ICP Profiler) com inteligencia competitiva e de mercado sobre as contas-alvo, reduzindo o tempo de setup do Account Universe Map
- Data Quality Guardian (5 ag, qualidade de dados) — acelera a confiabilidade do Account Universe Map e dos Account Intelligence Profiles: os agentes de validação e limpeza do Data Quality Guardian podem ser reutilizados para garantir que o enriquecimento do Clay não introduza dados duplicados, emails inválidos ou contatos desatualizados no pipeline ABM

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M1 · TopSquad de Demand Gen & ABM Orchestration** — Detecta a demanda antes do concorrente e orquestra o toque certo em contas e criadores.

- **Missão:** O motor de geração de demanda baseado em sinais: sente o mercado esquentando (demand sensing), seleciona contas-alvo (ABM) e criadores relevantes, e orquestra o outreach coordenado — anúncio, e-mail, conteúdo, criador — para chegar à conta no momento certo.
- **Por que consolidar:** Os quatro partem do mesmo insumo — sinais de intenção de mercado — e divergem só no destino do toque (conta, lead, criador). Demand sensing alimenta o ABM, que define quem o AI SDR aborda e quais criadores ativar. Separados, cada um tinha seu próprio radar de sinais; juntos, um radar serve a todos.
- **Squads irmãos:** ABM Signal Orchestrator, AI SDR Outbound Agêntico, Demand Sensing Radar, Influencer & Creator Outreach Agêntico

## Estrutura

```
marketing-abm-signal-orchestrator/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
