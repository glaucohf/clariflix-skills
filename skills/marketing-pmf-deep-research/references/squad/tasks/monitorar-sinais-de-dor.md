---
task: vesper()
responsavel: "Vesper"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "ICP clusters definidos por Iris, lista de palavras-chave de dor, concorrentes a monitorar, verticais de mercado, período de monitoramento (default: últimos 90 dias)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Signal Report: top-20 patterns de linguagem de dor com frequencia e exemplos reais (citacoes anonimizadas), mapa de gatilhos de compra por cluster de ICP, reclamacoes recorrentes sobre concorrentes (oportunidades de posicionamento), trending topics do nicho e calendario de sazonalidade de demanda"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Orion em paralelo com Iris na fase Discovery. Pode ser re-ativado semanalmente para monitoramento contínuo após entrega do framework."
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

# Monitorar Sinais De Dor

**Task ID:** `vesper()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** PMF & Market Deep Research Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais De Dor |
| **status** | `pending` |
| **responsible_executor** | Vesper (Vesper — Signal Sensor) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de monitoramento de sinais de dor e intencao de compra em tempo real. Varre canais organicos (LinkedIn, Reddit, Twitter/X, forums, grupos de WhatsApp publicos, Product Hunt, Indie Hackers) para capturar linguagem real de dor, perguntas frequentes, reclamacoes de concorrentes e gatilhos de compra. Converte sinal bruto em insights acionaveis.

## Input

- ICP clusters definidos por Iris, lista de palavras-chave de dor, concorrentes a monitorar, verticais de mercado, período de monitoramento (default: últimos 90 dias)

## Output

- Signal Report: top-20 patterns de linguagem de dor com frequencia e exemplos reais (citacoes anonimizadas), mapa de gatilhos de compra por cluster de ICP, reclamacoes recorrentes sobre concorrentes (oportunidades de posicionamento), trending topics do nicho e calendario de sazonalidade de demanda

## Trigger

Ativado pelo Orion em paralelo com Iris na fase Discovery. Pode ser re-ativado semanalmente para monitoramento contínuo após entrega do framework.

## Knowledge base (o que o executor consulta)

- Queries de busca semântica por vertical, base de keywords do nicho, lista de comunidades online relevantes (subreddits, grupos LinkedIn, Slack communities), feed de menções de marca dos concorrentes, dados históricos de trends (Google Trends, SEMrush)

## Action Items

1. Confirmar o gatilho e carregar a entrada (ICP clusters definidos por Iris, lista de palavras-chave de dor, concorrentes a monitorar, verticais de mercado, períod…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Signal Report: top-20 patterns de linguagem de dor com frequencia e exemplos reais (citacoes anonimizadas), mapa de gat…) e persistir no artefato do squad.
4. Entregar ao critic Brutus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Signal Report: top-20 patterns de linguagem de dor com frequencia e exemplos reais (citacoes anonimizadas), mapa de gatilhos de compra por cluster de ICP, recl…
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

- **to:** Nyx
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
