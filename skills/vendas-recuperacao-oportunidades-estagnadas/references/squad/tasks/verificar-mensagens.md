---
task: criticEVerifierDeMensagens()
responsavel: "Critic e Verifier de Mensagens"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sequência de mensagens do Arquiteto, contexto do deal, políticas comerciais do cliente, regras de compliance"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens aprovadas com selo de validação OU lista de correções obrigatórias com justificativa"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato: review-{dealId}.json com resultado do checklist"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Playbook entregue pelo Arquiteto, antes de qualquer envio externo"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Critic e Verifier de Mensagens 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado — gate L3 no Mensageiro)"
    - "[ ] HITL: Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa"
    - "[ ] HITL: Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial"
    - "[ ] HITL: Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção"
    - "[ ] HITL: Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo"
---

# Verificar Mensagens

**Task ID:** `criticEVerifierDeMensagens()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Recuperação de Oportunidades Estagnadas

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Mensagens |
| **status** | `pending` |
| **responsible_executor** | Critic e Verifier de Mensagens (Guardião (Critic e Verifier de Mensagens)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Verifica cada mensagem gerada pelo Arquiteto ANTES do envio. Checklist de 7 pontos: (1) personalizacao genuina ou generica?, (2) tom adequado ao historico do lead?, (3) CTA claro e unico?, (4) sem promessas comerciais nao autorizadas?, (5) sem desconto fora de aprovacao L3?, (6) compliance com LGPD e politica de opt-out?, (7) sem informacoes factuais incorretas sobre o produto? Rejeita e devolve ao Arquiteto ou aprova para o Mensageiro.

## Input

- Sequência de mensagens do Arquiteto, contexto do deal, políticas comerciais do cliente, regras de compliance

## Output

- Mensagens aprovadas com selo de validação OU lista de correções obrigatórias com justificativa
- Artefato: review-{dealId}.json com resultado do checklist

## Trigger

Playbook entregue pelo Arquiteto, antes de qualquer envio externo

## Knowledge base (o que o executor consulta)

- Política comercial do cliente (descontos autorizados, promessas permitidas), regras de compliance (LGPD, CAN-SPAM, política de opt-out WhatsApp), catálogo de produtos com especificações corretas, histórico de mensagens rejeitadas (aprendizado)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sequência de mensagens do Arquiteto, contexto do deal, políticas comerciais do cliente, regras de compliance).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens aprovadas com selo de validação OU lista de correções obrigatórias com justificativa) e persistir no artefato do squad.
4. Entregar ao critic Critic e Verifier de Mensagens 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens aprovadas com selo de validação OU lista de correções obrigatórias com justificativa
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Critic e Verifier de Mensagens 2 registrado
- [ ] Gate HITL respeitado: Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeir…
- [ ] Gate HITL respeitado: Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa
- [ ] Gate HITL respeitado: Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável c…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Opt-out recebido — registrado imediatamente, comunicado ao comercial, nenhuma acao adicional automatica alem do registro de compliance | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Critic e Verifier de Mensagens 2 | BLOQUEIA entrega |

## Handoff

- **to:** Worker de Outreach Multicanal
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
