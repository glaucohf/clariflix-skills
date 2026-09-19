---
task: fluxo()
responsavel: "Fluxo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Credenciais de API por fonte financeira (banco via Open Banking/OFX, ERP via API REST ou exportacao, billing system via API Stripe/Chargebee/Vindi/Iugu), arquivos de importacao manual carregados pelo analista (OFX, CSV, XLSX), configuracao de sources.json (quais fontes estao ativas, qual o formato, qual o endpoint, qual a janela temporal a coletar)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Para o ciclo mensal: janela do mes completo"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Para modo continuo: janela das ultimas 24-48h"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Canonical Transaction Set (JSON array: cada transacao com transaction_id, source_system, source_id, date, value_cents, currency, counterparty_id, counterparty_name_normalized, description_normalized, status, metadata_raw)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Ingestion Report (total de transacoes por fonte, registros rejeitados com motivo, duplicatas removidas na fonte, data lineage hash por batch)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alertas de falha de coleta (fonte indisponivel, credencial expirada, formato inesperado) disparados imediatamente para o Maestro Caixa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron no inicio de cada ciclo de fechamento (configuravel: D+1 do fechamento do periodo, tipicamente dia 1 do mes para fechamento mensal) + chamado manual pelo Maestro Caixa para reprocessar uma fonte…"
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

# Extrair E Normalizar Transacoes

**Task ID:** `fluxo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Extrair E Normalizar Transacoes |
| **status** | `pending` |
| **responsible_executor** | Fluxo (Fluxo — O Extrator e Normalizador de Transacoes) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsavel por coletar transacoes de todas as fontes financeiras configuradas e normalizar para o schema canonico do squad. Conecta via API (preferencial) ou importacao de arquivo (OFX, CSV, XLSX, XML NF-e) e aplica as regras de normalizacao: padroniza campos de data (ISO 8601), normaliza valores monetarios (elimina diferenca de representacao de centavos), limpa e estrutura o campo de descricao livre para facilitar o matching fuzzy, e resolve duplicatas evidentes na fonte (mesmo transaction_id, mesmo valor, mesmo timestamp — dentro de 1 minuto). Gera o Canonical Transaction Set por ciclo: cada transacao com transaction_id unico, source_system, source_id, date, value, counterparty_id, counterparty_name, description_raw, description_normalized, currency, status_raw. Registra o data lineage completo para auditoria.

## Input

- Credenciais de API por fonte financeira (banco via Open Banking/OFX, ERP via API REST ou exportacao, billing system via API Stripe/Chargebee/Vindi/Iugu), arquivos de importacao manual carregados pelo analista (OFX, CSV, XLSX), configuracao de sources.json (quais fontes estao ativas, qual o formato, qual o endpoint, qual a janela temporal a coletar)
- Para o ciclo mensal: janela do mes completo
- Para modo continuo: janela das ultimas 24-48h

## Output

- Canonical Transaction Set (JSON array: cada transacao com transaction_id, source_system, source_id, date, value_cents, currency, counterparty_id, counterparty_name_normalized, description_normalized, status, metadata_raw)
- Ingestion Report (total de transacoes por fonte, registros rejeitados com motivo, duplicatas removidas na fonte, data lineage hash por batch)
- Alertas de falha de coleta (fonte indisponivel, credencial expirada, formato inesperado) disparados imediatamente para o Maestro Caixa

## Trigger

Cron no inicio de cada ciclo de fechamento (configuravel: D+1 do fechamento do periodo, tipicamente dia 1 do mes para fechamento mensal) + chamado manual pelo Maestro Caixa para reprocessar uma fonte especifica + modo continuo: cron diario a cada 24h para reconciliacao incremental. Tambem disparado por upload manual de arquivo pelo analista financeiro.

## Knowledge base (o que o executor consulta)

- sources.json (configuracao de todas as fontes: endpoint, credencial, formato, janela temporal, campos de mapeamento), schema canonico de transacoes, regras de normalizacao de descricao por fonte (ex: padroes de descricao do Bradesco vs
- Nubank), historico de rejeicoes anteriores por fonte para identificar padroes de falha recorrente, mapa de CNPJ/CPF -> counterparty_id para resolucao de entidade

## Action Items

1. Confirmar o gatilho e carregar a entrada (Credenciais de API por fonte financeira (banco via Open Banking/OFX, ERP via API REST ou exportacao, billing system via…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Canonical Transaction Set (JSON array: cada transacao com transaction_id, source_system, source_id, date, value_cents,…) e persistir no artefato do squad.
4. Entregar ao critic Aurum 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Canonical Transaction Set (JSON array: cada transacao com transaction_id, source_system, source_id, date, value_cents, currency, counterparty_id, counterparty_…
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
