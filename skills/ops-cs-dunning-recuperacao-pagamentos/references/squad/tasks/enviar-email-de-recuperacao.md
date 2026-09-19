---
task: iris()
responsavel: "Iris"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Instrução de disparo do Dante (template ID, dados de personalização, remetente, link de pagamento) + dados do cliente (nome, email, nome da empresa, valor em atraso, data de falha, opções de negociação autorizadas para este step) + credenciais SendGrid/SES via MCP"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Email enviado com rastreamento ativo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registro no Supabase: message_id, timestamp de envio, status (sent/delivered/opened/clicked/bounced/replied)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Notificação ao Cobalt: se bounce (email inválido"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "trocar canal), se opened-sem-clique após 4h (Dante agenda follow-up via WhatsApp), se clicou-sem-pagar após 2h (Dante agenda email de abandono de checkout), se respondeu (Flex e acionado para processar resposta)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Dante quando o step atual da sequência e canal email; acionado por webhook de evento de abandono de checkout (cliente clicou no link mas não finalizou o pagamento); acionado pelo Cobalt…"
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

# Enviar Email De Recuperação

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Email De Recuperação |
| **status** | `pending` |
| **responsible_executor** | Iris (Iris — Dispatcher de Email de Cobrança) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa o envio de emails de recuperação de pagamento com personalização profunda e rastreamento de engajamento. Para cada instrução recebida do Dante, Iris: (1) Renderiza o template do step atual com dados personalizados do cliente (nome, nome da empresa, valor exato em atraso, data de vencimento original, link de pagamento direto e único por email, opções de negociação disponíveis); (2) Seleciona o remetente correto — email do CSM responsável para clientes High Value/Enterprise, email da cobrança para Standard/Quick Win; (3) Envia via provedor de email (SendGrid/Amazon SES) com configuração de rastreamento de abertura, clique no link de pagamento e resposta; (4) Registra no Supabase o status de entrega, abertura (timestamp) e clique; (5) Detecta respostas automáticas (OOO, bounce) e notifica o Cobalt para ajuste de sequência; (6) Para clientes que clicaram no link mas não finalizaram o pagamento: sinaliza ao Cobalt para step de follow-up específico de abandono de checkout.

## Input

- Instrução de disparo do Dante (template ID, dados de personalização, remetente, link de pagamento) + dados do cliente (nome, email, nome da empresa, valor em atraso, data de falha, opções de negociação autorizadas para este step) + credenciais SendGrid/SES via MCP

## Output

- Email enviado com rastreamento ativo
- Registro no Supabase: message_id, timestamp de envio, status (sent/delivered/opened/clicked/bounced/replied)
- Notificação ao Cobalt: se bounce (email inválido
- trocar canal), se opened-sem-clique após 4h (Dante agenda follow-up via WhatsApp), se clicou-sem-pagar após 2h (Dante agenda email de abandono de checkout), se respondeu (Flex e acionado para processar resposta)

## Trigger

Acionado pelo Dante quando o step atual da sequência e canal email; acionado por webhook de evento de abandono de checkout (cliente clicou no link mas não finalizou o pagamento); acionado pelo Cobalt para envio de confirmação de pagamento recebido

## Knowledge base (o que o executor consulta)

- Biblioteca de templates de email por step (informativo D0, urgente D3, negociacao D5, ultima chance D7, confirmacao de pagamento) e por perfil (QUICK_WIN/STANDARD/HIGH_VALUE), regras de personalizacao por campo (valor formatado em BRL, data no formato DD/MM/AAAA, link de pagamento por integracao com gateway), remetentes autorizados por segmento, configuracao de rastreamento por provedor (SendGrid/SES), regras de deteccao de bounce e OOO, historico de taxas de abertura por assunto e horario (para otimizacao continua)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Instrução de disparo do Dante (template ID, dados de personalização, remetente, link de pagamento) + dados do cliente (…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Email enviado com rastreamento ativo) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Email enviado com rastreamento ativo
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

- **to:** Zap
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
