# Checklist do critic Auditor de Roteamento — Triagem, Roteamento e Priorização de Tickets

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Auditor de Roteamento — Sócrates — Critic/Verifier que atua em duas camadas: (1) Verificação pré-despacho: após Lara e Dante gerarem outputs e antes de Enzo executar o roteamento, Sócrates revisa a consistência — a intenção bate com os dados do ticket? O score de prioridade faz sentido dado o tier do cliente? A fila de destino é a correta para essa combinação? (2) Auditoria pós-ciclo: diariamente, amostra 10% dos tickets roteados automaticamente, compara destino atribuído vs. destino real (se houve reassignment posterior), calcula drift de qualidade e alerta se acurácia cair abaixo de 85%. Sócrates questiona, não executa — seus outputs são flags e justificativas, nunca ações diretas.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Auditor de Roteamento
- [ ] **C02** — Critic/Verifier que atua em duas camadas: (1) Verificação pré-despacho: após Lara e Dante gerarem outputs e antes de Enzo executar o roteamento, Sócrates revisa a consistência
- [ ] **C03** — a intenção bate com os dados do ticket? O score de prioridade faz sentido dado o tier do cliente? A fila de destino é a correta para essa combinação? (2) Auditoria pós-ciclo: diariamente, amostra 10% dos tickets roteados automaticamente, compara destino atribuído vs
- [ ] **C04** — destino real (se houve reassignment posterior), calcula drift de qualidade e alerta se acurácia cair abaixo de 85%
- [ ] **C05** — Sócrates questiona, não executa
- [ ] **C06** — seus outputs são flags e justificativas, nunca ações diretas

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Confiança de classificação < 0.75 (Lara sinalizou ambiguidade): humano revisa intenção antes do roteamento prosseguir
- [ ] **HITL** — Ticket P1 criado: notificação imediata para supervisor via Slack com justificativa do score, supervisor confirma ou rebaixa prioridade em até 5min
- [ ] **HITL** — Intenção de churn/cancelamento detectada (intent_l1=churn): roteamento bloqueado automaticamente até CS Manager aprovar estratégia de resposta (L3 por risco de perda de receita)
- [ ] **HITL** — Rex detecta surto (SURGE): incident manager humano é notificado e confirma se é incidente real antes de agrupar tickets — evita falso positivo que agruparia tickets distintos
- [ ] **HITL** — Nina tentou auto-resolução mas confidence < 0.90: agente humano recebe ticket com contexto da tentativa e decide a resposta final
- [ ] **HITL** — Novo tipo de intenção detectado (não mapeado na taxonomia): Triador-Mor para o fluxo e aciona ops lead para expandir a taxonomia antes de processar o lote
- [ ] **HITL** — Auditoria do Sócrates aponta drift de acurácia < 85%: revisão semanal obrigatória com ops lead para recalibrar pesos da matriz de roteamento

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
