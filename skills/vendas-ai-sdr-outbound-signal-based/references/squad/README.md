# Squad AI SDR Outbound Signal-Based

> Do sinal de intenção ao slot agendado em menos de 90 segundos, personalizado por IA e aprovado por crític antes de tocar o lead.

**Área:** Vendas · **TopSquad:** V1 Prospecção & Outbound Multicanal · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Prospeccao outbound manual e lenta, generica e nao escala. Sem deteccao de sinais e personalizacao em escala validada por critic, as taxas de resposta despencam e o SDR humano nao cobre o volume necessario para alimentar o funil com leads qualificados.

## Impacto esperado

Aumento de 3-5x no volume de leads qualificados prospectados por semana sem adição de headcount. Redução do tempo de resposta a sinais de intenção de horas/dias para menos de 2 minutos (benchmark: empresas que respondem em 5min têm 21x mais chance de qualificar). Taxa de resposta a cold outreach pode subir de 1-3% para 8-15% com hiperpersonalização signal-based validada por crític. ROI estimado: para uma empresa fechando 10 deals/mês a R$5k ticket médio, um aumento de 30% na taxa de conversão de leads qualificados = R$15k/mês adicionais — payback do squad em 30-45 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · Nexus | Nexus — O Maestro Comercial | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Radar — Detector de Sinais de Intenção | L1 · worker autônomo | `detectar-sinais-intencao.md` |
| `sherlock` · Sherlock | Sherlock — Pesquisador de Conta | L1 · worker autônomo | `construir-dossie-completo.md` |
| `magnus` · Magnus | Magnus — Scorer e Priorizador de Leads | L0 · worker determinístico | `classificar-leads.md` |
| `penna` · Penna | Penna — Copywriter de Outreach Multicanal | L2 · orquestra / decide | `redigir-mensagens-personalizadas.md` |
| `vox` · Vox | Vox — Dispatchêr e Agendador | L3 · aprovação humana | `agendar-mensagens.md` |
| `lumen` · Lumen | Lumen — Analista de Conversação e Coaching | L1 · worker autônomo | `analisar-respostas-recebidas.md` |
| `argus` · Argus | Argus — Verificador de Mensagens e Compliance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-ai-sdr-outbound-signal-based:nexus` (ou instale via `npx squads add ./vendas-ai-sdr-outbound-signal-based`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-ai-sdr-outbound-signal-based-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo.
- Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial.
- Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual.
- Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo.
- Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach.
- Unsubscribe ou resposta negativa agressiva: processado pelo Lumen, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente.

## KPIs

- Volume de leads prospectados por semana (baseline vs pós-implantação, meta: 3-5x)
- Tempo de resposta a sinal de intenção: da detecção ao primeiro outreach enviado (meta: <2 minutos para sinais HOT)
- Taxa de aprovação do Critic no primeiro ciclo (meta: >70% sem reescritura)
- Taxa de resposta ao cold outreach por canal (email: meta >8%, WhatsApp: meta >20%, LinkedIn: meta >12%)
- Taxa de conversão de lead contactado para reunião agendada (meta: >15% em HOT leads)
- Número de reuniões agendadas por semana (meta: 3-5x o baseline manual)
- Score médio de personalização das mensagens aprovadas (Argus metric, meta: >7/10)
- Taxa de tâsk success no Langfuse por agênt (gâte: dêv 70% / stâging 85% / prôd 95%)
- Redução de tempo do SDR humano em tarefas de pesquisa e redação (meta: liberação de 60%+ do tempo para calls e fechamento)
- Pipeline gerado pelo squad em R$ (meta: ROI 3x no primeiro trimestre)

## Integrações

- CRM: HubSpot (MCP disponível), Pipedrive ou Salesforce — fonte de verdade para estado do lead e log de atividades
- Enriquecimento de dados: Clay (enriquecimento em escala via workflows), Apollo.io (275M+ contatos, intent data, sequências)
- Email: SendGrid ou AWS SES (envio transacional), Instantly.ai ou Lemlist (warmup de domínio e sequências cold)
- WhatsApp Business API: Gupshup, AiSensy ou QuickReply.ai (crítico para o mercado brasileiro)
- LinkedIn: Phantombuster ou Expandi (automação de InMail/connection request dentro dos limites)
- Voz AI: Vapi (<600ms latência) com Deepgram STT + Claude/GPT LLM + ElevenLabs TTS para cold calls automatizadas
- Calendário: Calendly ou Cal.com (booking automático via link ou conversacional)
- Intent data e sinais: LinkedIn Sales Navigator, Bombora (intent data B2B), Google Alerts (menções de empresa)
- Gestão de tarefas e prova de trabalho: ClickUp (artefatos verificáveis por task — dossiê, draft aprovado, log de envio)
- Orquestração: LangGraph (controle fino de estado do funil) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (OTEL) para quality gates dev 70% / staging 85% / prod 95% task success
- Notificações internas: Slack ou WhatsApp do SDR humano para alertas de HITL e leads HOT

## Entregável (prova de trabalho)

Pacote de outreach verificado e rastreável por lead: (1) Dossiê de conta estruturado (Sherlock) salvo no ClickUp e CRM, (2) Draft de mensagem aprovado pelo Argus com score de personalização e checklist de compliance, (3) Log de envio com timestamp e canal no CRM e ClickUp, (4) Score de lead atualizado com breakdown (Magnus), (5) Análise de resposta com intenção e próxima ação sugerida (Lumen). Todo o pipeline é auditável: cada artefato tem prova de trabalho com agente responsável, timestamp e veredicto do critic.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 agentes, red-team/QA) — base para o Argus: o protocolo de crítica adversarial pode ser adaptado para o checklist de 8 pontos do critic de mensagens, acelerando o desenvolvimento do gate de qualidade.
- Mãe Intuitiva CRM (CRM/leads) — base para o Magnus e a integração de CRM: lógica de scoring, atualização de campos e gestão de estado de leads pode ser reutilizada e customizada para o contexto de outreach signal-based.
- Data Quality Guardian (5 agentes, qualidade de dados) — base para o Sherlock e a higiene de CRM: os agentes de validação e enriquecimento de dados podem acelerar a construção do pipeline de dossiê de conta e dedup de leads.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V1 · TopSquad de Prospecção & Outbound Multicanal** — Do sinal de intenção ao primeiro toque humano-grade — e-mail, social ou voz — sempre aprovado por um critic.

- **Missão:** Motor único de geração de demanda fria: detecta sinais de intenção, escolhe o canal certo (e-mail, LinkedIn/social ou ligação por voz), hiperpersonaliza a abordagem e dispara cadências cross-channel — tudo validado por um critic antes de tocar o lead.
- **Por que consolidar:** Os três squads absorvidos compartilhavam o mesmo cérebro — detecção de sinal + enriquecimento + personalização + critic anti-spam — e divergiam apenas no canal de saída. Unificados, viram um orquestrador que decide o canal por contexto e habilita cadência cross-channel (e-mail → social → voz no mesmo lead).
- **Squads irmãos:** AI SDR Outbound Signal-Based, Social Selling & Inbound LinkedIn, Voz para Cold Calling & Discovery

## Estrutura

```
vendas-ai-sdr-outbound-signal-based/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
