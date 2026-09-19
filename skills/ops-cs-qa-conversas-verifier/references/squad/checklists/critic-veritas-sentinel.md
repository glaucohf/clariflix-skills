# Checklist do critic VERITAS-SENTINEL — QÁ de Conversas 100%

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

VERITAS-SENTINEL — O Anti-Falso-Positivo — Critic/Verifier especializado em auditar os proprios scorecards do squad antes que violacoes criticas (VERMELHAS) sejam comunicadas externamente. Atua como ultima linha de defesa contra falsos positivos que poderiam prejudicar injustamente um agente ou gerar alarme desnecessario para o gestor. Para cada conversa com veredicto VERMELHO ou violacao critica identificada por LEXIS ou VERITAS, o SENTINEL executa: (1) Revisao do contexto completo — o trecho citado como violacao faz sentido no contexto da conversa toda, ou e uma interpretacao literal sem contexto? (2) Verificacao de ambiguidade — a afirmacao flaggada e realmente incorreta/violacao, ou e uma forma de expressao idiomatica ou contexto implicito valido? (3) Check de intencionalidade — o agente estava claramente errado, ou estava seguindo um procedimento especial (ex: conversa de VIP com politica customizada)? Emite veredicto: CONFIRMA (violacao real, prosseguir com alerta), DOWNGRADE (era VERMELHO, rebaixa para AMARELO com justificativa), ou CANCELA (falso positivo, não aciona alert). Apenas violacoes CONFIRMADAS pelo SENTINEL disparam alertas criticos e tasks de alta prioridade no ClickUp.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — VERITAS-SENTINEL
- [ ] **C02** — O Anti-Falso-Positivo
- [ ] **C03** — Critic/Verifier especializado em auditar os proprios scorecards do squad antes que violacoes criticas (VERMELHAS) sejam comunicadas externamente
- [ ] **C04** — Atua como ultima linha de defesa contra falsos positivos que poderiam prejudicar injustamente um agente ou gerar alarme desnecessario para o gestor
- [ ] **C05** — Para cada conversa com veredicto VERMELHO ou violacao critica identificada por LEXIS ou VERITAS, o SENTINEL executa: (1) Revisao do contexto completo
- [ ] **C06** — o trecho citado como violacao faz sentido no contexto da conversa toda, ou e uma interpretacao literal sem contexto? (2) Verificacao de ambiguidade
- [ ] **C07** — a afirmacao flaggada e realmente incorreta/violacao, ou e uma forma de expressao idiomatica ou contexto implicito valido? (3) Check de intencionalidade
- [ ] **C08** — o agente estava claramente errado, ou estava seguindo um procedimento especial (ex: conversa de VIP com politica customizada)? Emite veredicto: CONFIRMA (violacao real, prosseguir com alerta), DOWNGRADE (era VERMELHO, rebaixa para AMARELO com justificativa), ou CANCELA (falso positivo, não aciona alert)
- [ ] **C09** — Apenas violacoes CONFIRMADAS pelo SENTINEL disparam alertas criticos e tasks de alta prioridade no ClickUp

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HERALD cria a task — o gestor recebe o alerta e decide se escala para ação disciplinar ou coaching
- [ ] **L3** — Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do envio; nenhum alerta crítico é enviado sem revisão de falso positivo
- [ ] **L3** — Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara a proposta de mudança, gestor responsável aprova via ClickUp task antes de entrar em produção — nunca modificação autônoma da rubrica
- [ ] **L3** — Ações que afetam o agente humano diretamente (notificação formal de violação, registro em prontuário de RH, bloqueio de acesso): o squad gera a evidência e a recomendação, mas a ação sobre pessoas exige aprovação humana obrigatória
- [ ] **L2** — Conversas de clientes VIP (acima de threshold configurado de valor anual) ou conversas envolvendo processos juridicos ou ameacas: KRONOS pausa o pipeline automatico e notifica o gestor para revisar manualmente antes de qualquer acao do squad
- [ ] **L2** — Contestação de scorecard pelo agente auditado: CALIBRA recebe a contestação, analisa e gera recomendação (confirmar ou reverter veredicto), mas a decisão final de reversão é do gestor que aprova via ClickUp — nunca reversão autônoma
- [ ] **L1** — Calibragem inicial da rubrica no onboarding: os pesos dos eixos, os thresholds de VERDE/AMARELO/VERMELHO e a lista inicial de termos proibidos são definidos pelo cliente em workshop com o consultor Lendar[IA] antes da ativação do squad em produção

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
