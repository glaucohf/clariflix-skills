---
task: herald()
responsavel: "HERALD"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Tipo de comunicacao solicitada (board memo, update semanal, comunicado interno, resposta a parceiro), dados e metricas mais recentes disponíveis (via integracao com dashboards), contexto da audiencia (quem vai receber, nivel de familiaridade, expectativas), tom desejado (formal/informal, detalhado/executivo), prazo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Draft de comunicação no tom do founder com: (1) Versão completa formatada, (2) Versão TL;DR de 3-5 bullets, (3) Indicação de cada afirmação factual com fonte/dado que a embasa, (4) Sugestões de customização por perfil de audiência, (5) Checklist de revisão pré-envio para o founder"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato salvo no ClickUp e Notion"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "NENHUM envio externo sem aprovação explícita do founder (L3 HITL obrigatório)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo ORION para comunicações externas ou críticas. Cron job semanal para Board Update Draft toda sexta às 9h. Também acionado manualmente pelo founder ou assistente executivo para qualquer c…"
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

# Gerar Drafts De Board Packs

**Task ID:** `herald()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Drafts De Board Packs |
| **status** | `pending` |
| **responsible_executor** | HERALD (HERALD — O Agente de Comunicação e Board Intelligence) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado na produção de comunicações estratégicas no tom e formato do founder. Gera drafts de board packs, memos para investidores, comunicados internos críticos, respostas a parceiros estratégicos e atualizações de stakeholders. Coleta sinais de múltiplas fontes (métricas internas, notícias relevantes, updates de projetos) para montar narrativas source-grounded que o founder apenas revisa e aprova. Também é responsável por preparar pre-briefings de reuniões importantes: agenda, contexto dos participantes, objetivos, perguntas sugeridas e materiais de referência.

## Input

- Tipo de comunicacao solicitada (board memo, update semanal, comunicado interno, resposta a parceiro), dados e metricas mais recentes disponíveis (via integracao com dashboards), contexto da audiencia (quem vai receber, nivel de familiaridade, expectativas), tom desejado (formal/informal, detalhado/executivo), prazo

## Output

- Draft de comunicação no tom do founder com: (1) Versão completa formatada, (2) Versão TL;DR de 3-5 bullets, (3) Indicação de cada afirmação factual com fonte/dado que a embasa, (4) Sugestões de customização por perfil de audiência, (5) Checklist de revisão pré-envio para o founder
- Artefato salvo no ClickUp e Notion
- NENHUM envio externo sem aprovação explícita do founder (L3 HITL obrigatório)

## Trigger

Acionado pelo ORION para comunicações externas ou críticas. Cron job semanal para Board Update Draft toda sexta às 9h. Também acionado manualmente pelo founder ou assistente executivo para qualquer comunicação de alto impacto.

## Knowledge base (o que o executor consulta)

- Knowledge Graph do founder (tom de voz, estilo narrativo, posicionamento), métricas e dashboards internos (via MCP de BI/analytics), histórico de comunicações anteriores aprovadas pelo founder (corpus de board packs, memos, emails estratégicos), perfis de stakeholders chave (investidores, board, parceiros estratégicos), templates de comunicação por tipo aprovados pelo founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Tipo de comunicacao solicitada (board memo, update semanal, comunicado interno, resposta a parceiro), dados e metricas…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Draft de comunicação no tom do founder com: (1) Versão completa formatada, (2) Versão TL;DR de 3-5 bullets, (3) Indicaç…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Draft de comunicação no tom do founder com: (1) Versão completa formatada, (2) Versão TL;DR de 3-5 bullets, (3) Indicação de cada afirmação factual com fonte/d…
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

- **to:** VIGIL
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
