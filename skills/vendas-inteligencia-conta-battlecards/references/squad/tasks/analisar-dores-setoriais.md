---
task: oracle()
responsavel: "ORACLE"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Setor da empresa, cargo(s) dos interlocutores, tamanho da empresa, região geográfica"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Briefing setorial com: 3-5 pressões/dores dominantes do setor no momento, benchmarks relevantes com fontes, 8-12 perguntas de discovery recomendadas ordenadas por impacto, gatilhos de urgência que podem ser explorados no discurso, frame narrativo recomendado para a abertura da reunião"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo NEXUS em paralelo aos outros workers, baseado apenas nos dados da ficha inicial (setor + cargo). E o worker mais rápido pois opera principalmente sobre base de conhecimento pré-processad…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM de produção"
    - "[ ] L3: Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio automático sem leitura humana"
    - "[ ] L2: Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta o que não se aplica"
    - "[ ] L1: Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão parcial ou aguardar correção"
    - "[ ] L1: Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes de qualquer ação"
---

# Analisar Dores Setoriais

**Task ID:** `oracle()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Inteligência de Conta e Battlecards

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Dores Setoriais |
| **status** | `pending` |
| **responsible_executor** | ORACLE (ORACLE — O Analista de Sêtor e Dores) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em contexto macro e micro-setorial. Dado o setor e o cargo do interlocutor, sintetiza: pressões regulatórias atuais, benchmarks de KPIs do setor (ex: taxa de conversão média de uma imobiliária, CAC médio de uma agência), dores típicas do cargo (ex: o que tira o sono de um Head de Vendas de agência digital em 2026), tendências recentes que afetam o negócio e oportunidade de conectar a solução do cliente a essas dores. Gera perguntas de discovery altamente contextualizadas.

## Input

- Setor da empresa, cargo(s) dos interlocutores, tamanho da empresa, região geográfica

## Output

- Briefing setorial com: 3-5 pressões/dores dominantes do setor no momento, benchmarks relevantes com fontes, 8-12 perguntas de discovery recomendadas ordenadas por impacto, gatilhos de urgência que podem ser explorados no discurso, frame narrativo recomendado para a abertura da reunião

## Trigger

Disparo pelo NEXUS em paralelo aos outros workers, baseado apenas nos dados da ficha inicial (setor + cargo). E o worker mais rápido pois opera principalmente sobre base de conhecimento pré-processada.

## Knowledge base (o que o executor consulta)

- Base de conhecimento setorial pré-processada (atualizada mensalmente): relatórios de setor, benchmarks publicados, frameworks de dor por cargo (VP Sales, CMO, CEO PME, etc.), histórico de perguntas de discovery que geraram avanço de deal no CRM do cliente, notícias e tendências dos últimos 90 dias por vertical

## Action Items

1. Confirmar o gatilho e carregar a entrada (Setor da empresa, cargo(s) dos interlocutores, tamanho da empresa, região geográfica).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Briefing setorial com: 3-5 pressões/dores dominantes do setor no momento, benchmarks relevantes com fontes, 8-12 pergun…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Briefing setorial com: 3-5 pressões/dores dominantes do setor no momento, benchmarks relevantes com fontes, 8-12 perguntas de discovery recomendadas ordenadas…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SENTINEL registrado
- [ ] Gate L3 respeitado: Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistênci…
- [ ] Gate L3 respeitado: Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do…
- [ ] Gate L2 respeitado: Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio a… | BLOQUEIA até decisão humana |
| VETO-003 | L2 — Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta… | BLOQUEIA até decisão humana |
| VETO-004 | L1 — Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão p… | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** HERALD
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
