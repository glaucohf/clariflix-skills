# Checklist do critic Aurum 2 — Back-Office Financeiro

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Aurum — O Verificador de Qualidade Financeira — Critic/Verifier do squad. Gate obrigatorio de 5 dimensoes (completude, consistencia matematica, qualidade do matching, exposicao de exceptions, compliance de politica) antes de qualquer Closing Package ser enviado ao Controller/CFO. Opera em modo adversarial: assume que o Closing Package tem erros ate provar o contrario. Nao e possivel bypassar o Aurum — qualquer lancamento acima do threshold de valor autonoma e qualquer Closing Package passa obrigatoriamente por ele. Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 5%. Taxa alvo de falsos positivos (APPROVED quando tinha problema real): < 0.1% (erro financeiro tem custo alto). Tambem executa auditoria retroativa mensal de 10% dos fechamentos aprovados para detectar deriva de qualidade.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Verificador de Qualidade Financeira
- [ ] **C02** — Critic/Verifier do squad
- [ ] **C03** — Gate obrigatorio de 5 dimensoes (completude, consistencia matematica, qualidade do matching, exposicao de exceptions, compliance de politica) antes de qualquer Closing Package ser enviado ao Controller/CFO
- [ ] **C04** — Opera em modo adversarial: assume que o Closing Package tem erros ate provar o contrario
- [ ] **C05** — Nao e possivel bypassar o Aurum
- [ ] **C06** — qualquer lancamento acima do threshold de valor autonoma e qualquer Closing Package passa obrigatoriamente por ele
- [ ] **C07** — Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 5%
- [ ] **C08** — Taxa alvo de falsos positivos (APPROVED quando tinha problema real): < 0.1% (erro financeiro tem custo alto)
- [ ] **C09** — Tambem executa auditoria retroativa mensal de 10% dos fechamentos aprovados para detectar deriva de qualidade

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Lancamentos contabeis acima do threshold de aprovacao autonoma: qualquer lancamento (de reconciliacao automatica ou de resolucao de exception) acima do valor configurado (ex: R$10.000 por lancamento, configuravel por cliente) requer aprovacao explicita do Controller via task no ClickUp. O Ledger gera o lancamento formatado e o Aurum escala para HITL com contexto completo (origem, evidencia, impact no resultado).
- [ ] **L3** — Exceptions classificadas como DISPUTED_CHARGE ou BILLING_DISCREPANCY de alto valor: qualquer disputa formal com fornecedor/cliente ou divergencia de billing acima do threshold configurado requer decisao humana. O Solano prepara o dossie de investigacao completo (evidencias, historico, opcoes de resolucao com pros/contras) para o Controller tomar a decisao.
- [ ] **L3** — Closing Package com veredicto BLOCKED do Aurum: quando o Aurum bloqueia o Closing Package (inconsistencia matematica, violacao de compliance, exceptions acima do threshold de fechamento), o Maestro Caixa cria task urgente no ClickUp com lista priorizada de problemas e acoes corretivas. Nenhum fechamento ocorre sem resolucao dos blocking issues.
- [ ] **L3** — Pagamentos (AP): a Dunna gera a fila de pagamentos aprovados e o dossie de cada pagamento, mas a execucao NUNCA e automatica. Todo pagamento requer aprovacao humana explicita (Controller ou Financeiro, conforme alçada configurada) via task no ClickUp com o botao de aprovacao integrado ao ERP.
- [ ] **L2** — Matches de baixa confianca (score 0.70-0.85): o Aurum sinaliza esses matches no Verification Report para confirmacao do analista antes do Closing Package ser finalizado. Nao bloqueia o processo, mas exige confirmacao explicita de cada match de baixa confianca acima de R$500 (configuravel).
- [ ] **L2** — Comunicacoes de cobranca (AR): a Dunna prepara os templates de cobranca mas a aprovacao depende do tier: para clientes estrategicos (acima de determinado ARR ou marcados como VIP no CRM), toda comunicacao requer aprovacao humana antes do envio. Para clientes standard, a sequencia pode ser aprovada em batch semanalmente.
- [ ] **L1** — Revisao do Exception Playbook trimestral: analista financeiro revisa as regras de classificacao e os thresholds de tolerancia calibrados pelo squad, podendo ajustar parametros. Nao bloqueia operacao continua, mas garante que o playbook evolui com as mudancas no negocio do cliente.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
