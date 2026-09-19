---
task: clio()
responsavel: "Clio"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artigo aprovado pelo Lex + KB completa vetorizada + data de última atualização de cada artigo + métricas de uso por artigo (views, resolução)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Conflict Report (lista de pares de artigos conflitantes com: trecho A, trecho B, data de cada um, sugestao de resolucao)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Lista de artigos orfaos para revisao ou deprecacao"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Badge de consistencia no artigo novo (LIMPO / CONFLITO_DETECTADO / PENDENTE_REVISAO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamada pelo Kael após Lex aprovar o draft. Também roda semanalmente em modo varredura completa da KB."
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

# Verificar Consistência Documental

**Task ID:** `clio()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KB Curator Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Consistência Documental |
| **status** | `pending` |
| **responsible_executor** | Clio (Clio — A Verificadora de Consistência) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Detecta contradições entre o artigo novo/atualizado e os demais documentos da KB. Faz cross-check semântico em toda a base: se dois artigos afirmam coisas diferentes sobre o mesmo tópico, gera um Conflict Report com os trechos conflitantes, qual é mais recente e sugestão de qual deve prevalecer. Também detecta artigos órfãos (sem link de entrada e sem tráfego nos últimos 30 dias).

## Input

- Artigo aprovado pelo Lex + KB completa vetorizada + data de última atualização de cada artigo + métricas de uso por artigo (views, resolução)

## Output

- Conflict Report (lista de pares de artigos conflitantes com: trecho A, trecho B, data de cada um, sugestao de resolucao)
- Lista de artigos orfaos para revisao ou deprecacao
- Badge de consistencia no artigo novo (LIMPO / CONFLITO_DETECTADO / PENDENTE_REVISAO)

## Trigger

Chamada pelo Kael após Lex aprovar o draft. Também roda semanalmente em modo varredura completa da KB.

## Knowledge base (o que o executor consulta)

- KB completa vetorizada (embeddings atualizados), log de conflitos anteriores já resolvidos, histórico de deprecações, métricas de uso por artigo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Artigo aprovado pelo Lex + KB completa vetorizada + data de última atualização de cada artigo + métricas de uso por art…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Conflict Report (lista de pares de artigos conflitantes com: trecho A, trecho B, data de cada um, sugestao de resolucao)) e persistir no artefato do squad.
4. Entregar ao critic Lex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Conflict Report (lista de pares de artigos conflitantes com: trecho A, trecho B, data de cada um, sugestao de resolucao)
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

- **to:** Petra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
