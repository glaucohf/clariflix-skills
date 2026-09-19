# Squad Speed-to-Lead

> Todo lead inbound respondido em menos de 60 segundos, 24/7 — antes do concorrente atender o telefone.

**Área:** Vendas · **TopSquad:** V2 Qualificação Conversacional & Speed-to-Lead · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Leads inbound esfriam em minutos: pesquisas MIT mostram queda de 100x na taxa de conversao quando o primeiro contato ultrapassa 5 minutos. A maioria das empresas leva horas — ou dias. Sem resposta instantanea 24/7 o lead ja fechou com o concorrente. O squad elimina o gap de tempo entre intencao de compra e primeiro contato qualificado, atuando em todos os canais simultaneamente sem depender de agenda humana.

## Impacto esperado

Reducao do tempo de primeiro contato de horas para menos de 60 segundos (baseline MIT: >5min = 100x queda de conversao). ROI estimado: aumento de 20-40% na taxa de conversao de inbound em 90 dias; reducao de 60-80% no custo por lead qualificado (QL) ao eliminar SDR humano em qualificacao inicial; capacidade de processar 10x mais leads sem headcount adicional. Para uma empresa com 200 leads/mes e ticket medio R$5.000, mover taxa de conversao de 5% para 8% = R$30.000/mes de receita incremental — payback do squad em 2-3 meses.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `claude-opus` · Claude Opus | Maestro Comercial (Claude Opus) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `flash` · Flash | Flash — Worker de Primeiro Contato | L2 · orquestra / decide | `enviar-primeira-resposta-ao-lead.md` |
| `sherlock` · Sherlock | Sherlock — Worker de Enriquecimento de Lead | L1 · worker autônomo | `enriquecer-dossie-lead.md` |
| `socrates` · Sócrates | Sócrates — Worker de Qualificacao Conversacional | L2 · orquestra / decide | `qualificar-lead-conversacionalmente.md` |
| `atlas` · Atlas | Atlas — Worker de Agendamento | L2 · orquestra / decide | `agendar-reuniao.md` |
| `argos` · Argos | Argos — Worker de Lead Scoring e Priorizacao | L1 · worker autônomo | `priorizar-leads.md` |
| `eco` · Eco | Eco — Worker de Follow-up e Nurture | L2 · orquestra / decide | `gerenciar-cadencias-de-follow-up.md` |
| `sdr-por-ligacao` · SDR por Ligacao | Vox — Worker de Voz (SDR por Ligacao) | L3 · aprovação humana | `realizar-ligacao-qualificadora.md` |
| `sentinel` · Sentinel | Sentinel — Critic de Mensagem e Compliance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-speed-to-lead:claude-opus` (ou instale via `npx squads add ./vendas-speed-to-lead`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-speed-to-lead-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead
- Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto
- Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio
- Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel
- Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano
- Reagendamento apos segundo no-show — Atlas escala para closer decidir se continua ou descarta lead
- Lead demonstra sinal negativo forte (reclamacao de contato excessivo, solicitacao de opt-out) — intervencao humana obrigatoria e imediata

## KPIs

- Speed-to-Lead: % de leads respondidos em < 60 segundos (meta: >95%)
- Taxa de conversao Lead -> SQL: benchmark atual vs. pos-squad (meta: +25% em 90 dias)
- Taxa de agendamento: % de SQLs que chegam a reuniao agendada (meta: >40%)
- Show rate: % de reunioes que efetivamente ocorrem (meta: >75% com lembretes do Atlas)
- Custo por Lead Qualificado (CPL-Q): reducao vs. baseline humano (meta: -50%)
- Cadencia de follow-up: % de leads que recebem ao menos 3 tentativas de contato (meta: 100%)
- Taxa de opt-out / reclamacao: indicador de saude da cadencia (meta: <0.5%)
- Task success rate no Langfuse: dev 70% / staging 85% / prod 95%
- Tempo medio de qualificacao (Flash->Socrates->SQL): meta < 15 minutos para leads responsivos
- Receita influenciada pelo squad: deals fechados onde o squad realizou o primeiro contato e qualificacao

## Integrações

- CRM: HubSpot (MCP disponivel) / Pipedrive / Salesforce — fonte de verdade de leads, contatos, deals e historico
- WhatsApp Business API: Gupshup / AiSensy / Interakt / QuickReply.ai — canal principal no Brasil, envio/recepcao de mensagens
- Voz IA: Vapi (<600ms latencia) ou Retell AI — ligacoes de qualificacao automatizadas com voz natural
- TTS: ElevenLabs — voz da marca para ligacoes do Vox
- STT: Deepgram — transcricao de calls em tempo real
- Email: Gmail API / Outlook API — cadencias de email do Eco e confirmacoes do Atlas
- Calendario: Google Calendar / Outlook Calendar — agendamento e lembretes do Atlas
- Enriquecimento: Clay + Apollo (275M+ contatos) — dados do Sherlock
- Intent Data: sinais de ads (Meta Ads, Google Ads) + plataformas de intent — gatilhos para o Argos
- Observabilidade: Langfuse (OTEL) — quality gates, evals, rastreamento de tasks por agente
- Gestao de tarefas: ClickUp — artefatos verificaveis por task, prova de trabalho auditavel
- Notificacoes internas: Slack / WhatsApp Business — alertas de lead quente e HITL para closers
- Videoconferencia: Google Meet / Zoom / Teams — links de reuniao gerados pelo Atlas

## Entregável (prova de trabalho)

Dossie de Lead Completo por Contato: documento estruturado (JSON + nota no CRM) contendo timestamp de cada etapa (primeiro contato, enriquecimento, qualificacao, agendamento), scorecard BANT preenchido, score de ICP, transcricao/sumario das interacoes por canal, proximo passo recomendado e closer responsavel. Auditavel em tempo real no ClickUp com tasks vinculadas por lead. Dashboard de KPIs atualizado em tempo real com metricas de velocidade, volume e conversao.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mae Intuitiva CRM (squadshub) — base para gestao de leads e integracao conversacional com CRM; ja tem logica de recepcao de inbound e roteamento que pode ser adaptada para o Orchestrator Maestro Comercial e o Flash
- Skeptic Protocol (5 agentes de red-team/QA) — base direta para o Sentinel; logica de verificacao adversarial e compliance antes de acoes externas se encaixa exatamente no papel de Critic do squad
- Data Quality Guardian (5 agentes de qualidade de dados) — base para o Sherlock e para higiene do CRM; ja implementa dedup, enriquecimento e validacao de campos que o Worker de Enriquecimento precisa

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V2 · TopSquad de Qualificação Conversacional & Speed-to-Lead** — Responde em segundos, qualifica em conversa, nunca perde a janela de ouro.

- **Missão:** Captura o lead no instante da entrada (form, anúncio, DM) e conduz, sem pausa, uma qualificação natural (BANT/SPIN) em WhatsApp/chat — antes que o interesse esfrie. Um único fluxo do "oi" ao "qualificado e roteável".
- **Por que consolidar:** Speed-to-lead sem qualificação é só velocidade vazia; qualificação sem velocidade chega depois que o lead esfriou. Eram o mesmo evento — a primeira resposta — partido em dois squads. Juntos viram um agente conversacional que responde no segundo zero e já qualifica na mesma thread.
- **Squads irmãos:** Speed-to-Lead, Qualificação Conversacional (WhatsApp)

## Estrutura

```
vendas-speed-to-lead/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
