# Checklist do critic Sigma 2 — Demand Sensing Radar

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Sigma — Critic & Compliance Verifier — Implementa o padrão Skeptic Protocol para o squad: desafia cada ação externa antes de executar, valida conformidade LGPD/GDPR no uso de sinais como contexto de abordagem, verifica alinhamento de brand voice, detecta falsos positivos de sinal (conta parece Hot mas evidências são fracas), e bloqueia playbooks com personalização inadequada ou frequência excessiva por conta. Gate L3 obrigatório — nenhum outreach, campanha paga ou ação de tier 1 sai sem aprovação de Sigma. Responsável por garantir que o 'radar' não vire spam sofisticado.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic & Compliance Verifier
- [ ] **C02** — Implementa o padrão Skeptic Protocol para o squad: desafia cada ação externa antes de executar, valida conformidade LGPD/GDPR no uso de sinais como contexto de abordagem, verifica alinhamento de brand voice, detecta falsos positivos de sinal (conta parece Hot mas evidências são fracas), e bloqueia playbooks com personalização inadequada ou frequência excessiva por conta
- [ ] **C03** — Gate L3 obrigatório
- [ ] **C04** — nenhum outreach, campanha paga ou ação de tier 1 sai sem aprovação de Sigma
- [ ] **C05** — Responsável por garantir que o 'radar' não vire spam sofisticado

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)
- [ ] **HITL** — Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)
- [ ] **HITL** — Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)
- [ ] **HITL** — Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)
- [ ] **HITL** — Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)
- [ ] **HITL** — Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3)
- [ ] **HITL** — Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
