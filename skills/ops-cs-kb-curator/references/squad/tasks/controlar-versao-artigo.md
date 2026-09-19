---
task: arco()
responsavel: "Arco"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft aprovado para publicação + metadados do ciclo (gap_id, data, agentes envolvidos, score do Léx, veredicto do Clío) + versão anterior do artigo (se update)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Commit de versao na KB com metadata estruturada (JSON no frontmatter do artigo)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Changelog mensal (Markdown: artigos novos, atualizados, deprecados, conflitos resolvidos)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Endpoint de rollback: restaura versao anterior em < 30 segundos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Kael como último passo antes de publicar (pos-HITL). Também chamado quando Petra dispara rollback por queda de performance."
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

# Controlar Versão Artigo

**Task ID:** `arco()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KB Curator Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Controlar Versão Artigo |
| **status** | `pending` |
| **responsible_executor** | Arco (Arco — O Archivista de Versoes) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mantem o controle de versao da KB: cada artigo tem historico de mudancas, quem aprovou, qual gap originou a alteracao e qual era o estado anterior. Permite rollback instantaneo se um artigo atualizado piorar a resolucao. Gera o changelog mensal da KB para o time de CS.

## Input

- Draft aprovado para publicação + metadados do ciclo (gap_id, data, agentes envolvidos, score do Léx, veredicto do Clío) + versão anterior do artigo (se update)

## Output

- Commit de versao na KB com metadata estruturada (JSON no frontmatter do artigo)
- Changelog mensal (Markdown: artigos novos, atualizados, deprecados, conflitos resolvidos)
- Endpoint de rollback: restaura versao anterior em < 30 segundos

## Trigger

Chamado pelo Kael como último passo antes de publicar (pos-HITL). Também chamado quando Petra dispara rollback por queda de performance.

## Knowledge base (o que o executor consulta)

- Repositório de versões da KB (Git ou CMS com versionamento), log de aprovações HITL, baseline de métricas no momento de cada publicação

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft aprovado para publicação + metadados do ciclo (gap_id, data, agentes envolvidos, score do Léx, veredicto do Clío)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Commit de versao na KB com metadata estruturada (JSON no frontmatter do artigo)) e persistir no artefato do squad.
4. Entregar ao critic Lex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Commit de versao na KB com metadata estruturada (JSON no frontmatter do artigo)
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

- **to:** Lex 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
