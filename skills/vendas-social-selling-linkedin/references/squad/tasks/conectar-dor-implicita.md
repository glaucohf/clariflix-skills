---
task: cypher()
responsavel: "Cypher"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead Dossiê do Sherlock, tipo_sinal, janela_timing, perfil_vendedor (tom de voz, restrições de compliance), playbook de mensagens aprovadas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Message Draft Package: connection_request_note (300 chars), linkedin_dm_v1 (abertura + gancho de sinal + CTA), linkedin_dm_followup_d3, linkedin_dm_followup_d7, variante_email (se email disponível), score_personalização (0-100), justificativa_do_gancho, flags_de_risco (menções imprecisas, tom agressivo, promessa comercial)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead Dossiê recebido do Orquestrador; re-trigger em caso de reprovação pelo Critic com feedback específico."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório."
    - "[ ] HITL: Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada."
    - "[ ] HITL: Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente."
    - "[ ] HITL: Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana."
    - "[ ] HITL: Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração."
---

# Conectar Dor Implicita

**Task ID:** `cypher()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Conectar Dor Implicita |
| **status** | `pending` |
| **responsible_executor** | Cypher (Redator de Sinal (Cypher)) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Drafta mensagens de outreach hiperpersonalizadas baseadas no sinal específico e no dossiê do lead. Não usa templates genéricos: cada mensagem referencia o sinal detectado (ex: 'Vi que você acabou de assumir como VP de Vendas na [empresa]...'), conecta a dor implícita no sinal, e propõe um próximo passo claro e de baixo atrito. Gera versões para LinkedIn DM, connection request note e follow-up.

## Input

- Lead Dossiê do Sherlock, tipo_sinal, janela_timing, perfil_vendedor (tom de voz, restrições de compliance), playbook de mensagens aprovadas

## Output

- Message Draft Package: connection_request_note (300 chars), linkedin_dm_v1 (abertura + gancho de sinal + CTA), linkedin_dm_followup_d3, linkedin_dm_followup_d7, variante_email (se email disponível), score_personalização (0-100), justificativa_do_gancho, flags_de_risco (menções imprecisas, tom agressivo, promessa comercial)

## Trigger

Lead Dossiê recebido do Orquestrador; re-trigger em caso de reprovação pelo Critic com feedback específico.

## Knowledge base (o que o executor consulta)

- Playbook de mensagens aprovadas por tipo de sinal (mudança de cargo, funding, post de dor, engajamento), exemplos de mensagens que geraram reunião (biblioteca positiva), exemplos de mensagens que geraram unfollow/block (biblioteca negativa), restrições de compliance do cliente, tom de voz da marca/vendedor, limites de caracteres LinkedIn por tipo de mensagem

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead Dossiê do Sherlock, tipo_sinal, janela_timing, perfil_vendedor (tom de voz, restrições de compliance), playbook de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Message Draft Package: connection_request_note (300 chars), linkedin_dm_v1 (abertura + gancho de sinal + CTA), linkedin…) e persistir no artefato do squad.
4. Entregar ao critic Argus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Message Draft Package: connection_request_note (300 chars), linkedin_dm_v1 (abertura + gancho de sinal + CTA), linkedin_dm_followup_d3, linkedin_dm_followup_d7…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus 2 registrado
- [ ] Gate HITL respeitado: Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório.
- [ ] Gate HITL respeitado: Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada.
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório. | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana. | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Primeiro envio de cadência para um novo segmento/persona não testado anteriormente: SDR revisa amostra de 5 mensagens antes de liberar automação plena. | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Lead responde mencionando nome de concorrente ou fazendo pergunta técnica complexa: desvia para SDR humano com contexto completo da conversa. | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Argus 2 | BLOQUEIA entrega |

## Handoff

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
