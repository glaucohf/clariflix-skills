---
task: radar()
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stream de turns transcritos em tempo real durante a sessao + historico de interacoes dos ultimos 30 dias do cliente + health score atual no CRM + tier e MRR do cliente + numero de tickets abertos recentemente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score de sentimento por turn (positivo/neutro/negativo/toxico) + nivel de risco em tempo real (verde/amarelo/vermelho/critico)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Em caso de threshold atingido: sinal de alerta injetado no Maestro com recomendacao (usar tom empatico / oferecer compensacao / escalar HITL)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Apos interacao: health score atualizado no CRM, brief de churn risk no Slack se score < 60, task no ClickUp com evidencias de risco detectadas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativo em toda sessao de voz em paralelo com Maestro/workers (nao bloqueia o fluxo principal). Dispara alerta ativo quando: sentimento cai para 'negativo' em 2 turns consecutivos; keyword de risco leg…"
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

# Analisar Sentimento E Risco

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Sentimento E Risco |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Agente de Sentimento & Risco em Tempo Real) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analisa sentimento e risco em tempo real durante a chamada/audio — nao aguarda o fim da interacao. Processa cada turn transcrito pelo Sono buscando: sinais de escalada emocional (frustacao crescente, tom agressivo, choro), mencao de termos de risco legal ('PROCON', 'Reclame Aqui', 'advogado', 'processo', 'denunciar'), indicadores de churn iminente ('cancela tudo', 'nao quero mais', 'vou embora', 'prefiro o concorrente'), e padrao de problema recorrente (mesmo problema pela 3a vez). Quando detecta threshold de risco, injeta sinal de alerta no pipeline do Maestro para priorizar resolucao empatica ou escalar para humano antes que o cliente desista. Apos a interacao, atualiza o health score no CRM e envia brief para o time de CS no Slack se risco de churn elevado.

## Input

- Stream de turns transcritos em tempo real durante a sessao + historico de interacoes dos ultimos 30 dias do cliente + health score atual no CRM + tier e MRR do cliente + numero de tickets abertos recentemente

## Output

- Score de sentimento por turn (positivo/neutro/negativo/toxico) + nivel de risco em tempo real (verde/amarelo/vermelho/critico)
- Em caso de threshold atingido: sinal de alerta injetado no Maestro com recomendacao (usar tom empatico / oferecer compensacao / escalar HITL)
- Apos interacao: health score atualizado no CRM, brief de churn risk no Slack se score < 60, task no ClickUp com evidencias de risco detectadas

## Trigger

Ativo em toda sessao de voz em paralelo com Maestro/workers (nao bloqueia o fluxo principal). Dispara alerta ativo quando: sentimento cai para 'negativo' em 2 turns consecutivos; keyword de risco legal detectada; cliente menciona concorrente ou cancelamento; terceira interacao na mesma semana sem resolucao confirmada; tom de voz (volume/velocidade) indica frustacao crescente via analise prosodica

## Knowledge base (o que o executor consulta)

- Modelo de analise de sentimento fine-tuned para PT-BR coloquial de atendimento (incluindo girias, ironias, eufemismos de reclamacao brasileiros)
- Lista de keywords de risco por categoria (juridico, PROCON, churn, concorrente) atualizada pelo time de CS
- Modelo de health score (features: frequencia de tickets, sentimento acumulado, uso do produto, MRR, tempo ate renovacao)
- Playbooks de retencao por perfil e motivo de risco
- Benchmarks de health score por segmento de cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stream de turns transcritos em tempo real durante a sessao + historico de interacoes dos ultimos 30 dias do cliente + h…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score de sentimento por turn (positivo/neutro/negativo/toxico) + nivel de risco em tempo real (verde/amarelo/vermelho/c…) e persistir no artefato do squad.
4. Entregar ao critic Eco 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score de sentimento por turn (positivo/neutro/negativo/toxico) + nivel de risco em tempo real (verde/amarelo/vermelho/critico)
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

- **to:** Eco
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
