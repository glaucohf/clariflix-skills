---
task: cobaltPipeline()
responsavel: "Cobalt"
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
    descricao: "Por evento de falha de pagamento: (1) Task no ClickUp criada automaticamente no momento da falha com dados completos da cobrança"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "cliente, valor, categoria de falha, sequência selecionada, canal priorizado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "como ponto de entrada rastreável de toda a sequência"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) Log completo no Supabase de cada mensagem enviada (canal, template, timestamp, status de entrega, leitura e resposta) e de cada tentativa de débito (timestamp, resultado, decline_code)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "prova de trabalho auditável e rastreável por cobrança"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(3) Registro de outcome final da cobrança (RECUPERADO_AUTOMÁTICO / RECUPERADO_NEGOCIAÇÃO / RECUPERADO_HITL / BAD_DEBT / CANCELAMENTO) com atribuição ao step e ao canal que converteu"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe o evento de falha de pagamento via webhook do gateway (Stripe/Asaas/Iugu) em tempo real, consulta o CRM e a base de dados do cliente para enriquecer o contexto (MRR, segmento, tempo de casa, h…"
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

# Orquestrar Pipeline do Cobrança e Recuperação de Pagamentos

**Task ID:** `cobaltPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Cobrança e Recuperação de Pagamentos |
| **status** | `pending` |
| **responsible_executor** | Cobalt (Cobalt — Maestro de Recuperação de Receita) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 9 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o evento de falha de pagamento via webhook do gateway (Stripe/Asaas/Iugu) em tempo real, consulta o CRM e a base de dados do cliente para enriquecer o contexto (MRR, segmento, tempo de casa, histórico de pagamentos, canais disponíveis), classifica o perfil de inadimplência (QUICK_WIN / STANDARD / HIGH_VALUE / ENTERPRISE) com base nas regras do playbook calibrado, instancia o workflow de recuperação correto no LangGraph com estado persistido no Supabase, orquestra a sequência de agentes (Dante para timing, Dispatchers para envio, Flex para negociação, Sentinel para validação, Prova para registro), monitora o status de cada cobrança em aberto e reage a eventos intermediários (pagamento realizado = encerra sequência; resposta do cliente = aciona Flex; timeout de etapa = avança para próximo step). Opera em modo event-driven contínuo, sem batch, para garantir que a janela de alta taxa de recuperação (0-24h após a falha) seja sempre capturada.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Por evento de falha de pagamento: (1) Task no ClickUp criada automaticamente no momento da falha com dados completos da cobrança
- cliente, valor, categoria de falha, sequência selecionada, canal priorizado
- como ponto de entrada rastreável de toda a sequência
- (2) Log completo no Supabase de cada mensagem enviada (canal, template, timestamp, status de entrega, leitura e resposta) e de cada tentativa de débito (timestamp, resultado, decline_code)
- prova de trabalho auditável e rastreável por cobrança
- (3) Registro de outcome final da cobrança (RECUPERADO_AUTOMÁTICO / RECUPERADO_NEGOCIAÇÃO / RECUPERADO_HITL / BAD_DEBT / CANCELAMENTO) com atribuição ao step e ao canal que converteu
- para calibração contínua do Atlas
- Por semana: relatório executivo de recuperação entregue no Slack do Head Financeiro com MRR recuperado, MRR em bad debt, breakdown por causa de falha, top-5 segmentos com maior taxa de inadimplência, performance de cada canal e recomendações de ajuste do playbook para a próxima semana
- Por mês: análise de cohort de inadimplentes com identificação de clientes com padrão recorrente e recomendação de ações preventivas (mudança de data de cobrança, troca de método de pagamento, contato proativo do CSM)

## Trigger

Recebe o evento de falha de pagamento via webhook do gateway (Stripe/Asaas/Iugu) em tempo real, consulta o CRM e a base de dados do cliente para enriquecer o contexto (MRR, segmento, tempo de casa, histórico de pagamentos, canais disponíveis), classifica o perfil de inadimplência (QUICK_WIN / STANDARD / HIGH_VALUE / ENTERPRISE) com base nas regras do playbook calibrado, instancia o workflow de recuperação correto no LangGraph com estado persistido no Supabase, orquestra a sequência de agentes (Dante para timing, Dispatchers para envio, Flex para negociação, Sentinel para validação, Prova para registro), monitora o status de cada cobrança em aberto e reage a eventos intermediários (pagamento realizado = encerra sequência; resposta do cliente = aciona Flex; timeout de etapa = avança para próximo step). Opera em modo event-driven contínuo, sem batch, para garantir que a janela de alta taxa de recuperação (0-24h após a falha) seja sempre capturada.

## Knowledge base (o que o executor consulta)

- Gateway de Pagamento: Stripe (Payment Intents, Customer Portal, Account Updater, webhooks de falha em tempo real), Asaas, Iugu, Vindi ou PagSeguro
- fonte primária de eventos de falha e endpoint de retry de cobrança
- WhatsApp Business API: 360dialog, Twilio ou Meta Cloud API direta
- canal #1 de recuperação no Brasil, com gestão de templates HSM aprovados e janela de conversação de 24h
- Email: SendGrid ou Amazon SES
- canal de cobrança formal com rastreamento de abertura, clique e resposta
- SMS: Twilio, Zenvia ou Sinch
- canal de reforço para steps críticos de última chance
- ClickUp (Brain2 / MCP server)
- hub de tasks de cobranca, prova de trabalho, historico de sequencias, HITL queue e registro de outcomes, espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce
- dados de conta (MRR, segmento, CSM responsável, tempo de casa, histórico de pagamentos, contatos autorizados)
- Supabase / Postgres
- estado das sequências de dunning, log de mensagens enviadas, histórico de tentativas de cobrança, negociações registradas, cohorts de inadimplentes e bad debt
- observabilidade OTEL, tracing de cada sequência de dunning, evals de qualidade das mensagens geradas pelo Flex, quality gates dev/staging/prod, rastreamento de custo por cobrança recuperada
- Claude Agent SDK / LangGraph
- orquestração do workflow de recuperação com estado persistido, retry logic e gerenciamento de eventos assíncronos (resposta de cliente pode chegar horas depois)
- notificações HITL urgentes para time financeiro (negociação acima do threshold), alertas de spike de falhas para time técnico, relatório semanal de recuperação para Head Financeiro
- Plataforma de CS (ChurnZero, Custify, Gainsight)
- integração bidirecional: leitura de segmento e health score do cliente para personalizar a abordagem, escrita de eventos de dunning no timeline do cliente para o CSM ter contexto completo

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Sentinel antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Por evento de falha de pagamento: (1) Task no ClickUp criada automaticamente no momento da falha com dados completos da cobrança
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

- **to:** Dante
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
