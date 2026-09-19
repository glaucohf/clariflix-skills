---
task: cartographer()
responsavel: "CARTOGRAPHER"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "JSON de chunks do SCRIBE (validados pelo Auditor), schema atual do grafo, índice de entidades existentes, regras de tipagem de arestas definidas no Discovery"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Grafo atualizado com novos nós e arestas, log de contradições detectadas (para HITL), mapa de cobertura por domínio (% de tópicos críticos com pelo menos 3 fontes convergentes), embeddings atualizados no vector store"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato de prova: relatório de ingestão com delta (X nós adicionados, Y arestas, Z contradições sinalizadas)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo ORION após cada lote de chunks validados pelo Auditor (mínimo 10 chunks ou 24h sem ingestão nova). Também acionado para reprocessamento quando o founder valida ou rejeita uma contradição…"
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

# Construir Grafo Conhecimento

**Task ID:** `cartographer()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Construir Grafo Conhecimento |
| **status** | `pending` |
| **responsible_executor** | CARTOGRAPHER (CARTOGRAPHER — O Construtor do Grafo) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em estruturar os chunks ingeridos pelo SCRIBE em um grafo de conhecimento coerente e consultável. Recebe os JSONs de chunks e executa: resolução de entidades (mesmo conceito citado com nomes diferentes), criação de nós (conceitos, pessoas, empresas, mercados, decisões, frameworks), criação de arestas tipadas (fundamenta / contradiz / evolui / exemplifica / decide / apoia), detecção de contradições (mesmo tópico com claims opostos em datas diferentes — sinaliza para validação humana), e cálculo de peso por aresta (baseado em frequência e nível de confiança). Mantém o grafo vetorizado para recuperação semântica (embeddings por nó e por aresta).

## Input

- JSON de chunks do SCRIBE (validados pelo Auditor), schema atual do grafo, índice de entidades existentes, regras de tipagem de arestas definidas no Discovery

## Output

- Grafo atualizado com novos nós e arestas, log de contradições detectadas (para HITL), mapa de cobertura por domínio (% de tópicos críticos com pelo menos 3 fontes convergentes), embeddings atualizados no vector store
- Artefato de prova: relatório de ingestão com delta (X nós adicionados, Y arestas, Z contradições sinalizadas)

## Trigger

Disparo pelo ORION após cada lote de chunks validados pelo Auditor (mínimo 10 chunks ou 24h sem ingestão nova). Também acionado para reprocessamento quando o founder valida ou rejeita uma contradição sinalizada.

## Knowledge base (o que o executor consulta)

- Schema do grafo (ontologia de entidades e tipos de aresta)
- Vector store (Supabase pgvector ou Pinecone) com embeddings do corpus
- Regras de deduplicacao de entidades
- Taxonomia de topicos do Discovery
- Historico de versoes do grafo (para rastreabilidade de evolucao do pensamento do founder)

## Action Items

1. Confirmar o gatilho e carregar a entrada (JSON de chunks do SCRIBE (validados pelo Auditor), schema atual do grafo, índice de entidades existentes, regras de tip…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Grafo atualizado com novos nós e arestas, log de contradições detectadas (para HITL), mapa de cobertura por domínio (%…) e persistir no artefato do squad.
4. Entregar ao critic AUDITOR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Grafo atualizado com novos nós e arestas, log de contradições detectadas (para HITL), mapa de cobertura por domínio (% de tópicos críticos com pelo menos 3 fon…
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

- **to:** PERSONA FORGE
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
