# Squad Dormant Lead Reactivation

> Cada lead dormente na sua base e CAC já pago esperando ser resgatado — o squad que transforma necromarketing em pipeline real sem gastar um centavo em nova aquisição.

**Área:** Marketing · **TopSquad:** M5 Captura, Qualificação & Reativação de Leads · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Empresas investem R$300-1.500 de CAC por lead e depois deixam 60-80% da base apodrecer sem follow-up estruturado. Leads que nao converteram no primeiro ciclo nao sao perdidos — sao oportunidades que exigem o timing certo, o angulo certo e a mensagem certa. O squad resolve tres falhas simultaneas: (1) falta de profiling atualizado dos leads dormentes — nao se sabe se o contexto deles mudou desde o primeiro contato; (2) ausencia de sequencias personalizadas para reativacao — os poucos follow-ups que acontecem sao genericos e tem taxa de resposta <2%; (3) ausencia de priorizacao baseada em sinais — sem saber quem esta mais proximo de comprar agora, os esforos humanos sao mal alocados. Mensuravel por: leads reativados (resposta positiva ou reuniao agendada), pipeline reaberto (R$ de oportunidades reativadas), e custo por reativacao vs. custo de novo lead (meta: reativacao custa 5-10x menos que novo lead).

## Impacto esperado

Para uma base de 2.000 leads dormentes com CAC medio de R$600 ja investido: valor latente na base = R$1.2M de aquisicao ja paga e esquecida. Com taxa de reativacao realista de 8-15% (benchmark de campanha de win-back B2B personalizada vs 1-3% de outreach generico), o squad recupera 160-300 leads para pipeline ativo. Assumindo ticket medio de R$8k e taxa de conversao de lead reativado para deal de 15-20%: 160 leads reativados x 17% de conversao = 27 novos deals x R$8k = R$216k de receita incremental por rodada de reativacao. Custo da rodada de reativacao (tokens + APIs + horas de HITL): estimado R$3-8k. ROI direto por rodada: 27x-72x sobre o custo da operacao. Comparativo critico: custo de novo lead = R$600 CAC; custo de reativacao via squad = R$15-30 por lead processado (sem campanha de midia). Reducao de CAC efetivo em 20-40x para leads ja na base.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `lazaro` · Lazaro | Lazaro — O Ressuscitador de Pipeline | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `arqueologa` · Arqueologa | Arqueóloga — A Detetive do Passado | L0 · worker determinístico | `reconstruir-historico-lead.md` |
| `radar` · Radar | Radar — O Caçador de Sinais Novos | L1 · worker autônomo | `verificar-mudancas-em-leads.md` |
| `oraculo-scorer` · Oraculo Scorer | Oraculo Scorer — O Priorizador de Ressurreicao | L0 · worker determinístico | `calcular-score-de-reativacao-lead.md` |
| `lazaro-writer` · Lázaro Writer | Lázaro Writer — O Alquimista de Segunda Chance | L2 · orquestra / decide | `redigir-mensagens-de-reativacao.md` |
| `charon-dispatcher` · Charon Dispatcher | Charon Dispatcher — O Operador da Travessia | L3 · aprovação humana | `enviar-mensagens-reativacao.md` |
| `echo-analyst` · Echo Analyst | Echo Analyst — O Intérprete do Eco | L1 · worker autônomo | `analisar-respostas-leads.md` |
| `atena` · Atena | Atena — A Guardiã da Segunda Chance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-dormant-lead-reactivation:lazaro` (ou instale via `npx squads add ./marketing-dormant-lead-reactivation`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-dormant-lead-reactivation-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao.
- Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado.
- Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio.
- Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa.
- Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática.
- Sinais de oportunidade detectados em lead que estava em ARQUIVO (score < 40): Radar detecta mudança significativa (investimento, mudança de decisor, sinal de intent forte) em lead que havia sido desprioritizado — alerta ao gestor para decisão de reintegrar o lead na fila ativa ou manter desprioritizado.
- Relatório semanal de performance: Echo Analyst gera relatório de taxa de reativação por trilha e archetype entregue ao gestor todo friday — ponto de HITL estruturado para revisão de qual trilha está funcionando e quais ajustes de playbook são necessários antes da próxima rodada.
- Opt-out recebido: processamento automático cancela a sequência e atualiza o CRM, mas a decisão de blacklist permanente (nunca mais contatar) é sempre humana — o agente sinaliza e aguarda confirmação do gestor antes de registrar blacklist definitiva.

## KPIs

- Taxa de reativação por rodada: percentual de leads dormentes que respondem positivamente (categoria RESSUSCITADO ou MORNO_NOVO) — baseline histórico de win-back B2B genérico e 1-3%, meta com squad personalizado e 8-15%
- Pipeline reaberto (R$/rodada): valor total de oportunidades criadas ou reativadas no CRM atribuídas a cada rodada de reativação — meta: ROI de 20x sobre o custo operacional da rodada em 90 dias
- Custo por lead reativado vs custo de novo lead (CAC): meta de reativação custa 5-15x menos que novo lead do mesmo segmento — KPI principal de justificativa econômica do squad
- Taxa de aprovacao do critic Atena no primeiro ciclo: meta > 65% — indica qualidade dos playbooks de reativacao e calibragem dos templates do Lazaro Writer
- Taxa de reativação por archetype de dormência: qual dos 5 archetypes (Nunca Respondeu, Engajou Sem Converter, Timing, Concorrente, Fantasma) tem maior taxa de sucesso — orienta priorização das próximas rodadas
- Taxa de reativação por trilha x canal: email vs WhatsApp vs LinkedIn por cluster — orienta alocação de canal por segmento nas próximas rodadas
- Tempo de ciclo da rodada: da ingestão da lista dormente ao primeiro draft aprovado enviado — meta menos de 4 horas para lotes de até 200 leads
- Taxa de task success por agente no Langfuse: gate de produção = 95% por agente — abaixo disto aciona alerta e revisão do agente com problema
- Taxa de opt-out por rodada: meta abaixo de 3% — acima disto indica problema de segmentação (enviando para leads que não deveriam estar na rodada) ou de qualidade de copy (ângulo muito agressivo para reativação)
- Percentual de leads reativados que progridem para oportunidade no CRM (30, 60, 90 dias): meta 15-25% dos RESSUSCITADOS viram oportunidade formal — valida a qualidade da reativação além do mero engajamento superficial

## Integrações

- CRM: HubSpot (MCP disponível — fonte de verdade para o estado de cada lead dormente, activities, histórico de interações, campo de score de reativação, pipeline de oportunidades reativadas), Salesforce com Agentforce SDK ou Pipedrive como alternativas
- Enriquecimento e sinais novos: Clay (waterfall de 100+ fontes para atualização de dados, intent signals, sinais de mudança de empresa e headcount), Apollo.io (verificação de email atual, cargo atual, sinais de mudança de emprego), LinkedIn Sales Navigator (mudanças de cargo, promoções, expansões de headcount)
- Validação de email: NeverBounce ou ZeroBounce integrados via Clay waterfall para verificação antes de qualquer envio — bounce em reativação e mais custoso que em cold (queima relação pre-existente)
- Email reativação: Instantly.ai ou Lemlist (sequências com rastreamento de abertura e click, warmup de domínio para proteger reputação), SendGrid ou AWS SES para volume alto
- WhatsApp Business API: plataformas purpose-built para mercado brasileiro — Gupshup, AiSensy ou QuickReply.ai (conformidade pós-restricoes Meta 2024, templates pré-aprovados para reativação B2B)
- LinkedIn outreach: Sales Navigator para verificação de dados + Phantombuster ou Expandi para automação controlada de InMails dentro dos limites diários
- Calendário para booking: Calendly ou Cal.com integrado ao Charon Dispatcher para envio automático de link de agendamento quando lead responde positivamente, sem intervenção humana no booking
- Gestão de tasks e artefatos: ClickUp (prova de trabalho verificável por rodada de reativação — ficha de arqueologia, ficha de sinais, score com breakdown, draft aprovado com checklist do crític, log de envio, análise de resposta) conectado ao Lázaro via MCP ou webhook
- Orquestração multi-agente: LangGraph para controle de estado do funil de reativação por lead (grafos de decisão: dormente -> em sequência -> reativado -> oportunidade -> fechado/arquivado) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (traces OTEL por agente, quality gates dev 70% / staging 85% / prod 95%, dashboard de reativação com KPIs em tempo real, alertas de anomalia quando taxa de bounce ou opt-out sobe acima do threshold)
- Notificações internas: Slack ou WhatsApp do vendedor/gestor para alertas de HITL urgentes, leads RESSUSCITADOS detectados e relatório semanal de ROI de reativação
- No-code complementar: n8n para automações de integração — webhook de resposta de email para Echo Analyst, cron de batch semanal de novos dormentes, sync de score de reativação para CRM custom fields sem código

## Entregável (prova de trabalho)

Rodada de Reativacao Verificavel e Auditavel: (1) Mapa de Base Dormentes — segmentacao completa por archetype, cluster e prioridade (Arqueologa + Oraculo Scorer) exportado como planilha e salvo no ClickUp, linkado ao CRM; (2) Ficha de Sinais Novos por lead processado (Radar) com mudancas detectadas, fontes verificadas e angulo de reativacao — salva no ClickUp e dados atualizados no CRM; (3) Pack de Reativacao aprovado por lead: drafts A/B por toque da sequencia com checklist do critic Atena preenchido, score de qualidade e compliance confirmado — versionado no ClickUp; (4) Log de Envio imutavel (Charon Dispatcher): timestamp, canal, variacao A/B, status de cada mensagem com rastreamento de abertura e click — activity no CRM e ClickUp; (5) Analise de Resposta estruturada (Echo Analyst): categoria de reativacao, objecao detectada, coaching note para o vendedor, proximo passo recomendado — CRM atualizado, notificacao ao vendedor; (6) Relatorio Executivo de ROI da Rodada: leads processados, taxa de reativacao por trilha e archetype, pipeline reaberto em R$, custo por lead reativado vs CAC original, variacoes A/B vencedoras, recomendacoes para proxima rodada — entregue ao gestor via ClickUp e Slack/email. Todo o pipeline e auditavel por design: cada artefato tem agente responsavel, timestamp, veredicto do critic e rastro no Langfuse. O gestor ve o ROI completo de cada centavo do CAC que foi resgatado.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 agentes, red-team/QA) — base direta para o crític Atena: o framework de crítica adversarial com checklist multi-ponto pode ser adaptado como a estrutura dos 10 pontos de validação específicos para reativação, acelerando em semanas o desenvolvimento do gate de qualidade que protege a relação pre-existente com o lead — erro em reativação é pior que erro em cold outreach.
- Mae Intuitiva CRM (CRM/leads) — base para o Oraculo Scorer e a camada de integracao com CRM: a logica de scoring de leads, atualizacao de campos customizados, gestao de estado no funil e sincronizacao de atividades pode ser reutilizada e reparametrizada para o contexto especifico de reativacao (archetype de dormencia, score de reativacao, trilha atribuida), evitando construir do zero a camada de persistencia de estado.
- Data Quality Guardian (5 agentes, qualidade de dados) — base para a Arqueologa e o Radar na camada de verificação e enriquecimento de dados dormentes: o squad especializado em qualidade de dados tem os patterns de detecção de dados desatualizados, validação de emails em lote e reconciliação de registros duplicados que são críticos para reativação — enviar para email errado ou para pessoa que mudou de empresa destroi a credibilidade da campanha.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M5 · TopSquad de Captura, Qualificação & Reativação de Leads** — Da captura à qualificação e ao reaquecimento da base adormecida.

- **Missão:** A ponte entre Marketing e Vendas: pontua e roteia os leads gerados pelas campanhas, qualifica via WhatsApp e reativa a base adormecida que o marketing já pagou para adquirir. Garante que nenhum lead capturado se perca.
- **Por que consolidar:** Os três operam sobre o mesmo objeto — o lead que o marketing capturou — em momentos distintos: na entrada (score/router), na conversa (WhatsApp) e no esfriamento (reativação). É o mesmo ciclo de vida do lead de marketing, partido em três. Espelha o V2/V3/V4 de Vendas; aqui fica do lado de marketing por nutrir o lead pago.
- **Squads irmãos:** Lead Scoring & Router, WhatsApp Qualifier, Dormant Lead Reactivation

## Estrutura

```
marketing-dormant-lead-reactivation/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
