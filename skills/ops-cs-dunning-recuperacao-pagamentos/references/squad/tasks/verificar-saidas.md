---
task: sentinelVerificar()
responsavel: "Sentinel"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes com menos de 3 meses de casa) — Flex classifica e cria task HITL urgente no ClickUp para o time financeiro com histórico completo e valor em risco"
    - "[ ] HITL: Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar no gateway e no CRM, e responde ao cliente confirmando que um humano vai verificar em até X horas"
    - "[ ] HITL: Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task de retenção para o CSM com contexto completo: cliente já estava em inadimplência + agora solicitou cancelamento = risco crítico combinado"
    - "[ ] HITL: Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgente para o Head Financeiro e para o CSM responsável da conta, com sugestão de abordagem via chamada telefônica"
    - "[ ] HITL: Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema no gateway de pagamento, no processador ou na infraestrutura (não é inadimplência — é incidente têcnico)"
---

# Verificar Saídas do Cobrança e Recuperação de Pagamentos

**Task ID:** `sentinelVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Cobrança e Recuperação de Pagamentos |
| **status** | `pending` |
| **responsible_executor** | Sentinel (Sentinel — Critic de Compliance e Tom de Cobrança) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Sentinel — Critic de Compliance e Tom de Cobranca — Valida cada mensagem de cobranca antes do envio em 5 dimensoes inegociaveis: (1) COMPLIANCE LEGAL — nenhuma mensagem viola o Codigo de Defesa do Consumidor (CDC), especialmente Art. 42 (proibicao de coacao, constrangimento ou ameaca), Art. 71 (proibicao de contato em horario excessivo) e a LGPD (mencao a dados pessoais apenas no contexto autorizado, link de pagamento unico e seguro); mensagens de WhatsApp fora de templates HSM aprovados sao bloqueadas automaticamente; (2) TOM PROPORCIONAL — o tom da mensagem deve ser proporcional ao dia de atraso: D0-D2 = informativo e prestativo, D3-D5 = urgente mas profissional, D6-D9 = firme mas sem ameaca, D10+ = ultima chance sem linguagem agressiva; qualquer mensagem com linguagem coercitiva, vexatoria ou que implique consequencias ilegais e BLOQUEADA; (3) PRECISAO DE DADOS — valor informado corresponde exatamente ao valor em aberto no gateway (sem arredondamentos), data de vencimento original correta, link de pagamento valido e testavel, nome do cliente sem erros de encoding PT-BR; (4) FREQUENCIA SEGURA — numero de contatos no dia nao ultrapassa o limite configurado por canal (maximo 1 email/dia, 1 WhatsApp/dia exceto resposta ativa, 1 SMS a cada 2 dias para o mesmo cliente); (5) PERSONALIZACAO INTEGRA — nenhum dado de outro cliente foi injetado na mensagem (verificacao de cross-contamination de variaveis nos templates renderizados). Score minimo para aprovacao: 45/50 (9/10 em cada dimensao). Abaixo disso: bloqueia o envio, registra a violacao no Supabase com dimensao e motivo, e devolve ao Dante com instrucao de correcao especifica.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Critic de Compliance e Tom de Cobranca
- Valida cada mensagem de cobranca antes do envio em 5 dimensoes inegociaveis: (1) COMPLIANCE LEGAL
- nenhuma mensagem viola o Codigo de Defesa do Consumidor (CDC), especialmente Art
- 42 (proibicao de coacao, constrangimento ou ameaca), Art
- 71 (proibicao de contato em horario excessivo) e a LGPD (mencao a dados pessoais apenas no contexto autorizado, link de pagamento unico e seguro)
- mensagens de WhatsApp fora de templates HSM aprovados sao bloqueadas automaticamente
- (2) TOM PROPORCIONAL
- o tom da mensagem deve ser proporcional ao dia de atraso: D0-D2 = informativo e prestativo, D3-D5 = urgente mas profissional, D6-D9 = firme mas sem ameaca, D10+ = ultima chance sem linguagem agressiva
- qualquer mensagem com linguagem coercitiva, vexatoria ou que implique consequencias ilegais e BLOQUEADA
- (3) PRECISAO DE DADOS
- valor informado corresponde exatamente ao valor em aberto no gateway (sem arredondamentos), data de vencimento original correta, link de pagamento valido e testavel, nome do cliente sem erros de encoding PT-BR
- (4) FREQUENCIA SEGURA
- numero de contatos no dia nao ultrapassa o limite configurado por canal (maximo 1 email/dia, 1 WhatsApp/dia exceto resposta ativa, 1 SMS a cada 2 dias para o mesmo cliente)
- (5) PERSONALIZACAO INTEGRA
- nenhum dado de outro cliente foi injetado na mensagem (verificacao de cross-contamination de variaveis nos templates renderizados)
- Score minimo para aprovacao: 45/50 (9/10 em cada dimensao)
- Abaixo disso: bloqueia o envio, registra a violacao no Supabase com dimensao e motivo, e devolve ao Dante com instrucao de correcao especifica

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Cobalt para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Cobalt
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
