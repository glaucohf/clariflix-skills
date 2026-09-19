# Squad de Voz do Cliente – Análise de Sentimento e Tendências

> Transforma o barulho espalhado de tickets, NPS e reviews em insights priorizados que produto e ops podem agir amanhã – não no próximo trimestre.

**Área:** Operações & CS · **TopSquad:** O2 Qualidade, Voz do Cliente & Knowledge Base · **Prioridade:** avançado · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Feedback do cliente fica fragmentado em silos desconectados: tickets no Zendesk sem análise, NPS sem verbatim categorizado, reviews públicos sem monitoramento, conversas de WhatsApp perdidas e chamadas sem transcrição. Ninguém consolida, ninguém cruza canais, ninguém prioriza pelo impacto real no negócio. Produto decide com base em feeling de CSM ou no cliente que grita mais alto. O Voice-of-Customer Analyst Squad agrega automaticamente todos os canais (helpdesk, NPS, reviews, conversas, pesquisas), aplica análise de sentimento PT-BR contextualizada, identifica tendências emergentes antes que virem crise, prioriza por volume x impacto x segmento, e entrega para produto e ops um relatório de tendências semanal com fontes citadas – pronto para virar prioridade de roadmap ou ação operacional imediata.

## Impacto esperado

Reducao de 60-80% no tempo de analise manual de feedback (de 12-20h/semana de analista para < 3h de revisao). Lead time de deteccao de tendencia emergente: de 30-60 dias (reactivo, apos cliente reclamar suficientemente) para 5-10 dias (proativo, detectado em volume e velocidade crescentes). NPS: aumento de 8-15 pontos em 6 meses em organizacoes que agem com base em insights semanais vs trimestrais. Reducao de 35-50% em tickets repetitivos sobre o mesmo tema quando insights geram correcao de produto ou processo. Para equipe de produto com 3 PMs: economia de 40h/mes em coleta e sintese de feedback = foco em construcao. Para CS com 5 CSMs: identificacao precoce de tendencias de insatisfacao reduz churn em contas de medio risco em 20-30%. ROI estimado: payback em < 45 dias considerando reducao de churn e economia de tempo de analise.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Voice-of-Customer Orchestrator | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `haruki` · Haruki | Haruki — Coletor e Normalizador de Feedback Multicanal | L0 · worker determinístico | `coletar-e-normalizar-feedback.md` |
| `yara` · Yara | Yara — Analista de Sentimento e Classificadora de Temas | L1 · worker autônomo | `classificar-temas-e-sentimento.md` |
| `orion-2` · Orion 2 | Orion — Detector de Tendências e Priorizador | L2 · orquestra / decide | `detectar-tendencias-acionaveis.md` |
| `lyra` · Lyra | Lyra — Sintetizadora de Relatório e Narrativa | L2 · orquestra / decide | `sintetizar-relatorio-executivo.md` |
| `rapid` · Rapid | Rapid — Agente de Alerta e Monitoramento em Tempo Real | L2 · orquestra / decide | `monitorar-pico-de-volume.md` |
| `atlas` · Atlas | Atlas – Agente de Ativação e Prova de Trabalho no ClickUp | L3 · aprovação humana | `criar-tasks-rastreaveis.md` |
| `cassandra` · Cassandra | Cassandra — Critic de Rastreabilidade e Qualidade de Insights | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-voz-do-cliente-sentimento:orion` (ou instale via `npx squads add ./ops-cs-voz-do-cliente-sentimento`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-voz-do-cliente-sentimento-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia lembrete; sem resposta em 8h, relatório é enviado com disclaimer 'pendente de revisão humana'
- Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para atendimento) antes de aparecer no backlog ativo; aprovação via bot no Slack com preview da task
- Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefing imediato e Atlas cria task de emergência; se falso positivo, threshold é ajustado automaticamente
- Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-processar histórico; impacto estimado em registros afetados e apresentado antes da aprovação
- Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; indica possível drift na linguagem dos clientes ou bug na ingestão
- Publicacao de insight que menciona concorrente especifico por nome — Lyra sinaliza e o Head de CS aprova antes de distribuir para evitar vazamento de informacao competitive sensivel
- Re-calibração de thresholds de alerta após detecção de falsos positivos recorrentes — o Rapid documenta a sugestão de ajuste e aguarda aprovação do PM ou Head de CS para alterar o threshold de produção
- Feedback de canal com volume insuficiente para análise estatística identificado pós-Discovery — Haruki notifica e aguarda decisão humana sobre incluir ou excluir canal do pipeline de produção

## KPIs

- Número de Insights Acionáveis por Semana: total de tendências no relatório semanal com score acima do threshold que geraram ao menos uma task de ação aprovada (meta: >= 3 por semana, crescente com o tempo)
- Lead Time de Detecção de Tendência Emergente: dias entre primeira menção de um tema novo e primeira aparição no relatório semanal como tendência confirmada (meta: <= 7 dias; baseline atual estimado em 30-60 dias com processo manual)
- Correlação de Insights com Variação de NPS: variação do NPS médio 30 dias após ação tomada sobre tendência identificada vs períodos sem ação baseada em VOC (meta: tendências atacadas correlacionam com +5 pontos de NPS em 60 dias)
- Taxa de Conversão Insight → Ação → Resultado: % de insights do relatório que viram tasks (meta: >= 60%), % de tasks concluídas em 30 dias (meta: >= 70%), % com resultado reportado no ClickUp (meta: >= 50%)
- Accuracy de Classificação de Temas: % de registros classificados corretamente pelo Yara validados na amostra mensal pelo Critic Cassandra (meta: >= 85% em produção)
- Taxa de Falsos Positivos em Alertas: % de alertas do Rapid classificados como 'Falso Positivo' pelo time (meta: <= 20%; thresholds auto-ajustados para convergir para este valor)
- Redução de Tickets Repetitivos: variação mensal no volume de tickets sobre temas que receberam ação a partir de insight VOC (meta: -35% a -50% em 90 dias pós-ação)
- Cobertura de Canais Ativos: % de canais de feedback configurados com ingestão bem-sucedida nas últimas 24h (meta: >= 95% de uptime; alerta quando canal fica offline > 4h)
- Tempo de Revisão Humana por Semana: horas que PM ou Head de CS gastam revisando e aprovando o relatório VOC (meta: <= 30 minutos; indica qualidade do relatório gerado)
- Relatórios Aprovados Sem Revisão Maior: % de relatórios semanais que passam pelo HITL com aprovação direta sem solicitação de ajuste substancial (meta: >= 75% após primeiro mês de operação)

## Integrações

- ClickUp (Brain2 / MCP server) — hub de tasks de ação, prova de trabalho com tags VOC, rastreabilidade de insights, espelhando arquitetura AIOX; usado pelo Atlas para criação de tasks e pelo Orion para leitura de eventos de produto
- Zendesk ou Intercom — fonte primária de tickets de suporte com CSAT e comentários; volume diário normalizado pelo Haruki; campo de tema do Yara pode ser gravado de volta como tag no ticket via API
- NPS / CSAT: Delighted, Typeform, Wootric ou SurveyMonkey — scores e verbatims de pesquisas; NPS é a fonte de sentimento mais estruturada e prioritária
- WhatsApp Business API — mensagens de atendimento anônimizadas; canal #1 de feedback informal no Brasil; exige tratamento nativo de texto curto e linguagem informal
- Reviews públicos: G2, Capterra, Trustpilot, App Store, Google Play — coletados semanalmente via API ou scraping; fonte de feedback de prospects além de clientes
- Notion — destino do relatorio semanal completo em markdown com historico pesquisavel por tema e data
- Slack — canal #voc-alertas para alertas do Rapid, canal #voc-insights para relatório semanal resumido, DMs para responsáveis de tasks aprovadas pelo Atlas
- Supabase / Postgres — banco de estado do squad: voc_raw_feedback, voc_analyzed_feedback, voc_trends_daily, voc_weekly_reports, voc_alerts, voc_actions; histórico completo auditável
- Langfuse — observabilidade OTEL do pipeline, tracing de classificação do Yara, evals de qualidade dos insights do Lyra, quality gates dev/staging/prod (70/85/95% accuracy)
- Claude Agent SDK / LangGraph — orquestração do pipeline multi-agente com gerenciamento de estado, retry logic e paralelização de ingestão de canais
- CRM: HubSpot ou Salesforce — dados de segmento, MRR e CSM responsável por account_id para ponderação de tendências por segmento e cálculo de impacto de receita
- Jira ou Linear (opcional) — leitura do changelog de produto para correlação de tendências com releases e incidentes no Orion
- Airtable ou Google Sheets (fallback) — canais de feedback que não tem API estruturada podem ser ingeridos via planilha compartilhada como fonte temporária

## Entregável (prova de trabalho)

CICLO DIÁRIO: (1) Log de ingestão no Supabase por canal — volume de registros, % de qualidade válida, anomalias detectadas — prova de trabalho verificável pelo time de dados; (2) Alertas em tempo real no Slack (#voc-alertas) quando temas cruzam threshold de emergência — com volume concreto, verbatims e sugestão de ação imediata; (3) Dashboard Langfuse atualizado com métricas de pipeline: registros processados, distribuição de sentimento do dia, top-5 temas por volume. CICLO SEMANAL: Relatório de Tendências Priorizadas — o artefato central do squad — entregue toda segunda-feira às 09h com: sumário executivo de 200 palavras, top-5 tendências com score de priorização, volume (menções com número absoluto e % do total), variação vs semana anterior (delta%), sentimento médio, breakdown por segmento de cliente, 3-5 verbatims representativos com canal e data citados (rastreabilidade completa), correlação com evento de produto se existir, e sugestão de ação específica por tendência. Versão completa no Notion, versão resumida no Slack. Tasks de ação aprovadas criadas no ClickUp com prova de trabalho rastreável (tag VOC). CICLO MENSAL: Relatório de impacto — insights gerados vs ações tomadas vs variação de NPS e volume de tickets nos temas atacados — ROI mensurável do squad.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 ag, qualidade de dados) — base para o pipeline de ingestão do Haruki: lógica de validação de schema, detecção de dados faltantes, deduplicação por hash, alertas de anomalia de volume e reports de qualidade por canal; acelera a construção das regras de validação que o Critic Cassandra usa para bloquear relatórios baseados em dados corrompidos
- Skeptic Protocol (5 ag, red-team/QA) — base para o Critic Cassandra: estrutura adversarial de validação multi-dimensão (rastreabilidade, representatividade, viés de seleção, hallucination), lógica de rejeição com feedback específico e ciclo de correção controlado (max 2 iterações antes de escalonar para humano)
- Athenaeum (11 ag, inteligência estratégica) — base para o agente Lyra na síntese de relatório executivo: estrutura de destilação de múltiplas fontes em narrativa coerente, priorização por impacto, formatação de insights com evidências citadas e recomendações acionáveis — acelera a construção do template de relatório e a lógica de seleção de verbatims representativos

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O2 · TopSquad de Qualidade, Voz do Cliente & Knowledge Base** — Audita 100% das conversas, ouve o que o cliente sente e devolve isso à base.

- **Missão:** A camada de aprendizado da operação: audita 100% das conversas (não amostra), extrai sentimento e tendências da voz do cliente, e converte tudo em atualizações da base de conhecimento. Fecha o loop qualidade → insight → conhecimento.
- **Por que consolidar:** Os três processam o mesmo material — as conversas de atendimento — para fins encadeados: auditar, entender e documentar. O QA descobre lacunas, a voz do cliente explica o porquê e o KB Curator corrige a fonte. Separados, ninguém fechava o loop; juntos, é um ciclo de melhoria contínua.
- **Squads irmãos:** QA de Conversas 100% (Quality Verifier), Voz do Cliente — Sentimento & Tendências, KB Curator

## Estrutura

```
ops-cs-voz-do-cliente-sentimento/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
