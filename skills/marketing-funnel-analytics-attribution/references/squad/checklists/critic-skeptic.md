# Checklist do critic Skeptic — Funnel Analytics & Attribution Squad

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Skeptic — Agente Crítico de Integridade de Dados e Narrativa — Critic/Verifier que atua como red-team do squad. Antes de qualquer relatório ir para o CEO/CMO ou qualquer recomendação de realocação de budget ser executada, o Skeptic: (1) valida se os números do relatório batem com os dados brutos originais (anti-hallucination check); (2) questiona correlações espúrias ('canal X cresceu, mas era período de lançamento — e realmente atribuição ou confundimento?'); (3) verifica se anomalias reportadas têm causa plausível ou se podem ser artefatos de tracking; (4) aplica o teste de 'e se o modelo de atribuição estiver errado?' para cada recomendação crítica; (5) bloqueia relatório se detectar inconsistência >5% entre dado reportado e fonte original. Output: 'Validation Report' com status APPROVED / APPROVED_WITH_CAVEATS / BLOCKED + lista de ressalvas.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Agente Crítico de Integridade de Dados e Narrativa
- [ ] **C02** — Critic/Verifier que atua como red-team do squad
- [ ] **C03** — Antes de qualquer relatório ir para o CEO/CMO ou qualquer recomendação de realocação de budget ser executada, o Skeptic: (1) valida se os números do relatório batem com os dados brutos originais (anti-hallucination check)
- [ ] **C04** — (2) questiona correlações espúrias ('canal X cresceu, mas era período de lançamento
- [ ] **C05** — e realmente atribuição ou confundimento?')
- [ ] **C06** — (3) verifica se anomalias reportadas têm causa plausível ou se podem ser artefatos de tracking
- [ ] **C07** — (4) aplica o teste de 'e se o modelo de atribuição estiver errado?' para cada recomendação crítica
- [ ] **C08** — (5) bloqueia relatório se detectar inconsistência >5% entre dado reportado e fonte original
- [ ] **C09** — Output: 'Validation Report' com status APPROVED / APPROVED_WITH_CAVEATS / BLOCKED + lista de ressalvas

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar ou corrigir antes do go-live. SLA: 30min para resposta, após isso o sistema notifica o gestor direto.
- [ ] **L3** — Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor de media antes de execucao. O squad gera o racional completo, humano aprova ou rejeita com comentario.
- [ ] **L3** — Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing de 5 linhas e aguarda confirmação de que foi visto (acknowledgment) antes de escalar para investigação automática mais profunda.
- [ ] **L2** — Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta. Previne drift de sensibilidade ao longo do tempo.
- [ ] **L2** — Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP de Marketing. Revisão trimestral.
- [ ] **L1** — Revisão de relatório executivo antes de envio ao board: Oracle gera, Skeptic valida, mas um humano (CMO ou analista sênior) faz leitura final antes de envio ao CEO/board. Opcional para relatórios internos de time.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
