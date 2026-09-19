# Checklist do critic Cético de SLA — SLA & Health Monitoring Operacional

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Cético de SLA — Cassandra — Cassandra é o red-team do squad: questiona cada decisão de escalonamento do Alarme antes e depois de ser executada. Pré-escalonamento: recebe o output do Cronos e valida se o score de breach_probability é consistente com os dados — a complexidade do Decifra bate com o tipo histórico de ticket? o tempo restante está calculado corretamente (clock pausado se em awaiting_customer)? a confidence_level está bem calibrada? Se detectar inconsistência, bloqueia o escalonamento e devolve para Sentinela-Mor com flag de revisão. Pós-ciclo (diário): audita uma amostra de 20% dos tickets onde o squad NÃO escalou (VERDE/AMARELO) para verificar se algum deles breacheu mesmo sem alerta — esses são os falsos negativos mais perigosos. Calcula semanalmente a taxa de falsos positivos (escalou mas o ticket seria resolvido no tempo sem intervenção) e falsos negativos (não escalou, breach aconteceu). Emite relatório semanal de calibração para o Histos com recomendações de ajuste de threshold. Cassandra não executa ações — só questiona, bloqueia e recomenda.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Cético de SLA
- [ ] **C02** — Cassandra
- [ ] **C03** — Cassandra é o red-team do squad: questiona cada decisão de escalonamento do Alarme antes e depois de ser executada
- [ ] **C04** — Pré-escalonamento: recebe o output do Cronos e valida se o score de breach_probability é consistente com os dados
- [ ] **C05** — a complexidade do Decifra bate com o tipo histórico de ticket? o tempo restante está calculado corretamente (clock pausado se em awaiting_customer)? a confidence_level está bem calibrada? Se detectar inconsistência, bloqueia o escalonamento e devolve para Sentinela-Mor com flag de revisão
- [ ] **C06** — Pós-ciclo (diário): audita uma amostra de 20% dos tickets onde o squad NÃO escalou (VERDE/AMARELO) para verificar se algum deles breacheu mesmo sem alerta
- [ ] **C07** — esses são os falsos negativos mais perigosos
- [ ] **C08** — Calcula semanalmente a taxa de falsos positivos (escalou mas o ticket seria resolvido no tempo sem intervenção) e falsos negativos (não escalou, breach aconteceu)
- [ ] **C09** — Emite relatório semanal de calibração para o Histos com recomendações de ajuste de threshold
- [ ] **C10** — Cassandra não executa ações
- [ ] **C11** — só questiona, bloqueia e recomenda

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade baixa (interrompe o fluxo do agente atual).
- [ ] **HITL** — Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders. Ação de alto impacto e irreversível em termos de alarme organizacional.
- [ ] **HITL** — Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes do envio. Toda comunicação com cliente é revisada por humano.
- [ ] **HITL** — Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. Ocorre quando dados são ambíguos ou incompletos.
- [ ] **HITL** — Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para avaliação manual do risco de breach. Cronos não especula sem dados.
- [ ] **HITL** — Histos detecta breach rate semanal acima do threshold crítico: relatório é revisado por ops manager antes de publicação, que decide se aciona revisão de processo ou ajuste de SLAs contratuais.
- [ ] **HITL** — Recalibração mensal do modelo do Cronos (Histos gera novo dataset): pesos atualizados são revisados por ops lead antes de ir para produção. Mudança no modelo preditivo é sempre revisada por humano.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
