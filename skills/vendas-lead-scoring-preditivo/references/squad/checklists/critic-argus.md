# Checklist do critic Argus — Lead Scoring Preditivo e Priorização

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Guardião de Qualidade (Argus) — Crític/Verifier que intercepta todo output do Nexus (mensagens de outreach) antes do envio e valida: (1) personalização genuína vs template genérico, (2) factualidade — toda afirmação sobre a empresa deve rastrear para dado do Sherlock, (3) compliance — sem promessas comerciais não autorizadas, sem linguagem de pressão abusiva, sem menção a concorrentes, (4) tom adequado ao canal e persona, (5) link de unsubscribe presente em emails, (6) score de qualidade >= 7/10 para liberar. Também audita amostra semanal de 10% das mensagens enviadas para detectar drift de qualidade.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Guardião de Qualidade (Argus)
- [ ] **C02** — Crític/Verifier que intercepta todo output do Nexus (mensagens de outreach) antes do envio e valida: (1) personalização genuína vs template genérico, (2) factualidade
- [ ] **C03** — toda afirmação sobre a empresa deve rastrear para dado do Sherlock, (3) compliance
- [ ] **C04** — sem promessas comerciais não autorizadas, sem linguagem de pressão abusiva, sem menção a concorrentes, (4) tom adequado ao canal e persona, (5) link de unsubscribe presente em emails, (6) score de qualidade >= 7/10 para liberar
- [ ] **C05** — Também audita amostra semanal de 10% das mensagens enviadas para detectar drift de qualidade

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes do disparo. SLA de aprovação: 2h.
- [ ] **HITL** — HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do Closer ou Gerente Comercial.
- [ ] **HITL** — HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos.
- [ ] **HITL** — HITL-4 (L3): Alerta de deal em risco alto — gestor recebe notificação e deve confirmar qual ação tomar (intervir diretamente, escalar para diretor, ajustar proposta) antes de qualquer comunicação automatizada.
- [ ] **HITL** — HITL-5 (L2): Ajuste manual de score por SDR — SDR pode adicionar nota qualitativa (ex: 'falei com o CEO, orçamento confirmado') que sobe o score manualmente, com registro no log de auditoria.
- [ ] **HITL** — HITL-6 (L1): Calibração mensal do modelo de scoring — analista de RevOps revisa os feature weights sugeridos pelo sistema e aprova ou ajusta antes do re-treino.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
