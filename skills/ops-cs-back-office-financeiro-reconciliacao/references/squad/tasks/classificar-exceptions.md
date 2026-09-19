---
task: iris()
responsavel: "Iris"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de unmatched_transactions do Nexus (com campos normalizados), Exception Playbook calibrado no Deep Dive (regras de classificacao por tipo, thresholds de tolerancia por tipo, acoes pre-autorizadas por tipo e faixa de valor), historico de exceptions anteriores do cliente (para identificar padroes recorrentes e calibrar confianca da classificacao), status de AR aging e AP aging para contexto de urgencia (ex: boleto vencendo em 3 dias vs"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "30 dias)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Exception Queue (JSON array: cada exception com exception_id, exception_type, financial_impact_cents, urgency_score [0-10], recommended_action, action_confidence [0-1], auto_resolvable [true/false"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "se o Solano pode investigar e resolver sem HITL], hitl_required_reason [preenchido quando auto_resolvable=false], evidence [campos relevantes], related_transactions)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Exception Summary (totais por tipo, valor total em exceptions, exceptions auto-resolvaveis vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "HITL, exceptions blocking para fechamento, top-5 por valor financeiro)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Maestro Caixa imediatamente apos o Matching Report do Nexus. Para modo continuo: chamado a cada ciclo diario para classificar novas exceptions. Tambem pode ser chamado manualmente pelo a…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aurum 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Lancamentos contabeis acima do threshold de aprovacao autonoma: qualquer lancamento (de reconciliacao automatica ou de resolucao de exception) acima do valor configurado (ex: R$10.000 por lancamento, configuravel por cliente) requer aprovacao explicita do Controller via task no ClickUp. O Ledger gera o lancamento formatado e o Aurum escala para HITL com contexto completo (origem, evidencia, impact no resultado)."
    - "[ ] L3: Exceptions classificadas como DISPUTED_CHARGE ou BILLING_DISCREPANCY de alto valor: qualquer disputa formal com fornecedor/cliente ou divergencia de billing acima do threshold configurado requer decisao humana. O Solano prepara o dossie de investigacao completo (evidencias, historico, opcoes de resolucao com pros/contras) para o Controller tomar a decisao."
    - "[ ] L3: Closing Package com veredicto BLOCKED do Aurum: quando o Aurum bloqueia o Closing Package (inconsistencia matematica, violacao de compliance, exceptions acima do threshold de fechamento), o Maestro Caixa cria task urgente no ClickUp com lista priorizada de problemas e acoes corretivas. Nenhum fechamento ocorre sem resolucao dos blocking issues."
    - "[ ] L3: Pagamentos (AP): a Dunna gera a fila de pagamentos aprovados e o dossie de cada pagamento, mas a execucao NUNCA e automatica. Todo pagamento requer aprovacao humana explicita (Controller ou Financeiro, conforme alçada configurada) via task no ClickUp com o botao de aprovacao integrado ao ERP."
    - "[ ] L2: Matches de baixa confianca (score 0.70-0.85): o Aurum sinaliza esses matches no Verification Report para confirmacao do analista antes do Closing Package ser finalizado. Nao bloqueia o processo, mas exige confirmacao explicita de cada match de baixa confianca acima de R$500 (configuravel)."
---

# Classificar Exceptions

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Exceptions |
| **status** | `pending` |
| **responsible_executor** | Iris (Iris — A Classificadora de Exceptions) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe a lista de transacoes sem match e classifica cada exception em um dos tipos pre-definidos no Exception Playbook, com prioridade financeira e acao recomendada. Tipos de exception: TIMING_DIFFERENCE (transacao existe em ambas as fontes mas em periodos diferentes — tipicamente pagamentos em trânsito, cheque/boleto emitido vs. compensado), DUPLICATE_SUSPECT (mesma contraparte, mesmo valor, datas proximas — possivel cobranca/pagamento em duplicidade), AMOUNT_MISMATCH (transacao matched por ID mas valor diverge — desconto nao aplicado, taxa bancaria, juros nao previstos), ORPHAN_BANK (extrato bancario tem debit/credit sem correspondente no ERP — transferencia interna nao registrada, IOF, tarifa bancaria), ORPHAN_ERP (ERP tem lancamento sem correspondente no banco — NF emitida nao paga, boleto nao compensado, lancamento manual erroneo), BILLING_DISCREPANCY (valor cobrado no billing system difere do contrato/proposta — upgrade/downgrade nao processado, prorata incorreta, desconto nao aplicado), DISPUTED_CHARGE (cliente ou fornecedor contesta o lancamento formalmente). Para cada exception: calcula o impacto financeiro, a urgencia (vencimento proximo, blocking para fechamento), e a acao recomendada com o nivel de confianca.

## Input

- Lista de unmatched_transactions do Nexus (com campos normalizados), Exception Playbook calibrado no Deep Dive (regras de classificacao por tipo, thresholds de tolerancia por tipo, acoes pre-autorizadas por tipo e faixa de valor), historico de exceptions anteriores do cliente (para identificar padroes recorrentes e calibrar confianca da classificacao), status de AR aging e AP aging para contexto de urgencia (ex: boleto vencendo em 3 dias vs
- 30 dias)

## Output

- Exception Queue (JSON array: cada exception com exception_id, exception_type, financial_impact_cents, urgency_score [0-10], recommended_action, action_confidence [0-1], auto_resolvable [true/false
- se o Solano pode investigar e resolver sem HITL], hitl_required_reason [preenchido quando auto_resolvable=false], evidence [campos relevantes], related_transactions)
- Exception Summary (totais por tipo, valor total em exceptions, exceptions auto-resolvaveis vs
- HITL, exceptions blocking para fechamento, top-5 por valor financeiro)

## Trigger

Chamado pelo Maestro Caixa imediatamente apos o Matching Report do Nexus. Para modo continuo: chamado a cada ciclo diario para classificar novas exceptions. Tambem pode ser chamado manualmente pelo analista para re-classificar uma exception especifica.

## Knowledge base (o que o executor consulta)

- Exception Playbook (regras de classificacao, thresholds de tolerancia, acoes pre-autorizadas por faixa de valor), historico de exceptions dos ultimos 12 meses com resolucao (para few-shot classification), politica de AP do cliente (prazo padrao de pagamento por fornecedor, limites de aprovacao por valor, politica de desconto), politica de AR (politica de credito, limites de concessao de desconto, regras de cobranca por inadimplencia)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de unmatched_transactions do Nexus (com campos normalizados), Exception Playbook calibrado no Deep Dive (regras d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Exception Queue (JSON array: cada exception com exception_id, exception_type, financial_impact_cents, urgency_score [0-…) e persistir no artefato do squad.
4. Entregar ao critic Aurum 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Exception Queue (JSON array: cada exception com exception_id, exception_type, financial_impact_cents, urgency_score [0-10], recommended_action, action_confiden…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aurum 2 registrado
- [ ] Gate L3 respeitado: Lancamentos contabeis acima do threshold de aprovacao autonoma: qualquer lancamento (de reconciliacao automatica ou de resolucao de excepti…
- [ ] Gate L3 respeitado: Exceptions classificadas como DISPUTED_CHARGE ou BILLING_DISCREPANCY de alto valor: qualquer disputa formal com fornecedor/cliente ou diver…
- [ ] Gate L3 respeitado: Closing Package com veredicto BLOCKED do Aurum: quando o Aurum bloqueia o Closing Package (inconsistencia matematica, violacao de complianc…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Lancamentos contabeis acima do threshold de aprovacao autonoma: qualquer lancamento (de reconciliacao automatica ou de resolucao de exception) acima do valor c… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Exceptions classificadas como DISPUTED_CHARGE ou BILLING_DISCREPANCY de alto valor: qualquer disputa formal com fornecedor/cliente ou divergencia de billing ac… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Closing Package com veredicto BLOCKED do Aurum: quando o Aurum bloqueia o Closing Package (inconsistencia matematica, violacao de compliance, exceptions acima… | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Pagamentos (AP): a Dunna gera a fila de pagamentos aprovados e o dossie de cada pagamento, mas a execucao NUNCA e automatica. Todo pagamento requer aprovacao h… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Matches de baixa confianca (score 0.70-0.85): o Aurum sinaliza esses matches no Verification Report para confirmacao do analista antes do Closing Package ser f… | BLOQUEIA até decisão humana |
| VETO-006 | L2 — Comunicacoes de cobranca (AR): a Dunna prepara os templates de cobranca mas a aprovacao depende do tier: para clientes estrategicos (acima de determinado ARR o… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — Revisao do Exception Playbook trimestral: analista financeiro revisa as regras de classificacao e os thresholds de tolerancia calibrados pelo squad, podendo aj… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Aurum 2 | BLOQUEIA entrega |

## Handoff

- **to:** Solano
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
