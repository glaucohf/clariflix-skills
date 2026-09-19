---
task: petra()
responsavel: "Petra"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de artigos publicados na semana + tickets novos dos últimos 7 dias com classificação de intenção + taxa de resolução Tier-1 por artigo (via webhook do helpdesk)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Weekly Impact Report (por artigo: resolução%, volume de tickets cobertos, escalonamentos evitados estimados, status SAUDÁVEL/ALERTA/CRÍTICO)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Fila de artigos para revisão urgente (resolução < 70%)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Input para o cálculo de ROI mensal do squad"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron semanal (segunda 08h00) + webhook de feedback negativo do Tier-1 Resolver (quando agente marca 'KB_NÃO_RESOLVEU')."
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

# Monitorar Impacto Artigos

**Task ID:** `petra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KB Curator Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Impacto Artigos |
| **status** | `pending` |
| **responsible_executor** | Petra (Petra — A Monitora de Impacto) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mede se os artigos publicados realmente resolvem os tickets que os originaram. Após cada publicação, monitora por 7 dias: quantos tickets com intenção equivalente foram resolvidos pelo Tier-1 citando o artigo novo vs. escalonados. Se resolução < 70%, dispara alerta de baixo desempenho para Kael iniciar ciclo de atualização.

## Input

- Lista de artigos publicados na semana + tickets novos dos últimos 7 dias com classificação de intenção + taxa de resolução Tier-1 por artigo (via webhook do helpdesk)

## Output

- Weekly Impact Report (por artigo: resolução%, volume de tickets cobertos, escalonamentos evitados estimados, status SAUDÁVEL/ALERTA/CRÍTICO)
- Fila de artigos para revisão urgente (resolução < 70%)
- Input para o cálculo de ROI mensal do squad

## Trigger

Cron semanal (segunda 08h00) + webhook de feedback negativo do Tier-1 Resolver (quando agente marca 'KB_NÃO_RESOLVEU').

## Knowledge base (o que o executor consulta)

- Log de publicações do squad (artigo, data, gap de origem), métricas de resolução do helpdesk, histórico de performance por categoria de artigo, baseline de escalonamentos pre-KB-Curator

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de artigos publicados na semana + tickets novos dos últimos 7 dias com classificação de intenção + taxa de resolu…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Weekly Impact Report (por artigo: resolução%, volume de tickets cobertos, escalonamentos evitados estimados, status SAU…) e persistir no artefato do squad.
4. Entregar ao critic Lex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Weekly Impact Report (por artigo: resolução%, volume de tickets cobertos, escalonamentos evitados estimados, status SAUDÁVEL/ALERTA/CRÍTICO)
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

- **to:** Arco
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
