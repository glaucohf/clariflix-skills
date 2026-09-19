---
task: kaelPipeline()
responsavel: "Kael"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de publicação por artigo (prova de trabalho): (1) artigo publicado na KB no formato padrão, (2) Gap Card vinculado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "ticket(s) de evidência + intenção identificada + volume impactado, (3) Lex QA Report"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "scores por dimensão + veredicto, (4) Clio Conflict Badge"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "LIMPO ou CONFLITO_RESOLVIDO, (5) ClickUp task fechada com histórico completo do ciclo (agentes, timestamps, iterações), (6) baseline de resolução pré-publicação para comparação pelo Petra na semana seguinte"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestra o ciclo completo de identificação de gap -> produção -> validação -> publicação. Lê o backlog de tickets sem fonte, prioriza por impacto, dispara os workers na sequência correta, agrega os…"
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

# Orquestrar Pipeline do KB Curator Squad

**Task ID:** `kaelPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KB Curator Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do KB Curator Squad |
| **status** | `pending` |
| **responsible_executor** | Kael (Kael — O Curador-Chefe) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestra o ciclo completo de identificação de gap -> produção -> validação -> publicação. Lê o backlog de tickets sem fonte, prioriza por impacto, dispara os workers na sequência correta, agrega os artefatos e gerencia o handoff HITL. Mantém o estado do pipeline no ClickUp (task por artigo, com status e prova de trabalho). Opera no modo orchestrator-worker: delega escrita para Vera, pesquisa para Milo, QA para Lex e monitoramento pós-publicação para Petra.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote de publicação por artigo (prova de trabalho): (1) artigo publicado na KB no formato padrão, (2) Gap Card vinculado
- ticket(s) de evidência + intenção identificada + volume impactado, (3) Lex QA Report
- scores por dimensão + veredicto, (4) Clio Conflict Badge
- LIMPO ou CONFLITO_RESOLVIDO, (5) ClickUp task fechada com histórico completo do ciclo (agentes, timestamps, iterações), (6) baseline de resolução pré-publicação para comparação pelo Petra na semana seguinte

## Trigger

Orquestra o ciclo completo de identificação de gap -> produção -> validação -> publicação. Lê o backlog de tickets sem fonte, prioriza por impacto, dispara os workers na sequência correta, agrega os artefatos e gerencia o handoff HITL. Mantém o estado do pipeline no ClickUp (task por artigo, com status e prova de trabalho). Opera no modo orchestrator-worker: delega escrita para Vera, pesquisa para Milo, QA para Lex e monitoramento pós-publicação para Petra.

## Knowledge base (o que o executor consulta)

- Zendesk / Intercom
- fonte primária de tickets sem match KB, webhooks de feedback de resolução do Tier-1, tags de intenção
- task por artigo (prova de trabalho), status do pipeline (Gap Identified -> Draft -> QA -> HITL -> Published -> Monitored), integracao com AIOX
- Confluence / Notion / GitBook / Freshdesk KB
- destino de publicação dos artigos (configurável por cliente), API de CRUD de artigos
- Supabase / Postgres
- estado do pipeline (gap_id, artigo_id, versão, scores, status), vetorização da KB (pgvector), log de aprovações HITL
- notificações de HITL pendente, alertas de artigo em estado CRÍTICO (Petra), resumo semanal do Impact Report para canal #kb-updates
- OpenAI Embeddings / Anthropic Claude
- geração de embeddings da KB para similarity search, geração de drafts (Vera), fact-check (Lex)
- tracing de cada ciclo de produção (gap -> draft -> revisões -> publicação), evals automatizados por dimensão, quality gates (dev 70% / staging 85% / prod 95% task success)
- Tier-1 Resolver (squad interno)
- recebe atualizações da KB via webhook pós-publicação, envia sinal KB_NÃO_RESOLVEU para Petra

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Lex 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de publicação por artigo (prova de trabalho): (1) artigo publicado na KB no formato padrão, (2) Gap Card vinculado
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

- **to:** Milo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
