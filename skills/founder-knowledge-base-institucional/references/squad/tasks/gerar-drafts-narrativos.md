---
task: scrivener()
responsavel: "SCRIVENER"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Tipo de memo (board pack / investor update / memo interno / apresentação), audiência (board / investidores / time / clientes), tópicos obrigatórios, período de referência (ex: Q2 2026), métricas atualizadas (quando aplicável), grafo de conhecimento, histórico de memos anteriores do mesmo tipo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Draft completo do memo em formato Markdown/Notion com: estrutura narrativa completa, todos os claims com fonte citada do grafo, secoes de destaque (headline numbers, decisoes chave, proximos passos), rodape de proveniencia (mapa de topicos do grafo usados), e lista de lacunas onde dados ou posicionamento do founder ainda nao estao no grafo (itens para o founder preencher manualmente)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Entregue ao founder via Notion com comentarios de contexto por secao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo ORION quando fundador ou Chief of Staff solicita memo com prazo definido. Tambem acionado automaticamente 2 semanas antes de datas de board ou investor meeting detectadas no calendario.…"
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

# Gerar Drafts Narrativos

**Task ID:** `scrivener()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Drafts Narrativos |
| **status** | `pending` |
| **responsible_executor** | SCRIVENER (SCRIVENER — O Motor de Mémos) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em gerar drafts de comunicacoes de alta alavancagem: board packs, investor updates, memos internos, apresentacoes de estrategia, manifestos de produto. Diferente de um gerador de texto generico, o Scrivener puxa claims diretamente do grafo com rastreabilidade total — cada paragrafo do memo e mapeado a nos especificos do grafo com data e fonte. Opera em dois modos: (1) Modo Estruturado — recebe template + topicos a cobrir e monta o memo puxando evidencias do grafo; (2) Modo Narrativo — recebe apenas o objetivo do memo e constroi a estrutura narrativa otima para o audiencia, depois preenche com dados do grafo. Todos os drafts saem com 'rodape de proveniencia' mostrando quais fontes embasaram cada secao.

## Input

- Tipo de memo (board pack / investor update / memo interno / apresentação), audiência (board / investidores / time / clientes), tópicos obrigatórios, período de referência (ex: Q2 2026), métricas atualizadas (quando aplicável), grafo de conhecimento, histórico de memos anteriores do mesmo tipo

## Output

- Draft completo do memo em formato Markdown/Notion com: estrutura narrativa completa, todos os claims com fonte citada do grafo, secoes de destaque (headline numbers, decisoes chave, proximos passos), rodape de proveniencia (mapa de topicos do grafo usados), e lista de lacunas onde dados ou posicionamento do founder ainda nao estao no grafo (itens para o founder preencher manualmente)
- Entregue ao founder via Notion com comentarios de contexto por secao

## Trigger

Disparo pelo ORION quando fundador ou Chief of Staff solicita memo com prazo definido. Tambem acionado automaticamente 2 semanas antes de datas de board ou investor meeting detectadas no calendario. Reacionado pelo ORION quando novos dados criticos entram no grafo (ex: metricas de fim de trimestre).

## Knowledge base (o que o executor consulta)

- Grafo de conhecimento completo
- Histórico de memos anteriores (para manter consistência narrativa e de posicionamento)
- Templates de board pack e investor update por formato (Series A / B / board mensal / quarterly)
- Métricas e dashboards via integração com ferramentas de analytics do cliente
- Guia de tom e estilo do founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Tipo de memo (board pack / investor update / memo interno / apresentação), audiência (board / investidores / time / cli…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Draft completo do memo em formato Markdown/Notion com: estrutura narrativa completa, todos os claims com fonte citada d…) e persistir no artefato do squad.
4. Entregar ao critic AUDITOR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Draft completo do memo em formato Markdown/Notion com: estrutura narrativa completa, todos os claims com fonte citada do grafo, secoes de destaque (headline nu…
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

- **to:** RADAR
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
