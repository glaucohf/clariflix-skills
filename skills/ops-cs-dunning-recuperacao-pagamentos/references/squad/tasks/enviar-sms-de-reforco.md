---
task: pulse()
responsavel: "Pulse"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Instrução de disparo do Dante (template SMS ID, número do cliente com DDI, link de pagamento encurtado) + credenciais do gateway SMS via MCP + calendário de feriados nacionais e estaduais para validação de horário"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "SMS enviado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registro no Supabase: sms_message_id, status (sent/delivered/failed), timestamp, custo unitário do envio"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Notificação ao Cobalt se entrega falhou (número inválido ou fora de área)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Notificação ao Cobalt se link de pagamento clicado (Dante agenda follow-up de checkout abandonado via WhatsApp se disponível)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Alerta ao time financeiro se número de recusas de entrega ultrapassa threshold (dados de telefone potencialmente desatualizados"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "criar task para CSM atualizar cadastro)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Dante em steps especificos da sequencia onde SMS e o canal correto (step de ultima chance ou step de reforco quando email+WhatsApp nao geraram leitura confirmada); nunca acionado como p…"
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

# Enviar SMS de Reforço

**Task ID:** `pulse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar SMS de Reforço |
| **status** | `pending` |
| **responsible_executor** | Pulse (Pulse — Dispatcher de SMS de Reforço) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa envio de SMS como canal de reforco para etapas criticas da sequencia quando email e WhatsApp nao geraram resposta, ou como canal primario quando WhatsApp nao esta disponivel para o cliente. Pulse e o canal de maior urgencia percebida e e usado com moderacao para preservar o impacto. Para cada instrucao do Dante: (1) Compoe mensagem SMS dentro de 160 caracteres com informacao essencial (nome, valor, link curto de pagamento) e call-to-action clara; (2) Envia via gateway SMS (Twilio/Zenvia/Sinch) com rastreamento de entrega; (3) Registra status (sent/delivered/failed) no Supabase; (4) Para links de pagamento em SMS: usa encurtador com rastreamento para identificar cliques e sinalizar ao Cobalt abandono de checkout; (5) Respeita estritamente as janelas legais de envio (8h-20h dias uteis, proibido domingos e feriados nacionais — CDC Art. 42).

## Input

- Instrução de disparo do Dante (template SMS ID, número do cliente com DDI, link de pagamento encurtado) + credenciais do gateway SMS via MCP + calendário de feriados nacionais e estaduais para validação de horário

## Output

- SMS enviado
- Registro no Supabase: sms_message_id, status (sent/delivered/failed), timestamp, custo unitário do envio
- Notificação ao Cobalt se entrega falhou (número inválido ou fora de área)
- Notificação ao Cobalt se link de pagamento clicado (Dante agenda follow-up de checkout abandonado via WhatsApp se disponível)
- Alerta ao time financeiro se número de recusas de entrega ultrapassa threshold (dados de telefone potencialmente desatualizados
- criar task para CSM atualizar cadastro)

## Trigger

Acionado pelo Dante em steps especificos da sequencia onde SMS e o canal correto (step de ultima chance ou step de reforco quando email+WhatsApp nao geraram leitura confirmada); nunca acionado como primeiro contato exceto quando WA e email nao estao disponiveis para o cliente

## Knowledge base (o que o executor consulta)

- Biblioteca de templates SMS por step (máximo 160 caracteres por template, sem abreviações confusas), calendário de feriados nacionais e dos principais estados (para respeito ao CDC), configuração de gateway SMS por região e por operadora (Twilio para roaming / Zenvia para Brasil), serviço de encurtamento de URL com rastreamento de clique configurado, regras de frequência máxima (máximo 2 SMS por semana por cliente para preservar eficácia), histórico de taxa de entrega por operadora para otimização de rota

## Action Items

1. Confirmar o gatilho e carregar a entrada (Instrução de disparo do Dante (template SMS ID, número do cliente com DDI, link de pagamento encurtado) + credenciais d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (SMS enviado) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: SMS enviado
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
