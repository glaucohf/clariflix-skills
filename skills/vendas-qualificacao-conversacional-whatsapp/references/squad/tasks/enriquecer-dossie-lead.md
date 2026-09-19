---
task: investigadorDeLead()
responsavel: "Investigador de Lead"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "lead_id + dados brutos capturados (telefone, email, nome, utm_source, utm_campaign, form_fields)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Payload do webhook de entrada"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê JSON enriquecido com: nome_completo, empresa, cargo, segmento, tamanho_empresa, canal_origem, anúncio_clicado, score_inicial_0a100, campos_bant_preenchidos_do_contexto"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Escrito no HubSpot como propriedades do contato"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Orchestrator imediatamente após recepção de novo lead. Também disparado quando Worker de Higiene detecta campo crítico vazio em lead existente."
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

# Enriquecer Dossiê Lead

**Task ID:** `investigadorDeLead()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dossiê Lead |
| **status** | `pending` |
| **responsible_executor** | Investigador de Lead (Investigador de Lead — Sherlock) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de Pesquisa e Enriquecimento de Conta/Lead. Dado um número de telefone, email ou nome, aciona Apollo/Clay/Clearbit para construir o dossiê inicial: empresa, cargo, tamanho da empresa, setor, presença digital, histórico de interações anteriores no CRM, anúncios que o lead clicou. Normaliza e escreve os campos no HubSpot antes que qualquer conversa comece.

## Input

- lead_id + dados brutos capturados (telefone, email, nome, utm_source, utm_campaign, form_fields)
- Payload do webhook de entrada

## Output

- Dossiê JSON enriquecido com: nome_completo, empresa, cargo, segmento, tamanho_empresa, canal_origem, anúncio_clicado, score_inicial_0a100, campos_bant_preenchidos_do_contexto
- Escrito no HubSpot como propriedades do contato

## Trigger

Disparado pelo Orchestrator imediatamente após recepção de novo lead. Também disparado quando Worker de Higiene detecta campo crítico vazio em lead existente.

## Knowledge base (o que o executor consulta)

- Criterios BANT/MEDDIC customizados do cliente
- Schema de campos do HubSpot do cliente
- Regras de deduplicação (ex: mesmo telefone = mesmo contato)
- Histórico de deals do CRM para verificar se já é cliente/ex-cliente
- Segmentos-alvo definidos no ICP (Ideal Customer Profile)

## Action Items

1. Confirmar o gatilho e carregar a entrada (lead_id + dados brutos capturados (telefone, email, nome, utm_source, utm_campaign, form_fields)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossiê JSON enriquecido com: nome_completo, empresa, cargo, segmento, tamanho_empresa, canal_origem, anúncio_clicado, s…) e persistir no artefato do squad.
4. Entregar ao critic Censor Comercial; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossiê JSON enriquecido com: nome_completo, empresa, cargo, segmento, tamanho_empresa, canal_origem, anúncio_clicado, score_inicial_0a100, campos_bant_preenchi…
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

- **to:** SDR Conversacional
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
