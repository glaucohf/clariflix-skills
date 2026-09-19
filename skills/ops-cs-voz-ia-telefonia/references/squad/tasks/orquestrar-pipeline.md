---
task: maestroPipeline()
responsavel: "Maestro"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Por cada interacao de voz processada, task no ClickUp com artefatos de prova de trabalho: (1) audio original recebido (referencia de URL segura, nao o arquivo), (2) transcricao ASR completa com confianca por segmento, (3) texto normalizado pos-processamento pelo Sono, (4) intencao classificada com confianca score e worker selecionado, (5) dados coletados (com turns de dialogo do Vivo se aplicavel), (6) sistemas consultados com IDs de referencia e latencias, (7) resposta gerada pre-Critic (texto), (8) score do Critic Eco por dimensao (naturalidade/brevidade/factualidade/compliance/empatia), (9) resposta final enviada (texto + ID do audio TTS), (10) resolucao: autonomo / escalado (motivo) / callback agendado, (11) sentimento detectado pelo Radar (score por turn + nivel de risco), (12) health score pos-interacao atualizado no CRM, (13) timestamp de cada step do pipeline para calculo de latencia"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Dashboard Langfuse em tempo real: deflection rate por canal (telefone vs WhatsApp), WER mensal, distribuicao de intencoes de voz, latencia percentil 95, CSAT historico, critic rejection breakdown, volume de escalonamentos por motivo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe o texto transcrito e normalizado do Agente Sono (ASR), enriquece com o contexto completo do cliente (historico de pedidos, tier, sentimento acumulado, ultima interacao), classifica a intencao…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Eco 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket prioritario antes de executar"
    - "[ ] HITL: Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona para humano"
    - "[ ] HITL: Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente para supervisor"
    - "[ ] HITL: Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana"
    - "[ ] HITL: Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especialista"
---

# Orquestrar Pipeline do Voz-IA para Atendimento Telefônico

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Voz-IA para Atendimento Telefônico |
| **status** | `pending` |
| **responsible_executor** | Maestro (Maestro — Orchestrator de Voz & Intencao) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o texto transcrito e normalizado do Agente Sono (ASR), enriquece com o contexto completo do cliente (historico de pedidos, tier, sentimento acumulado, ultima interacao), classifica a intencao da chamada/audio com confianca score usando o classificador fine-tuned com exemplos reais de voz PT-BR, decide se ha dados suficientes para roteamento ou se precisa de uma turn de coleta adicional, roteia para o worker especializado correto, aguarda o output do worker, aciona o Critic Eco para validacao antes da sintese TTS, registra a prova de trabalho no ClickUp com todos os artefatos e decide escalonamento HITL quando: confianca < 0.75, acao irreversivel acima de limite, ou sentimento muito negativo detectado.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Por cada interacao de voz processada, task no ClickUp com artefatos de prova de trabalho: (1) audio original recebido (referencia de URL segura, nao o arquivo), (2) transcricao ASR completa com confianca por segmento, (3) texto normalizado pos-processamento pelo Sono, (4) intencao classificada com confianca score e worker selecionado, (5) dados coletados (com turns de dialogo do Vivo se aplicavel), (6) sistemas consultados com IDs de referencia e latencias, (7) resposta gerada pre-Critic (texto), (8) score do Critic Eco por dimensao (naturalidade/brevidade/factualidade/compliance/empatia), (9) resposta final enviada (texto + ID do audio TTS), (10) resolucao: autonomo / escalado (motivo) / callback agendado, (11) sentimento detectado pelo Radar (score por turn + nivel de risco), (12) health score pos-interacao atualizado no CRM, (13) timestamp de cada step do pipeline para calculo de latencia
- Dashboard Langfuse em tempo real: deflection rate por canal (telefone vs WhatsApp), WER mensal, distribuicao de intencoes de voz, latencia percentil 95, CSAT historico, critic rejection breakdown, volume de escalonamentos por motivo

## Trigger

Recebe o texto transcrito e normalizado do Agente Sono (ASR), enriquece com o contexto completo do cliente (historico de pedidos, tier, sentimento acumulado, ultima interacao), classifica a intencao da chamada/audio com confianca score usando o classificador fine-tuned com exemplos reais de voz PT-BR, decide se ha dados suficientes para roteamento ou se precisa de uma turn de coleta adicional, roteia para o worker especializado correto, aguarda o output do worker, aciona o Critic Eco para validacao antes da sintese TTS, registra a prova de trabalho no ClickUp com todos os artefatos e decide escalonamento HITL quando: confianca < 0.75, acao irreversivel acima de limite, ou sentimento muito negativo detectado.

## Knowledge base (o que o executor consulta)

- plataforma de telefonia principal: webhook de chamada entrante, transferencia quente, callback scheduling, disponibilidade de filas em tempo real
- WhatsApp Business API
- canal #1 no Brasil: webhook de mensagens de audio (OGG Opus), envio de audio TTS sintetizado, status de entrega de mensagem
- Deepgram Nova-2 PT-BR
- ASR principal com vocabulario de dominio customizado (latencia < 300ms para streaming)
- OpenAI Whisper Large-v3
- ASR fallback para audios longos ou de qualidade muito baixa
- ElevenLabs PT-BR ou Azure Neural TTS
- sintese de voz com persona da marca (latencia < 400ms)
- ClickUp (Brain2 / MCP server)
- hub de tasks e prova de trabalho por interacao de voz, espelhando AIOX
- CRM: HubSpot ou Salesforce
- dados de conta, tier, MRR, historico de interacoes, health score
- ERP / OMS
- consulta de pedidos, status, estoque (API REST ou MCP customizado, SLA < 1.5s)
- Zendesk / Intercom
- criacao de tickets de escalonamento com transcricao e contexto, KB para RAG
- notificacoes de escalonamento urgente, alertas de churn do Radar, briefings para CSMs
- Supabase / Postgres
- estado de sessao dos agentes, health scores, logs de transcricoes, fila de handoffs, consentimentos LGPD
- observabilidade OTEL: tracing de cada step do pipeline de voz (audio -> ASR -> NER -> classificacao -> worker -> critic -> TTS), metricas de WER, latencia fim-a-fim, CSAT, deflection rate
- Claude Agent SDK / LangGraph
- orquestracao multi-agente com gerenciamento de estado de sessao de voz
- Gateway de pagamento: Stripe / Pagarme / Iugu
- consulta de transacoes e submissao de refund pelo Onda
- Google Calendar ou Aircall Scheduling
- agendamento de callbacks pelo Hertz

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Eco 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Por cada interacao de voz processada, task no ClickUp com artefatos de prova de trabalho: (1) audio original recebido (referencia de URL segura, nao o arquivo)…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Eco 2 registrado
- [ ] Gate HITL respeitado: Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3…
- [ ] Gate HITL respeitado: Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa fa…
- [ ] Gate HITL respeitado: Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz tra…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especiali… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Cliente VIP, Enterprise ou MRR > R$5k: toda acao irreversivel (cancelamento, mudanca de plano, refund parcial) requer aprovacao do CSM responsavel antes da exe… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Audio com duracao > 3 minutos e confianca media ASR < 0.82 — transcricao marcada para revisao humana antes do processamento completo pelo Maestro | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Intencao nao reconhecida apos 2 turns de coleta pelo Vivo (confianca < 0.55) — Hertz escalona com transcricao completa para o humano interpretar e resolver | BLOQUEIA até decisão humana |
| VETO-009 | HITL — Solicitacao de dados de terceiros, portabilidade de dados, ou qualquer direito LGPD em voz — Hertz bloqueia automacao e direciona para DPO/time juridico | BLOQUEIA até decisão humana |
| VETO-010 | Saída sem veredito do critic Eco 2 | BLOQUEIA entrega |

## Handoff

- **to:** Sono
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
