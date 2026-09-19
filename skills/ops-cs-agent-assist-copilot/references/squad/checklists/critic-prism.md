# Checklist do critic Prism — Copíloto do Agente Humano

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Prism — Critic de Qualidade de Sugestão — Valida cada sugestão gerada pelo Scribe antes de exibi-la ao atendente. Rubrica de 4 dimensões: (1) PRECISÃO — a informação factual da sugestão é verificável no KB, CRM ou ERP (0-10, alucina = 0 imediato); (2) COMPLIANCE — a sugestão não promete além da política autorizada, não cria compromisso jurídico não intencional (0-10); (3) CONTEXTUALIZAÇÃO — a sugestão usa dados específicos da conta (nome, plano, pedido) em vez de ser genérica demais para ser útil (0-10); (4) TOM & CLAREZA — adequado ao canal, ao sentimento do cliente e ao estilo da empresa (0-10). Score mínimo para exibição: 32/40. Abaixo de 32 ou score 0 em Precisão: rejeita e devolve ao Scribe com feedback específico para nova tentativa (max 1 retry). Se segunda tentativa também falhar: exibe apenas a macro base sem personalização, com aviso visual ao atendente.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Qualidade de Sugestão
- [ ] **C02** — Valida cada sugestão gerada pelo Scribe antes de exibi-la ao atendente
- [ ] **C03** — Rubrica de 4 dimensões: (1) PRECISÃO
- [ ] **C04** — a informação factual da sugestão é verificável no KB, CRM ou ERP (0-10, alucina = 0 imediato)
- [ ] **C05** — (2) COMPLIANCE
- [ ] **C06** — a sugestão não promete além da política autorizada, não cria compromisso jurídico não intencional (0-10)
- [ ] **C07** — (3) CONTEXTUALIZAÇÃO
- [ ] **C08** — a sugestão usa dados específicos da conta (nome, plano, pedido) em vez de ser genérica demais para ser útil (0-10)
- [ ] **C09** — (4) TOM & CLAREZA
- [ ] **C10** — adequado ao canal, ao sentimento do cliente e ao estilo da empresa (0-10)
- [ ] **C11** — Score mínimo para exibição: 32/40
- [ ] **C12** — Abaixo de 32 ou score 0 em Precisão: rejeita e devolve ao Scribe com feedback específico para nova tentativa (max 1 retry)
- [ ] **C13** — Se segunda tentativa também falhar: exibe apenas a macro base sem personalização, com aviso visual ao atendente

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar conscientemente ou corrigir
- [ ] **HITL** — Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — responda manualmente'
- [ ] **HITL** — Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico
- [ ] **HITL** — Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromisso
- [ ] **HITL** — Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente
- [ ] **HITL** — Vault retorna flag 'cliente_em_risco_de_churn' (health score < 50): todas as sugestões do Scribe são marcadas com indicador visual e Lumen adiciona sugestão de escalonamento para CSM
- [ ] **HITL** — Echo detecta que uma macro tem rejection_rate > 60% por 7 dias consecutivos: dispara alerta para gestor de CS no Slack pedindo revisão manual da macro antes de continuar exibindo
- [ ] **HITL** — Shield detecta promessa de desconto ou benefício financeiro no rascunho do atendente: alerta de policy_violation com valor exato do limite autorizado e botão de consulta ao supervisor

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
