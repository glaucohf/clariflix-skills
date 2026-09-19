---
task: juizDeFit()
responsavel: "Juiz de Fit"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "qualification_scorecard.json da Vera"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Dados do dossiê do Sherlock (empresa, cargo, segmento)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Configuração dos pesos por critério (definida no onboarding)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Histórico de deals fechados para calibragem do modelo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score final 0-100 com breakdown por dimensão"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tier de prioridade: HOT (>=70) / WARM (40-69) / COLD (<40)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Justificativa em 3 linhas legível pelo humano"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Deal value estimado"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Próximo passo recomendado"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Escrito no HubSpot como lead_score + tier + next_action"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado automaticamente ao fim da qualificação da Vera. Também re-executado a cada 72h para leads WARM ainda no pipeline (re-scoring com novos sinais de intenção)."
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

# Priorizar Leads

**Task ID:** `juizDeFit()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Priorizar Leads |
| **status** | `pending` |
| **responsible_executor** | Juiz de Fit (Juiz de Fit — Magnus) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 7 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de Lead Scoring e Priorizacao. Recebe o scorecard bruto da Vera e aplica modelo de scoring multicritério ponderado conforme o ICP do cliente. Pondera Budget (40%), Need (30%), Authority (20%), Timeline (10%) para BANT simples; aplica matriz MEDDIC completa para vendas complexas (tickets > R$50k). Re-ranqueia a fila de leads qualificados por urgencia x valor x probabilidade de fechamento. Sinaliza leads VIP (score >= 85) para atencao imediata do closer.

## Input

- qualification_scorecard.json da Vera
- Dados do dossiê do Sherlock (empresa, cargo, segmento)
- Configuração dos pesos por critério (definida no onboarding)
- Histórico de deals fechados para calibragem do modelo

## Output

- Score final 0-100 com breakdown por dimensão
- Tier de prioridade: HOT (>=70) / WARM (40-69) / COLD (<40)
- Justificativa em 3 linhas legível pelo humano
- Deal value estimado
- Próximo passo recomendado
- Escrito no HubSpot como lead_score + tier + next_action
- Artefato: scoring_report.json linkado no ClickUp

## Trigger

Disparado automaticamente ao fim da qualificação da Vera. Também re-executado a cada 72h para leads WARM ainda no pipeline (re-scoring com novos sinais de intenção).

## Knowledge base (o que o executor consulta)

- Pesos por critério BANT/MEDDIC definidos no Deep Dive
- Histórico de deals: quais scores realmente fecharam (feedback loop para calibragem)
- ICP detalhado: segmentos, tamanhos de empresa, cargos de decisores, ticket médio por segmento
- Regras de escalação VIP (ex: CEO de empresa > 50 funcionários = sempre HOT independente de score)

## Action Items

1. Confirmar o gatilho e carregar a entrada (qualification_scorecard.json da Vera).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score final 0-100 com breakdown por dimensão) e persistir no artefato do squad.
4. Entregar ao critic Censor Comercial; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score final 0-100 com breakdown por dimensão
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

- **to:** Agendador de Reuniões
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
