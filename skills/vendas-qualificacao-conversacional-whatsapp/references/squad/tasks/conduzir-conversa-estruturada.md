---
task: sdrConversacional()
responsavel: "SDR Conversacional"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê enriquecido do Sherlock"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Mensagem de WhatsApp do lead (texto/audio transcrito)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Histórico de conversa (últimas 10 mensagens)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Playbook de qualificação customizado do cliente"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Thresholds de score para roteamento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Conversa de WhatsApp conduzida até coleta completa dos critérios"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Score BANT/MEDDIC 0-100 calculado por dimensão e consolidado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Campos BANT preenchidos no HubSpot"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Status do lead: QUALIFIED / NURTURE / DISQUALIFIED"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Resumo de qualificação em 5 bullets para o closer"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Artefato verificável: conversation_log + qualification_scorecard.json salvo no ClickUp e linkado no deal do HubSpot"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Orchestrator após enriquecimento do Sherlock. Também reativado pelo Worker de Follow-up quando lead volta a interagir após período de silêncio."
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

# Conduzir Conversa Estruturada

**Task ID:** `sdrConversacional()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Conduzir Conversa Estruturada |
| **status** | `pending` |
| **responsible_executor** | SDR Conversacional (SDR Conversacional — Véra) |
| **execution_type** | `Agent` |
| **input** | 5 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de Qualificação Conversacional BANT/MEDDIC via WhatsApp. Conduz diálogo estruturado em linguagem natural e coloquial brasileira, coletando os 4 pilares BANT (Budget, Authority, Need, Timeline) e os 6 de MEDDIC (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion) de forma não-robotica. Adapta o roteiro ao contexto do lead (ex: se veio de anúncio de imóvel de R$800k, não pergunta faixa de preço — confirma). Trata objeções de primeiro nível. Encerra a conversa com score calculado e próximo passo claro.

## Input

- Dossiê enriquecido do Sherlock
- Mensagem de WhatsApp do lead (texto/audio transcrito)
- Histórico de conversa (últimas 10 mensagens)
- Playbook de qualificação customizado do cliente
- Thresholds de score para roteamento

## Output

- Conversa de WhatsApp conduzida até coleta completa dos critérios
- Score BANT/MEDDIC 0-100 calculado por dimensão e consolidado
- Campos BANT preenchidos no HubSpot
- Status do lead: QUALIFIED / NURTURE / DISQUALIFIED
- Resumo de qualificação em 5 bullets para o closer
- Artefato verificável: conversation_log + qualification_scorecard.json salvo no ClickUp e linkado no deal do HubSpot

## Trigger

Disparado pelo Orchestrator após enriquecimento do Sherlock. Também reativado pelo Worker de Follow-up quando lead volta a interagir após período de silêncio.

## Knowledge base (o que o executor consulta)

- Roteiro BANT/MEDDIC customizado (versão imobiliária OU agência OU genérico
- selecionado pelo Orchestrator)
- Biblioteca de 50+ objeções mapeadas com respostas validadas
- Tom de voz da marca do cliente
- Exemplos de conversas que converteram (few-shot)
- Regras de compliance (LGPD: nunca pedir CPF/dados sensíveis sem consentimento explícito)
- Limites de tentativas por janela (max 3 mensagens sem resposta antes de escalar para Follow-up)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossiê enriquecido do Sherlock).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Conversa de WhatsApp conduzida até coleta completa dos critérios) e persistir no artefato do squad.
4. Entregar ao critic Censor Comercial; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Conversa de WhatsApp conduzida até coleta completa dos critérios
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

- **to:** Juiz de Fit
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
