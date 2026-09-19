---
task: atlas()
responsavel: "ATLAS"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Query de pesquisa estruturada pelo ORION (o que precisa ser descoberto, ângulos a explorar, fontes prioritárias, nível de profundidade requerido"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "executivo vs detalhado), deadline da demanda original"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de pesquisa com: resumo executivo (3-5 bullets), findings detalhados por ângulo de pesquisa, todas as afirmações com fonte + URL + data, grau de confiabilidade por claim (VERIFICADO / INFERIDO / HIPÓTESE), gaps de informação identificados, recomendação de síntese para o ECHO"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo ORION quando a demanda requer dados externos (Research Mode). Também acionado proativamente para o monitoramento semanal de concorrentes (COMPETITIVE INTEL) e para pre-briefings de reuni…"
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

# Conduzir Pesquisa Multi-fonte

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Conduzir Pesquisa Multi-fonte |
| **status** | `pending` |
| **responsible_executor** | ATLAS (ATLAS — O Deep Research Worker) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de pesquisa profunda. Quando uma demanda requer dados externos, análise de mercado, benchmarks, inteligência competitiva ou qualquer informação que não está no corpus do founder, ATLAS conduz pesquisa multi-fonte em paralelo. Opera em swarm de 3-5 instâncias para cobrir ângulos simultâneos (mercado, concorrentes, regulação, tendências, dados financeiros). Todo claim gerado por ATLAS vem com citação de fonte, data e grau de confiabilidade. Alimenta o ECHO com o contexto externo necessário para que a resposta final seja sintetizada na lógica do founder — ATLAS traz os fatos, ECHO traz o frame.

## Input

- Query de pesquisa estruturada pelo ORION (o que precisa ser descoberto, ângulos a explorar, fontes prioritárias, nível de profundidade requerido
- executivo vs detalhado), deadline da demanda original

## Output

- Relatório de pesquisa com: resumo executivo (3-5 bullets), findings detalhados por ângulo de pesquisa, todas as afirmações com fonte + URL + data, grau de confiabilidade por claim (VERIFICADO / INFERIDO / HIPÓTESE), gaps de informação identificados, recomendação de síntese para o ECHO

## Trigger

Disparo pelo ORION quando a demanda requer dados externos (Research Mode). Também acionado proativamente para o monitoramento semanal de concorrentes (COMPETITIVE INTEL) e para pre-briefings de reuniões com stakeholders externos.

## Knowledge base (o que o executor consulta)

- EXA MCP (busca web em tempo real), Apify (scraping de fontes especificas), feeds RSS de setores relevantes, bases de dados publicas (relatorios setoriais, dados regulatorios), historico de pesquisas anteriores para evitar retrabalho, base de fontes confiaves curada pelo founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Query de pesquisa estruturada pelo ORION (o que precisa ser descoberto, ângulos a explorar, fontes prioritárias, nível…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de pesquisa com: resumo executivo (3-5 bullets), findings detalhados por ângulo de pesquisa, todas as afirmaç…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de pesquisa com: resumo executivo (3-5 bullets), findings detalhados por ângulo de pesquisa, todas as afirmações com fonte + URL + data, grau de conf…
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

- **to:** CHRONICLE
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
