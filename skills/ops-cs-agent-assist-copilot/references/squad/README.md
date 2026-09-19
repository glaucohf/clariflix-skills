# Squad de Copiloto do Agente Humano (Agent Assist Copilot)

> O atendente humano fala, o Copiloto já sabe a resposta — sugestão certa, no canal certo, em menos de 3 segundos.

**Área:** Operações & CS · **TopSquad:** O1 Atendimento & Suporte Conversacional · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Atendentes humanos desperdiçam 40-60% do AHT procurando informação no KB, redigindo respostas do zero e tentando lembrar o histórico do cliente. O resultado: AHT elevado (média de 8-14 min em suporte B2B), variabilidade absurda de qualidade entre atendentes, erros de compliance e esgotamento de equipe. O Agent Assist Copilot atua como um 'segundo cérebro' silencioso ao lado do atendente: le a conversa em tempo real, recupera contexto da conta, sugere a próxima resposta ideal (com macro ou draft livre), resume o histórico do ticket em segundos e alerta sobre riscos antes que o humano cometa o erro.

## Impacto esperado

Reducao de AHT de 35-50% (de 10 min para 5-6 min em suporte Tier-2): equivale a 30-45 tickets a mais por atendente por dia. Taxa de adocao de sugestoes meta >= 55% (benchmark: Intercom Fin AI 60-65%). Consistencia de respostas: reducao de 70% na variabilidade de tom e compliance entre atendentes. Reducao de erros de politica: < 2% de respostas violando regras de negocio (vs. 12-18% sem copiloto). Onboarding de novos atendentes: de 3 semanas para 5-7 dias com copiloto ativo. Para uma equipe de 10 atendentes com 800 tickets/dia: ROI estimado R$25-40k/mes em produtividade recuperada + reducao de 20-25% em re-abertura de tickets por resposta inadequada.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `compass` · Compass | Compass — Orchestrator de Assist em Tempo Real | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Radar — Listener & Classifier de Intenção | L0 · worker determinístico | `classificar-intencao-do-cliente.md` |
| `vault` · Vault | Vault — Context Fetcher de Conta | L0 · worker determinístico | `recuperar-dados-de-conta.md` |
| `scribe` · Scribe | Scribe — Worker de Sugestão de Resposta | L1 · worker autônomo | `gerar-sugestao-de-resposta.md` |
| `memo` · Memo | Memo — Agente de Resumo de Ticket | L1 · worker autônomo | `gerar-resumo-executivo.md` |
| `lumen` · Lumen | Lumen — Agente de Sugestão de Próximo Passo | L1 · worker autônomo | `sugerir-proximo-passo.md` |
| `echo` · Echo | Echo — Agente de Feedback & Aprendizado Contínuo | L2 · orquestra / decide | `analisar-sugestoes-atendente.md` |
| `shield` · Shield | Shield — Agente de Alerta de Risco & Compliance | L3 · aprovação humana | `monitorar-mensagens-atendente.md` |
| `prism` · Prism | Prism — Critic de Qualidade de Sugestão | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-agent-assist-copilot:compass` (ou instale via `npx squads add ./ops-cs-agent-assist-copilot`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-agent-assist-copilot-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar conscientemente ou corrigir
- Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — responda manualmente'
- Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico
- Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromisso
- Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente
- Vault retorna flag 'cliente_em_risco_de_churn' (health score < 50): todas as sugestões do Scribe são marcadas com indicador visual e Lumen adiciona sugestão de escalonamento para CSM
- Echo detecta que uma macro tem rejection_rate > 60% por 7 dias consecutivos: dispara alerta para gestor de CS no Slack pedindo revisão manual da macro antes de continuar exibindo
- Shield detecta promessa de desconto ou benefício financeiro no rascunho do atendente: alerta de policy_violation com valor exato do limite autorizado e botão de consulta ao supervisor

## KPIs

- AHT (Average Handle Time): tempo médio de atendimento com copiloto vs. sem (meta: redução >= 35% em 90 dias)
- Suggestion Adoption Rate: % de sugestoes exibidas que o atendente aceita (integralmente ou editada) (meta: >= 55%)
- Suggestion Rejection Rate por Intencao: identifica intencoes onde o copiloto e fraco e precisa de melhoria de KB
- Edit Distance Ratio: quão diferente é a resposta editada em relação à sugestão original (meta: < 20% de edição = sugestão precisa)
- Critic Rejection Rate: % de sugestoes do Scribe rejeitadas pelo Prism antes de exibir (meta: < 10% — indica qualidade do gerador)
- Policy Violation Rate: % de rascunhos do atendente que o Shield detecta violação de política (meta: < 2%)
- Re-open Rate: % de tickets reabertos nos 7 dias seguintes à resolução com copiloto (benchmark: comparar vs. sem copiloto, meta redução 20%)
- Onboarding Time to Proficiency: dias até novo atendente atingir AHT médio da equipe (meta: redução de 3 semanas para 7 dias)
- Custo por Sugestao: custo de tokens + infra / numero de sugestoes exibidas (meta: < R$0.15 por sugestao)
- CSAT pos-atendimento com copiloto vs. sem: comparativo de satisfacao do cliente (meta: delta positivo >= 0.3 pontos em escala 1-5)

## Integrações

- Zendesk (webhook de nova mensagem + API de ticket + campo de resolução) — helpdesk primário
- Intercom (webhook conversation.message.created + Fin AI overlay API) — helpdesk alternativo
- ClickUp (Brain2 / MCP server) — task por atendimento como prova de trabalho espelhando AIOX
- CRM: HubSpot ou Salesforce — dados de conta, MRR, renovação, notas do CSM via MCP
- CS Platform: ChurnZero / Gainsight / Custify — health score, uso do produto, alertas de churn
- ERP / OMS — consulta de pedidos, status, histórico de compras via MCP customizado
- Supabase / Postgres — cache de contexto de conta, log de sugestões e feedbacks, macros vetorizadas
- Langfuse — observabilidade OTEL, tracing de cada step do pipeline, adoption rate, AHT delta, quality gates
- Slack — alertas de SLA em risco, relatorio semanal do Echo, alertas de macro com alta rejection rate
- Claude Agent SDK / LangGraph — orquestração do pipeline multi-agente com latência controlada
- Widget de overlay no Zendesk/Intercom (extensão de browser ou app interno) — UI de exibição das sugestões e coleta de feedback do atendente
- Webhook de composição do helpdesk — captura rascunho do atendente para o Shield em tempo real

## Entregável (prova de trabalho)

Por atendimento concluido: Task no ClickUp com (1) ID do ticket e atendente responsavel, (2) intencoes detectadas na conversa com confianca scores, (3) numero de sugestoes exibidas vs. aceitas vs. rejeitadas vs. editadas, (4) resumo de resolucao gerado pelo Memo, (5) alertas do Shield disparados (se houver), (6) AHT do atendimento, (7) flags de next-step do Lumen acionadas, (8) timestamp de cada step do pipeline Compass. Dashboard Langfuse com: adoption rate em tempo real por atendente e por intencao, AHT trending semanal, critic rejection breakdown por dimensao, top macros aceitas e rejeitadas, mapa de heat das violacoes do Shield por tipo. Relatorio semanal do Echo no Slack com analise de qualidade das sugestoes e recomendacoes de melhoria.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 ag, red-team/QA) — base para o Critic Prism: lógica de adversarial review multi-dimensão, rubrica de validação com feedback estruturado por dimensão e mecanismo de retry com instrução específica de correção
- Apex Context Supreme (5 ag, context engineering) — base para o Vault e o Compass: arquitetura de recuperação e compactação de contexto de conta em alta velocidade, priorização de dados por relevância para a intenção ativa
- Data Quality Guardian (5 ag, qualidade de dados) — base para o Echo: pipeline de monitoramento de qualidade de sugestões ao longo do tempo, detecção de degradação de performance por intenção e geração de alertas com análise de causa raiz

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O1 · TopSquad de Atendimento & Suporte Conversacional** — Resolve, tria, escala e assiste — toda a linha de frente em um cérebro só.

- **Missão:** A linha de frente inteira: resolve o Tier-1 em texto e voz (PT-BR), tria e prioriza tickets, decide quando escalar para humano (handoff) e assiste o agente humano quando ele assume. Um único cérebro de atendimento, multicanal.
- **Por que consolidar:** Os cinco vivem na mesma conversa do cliente — só atuam em momentos diferentes (resolver, triar, escalar, assistir). Mantê-los separados quebrava o contexto a cada passagem de bastão. Unidos, a conversa flui do bot ao humano e de volta sem reiniciar, com triagem e copiloto compartilhando o mesmo estado.
- **Squads irmãos:** Suporte Conversacional Multicanal (Tier-1), Voz-IA para Atendimento Telefônico (PT-BR), Triagem, Roteamento e Priorização de Tickets, Handoff Orchestrator HITL, Copiloto do Agente Humano

## Estrutura

```
ops-cs-agent-assist-copilot/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
