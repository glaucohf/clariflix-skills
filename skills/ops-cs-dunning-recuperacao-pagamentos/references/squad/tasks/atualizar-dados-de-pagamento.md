---
task: vault()
responsavel: "Vault"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Feed diário do gateway de pagamento com lista de cartões ativos com data de expiração (MM/AA) dos clientes com MRR ativo + dados do cliente para personalização (nome, email, WhatsApp) + configuração de account updater do gateway (se disponível) + credenciais de gateway via MCP"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Para account updater disponível: solicitação de atualização de token enviada para a rede da bandeira, registro no Supabase do status (updated/not_found/error)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para clientes sem account updater: email ou WhatsApp de serviço com link seguro de atualização de cartão (hosted payment page do gateway), registro de abertura e clique"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "KPI diário: número de cartões atualizados proativamente vs total próximos da expiração (taxa de prevenção)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Alerta semanal ao Atlas sobre a taxa de prevenção para inclusão no relatório"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diário (07h) para scan de cartões com expiração nos próximos 30 dias; webhook do gateway quando account updater retorna resultado de atualização automática; acionado pelo Cobalt quando a categor…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes com menos de 3 meses de casa) — Flex classifica e cria task HITL urgente no ClickUp para o time financeiro com histórico completo e valor em risco"
    - "[ ] HITL: Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar no gateway e no CRM, e responde ao cliente confirmando que um humano vai verificar em até X horas"
    - "[ ] HITL: Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task de retenção para o CSM com contexto completo: cliente já estava em inadimplência + agora solicitou cancelamento = risco crítico combinado"
    - "[ ] HITL: Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgente para o Head Financeiro e para o CSM responsável da conta, com sugestão de abordagem via chamada telefônica"
    - "[ ] HITL: Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema no gateway de pagamento, no processador ou na infraestrutura (não é inadimplência — é incidente têcnico)"
---

# Atualizar Dados de Pagamento

**Task ID:** `vault()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Atualizar Dados de Pagamento |
| **status** | `pending` |
| **responsible_executor** | Vault (Vault — Agente de Atualização de Dados de Pagamento) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em capturar proativamente dados de pagamento atualizados ANTES que a falha ocorra, reduzindo a taxa de inadimplencia por cartao expirado (a categoria mais recuperavel e mais evitavel). Vault: (1) Monitora diariamente os cartoes proximos da expiracao (vencimento nos proximos 30, 15 e 7 dias) via gateway de pagamento; (2) Dispara sequencia proativa de atualizacao de cartao com link seguro de atualizacao 30 dias antes — sem tom de cobranca, como servico ao cliente ('seu cartao expira em breve, atualize para nao ter interrupcao'); (3) Para gateways com suporte a account updater (Stripe/Visa/Mastercard): solicita atualizacao automatica de token de cartao via rede de bandeiras sem envolver o cliente — zero atrito; (4) Integra com o Cobalt para que cobracas de cartao expirado sejam automaticamente depriorizadas na sequencia de dunning se o Vault ja tem uma solicitacao de atualizacao em curso; (5) Registra taxa de prevencao de falha por cartao expirado como KPI proprio.

## Input

- Feed diário do gateway de pagamento com lista de cartões ativos com data de expiração (MM/AA) dos clientes com MRR ativo + dados do cliente para personalização (nome, email, WhatsApp) + configuração de account updater do gateway (se disponível) + credenciais de gateway via MCP

## Output

- Para account updater disponível: solicitação de atualização de token enviada para a rede da bandeira, registro no Supabase do status (updated/not_found/error)
- Para clientes sem account updater: email ou WhatsApp de serviço com link seguro de atualização de cartão (hosted payment page do gateway), registro de abertura e clique
- KPI diário: número de cartões atualizados proativamente vs total próximos da expiração (taxa de prevenção)
- Alerta semanal ao Atlas sobre a taxa de prevenção para inclusão no relatório

## Trigger

Cron diário (07h) para scan de cartões com expiração nos próximos 30 dias; webhook do gateway quando account updater retorna resultado de atualização automática; acionado pelo Cobalt quando a categoria de falha de uma cobrança nova é 'cartão expirado' (verificar se Vault já tem solicitação em curso para evitar duplicidade de contato)

## Knowledge base (o que o executor consulta)

- API do gateway de pagamento para consulta de metadados de cartão (expiração, últimos 4 dígitos, bandeira) e para solicitação de account updater (Stripe: /v1/payment_methods com automatic_payment_methods), templates de comunicação proativa de atualização de cartão (tom: serviço, não cobrança), link seguro de atualização (Stripe Customer Portal / Asaas link de atualização / página customizada), política de frequência de contato (máximo 1 comunicação por janela de 7 dias sobre atualização de cartão para não alarmar desnecessariamente), histórico de taxa de sucesso do account updater por bandeira (Visa tem ~60-70%, Mastercard ~50-60%)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Feed diário do gateway de pagamento com lista de cartões ativos com data de expiração (MM/AA) dos clientes com MRR ativ…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Para account updater disponível: solicitação de atualização de token enviada para a rede da bandeira, registro no Supab…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Para account updater disponível: solicitação de atualização de token enviada para a rede da bandeira, registro no Supabase do status (updated/not_found/error)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dia…
- [ ] Gate HITL respeitado: Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time fin…
- [ ] Gate HITL respeitado: Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes c… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task d… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgent… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Sentinel reprova uma mensagem por violação de compliance legal (CDC/LGPD) — bloqueia o disparo, notifica o Head Jurídico e o responsável de CS via Slack, e sus… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Cliente com histórico de chargeback ou de fraude identificado pelo gateway — Cobalt bloqueia a sequência de dunning automática e cria task manual para o time f… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Bad debt confirmado (cobranca nao recuperada apos sequencia completa + tentativas manuais) — Cobalt fecha a sequencia como IRRECUPERAVEL, Atlas atualiza o coho… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Sentinel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
