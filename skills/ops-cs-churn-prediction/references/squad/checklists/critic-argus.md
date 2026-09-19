# Checklist do critic Argus — Predição e Prevenção de Churn

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Argus — Critic de Qualidade de Score e Acoes — Valida dois artefatos antes de qualquer disparo externo: (A) HEALTH SCORE — verifica se o score calculado pelo Prism e plausivel e consistente: score nao pode ter variacao > 25 pontos em 24h sem evento critico documentado (protecao contra anomalia de dados), os sinais de entrada devem estar todos presentes e dentro de range esperado (deteccao de dados faltantes ou corrompidos), o segmento correto foi aplicado para o modelo de pesos. Score invalido = reenvia para Prism com flag de dado suspeito. (B) BRIEF E NEXT-BEST-ACTION — valida o brief gerado pelo Mira em 4 dimensoes: (1) EVIDENCIA — toda afirmacao do brief tem sinal concreto que a suporta, nada inventado; (2) ACAO PROPORCIONAL — a acao recomendada e proporcional ao risco e ao perfil da conta (nao oferece desconto imediato para risco MEDIO, nao sugere email generativo para conta Enterprise em risco CRITICO); (3) COMPLETUDE — o CSM tem tudo que precisa para agir sem buscar mais informacao; (4) RISCO DE ACAO — acoes sensiveis (desconto acima de X%, cancelamento de feature, reuniao de exec sponsor) sao flaggeadas como L3 e requerem aprovacao humana antes do Spark criar a task com essa acao. Score minimo para aprovacao do brief: 36/40. Abaixo disso: devolve para Mira com feedback especifico.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Qualidade de Score e Acoes
- [ ] **C02** — Valida dois artefatos antes de qualquer disparo externo: (A) HEALTH SCORE
- [ ] **C03** — verifica se o score calculado pelo Prism e plausivel e consistente: score nao pode ter variacao > 25 pontos em 24h sem evento critico documentado (protecao contra anomalia de dados), os sinais de entrada devem estar todos presentes e dentro de range esperado (deteccao de dados faltantes ou corrompidos), o segmento correto foi aplicado para o modelo de pesos
- [ ] **C04** — Score invalido = reenvia para Prism com flag de dado suspeito
- [ ] **C05** — (B) BRIEF E NEXT-BEST-ACTION
- [ ] **C06** — valida o brief gerado pelo Mira em 4 dimensoes: (1) EVIDENCIA
- [ ] **C07** — toda afirmacao do brief tem sinal concreto que a suporta, nada inventado
- [ ] **C08** — (2) ACAO PROPORCIONAL
- [ ] **C09** — a acao recomendada e proporcional ao risco e ao perfil da conta (nao oferece desconto imediato para risco MEDIO, nao sugere email generativo para conta Enterprise em risco CRITICO)
- [ ] **C10** — (3) COMPLETUDE
- [ ] **C11** — o CSM tem tudo que precisa para agir sem buscar mais informacao
- [ ] **C12** — (4) RISCO DE ACAO
- [ ] **C13** — acoes sensiveis (desconto acima de X%, cancelamento de feature, reuniao de exec sponsor) sao flaggeadas como L3 e requerem aprovacao humana antes do Spark criar a task com essa acao
- [ ] **C14** — Score minimo para aprovacao do brief: 36/40
- [ ] **C15** — Abaixo disso: devolve para Mira com feedback especifico

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica
- [ ] **HITL** — Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato
- [ ] **HITL** — Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados
- [ ] **HITL** — Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch
- [ ] **HITL** — Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar
- [ ] **HITL** — Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar task
- [ ] **HITL** — Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de relacionamento antes de qualquer ação automática
- [ ] **HITL** — Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada antes de reprocessar

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
