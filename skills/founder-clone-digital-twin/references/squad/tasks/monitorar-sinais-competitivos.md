---
task: vigil()
responsavel: "VIGIL"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de concorrentes e players a monitorar (configurada na fase Discovery e atualizada pelo founder), palavras-chave e temas de interesse, fontes a rastrear (sites, LinkedIn, Google Alerts, redes sociais, fontes regulatórias), threshold de urgência configurado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório Semanal de Inteligência Competitiva com: (1) Movimentos de concorrentes na semana (classificados por impacto: CRÍTICO / RELEVANTE / INFORMATIVO), (2) Sinais de mercado (tendências, novos entrantes, funding), (3) Oportunidades identificadas (janelas de mercado, fraquezas de concorrentes), (4) Alertas CRÍTICOS (entregues imediatamente ao ORION fora do ciclo semanal), (5) Recomendação de contra-jogada para sinais críticos (sintetizado com frameworks do ECHO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Monitoramento contínuo via cron job a cada 6 horas. Relatório semanal consolidado toda segunda às 7h (antes da semana começar). Alertas CRÍTICOS disparados imediatamente ao detectar sinais de thresho…"
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

# Monitorar Sinais Competitivos

**Task ID:** `vigil()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais Competitivos |
| **status** | `pending` |
| **responsible_executor** | VIGIL (VIGIL — O Monitor de Inteligência Competitiva) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de monitoramento contínuo 24/7. Rastreia sinais de concorrentes, movimentos de mercado, mudanças regulatórias, novas entradas no setor, contratações estratégicas de players relevantes, funding rounds, lançamentos de produto e menções relevantes. Categoriza por urgência e impacto, gera alertas proativos para o ORION e produz o Relatório Semanal de Inteligência. Quando detecta sinal de alta urgência (ex: concorrente lançou produto direto, mudança regulatória crítica), aciona ORION fora do ciclo regular para resposta imediata.

## Input

- Lista de concorrentes e players a monitorar (configurada na fase Discovery e atualizada pelo founder), palavras-chave e temas de interesse, fontes a rastrear (sites, LinkedIn, Google Alerts, redes sociais, fontes regulatórias), threshold de urgência configurado

## Output

- Relatório Semanal de Inteligência Competitiva com: (1) Movimentos de concorrentes na semana (classificados por impacto: CRÍTICO / RELEVANTE / INFORMATIVO), (2) Sinais de mercado (tendências, novos entrantes, funding), (3) Oportunidades identificadas (janelas de mercado, fraquezas de concorrentes), (4) Alertas CRÍTICOS (entregues imediatamente ao ORION fora do ciclo semanal), (5) Recomendação de contra-jogada para sinais críticos (sintetizado com frameworks do ECHO)

## Trigger

Monitoramento contínuo via cron job a cada 6 horas. Relatório semanal consolidado toda segunda às 7h (antes da semana começar). Alertas CRÍTICOS disparados imediatamente ao detectar sinais de threshold alto. Também acionado manualmente para análise aprofundada de player específico.

## Knowledge base (o que o executor consulta)

- EXA MCP (busca web em tempo real), Apify (scraping de sites de concorrentes, LinkedIn, G2/Capterra), feeds RSS curados, Google Alerts equivalente, base de perfis de concorrentes construída na fase Discovery, histórico de alertas anteriores para evitar ruído repetitivo, critérios de priorização e pesos definidos pelo founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de concorrentes e players a monitorar (configurada na fase Discovery e atualizada pelo founder), palavras-chave e…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório Semanal de Inteligência Competitiva com: (1) Movimentos de concorrentes na semana (classificados por impacto:…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório Semanal de Inteligência Competitiva com: (1) Movimentos de concorrentes na semana (classificados por impacto: CRÍTICO / RELEVANTE / INFORMATIVO), (2)…
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

- **to:** GATE
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
