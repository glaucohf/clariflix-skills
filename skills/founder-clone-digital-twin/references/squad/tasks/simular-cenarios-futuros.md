---
task: strategos()
responsavel: "STRATEGOS"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Decisão ou cenário estratégico a ser avaliado, contexto de negócio atual (métricas, posição competitiva), constraints declarados pelo founder, outputs relevantes do ATLAS (dados de mercado) e do ECHO (frameworks do founder), horizonte de tempo para a análise"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Análise de cenários com: (1) Árvore de decisão com 3-5 caminhos principais e probabilidades estimadas, (2) Para cada caminho: upside, downside, riscos não óbvios e triggers de mudança de curso, (3) Simulação de reação de concorrentes chave por caminho, (4) Recomendação de caminho preferido com justificativa nos frameworks do founder, (5) Sinais de alerta a monitorar (early warning indicators), (6) Próximos 3 passos concretos recomendados"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo ORION para decisões classificadas como ALTA COMPLEXIDADE + ALTA IRREVERSIBILIDADE. Também disparado manualmente pelo founder ou por membro de confiança do time para análise estratégica…"
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

# Simular Cenarios Futuros

**Task ID:** `strategos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Simular Cenarios Futuros |
| **status** | `pending` |
| **responsible_executor** | STRATEGOS (STRATEGOS — O Agente de Cenários e Wargaming) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de inteligência estratégica avançada. Quando o founder ou o ORION precisam avaliar uma decisão de alto impacto, STRATEGOS simula cenários futuros, adversários autônomos e consequências de segunda e terceira ordem. Usa os frameworks mentais do founder (via ECHO) combinados com dados externos (via ATLAS) para construir árvores de decisão, identificar riscos não óbvios, mapear jogadas competitivas e gerar recomendações estratégicas com probabilidades estimadas. Especialista em perguntas do tipo 'e se' e 'o que o concorrente X faria se fizéssemos Y'.

## Input

- Decisão ou cenário estratégico a ser avaliado, contexto de negócio atual (métricas, posição competitiva), constraints declarados pelo founder, outputs relevantes do ATLAS (dados de mercado) e do ECHO (frameworks do founder), horizonte de tempo para a análise

## Output

- Análise de cenários com: (1) Árvore de decisão com 3-5 caminhos principais e probabilidades estimadas, (2) Para cada caminho: upside, downside, riscos não óbvios e triggers de mudança de curso, (3) Simulação de reação de concorrentes chave por caminho, (4) Recomendação de caminho preferido com justificativa nos frameworks do founder, (5) Sinais de alerta a monitorar (early warning indicators), (6) Próximos 3 passos concretos recomendados

## Trigger

Acionado pelo ORION para decisões classificadas como ALTA COMPLEXIDADE + ALTA IRREVERSIBILIDADE. Também disparado manualmente pelo founder ou por membro de confiança do time para análise estratégica proativa. Frequência típica: 1-3 vezes por semana em empresas em fase de crescimento acelerado.

## Knowledge base (o que o executor consulta)

- Frameworks de decisão do founder (via ECHO / Knowledge Graph), dados de mercado e competitivos recentes (via ATLAS), histórico de decisões estratégicas anteriores e seus outcomes (Knowledge Graph), modelos de wargaming competitivo (Porter, OODA Loop, Red Team thinking), dados internos de performance (via Analytics/SQL Agent quando integrado ao BI)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Decisão ou cenário estratégico a ser avaliado, contexto de negócio atual (métricas, posição competitiva), constraints d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Análise de cenários com: (1) Árvore de decisão com 3-5 caminhos principais e probabilidades estimadas, (2) Para cada ca…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Análise de cenários com: (1) Árvore de decisão com 3-5 caminhos principais e probabilidades estimadas, (2) Para cada caminho: upside, downside, riscos não óbvi…
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

- **to:** HERALD
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
