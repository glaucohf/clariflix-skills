# Squad de Voz-IA para Atendimento Telefônico (PT-BR)

> Atende o telefone, entende o audio do WhatsApp e resolve — sem fila, sem espera, em portugues de verdade.

**Área:** Operações & CS · **TopSquad:** O1 Atendimento & Suporte Conversacional · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Voice notes de WhatsApp (canal #1 no Brasil) e ligacoes telefonicas ficam sem cobertura automatizada: cada audio exige transcricao manual pelo atendente, cada ligacao ocupa um headcount em tempo real, e o backlog cresce enquanto o CSAT cai. O squad processa ASR/TTS em PT-BR com latencia < 1.5s, atende chamadas em fluxo conversacional autonomo, converte audios de WhatsApp em intencoes estruturadas e despacha para os workers especializados de suporte — tudo com prova de trabalho rastreavel no ClickUp e qualidade validada pelo Critic antes de qualquer resposta ao cliente.

## Impacto esperado

Cobertura autonoma target: 60-70% dos audios de WhatsApp e 50-60% das ligacoes resolvidas sem toque humano. Reducao de 70-80% no tempo de transcricao manual (de 3-5 min/audio para < 5 segundos). CSAT em voz: meta >= 4.0/5 (canal historicamente abandonado). Tempo de atendimento telefonico: de fila media de 8-15 min para resposta em < 10 segundos. Para uma operacao com 500 ligacoes/mes + 2.000 voice notes/WhatsApp, ROI estimado: R$20-40k/mes em custo de atendimento evitado + eliminacao de 1-2 posicoes de atendente dedicado a transcricao manual.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Maestro — Orchestrator de Voz & Intencao | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `sono` · Sono | Sono — Agente ASR/TTS PT-BR | L2 · orquestra / decide | `transcrever-e-normalizar-audio.md` |
| `vivo` · Vivo | Vivo — Worker de Dialogo & Coleta de Dados | L1 · worker autônomo | `coletar-dados-necessarios.md` |
| `falco` · Falco | Falco — Worker de Resolucao por Voz | L2 · orquestra / decide | `resolver-intencoes-de-voz.md` |
| `onda` · Onda | Onda — Worker de Acao & Transacao por Voz | L3 · aprovação humana | `escrever-acoes-transacionais.md` |
| `radar` · Radar | Radar — Agente de Sentimento & Risco em Tempo Real | L2 · orquestra / decide | `analisar-sentimento-e-risco.md` |
| `eco` · Eco | Eco — Critic de Qualidade de Voz | L2 · orquestra / decide | `validar-qualidade-de-voz.md` |
| `hertz` · Hertz | Hertz — Agente de Handoff & Escalonamento Telefonico | L2 · orquestra / decide | `gerenciar-transferencia-para-humanos.md` |
| `eco-2` · Eco 2 | Eco — Critic de Qualidade de Voz | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-voz-ia-telefonia:maestro` (ou instale via `npx squads add ./ops-cs-voz-ia-telefonia`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-voz-ia-telefonia-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket prioritario antes de executar
- Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona para humano
- Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente para supervisor
- Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana
- Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especialista
- Cliente VIP, Enterprise ou MRR > R$5k: toda acao irreversivel (cancelamento, mudanca de plano, refund parcial) requer aprovacao do CSM responsavel antes da execucao
- Audio com duracao > 3 minutos e confianca media ASR < 0.82 — transcricao marcada para revisao humana antes do processamento completo pelo Maestro
- Intencao nao reconhecida apos 2 turns de coleta pelo Vivo (confianca < 0.55) — Hertz escalona com transcricao completa para o humano interpretar e resolver
- Solicitacao de dados de terceiros, portabilidade de dados, ou qualquer direito LGPD em voz — Hertz bloqueia automacao e direciona para DPO/time juridico

## KPIs

- Voice Deflection Rate: % de chamadas telefonicas resolvidas autonomamente sem transferencia para humano (meta: >= 50% em 90 dias)
- Audio Deflection Rate: % de voice notes do WhatsApp convertidos em resolucao automatica sem intervencao humana (meta: >= 65% em 90 dias)
- ASR Word Error Rate (WER): taxa de erro de transcricao medida em amostras mensais com ground truth (meta: < 8% para audio de boa qualidade, < 15% para audio com ruido)
- Latencia Fim-a-Fim: tempo entre recebimento do audio e inicio da resposta TTS (meta: < 2.5s para telefone, < 5s para WhatsApp audio)
- CSAT em Voz: pesquisa IVR pos-chamada de 1 pergunta ('0 a 5, como foi seu atendimento?') (meta: >= 4.0/5)
- Taxa de Abandono de Chamada: % de clientes que desligam antes de ser atendidos pelo sistema (meta: reducao de 60% vs baseline atual)
- Critic Rejection Rate: % de respostas rejeitadas pelo Eco antes do TTS (meta: < 10% — indica qualidade dos workers de voz)
- Taxa de Escalonamento Desnecessario: % de escalonamentos para humano que o agente poderia ter resolvido (meta: < 15%)
- Custo por Interacao de Voz: custo total (ASR + TTS + tokens LLM + infra) por interacao processada (meta: < R$0.40 por audio de WhatsApp, < R$1.20 por chamada de 3 min)
- Health Score Update Coverage: % de interacoes de voz que resultam em atualizacao de health score no CRM (meta: 100% das sessoes concluidas)

## Integrações

- Aircall — plataforma de telefonia principal: webhook de chamada entrante, transferencia quente, callback scheduling, disponibilidade de filas em tempo real
- WhatsApp Business API — canal #1 no Brasil: webhook de mensagens de audio (OGG Opus), envio de audio TTS sintetizado, status de entrega de mensagem
- Deepgram Nova-2 PT-BR — ASR principal com vocabulario de dominio customizado (latencia < 300ms para streaming)
- OpenAI Whisper Large-v3 — ASR fallback para audios longos ou de qualidade muito baixa
- ElevenLabs PT-BR ou Azure Neural TTS — sintese de voz com persona da marca (latencia < 400ms)
- ClickUp (Brain2 / MCP server) — hub de tasks e prova de trabalho por interacao de voz, espelhando AIOX
- CRM: HubSpot ou Salesforce — dados de conta, tier, MRR, historico de interacoes, health score
- ERP / OMS — consulta de pedidos, status, estoque (API REST ou MCP customizado, SLA < 1.5s)
- Zendesk / Intercom — criacao de tickets de escalonamento com transcricao e contexto, KB para RAG
- Slack — notificacoes de escalonamento urgente, alertas de churn do Radar, briefings para CSMs
- Supabase / Postgres — estado de sessao dos agentes, health scores, logs de transcricoes, fila de handoffs, consentimentos LGPD
- Langfuse — observabilidade OTEL: tracing de cada step do pipeline de voz (audio -> ASR -> NER -> classificacao -> worker -> critic -> TTS), metricas de WER, latencia fim-a-fim, CSAT, deflection rate
- Claude Agent SDK / LangGraph — orquestracao multi-agente com gerenciamento de estado de sessao de voz
- Gateway de pagamento: Stripe / Pagarme / Iugu — consulta de transacoes e submissao de refund pelo Onda
- Google Calendar ou Aircall Scheduling — agendamento de callbacks pelo Hertz

## Entregável (prova de trabalho)

Por cada interacao de voz processada, task no ClickUp com artefatos de prova de trabalho: (1) audio original recebido (referencia de URL segura, nao o arquivo), (2) transcricao ASR completa com confianca por segmento, (3) texto normalizado pos-processamento pelo Sono, (4) intencao classificada com confianca score e worker selecionado, (5) dados coletados (com turns de dialogo do Vivo se aplicavel), (6) sistemas consultados com IDs de referencia e latencias, (7) resposta gerada pre-Critic (texto), (8) score do Critic Eco por dimensao (naturalidade/brevidade/factualidade/compliance/empatia), (9) resposta final enviada (texto + ID do audio TTS), (10) resolucao: autonomo / escalado (motivo) / callback agendado, (11) sentimento detectado pelo Radar (score por turn + nivel de risco), (12) health score pos-interacao atualizado no CRM, (13) timestamp de cada step do pipeline para calculo de latencia. Dashboard Langfuse em tempo real: deflection rate por canal (telefone vs WhatsApp), WER mensal, distribuicao de intencoes de voz, latencia percentil 95, CSAT historico, critic rejection breakdown, volume de escalonamentos por motivo.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Incident Response Squad (5 ag) — base para o Hertz de Handoff Telefonico: logica de escalonamento por criticidade, briefing estruturado para handoff, notificacao multicanal e gerenciamento de fila de resolucao urgente
- Skeptic Protocol (5 ag, red-team/QA) — base para o Critic Eco: arquitetura de validacao adversarial com rubrica multidimensional, logica de rejeicao com feedback estruturado e threshold de escalonamento
- Data Quality Guardian (5 ag, qualidade de dados) — base para o Radar de Sentimento: deteccao de anomalia em streams de dados em tempo real (aplicada a sentimento/risco em vez de dados de sistema), geracao de alertas contextuais com evidencias

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O1 · TopSquad de Atendimento & Suporte Conversacional** — Resolve, tria, escala e assiste — toda a linha de frente em um cérebro só.

- **Missão:** A linha de frente inteira: resolve o Tier-1 em texto e voz (PT-BR), tria e prioriza tickets, decide quando escalar para humano (handoff) e assiste o agente humano quando ele assume. Um único cérebro de atendimento, multicanal.
- **Por que consolidar:** Os cinco vivem na mesma conversa do cliente — só atuam em momentos diferentes (resolver, triar, escalar, assistir). Mantê-los separados quebrava o contexto a cada passagem de bastão. Unidos, a conversa flui do bot ao humano e de volta sem reiniciar, com triagem e copiloto compartilhando o mesmo estado.
- **Squads irmãos:** Suporte Conversacional Multicanal (Tier-1), Voz-IA para Atendimento Telefônico (PT-BR), Triagem, Roteamento e Priorização de Tickets, Handoff Orchestrator HITL, Copiloto do Agente Humano

## Estrutura

```
ops-cs-voz-ia-telefonia/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
