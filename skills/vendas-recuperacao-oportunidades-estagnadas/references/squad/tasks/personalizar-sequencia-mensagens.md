---
task: arquiteto()
responsavel: "Arquiteto"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados do deal, bucket de classificacao, Dossie de Reativacao do Escavador, playbooks de recuperacao configurados, historico de mensagens anteriores"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sequência de recuperação personalizada: N mensagens com canal, timing, copy completo e CTA"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato: playbook-{dealId}.json com todas as mensagens prontas para revisão do Guardião"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Dossiê de Reativação entregue pelo Escavador, classificação de bucket confirmada pelo Orquestrador"
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

# Personalizar Sequência Mensagens

**Task ID:** `arquiteto()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Recuperação de Oportunidades Estagnadas

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Personalizar Sequência Mensagens |
| **status** | `pending` |
| **responsible_executor** | Arquiteto (Arquiteto (Worker de Playbook e Roteiro de Recuperação)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Seleciona e personaliza o playbook de recuperação correto para cada deal com base no bucket, canal preferencial, histórico de interações e Dossiê do Escavador. Gera a sequência completa de mensagens (entre 2 e 5 toques) com timing, canal, ângulo de abordagem e CTA específico. Sem criatividade genérica — cada mensagem referencia algo específico do contexto do lead.

## Input

- Dados do deal, bucket de classificacao, Dossie de Reativacao do Escavador, playbooks de recuperacao configurados, historico de mensagens anteriores

## Output

- Sequência de recuperação personalizada: N mensagens com canal, timing, copy completo e CTA
- Artefato: playbook-{dealId}.json com todas as mensagens prontas para revisão do Guardião

## Trigger

Dossiê de Reativação entregue pelo Escavador, classificação de bucket confirmada pelo Orquestrador

## Knowledge base (o que o executor consulta)

- Biblioteca de playbooks por tipo de estagnação (ghosting pós-proposta, carrinho abandonado, sem orçamento no momento, precisa de aprovação interna), templates de mensagens por canal (WhatsApp, email, LinkedIn, voz), histórico de mensagens que converteram x que não converteram, tom de voz da marca do cliente, objeções mais comuns e respostas validadas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados do deal, bucket de classificacao, Dossie de Reativacao do Escavador, playbooks de recuperacao configurados, histo…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sequência de recuperação personalizada: N mensagens com canal, timing, copy completo e CTA) e persistir no artefato do squad.
4. Entregar ao critic Critic e Verifier de Mensagens 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sequência de recuperação personalizada: N mensagens com canal, timing, copy completo e CTA
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

- **to:** Critic e Verifier de Mensagens
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
