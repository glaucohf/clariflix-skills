---
task: flash()
responsavel: "Flash"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Payload do lead (nome, email, telefone, canal de origem, produto de interesse, timestamp) vindo do Orchestrator via webhook/CRM trigger"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem de boas-vindas enviada + confirmacao de entrega + registro de interacao no CRM (campo 'primeiro_contato_em', 'canal_primeiro_contato')"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato no ClickUp: task 'Primeiro Contato Realizado' com timestamp e print da mensagem"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo lead criado no CRM; webhook de formulario recebido; nova mensagem em canal monitorado; chamada entrante identificada. SLA: acao em ate 60 segundos do evento."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead"
    - "[ ] HITL: Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto"
    - "[ ] HITL: Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio"
    - "[ ] HITL: Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel"
    - "[ ] HITL: Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano"
---

# Enviar Primeira Resposta ao Lead

**Task ID:** `flash()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Primeira Resposta ao Lead |
| **status** | `pending` |
| **responsible_executor** | Flash (Flash — Worker de Primeiro Contato) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Envia a primeira resposta ao lead em qualquer canal em menos de 60 segundos. Personaliza a abertura com nome, origem (qual formulario/anuncio/post gerou o lead) e contexto do produto de interesse. Objetivo unico: manter o lead engajado e coletar o numero de telefone/WhatsApp se ainda nao disponivel.

## Input

- Payload do lead (nome, email, telefone, canal de origem, produto de interesse, timestamp) vindo do Orchestrator via webhook/CRM trigger

## Output

- Mensagem de boas-vindas enviada + confirmacao de entrega + registro de interacao no CRM (campo 'primeiro_contato_em', 'canal_primeiro_contato')
- Artefato no ClickUp: task 'Primeiro Contato Realizado' com timestamp e print da mensagem

## Trigger

Novo lead criado no CRM; webhook de formulario recebido; nova mensagem em canal monitorado; chamada entrante identificada. SLA: acao em ate 60 segundos do evento.

## Knowledge base (o que o executor consulta)

- Templates de abertura por canal (WhatsApp, email, chat, voz)
- mapa de produtos/servicos do cliente com descricao de 1 linha
- scripts de coleta de contato ausente
- horarios de funcionamento e mensagens fora de horario

## Action Items

1. Confirmar o gatilho e carregar a entrada (Payload do lead (nome, email, telefone, canal de origem, produto de interesse, timestamp) vindo do Orchestrator via web…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagem de boas-vindas enviada + confirmacao de entrega + registro de interacao no CRM (campo 'primeiro_contato_em', '…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagem de boas-vindas enviada + confirmacao de entrega + registro de interacao no CRM (campo 'primeiro_contato_em', 'canal_primeiro_contato')
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead
- [ ] Gate HITL respeitado: Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Reagendamento apos segundo no-show — Atlas escala para closer decidir se continua ou descarta lead | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Lead demonstra sinal negativo forte (reclamacao de contato excessivo, solicitacao de opt-out) — intervencao humana obrigatoria e imediata | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Sherlock
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
