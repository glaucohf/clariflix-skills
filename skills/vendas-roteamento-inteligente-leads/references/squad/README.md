# Squad de Roteamento Inteligente de Leads

> Cada lead no vendedor certo, no segundo certo — zero fila errada, zero lead órfão.

**Área:** Vendas · **TopSquad:** V3 Scoring, Roteamento & Agendamento · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Leads chegam de multiplos canais (ads, WhatsApp, site, indicacao) e caem manualmente em filas genericas ou no primeiro vendedor disponivel, ignorando score, territorio, especialidade e capacidade real. O resultado e contato tardio (>5 min ja reduz conversao em 80%), desbalanceamento de carteira e leads que morrem sem followup. Sem roteamento automatico por regras compostas (score + territorio + especialidade + disponibilidade), a operacao desperdicou ciclos de venda e deixa receita na mesa.

## Impacto esperado

Redução de tempo de primeiro contato de horas para <2 minutos (+80% conversão no primeiro contato segundo Harvard Business Review); aumento de 25-40% na taxa de conexão com leads (benchmarks Salesforce/HubSpot); redução de 60% em leads órfãos (sem follow-up); balanceamento de carteira reduz churn de vendedores sobrecarregados; ROI estimado: para uma operação com 500 leads/mês e ticket médio de R$5.000, recuperar 15% dos leads órfãos = R$37.500/mês adicional. Payback do squad em 30-60 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orquestrador-comercial` · Orquestrador Comercial | Maestro (Orquestrador Comercial) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `worker-de-enriquecimento` · Worker de Enriquecimento | Argos (Worker de Enriquecimento) | L1 · worker autônomo | `retornar-dossie-estruturado.md` |
| `worker-de-lead-scoring` · Worker de Lead Scoring | Oracle (Worker de Lead Scoring) | L1 · worker autônomo | `calcular-score-lead.md` |
| `atlas` · Atlas | Atlas (Worker de Disponibilidade e Capacidade) | L1 · worker autônomo | `consultar-capacidade-vendedores.md` |
| `worker-de-notificacao-e-aceite` · Worker de Notificação e Aceite | Hermes (Worker de Notificação e Aceite) | L3 · aprovação humana | `notificar-vendedor-lead.md` |
| `worker-de-higiene-de-crm` · Worker de Higiene de CRM | Mnemosyne (Worker de Higienê de CRM) | L2 · orquestra / decide | `consolidar-dados-crm.md` |
| `veredito` · Veredito | Veredito (Critic / Verifier de Roteamento) | L2 · orquestra / decide | `verificar-roteamento.md` |
| `farol` · Farol | Farol (Worker de Monitor de SLA e Re-roteamento) | L2 · orquestra / decide | `monitorar-primeiro-contato.md` |
| `veredito-2` · Veredito 2 | Veredito (Critic / Verifier de Roteamento) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-roteamento-inteligente-leads:orquestrador-comercial` (ou instale via `npx squads add ./vendas-roteamento-inteligente-leads`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-roteamento-inteligente-leads-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro deploy; em produção, amostras aleatórias (10%) passam por revisão humana
- L3 — Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratamento especial
- L3 — Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente
- L3 — Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interface de configuração, com log de auditoria
- L3 — Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor designado
- Revisão humana semanal do relatório de auditoria do Veredito para identificar vieses sistemáticos e calibrar o modelo de scoring

## KPIs

- Tempo de primeiro contato: mediana <2 minutos (baseline atual a medir no Discovery)
- Taxa de leads órfãos (sem follow-up em 24h): redução para <5% (baseline típico 30-50%)
- Taxa de aceite de roteamento pelo vendedor: >90% (mede qualidade do roteamento)
- Acurácia de roteamento (lead no vendedor certo, validado por vendedor): >85% em staging, >95% em prod
- Taxa de re-roteamento por SLA vencido: <10% dos leads (mede capacidade de Atlas)
- Score de qualidadê de dâdos do CRM (Mnemosyne): >85/100
- Taxa de conversão do primeiro contato (lead aceito vs deal aberto): aumento de 15-25% vs baseline
- Distribuição de carteira (Gini coefficient de leads por vendedor): <0.3 (mede balanceamento)
- Task success rate no Langfuse: 70% dev / 85% staging / 95% prod

## Integrações

- CRM: HubSpot (MCP HubSpot disponível) ou Pipedrive/Salesforce via API — leitura e escrita de leads, contatos, deals, atividades
- WhatsApp Business API: Gupshup ou AiSensy (crítico Brasil) — notificação de vendedores e mensagem de apresentação ao lead
- Calendário: Google Calendar e/ou Microsoft Outlook via MCP — consulta de disponibilidade em tempo real para Atlas
- Enriquecimento: Clay (principal) + Apollo.io (275M+ contatos) — enriquecimento automático pelo Argos
- Comunicação interna: Slack — alertas do Farol e notificações do Hermes para vendedores
- Gestão de tarefas/prova de trabalho: ClickUp — cada roteamento gera task com artefato verificável (card de lead + decisão documentada)
- Observabilidade: Langfuse (OTEL) — rastreamento de todas as decisões de roteamento, latência por agente, quality gates
- Ads/Sinais de intenção: Meta Ads + Google Ads (UTM params) — contexto de origem do lead para scoring de intenção do Oracle
- Orquestração: LangGraph (controle fino de estado do funil) + Claude Agent SDK (Maestro como Ópus lead, workers como Sonnet)

## Entregável (prova de trabalho)

Card de Roteamento Verificado: artefato JSON gerado por decisao de roteamento, contendo {lead_id, timestamp_entrada, timestamp_roteamento, dossie_enriquecido, score_oracle_breakdown, vendedor_designado, justificativa_roteamento, veredicto_critic, sla_aplicado, status_aceite, timestamp_primeiro_contato}. Artefato e registrado no CRM como atividade, linkado no ClickUp como task concluida com prova de trabalho, e indexado no Langfuse para observabilidade e quality gates. Dashboard em tempo real mostra todos os roteamentos do dia com status de SLA.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM (squad gratuito) — base para lógica de CRM/leads, gestão de estado do funil e integração com WhatsApp; acelera implementação do Maestro e Hermes
- Data Quality Guardian (5 ag, qualidade de dados) — base para o Mnemosyne; logica de dedup, normalizacao e higiene de dados ja testada e reutilizavel
- Skeptic Protocol (5 ag, red-team/QA) — base para o Veredito; framework de critic/verifier com logica de auditoria, deteccao de vieses e relatorio de qualidade

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V3 · TopSquad de Scoring, Roteamento & Agendamento** — Pontua, decide o dono certo e entrega a reunião confirmada — sem mão humana no meio.

- **Missão:** A cadeia de decisão pós-qualificação: pontua o lead, decide quem o atende (território/skill/carga) e o conduz ao calendário confirmado com lembretes anti-no-show e briefing pré-reunião. Score → route → book em um fluxo só.
- **Por que consolidar:** São três elos de uma corrente única — o score define a prioridade que define o roteamento que define o agendamento. Separados, cada um relia o CRM e recalculava o estado do lead. Unificados, o mesmo modelo de priorização alimenta diretamente o booking.
- **Squads irmãos:** Lead Scoring Preditivo & Priorização, Roteamento Inteligente de Leads, Agendamento — Appointment Setting

## Estrutura

```
vendas-roteamento-inteligente-leads/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
