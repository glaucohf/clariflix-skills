# Squad de Qualificação Conversacional (WhatsApp)

> Seu melhor SDR nunca dorme, nunca perde um lead e qualifica BANT/MEDDIC em 3 mensagens no WhatsApp.

**Área:** Vendas · **TopSquad:** V2 Qualificação Conversacional & Speed-to-Lead · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Vendedores desperdicam 60-70% do tempo com leads sem fit, sem budget ou sem autoridade de decisao. Sem triagem automatica no canal de maior taxa de abertura do Brasil (WhatsApp: 98%), o pipeline fica congestionado, o CAC sobe e o closer perde deals que importam. O squad intercepta cada lead na entrada, conduz um dialogo consultivo BANT/MEDDIC estruturado em linguagem natural, pontua o fit em tempo real e so entrega ao humano o lead validado — com dossie preenchido, score calculado e slot de reuniao reservado.

## Impacto esperado

Redução de 65% no tempo de SDR gasto com leads sem fit (benchmark: squads de SDR conversacional como Vivo/Alana/11x). Taxa de qualificação esperada: de 12% (média manual) para 35-42% dos leads que chegam ao CRM. Redução do ciclo de qualificação de 48-72h para menos de 8 minutos. ROI estimado: para 300 leads/mês a R$150 CAC médio, economiza ~R$27.000/mês em custo de SDR + libera closer para triplicar taxa de fechamento em deals qualificados. Payback do squad em 45-90 dias para carteiras com ticket médio acima de R$5k.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro-comercial` · Maestro Comercial | Maestro Comercial — Orion | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `investigador-de-lead` · Investigador de Lead | Investigador de Lead — Sherlock | L1 · worker autônomo | `enriquecer-dossie-lead.md` |
| `sdr-conversacional` · SDR Conversacional | SDR Conversacional — Véra | L2 · orquestra / decide | `conduzir-conversa-estruturada.md` |
| `juiz-de-fit` · Juiz de Fit | Juiz de Fit — Magnus | L1 · worker autônomo | `priorizar-leads.md` |
| `agendador-de-reunioes` · Agendador de Reuniões | Agendador de Reuniões — Tempo | L2 · orquestra / decide | `agendar-reuniao.md` |
| `reativador-de-pipeline` · Reativador de Pipeline | Reativador de Pipeline — Lázaro | L2 · orquestra / decide | `reativar-leads-frios.md` |
| `guardiao-do-crm` · Guardião do CRM | Guardião do CRM — Clio | L1 · worker autônomo | `auditar-saude-do-pipeline.md` |
| `analista-de-conversas` · Analista de Conversas | Analista de Conversas — Éco | L1 · worker autônomo | `analisar-conversas-qualificadas.md` |
| `censor-comercial` · Censor Comercial | Censor Comercial — Veto | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-qualificacao-conversacional-whatsapp:maestro-comercial` (ou instale via `npx squads add ./vendas-qualificacao-conversacional-whatsapp`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-qualificacao-conversacional-whatsapp-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comercial aprova batch antes do disparo.
- HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por desconto, Vera responde 'vou verificar com nosso especialista' e escala ao closer via notificação imediata.
- HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes de qualquer ação automática adicional. Closer decide se assume a conversa ou deixa o squad continuar.
- HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada.
- HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor responde o que fazer; resposta é adicionada ao playbook para aprendizado.
- HITL-6 (L1): Relatório semanal do Eco com sugestões de ajuste de prompt — gestor revisa e aprova antes de qualquer alteração ser aplicada nos prompts da Vera ou nos pesos do Magnus.

## KPIs

- Taxa de qualificação completa: % de leads que completam o fluxo BANT/MEDDIC inteiro (meta: >60% dos leads que iniciam conversa)
- Tempo médio de qualificação: minutos do primeiro contato até scorecard gerado (meta: <8 minutos)
- Taxa de conversão Lead-to-Meeting: % de leads qualificados que agendam reunião (meta: >35%)
- Qualidade dos leads entregues: avaliação do closer sobre leads recebidos 1-5 (meta: média >4.2)
- Taxa de abandono por etapa: % de leads que dropam em cada pergunta BANT (diagnóstico de gargalo)
- Task success rate por agente: monitorado no Langfuse (dev 70% / staging 85% / prod 95%)
- Score médio dos leads qualificados: média do score Magnus na fila do closer (meta: >65)
- Taxa de reativação de leads frios: % de COLD que voltam ao funil com Lazaro (meta: >15% em 30 dias)
- CAC de qualificação: custo por lead qualificado (tokens LLM + custo de ferramentas / n. de leads qualificados)
- Taxa de falso positivo: % de leads classificados HOT que não avançam apos reuniao com closer (meta: <20%)

## Integrações

- WhatsApp Business API via Gupshup ou AiSensy (envio/recepção de mensagens, webhooks de status)
- HubSpot CRM via MCP HubSpot oficial (leitura e escrita de contatos, deals, propriedades customizadas, activities)
- Google Calendar ou Calendly API (disponibilidade de closers, criação de eventos, webhooks de cancelamento)
- Meta Ads Lead Ads (webhook de novo lead -> N8N -> Orchestrator)
- Apollo.io ou Clay (enriquecimento de dados B2B: empresa, cargo, contato)
- N8N como middleware de webhook (recebe sinais de múltiplas fontes e normaliza payload para o Orchestrator)
- ClickUp (artefatos verificáveis por task: scorecards, conversation logs, relatórios de higiene e intelligence)
- Langfuse OTEL (observabilidade de todas as chamadas LLM: latência, tokens, task success rate por agente, evals customizados)
- LangGraph (orquestração do grafo de agentes com estado persistente por lead_id)
- Claude API — Opus 4 para Orchestrator e Critic; Sonnet 4 para workers (balanço custo/performance)
- Píxel de site do cliente (sinais de reativação para o Lázaro via webhook de evento personalizado)

## Entregável (prova de trabalho)

Dossiê de Qualificação Acionável: para cada lead processado, o squad entrega ao closer um artefato padronizado contendo — (1) qualification_scorecard.json com score 0-100 por dimensão BANT/MEDDIC, (2) conversation_log completo anotado com as respostas-chave do lead, (3) resumo executivo em 5 bullets (dor principal, budget confirmado, decisor identificado, urgência, objeção principal), (4) slot de reunião agendado ou próximo passo recomendado, (5) deal criado/atualizado no HubSpot com todos os campos preenchidos. Artefato linkado no ClickUp como prova de trabalho verificável.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM — base para lógica de gestão conversacional de leads e integração CRM; adaptar os flows de identificação de intenção e atualização de contato para o contexto BANT/WhatsApp deste squad.
- Skeptic Protocol — usar como blueprint para o Critic/Verifier (Veto); os 5 agentes de red-team do Skeptic Protocol mapeiam diretamente para as dimensões de verificação do Veto (factualidade, tom, compliance, personalização, acionabilidade do scorecard).
- Data Quality Guardian — base para o Worker de Higiene do CRM (Clio); os 5 agentes de qualidade de dados do DQG cobrem deduplicação, validação de schema e enriquecimento — replicar a lógica de auditoria periódica e alertas de anomalia para o contexto do HubSpot deste squad.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V2 · TopSquad de Qualificação Conversacional & Speed-to-Lead** — Responde em segundos, qualifica em conversa, nunca perde a janela de ouro.

- **Missão:** Captura o lead no instante da entrada (form, anúncio, DM) e conduz, sem pausa, uma qualificação natural (BANT/SPIN) em WhatsApp/chat — antes que o interesse esfrie. Um único fluxo do "oi" ao "qualificado e roteável".
- **Por que consolidar:** Speed-to-lead sem qualificação é só velocidade vazia; qualificação sem velocidade chega depois que o lead esfriou. Eram o mesmo evento — a primeira resposta — partido em dois squads. Juntos viram um agente conversacional que responde no segundo zero e já qualifica na mesma thread.
- **Squads irmãos:** Speed-to-Lead, Qualificação Conversacional (WhatsApp)

## Estrutura

```
vendas-qualificacao-conversacional-whatsapp/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
