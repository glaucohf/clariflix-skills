---
task: pulse()
responsavel: "Pulse"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Eventos de engajamento do CRM e plataformas de email/WhatsApp (opens, clicks, replies, page views)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Dados firmográficos do lead (empresa, cargo, segmento, tamanho)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Histórico de interações"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score atualizado por lead (0-100) com breakdown por dimensão (fit, intent, engagement)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Fila priorizada de leads para ação imediata"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alertas de lead esquentando (score subiu 20+ pontos em 24h)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "CRM atualizado com campo lead_score e priority_tier (HOT/WARM/COLD)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato: lead_priority_queue.json"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento de engajamento detectado (email aberto, link clicado, mensagem respondida). Rotina diária de re-scoring (6h da manhã). Lead sem interação por X dias (re-score para baixo)."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinela antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar abordagem e personalização antes do envio."
    - "[ ] L3: Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial fora da política padrão)."
    - "[ ] L3: Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nova tentativa."
    - "[ ] L2: Notificação ao closer/SDR quando lead muda de COLD para HOT (score sobe 30+ pontos em 24h) para decisão de abordar manualmente em vez de deixar o squad rodar sozinho."
    - "[ ] L2: Alerta ao gerente de vendas quando taxa de no-show da semana ultrapassar threshold configurado (ex: >20%) — indica problema sistêmico que requer revisão de ICP ou abordagem."
---

# Priorizar Leads

**Task ID:** `pulse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Agendamento — Appointment Setting

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Priorizar Leads |
| **status** | `pending` |
| **responsible_executor** | Pulse (Pulse — Worker de Lead Scoring e Priorização) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pontua e re-ranqueia leads continuamente com base em sinais de comportamento (abertura de email, clique em link, visita ao site, resposta no WhatsApp, tempo sem interação) e dados firmográficos. Define qual lead deve ser abordado primeiro pelo Maestro e qual cadência de intensidade aplicar (quente, morno, frio). Alimenta o Maestro com fila priorizada para maximizar conversão por slot de vendedor.

## Input

- Eventos de engajamento do CRM e plataformas de email/WhatsApp (opens, clicks, replies, page views)
- Dados firmográficos do lead (empresa, cargo, segmento, tamanho)
- Histórico de interações

## Output

- Score atualizado por lead (0-100) com breakdown por dimensão (fit, intent, engagement)
- Fila priorizada de leads para ação imediata
- Alertas de lead esquentando (score subiu 20+ pontos em 24h)
- CRM atualizado com campo lead_score e priority_tier (HOT/WARM/COLD)
- Artefato: lead_priority_queue.json

## Trigger

Evento de engajamento detectado (email aberto, link clicado, mensagem respondida). Rotina diária de re-scoring (6h da manhã). Lead sem interação por X dias (re-score para baixo).

## Knowledge base (o que o executor consulta)

- Modelo de scoring do cliente (pesos por sinal), dados históricos de conversão (quais scores fecharam, quais não fecharam), regras de decaimento de score por inatividade, ICP e critérios de fit por segmento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Eventos de engajamento do CRM e plataformas de email/WhatsApp (opens, clicks, replies, page views)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score atualizado por lead (0-100) com breakdown por dimensão (fit, intent, engagement)) e persistir no artefato do squad.
4. Entregar ao critic Sentinela; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score atualizado por lead (0-100) com breakdown por dimensão (fit, intent, engagement)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinela registrado
- [ ] Gate L3 respeitado: Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar…
- [ ] Gate L3 respeitado: Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial…
- [ ] Gate L3 respeitado: Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nov…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar abordagem e persona… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial fora da política pad… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nova tentativa. | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Notificação ao closer/SDR quando lead muda de COLD para HOT (score sobe 30+ pontos em 24h) para decisão de abordar manualmente em vez de deixar o squad rodar s… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Alerta ao gerente de vendas quando taxa de no-show da semana ultrapassar threshold configurado (ex: >20%) — indica problema sistêmico que requer revisão de ICP… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão humana do briefing pre-reunião antes do envio ao closer, opcional mas recomendado nas primeiras 2 semanas de operação do squad para calibragem. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Sentinela | BLOQUEIA entrega |

## Handoff

- **to:** Sentinela
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
