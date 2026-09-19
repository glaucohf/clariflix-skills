---
task: workerDeOutreachMulticanal()
responsavel: "Worker de Outreach Multicanal"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens aprovadas com canal, timing e destinatário"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Credenciais de integração por canal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Log de envios com status (entregue, aberto, respondido, optout), registro automático no CRM de cada interação, alertas de resposta para o comercial humano"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato: outreach-log-{dealId}.json"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Aprovação do Guardião, janela de tempo configurada (não enviar fora de horário comercial), confirmação do HITL Gatekeeper para deals acima do threshold de valor"
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

# Enviar Mensagens Multicanal

**Task ID:** `workerDeOutreachMulticanal()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Recuperação de Oportunidades Estagnadas

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagens Multicanal |
| **status** | `pending` |
| **responsible_executor** | Worker de Outreach Multicanal (Mensageiro (Worker de Outreach Multicanal)) |
| **execution_type** | `Hybrid` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa o envio das mensagens aprovadas pelo Guardião nos canais corretos e no timing definido. WhatsApp via API Business, email via sequenciador, LinkedIn via automação, voz via Vapi/Retell. Monitora entrega, abertura e resposta. Registra cada interação no CRM automaticamente. Escala para HITL se receber resposta que requer julgamento humano (negociação, reclamação, proposta de reunião).

## Input

- Mensagens aprovadas com canal, timing e destinatário
- Credenciais de integração por canal

## Output

- Log de envios com status (entregue, aberto, respondido, optout), registro automático no CRM de cada interação, alertas de resposta para o comercial humano
- Artefato: outreach-log-{dealId}.json

## Trigger

Aprovação do Guardião, janela de tempo configurada (não enviar fora de horário comercial), confirmação do HITL Gatekeeper para deals acima do threshold de valor

## Knowledge base (o que o executor consulta)

- Credenciais das APIs de canal (WhatsApp Business, SMTP, LinkedIn, Vapi), horários permitidos de envio por canal, limites de frequência (anti-spam), regras de opt-out, template IDs aprovados no WhatsApp Business

## Action Items

1. Confirmar o gatilho e carregar a entrada (Mensagens aprovadas com canal, timing e destinatário).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Log de envios com status (entregue, aberto, respondido, optout), registro automático no CRM de cada interação, alertas…) e persistir no artefato do squad.
4. Entregar ao critic Critic e Verifier de Mensagens 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Log de envios com status (entregue, aberto, respondido, optout), registro automático no CRM de cada interação, alertas de resposta para o comercial humano
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

- **to:** Monge
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
