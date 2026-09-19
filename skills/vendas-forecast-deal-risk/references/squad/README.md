# Squad de Forecast de Pipeline e Risco de Deal

> Seu pipeline para de mentir: detecta risco antes do silêncio virar perda.

**Área:** Vendas · **TopSquad:** V6 RevOps: Higiene de CRM & Forecast · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Forecast por planilha e intuicao erra em media 40-60% no mid-market brasileiro. Deals morrem em silencio por falta de engajamento, ausencia de proximo passo definido ou estagnacao de estagio. O gestor so descobre na reuniao de pipeline — tarde demais para agir. Sem visibilidade preditiva, o closers empurra os deals errados, o board recebe numeros inventados e o ciclo se repete.

## Impacto esperado

Redução de 35-50% no erro de forecast (accuracy de 55% para 85%+). Detecção precoce de 70%+ dos deals em risco com 7-14 dias de antecedência para intervenção. Redução de 20-30% no ciclo de vendas por priorização correta de atenção do closer. ROI estimado: para uma empresa com R$500k/mês em pipeline, recuperar 10% dos deals em risco = R$50k/mês de receita preservada. Payback do squad em 30-60 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `cassandra` · Cassandra | Cassandra — Oráculo Comercial | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `argus` · Argus | Argus — Vigia de Sinais | L0 · worker determinístico | `monitorar-deals-ativos.md` |
| `oracle` · Oracle | Oracle — Calculista de Risco | L1 · worker autônomo | `calcular-score-risco-deal.md` |
| `sibila` · Sibila | Síbila — Vidente do Forecast | L1 · worker autônomo | `gerar-forecast-pipeline.md` |
| `hermes` · Hermes | Hermes — Alertador de Risco | L3 · aprovação humana | `formatar-alertas-contextualizados.md` |
| `mnemosine` · Mnemosine | Mnemosine — Arquivista de Deals | L1 · worker autônomo | `analisar-deals-fechados.md` |
| `cronos` · Cronos | Cronos — Gestor de Próximo Passo | L2 · orquestra / decide | `sugerir-proximo-passo.md` |
| `nemesis` · Nemesis | Nemesis — Verificador de Alertas | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-forecast-deal-risk:cassandra` (ou instale via `npx squads add ./vendas-forecast-deal-risk`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-forecast-deal-risk-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora da empresa
- L3 — Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM
- L2 — Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa
- L2 — Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle
- L1 — Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal

## KPIs

- Forecast Accuracy (%): meta de 80%+ (baseline típico do cliente: 45-60%)
- Deal Risk Detection Rate (%): percentual de deals perdidos que tiveram alerta prévio com 7+ dias de antecedência — meta 70%+
- Mean Time to Alert (MTTA): tempo médio entre sinal de risco detectado e alerta enviado ao closer — meta <2h
- Intervenção Rate (%): percentual de deals em risco onde o closer tomou ação após alerta — meta 60%+
- Deal Recovery Rate (%): percentual de deals Vermelhos que voltaram a Verde após intervenção — meta 25%+
- Deals sem Próximo Passo (%): percentual do pipeline ativo sem próxima atividade definida — meta <10%
- Squad Accuracy Improvement (% ao mês): evolução da accuracy do modelo mês a mês pelo feedback loop da Mnemosine — meta +2-5pp/mês nos primeiros 3 meses

## Integrações

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce — fonte primária de dados de deals, atividades e estágios
- ClickUp — gestão de tarefas de intervenção, registro de próximo passo, prova de trabalho por deal
- Slack — canal principal de alertas para closers e gestores (webhook)
- WhatsApp Business API (Gupshup / AiSensy) — alertas urgentes para closers via WhatsApp
- Email (SMTP/SendGrid) — digest semanal para gestores e report para board
- Langfuse (OTEL) — observabilidade do squad, quality gates (70% dev / 85% staging / 95% prod), rastreio de accuracy do forecast
- Google Calendar / Outlook Calendar — verificação de disponibilidade para sugestões de próximo passo do Cronos
- Clay / Apollo — enriquecimento de dados do contato quando necessário para contexto do alerta
- Notion / Google Sheets — export do relatório de forecast para clientes sem dashboard dedicado

## Entregável (prova de trabalho)

Painel de Pipeline Intelligence (atualizado a cada 4h) com: (1) lista priorizada de deals em risco com score, categoria e ação recomendada; (2) forecast de 30/60/90 dias em três cenários com gap para meta; (3) alertas contextualizados por deal entregues no canal preferido do closer; (4) relatório mensal de aprendizado com accuracy do forecast e ROI das intervenções. Artefato verificável: JSON de estado do pipeline com timestamp, acessível via ClickUp e exportável para CRM.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 ag) — base para o módulo de higiene do CRM que alimenta o Argus; os agentes de validação e dedup podem ser reaproveitados diretamente para garantir que o Argus recebe dados limpos antes de calcular sinais de risco
- Skeptic Protocol (5 ag, red-team/QA) — base para o Nemesis (Critic); o framework de red-team adversarial do Skeptic Protocol pode ser adaptado para o papel de verificador de alertas, especialmente nos checks de coerência do score e tom da mensagem
- Genius Athena Strange (5 ag, decisão sob incerteza) — base para o módulo de cenários da Sibila; o framework de decisão sob incerteza ajuda a construir os três cenários de forecast (pessimista/provável/otimista) com raciocínio estruturado sobre probabilidades

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V6 · TopSquad de RevOps: Higiene de CRM & Forecast** — Dados limpos viram previsão confiável — o sistema nervoso do pipeline.

- **Missão:** A camada de verdade do funil: mantém o CRM limpo e enriquecido (dedupe, normalização, campos faltantes) e, sobre esses dados confiáveis, projeta o forecast e sinaliza deals em risco antes que escorreguem.
- **Por que consolidar:** Forecast só é confiável sobre dados limpos — eram causa e efeito separados em dois squads. O squad de higiene gerava o insumo que o de forecast consumia. Unidos, a limpeza acontece a serviço da previsão, num loop contínuo de qualidade-de-dado → previsão.
- **Squads irmãos:** Higiene e Enriquecimento de CRM (RevOps), Forecast de Pipeline & Risco de Deal

## Estrutura

```
vendas-forecast-deal-risk/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
