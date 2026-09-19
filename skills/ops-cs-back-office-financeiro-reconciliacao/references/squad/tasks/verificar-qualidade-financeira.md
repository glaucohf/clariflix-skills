---
task: aurum()
responsavel: "Aurum"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Closing Package completo do Ledger (Reconciliation Statement, Journal Entry Batch, Exception Status Report, Audit Trail, Closing Readiness Score), low_confidence_matches do Nexus (score 0.70-0.85 para revisao), politica de aprovacao do cliente (limites por tipo de lancamento e por valor, lista de fornecedores/clientes com restricao), regras de compliance financeiro (ex: nao pagar fornecedor com CNPJ irregular, nao liberar credito acima de X sem aprovacao do CFO), threshold de fechamento (qual % de reconciliacao e suficiente para aprovar o fechamento)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Verification Report (JSON: verdict [APPROVED | APPROVED_WITH_FLAGS | BLOCKED], checks_passed [lista de dimensoes aprovadas com evidencias], checks_failed [lista de problemas com severidade e descricao], flags [itens de atencao em APPROVED_WITH_FLAGS], low_confidence_matches_review [lista de matches que precisam de confirmacao humana com contexto], compliance_violations [lancamentos que violam politica], closing_readiness_score_final, recommended_controller_actions [lista de acoes que o Controller deve tomar antes de aprovar])"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Em BLOCKED, gera lista priorizada de problemas com acao corretiva sugerida"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Maestro Caixa SEMPRE apos o Closing Package ser gerado pelo Ledger. Nao ha bypass — todo Closing Package passa pelo Aurum. Tambem chamado de forma continua para validar cada lancamento i…"
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

# Verificar Qualidade Financeira

**Task ID:** `aurum()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Qualidade Financeira |
| **status** | `pending` |
| **responsible_executor** | Aurum (Aurum — O Verificador de Qualidade Financeira) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Critic/Verifier do squad. Gate de qualidade obrigatorio antes de qualquer Closing Package chegar ao Controller/CFO e antes de qualquer lancamento contabil ser importado no ERP. Valida 5 dimensoes: (1) Completude — todas as fontes foram processadas? Ha transacoes faltando no Canonical Transaction Set? (2) Consistencia matematica — o saldo final do Reconciliation Statement fecha? A soma dos lancamentos do Journal Entry Batch corresponde ao delta esperado? (3) Qualidade do matching — low_confidence_matches (score 0.70-0.85) foram revisados? Ha matches com evidencias frageis que precisam de confirmacao humana? (4) Exposicao de exceptions — o valor total em exceptions abertas esta dentro do threshold de tolerancia para fechamento? Exceptions de alto valor ou alto risco estao adequadamente escaladas para HITL L3? (5) Compliance de politica — todos os lancamentos acima do limite de aprovacao autonoma estao sinalizados para HITL? Ha algum lancamento que fere a politica de AP/AR (ex: pagamento a fornecedor bloqueado, liberacao de credito acima do limite)? Emite veredicto APPROVED (Closing Package vai para Controller), APPROVED_WITH_FLAGS (aprovado mas com items de atencao listados), ou BLOCKED (Closing Package nao pode ser enviado — retorna ao Maestro Caixa com lista de problemas).

## Input

- Closing Package completo do Ledger (Reconciliation Statement, Journal Entry Batch, Exception Status Report, Audit Trail, Closing Readiness Score), low_confidence_matches do Nexus (score 0.70-0.85 para revisao), politica de aprovacao do cliente (limites por tipo de lancamento e por valor, lista de fornecedores/clientes com restricao), regras de compliance financeiro (ex: nao pagar fornecedor com CNPJ irregular, nao liberar credito acima de X sem aprovacao do CFO), threshold de fechamento (qual % de reconciliacao e suficiente para aprovar o fechamento)

## Output

- Verification Report (JSON: verdict [APPROVED | APPROVED_WITH_FLAGS | BLOCKED], checks_passed [lista de dimensoes aprovadas com evidencias], checks_failed [lista de problemas com severidade e descricao], flags [itens de atencao em APPROVED_WITH_FLAGS], low_confidence_matches_review [lista de matches que precisam de confirmacao humana com contexto], compliance_violations [lancamentos que violam politica], closing_readiness_score_final, recommended_controller_actions [lista de acoes que o Controller deve tomar antes de aprovar])
- Em BLOCKED, gera lista priorizada de problemas com acao corretiva sugerida

## Trigger

Chamado pelo Maestro Caixa SEMPRE apos o Closing Package ser gerado pelo Ledger. Nao ha bypass — todo Closing Package passa pelo Aurum. Tambem chamado de forma continua para validar cada lancamento individual gerado pelo Solano antes de ser incluido no Closing Package (validacao incremental para exceptions de alto valor).

## Knowledge base (o que o executor consulta)

- Politica de aprovacao do cliente por tipo de lancamento e faixa de valor, lista de fornecedores/clientes com restricoes (CNPJ bloqueado, cliente inadimplente, fornecedor em disputa), regras de compliance (legislacao fiscal relevante, politicas internas de AP/AR), historico de rejeicoes anteriores do Controller (para identificar padroes de qualidade exigidos), threshold de fechamento por conta bancaria e por conta contabil, formulas de validacao matematica do Reconciliation Statement

## Action Items

1. Confirmar o gatilho e carregar a entrada (Closing Package completo do Ledger (Reconciliation Statement, Journal Entry Batch, Exception Status Report, Audit Trail…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Verification Report (JSON: verdict [APPROVED | APPROVED_WITH_FLAGS | BLOCKED], checks_passed [lista de dimensoes aprova…) e persistir no artefato do squad.
4. Entregar ao critic Aurum 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Verification Report (JSON: verdict [APPROVED | APPROVED_WITH_FLAGS | BLOCKED], checks_passed [lista de dimensoes aprovadas com evidencias], checks_failed [list…
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

- **to:** Dunna
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
