---
task: vera()
responsavel: "Vera"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Brief estruturado do Milo (contexto, público, fontes, tom), template de artigo da empresa, artigos similares existentes para consistência de estilo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Draft de artigo completo (Markdown formatado conforme template), metadados preenchidos (categoria, tags, público, produto afetado, versão), diff linha a linha em relação ao artigo anterior (se for update)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe brief aprovado do Milo via Kael. Também dispara para atualizações quando Petra detecta artigo com queda de resolução > 20% na semana."
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

# Escrever Artigo De KB

**Task ID:** `vera()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KB Curator Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Escrever Artigo De KB |
| **status** | `pending` |
| **responsible_executor** | Vera (Véra — A Escritora de Artigos) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Transforma o brief do Milo em artigo de KB no formato padrão da empresa: título SEO-friendly, resumo de 2 linhas, corpo estruturado (problema -> causa -> solução -> verificação), tags, metadados de categoria e link de artigos relacionados.

## Input

- Brief estruturado do Milo (contexto, público, fontes, tom), template de artigo da empresa, artigos similares existentes para consistência de estilo

## Output

- Draft de artigo completo (Markdown formatado conforme template), metadados preenchidos (categoria, tags, público, produto afetado, versão), diff linha a linha em relação ao artigo anterior (se for update)

## Trigger

Recebe brief aprovado do Milo via Kael. Também dispara para atualizações quando Petra detecta artigo com queda de resolução > 20% na semana.

## Knowledge base (o que o executor consulta)

- Template de artigos da empresa, guia de estilo editorial, glossário técnico, lista de artigos relacionados por categoria, histórico de artigos aprovados para benchmarking de qualidade

## Action Items

1. Confirmar o gatilho e carregar a entrada (Brief estruturado do Milo (contexto, público, fontes, tom), template de artigo da empresa, artigos similares existentes…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Draft de artigo completo (Markdown formatado conforme template), metadados preenchidos (categoria, tags, público, produ…) e persistir no artefato do squad.
4. Entregar ao critic Lex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Draft de artigo completo (Markdown formatado conforme template), metadados preenchidos (categoria, tags, público, produto afetado, versão), diff linha a linha…
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

- **to:** Lex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
