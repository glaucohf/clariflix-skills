---
task: maestroCaixaPipeline()
responsavel: "Maestro Caixa"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Closing Package no ClickUp como prova de trabalho verificavel por ciclo de fechamento: (1) Reconciliation Statement por conta bancaria (saldo extrato vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "saldo ERP + itens conciliantes + saldo ajustado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "formato auditavel), (2) Journal Entry Batch no formato do ERP do cliente (pronto para importacao click-to-approve), (3) Exception Log completo (cada exception com tipo, valor, investigacao do Solano, resolucao aplicada ou pendente, audit trail), (4) Closing Readiness Score com breakdown por dimensao, (5) Verification Report do Aurum (veredicto e flags), (6) AP-AR Status Report da Dunna (pagamentos pendentes de aprovacao, cobrancas enviadas na semana, titulos em risco)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Cada lancamento rastreavel de volta a transacao de origem via audit trail imutavel"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp por exception HITL L3 com dossie de investigacao completo e botao de aprovacao integrado ao ERP"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestra o ciclo completo de reconciliacao: da coleta de dados ate o Closing Package aprovado. Mantem o estado de cada ciclo de fechamento (qual periodo, quais fontes ja foram processadas, quantas t…"
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

# Orquestrar Pipeline do Back-Office Financeiro

**Task ID:** `maestroCaixaPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Back-Office Financeiro |
| **status** | `pending` |
| **responsible_executor** | Maestro Caixa (Maestro Caixa — O Controlador do Ciclo de Fechamento) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestra o ciclo completo de reconciliacao: da coleta de dados ate o Closing Package aprovado. Mantem o estado de cada ciclo de fechamento (qual periodo, quais fontes ja foram processadas, quantas transacoes pendentes, exceptions abertas, deadline do fechamento). Prioriza exceptions pela combinacao de valor financeiro x urgencia x tipo. Delega para cada worker na sequencia correta e garante que nenhuma transacao seja perdida entre as etapas. Em modo ciclo de fechamento (ativado manualmente ou por cron mensal), orquestra o fluxo completo. Em modo continuo (para empresas que reconciliam diariamente), monitora o fluxo incremental e escala exceptions criticas imediatamente. Nunca aprova lancamentos contabeis diretamente — toda aprovacao final e do Controller/CFO via HITL.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Closing Package no ClickUp como prova de trabalho verificavel por ciclo de fechamento: (1) Reconciliation Statement por conta bancaria (saldo extrato vs
- saldo ERP + itens conciliantes + saldo ajustado
- formato auditavel), (2) Journal Entry Batch no formato do ERP do cliente (pronto para importacao click-to-approve), (3) Exception Log completo (cada exception com tipo, valor, investigacao do Solano, resolucao aplicada ou pendente, audit trail), (4) Closing Readiness Score com breakdown por dimensao, (5) Verification Report do Aurum (veredicto e flags), (6) AP-AR Status Report da Dunna (pagamentos pendentes de aprovacao, cobrancas enviadas na semana, titulos em risco)
- Cada lancamento rastreavel de volta a transacao de origem via audit trail imutavel
- Task no ClickUp por exception HITL L3 com dossie de investigacao completo e botao de aprovacao integrado ao ERP

## Trigger

Orquestra o ciclo completo de reconciliacao: da coleta de dados ate o Closing Package aprovado. Mantem o estado de cada ciclo de fechamento (qual periodo, quais fontes ja foram processadas, quantas transacoes pendentes, exceptions abertas, deadline do fechamento). Prioriza exceptions pela combinacao de valor financeiro x urgencia x tipo. Delega para cada worker na sequencia correta e garante que nenhuma transacao seja perdida entre as etapas. Em modo ciclo de fechamento (ativado manualmente ou por cron mensal), orquestra o fluxo completo. Em modo continuo (para empresas que reconciliam diariamente), monitora o fluxo incremental e escala exceptions criticas imediatamente. Nunca aprova lancamentos contabeis diretamente — toda aprovacao final e do Controller/CFO via HITL.

## Knowledge base (o que o executor consulta)

- ERP (SAP / Omie / Conta Azul / Totvs / Netsuite)
- fonte primaria de lancamentos contabeis: API de leitura para extrair transacoes, NFs, contratos, saldos de AP e AR
- API de escrita para importacao de journal entries aprovados (somente apos HITL)
- acesso ao plano de contas
- Bancos via Open Finance / OFX / API Bancaria (Bradesco, Itau, Banco do Brasil, Nubank Business, BTG, Inter)
- extrato bancario automatizado diario ou mensal
- integracao via Open Finance API (BACEN) para bancos disponiveis ou exportacao OFX para os demais
- Billing Systems (Stripe / Chargebee / Vindi / Iugu / Hotmart / Eduzz)
- historico de cobranças, assinaturas, mudancas de plano, descontos, estornos, webhooks de eventos de pagamento em tempo real
- ClickUp (Brain2 / Super Agents / Autopilot Agents + MCP)
- hub de tasks e prova de trabalho: task por excecao HITL L3, Closing Package como task de aprovacao click-to-approve, filas de AP e AR como tasks com due date, integracao com AIOX espelhando o workflow de aprovacao
- notificacoes em tempo real: alerta de Closing Package pronto para aprovacao, exceptions de alto valor detectadas, pagamentos vencendo hoje sem aprovacao, Closing Readiness Score no canal #financeiro
- CRM (HubSpot / Salesforce / Pipedrive)
- dados de conta do cliente para AR: historico de relacionamento, tier do cliente, health score, open tickets de suporte (contexto para cobranca empatetica)
- CS Platforms (ChurnZero / Custify / Chargebee / Gainsight)
- health score para priorizacao de cobranca: clientes em risco de churn recebem abordagem diferente de cobranca (empatetica, com oferta de renegociacao) vs
- clientes saudaveis
- WhatsApp Business API
- canal de cobranca AR: envio de lembretes de vencimento e comunicacoes de cobranca na sequencia configurada pela Dunna, com templates pre-aprovados pela politica de cobranca
- Supabase / Postgres
- estado do squad: Canonical Transaction Set, Exception Queue, status de cada ciclo de fechamento, historico de matches e exceptions, Closing Packages gerados e aprovados
- observabilidade OTEL: tracing de cada ciclo de reconciliacao (source collection -> matching -> exception classification -> investigation -> closing package -> approval), evals por tipo de match e exception, quality gates (dev 70% / staging 85% / prod 95% de precisao de matching)
- Claude Agent SDK / LangGraph
- orquestracao multi-agente do ciclo de reconciliacao, state management do ciclo de fechamento, embedding similarity para matching probabilistico de descricoes de transacoes
- MCP Servers (camada de integracao universal)
- ClickUp MCP, Supabase MCP para acesso padronizado
- integracao com bancos via MCP customizado de Open Finance

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Aurum 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Closing Package no ClickUp como prova de trabalho verificavel por ciclo de fechamento: (1) Reconciliation Statement por conta bancaria (saldo extrato vs
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

- **to:** Fluxo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
