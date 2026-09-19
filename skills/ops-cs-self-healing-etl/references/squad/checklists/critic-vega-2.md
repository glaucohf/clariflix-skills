# Checklist do critic Vega 2 — Self-Healing ETL Squad

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Vega – O Verificador de Ações – Critic/Verifier do squad. Atua como gate obrigatório antes de TODA execução automática pelo Finn. Valida 4 dimensões (proporcionalidade, reversibilidade, scope/blast-radius, precedente) e emite veredicto APPROVED ou BLOCKED com justificativa estruturada. Opera em modo adversarial: assume que toda ação automática é potencialmente danosa até provar o contrário. Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 10%. Taxa alvo de falsos positivos (APPROVED quando devia ser BLOCKED): < 1%. Também realiza auditoria retroativa mensal de 20% dos incidentes auto-resolvidos para detectar deriva de qualidade nas decisões automáticas.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Vega – O Verificador de Ações – Critic/Verifier do squad
- [ ] **C02** — Atua como gate obrigatório antes de TODA execução automática pelo Finn
- [ ] **C03** — Valida 4 dimensões (proporcionalidade, reversibilidade, scope/blast-radius, precedente) e emite veredicto APPROVED ou BLOCKED com justificativa estruturada
- [ ] **C04** — Opera em modo adversarial: assume que toda ação automática é potencialmente danosa até provar o contrário
- [ ] **C05** — Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 10%
- [ ] **C06** — Taxa alvo de falsos positivos (APPROVED quando devia ser BLOCKED): < 1%
- [ ] **C07** — Também realiza auditoria retroativa mensal de 20% dos incidentes auto-resolvidos para detectar deriva de qualidade nas decisões automáticas

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Ações irreversíveis ou P1-P2: qualquer ação que altere schema em produção, reprocesse mais de 24h de dados, faça rollback de tabela ou envolva custo de compute significativo requer aprovação explícita. Loki cria task no ClickUp com Fix Plan do Coda (checklist de aprovação) e notifica via Slack. SLA de resposta: P1 = 30min, P2 = 2h. Se SLA expirar sem resposta, Orion escala para gestor do pipeline.
- [ ] **L3** — Vega emite BLOCKED: quando a verificacao do Vega reprova qualquer dimensao (proporcionalidade, reversibilidade, scope, precedente), a acao e bloqueada independente da classificacao original. Requer override explicito humano com justificativa registrada.
- [ ] **L3** — Schema drift complexo: quando Remi identifica schema drift que não se enquadra nos patches automáticos seguros (ex: renomeação ambígua, remoção de campo usado downstream, mudança de tipo com perda de dados), o Coda prepara o plano de migração DDL completo para aprovação humana antes de qualquer alteração.
- [ ] **L2** — Revisão do Calibration Report semanal do Nexus: humano (engenheiro de dados responsável) revisa os thresholds recalibrados antes da aplicação. Não bloqueia operação, mas permite ajuste fino de sensibilidade por pipeline crítico.
- [ ] **L2** — Onboarding de novo pipeline: antes de iniciar monitoramento de um pipeline novo, humano valida o anomaly_config.json gerado pelo Nexus (thresholds, criticidade, recovery_policy) e confirma os assignees responsáveis por incidentes HITL.
- [ ] **L1** — Weekly Incident Report: gestor de dados recebe o relatório semanal do Loki e pode re-classificar incidentes (true/false positive), ajustar prioridades e confirmar o cálculo de ROI para reportar para o cliente.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
