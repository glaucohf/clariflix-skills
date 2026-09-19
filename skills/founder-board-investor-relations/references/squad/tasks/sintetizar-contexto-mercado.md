---
task: marlowe()
responsavel: "Marlowe"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de claims de narrativa que precisam de suporte externo (extraída do outline do board pack)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Setor, geografias e comparáveis a pesquisar"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Nível de profundidade (rápido para updates mensais, profundo para IC memos de rodada)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Context Brief: bullets de contexto de mercado com fonte citada (URL + data de acesso), benchmarks de comparáveis com metodologia de comparação, análise de 3 movimentos competitivos relevantes do período"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Formato: Notion page + JSON estruturado para o Provenance Agent consumir"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Início de ciclo de board pack ou IC memo. Claim de narrativa sem fonte detectado pelo Provenance Agent. Founder solicita benchmark específico para suportar argumento de valuation ou posicionamento. A…"
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

# Sintetizar Contexto Mercado

**Task ID:** `marlowe()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Contexto Mercado |
| **status** | `pending` |
| **responsible_executor** | Marlowe (Marlowe — Narrative & Market Context Worker) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pesquisa e sintetiza o contexto externo que embase a narrativa do board pack: benchmarks de setor, comparáveis de crescimento, movimentos de mercado relevantes, regulação e macro. Garante que claims de posicionamento ('somos o único player que X', 'o mercado está crescendo Y%') tenham fonte verificável. Entrega parágrafos de contexto já com citações inline, prontos para inserção no draft.

## Input

- Lista de claims de narrativa que precisam de suporte externo (extraída do outline do board pack)
- Setor, geografias e comparáveis a pesquisar
- Nível de profundidade (rápido para updates mensais, profundo para IC memos de rodada)

## Output

- Context Brief: bullets de contexto de mercado com fonte citada (URL + data de acesso), benchmarks de comparáveis com metodologia de comparação, análise de 3 movimentos competitivos relevantes do período
- Formato: Notion page + JSON estruturado para o Provenance Agent consumir

## Trigger

Início de ciclo de board pack ou IC memo. Claim de narrativa sem fonte detectado pelo Provenance Agent. Founder solicita benchmark específico para suportar argumento de valuation ou posicionamento. Alerta de movimento competitivo relevante.

## Knowledge base (o que o executor consulta)

- Web search (EXA/Perplexity MCP)
- Crunchbase, PitchBook (comparáveis, funding rounds)
- Relatórios setoriais públicos (CB Insights, Gartner públicos, ABVCAP, Distrito)
- News de setor (feeds RSS, Google Alerts configurados)
- Vector DB com histórico de pesquisas de contexto de ciclos anteriores

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de claims de narrativa que precisam de suporte externo (extraída do outline do board pack)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Context Brief: bullets de contexto de mercado com fonte citada (URL + data de acesso), benchmarks de comparáveis com me…) e persistir no artefato do squad.
4. Entregar ao critic Axiom; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Context Brief: bullets de contexto de mercado com fonte citada (URL + data de acesso), benchmarks de comparáveis com metodologia de comparação, análise de 3 mo…
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

- **to:** Vera
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
