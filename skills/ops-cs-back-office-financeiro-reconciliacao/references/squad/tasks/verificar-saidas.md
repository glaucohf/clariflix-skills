---
task: aurum2Verificar()
responsavel: "Aurum 2"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] L3: Lancamentos contabeis acima do threshold de aprovacao autonoma: qualquer lancamento (de reconciliacao automatica ou de resolucao de exception) acima do valor configurado (ex: R$10.000 por lancamento, configuravel por cliente) requer aprovacao explicita do Controller via task no ClickUp. O Ledger gera o lancamento formatado e o Aurum escala para HITL com contexto completo (origem, evidencia, impact no resultado)."
    - "[ ] L3: Exceptions classificadas como DISPUTED_CHARGE ou BILLING_DISCREPANCY de alto valor: qualquer disputa formal com fornecedor/cliente ou divergencia de billing acima do threshold configurado requer decisao humana. O Solano prepara o dossie de investigacao completo (evidencias, historico, opcoes de resolucao com pros/contras) para o Controller tomar a decisao."
    - "[ ] L3: Closing Package com veredicto BLOCKED do Aurum: quando o Aurum bloqueia o Closing Package (inconsistencia matematica, violacao de compliance, exceptions acima do threshold de fechamento), o Maestro Caixa cria task urgente no ClickUp com lista priorizada de problemas e acoes corretivas. Nenhum fechamento ocorre sem resolucao dos blocking issues."
    - "[ ] L3: Pagamentos (AP): a Dunna gera a fila de pagamentos aprovados e o dossie de cada pagamento, mas a execucao NUNCA e automatica. Todo pagamento requer aprovacao humana explicita (Controller ou Financeiro, conforme alçada configurada) via task no ClickUp com o botao de aprovacao integrado ao ERP."
    - "[ ] L2: Matches de baixa confianca (score 0.70-0.85): o Aurum sinaliza esses matches no Verification Report para confirmacao do analista antes do Closing Package ser finalizado. Nao bloqueia o processo, mas exige confirmacao explicita de cada match de baixa confianca acima de R$500 (configuravel)."
---

# Verificar Saídas do Back-Office Financeiro

**Task ID:** `aurum2Verificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Back-Office Financeiro |
| **status** | `pending` |
| **responsible_executor** | Aurum 2 (Aurum — O Verificador de Qualidade Financeira) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Aurum — O Verificador de Qualidade Financeira — Critic/Verifier do squad. Gate obrigatorio de 5 dimensoes (completude, consistencia matematica, qualidade do matching, exposicao de exceptions, compliance de politica) antes de qualquer Closing Package ser enviado ao Controller/CFO. Opera em modo adversarial: assume que o Closing Package tem erros ate provar o contrario. Nao e possivel bypassar o Aurum — qualquer lancamento acima do threshold de valor autonoma e qualquer Closing Package passa obrigatoriamente por ele. Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 5%. Taxa alvo de falsos positivos (APPROVED quando tinha problema real): < 0.1% (erro financeiro tem custo alto). Tambem executa auditoria retroativa mensal de 10% dos fechamentos aprovados para detectar deriva de qualidade.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- O Verificador de Qualidade Financeira
- Critic/Verifier do squad
- Gate obrigatorio de 5 dimensoes (completude, consistencia matematica, qualidade do matching, exposicao de exceptions, compliance de politica) antes de qualquer Closing Package ser enviado ao Controller/CFO
- Opera em modo adversarial: assume que o Closing Package tem erros ate provar o contrario
- Nao e possivel bypassar o Aurum
- qualquer lancamento acima do threshold de valor autonoma e qualquer Closing Package passa obrigatoriamente por ele
- Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 5%
- Taxa alvo de falsos positivos (APPROVED quando tinha problema real): < 0.1% (erro financeiro tem custo alto)
- Tambem executa auditoria retroativa mensal de 10% dos fechamentos aprovados para detectar deriva de qualidade

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Maestro Caixa para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Maestro Caixa
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
