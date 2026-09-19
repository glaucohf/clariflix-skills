---
task: argus()
responsavel: "Argus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Message Draft Package do Cypher, Lead Dossie do Sherlock, Signal Event original, histórico de interações com o lead"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Validation Report: verdict (APROVADO / REVISAR / BLOQUEADO), score_personalizacao_validado, score_factualidade (0-100), issues_encontrados (lista com severidade), sugestoes_de_correcao, mensagem_aprovada_final (se APROVADO), motivo_bloqueio (se BLOQUEADO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Message Draft Package recebido; re-validação apos correção do Cypher (max 2 iterações antes de escalar para HITL)."
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

# Verificar Mensagem Antes Do Envio

**Task ID:** `argus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Mensagem Antes Do Envio |
| **status** | `pending` |
| **responsible_executor** | Argus (Fiscal de Mensagem (Árgus)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Critic/Verifier que valida cada mensagem ANTES do envio. Verifica: (1) factualidade — o sinal citado realmente aconteceu?, (2) personalizacao genuina vs template disfarado, (3) tom e adequacao cultural, (4) compliance (sem promessas comerciais, sem dados inventados), (5) proporcionalidade (mensagem muito longa/curta), (6) CTA claro e de baixo atrito. Aprova, solicita revisao com feedback especifico, ou bloqueia com justificativa.

## Input

- Message Draft Package do Cypher, Lead Dossie do Sherlock, Signal Event original, histórico de interações com o lead

## Output

- Validation Report: verdict (APROVADO / REVISAR / BLOQUEADO), score_personalizacao_validado, score_factualidade (0-100), issues_encontrados (lista com severidade), sugestoes_de_correcao, mensagem_aprovada_final (se APROVADO), motivo_bloqueio (se BLOQUEADO)

## Trigger

Message Draft Package recebido; re-validação apos correção do Cypher (max 2 iterações antes de escalar para HITL).

## Knowledge base (o que o executor consulta)

- Checklist de validação de mensagens LinkedIn (15 critérios), base de fatos verificáveis sobre o lead (do dossiê), restrições de compliance do cliente, histórico de validações anteriores para calibração de score, exemplos de mensagens reprovadas com motivo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Message Draft Package do Cypher, Lead Dossie do Sherlock, Signal Event original, histórico de interações com o lead).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Validation Report: verdict (APROVADO / REVISAR / BLOQUEADO), score_personalizacao_validado, score_factualidade (0-100),…) e persistir no artefato do squad.
4. Entregar ao critic Argus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Validation Report: verdict (APROVADO / REVISAR / BLOQUEADO), score_personalizacao_validado, score_factualidade (0-100), issues_encontrados (lista com severidad…
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

- **to:** Pulso
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
