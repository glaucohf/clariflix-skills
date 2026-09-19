# Squad de Social Selling e Inbound LinkedIn

> Captura sinais de intenção no LinkedIn antes que o concorrente veja a oportunidade.

**Área:** Vendas · **TopSquad:** V1 Prospecção & Outbound Multicanal · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Social selling manual no LinkedIn não escala e perde janelas críticas de timing — mudança de cargo, post viral de decisor, funding anunciado, engajamento em conteúdo próprio. Sem monitoramento automatizado de sinais e outreach contextual e personalizado, equipes de vendas B2B reagem tarde ou não reagem, perdendo a janela de intenção no principal canal de negociação B2B do Brasil.

## Impacto esperado

Reduz de 48-72h para menos de 15 minutos o tempo de resposta a sinais de intenção no LinkedIn. Aumenta taxa de aceite de conexão em 3-5x com mensagens contextuais (benchmark: 12-18% outreach genérico vs 40-55% signal-driven). Pipeline gerado por canal LinkedIn cresce 2-4x em 90 dias. ROI estimado: para uma equipe de 3 SDRs gerando R$150k/mês em pipeline LinkedIn, o squad gera R$300-600k/mês adicionais com custo operacional 10x menor que contratar mais SDRs.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Maestro Comercial (Órion) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `scout` · Scout | Sentinela de Sinais (Scout) | L1 · worker autônomo | `monitorar-sinais-de-intencao.md` |
| `sherlock` · Sherlock | Detetive de Conta (Sherlock) | L1 · worker autônomo | `enriquecer-dados-firmograficos.md` |
| `cypher` · Cypher | Redator de Sinal (Cypher) | L3 · aprovação humana | `conectar-dor-implicita.md` |
| `argus` · Argus | Fiscal de Mensagem (Árgus) | L2 · orquestra / decide | `verificar-mensagem-antes-do-envio.md` |
| `pulso` · Pulso | Executor de Cadência (Pulso) | L3 · aprovação humana | `executar-cadencia-pulso.md` |
| `radar` · Radar | Qualificador de Resposta (Radar) | L2 · orquestra / decide | `classificar-intencao.md` |
| `nexus` · Nexus | Guardião do Pipeline (Nexus) | L1 · worker autônomo | `sincronizar-dados-crm.md` |
| `argus-2` · Argus 2 | Fiscal de Mensagem (Árgus) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-social-selling-linkedin:orion` (ou instale via `npx squads add ./vendas-social-selling-linkedin`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-social-selling-linkedin-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório.
- Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada.
- Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente.
- Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana.
- Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração.
- Primeiro envio de cadência para um novo segmento/persona não testado anteriormente: SDR revisa amostra de 5 mensagens antes de liberar automação plena.
- Lead responde mencionando nome de concorrente ou fazendo pergunta técnica complexa: desvia para SDR humano com contexto completo da conversa.

## KPIs

- Time-to-Signal-Response: tempo médio entre detecção do sinal e envio da primeira mensagem (meta: <15 min)
- Taxa de Aceite de Conexão: % de connection requests aceitas (baseline mercado: 15-20%, meta squad: 40-55%)
- Taxa de Resposta a DMs: % de DMs que recebem resposta (baseline: 5-8%, meta squad: 15-25%)
- Lead-to-HOT Rate: % de leads abordados que classificam como HOT (meta: >8%)
- Meetings Booked via LinkedIn: reunioes agendadas origindas do canal LinkedIn por semana
- Pipeline Gerado LinkedIn (R$): valor total de oportunidades abertas com origem em sinal LinkedIn nos ultimos 30 dias
- Custo por Lead Qualificado: custo de API + infra / total de HOTs gerados (meta: <R$50/HOT)
- Taxa de Aprovação do Critic: % de mensagens aprovadas pelo Argus na primeira iteração (meta: >80%)
- CRM Data Completeness: % de contatos com LinkedIn URL + cargo + empresa atualizados (meta: >95%)
- Sinal-to-Meeting Conversion: % de sinais detectados que resultam em reunião agendada (meta: >3%)

## Integrações

- LinkedIn Sales Navigator — fonte primária de sinais e canal de outreach (via automação com limites de segurança para não violar ToS)
- Apollo.io — enriquecimento de contatos (email, cargo, empresa), alertas de mudança de cargo, base de 275M+ contatos
- Clay — enriquecimento avançado e workflows de pesquisa de conta (waterfall de provedores de dados)
- HubSpot CRM (MCP disponível) — CRM primário: criação de deals, atualização de contatos, registro de atividades, pipeline stages
- Pipedrive — alternativa de CRM para clientes que usam Pipedrive (mesmo contrato de integração)
- ClickUp — gestão de tarefas do squad, prova de trabalho verificável por lead, dashboard de KPIs, filas de aprovação HITL
- Gmail/Outlook — canal secundário de outreach quando email disponível (via Apollo enriquecimento)
- Slack/WhatsApp Business — notificações HITL em tempo real para SDRs e closers (alerts HOT, aprovações tier-1)
- Langfuse — observabilidade OTEL, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de custo por lead
- n8n / Make — orquestracao de webhooks e automacoes de suporte (alternativa leve para integrações pontuais)
- Calendly / Google Calendar — agendamento automático quando lead classifica como HOT e aceita reunião

## Entregável (prova de trabalho)

Signal-to-Meeting Dossie: para cada lead abordado, um artefato verificável no ClickUp contendo — (1) Signal Card (tipo de sinal, timestamp, score de urgência, fonte), (2) Lead Dossie completo (Sherlock), (3) Message Package aprovado pelo Argus com score de personalização, (4) Execution Log da cadência com timestamps de cada toque, (5) Classification Card da resposta (se houver), (6) CRM Update Confirmation com link para o deal/contato. Dashboard consolidado no ClickUp com métricas do squad em tempo real e relatório executivo semanal automático.

## Bases gratuitas reutilizáveis (citadas na especificação)

- LinkedIn (6 ag, social) — squad gratuito do squads.sh/myclaude com agentes especializados em monitoramento e outreach LinkedIn; serve de base para os workers Scout e Cypher, acelerando a implementação dos módulos de detecção de sinal e redação de mensagem.
- Mãe Intuitiva CRM (CRM/leads) — squad gratuito focado em gestão de leads e CRM; acelera a implementação do Nexus (Guardião do Pipeline) com lógica de dedup, enriquecimento e sincronização de CRM já estruturada.
- Skeptic Protocol (5 ag, red-team/QA) — squad gratuito de verificacao adversarial; a logica do Critic multi-perspectiva pode ser adaptada diretamente para o Argus (Fiscal de Mensagem), especialmente os modulos de factualidade e compliance.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V1 · TopSquad de Prospecção & Outbound Multicanal** — Do sinal de intenção ao primeiro toque humano-grade — e-mail, social ou voz — sempre aprovado por um critic.

- **Missão:** Motor único de geração de demanda fria: detecta sinais de intenção, escolhe o canal certo (e-mail, LinkedIn/social ou ligação por voz), hiperpersonaliza a abordagem e dispara cadências cross-channel — tudo validado por um critic antes de tocar o lead.
- **Por que consolidar:** Os três squads absorvidos compartilhavam o mesmo cérebro — detecção de sinal + enriquecimento + personalização + critic anti-spam — e divergiam apenas no canal de saída. Unificados, viram um orquestrador que decide o canal por contexto e habilita cadência cross-channel (e-mail → social → voz no mesmo lead).
- **Squads irmãos:** AI SDR Outbound Signal-Based, Social Selling & Inbound LinkedIn, Voz para Cold Calling & Discovery

## Estrutura

```
vendas-social-selling-linkedin/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
