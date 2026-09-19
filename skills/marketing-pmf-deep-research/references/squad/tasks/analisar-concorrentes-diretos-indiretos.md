---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de concorrentes (diretos e indiretos) validada pelo cliente, verticais de mercado, relatório parcial de Marco, critérios de avaliação priorizados pelo cliente (pricing, copy, UX, suporte, etc.)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Competitive Matrix (planilha): 10-15 dimensões de comparação por concorrente"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Battle Cards (1 página por concorrente top-3): como vencer, objeções comuns do concorrente e respostas recomendadas, pontos fracos exploráveis"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Positioning Gap Map: espaços de mercado não ocupados com estimativa de oportunidade"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Share of Voice estimado por canal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Orion em paralelo com Marco na fase Deep Dive. Re-ativado quando cliente identifica novo concorrente relevante ou quando Brutus detecta claims competitivos sem evidência."
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

# Analisar Concorrentes Diretos Indiretos

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** PMF & Market Deep Research Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Concorrentes Diretos Indiretos |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Competitive Intelligence Analyst) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente especialista em inteligência competitiva. Executa análise profunda de 5-10 concorrentes diretos e indiretos: pricing, copy de ads e landing pages, reviews de clientes, estratégia de conteúdo, canais de aquisição, pontos fracos exploráveis e movimentos recentes (funding, hirings, novos produtos). Identifica gaps de posicionamento e oportunidades de diferenciação.

## Input

- Lista de concorrentes (diretos e indiretos) validada pelo cliente, verticais de mercado, relatório parcial de Marco, critérios de avaliação priorizados pelo cliente (pricing, copy, UX, suporte, etc.)

## Output

- Competitive Matrix (planilha): 10-15 dimensões de comparação por concorrente
- Battle Cards (1 página por concorrente top-3): como vencer, objeções comuns do concorrente e respostas recomendadas, pontos fracos exploráveis
- Positioning Gap Map: espaços de mercado não ocupados com estimativa de oportunidade
- Share of Voice estimado por canal

## Trigger

Ativado pelo Orion em paralelo com Marco na fase Deep Dive. Re-ativado quando cliente identifica novo concorrente relevante ou quando Brutus detecta claims competitivos sem evidência.

## Knowledge base (o que o executor consulta)

- Dados públicos de ads (Meta Ad Library, Google Ads Transparency), reviews em G2/Capterra/Trustpilot, SEMrush/SimilarWeb para share of voice, LinkedIn para sinais de hiring/estratégia, Product Hunt para lançamentos recentes, press releases e blogs dos concorrentes

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de concorrentes (diretos e indiretos) validada pelo cliente, verticais de mercado, relatório parcial de Marco, cr…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Competitive Matrix (planilha): 10-15 dimensões de comparação por concorrente) e persistir no artefato do squad.
4. Entregar ao critic Brutus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Competitive Matrix (planilha): 10-15 dimensões de comparação por concorrente
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

- **to:** Brutus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
