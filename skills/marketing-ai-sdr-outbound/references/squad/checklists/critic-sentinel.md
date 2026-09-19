# Checklist do critic Sentinel — AI SDR Outbound Agentico

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Sentinel – O Guardião da Qualidade – Valida CADA draft gerado pelo Cyrano antes de qualquer envio externo. Checklist obrigatório de 9 pontos – reprovar em qualquer item bloqueia o envio: (1) Personalização real: a mensagem usa pelo menos 3 elementos específicos e verificáveis do dossiê do Scout Profiler? Frases como 'vi que voces cresceram muito' sem dado específico = REPROVADO; (2) Factualidade: todas as afirmações sobre a empresa ou lead são rastreadas a uma fonte no dossiê? Nenhuma suposição sem evidência; (3) Tom adequado: o tom corresponde ao cargo do destinatário e ao canal? CEO via email = diferente de SDR via WhatsApp; (4) CTA único e claro: a mensagem tem exatamente 1 call-to-action, sem ambiguidade e sem múltiplas solicitações; (5) Compliance LGPD: tem mecanismo de opt-out, não usa dados que o destinatário não tornou públicos, não promete resultados garantidos; (6) Ausência de red flags comerciais: sem promessa de desconto não autorizado, sem SLA que o cliente não confirmou, sem benchmark de concorrente que pode ser questionado; (7) Formato e comprimento: email cold max 150 palavras, WhatsApp max 3 blocos curtos com espaçamento, LinkedIn max 300 caracteres, script de voz max 60s; (8) Subject line: max 50 caracteres, não abre com 'Re:' falso, não tem palavras de spam (grátis, urgente, exclusivo); (9) Coerência com a sequência: se é follow-up, referencia a mensagem anterior sem repetir o mesmo pitch? Veredicto: APROVADO (segue para Cadence Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Cyrano, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (gates de compliance, inconsistência de dados crítica, ambiguidade de intenção da mensagem). Opera em paralelo com todos os drafts – nunca serializa desnecessariamente o pipeline.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Sentinel – O Guardião da Qualidade – Valida CADA draft gerado pelo Cyrano antes de qualquer envio externo
- [ ] **C02** — Checklist obrigatório de 9 pontos – reprovar em qualquer item bloqueia o envio: (1) Personalização real: a mensagem usa pelo menos 3 elementos específicos e verificáveis do dossiê do Scout Profiler? Frases como 'vi que voces cresceram muito' sem dado específico = REPROVADO
- [ ] **C03** — (2) Factualidade: todas as afirmações sobre a empresa ou lead são rastreadas a uma fonte no dossiê? Nenhuma suposição sem evidência
- [ ] **C04** — (3) Tom adequado: o tom corresponde ao cargo do destinatário e ao canal? CEO via email = diferente de SDR via WhatsApp
- [ ] **C05** — (4) CTA único e claro: a mensagem tem exatamente 1 call-to-action, sem ambiguidade e sem múltiplas solicitações
- [ ] **C06** — (5) Compliance LGPD: tem mecanismo de opt-out, não usa dados que o destinatário não tornou públicos, não promete resultados garantidos
- [ ] **C07** — (6) Ausência de red flags comerciais: sem promessa de desconto não autorizado, sem SLA que o cliente não confirmou, sem benchmark de concorrente que pode ser questionado
- [ ] **C08** — (7) Formato e comprimento: email cold max 150 palavras, WhatsApp max 3 blocos curtos com espaçamento, LinkedIn max 300 caracteres, script de voz max 60s
- [ ] **C09** — (8) Subject line: max 50 caracteres, não abre com 'Re:' falso, não tem palavras de spam (grátis, urgente, exclusivo)
- [ ] **C10** — (9) Coerência com a sequência: se é follow-up, referencia a mensagem anterior sem repetir o mesmo pitch? Veredicto: APROVADO (segue para Cadence Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Cyrano, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (gates de compliance, inconsistência de dados crítica, ambiguidade de intenção da mensagem)
- [ ] **C11** — Opera em paralelo com todos os drafts – nunca serializa desnecessariamente o pipeline

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR humano com draft completo, dossiê e score para aprovação ou rejeição com 1 clique antes de qualquer disparo.
- [ ] **HITL** — Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o feedback detalhado do critic para reescritura manual.
- [ ] **HITL** — Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente não envia com informação não verificada.
- [ ] **HITL** — Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para assumir a conversa — o squad nao conduz negociacao, apenas entrega o contexto completo e recua.
- [ ] **HITL** — Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do gestor comercial antes de qualquer envio.
- [ ] **HITL** — ICP Cartografo detecta shift significativo de mercado (nova objecao emergindo em >30% das respostas, queda de >20% no reply rate em 2 semanas consecutivas): alerta ao time de marketing e vendas para revisao estrategica do ICP e playbooks antes de continuar prospeccao.
- [ ] **HITL** — Opt-out ou resposta negativa agressiva: processado pelo Pulse Analyst, sequência cancelada automaticamente, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente — decisão de blacklist é sempre humana.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
