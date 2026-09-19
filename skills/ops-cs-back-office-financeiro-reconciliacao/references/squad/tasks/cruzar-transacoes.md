---
task: nexus()
responsavel: "Nexus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Canonical Transaction Set do Fluxo (transacoes das multiplas fontes do periodo), matching_rules.json (regras calibradas pelo Deep Dive: regras exact, fuzzy e probabilistic com thresholds por tipo de transacao e por par de fontes), historico de matches anteriores (para usar como ancora do modelo probabilistico), embeddings de descricoes de transacoes anteriores matched (para similarity search)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Matching Report (JSON: matched_transactions [lista de pares com match_type, confidence_score, match_evidence], unmatched_transactions [lista de transacoes sem par, por fonte], low_confidence_matches [matched mas score 0.70-0.85, flagged para revisao do Aurum], match_summary [% matched por fonte, valor total matched, valor total em exceptions])"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Cada par matched inclui audit trail completo: qual regra disparou, qual o confidence score, quais campos foram comparados e com qual similaridade"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: conforme especificação"
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

# Cruzar Transações

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Cruzar Transações |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — O Matcher de Transacoes) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Aplica as regras de matching calibradas para cruzar transacoes entre fontes (banco vs. ERP, billing vs. banco, AP vs. NF-e). Opera em 3 camadas de matching em cascata, do mais preciso ao mais probabilistico: (1) Exact Match — transaction_id ou invoice_number identico entre as fontes, mesmo valor exato, (2) Fuzzy Match — mesmo counterparty_id + valor dentro da tolerancia configurada (ex: +/- R$0,05 para diferenca de centavos ou taxa bancaria) + janela temporal de +/- N dias configuravel por tipo de transacao, (3) Probabilistic Match — scoring multi-fator (counterparty similarity 0-1 + valor similarity 0-1 + date proximity 0-1 + description similarity via embedding 0-1) com threshold de confianca configuravel (default: 0.85 para match automatico, 0.70-0.85 para match com flag de revisao). Transacoes com score < 0.70 vao automaticamente para a fila de exceptions do Iris. Transacoes matched com score 0.70-0.85 vao para match confirmado com flag low_confidence para o Verificador Aurum revisar.

## Input

- Canonical Transaction Set do Fluxo (transacoes das multiplas fontes do periodo), matching_rules.json (regras calibradas pelo Deep Dive: regras exact, fuzzy e probabilistic com thresholds por tipo de transacao e por par de fontes), historico de matches anteriores (para usar como ancora do modelo probabilistico), embeddings de descricoes de transacoes anteriores matched (para similarity search)

## Output

- Matching Report (JSON: matched_transactions [lista de pares com match_type, confidence_score, match_evidence], unmatched_transactions [lista de transacoes sem par, por fonte], low_confidence_matches [matched mas score 0.70-0.85, flagged para revisao do Aurum], match_summary [% matched por fonte, valor total matched, valor total em exceptions])
- Cada par matched inclui audit trail completo: qual regra disparou, qual o confidence score, quais campos foram comparados e com qual similaridade

## Trigger

—

## Action Items

1. Confirmar o gatilho e carregar a entrada (Canonical Transaction Set do Fluxo (transacoes das multiplas fontes do periodo), matching_rules.json (regras calibradas…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Matching Report (JSON: matched_transactions [lista de pares com match_type, confidence_score, match_evidence], unmatche…) e persistir no artefato do squad.
4. Entregar ao critic Aurum 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Matching Report (JSON: matched_transactions [lista de pares com match_type, confidence_score, match_evidence], unmatched_transactions [lista de transacoes sem…
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

- **to:** Iris
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
