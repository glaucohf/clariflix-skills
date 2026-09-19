---
task: rex()
responsavel: "Rex"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Range de datas do ciclo, lista de métricas requeridas pelo tipo de comunicação (board pack vs investor update vs IC memo), credenciais de acesso às fontes (via MCP)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Queries ad-hoc do founder em linguagem natural ('qual foi o churn líquido do Q2 vs Q1?')"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Metrics Table canônica (formato estruturado JSON + tabela visual): cada métrica com valor, período, fonte primária, data de extração e flag de inconsistência se divergência detectada entre fontes"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Query log auditável"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alertas de gap (métrica solicitada sem dado disponível)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Início de ciclo de board/investor (D-14 antes do meeting). Solicitação ad-hoc de métrica pelo founder. Inconsistência detectada em dado recebido de outro agente. Check mensal automático de health das…"
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

# Reconciliar Métricas

**Task ID:** `rex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reconciliar Métricas |
| **status** | `pending` |
| **responsible_executor** | Rex (Rex — Analytics & Metrics Reconciler) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Puxa e reconcilia automaticamente todas as métricas do período a partir de múltiplas fontes (dashboard financeiro, CRM, produto, payroll). Traduz perguntas em linguagem natural para queries SQL sobre a camada semântica governada. Detecta e sinaliza divergências entre fontes antes de qualquer número entrar no draft. Produz a tabela de métricas canônica do ciclo, que serve de single source of truth para todos os outros agentes.

## Input

- Range de datas do ciclo, lista de métricas requeridas pelo tipo de comunicação (board pack vs investor update vs IC memo), credenciais de acesso às fontes (via MCP)
- Queries ad-hoc do founder em linguagem natural ('qual foi o churn líquido do Q2 vs Q1?')

## Output

- Metrics Table canônica (formato estruturado JSON + tabela visual): cada métrica com valor, período, fonte primária, data de extração e flag de inconsistência se divergência detectada entre fontes
- Query log auditável
- Alertas de gap (métrica solicitada sem dado disponível)

## Trigger

Início de ciclo de board/investor (D-14 antes do meeting). Solicitação ad-hoc de métrica pelo founder. Inconsistência detectada em dado recebido de outro agente. Check mensal automático de health das integrações de dados.

## Knowledge base (o que o executor consulta)

- Dashboards financeiros (Stripe, QuickBooks, Conta Azul
- receita, burn, runway)
- CRM (HubSpot/Salesforce
- pipeline, churn, expansão, CAC)
- Produto (Mixpanel/Amplitude/PostHog
- DAU, NPS, feature adoption)
- Hiring tracker (Gupy/Lever
- headcount, offers, attrition)
- Cap table (Captable.io/Carta
- ownership, dilution)
- Camada semântica via WrenAI ou Snowflake Cortex

## Action Items

1. Confirmar o gatilho e carregar a entrada (Range de datas do ciclo, lista de métricas requeridas pelo tipo de comunicação (board pack vs investor update vs IC mem…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Metrics Table canônica (formato estruturado JSON + tabela visual): cada métrica com valor, período, fonte primária, dat…) e persistir no artefato do squad.
4. Entregar ao critic Axiom; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Metrics Table canônica (formato estruturado JSON + tabela visual): cada métrica com valor, período, fonte primária, data de extração e flag de inconsistência s…
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

- **to:** Marlowe
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
