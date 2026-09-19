---
task: analistaDeConversas()
responsavel: "Analista de Conversas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lote de conversation_logs.json da última semana"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Qualification_scorecards.json correspondentes"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Taxa de conversão por etapa (do HubSpot)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Feedback dos closers sobre qualidade dos leads entregues"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de insights: top 5 perguntas com maior taxa de abandono, top 3 objeções não mapeadas, sugestões de ajuste de prompt para Vera, sugestões de recalibragem de pesos para Magnus"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato: conversation_intelligence_report_W{N}.md salvo no ClickUp e enviado ao gestor via WhatsApp resumido"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron: toda sexta-feira 18h00 para fechamento de ciclo semanal. Também acionado após qualquer batch de >50 qualificações para análise por lote."
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

# Analisar Conversas Qualificadas

**Task ID:** `analistaDeConversas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Conversas Qualificadas |
| **status** | `pending` |
| **responsible_executor** | Analista de Conversas (Analista de Conversas — Éco) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de Conversation Intelligence. Analisa as conversas de qualificação concluídas para identificar padrões: quais perguntas geram mais abandono, quais respostas da Vera têm maior taxa de continuidade, quais objeções não estão no playbook, qual o tempo médio de qualificação por segmento. Gera insights semanais para melhoria contínua dos prompts da Vera e dos critérios de scoring do Magnus.

## Input

- Lote de conversation_logs.json da última semana
- Qualification_scorecards.json correspondentes
- Taxa de conversão por etapa (do HubSpot)
- Feedback dos closers sobre qualidade dos leads entregues

## Output

- Relatório de insights: top 5 perguntas com maior taxa de abandono, top 3 objeções não mapeadas, sugestões de ajuste de prompt para Vera, sugestões de recalibragem de pesos para Magnus
- Artefato: conversation_intelligence_report_W{N}.md salvo no ClickUp e enviado ao gestor via WhatsApp resumido

## Trigger

Cron: toda sexta-feira 18h00 para fechamento de ciclo semanal. Também acionado após qualquer batch de >50 qualificações para análise por lote.

## Knowledge base (o que o executor consulta)

- Métricas de benchmark do setor (taxa de qualificação média por vertical)
- Histórico de insights anteriores para evitar repetição de recomendações
- Mapeamento de etapas do funil para identificar gargalos
- Critérios de qualidade de conversa (completude BANT, clareza de próximo passo, tom adequado)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lote de conversation_logs.json da última semana).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de insights: top 5 perguntas com maior taxa de abandono, top 3 objeções não mapeadas, sugestões de ajuste de…) e persistir no artefato do squad.
4. Entregar ao critic Censor Comercial; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de insights: top 5 perguntas com maior taxa de abandono, top 3 objeções não mapeadas, sugestões de ajuste de prompt para Vera, sugestões de recalibra…
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

- **to:** Censor Comercial
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
