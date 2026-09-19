# Squad de Predição e Prevenção de Churn

> Detecta o cliente prestes a sair antes que ele decida — e coloca o CSM em movimento com a ação certa no momento certo.

**Área:** Operações & CS · **TopSquad:** O3 Customer Success: Onboarding, Retenção & Expansão · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Churn é detectado tarde demais — quando o cliente já decidiu cancelar — porque ninguém cruza sinais de uso, sentimento e suporte em tempo real. O time de CS só age após o aviso de cancelamento, quando a taxa de save já é < 15%. O squad cruza automaticamente dados de produto (logins, features ativas, tempo de sessão), sentimento (NPS, CSAT, transcrições de suporte) e contexto de conta (MRR, renovação próxima, tickets abertos) para gerar um health score por conta a cada 24h, identificar os 10-20% de contas em risco crítico e disparar a next-best-action prioritária como task no ClickUp para o CSM responsável — antes que o cliente chegue ao ponto de cancelar.

## Impacto esperado

Churn reduzido em 25-40% na base monitorada dentro de 90 dias. Lead time de alerta antecipado: de 0 dias (reactivo) para 21-45 dias antes do cancelamento previsto. Taxa de save pós-alerta: meta >= 35% (vs. < 15% sem o squad). Para uma base de 200 contas com MRR médio de R$3k: preservar 10 contas/mês = R$30k MRR protegido/mês = R$360k ARR. ROI do squad: payback em < 60 dias. NPS de contas monitoradas: aumento de 12-18 pontos em 6 meses. Redução de 60% no tempo do CSM em triagem manual de contas em risco (de 8h/semana para < 2h).

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · Nexus | Nexus — Analista de Churn Orchestrator | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `vega` · Vega | Vega — Sensor de Sinais de Uso e Sentimento | L0 · worker determinístico | `monitorar-sinais-de-uso-e-sentimento.md` |
| `prism` · Prism | Prism — Calculador de Health Score | L0 · worker determinístico | `calcular-health-score-composito.md` |
| `mira` · Mira | Míra — Geradora de Brief e Next-Best-Action | L1 · worker autônomo | `gerar-brief-personalizado.md` |
| `spark` · Spark | Spark — Agente de Ativação no ClickUp | L2 · orquestra / decide | `criar-task-retencao.md` |
| `iris` · Iris | Íris — Analista de Sentimento e Voz do Cliente | L1 · worker autônomo | `analisar-sentimento-cliente.md` |
| `lumen` · Lumen | Lumen — Agente de Contexto Comercial e Expansão | L1 · worker autônomo | `analisar-contexto-comercial.md` |
| `echo` · Echo | Echo — Monitor de Saúde Continua e Tendências | L2 · orquestra / decide | `monitorar-health-score.md` |
| `argus` · Argus | Argus — Critic de Qualidade de Score e Ações | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-churn-prediction:nexus` (ou instale via `npx squads add ./ops-cs-churn-prediction`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-churn-prediction-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica
- Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato
- Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados
- Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch
- Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar
- Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar task
- Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de relacionamento antes de qualquer ação automática
- Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada antes de reprocessar

## KPIs

- Churn Rate na Base Monitorada: redução percentual de churn nas contas cobertas pelo squad vs baseline dos 90 dias anteriores (meta: -25% a -40%)
- Lead Time de Alerta: média de dias entre o primeiro alerta gerado pelo squad e o evento de cancelamento (meta: >= 21 dias de antecedência)
- Taxa de Save pós-Alerta: % de contas com alerta CRÍTICO/ALTO que não churnam após intervenção do CSM dentro de 30 dias (meta: >= 35%)
- MRR Protegido por Mês: soma do MRR de contas salvas atribuível às intervenções disparadas pelo squad (meta: > 5x o custo mensal do squad)
- Tempo do CSM em Triagem Manual: horas/semana que o CSM gasta identificando contas em risco sem suporte do squad (meta: < 2h/semana, redução de 60%)
- Acurácia do Health Score: correlação entre score CRÍTICO e churn real em 30 dias (meta: precision >= 70%, recall >= 60%)
- Cobertura de Alertas: % de churns reais que foram antecipados pelo squad com alerta >= 14 dias antes (meta: >= 75%)
- CSAT de Contas Monitoradas: variação do NPS/CSAT médio das contas que receberam intervenção proativa vs grupo controle (meta: +12 pontos NPS em 6 meses)
- Taxa de Ativação de Tasks: % de tasks criadas no ClickUp que o CSM inicia dentro do prazo (meta: >= 85% — indica qualidade e urgência percebida das tasks)
- Critic Approval Rate: % de briefs aprovados pelo Argus na primeira iteração sem necessidade de reprocessamento (meta: >= 80% — indica qualidade do Mira)

## Integrações

- ClickUp (Brain2 / MCP server) — hub de tasks de retenção, prova de trabalho, prioridade e prazos automáticos, espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce — fonte de dados de Account, Contract, MRR, CSM, histórico de interações, QBRs e pipeline de renovação
- Plataforma de produto: Mixpanel, Amplitude ou Segment — eventos de uso, DAU/MAU, feature adoption, sessões por conta
- Helpdesk: Zendesk ou Intercom — volume de tickets, CSAT, categorias, transcrições e histórico de suporte por conta
- NPS / CSAT: Delighted, Typeform ou Wootric — scores e verbatims de pesquisas de satisfação
- CS Platforms: ChurnZero, Custify, Gainsight, ou Velaris — plataformas especializadas de health scoring (integração bidirecional: leitura de dados + escrita de scores calculados)
- Slack — notificações em tempo real para CSM (alerta de churn), manager (escalonamento) e Head de CS (relatório semanal e padrões sistêmicos)
- Supabase / Postgres — estado dos agentes, armazenamento de health scores históricos, sinais normalizados, log de tasks e outcomes
- Langfuse — observabilidade OTEL, tracing do pipeline de cálculo de score, evals de qualidade dos briefs, quality gates dev/staging/prod
- Claude Agent SDK / LangGraph — orquestração do pipeline multi-agente com gerenciamento de estado e retry logic
- Email / SMTP — envio de relatório semanal de saúde da base para Head de CS e stakeholders
- News/alerts API (NewsAPI, Google Alerts webhook) — detecção de mudanças organizacionais em contas monitoradas (M&A, redução de headcount, mudança de liderança)

## Entregável (prova de trabalho)

Por ciclo diario: (1) Dashboard Langfuse atualizado com health scores de toda a base, distribuicao por faixa de risco, trending de deterioracao e mapa de calor por CSM/segmento; (2) Tasks no ClickUp para cada conta em risco CRITICO e ALTO com brief completo, sinais que compoem o score com valores concretos, next-best-action prioritaria com taxa de sucesso historica, acoes alternativas rankeadas e script de abertura sugerido; (3) Registro no Supabase de cada score calculado com breakdown por dimensao, sinais de entrada utilizados, timestamp e versao do modelo — prova de trabalho auditavel e rastreavel. Por semana: relatorio de saude da base (distribuicao de scores, saves confirmados, MRR protegido, padroes sistemicos detectados) entregue no Slack do Head de CS. Por save confirmado: medicao de impacto (variacao do health score pre/pos-intervencao, MRR protegido) registrada no CRM.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 ag, qualidade de dados) — base para o pipeline de ingestão e validação de sinais do Vega: lógica de detecção de anomalia em dados, validação de schema, tratamento de dados faltantes e alertas de qualidade que o Argus usa para bloquear scores baseados em dados corrompidos
- Skeptic Protocol (5 ag, red-team/QA) — base para o Critic Argus: estrutura adversarial de validação com rubrica multi-dimensão, lógica de rejeição com feedback específico e iteração controlada (max 2 reprocessamentos antes de escalar para humano)
- Five Vitals (diagnóstico de sistemas) — base para o agente Echo de monitoramento contínuo: lógica de medição de saúde de sistema com 5 dimensões, detecção de degradação acelerada, correlação de eventos externos com variações de métrica e geração de relatório executivo com tendências

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O3 · TopSquad de Customer Success: Onboarding, Retenção & Expansão** — O ciclo de vida pós-venda inteiro: ativar, reter, expandir.

- **Missão:** O squad do cliente após a venda: conduz o onboarding/implementação, prevê e previne churn ao longo da vida, e automatiza renovação, expansão e QBRs. Ativar → reter → expandir em um motor único de Customer Success.
- **Por que consolidar:** É a mesma jornada do cliente em três fases — ativar, manter, crescer — e os sinais fluem entre elas: um onboarding fraco prevê churn, que (evitado) abre expansão. Separados, o sinal de saúde vivia em silos; unidos, o health score atravessa todo o ciclo de vida.
- **Squads irmãos:** Onboarding & Implementação (PSA Agêntica), Predição & Prevenção de Churn, Renovação, Expansão & QBR Automatizado

## Estrutura

```
ops-cs-churn-prediction/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
