---
task: sentinelVerificar()
responsavel: "Sentinel"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR humano com draft completo, dossiê e score para aprovação ou rejeição com 1 clique antes de qualquer disparo."
    - "[ ] HITL: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o feedback detalhado do critic para reescritura manual."
    - "[ ] HITL: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente não envia com informação não verificada."
    - "[ ] HITL: Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para assumir a conversa — o squad nao conduz negociacao, apenas entrega o contexto completo e recua."
    - "[ ] HITL: Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do gestor comercial antes de qualquer envio."
---

# Verificar Saídas do AI SDR Outbound Agentico

**Task ID:** `sentinelVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do AI SDR Outbound Agentico |
| **status** | `pending` |
| **responsible_executor** | Sentinel (Sentinel – O Guardião da Qualidade) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Sentinel – O Guardião da Qualidade – Valida CADA draft gerado pelo Cyrano antes de qualquer envio externo. Checklist obrigatório de 9 pontos – reprovar em qualquer item bloqueia o envio: (1) Personalização real: a mensagem usa pelo menos 3 elementos específicos e verificáveis do dossiê do Scout Profiler? Frases como 'vi que voces cresceram muito' sem dado específico = REPROVADO; (2) Factualidade: todas as afirmações sobre a empresa ou lead são rastreadas a uma fonte no dossiê? Nenhuma suposição sem evidência; (3) Tom adequado: o tom corresponde ao cargo do destinatário e ao canal? CEO via email = diferente de SDR via WhatsApp; (4) CTA único e claro: a mensagem tem exatamente 1 call-to-action, sem ambiguidade e sem múltiplas solicitações; (5) Compliance LGPD: tem mecanismo de opt-out, não usa dados que o destinatário não tornou públicos, não promete resultados garantidos; (6) Ausência de red flags comerciais: sem promessa de desconto não autorizado, sem SLA que o cliente não confirmou, sem benchmark de concorrente que pode ser questionado; (7) Formato e comprimento: email cold max 150 palavras, WhatsApp max 3 blocos curtos com espaçamento, LinkedIn max 300 caracteres, script de voz max 60s; (8) Subject line: max 50 caracteres, não abre com 'Re:' falso, não tem palavras de spam (grátis, urgente, exclusivo); (9) Coerência com a sequência: se é follow-up, referencia a mensagem anterior sem repetir o mesmo pitch? Veredicto: APROVADO (segue para Cadence Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Cyrano, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (gates de compliance, inconsistência de dados crítica, ambiguidade de intenção da mensagem). Opera em paralelo com todos os drafts – nunca serializa desnecessariamente o pipeline.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Sentinel – O Guardião da Qualidade – Valida CADA draft gerado pelo Cyrano antes de qualquer envio externo
- Checklist obrigatório de 9 pontos – reprovar em qualquer item bloqueia o envio: (1) Personalização real: a mensagem usa pelo menos 3 elementos específicos e verificáveis do dossiê do Scout Profiler? Frases como 'vi que voces cresceram muito' sem dado específico = REPROVADO
- (2) Factualidade: todas as afirmações sobre a empresa ou lead são rastreadas a uma fonte no dossiê? Nenhuma suposição sem evidência
- (3) Tom adequado: o tom corresponde ao cargo do destinatário e ao canal? CEO via email = diferente de SDR via WhatsApp
- (4) CTA único e claro: a mensagem tem exatamente 1 call-to-action, sem ambiguidade e sem múltiplas solicitações
- (5) Compliance LGPD: tem mecanismo de opt-out, não usa dados que o destinatário não tornou públicos, não promete resultados garantidos
- (6) Ausência de red flags comerciais: sem promessa de desconto não autorizado, sem SLA que o cliente não confirmou, sem benchmark de concorrente que pode ser questionado
- (7) Formato e comprimento: email cold max 150 palavras, WhatsApp max 3 blocos curtos com espaçamento, LinkedIn max 300 caracteres, script de voz max 60s
- (8) Subject line: max 50 caracteres, não abre com 'Re:' falso, não tem palavras de spam (grátis, urgente, exclusivo)
- (9) Coerência com a sequência: se é follow-up, referencia a mensagem anterior sem repetir o mesmo pitch? Veredicto: APROVADO (segue para Cadence Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Cyrano, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (gates de compliance, inconsistência de dados crítica, ambiguidade de intenção da mensagem)
- Opera em paralelo com todos os drafts – nunca serializa desnecessariamente o pipeline

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Maestro para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloquei…
- [ ] Gate HITL respeitado: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para…
- [ ] Gate HITL respeitado: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR h… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o f… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente nã… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para a… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ICP Cartografo detecta shift significativo de mercado (nova objecao emergindo em >30% das respostas, queda de >20% no reply rate em 2 semanas consecutivas): al… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out ou resposta negativa agressiva: processado pelo Pulse Analyst, sequência cancelada automaticamente, CRM atualizado, notificação ao SDR para decisão sob… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Maestro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
