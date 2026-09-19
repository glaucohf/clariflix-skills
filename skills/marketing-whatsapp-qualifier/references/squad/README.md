# WhatsApp Qualifier

> Nenhum lead esfria mais: qualificacao conversacional purpose-built no WhatsApp que responde em segundos, trata objecao como um bom SDR e agenda reuniao antes da concorrencia ligar.

**Área:** Marketing · **TopSquad:** M5 Captura, Qualificação & Reativação de Leads · **Prioridade:** must‑have · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Leads de topo chegam pelo WhatsApp e esfriam por demora de resposta (media de mercado: 5-47 horas para primeiro contato humano) e qualificacao inconsistente entre atendentes — cada SDR qualifica de um jeito, gerando pipeline ruidoso. Pos-proibicao Meta de chatbots genericos (2024-2025), solucoes de automacao de massa foram banidas. O resultado mensuravel e critico: taxa de qualificacao < 30% dos leads recebidos, show-rate de reunioes abaixo de 50% e custo de SDR humano para cobrir o volume total. O squad entrega qualificacao conversacional purpose-built no WhatsApp — alinhada as regras pos-proibicao Meta — com resposta em < 5 minutos, BANT/MEDDIC estruturado, tratamento de objecoes baseado em playbook real e agendamento direto no calendario do closer.

## Impacto esperado

Para empresas com 100-500 leads/mes pelo WhatsApp, o squad reduz tempo de primeira resposta de horas para < 5 minutos (+900% de velocidade), eleva taxa de qualificacao de 25-30% para 65-75% (+150%) e aumenta show-rate de reunioes de 40-50% para 65-75% (+40%). ROI estimado: empresa com 200 leads/mes, ticket medio R$15k, taxa de fechamento de 20% — passando de 15 para 35 reunioes qualificadas/mes (+20 oportunidades), ao custo de 1 SDR humano (~R$4-6k/mes), o squad gera R$40-60k de pipeline adicional mensalmente. Payback em 30-45 dias de operacao. KPI primario: taxa de qualificacao (lead -> reuniao agendada) acima de 50% em 60 dias de producao.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Maestro Comercial | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `vance` · Vance | Vance — Conversational Qualifier | L2 · orquestra / decide | `qualificar-conversas-whatsapp.md` |
| `rex` · Rex | Rex — Real-Time Enrichment Agent | L2 · orquestra / decide | `enriquecer-lead-em-tempo-real.md` |
| `mia` · Mia | Mia — Smart Scheduling Agent | L2 · orquestra / decide | `agendar-reuniao-lead.md` |
| `lilo` · Lilo | Lilo — Funnel Analyst Agent | L1 · worker autônomo | `analisar-funil-de-qualificacao.md` |
| `kira` · Kira | Kira — Compliance & Voice Guardian | L3 · aprovação humana | `validar-mensagem-playbook.md` |
| `nova` · Nova | Nova — Attribution & ROI Agent | L1 · worker autônomo | `calcular-roi-do-squad.md` |
| `kira-2` · Kira 2 | Kira — Compliance & Voice Guardian | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-whatsapp-qualifier:orion` (ou instale via `npx squads add ./marketing-whatsapp-qualifier`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-whatsapp-qualifier-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado (L3, sem aprovacao o squad nao avanca)
- Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao. Kira ja auditou conformidade, mas humano decide se o tom esta certo (L3, gate obrigatorio)
- Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa manualmente antes de Vance responder (L3, acao irreversivel: primeira impressao com conta estrategica)
- Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion antes de Vance ser atualizado (L2, recorrente toda segunda-feira)
- Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 com head de vendas e Kira antes de producao
- Decisao de escalada por irritacao detectada — quando Vance detecta 3+ sinais de irritacao em sequencia, Orion alerta SDR humano via notificacao para assumir a conversa. Humano decide se assume imediatamente ou deixa Vance tentar uma ultima mensagem de reengajamento (L3)
- Revisao mensal de metricas com Nova — CEO/CMO aprova redistribuicao de budget por fonte de lead com base no ROI report de Nova (L3, envolve gasto financeiro)

## KPIs

- Tempo de primeira resposta: meta < 5 minutos para 95% dos leads (baseline atual a medir no Discovery, tipicamente 2-47 horas)
- Taxa de qualificacao (lead -> reuniao agendada): meta > 50% em 60 dias de producao (baseline tipico: 20-30%)
- Show-rate de reunioes agendadas pelo squad: meta > 65% (baseline tipico: 40-50%). Mia otimiza por slots de melhor historico
- Lead Score medio de leads enviados para o closer: meta > 7.0/10 (indica qualidade da qualificacao, nao apenas volume)
- Taxa de escalada desnecessaria para SDR humano: meta < 15% do total de leads (escaladas devem ser casos reais de VIP ou objecao critica, nao falhas de Vance)
- Compliance Score de Kira: 100% das versoes de playbook publicadas com score >= 90/100. Zero flags criticos em producao
- Taxa de abandono por etapa do funil de qualificacao: rastreada por Lilo, meta de reducao de 10% por mes durante os 3 primeiros meses
- ROI do squad (Nova): pipeline gerado >= 10x o custo mensal do squad em 90 dias de producao
- Quality Gate Langfuse: task success rate >= 95% em producao (Vance respondendo adequadamente, Rex enriquecendo, Mia agendando sem erros)

## Integrações

- WhatsApp Business API via BSP purpose-built pos-proibicao Meta — Patagon AI (LATAM-first, recomendado), Leadsales ou BotPenguin como fallback. Gateway principal de entrada e saida de mensagens
- HubSpot CRM — registro automatico de leads qualificados, campos customizados de BANT (Budget, Authority, Need, Timeline), Lead Score pos-qualificacao, historico de conversa estruturado, trigger de criacao de oportunidade pos-qualificacao
- Google Calendar / Calendly — disponibilidade em tempo real para Mia agendar reunioes, criacao de eventos com dados do lead, link de videoconferencia automatico (Google Meet / Zoom)
- Clay — waterfall enrichment em tempo real por Rex (firmographic, technographic, intent signals). Opcional se cliente ja tem Clay; fallback para Apollo direto
- Apollo.io — prospecting e enriquecimento de contatos B2B como fonte primaria ou backup do Clay
- ClickUp — prova de trabalho central: task automatica por lead qualificado, dashboard de metricas do squad (taxa de qualificacao, show-rate, ROI), briefing pre-reuniao para o closer, historico de playbook versions
- Langfuse — observabilidade OTEL de todos os agents, quality gates por ambiente (dev 70% / staging 85% / prod 95% task success), rastreamento de cada conversa como trace completo, evals de qualidade de resposta de Vance
- n8n — orquestracao de webhooks e workflows de notificacao (complemento no-code): alerta de lead VIP para SDR, notificacao de no-show para reengajamento, relatorio semanal de Lilo para Slack/email
- Slack / Email — notificacoes de escalada para SDR humano (lead VIP, irritacao, objecao critica), alertas de anomalia de Lilo, relatorio semanal de performance do squad
- Meta Business Suite / BSP Dashboard — monitoramento de saude da conta WhatsApp Business (Quality Rating, Phone Number Status, Message Template Status) integrado com Kira para alertas precoces de risco de banimento

## Entregável (prova de trabalho)

Artefato principal verificavel no ClickUp: Lead Qualification Record — por cada lead processado pelo squad, um registro estruturado contendo: (1) Transcript da conversa WhatsApp com etapas de qualificacao marcadas, (2) BANT Score preenchido por campo (0-3 por dimensao), (3) Lead Score total pos-qualificacao (0-10), (4) Enrichment Record de Rex com dados da empresa e contato, (5) Status final (Qualificado+Agendado / Qualificado+Pendente / Desqualificado com motivo / Escalado para SDR com motivo), (6) Link do evento de calendario criado por Mia (se agendado), (7) Briefing pre-reuniao de 5 linhas para o closer. Artefatos secundarios: Playbook Conversacional versionado (Kira-approved), Dashboard semanal de metricas (Lilo), ROI Report mensal (Nova), Audit Log de conformidade Meta (Kira).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mae Intuitiva CRM (CRM/leads) — base direta para a logica de registro de leads qualificados no CRM e triggers de follow-up: reutilizar a estrutura de estados de lead, fluxo de nurture e notificacoes para SDR que este squad ja implementa, customizando para o contexto WhatsApp
- Skeptic Protocol (5 agentes, red-team/QA) — acelera a construcao de Kira (Compliance Guardian): a logica de adversarial review, checklist de validacao multi-camada e veredicto APPROVED/NEEDS_REVISION/BLOCKED e diretamente reutilizavel, apenas trocando as regras de QA de codigo por regras de conformidade Meta/LGPD
- Landing Funnel (13 agentes, landing/CRO) — complementar para o pipeline de aquisicao: os agentes de analise de funil e otimizacao de conversao podem ser integrados com Nova (Attribution Agent) para fechar o loop entre campanha de aquisicao -> lead no WhatsApp -> reuniao agendada -> deal fechado

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M5 · TopSquad de Captura, Qualificação & Reativação de Leads** — Da captura à qualificação e ao reaquecimento da base adormecida.

- **Missão:** A ponte entre Marketing e Vendas: pontua e roteia os leads gerados pelas campanhas, qualifica via WhatsApp e reativa a base adormecida que o marketing já pagou para adquirir. Garante que nenhum lead capturado se perca.
- **Por que consolidar:** Os três operam sobre o mesmo objeto — o lead que o marketing capturou — em momentos distintos: na entrada (score/router), na conversa (WhatsApp) e no esfriamento (reativação). É o mesmo ciclo de vida do lead de marketing, partido em três. Espelha o V2/V3/V4 de Vendas; aqui fica do lado de marketing por nutrir o lead pago.
- **Squads irmãos:** Lead Scoring & Router, WhatsApp Qualifier, Dormant Lead Reactivation

## Estrutura

```
marketing-whatsapp-qualifier/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
