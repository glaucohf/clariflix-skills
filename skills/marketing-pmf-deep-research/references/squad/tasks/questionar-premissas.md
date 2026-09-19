---
task: brutus()
responsavel: "Brutus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Todos os outputs intermediários: Relatório de Marco, ICP Profile de Iris, Signal Report de Vesper, Persona Cards de Nyx, Competitive Matrix de Atlas"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Recebe também o PMF Score draft para auditoria"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Critique Report por artefato: lista de claims contestados (com grau de confianca: Alto/Medio/Baixo), gaps de evidencia identificados, sugestoes de pesquisa adicional, vieses detectados, endorsements (o que esta solido)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "PMF Score Audit: ajuste justificado do score com base em inconsistencias encontradas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Red-Team Summary para o Orion decidir o que retrabalhar vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "aceitar com ressalva"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Orion automaticamente após cada agente entregar output principal. Executa em série (não paralelo) para ter visão completa. HITL ativado se Brutus reprovar mais de 30% dos claims de qualq…"
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

# Questionar Premissas

**Task ID:** `brutus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** PMF & Market Deep Research Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Questionar Premissas |
| **status** | `pending` |
| **responsible_executor** | Brutus (Brutus — Research Crític & Réd-Team) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agênte crític/verifier que contesta sistematicamente todos os outputs do squad antes da síntese final. Aplica red-team epistêmico: busca contra-evidências, questiona premissas, identifica vieses de confirmação, valida fontes e detecta claims sem evidência suficiente. Garante que o PMF Framework Document seja defensável perante stakeholders exigentes.

## Input

- Todos os outputs intermediários: Relatório de Marco, ICP Profile de Iris, Signal Report de Vesper, Persona Cards de Nyx, Competitive Matrix de Atlas
- Recebe também o PMF Score draft para auditoria

## Output

- Critique Report por artefato: lista de claims contestados (com grau de confianca: Alto/Medio/Baixo), gaps de evidencia identificados, sugestoes de pesquisa adicional, vieses detectados, endorsements (o que esta solido)
- PMF Score Audit: ajuste justificado do score com base em inconsistencias encontradas
- Red-Team Summary para o Orion decidir o que retrabalhar vs
- aceitar com ressalva

## Trigger

Ativado pelo Orion automaticamente após cada agente entregar output principal. Executa em série (não paralelo) para ter visão completa. HITL ativado se Brutus reprovar mais de 30% dos claims de qualquer artefato.

## Knowledge base (o que o executor consulta)

- Metodologias de avaliação de evidências (pirâmide de evidências, CRAAP test), histórico de outputs anteriores do squad para consistência, base de vieses cognitivos comuns em pesquisa de mercado, critérios de quality gate (dev 70% / staging 85% / prod 95%)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Todos os outputs intermediários: Relatório de Marco, ICP Profile de Iris, Signal Report de Vesper, Persona Cards de Nyx…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Critique Report por artefato: lista de claims contestados (com grau de confianca: Alto/Medio/Baixo), gaps de evidencia…) e persistir no artefato do squad.
4. Entregar ao critic Brutus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Critique Report por artefato: lista de claims contestados (com grau de confianca: Alto/Medio/Baixo), gaps de evidencia identificados, sugestoes de pesquisa adi…
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

- **to:** Vega
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
