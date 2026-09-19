---
task: reativadorDePipeline()
responsavel: "Reativador de Pipeline"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de leads COLD e WARM sem agendamento"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Score e histórico de qualificação"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Biblioteca de conteúdos de nurture por segmento"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Sinais de reativação (webhooks de pixel, respostas de WhatsApp, abertura de email)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sequência de mensagens de nurture enviadas com timestamps"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Log de tentativas por lead"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Taxa de reativação por cadência"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Leads reativados sinalizados ao Orchestrator para novo ciclo de qualificação"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato: nurture_cadence_log.json atualizado no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado 24h após lead ser classificado COLD ou 48h após lead WARM não responder ao convite de agendamento. Também acionado por sinal de intenção detectado em lead hibernado (visita ao site, engajam…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Censor Comercial antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comercial aprova batch antes do disparo."
    - "[ ] HITL: HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por desconto, Vera responde 'vou verificar com nosso especialista' e escala ao closer via notificação imediata."
    - "[ ] HITL: HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes de qualquer ação automática adicional. Closer decide se assume a conversa ou deixa o squad continuar."
    - "[ ] HITL: HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada."
    - "[ ] HITL: HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor responde o que fazer; resposta é adicionada ao playbook para aprendizado."
---

# Reativar Leads Frios

**Task ID:** `reativadorDePipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reativar Leads Frios |
| **status** | `pending` |
| **responsible_executor** | Reativador de Pipeline (Reativador de Pipeline — Lázaro) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de Follow-up e Nurture. Gerencia leads COLD e leads WARM que não agendaram. Executa cadências persistentes via WhatsApp com mensagens de valor (não spam): compartilha case relevante, artigo do segmento, resultado de cliente similar. Detecta sinais de reativação (resposta, clique, visita ao site via pixel) e notifica o Orchestrator para reiniciar o fluxo de qualificação. Reativa leads 'frios' hibernados há mais de 30 dias com abordagem de ângulo diferente.

## Input

- Lista de leads COLD e WARM sem agendamento
- Score e histórico de qualificação
- Biblioteca de conteúdos de nurture por segmento
- Sinais de reativação (webhooks de pixel, respostas de WhatsApp, abertura de email)

## Output

- Sequência de mensagens de nurture enviadas com timestamps
- Log de tentativas por lead
- Taxa de reativação por cadência
- Leads reativados sinalizados ao Orchestrator para novo ciclo de qualificação
- Artefato: nurture_cadence_log.json atualizado no ClickUp

## Trigger

Disparado 24h após lead ser classificado COLD ou 48h após lead WARM não responder ao convite de agendamento. Também acionado por sinal de intenção detectado em lead hibernado (visita ao site, engajamento com anúncio).

## Knowledge base (o que o executor consulta)

- Biblioteca de conteúdos de nurture segmentados por vertical (imobiliária, agência, SaaS)
- Regras de frequência máxima (LGPD: max 2 mensagens/semana sem resposta)
- Histórico de tentativas por lead para evitar repetição
- Templates de reativação com diferentes ângulos (social proof, urgência, novidade, case study)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de leads COLD e WARM sem agendamento).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sequência de mensagens de nurture enviadas com timestamps) e persistir no artefato do squad.
4. Entregar ao critic Censor Comercial; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sequência de mensagens de nurture enviadas com timestamps
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Censor Comercial registrado
- [ ] Gate HITL respeitado: HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputaci…
- [ ] Gate HITL respeitado: HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se l…
- [ ] Gate HITL respeitado: HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comerci… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por des… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada. | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor res… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL-6 (L1): Relatório semanal do Eco com sugestões de ajuste de prompt — gestor revisa e aprova antes de qualquer alteração ser aplicada nos prompts da Vera o… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Censor Comercial | BLOQUEIA entrega |

## Handoff

- **to:** Guardião do CRM
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
