---
task: solano()
responsavel: "Solano"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Exception Queue do Iris (apenas exceptions com auto_resolvable=true), acesso de leitura ao ERP (historico de lancamentos da contraparte, NFs emitidas, contratos), acesso de leitura ao billing system (historico de assinaturas, mudancas de plano, prorata, descontos aplicados), acesso de leitura ao banco (extratos dos ultimos 90 dias para busca de transacoes similares), documents.json (NFs escaneadas/XML, contratos, propostas comerciais indexados por contraparte), tolerance_config.json (thresholds financeiros pre-autorizados por tipo: ex tarifas bancarias < R$50 sao registradas automaticamente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Findings Report por exception (JSON: exception_id, investigation_steps [lista de verificacoes realizadas com evidencias], root_cause [explicacao em linguagem natural], recommended_resolution [acao especifica: registrar como tarifa bancaria / reconciliar com item em transito / estornar duplicata / solicitar nota de credito], resolution_confidence [0-1], resolution_requires_approval [true se valor > threshold ou impacto > politica], evidence_attachments [links para documentos relevantes no storage])"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para exceptions com resolution_confidence > 0.90 e valor < threshold: gera o lancamento contabil diretamente no formato do ERP para aprovacao final do Aurum"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Maestro Caixa apos a Exception Queue do Iris, para o subset de exceptions auto_resolvable=true. Opera de forma assíncrona (investiga exceptions em paralelo, reporta cada uma conforme con…"
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

# Investigar Exceptions Automáticamente

**Task ID:** `solano()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Investigar Exceptions Automáticamente |
| **status** | `pending` |
| **responsible_executor** | Solano (Solano — O Investigador de Exceptions) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa a investigacao automatica das exceptions classificadas como auto_resolvable=true pelo Iris. Para cada tipo, aplica o playbook de investigacao correspondente: (1) TIMING_DIFFERENCE — verifica se a transacao aparece no extrato do proximo periodo ou no historico de itens em transito do ERP, propoe reconciliacao com ajuste de periodo ou item em transito, (2) DUPLICATE_SUSPECT — consulta historico de pagamentos/cobranças para a mesma contraparte nos ultimos 30 dias, verifica se ambas as transacoes tem comprovantes distintos, propoe estorno da duplicata ou confirmacao de que sao transacoes legitimas distintas, (3) AMOUNT_MISMATCH — busca o documento de origem (NF-e, contrato, proposta) para verificar o valor correto, identifica a diferenca como taxa bancaria (tolerancia automatica < R$X configuravel) ou erro genuino, (4) ORPHAN_BANK — classifica como tarifa bancaria (IOF, TED, manutencao de conta — registro automatico) ou transacao desconhecida que precisa de identificacao humana, (5) BILLING_DISCREPANCY — cruza com o contrato vigente e o historico de mudancas de plano no CRM/billing system para identificar a causa da divergencia. Para cada exception investigada, produz um Findings Report com evidencias e acao recomendada + nivel de confianca.

## Input

- Exception Queue do Iris (apenas exceptions com auto_resolvable=true), acesso de leitura ao ERP (historico de lancamentos da contraparte, NFs emitidas, contratos), acesso de leitura ao billing system (historico de assinaturas, mudancas de plano, prorata, descontos aplicados), acesso de leitura ao banco (extratos dos ultimos 90 dias para busca de transacoes similares), documents.json (NFs escaneadas/XML, contratos, propostas comerciais indexados por contraparte), tolerance_config.json (thresholds financeiros pre-autorizados por tipo: ex tarifas bancarias < R$50 sao registradas automaticamente)

## Output

- Findings Report por exception (JSON: exception_id, investigation_steps [lista de verificacoes realizadas com evidencias], root_cause [explicacao em linguagem natural], recommended_resolution [acao especifica: registrar como tarifa bancaria / reconciliar com item em transito / estornar duplicata / solicitar nota de credito], resolution_confidence [0-1], resolution_requires_approval [true se valor > threshold ou impacto > politica], evidence_attachments [links para documentos relevantes no storage])
- Para exceptions com resolution_confidence > 0.90 e valor < threshold: gera o lancamento contabil diretamente no formato do ERP para aprovacao final do Aurum

## Trigger

Chamado pelo Maestro Caixa apos a Exception Queue do Iris, para o subset de exceptions auto_resolvable=true. Opera de forma assíncrona (investiga exceptions em paralelo, reporta cada uma conforme conclui). SLA interno: exceptions de alta urgencia (urgency_score >= 8) em < 30 minutos, demais em < 2h.

## Knowledge base (o que o executor consulta)

- Exception Playbook com investigacao step-by-step por tipo, acesso de leitura ao ERP (SAP/Omie/Conta Azul), historico de transacoes por contraparte (12 meses), contratos e NFs indexados por contraparte, tolerance_config.json (thresholds pre-autorizados por tipo de exception e por faixa de valor), politica de AP/AR do cliente (prazos, limites, aprovadores por faixa de valor), historico de investigacoes anteriores para exceptions similares (few-shot para situacoes recorrentes)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Exception Queue do Iris (apenas exceptions com auto_resolvable=true), acesso de leitura ao ERP (historico de lancamento…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Findings Report por exception (JSON: exception_id, investigation_steps [lista de verificacoes realizadas com evidencias…) e persistir no artefato do squad.
4. Entregar ao critic Aurum 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Findings Report por exception (JSON: exception_id, investigation_steps [lista de verificacoes realizadas com evidencias], root_cause [explicacao em linguagem n…
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

- **to:** Ledger
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
