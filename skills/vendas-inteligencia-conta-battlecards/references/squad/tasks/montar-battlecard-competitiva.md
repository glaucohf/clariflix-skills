---
task: warfare()
responsavel: "WARFARE"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Perfil da empresa (output do SCOUT), setor, stack tecnológica detectada, histórico de objeções do CRM, base de battlecards existente do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Battlecard por concorrente (máximo 3) com: tabela comparativa (5-7 dimensões chave), objeções previstas com respostas sugeridas, ângulo de ataque recomendado, casos análogos de win com este perfil de conta, red flags que indicam risco de perda"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo NEXUS apos output parcial do SCOUT (precisa da stack tecnologica detectada). Pode ser reacionado manualmente quando o vendedor informa que um concorrente especifico entrou no deal."
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

# Montar Battlecard Competitiva

**Task ID:** `warfare()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Inteligência de Conta e Battlecards

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Montar Battlecard Competitiva |
| **status** | `pending` |
| **responsible_executor** | WARFARE (WARFARE — O Especialista em Battlecards) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em inteligência competitiva. Identifica quais concorrentes estão provavelmente em avaliação pelo prospect (via sinais: stack atual, job descriptions publicadas, menções em redes, perguntas feitas em calls anteriores registradas no CRM). Para cada concorrente identificado, monta um battlecard com: diferenciais da solução do cliente, fraquezas do concorrente exploráveis, objeções típicas que o concorrente levanta e respostas prontas, casos de win/loss históricos analogos.

## Input

- Perfil da empresa (output do SCOUT), setor, stack tecnológica detectada, histórico de objeções do CRM, base de battlecards existente do cliente

## Output

- Battlecard por concorrente (máximo 3) com: tabela comparativa (5-7 dimensões chave), objeções previstas com respostas sugeridas, ângulo de ataque recomendado, casos análogos de win com este perfil de conta, red flags que indicam risco de perda

## Trigger

Disparo pelo NEXUS apos output parcial do SCOUT (precisa da stack tecnologica detectada). Pode ser reacionado manualmente quando o vendedor informa que um concorrente especifico entrou no deal.

## Knowledge base (o que o executor consulta)

- Base interna de battlecards do cliente (mantida e atualizada pelo próprio squad), histórico de win/loss no CRM com motivo, job descriptions do prospect (sinal de stack), reviews públicas em G2/Capterra dos concorrentes, materiais de posicionamento do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Perfil da empresa (output do SCOUT), setor, stack tecnológica detectada, histórico de objeções do CRM, base de battleca…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Battlecard por concorrente (máximo 3) com: tabela comparativa (5-7 dimensões chave), objeções previstas com respostas s…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Battlecard por concorrente (máximo 3) com: tabela comparativa (5-7 dimensões chave), objeções previstas com respostas sugeridas, ângulo de ataque recomendado,…
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

- **to:** ORACLE
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
