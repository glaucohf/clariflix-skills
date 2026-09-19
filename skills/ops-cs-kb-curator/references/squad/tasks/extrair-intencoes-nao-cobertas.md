---
task: milo()
responsavel: "Milo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dump de tickets fechados sem fonte KB (JSON/CSV do Zendesk ou Intercom), vetor da KB atual (embeddings), taxonomia de intenções do produto"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Gap Priority Report (JSON rankeado: intenção, volume, criticidade, tickets de evidência, artigos parciais existentes, sugestão de fonte)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Brief por gap (Markdown: contexto, público-alvo, tom, fontes primárias, conflitos detectados)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diário (02h00) + webhook a cada 50 tickets novos fechados sem match KB + chamada manual do Kael."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Lex 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Publicação de artigo novo ou update em produção: Kael agrega o pacote (artigo + gap de origem + diff + scores do Lex + badge do Clio) e envia para aprovação humana via ClickUp task com preview. SLA de resposta: 24h. Se não aprovado em 24h, artigo fica em staging e Kael notifica no Slack."
    - "[ ] L3: Deprecação de artigo existente: Clio detecta artigo órfão ou conflitante que deve ser removido. Requer aprovação explícita do gestor de CS antes de despublicar."
    - "[ ] L3: Resolução de conflito entre artigos: quando Clio identifica contradição direta entre dois artigos e não consegue determinar automaticamente qual é a fonte de verdade (ex: ambos recentes, ambos com alto uso), escala para SME humano com Conflict Report estruturado."
    - "[ ] L2: Reescrita após 2 iterações Lex/Véra: se após dois ciclos de revisão o artigo não atingiu score mínimo (7/10 em compliance e acionabilidade), Kael escala para editor humano com histórico completo das iterações."
    - "[ ] L1: Validação do Gap Priority Report semanal: Milo gera o ranking de gaps, humano (CS lead) confirma ou reordena as prioridades antes do ciclo de produção começar. Não bloqueia execução, mas calibra o roadmap da KB."
---

# Extrair Intenções Nao Cobertas

**Task ID:** `milo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KB Curator Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Extrair Intenções Nao Cobertas |
| **status** | `pending` |
| **responsible_executor** | Milo (Milo — O Pesquisador de Contexto) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Extrai intenções não cobertas dos tickets, faz embedding similarity contra a KB atual, classifica gaps por categoria e gera o brief estruturado com fontes e linguagem real do cliente.

## Input

- Dump de tickets fechados sem fonte KB (JSON/CSV do Zendesk ou Intercom), vetor da KB atual (embeddings), taxonomia de intenções do produto

## Output

- Gap Priority Report (JSON rankeado: intenção, volume, criticidade, tickets de evidência, artigos parciais existentes, sugestão de fonte)
- Brief por gap (Markdown: contexto, público-alvo, tom, fontes primárias, conflitos detectados)

## Trigger

Cron diário (02h00) + webhook a cada 50 tickets novos fechados sem match KB + chamada manual do Kael.

## Knowledge base (o que o executor consulta)

- Histórico de tickets (90 dias), KB atual vetorizada, taxonomia de intenções, lista de SMEs internos por área, glossário de produto

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dump de tickets fechados sem fonte KB (JSON/CSV do Zendesk ou Intercom), vetor da KB atual (embeddings), taxonomia de i…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Gap Priority Report (JSON rankeado: intenção, volume, criticidade, tickets de evidência, artigos parciais existentes, s…) e persistir no artefato do squad.
4. Entregar ao critic Lex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Gap Priority Report (JSON rankeado: intenção, volume, criticidade, tickets de evidência, artigos parciais existentes, sugestão de fonte)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Lex 2 registrado
- [ ] Gate L3 respeitado: Publicação de artigo novo ou update em produção: Kael agrega o pacote (artigo + gap de origem + diff + scores do Lex + badge do Clio) e env…
- [ ] Gate L3 respeitado: Deprecação de artigo existente: Clio detecta artigo órfão ou conflitante que deve ser removido. Requer aprovação explícita do gestor de CS…
- [ ] Gate L3 respeitado: Resolução de conflito entre artigos: quando Clio identifica contradição direta entre dois artigos e não consegue determinar automaticamente…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Publicação de artigo novo ou update em produção: Kael agrega o pacote (artigo + gap de origem + diff + scores do Lex + badge do Clio) e envia para aprovação hu… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Deprecação de artigo existente: Clio detecta artigo órfão ou conflitante que deve ser removido. Requer aprovação explícita do gestor de CS antes de despublicar. | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Resolução de conflito entre artigos: quando Clio identifica contradição direta entre dois artigos e não consegue determinar automaticamente qual é a fonte de v… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Reescrita após 2 iterações Lex/Véra: se após dois ciclos de revisão o artigo não atingiu score mínimo (7/10 em compliance e acionabilidade), Kael escala para e… | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Validação do Gap Priority Report semanal: Milo gera o ranking de gaps, humano (CS lead) confirma ou reordena as prioridades antes do ciclo de produção começar.… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Lex 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vera
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
