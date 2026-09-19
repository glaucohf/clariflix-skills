# Intelligent Timing Orchestrator

> A mensagem certa perde para o momento errado: este squad aprende quando cada usuario abre, responde e converte — e envia exatamente nesse instante.

**Área:** Marketing · **TopSquad:** M2 Performance: Paid Media, CRO & Attribution · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Campanhas de aquisicao disparam touchpoints em horarios padronizados (ex: terca as 10h) ignorando que cada usuario tem uma janela de receptividade individual. O resultado e mensuravel: open rate abaixo de 20% em email, reply rate de cold outreach abaixo de 3%, e fadiga acelerada de canal que queima listas inteiras em semanas. O problema se agrava em sequencias multicanal (email + LinkedIn + WhatsApp) onde a sobreposicao de toques no mesmo horario parece spam mesmo com conteudo relevante. O Intelligent Timing Orchestrator constroi um perfil de comportamento temporal por usuario — horario de pico de leitura, canal preferido por momento do dia, frequencia ideal entre toques — e usa esse modelo para agendar cada mensagem na janela de maxima probabilidade de engajamento. Mensuravel por: open/reply rate por toque vs. benchmark de envio padrao, uplift de conversao em sequencias otimizadas vs. controle, e indice de fadiga de canal (unsubscribes/spam reports) ao longo do tempo.

## Impacto esperado

Empresas que implementam send-time optimization reportam uplift medio de 25-40% em open rate de email e 15-30% em reply rate de outreach (benchmarks HubSpot, Instantly, Salesloft 2024-2025). Para uma sequencia de cold outreach com 1.000 prospects/mes e ticket medio de R$30k: se o timing otimizado eleva de 2% para 3.5% a taxa de resposta positiva, sao 15 reunioes adicionais por mes — a R$30k de ticket e taxa de fechamento de 25%, e R$112.500/mes em pipeline incremental. ROI do squad estimado em 2-3 meses. KPI primario: uplift de open rate >= 25% e reply rate >= 20% em relacao ao baseline de envio padrao, medido em A/B test nos primeiros 60 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `kronos` · Kronos | Kronos — Orquestrador de Timing | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `sirius` · Sirius | Sirius — Behavioral Historian | L2 · orquestra / decide | `calcular-janelas-receptividade.md` |
| `pulsar` · Pulsar | Pulsar — Channel & Fatigue Analyst | L2 · orquestra / decide | `monitorar-saude-de-canal.md` |
| `helios` · Helios | Helios — Timing Model Builder | L2 · orquestra / decide | `construir-modelo-preditivo-timing.md` |
| `vega` · Vega | Vega — Sequence Architect | L1 · worker autônomo | `otimizar-sequencias-outreach.md` |
| `nexus` · Nexus | Nexus — Send Execution & Scheduler | L3 · aprovação humana | `enviar-mensagens-agendadas.md` |
| `aura` · Aura | Aura — Critic & Compliance Verifier | L3 · aprovação humana | `verificar-compliance-e-qualidade.md` |
| `lumina` · Lumina | Lumina — Insights & Attribution Reporter | L2 · orquestra / decide | `analisar-dados-de-envio.md` |
| `aura-2` · Aura 2 | Aura — Critic & Compliance Verifier | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-intelligent-timing:kronos` (ou instale via `npx squads add ./marketing-intelligent-timing`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-intelligent-timing-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e sequencia sao foco prioritario antes de iniciar o modelo (L3, gate de entrada)
- Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualquer envio em producao (L3, gate de seguranca antes de go-live)
- Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente do nivel de automacao configurado (L3, por volume e irreversibilidade)
- Quando Channel Health Score de qualquer canal cai abaixo de 50 — Aura bloqueia o canal e Kronos escala para decisao humana sobre pausa, reducao de frequencia ou investigacao de causa raiz (L3, saude de canal critica)
- Promocao de modelo candidato de Helios para producao — uplift confirmado no A/B test e condição necessaria mas nao suficiente; Head de Aquisicao aprova a troca de modelo que afeta toda a base (L3, decisao de alto impacto)
- Quando Aura detecta violacao de compliance legal (opt-out nao respeitado, envio fora de horario legal, campo LGPD violado) — independente de qualquer autonomia configurada, eleva imediatamente para responsavel legal/CMO (L3 emergencial)
- Revisao trimestral de thresholds de timing e limites de frequencia — calibracao dos parametros do modelo com Sales Lead e CMO para alinhar com estrategia comercial atual (L1, ciclo recorrente de governanca)

## KPIs

- Uplift de open rate vs. baseline: meta >= 25% de melhora em 60 dias (medido em A/B test com grupo controle de envio no horario padrao)
- Uplift de reply rate vs. baseline: meta >= 20% de melhora em 60 dias para cold outreach multicanal
- Channel Health Score: todos os canais ativos acima de 70/100 mantidos ao longo do tempo (fadiga controlada)
- Taxa de unsubscribe: abaixo de 0.3% por mes em email e abaixo de 1% de opt-out em WhatsApp (reducao de fadiga mensuravel)
- Pipeline incremental gerado por timing otimizado: reunioes adicionais por mes atribuiveis ao uplift de reply rate vs. controle
- Cobertura de Timing Profile: >= 80% dos leads ativos com perfil de confianca > 50% em 90 dias (maturidade do modelo)
- Latencia de agendamento: tempo entre calculo de janela otima e disparo efetivo do toque < 5 minutos (eficiencia operacional de Nexus)
- Compliance rate: 100% dos envios passando pela auditoria de Aura sem violacao de compliance legal (zero tolerancia)

## Integrações

- HubSpot CRM — leitura de historico de engajamento por contato, escrita de Timing Profile como propriedade customizada por lead, webhooks de eventos de abertura/clique/resposta, sincronizacao de opt-out list em tempo real
- Instantly.ai — plataforma de cold email outreach: leitura de metricas de engajamento por sequencia e por toque, escrita de agendamentos otimizados via API, sincronizacao de blacklist e bounce list
- LinkedIn Sales Navigator — leitura de eventos de visualizacao de perfil e interacoes, agendamento de InMails via API no horario otimizado
- WhatsApp Business API (via Patagon AI ou BotPenguin) — envio de mensagens de outreach e follow-up no horario calculado por Helios, leitura de status de leitura (double-check azul) como sinal de engajamento para Sirius
- ClickUp — prova de trabalho: task automatica por ciclo de schedule gerado, dashboard de KPIs de timing (open rate, reply rate, uplift vs. baseline, Channel Health Score por canal), alertas de anomalia como tasks de alta prioridade
- Langfuse — observabilidade OTEL de todos os agents, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latencia do pipeline de agendamento, evals de qualidade do modelo de timing
- n8n — orquestracao dos workflows de webhooks de engajamento, filas de retry de envio, sincronizacao de opt-out entre plataformas e notificacoes para o time (complemento no-code para integracao entre sistemas)
- Google Sheets / Looker Studio — dashboard executivo de Uplift Report mensal para apresentacao ao board (Lumina output renderizado em visualizacao acessivel sem acesso ao sistema)
- Mailchimp / ActiveCampaign (opcional) — integracao para squads que usam email marketing em adicao ao cold outreach, leitura de metricas de campanha nurture para incluir no modelo de Sirius

## Entregável (prova de trabalho)

Timing Intelligence System operacional com: (1) Timing Profile individual por lead publicado como propriedade customizada no CRM (janela otima de abertura por canal, probabilidade estimada, confianca do modelo), (2) Schedule otimizado diario para todos os leads ativos nas sequencias (proximas 48h com canal, horario e justificativa), (3) Timing Performance Report semanal no ClickUp com uplift observado vs. baseline por canal e segmento com significancia estatistica, (4) Channel Health Dashboard com Score 0-100 por canal e historico de 12 semanas, (5) A/B Test Report mensal com uplift confirmado e recomendacao de evolucao do modelo, (6) Uplift Report trimestral com ROI calculado do squad (pipeline incremental / custo operacional), (7) Audit Log completo de todos os envios executados com timestamp, canal, lead e status para rastreabilidade e compliance.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 agentes, qualidade de dados) — acelera a construcao de Aura (Critic): a logica de validacao, deteccao de anomalias e scoring de qualidade ja esta implementada; customizar as regras para validacao de compliance de envio, deteccao de opt-out nao sincronizado e spot-check de personalizacao de copy
- Athenaeum (11 agentes, inteligencia estrategica) — base para Lumina (Insights Reporter): a estrutura de coleta, sintese e apresentacao de inteligencia estrategica e reutilizavel para o modulo de Uplift Report e deteccao de anomalias; adaptar os agentes de analise para o dominio de metricas de engajamento e attribution de pipeline
- Skeptic Protocol (5 agentes, red-team/QA) — base direta para o padrao critico de Aura: o framework de questionamento sistematico e verificacao adversarial ja implementado pode ser adaptado para o contexto de auditoria de compliance de envio e validacao de qualidade de copy antes do disparo

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M2 · TopSquad de Performance: Paid Media, CRO & Attribution** — O loop fechado da mídia: investe, otimiza a página, acerta o timing e prova o que deu retorno.

- **Missão:** O ciclo fechado de performance: aloca e otimiza mídia paga, melhora a landing page para converter, dispara no melhor horário e mede a atribuição real — fechando o loop investir → converter → medir → reinvestir.
- **Por que consolidar:** Mídia, CRO, timing e atribuição são o mesmo loop de otimização visto de ângulos diferentes — e a atribuição é justamente o sinal que deveria realimentar a mídia. Em squads isolados, o de mídia não enxergava o que a atribuição via, e o de CRO otimizava cego. Unidos, a medição fecha o ciclo.
- **Squads irmãos:** Paid Media Autopilot, CRO & Landing Page Agêntico, Intelligent Timing Orchestrator, Funnel Analytics & Attribution

## Estrutura

```
marketing-intelligent-timing/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
