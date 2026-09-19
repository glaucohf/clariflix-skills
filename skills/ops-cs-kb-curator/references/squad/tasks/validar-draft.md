---
task: lex()
responsavel: "Lex"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft da Vera + brief original do Milo + políticas de compliance da empresa + SLAs contratuais + artigos de referência para fact-check"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de revisão (JSON: score por dimensão 0-10, lista de issues com severidade, sugestões de correção linha a linha)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Veredicto: APROVADO / AJUSTE_MENOR / REESCREVER"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Se AJUSTE_MENOR, retorna para Vera com anotações inline"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Se REESCREVER, escala para Kael com justificativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Kael imediatamente após Vera finalizar draft. Também chamado após cada reescrita da Vera."
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

# Validar Draft

**Task ID:** `lex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KB Curator Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validar Draft |
| **status** | `pending` |
| **responsible_executor** | Lex (Lex — O Revisor de Qualidade) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Valida o draft da Vera contra 5 dimensões antes de publicar: (1) alucinação/invenção — toda afirmação deve ter fonte rastreável, (2) tom — adequado ao público (usuário final vs técnico), (3) completude — cobre o gap identificado?, (4) compliance — sem promessas não autorizadas, SLAs incorretos ou dados regulatórios errados, (5) acionabilidade — o usuário consegue resolver o problema sozinho seguindo o artigo?

## Input

- Draft da Vera + brief original do Milo + políticas de compliance da empresa + SLAs contratuais + artigos de referência para fact-check

## Output

- Relatório de revisão (JSON: score por dimensão 0-10, lista de issues com severidade, sugestões de correção linha a linha)
- Veredicto: APROVADO / AJUSTE_MENOR / REESCREVER
- Se AJUSTE_MENOR, retorna para Vera com anotações inline
- Se REESCREVER, escala para Kael com justificativa

## Trigger

Chamado pelo Kael imediatamente após Vera finalizar draft. Também chamado após cada reescrita da Vera.

## Knowledge base (o que o executor consulta)

- Políticas de compliance e legal da empresa, SLAs contratuais por tier de cliente, histórico de artigos reprovados (para aprender padrões de erro), guia de tom e voz da marca

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft da Vera + brief original do Milo + políticas de compliance da empresa + SLAs contratuais + artigos de referência…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de revisão (JSON: score por dimensão 0-10, lista de issues com severidade, sugestões de correção linha a linh…) e persistir no artefato do squad.
4. Entregar ao critic Lex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de revisão (JSON: score por dimensão 0-10, lista de issues com severidade, sugestões de correção linha a linha)
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

- **to:** Clio
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
