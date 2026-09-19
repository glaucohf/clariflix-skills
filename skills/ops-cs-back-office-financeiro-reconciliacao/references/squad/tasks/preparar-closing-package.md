---
task: ledger()
responsavel: "Ledger"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Matching Report final do Nexus (matched_transactions com audit trail), Findings Reports do Solano para exceptions resolvidas (lancamentos gerados com confidence > threshold), Exception Queue residual do Iris (exceptions HITL L3 ainda abertas com valor e classificacao), ERP journal entry template do cliente (formato exato para importacao), saldos iniciais por conta bancaria e por conta contabil no ERP, periodo de fechamento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Closing Package (documento estruturado): (1) Reconciliation Statement por conta bancaria (saldo extrato vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "saldo ERP + itens conciliantes + saldo ajustado), (2) Journal Entry Batch (arquivo de lancamentos no formato do ERP"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "pronto para importacao), (3) Exception Status Report (exceptions resolvidas automaticamente vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "pendentes HITL, valor total em aberto, impacto estimado no resultado do periodo), (4) Audit Trail completo (cada lancamento rastreado ate a transacao de origem + regra de matching + agente responsavel + timestamp), (5) Closing Readiness Score (0-100: % do volume reconciliado x % de exceptions resolvidas x impacto das exceptions abertas no fechamento)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "O Closing Package vai para o Verificador Aurum antes de ser enviado para o Controller"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Maestro Caixa apos todos os Findings Reports do Solano serem entregues (ou timeout de SLA atingido para exceptions nao concluidas). Tambem pode ser chamado manualmente para gerar um Clos…"
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

# Preparar Closing Package

**Task ID:** `ledger()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Preparar Closing Package |
| **status** | `pending` |
| **responsible_executor** | Ledger (Ledger — O Preparador do Closing Package) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Consolida todos os resultados do ciclo de reconciliacao em um Closing Package estruturado e pronto para aprovacao do Controller/CFO. Recebe: (1) matched_transactions do Nexus — gera os lancamentos de baixa/quitacao automaticos no formato do ERP, (2) Findings Reports do Solano para exceptions auto-resolvidas — gera os lancamentos de ajuste correspondentes (diferenca de centavos, tarifa bancaria, item em transito), (3) lista de exceptions ainda abertas (HITL L3 pendente) — inclui no Closing Package como itens pendentes com valor e impacto no fechamento. Calcula o impacto total das exceptions abertas no resultado do periodo. Gera os lancamentos no formato exato do ERP do cliente (SAP BAPI, Omie API, Conta Azul API) — pronto para importacao ou aprovacao click-to-approve. Tambem gera o Reconciliation Statement: demonstrativo de conciliacao bancaria no formato padrao (saldo inicial + transacoes + ajustes = saldo final, por conta bancaria).

## Input

- Matching Report final do Nexus (matched_transactions com audit trail), Findings Reports do Solano para exceptions resolvidas (lancamentos gerados com confidence > threshold), Exception Queue residual do Iris (exceptions HITL L3 ainda abertas com valor e classificacao), ERP journal entry template do cliente (formato exato para importacao), saldos iniciais por conta bancaria e por conta contabil no ERP, periodo de fechamento

## Output

- Closing Package (documento estruturado): (1) Reconciliation Statement por conta bancaria (saldo extrato vs
- saldo ERP + itens conciliantes + saldo ajustado), (2) Journal Entry Batch (arquivo de lancamentos no formato do ERP
- pronto para importacao), (3) Exception Status Report (exceptions resolvidas automaticamente vs
- pendentes HITL, valor total em aberto, impacto estimado no resultado do periodo), (4) Audit Trail completo (cada lancamento rastreado ate a transacao de origem + regra de matching + agente responsavel + timestamp), (5) Closing Readiness Score (0-100: % do volume reconciliado x % de exceptions resolvidas x impacto das exceptions abertas no fechamento)
- O Closing Package vai para o Verificador Aurum antes de ser enviado para o Controller

## Trigger

Chamado pelo Maestro Caixa apos todos os Findings Reports do Solano serem entregues (ou timeout de SLA atingido para exceptions nao concluidas). Tambem pode ser chamado manualmente para gerar um Closing Package parcial com status em tempo real do progresso do ciclo.

## Knowledge base (o que o executor consulta)

- ERP journal entry templates por tipo de lancamento (quitacao de AP, baixa de AR, ajuste de diferenca, lancamento de tarifa bancaria, item em transito), plano de contas do cliente (codigos contabeis por tipo de transacao), politica de fechamento (qual o % minimo de reconciliacao aceito para fechar o periodo, quais contas sao blocking), formato de Reconciliation Statement aceito pela auditoria do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Matching Report final do Nexus (matched_transactions com audit trail), Findings Reports do Solano para exceptions resol…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Closing Package (documento estruturado): (1) Reconciliation Statement por conta bancaria (saldo extrato vs) e persistir no artefato do squad.
4. Entregar ao critic Aurum 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Closing Package (documento estruturado): (1) Reconciliation Statement por conta bancaria (saldo extrato vs
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

- **to:** Aurum
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
