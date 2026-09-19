---
task: personaForge()
responsavel: "PERSONA FORGE"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pergunta estrategica (texto livre), contexto da consulta (quem pergunta, qual decisao esta em jogo), grafo de conhecimento vetorizado, corpus de exemplos de raciocinio e tom do founder"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta estruturada com: sintese da posicao do founder sobre o topico, frameworks aplicados (nomeados e explicados), evidencias do corpus com citacoes e datas, nivel de confianca geral, lacunas identificadas (topicos relacionados ainda nao estruturados), e sugestao de pergunta de follow-up para aprofundamento"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Nunca responde sem citar fonte do grafo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo ORION quando membro do time ou outro squad faz consulta estrategica. Tambem acionado diretamente pelo Chief of Staff Agent para preparacao de reunioes. Disponivel via interface de chat i…"
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

# Sintetizar Respostas Confidentes

**Task ID:** `personaForge()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Respostas Confidentes |
| **status** | `pending` |
| **responsible_executor** | PERSONA FORGE (PERSONA FORGE — O Clone Estratégico) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker que encarna a logica de raciocinio, os frameworks, o tom e os modelos mentais do founder para responder perguntas estrategicas como ele responderia. Diferente de um chatbot generico, o Persona Forge opera EXCLUSIVAMENTE sobre o corpus verificado do grafo — nao inventa, nao extrapola alem das evidencias. Para cada consulta, executa: recuperacao semantica dos nos mais relevantes do grafo, verificacao de cobertura (se o grafo nao tem evidencia suficiente, responde com 'lacuna identificada' ao inves de especular), sintese da resposta no tom e com os frameworks do founder (citando as fontes do grafo), e flag de confianca (ALTA: multiplas fontes convergentes / MEDIA: fonte unica / BAIXA: inferencia do grafo sem declaracao direta).

## Input

- Pergunta estrategica (texto livre), contexto da consulta (quem pergunta, qual decisao esta em jogo), grafo de conhecimento vetorizado, corpus de exemplos de raciocinio e tom do founder

## Output

- Resposta estruturada com: sintese da posicao do founder sobre o topico, frameworks aplicados (nomeados e explicados), evidencias do corpus com citacoes e datas, nivel de confianca geral, lacunas identificadas (topicos relacionados ainda nao estruturados), e sugestao de pergunta de follow-up para aprofundamento
- Nunca responde sem citar fonte do grafo

## Trigger

Disparo pelo ORION quando membro do time ou outro squad faz consulta estrategica. Tambem acionado diretamente pelo Chief of Staff Agent para preparacao de reunioes. Disponivel via interface de chat integrada ao Slack ou Notion com comando /clone.

## Knowledge base (o que o executor consulta)

- Grafo de conhecimento completo (nos + arestas + embeddings)
- Corpus de exemplos de escrita e raciocinio do founder (emails, posts, palestras)
- Dicionario de frameworks proprios do founder (nomeclatura especifica, definicoes, exemplos de aplicacao)
- Historico de consultas anteriores (para melhoria continua e identificacao de topicos mais demandados)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pergunta estrategica (texto livre), contexto da consulta (quem pergunta, qual decisao esta em jogo), grafo de conhecime…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resposta estruturada com: sintese da posicao do founder sobre o topico, frameworks aplicados (nomeados e explicados), e…) e persistir no artefato do squad.
4. Entregar ao critic AUDITOR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta estruturada com: sintese da posicao do founder sobre o topico, frameworks aplicados (nomeados e explicados), evidencias do corpus com citacoes e datas…
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

- **to:** SCRIVENER
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
