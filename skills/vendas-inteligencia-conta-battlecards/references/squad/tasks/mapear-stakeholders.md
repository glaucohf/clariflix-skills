---
task: iris()
responsavel: "IRIS"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Nome(s) e cargo(s) dos stakeholders, nome da empresa, domínio do email, URL do LinkedIn quando disponível"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Perfil por stakeholder com: resumo executivo (3-5 linhas), dores previstas pelo cargo, ganchos de abertura baseados em conteudo recente, estilo de abordagem recomendado (data-driven / relacional / tecnico), mapa de poder da conta (diagrama textual: decisor / influenciador / usuario / bloqueador)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo NEXUS em paralelo ao SCOUT, após receber lista de participantes da reunião (extraída do convite de calendário via MCP de calendário ou inserida manualmente)."
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

# Mapear Stakeholders

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Inteligência de Conta e Battlecards

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Mapear Stakeholders |
| **status** | `pending` |
| **responsible_executor** | IRIS (IRÍS — A Mapeadora de Stakeholders) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em inteligencia de pessoas. Para cada participante confirmado na reuniao (e potenciais decisores nao convidados), constroi um mini-perfil: trajetoria profissional, mandato atual, posts e artigos publicados recentemente, interesses declarados, estilo de comunicacao inferido, conexoes em comum, historico com a empresa do vendedor (se houver). Identifica o mapa de poder informal: quem decide, quem influencia, quem bloqueia.

## Input

- Nome(s) e cargo(s) dos stakeholders, nome da empresa, domínio do email, URL do LinkedIn quando disponível

## Output

- Perfil por stakeholder com: resumo executivo (3-5 linhas), dores previstas pelo cargo, ganchos de abertura baseados em conteudo recente, estilo de abordagem recomendado (data-driven / relacional / tecnico), mapa de poder da conta (diagrama textual: decisor / influenciador / usuario / bloqueador)

## Trigger

Disparo pelo NEXUS em paralelo ao SCOUT, após receber lista de participantes da reunião (extraída do convite de calendário via MCP de calendário ou inserida manualmente).

## Knowledge base (o que o executor consulta)

- LinkedIn Prospect API ou scraping autorizado via Clay/Apollo, histórico de interações no CRM (emails, calls anteriores), base de personas por cargo construída pelo cliente nos encontros de diagnóstico, posts públicos do LinkedIn dos stakeholders

## Action Items

1. Confirmar o gatilho e carregar a entrada (Nome(s) e cargo(s) dos stakeholders, nome da empresa, domínio do email, URL do LinkedIn quando disponível).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Perfil por stakeholder com: resumo executivo (3-5 linhas), dores previstas pelo cargo, ganchos de abertura baseados em…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Perfil por stakeholder com: resumo executivo (3-5 linhas), dores previstas pelo cargo, ganchos de abertura baseados em conteudo recente, estilo de abordagem re…
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

- **to:** WARFARE
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
