---
task: marco()
responsavel: "Marco"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Briefing de Contexto aprovado pelo cliente + lista de concorrentes + verticais de mercado alvo + perguntas de pesquisa priorizadas pelo Orion"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de Deep Research (30-50 páginas): TAM/SAM/SOM estimado, mapa competitivo (pricing, copy, diferenciais, pontos fracos), top-10 insights de mercado rankeados por impacto, fontes primárias e secundárias citadas, PMF Score draft (1-10) com justificativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Orion após aprovação do Briefing de Contexto (fase Discovery). Re-ativado quando Brutus retorna claims contestados para revisão."
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

# Pesquisar Tendencias Industriais

**Task ID:** `marco()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** PMF & Market Deep Research Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Pesquisar Tendencias Industriais |
| **status** | `pending` |
| **responsible_executor** | Marco (Marco — Research Lead) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de deep research responsável por pesquisa de mercado (TAM/SAM/SOM), tendências de indústria, benchmarking de concorrentes e síntese de evidências qualitativas e quantitativas. Usa web search em múltiplas fontes (G2, Capterra, LinkedIn, Reddit, relatórios de mercado, SEMrush, SimilarWeb) e consolida em relatório estruturado com fontes citadas.

## Input

- Briefing de Contexto aprovado pelo cliente + lista de concorrentes + verticais de mercado alvo + perguntas de pesquisa priorizadas pelo Orion

## Output

- Relatório de Deep Research (30-50 páginas): TAM/SAM/SOM estimado, mapa competitivo (pricing, copy, diferenciais, pontos fracos), top-10 insights de mercado rankeados por impacto, fontes primárias e secundárias citadas, PMF Score draft (1-10) com justificativa

## Trigger

Ativado pelo Orion após aprovação do Briefing de Contexto (fase Discovery). Re-ativado quando Brutus retorna claims contestados para revisão.

## Knowledge base (o que o executor consulta)

- Relatórios de mercado (Gartner, G2, CB Insights se públicos), dados de SEMrush/SimilarWeb da empresa e concorrentes, reviews de produto em G2/Capterra/Trustpilot, threads relevantes do Reddit/LinkedIn, histórico de pesquisas anteriores do cliente, benchmark de CPAs do setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Briefing de Contexto aprovado pelo cliente + lista de concorrentes + verticais de mercado alvo + perguntas de pesquisa…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de Deep Research (30-50 páginas): TAM/SAM/SOM estimado, mapa competitivo (pricing, copy, diferenciais, pontos…) e persistir no artefato do squad.
4. Entregar ao critic Brutus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de Deep Research (30-50 páginas): TAM/SAM/SOM estimado, mapa competitivo (pricing, copy, diferenciais, pontos fracos), top-10 insights de mercado ran…
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

- **to:** Iris
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
