---
task: flex()
responsavel: "Flex"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Resposta do cliente (texto da mensagem + canal de origem + timestamp) + histórico completo da sequência de cobrança do cliente (steps executados, respostas anteriores) + dados da cobrança (valor, data de falha, categoria de falha, número de tentativas de débito) + regras de negociação pre-aprovadas por segmento e por valor + status atual no gateway de pagamento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Para negociações autônomas executadas: novo link de pagamento gerado e enviado pelo Dispatcher correto, registro da negociação no Supabase e no CRM (tipo de acordo, valor, nova data), task no ClickUp como prova de trabalho"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para escalações HITL: task criada no ClickUp com prioridade URGENTE, histórico completo da sequência, intenção classificada, sugestão de abordagem e valor em risco"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "notificação Slack para responsável"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Para sequências encerradas: registro de outcome (RECUPERADO / CONTESTAÇÃO / CANCELAMENTO_SOLICITADO / NEGOCIAÇÃO_APROVADA)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado quando qualquer Dispatcher (Iris, Zap, Pulse) recebe resposta de cliente; acionado pelo Cobalt quando a sequência esgota todos os steps sem recuperação (gerar relatório de inadimplente crôni…"
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

# Classificar Respostas Cliente

**Task ID:** `flex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Respostas Cliente |
| **status** | `pending` |
| **responsible_executor** | Flex (Flex — Agente de Negociação e Classificação de Respostas) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em receber respostas dos clientes (via qualquer canal) e executar o fluxo correto: classificar intencao, responder duvidas simples e executar negociacoes pre-aprovadas autonomamente ou elevar para HITL quando necessario. Flex: (1) CLASSIFICA a resposta do cliente em uma das 8 intencoes: VAI_PAGAR (confimou que vai pagar, aguardando data), JA_PAGOU (afirma ter pago — verificar no gateway antes de encerrar), QUER_PARCELAR (solicita parcelamento), QUER_EXTENSAO (solicita mais prazo), CONTESTA_COBRANCA (afirma que nao deve / que e um erro), QUER_CANCELAR (aproveita a cobranca para solicitar cancelamento), PEDIU_CONTATO_HUMANO (quer falar com atendente), IGNORANDO (resposta irrelevante ou nao relacionada); (2) Para VAI_PAGAR e JA_PAGOU: verifica no gateway o status real, encerra ou ajusta a sequencia; (3) Para QUER_PARCELAR e QUER_EXTENSAO dentro das regras pre-aprovadas (parcelamento em ate 3x para valores < R$2k, extensao de 7 dias para clientes com mais de 6 meses de casa): executa a negociacao autonomamente, gera novo link de pagamento e confirma via canal; (4) Para negociacoes acima do threshold, CONTESTA_COBRANCA ou QUER_CANCELAR: cria task HITL urgente no ClickUp para o time financeiro/CS com historico completo.

## Input

- Resposta do cliente (texto da mensagem + canal de origem + timestamp) + histórico completo da sequência de cobrança do cliente (steps executados, respostas anteriores) + dados da cobrança (valor, data de falha, categoria de falha, número de tentativas de débito) + regras de negociação pre-aprovadas por segmento e por valor + status atual no gateway de pagamento

## Output

- Para negociações autônomas executadas: novo link de pagamento gerado e enviado pelo Dispatcher correto, registro da negociação no Supabase e no CRM (tipo de acordo, valor, nova data), task no ClickUp como prova de trabalho
- Para escalações HITL: task criada no ClickUp com prioridade URGENTE, histórico completo da sequência, intenção classificada, sugestão de abordagem e valor em risco
- notificação Slack para responsável
- Para sequências encerradas: registro de outcome (RECUPERADO / CONTESTAÇÃO / CANCELAMENTO_SOLICITADO / NEGOCIAÇÃO_APROVADA)

## Trigger

Acionado quando qualquer Dispatcher (Iris, Zap, Pulse) recebe resposta de cliente; acionado pelo Cobalt quando a sequência esgota todos os steps sem recuperação (gerar relatório de inadimplente crônico para análise manual); acionado sob demanda pelo time financeiro via comando no ClickUp para reprocessar uma resposta específica

## Knowledge base (o que o executor consulta)

- Regras de negociação pré-aprovadas por segmento e por valor (parcelamento: máximo de parcelas, percentual de desconto de multa, extensão: dias máximos por perfil de cliente), prompts de classificação de intenção com exemplos em PT-BR para cada categoria (incluindo eufemismos e linguagem informal de quem 'vai pagar mas...'), API do gateway para verificação de status de pagamento em tempo real (Stripe Payment Intent, Asaas Boleto, Iugu Invoice), histórico de negociações bem-sucedidas por tipo de acordo para few-shot, fluxos de resposta por intenção classificada, templates de confirmação de acordo por canal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Resposta do cliente (texto da mensagem + canal de origem + timestamp) + histórico completo da sequência de cobrança do…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Para negociações autônomas executadas: novo link de pagamento gerado e enviado pelo Dispatcher correto, registro da neg…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Para negociações autônomas executadas: novo link de pagamento gerado e enviado pelo Dispatcher correto, registro da negociação no Supabase e no CRM (tipo de ac…
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

- **to:** Pulse
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
