---
task: dunna()
responsavel: "Dunna"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "AR aging report atualizado (extraido do ERP via Fluxo), AP aging report atualizado, dados de health score dos clientes (ChurnZero/Custify ou similar, se disponivel), historico de comunicacoes de cobranca enviadas (para nao duplicar), politica de cobranca do cliente (sequencia, canais, tom por tier de cliente, threshold para escalonamento para cobranca juridica), dados de CRM sobre status da conta do cliente (plano, ultima interacao, open tickets), configuracao de early payment discounts por fornecedor"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "AP Action Queue (JSON: pagamentos vencendo em 5 dias com status de aprovacao, pagamentos bloqueados por aprovacao pendente, oportunidades de early payment discount com ROI calculado, duplicidades detectadas na fila de pagamento)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "AR Action Queue (JSON: aging analysis atualizada por cliente, clientes que entram na sequencia de cobranca hoje com template de mensagem gerado, clientes em risco de inadimplência com score e evidencia, titulos que atingiram threshold para escalonamento juridico)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Ambas as filas vao para HITL L3 para execucao de pagamentos e para HITL L2/L3 para aprovacao de comunicacoes de cobranca conforme threshold configurado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diario (07h00) para geracao das filas AP e AR do dia + chamado pelo Maestro Caixa ao inicio de cada ciclo de fechamento para incluir o status de AP-AR no Closing Package + alerta imediato para t…"
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

# Gerar Aging Analysis Automática

**Task ID:** `dunna()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Aging Analysis Automática |
| **status** | `pending` |
| **responsible_executor** | Dunna (Dunna — A Gestora de AP-AR e Cobranca) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Opera em paralelo ao ciclo de reconciliacao, focada em acoes proativas de AP (contas a pagar) e AR (contas a receber). No AP: monitora vencimentos proximos (proximos 5, 10, 30 dias), verifica se ha aprovacao pendente para pagamentos acima do threshold, identifica oportunidades de desconto por pagamento antecipado (early payment discount), e sinaliza duplicidades na fila de pagamento. No AR: gera a aging analysis automatica (0-30, 31-60, 61-90, 90+ dias de vencimento), identifica clientes em risco de inadimplência baseado em sinais do CRM (uso do produto, tickets de suporte, sinais de churn), e prepara a sequencia de cobranca multicanal para titulos vencidos (email D+1, WhatsApp D+5, lembrete formal D+15, escalonamento para cobranca D+30) de acordo com a politica de cobranca configurada. Nao executa pagamentos (L3 obrigatorio) e nao envia comunicacoes de cobranca sem aprovacao (L2 para baixo valor, L3 para alto valor ou disputa).

## Input

- AR aging report atualizado (extraido do ERP via Fluxo), AP aging report atualizado, dados de health score dos clientes (ChurnZero/Custify ou similar, se disponivel), historico de comunicacoes de cobranca enviadas (para nao duplicar), politica de cobranca do cliente (sequencia, canais, tom por tier de cliente, threshold para escalonamento para cobranca juridica), dados de CRM sobre status da conta do cliente (plano, ultima interacao, open tickets), configuracao de early payment discounts por fornecedor

## Output

- AP Action Queue (JSON: pagamentos vencendo em 5 dias com status de aprovacao, pagamentos bloqueados por aprovacao pendente, oportunidades de early payment discount com ROI calculado, duplicidades detectadas na fila de pagamento)
- AR Action Queue (JSON: aging analysis atualizada por cliente, clientes que entram na sequencia de cobranca hoje com template de mensagem gerado, clientes em risco de inadimplência com score e evidencia, titulos que atingiram threshold para escalonamento juridico)
- Ambas as filas vao para HITL L3 para execucao de pagamentos e para HITL L2/L3 para aprovacao de comunicacoes de cobranca conforme threshold configurado

## Trigger

Cron diario (07h00) para geracao das filas AP e AR do dia + chamado pelo Maestro Caixa ao inicio de cada ciclo de fechamento para incluir o status de AP-AR no Closing Package + alerta imediato para titulos vencendo em menos de 24h que ainda nao tem aprovacao de pagamento.

## Knowledge base (o que o executor consulta)

- Politica de AP do cliente (prazos por fornecedor, aprovadores por faixa de valor, regras de desconto), politica de AR e cobranca (sequencia, canais, tom, thresholds por tier de cliente, momento de escalonamento juridico), templates de comunicacao de cobranca por etapa e por canal (email, WhatsApp), health scores dos clientes se disponivel (ChurnZero/Custify), historico de comunicacoes de cobranca enviadas (para controle de sequencia), dados de CRM sobre relacionamento com o cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (AR aging report atualizado (extraido do ERP via Fluxo), AP aging report atualizado, dados de health score dos clientes…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (AP Action Queue (JSON: pagamentos vencendo em 5 dias com status de aprovacao, pagamentos bloqueados por aprovacao pende…) e persistir no artefato do squad.
4. Entregar ao critic Aurum 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: AP Action Queue (JSON: pagamentos vencendo em 5 dias com status de aprovacao, pagamentos bloqueados por aprovacao pendente, oportunidades de early payment disc…
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

- **to:** Aurum 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
