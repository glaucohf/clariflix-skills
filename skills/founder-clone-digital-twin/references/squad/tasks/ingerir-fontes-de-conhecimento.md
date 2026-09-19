---
task: chronicle()
responsavel: "CHRONICLE"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Novas fontes de conhecimento (áudio transcrito via Sembly, documentos PDF/Notion, threads de email via Gmail MCP, posts LinkedIn, anotações manuais do founder), feedback validado pelo founder sobre respostas do ECHO (correto / incorreto / parcialmente correto + correção), pedidos de atualização manuais"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Knowledge Graph atualizado (novas entidades, relações, exemplos canônicos adicionados), base vetorial sincronizada, relatório de atualização (o que foi adicionado, o que foi corrigido, gaps identificados), alertas de gaps críticos para o ORION, score de completude do corpus por categoria (operacional / estratégica / cultural / técnica)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ingestão contínua: disparado por webhook sempre que nova fonte é adicionada ao repositório (Notion, Google Drive, email marcado com label específico). Loop de aprendizado: disparado após cada ciclo d…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio – o squad nunca envia comunicação externa autonomamente"
    - "[ ] L3: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política interna – founder aprova com opções claras antes da execução"
    - "[ ] L3: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao de pensamento antes de ser persistida no corpus canônico"
    - "[ ] L2: ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma aproximação e pode escalonar"
    - "[ ] L2: STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer caminho seja comunicado como recomendacao oficial do squad"
---

# Ingerir Fontes De Conhecimento

**Task ID:** `chronicle()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Ingerir Fontes De Conhecimento |
| **status** | `pending` |
| **responsible_executor** | CHRONICLE (CHRONICLE — O Agente de Ingestão e Knowledge Graph) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker responsável pela construção, manutenção e expansão contínua do segundo cérebro do founder. Ingere novas fontes de conhecimento (reuniões gravadas, documentos, emails estratégicos, conteúdo publicado, anotações avulsas), extrai entidades, frameworks, princípios de decisão e relações, estrutura no Knowledge Graph e atualiza a base vetorial para recuperação semântica. Também executa o loop de aprendizado: após cada interação validada pelo founder, processa o feedback, identifica o que o ECHO acertou/errou e atualiza o grafo. Detecta proativamente gaps críticos no corpus e notifica o ORION para agendar sessões de captura de conhecimento com o founder.

## Input

- Novas fontes de conhecimento (áudio transcrito via Sembly, documentos PDF/Notion, threads de email via Gmail MCP, posts LinkedIn, anotações manuais do founder), feedback validado pelo founder sobre respostas do ECHO (correto / incorreto / parcialmente correto + correção), pedidos de atualização manuais

## Output

- Knowledge Graph atualizado (novas entidades, relações, exemplos canônicos adicionados), base vetorial sincronizada, relatório de atualização (o que foi adicionado, o que foi corrigido, gaps identificados), alertas de gaps críticos para o ORION, score de completude do corpus por categoria (operacional / estratégica / cultural / técnica)

## Trigger

Ingestão contínua: disparado por webhook sempre que nova fonte é adicionada ao repositório (Notion, Google Drive, email marcado com label específico). Loop de aprendizado: disparado após cada ciclo de feedback do founder. Relatório semanal: cron job todo domingo às 18h.

## Knowledge base (o que o executor consulta)

- Repositório de fontes brutas do founder (Notion workspace, Google Drive, Gmail com labels específicos, Sembly para transcrições de reuniões), grafo de conhecimento atual (Neo4j ou Supabase com relações estruturadas), base vetorial para busca semântica (Supabase pgvector ou Pinecone), schema de ontologia do founder (definido na fase Discovery e evoluído iterativamente)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Novas fontes de conhecimento (áudio transcrito via Sembly, documentos PDF/Notion, threads de email via Gmail MCP, posts…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Knowledge Graph atualizado (novas entidades, relações, exemplos canônicos adicionados), base vetorial sincronizada, rel…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Knowledge Graph atualizado (novas entidades, relações, exemplos canônicos adicionados), base vetorial sincronizada, relatório de atualização (o que foi adicion…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SENTINEL registrado
- [ ] Gate L3 respeitado: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder ante…
- [ ] Gate L3 respeitado: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou…
- [ ] Gate L3 respeitado: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuin…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma apr… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — VIGIL ao detectar sinal competitivo CRÍTICO fora do ciclo semanal: notificação imediata ao founder com proposta de contra-jogada — founder decide se ativa resp… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — CHRONICLE ao identificar gap crítico no corpus que impacta a confiabilidade do ECHO em categoria de alto volume: agenda sessão de captura de conhecimento com o… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** STRATEGOS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
