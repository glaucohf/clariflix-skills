# Checklist do critic Sentinel — Cobrança e Recuperação de Pagamentos

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Sentinel — Critic de Compliance e Tom de Cobranca — Valida cada mensagem de cobranca antes do envio em 5 dimensoes inegociaveis: (1) COMPLIANCE LEGAL — nenhuma mensagem viola o Codigo de Defesa do Consumidor (CDC), especialmente Art. 42 (proibicao de coacao, constrangimento ou ameaca), Art. 71 (proibicao de contato em horario excessivo) e a LGPD (mencao a dados pessoais apenas no contexto autorizado, link de pagamento unico e seguro); mensagens de WhatsApp fora de templates HSM aprovados sao bloqueadas automaticamente; (2) TOM PROPORCIONAL — o tom da mensagem deve ser proporcional ao dia de atraso: D0-D2 = informativo e prestativo, D3-D5 = urgente mas profissional, D6-D9 = firme mas sem ameaca, D10+ = ultima chance sem linguagem agressiva; qualquer mensagem com linguagem coercitiva, vexatoria ou que implique consequencias ilegais e BLOQUEADA; (3) PRECISAO DE DADOS — valor informado corresponde exatamente ao valor em aberto no gateway (sem arredondamentos), data de vencimento original correta, link de pagamento valido e testavel, nome do cliente sem erros de encoding PT-BR; (4) FREQUENCIA SEGURA — numero de contatos no dia nao ultrapassa o limite configurado por canal (maximo 1 email/dia, 1 WhatsApp/dia exceto resposta ativa, 1 SMS a cada 2 dias para o mesmo cliente); (5) PERSONALIZACAO INTEGRA — nenhum dado de outro cliente foi injetado na mensagem (verificacao de cross-contamination de variaveis nos templates renderizados). Score minimo para aprovacao: 45/50 (9/10 em cada dimensao). Abaixo disso: bloqueia o envio, registra a violacao no Supabase com dimensao e motivo, e devolve ao Dante com instrucao de correcao especifica.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Compliance e Tom de Cobranca
- [ ] **C02** — Valida cada mensagem de cobranca antes do envio em 5 dimensoes inegociaveis: (1) COMPLIANCE LEGAL
- [ ] **C03** — nenhuma mensagem viola o Codigo de Defesa do Consumidor (CDC), especialmente Art
- [ ] **C04** — 42 (proibicao de coacao, constrangimento ou ameaca), Art
- [ ] **C05** — 71 (proibicao de contato em horario excessivo) e a LGPD (mencao a dados pessoais apenas no contexto autorizado, link de pagamento unico e seguro)
- [ ] **C06** — mensagens de WhatsApp fora de templates HSM aprovados sao bloqueadas automaticamente
- [ ] **C07** — (2) TOM PROPORCIONAL
- [ ] **C08** — o tom da mensagem deve ser proporcional ao dia de atraso: D0-D2 = informativo e prestativo, D3-D5 = urgente mas profissional, D6-D9 = firme mas sem ameaca, D10+ = ultima chance sem linguagem agressiva
- [ ] **C09** — qualquer mensagem com linguagem coercitiva, vexatoria ou que implique consequencias ilegais e BLOQUEADA
- [ ] **C10** — (3) PRECISAO DE DADOS
- [ ] **C11** — valor informado corresponde exatamente ao valor em aberto no gateway (sem arredondamentos), data de vencimento original correta, link de pagamento valido e testavel, nome do cliente sem erros de encoding PT-BR
- [ ] **C12** — (4) FREQUENCIA SEGURA
- [ ] **C13** — numero de contatos no dia nao ultrapassa o limite configurado por canal (maximo 1 email/dia, 1 WhatsApp/dia exceto resposta ativa, 1 SMS a cada 2 dias para o mesmo cliente)
- [ ] **C14** — (5) PERSONALIZACAO INTEGRA
- [ ] **C15** — nenhum dado de outro cliente foi injetado na mensagem (verificacao de cross-contamination de variaveis nos templates renderizados)
- [ ] **C16** — Score minimo para aprovacao: 45/50 (9/10 em cada dimensao)
- [ ] **C17** — Abaixo disso: bloqueia o envio, registra a violacao no Supabase com dimensao e motivo, e devolve ao Dante com instrucao de correcao especifica

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes com menos de 3 meses de casa) — Flex classifica e cria task HITL urgente no ClickUp para o time financeiro com histórico completo e valor em risco
- [ ] **HITL** — Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar no gateway e no CRM, e responde ao cliente confirmando que um humano vai verificar em até X horas
- [ ] **HITL** — Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task de retenção para o CSM com contexto completo: cliente já estava em inadimplência + agora solicitou cancelamento = risco crítico combinado
- [ ] **HITL** — Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgente para o Head Financeiro e para o CSM responsável da conta, com sugestão de abordagem via chamada telefônica
- [ ] **HITL** — Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema no gateway de pagamento, no processador ou na infraestrutura (não é inadimplência — é incidente têcnico)
- [ ] **HITL** — Sentinel reprova uma mensagem por violação de compliance legal (CDC/LGPD) — bloqueia o disparo, notifica o Head Jurídico e o responsável de CS via Slack, e suspende o envio para todos os clientes no mesmo step até que o template seja revisado e re-aprovado
- [ ] **HITL** — Cliente com histórico de chargeback ou de fraude identificado pelo gateway — Cobalt bloqueia a sequência de dunning automática e cria task manual para o time financeiro gerenciar o caso diretamente (cobrança de fraude tem tratamento jurídico diferente de inadimplência comum)
- [ ] **HITL** — Bad debt confirmado (cobranca nao recuperada apos sequencia completa + tentativas manuais) — Cobalt fecha a sequencia como IRRECUPERAVEL, Atlas atualiza o cohort de bad debt, e cria task para o time juridico/financeiro avaliar encaminhamento para assessoria de cobranca ou baixa contabil

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
