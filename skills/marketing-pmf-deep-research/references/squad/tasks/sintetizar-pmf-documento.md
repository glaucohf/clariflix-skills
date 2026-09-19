---
task: vega()
responsavel: "Vega"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Todos os outputs aprovados por Brutus: Relatório de Deep Research, ICP Master Profile, Signal Report, Persona Cards, Competitive Matrix, Angle Validation Matrix"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "PMF Score final auditado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "PMF Framework Document (PDF/Notion, 10-15 páginas executivas): executive summary (1 página para o board), PMF Score final (1-10) com breakdown por dimensão, top-3 ângulos de posicionamento rankeados com justificativa, mensagens-chave por persona (linguagem real extraída de sinais), roadmap de validação (próximos 30 dias: o que testar, como medir, critério de sucesso)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Angle Test Kit: 3-5 headlines/hooks prontos para A/B test por canal (Meta, Google, LinkedIn, email)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Backlog de pesquisa para próximos ciclos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Orion somente após Brutus aprovar todos os artefatos principais (ou Orion+HITL decidirem aceitar ressalvas). E o último agente a executar antes da entrega ao cliente."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Brutus 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias de pesquisa na direção errada"
    - "[ ] HITL: Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx simular entrevistas"
    - "[ ] HITL: Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva documentada"
    - "[ ] HITL: Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução (Copywriter, Media Buying) — gate L3 porque decisões de mídia são financeiramente irreversíveis"
    - "[ ] HITL: Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser incluído no documento final"
---

# Sintetizar PMF Documento

**Task ID:** `vega()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** PMF & Market Deep Research Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar PMF Documento |
| **status** | `pending` |
| **responsible_executor** | Vega (Vega — PMF Synthesizer & Storyteller) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de síntese final responsável por transformar todos os outputs validados em um PMF Framework Document narrativo e acionável. Converte dados brutos em story de posicionamento clara, escreve o executive summary para o board, prioriza hipóteses por impacto x facilidade e entrega o Angle Test Kit com variantes de copy prontas para A/B test.

## Input

- Todos os outputs aprovados por Brutus: Relatório de Deep Research, ICP Master Profile, Signal Report, Persona Cards, Competitive Matrix, Angle Validation Matrix
- PMF Score final auditado

## Output

- PMF Framework Document (PDF/Notion, 10-15 páginas executivas): executive summary (1 página para o board), PMF Score final (1-10) com breakdown por dimensão, top-3 ângulos de posicionamento rankeados com justificativa, mensagens-chave por persona (linguagem real extraída de sinais), roadmap de validação (próximos 30 dias: o que testar, como medir, critério de sucesso)
- Angle Test Kit: 3-5 headlines/hooks prontos para A/B test por canal (Meta, Google, LinkedIn, email)
- Backlog de pesquisa para próximos ciclos

## Trigger

Ativado pelo Orion somente após Brutus aprovar todos os artefatos principais (ou Orion+HITL decidirem aceitar ressalvas). E o último agente a executar antes da entrega ao cliente.

## Knowledge base (o que o executor consulta)

- Templates de PMF Framework da consultoria Lendar[IA], frameworks de posicionamento (April Dunford Obviously Awesome, StoryBrand), base de ângulos de copy que converteram em campanhas anteriores, guia de brand voice do cliente, critérios de PMF score do board (referências Alan Deepresearch)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Todos os outputs aprovados por Brutus: Relatório de Deep Research, ICP Master Profile, Signal Report, Persona Cards, Co…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (PMF Framework Document (PDF/Notion, 10-15 páginas executivas): executive summary (1 página para o board), PMF Score fin…) e persistir no artefato do squad.
4. Entregar ao critic Brutus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: PMF Framework Document (PDF/Notion, 10-15 páginas executivas): executive summary (1 página para o board), PMF Score final (1-10) com breakdown por dimensão, to…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Brutus 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começ…
- [ ] Gate HITL respeitado: Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a re…
- [ ] Gate HITL respeitado: Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva docume… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser i… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Brutus 2 | BLOQUEIA entrega |

## Handoff

- **to:** Brutus 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
