---
task: sono()
responsavel: "Sono"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stream de audio de chamada (PCM 16kHz via Aircall webhook) OU arquivo de audio do WhatsApp Business API (OGG Opus, max 16MB) + ID do cliente + canal de origem (telefone/whatsapp) + idioma/sotaque hint se disponivel"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Texto transcrito normalizado com: (1) transcricao raw completa, (2) texto normalizado sem disfluencias, (3) entidades extraidas (CPF, pedido, telefone, nome), (4) confianca media ASR, (5) segmentos de baixa confianca marcados para confirmacao"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Na direcao inversa: arquivo de audio TTS sintetizado (MP3/OGG) para envio ao canal"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Log de qualidade no Langfuse: WER estimado, latencia ASR, latencia TTS"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook Aircall detecta chamada entrante no numero configurado; Webhook WhatsApp Business API detecta mensagem do tipo 'audio' ou 'voice' no numero da conta; Fim de turn do cliente na chamada (detecc…"
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

# Transcrever E Normalizar Audio

**Task ID:** `sono()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Transcrever E Normalizar Audio |
| **status** | `pending` |
| **responsible_executor** | Sono (Sono — Agente ASR/TTS PT-BR) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em processamento de audio PT-BR de baixa latencia. Recebe stream de audio de chamada telefonica (via webhook Aircall) ou arquivo de voice note do WhatsApp (OGG/MP3/WAV/OPUS), executa transcricao ASR com vocabulario de dominio customizado (SKUs, nomes de produto, termos internos), normaliza o texto transcrito (remove disfluencias como 'ahn', 'eh', 'tipo assim', adiciona pontuacao, identifica entidades: CPF, numero de pedido, telefone via NER), e retorna texto estruturado para o Maestro. Na saida, recebe texto de resposta do Critic e sintetiza em audio TTS PT-BR (voz com persona da marca, velocidade e tom calibrados por canal: mais formal no telefone, mais casual no WhatsApp). Monitora qualidade de transcricao frame-a-frame: se confianca ASR < 0.78 em trecho critico (dado solicitado), dispara turn de confirmacao antes de prosseguir.

## Input

- Stream de audio de chamada (PCM 16kHz via Aircall webhook) OU arquivo de audio do WhatsApp Business API (OGG Opus, max 16MB) + ID do cliente + canal de origem (telefone/whatsapp) + idioma/sotaque hint se disponivel

## Output

- Texto transcrito normalizado com: (1) transcricao raw completa, (2) texto normalizado sem disfluencias, (3) entidades extraidas (CPF, pedido, telefone, nome), (4) confianca media ASR, (5) segmentos de baixa confianca marcados para confirmacao
- Na direcao inversa: arquivo de audio TTS sintetizado (MP3/OGG) para envio ao canal
- Log de qualidade no Langfuse: WER estimado, latencia ASR, latencia TTS

## Trigger

Webhook Aircall detecta chamada entrante no numero configurado; Webhook WhatsApp Business API detecta mensagem do tipo 'audio' ou 'voice' no numero da conta; Fim de turn do cliente na chamada (deteccao de silencio > 800ms ou end-of-utterance signal do Aircall)

## Knowledge base (o que o executor consulta)

- Modelo ASR Deepgram Nova-2 PT-BR com vocabulario customizado (lista de SKUs, nomes de produto, termos tecnicos da empresa)
- Whisper Large-v3 como fallback
- Dicionario de normalizacao PT-BR (disfluencias, abreviacoes de WhatsApp, grafias informais)
- Modelo NER para CPF/CNPJ, numeros de pedido, datas, valores monetarios em PT-BR
- Banco de vozes TTS calibradas por canal (ElevenLabs PT-BR ou Azure Neural TTS)
- Parametros de qualidade por canal (threshold de confianca, velocidade de sintese, tom)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stream de audio de chamada (PCM 16kHz via Aircall webhook) OU arquivo de audio do WhatsApp Business API (OGG Opus, max…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Texto transcrito normalizado com: (1) transcricao raw completa, (2) texto normalizado sem disfluencias, (3) entidades e…) e persistir no artefato do squad.
4. Entregar ao critic Eco 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Texto transcrito normalizado com: (1) transcricao raw completa, (2) texto normalizado sem disfluencias, (3) entidades extraidas (CPF, pedido, telefone, nome),…
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

- **to:** Vivo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
