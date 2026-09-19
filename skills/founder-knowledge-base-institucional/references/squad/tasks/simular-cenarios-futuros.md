---
task: wargame()
responsavel: "WARGAME"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Contexto da decisão ou cenário a simular, tese do founder sobre o tópico (do grafo), dados de mercado e concorrentes (do Radar), restrições relevantes (financeiras, operacionais, temporais), audiência do output (uso interno vs apresentação externa)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio de cenarios com: 3-5 futuros possiveis com probabilidade estimada e premissas, mapa de riscos por cenario com nivel de reversibilidade, estrategias de resposta por cenario com acoes concretas, secao adversarial (as melhores objecoes e como respondelas), e recomendacao sintetica baseada nos frameworks do founder"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Cada cenario com rastreabilidade ao grafo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo ORION quando founder ou Chief of Staff solicita análise de decisão complexa. Também disparado automaticamente quando o Radar detecta sinal de alta urgência (ex: concorrente lançou produ…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic AUDITOR antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automaticamente — pausa e apresenta ao founder os dois claims com contexto (data, situacao) para ele determinar qual e a posicao atual e por que evoluiu. Irreversivel porque altera permanentemente o grafo canônico."
    - "[ ] L3: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída para fora da empresa exige leitura e aprovação explícita do founder. O clone fala pela empresa — erro de representação e irreversível reputacionalmente."
    - "[ ] L3: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com anotações de contexto por seção para facilitar a revisão, mas o envio nunca é automático."
    - "[ ] L2: Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para reunião'. O founder decide o que fazer com o sinal, não o squad."
    - "[ ] L2: Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao ha ingestao forçada — o founder controla o ritmo de captura do proprio conhecimento."
---

# Simular Cenários Futuros

**Task ID:** `wargame()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Simular Cenários Futuros |
| **status** | `pending` |
| **responsible_executor** | WARGAME (WARGAME — O Simulador de Cenários) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de inteligência estratégica prospectiva. Dado um contexto de decisão ou ameaça competitiva, o Wargame simula cenários futuros e adversários autônomos a partir do grafo de conhecimento. Opera em dois modos: (1) Modo Decisão — para uma decisão estratégica do founder (ex: entrar em novo mercado, lançar novo produto, mudar pricing), simula 3-5 cenários com probabilidades, impactos e estratégias de resposta, sempre ancorado nas teses e frameworks do founder no grafo; (2) Modo Adversarial — assume o papel de concorrente específico ou investidor cético e gera as melhores objeções possíveis a uma tese ou plano, ajudando o founder a fortalecer o argumento antes de apresentar externamente. Todos os cenários citam as premissas do grafo que os fundamentam.

## Input

- Contexto da decisão ou cenário a simular, tese do founder sobre o tópico (do grafo), dados de mercado e concorrentes (do Radar), restrições relevantes (financeiras, operacionais, temporais), audiência do output (uso interno vs apresentação externa)

## Output

- Relatorio de cenarios com: 3-5 futuros possiveis com probabilidade estimada e premissas, mapa de riscos por cenario com nivel de reversibilidade, estrategias de resposta por cenario com acoes concretas, secao adversarial (as melhores objecoes e como respondelas), e recomendacao sintetica baseada nos frameworks do founder
- Cada cenario com rastreabilidade ao grafo

## Trigger

Acionado pelo ORION quando founder ou Chief of Staff solicita análise de decisão complexa. Também disparado automaticamente quando o Radar detecta sinal de alta urgência (ex: concorrente lançou produto direto) — gera análise de cenários de resposta sem esperar solicitação manual. Acionado pelo Scrivener quando memo de board requer seção de riscos e estratégia.

## Knowledge base (o que o executor consulta)

- Grafo de conhecimento (teses, frameworks, histórico de decisões do founder)
- Dados de inteligência competitiva do Radar
- Histórico de cenários anteriores e acurácia das previsões
- Frameworks de strategic foresight (2x2 de incerteza, cenários de Porter, wargaming competitivo)
- Dados de mercado e benchmarks setoriais

## Action Items

1. Confirmar o gatilho e carregar a entrada (Contexto da decisão ou cenário a simular, tese do founder sobre o tópico (do grafo), dados de mercado e concorrentes (d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio de cenarios com: 3-5 futuros possiveis com probabilidade estimada e premissas, mapa de riscos por cenario com…) e persistir no artefato do squad.
4. Entregar ao critic AUDITOR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio de cenarios com: 3-5 futuros possiveis com probabilidade estimada e premissas, mapa de riscos por cenario com nivel de reversibilidade, estrategias d…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic AUDITOR registrado
- [ ] Gate L3 respeitado: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o graf…
- [ ] Gate L3 respeitado: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, m…
- [ ] Gate L3 respeitado: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scriv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automat… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída pa… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com ano… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao h… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão do mapa de lacunas gerado no Discovery: antes de priorizar quais tópicos capturar, o founder valida se a taxonomia e as lacunas identificadas fazem sen… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic AUDITOR | BLOQUEIA entrega |

## Handoff

- **to:** AUDITOR
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
