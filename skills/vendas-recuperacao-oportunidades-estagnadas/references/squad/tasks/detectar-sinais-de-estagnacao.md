---
task: workerDeDeteccaoETriagem()
responsavel: "Worker de Detecção e Triagem"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Webhooks do CRM (deal updated/stalled), polling diário de deals, eventos de abandono de carrinho, logs de engajamento de email/WhatsApp"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Fila priorizada de oportunidades estagnadas com Score de Urgência, bucket de classificação (Salvar Agora / Nutrir / Reciclar / Arquivar) e contexto completo do deal"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato: stagnation-report-{date}.json no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Deal sem atividade por mais de N dias (configurável por etapa: 3 dias em Proposta, 7 dias em Qualificação, 1 dia em Carrinho Abandonado), mudança de status para Stalled no CRM, trigger manual pelo co…"
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

# Detectar Sinais De Estagnação

**Task ID:** `workerDeDeteccaoETriagem()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Recuperação de Oportunidades Estagnadas

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Sinais De Estagnação |
| **status** | `pending` |
| **responsible_executor** | Worker de Detecção e Triagem (Radar (Worker de Detecção e Triagem)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente o CRM e plataformas de e-commerce em busca de sinais de estagnação: deals sem atividade há N dias, carrinhos abandonados, leads que não responderam ao último contato, oportunidades com data de fechamento ultrapassada. Calcula Score de Urgência (valor x probabilidade x dias parado x sinais externos) e gera a fila priorizada de recuperação. Alimenta o Orquestrador com contexto completo de cada deal.

## Input

- Webhooks do CRM (deal updated/stalled), polling diário de deals, eventos de abandono de carrinho, logs de engajamento de email/WhatsApp

## Output

- Fila priorizada de oportunidades estagnadas com Score de Urgência, bucket de classificação (Salvar Agora / Nutrir / Reciclar / Arquivar) e contexto completo do deal
- Artefato: stagnation-report-{date}.json no ClickUp

## Trigger

Deal sem atividade por mais de N dias (configurável por etapa: 3 dias em Proposta, 7 dias em Qualificação, 1 dia em Carrinho Abandonado), mudança de status para Stalled no CRM, trigger manual pelo comercial

## Knowledge base (o que o executor consulta)

- Regras de estagnação por etapa do funil, histórico de deals perdidos (padrões), SLA de resposta por tier de cliente, configuração de N dias por etapa, mapa de estágios do funil no CRM do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Webhooks do CRM (deal updated/stalled), polling diário de deals, eventos de abandono de carrinho, logs de engajamento d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Fila priorizada de oportunidades estagnadas com Score de Urgência, bucket de classificação (Salvar Agora / Nutrir / Rec…) e persistir no artefato do squad.
4. Entregar ao critic Critic e Verifier de Mensagens 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Fila priorizada de oportunidades estagnadas com Score de Urgência, bucket de classificação (Salvar Agora / Nutrir / Reciclar / Arquivar) e contexto completo do…
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

- **to:** Escavador
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
