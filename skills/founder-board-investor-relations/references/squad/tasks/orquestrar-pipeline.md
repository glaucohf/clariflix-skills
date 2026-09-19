---
task: cassidyPipeline()
responsavel: "Cassidy"
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
    descricao: "Board Pack Cycle Artifact"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "artefato verificável por ciclo composto de: (1) Board Pack ou Investor Update final em PDF/Notion com 95%+ de claims rastreáveis e Source Manifest anexo"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Metrics Table canônica do ciclo (todas as fontes, datas de extração, flags de inconsistência resolvidas)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Q&A Brief com top 10 perguntas previstas e respostas preparadas pelo founder"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(4) Diff de ciclo (o que mudou vs comunicação anterior em métricas e narrativa)"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(5) Audit trail completo no ClickUp (versão enviada, aprovador, destinatários, timestamp)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestradora central do squad de Board & Investor Relations. Recebe o trigger do ciclo (data do board meeting, solicitação de investor update, preparação de IC memo) e decompõe a intenção em tarefas…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Axiom antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção"
    - "[ ] HITL: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores"
    - "[ ] HITL: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%"
    - "[ ] HITL: Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)"
    - "[ ] HITL: Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final"
---

# Orquestrar Pipeline do Board & Investor Relations

**Task ID:** `cassidyPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Board & Investor Relations |
| **status** | `pending` |
| **responsible_executor** | Cassidy (Cassidy — Board Relations Orchestrator) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestradora central do squad de Board & Investor Relations. Recebe o trigger do ciclo (data do board meeting, solicitação de investor update, preparação de IC memo) e decompõe a intenção em tarefas atômicas: quais dados coletar, quais workers ativar, qual narrativa construir, quais claims validar. Mantém o estado do ciclo (qual versão está em draft, quais seções foram aprovadas, quais perguntas do board estão previstas). Sintetiza outputs de todos os workers em artefatos coesos. Nunca envia artefatos externamente — roteia tudo pelo HITL Gate antes de qualquer saída do sistema.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Board Pack Cycle Artifact
- artefato verificável por ciclo composto de: (1) Board Pack ou Investor Update final em PDF/Notion com 95%+ de claims rastreáveis e Source Manifest anexo
- (2) Metrics Table canônica do ciclo (todas as fontes, datas de extração, flags de inconsistência resolvidas)
- (3) Q&A Brief com top 10 perguntas previstas e respostas preparadas pelo founder
- (4) Diff de ciclo (o que mudou vs comunicação anterior em métricas e narrativa)
- (5) Audit trail completo no ClickUp (versão enviada, aprovador, destinatários, timestamp)
- (6) Score de rastreabilidade do Axiom por seção
- Tudo arquivado no data room com versionamento e auditável pelo board ou due diligence de futura rodada

## Trigger

Orquestradora central do squad de Board & Investor Relations. Recebe o trigger do ciclo (data do board meeting, solicitação de investor update, preparação de IC memo) e decompõe a intenção em tarefas atômicas: quais dados coletar, quais workers ativar, qual narrativa construir, quais claims validar. Mantém o estado do ciclo (qual versão está em draft, quais seções foram aprovadas, quais perguntas do board estão previstas). Sintetiza outputs de todos os workers em artefatos coesos. Nunca envia artefatos externamente — roteia tudo pelo HITL Gate antes de qualquer saída do sistema.

## Knowledge base (o que o executor consulta)

- Stripe / QuickBooks / Conta Azul (receita, MRR/ARR, burn, runway
- fonte primária para Rex)
- HubSpot / Salesforce CRM (pipeline, novos clientes, churn, expansão, CAC
- fonte primária para Rex)
- Mixpanel / Amplitude / PostHog (métricas de produto, DAU/MAU, NPS, feature adoption)
- Gupy / Lever / Greenhouse (headcount, hiring, attrition
- componente de board pack)
- Captable.io / Carta (cap table, ownership, opções
- para seções de governance e rodada)
- Notion (data room estruturado, board packs arquivados, knowledge base do squad)
- Google Drive / Slides (geração e armazenamento de apresentações de board)
- Gmail / Outlook (envio controlado de investor updates via Gate Agent após aprovação HITL)
- Slack (entrega de drafts e alertas ao founder, interface conversacional com Cassidy)
- ClickUp (audit trail de ciclos, tasks de revisão, prova de trabalho do squad)
- WrenAI / Snowflake Cortex (camada semântica governada para text-to-SQL do Rex)
- EXA / Perplexity MCP (deep research externo para Marlowe
- benchmarks e contexto de mercado)
- Langfuse (observabilidade OTEL
- tracing de tokens, custo por agente, task success rate)
- Vector DB
- Pinecone / Qdrant (corpus do founder para Sage, histórico de Source Manifests)
- Sembly / Fireflies (transcrições de board meetings e investor calls para alimentar Quincy e Sage)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Axiom antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Board Pack Cycle Artifact
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Axiom registrado
- [ ] Gate HITL respeitado: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- [ ] Gate HITL respeitado: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao b…
- [ ] Gate HITL respeitado: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90% | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa nã… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downr… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser r… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Axiom | BLOQUEIA entrega |

## Handoff

- **to:** Rex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
