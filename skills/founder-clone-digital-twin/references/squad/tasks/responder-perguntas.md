---
task: echo()
responsavel: "ECHO"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pergunta ou demanda estruturada pelo ORION, contexto da situação (quem pergunta, canal, urgência, histórico relevante), segmento do Knowledge Graph mais relevante para a query, nível de confiança calculado pelo ORION"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta estruturada no tôm e lógica do founder com: (1) Resposta direta (ação ou diretriz recomendada), (2) Raciocínio subjacente (qual framework ou princípio guiou a resposta), (3) Precedentes análogos do corpus (decisões passadas similares), (4) Grau de confiança (ALTO / MÉDIO / BAIXO) e indicação de gaps se houver, (5) Flag de escalação se a resposta exigir julgamento original"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo ORION quando confiança do corpus para a query e >= 70%. Também acionado diretamente para drafts de comunicação interna, onboarding de novos colaboradores, respostas a perguntas culturais…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio – o squad nunca envia comunicação externa autonomamente"
    - "[ ] L3: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política interna – founder aprova com opções claras antes da execução"
    - "[ ] L3: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao de pensamento antes de ser persistida no corpus canônico"
    - "[ ] L2: ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma aproximação e pode escalonar"
    - "[ ] L2: STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer caminho seja comunicado como recomendacao oficial do squad"
---

# Responder Perguntas

**Task ID:** `echo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Responder Perguntas |
| **status** | `pending` |
| **responsible_executor** | ECHO (ECHO — O Clone Cognitivo do Founder) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker principal e alma do squad. Encarna o conhecimento tacito, frameworks mentais, criterios de decisao e tom de voz do founder. Quando acionado pelo ORION com alta confianca de corpus, responde perguntas, orienta decisoes, redige comunicacoes e produz analises como se fosse o proprio founder. Opera exclusivamente sobre o Knowledge Graph construido e validado — nunca inventa, nunca extrapola para fora do corpus sem sinalizacao explicita. Em cada resposta, cita qual parte do corpus embasou o raciocinio (framework X, decisao analoga Y, principio Z) para transparencia e auditabilidade. Tambem detecta quando uma pergunta esta fora do corpus e sinaliza ao ORION para escalonar ao Research Mode ou Escalation Mode.

## Input

- Pergunta ou demanda estruturada pelo ORION, contexto da situação (quem pergunta, canal, urgência, histórico relevante), segmento do Knowledge Graph mais relevante para a query, nível de confiança calculado pelo ORION

## Output

- Resposta estruturada no tôm e lógica do founder com: (1) Resposta direta (ação ou diretriz recomendada), (2) Raciocínio subjacente (qual framework ou princípio guiou a resposta), (3) Precedentes análogos do corpus (decisões passadas similares), (4) Grau de confiança (ALTO / MÉDIO / BAIXO) e indicação de gaps se houver, (5) Flag de escalação se a resposta exigir julgamento original

## Trigger

Disparo pelo ORION quando confiança do corpus para a query e >= 70%. Também acionado diretamente para drafts de comunicação interna, onboarding de novos colaboradores, respostas a perguntas culturais e estratégicas recorrentes.

## Knowledge base (o que o executor consulta)

- Knowledge Graph do founder (grafo estruturado com entidades, frameworks, decisões, princípios, exemplos canônicos e vocabulário específico), corpus de comunicações históricas (emails, Slack, documentos estratégicos), gravações transcritas de reuniões e palestras, manual de cultura e posicionamento da empresa, histórico de decisões documentadas com contexto e outcome, base vetorial (Supabase pgvector) para recuperação semântica de precedentes análogos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pergunta ou demanda estruturada pelo ORION, contexto da situação (quem pergunta, canal, urgência, histórico relevante),…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resposta estruturada no tôm e lógica do founder com: (1) Resposta direta (ação ou diretriz recomendada), (2) Raciocínio…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta estruturada no tôm e lógica do founder com: (1) Resposta direta (ação ou diretriz recomendada), (2) Raciocínio subjacente (qual framework ou princípio…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SENTINEL registrado
- [ ] Gate L3 respeitado: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder ante…
- [ ] Gate L3 respeitado: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou…
- [ ] Gate L3 respeitado: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuin…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma apr… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — VIGIL ao detectar sinal competitivo CRÍTICO fora do ciclo semanal: notificação imediata ao founder com proposta de contra-jogada — founder decide se ativa resp… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — CHRONICLE ao identificar gap crítico no corpus que impacta a confiabilidade do ECHO em categoria de alto volume: agenda sessão de captura de conhecimento com o… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** ATLAS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
