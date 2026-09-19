# Squad de Voz para Cold Calling e Discovery

> Voz de IA sub-600ms que liga, qualifica e agenda — sem SDR humano no primeiro contato.

**Área:** Vendas · **TopSquad:** V1 Prospecção & Outbound Multicanal · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Cold calling humano e caro (R$4-12k/mês por SDR), inconsistente em qualidade e incapaz de cobrir volume de discagem em escala. Sem agente de voz de baixa latência (<600ms), empresas perdem alcance, padronização e velocidade de resposta a leads inbound/outbound. O resultado é funil furado na entrada: leads frios nunca discados, descobertas de dor sem script e agenda de closer subotimizada.

## Impacto esperado

Redução de 60-80% no custo por lead qualificado (SDR humano ~R$180-300/lead vs agente ~R$8-30/lead). Aumento de 3-5x no volume de discagens diárias sem contratação. Taxa de conexão sustentada 24/7 (elimina janela horária humana). Conversion rate de lead para discovery call qualificada estimada em 12-18% (benchmark: SDR humano top 8-14%). ROI esperado: payback em 45-90 dias para operações com >200 discagens/semana.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orquestrador-comercial-de-voz` · Orquestrador Comercial de Voz | Maestro (Orquestrador Comercial de Voz) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `dossie` · Dossie | Dossié (Worker de Enriquecimento e Pesquisa de Conta) | L1 · worker autônomo | `enriquecer-dossie-contextual.md` |
| `vox-worker-de-voz` · Vox (Worker de Voz | Vox (Worker de Voz — Cold Call e Abertura) | L2 · orquestra / decide | `realizar-ligacao-cold-call.md` |
| `filtro` · Filtro | Filtro (Critic/Verifier de Qualificação e Compliance) | L1 · worker autônomo | `analisar-transcricao-call.md` |
| `agenda` · Agenda | Agenda (Worker de Agendamento e Booking) | L2 · orquestra / decide | `agendar-reuniao.md` |
| `eco` · Eco | Eco (Worker de Follow-up e Nurture de Frios) | L2 · orquestra / decide | `reativar-interesse-frios.md` |
| `radar` · Radar | Radar (Worker de Lead Scoring e Priorização de Fila) | L1 · worker autônomo | `ranquear-leads.md` |
| `insight` · Insight | Insight (Worker de Conversation Intelligence e Coaching) | L1 · worker autônomo | `analisar-padroes-de-conversas.md` |
| `filtro-2` · Filtro 2 | Filtro (Critic/Verifier de Qualificação e Compliance) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-voz-cold-calling-discovery:orquestrador-comercial-de-voz` (ou instale via `npx squads add ./vendas-voz-cold-calling-discovery`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-voz-cold-calling-discovery-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3).
- Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3).
- Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3).
- Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3).
- Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation).
- Confirmação de reagendamento quando prospect cancela reunião pela segunda vez consecutiva (decisão humana sobre continuar ou desqualificar — L3).
- Calibragem quinzenal de voz e persona do Vox Agent com gestor de vendas (revisão humana de amostras de áudio — L1).

## KPIs

- Taxa de Conexão: % de ligações atendidas por humano / total de discagens (benchmark: 8-15%)
- Taxa de Qualificacao: % de leads que passam pelo Filtro Agent como VALIDO / total de calls conectadas (meta: >35%)
- Taxa de Agendamento: % de leads qualificados que chegam à reunião agendada / total qualificados (meta: >55%)
- Taxa de Show: % de reuniões que efetivamente ocorrem / total agendadas (meta: >70%)
- Custo por Lead Qualificado: custo total do squad (API + plataformas) / leads qualificados entregues (meta: R$15-40/lead)
- Latência de Resposta do Vox Agent: tempo entre fala do prospect e início de resposta do agente (meta: <600ms P95)
- Score de Qualidade de Call: média do Filtro Agent nas calls da semana (meta: >75/100)
- Volume de Discagens por Dia: total de tentativas realizadas pelo Vox Agent (meta: 3-5x baseline humano)
- Taxa de Reativacao de Frios: % de leads nurturados pelo Eco Agent que retornam a fila ativa em 90 dias (meta: >12%)
- Task Success Rate no Quality Gate: Langfuse tracking — dev 70% / staging 85% / prod 95%

## Integrações

- Vapi ou Rétell AI (plataforma de agente de voz sub-600ms)
- Deepgram (STT — Speech-to-Text de baixa latência)
- ElevenLabs (TTS — Text-to-Speech com voz personalizada)
- HubSpot CRM (MCP disponível — leitura e escrita de leads, deals, activities)
- Google Calendar ou Outlook (agendamento e gestão de disponibilidade do closer)
- WhatsApp Business API via Gupshup ou AiSensy (confirmações, lembretes, nurture)
- Apollo.io (enriquecimento de leads — 275M+ contatos)
- Clay (enriquecimento dinâmico e waterfall de dados)
- ClickUp (gestão de tarefas e artefatos verificáveis por story)
- Langfuse (observabilidade OTEL, evals e quality gates por fase)
- LangGraph (orquestração do grafo de estados conversacional do Vox Agent)
- Twilio ou Vonage (gateway de telefonia para discagem programática)
- Google Sheets ou Airtable (lista de prospectos e relatórios para clientes sem CRM robusto)
- Slack ou Teams (notificações de leads qualificados e alertas de HITL para gestor comercial)

## Entregável (prova de trabalho)

Artefato principal por ciclo de operação: Relatório Diário de Discagem (JSON + dashboard) contendo — leads discados, taxa de conexão do dia, leads qualificados com campos BANT preenchidos, reuniões agendadas, calls com flag de HITL pendente, e score de qualidade médio. Artefatos secundários: Dossiês de Lead (pré-call), Transcrições e Gravações de Call (pós-call), Relatório Semanal de Conversation Intelligence, e Fila de Discagem Priorizada pelo Radar Agent. Todos os artefatos rastreados no ClickUp com link direto ao registro do CRM.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM — base para lógica de gestão de leads, priorização de fila e nurture de frios; adaptar o grafo de estados para o contexto de voz outbound.
- Skeptic Protocol — usar a estrutura de red-team/QA dos 5 agentes como base para o Filtro Agent (Critic/Verifier), especialmente os padroes de verificacao adversarial e flags de compliance.
- Win Proposal Deal — reutilizar os 4 agentes de proposta comercial como camada downstream: quando Vox Agent qualifica lead e agenda reunião, acionar squad de proposta para pre-preparar material do closer com contexto do dossiê.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V1 · TopSquad de Prospecção & Outbound Multicanal** — Do sinal de intenção ao primeiro toque humano-grade — e-mail, social ou voz — sempre aprovado por um critic.

- **Missão:** Motor único de geração de demanda fria: detecta sinais de intenção, escolhe o canal certo (e-mail, LinkedIn/social ou ligação por voz), hiperpersonaliza a abordagem e dispara cadências cross-channel — tudo validado por um critic antes de tocar o lead.
- **Por que consolidar:** Os três squads absorvidos compartilhavam o mesmo cérebro — detecção de sinal + enriquecimento + personalização + critic anti-spam — e divergiam apenas no canal de saída. Unificados, viram um orquestrador que decide o canal por contexto e habilita cadência cross-channel (e-mail → social → voz no mesmo lead).
- **Squads irmãos:** AI SDR Outbound Signal-Based, Social Selling & Inbound LinkedIn, Voz para Cold Calling & Discovery

## Estrutura

```
vendas-voz-cold-calling-discovery/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
