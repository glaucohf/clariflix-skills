---
task: intell()
responsavel: "Intell"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados do lead do CRM (nome, empresa, cargo, LinkedIn URL se disponível)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "booking_confirmation.json com data/hora da reunião"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso a ferramentas de enriquecimento (Apollo, Clay ou alternativa configurada)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Briefing pré-reunião em markdown: perfil do decisor, contexto da empresa, possíveis dores/oportunidades identificadas, sugestão de abertura personalizada, histórico de interações anteriores com a empresa"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Enviado ao closer via CRM + notificação (email ou Slack)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato: pre_meeting_brief.md"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Agendamento confirmado (confirmation_status = CONFIRMED). Reunião em menos de 24h sem briefing gerado."
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

# Enriquecer Dossiê Lead

**Task ID:** `intell()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Agendamento — Appointment Setting

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dossiê Lead |
| **status** | `pending` |
| **responsible_executor** | Intell (Intell — Worker de Enriquecimento pré-Reunião) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Prepara o dossiê do lead para o closer antes da reunião. Pesquisa empresa e decisor nas fontes disponíveis (LinkedIn, site, notícias recentes, dados do CRM), identifica contexto atual da empresa (crescimento, expansão, contratações recentes, sinais de dor), e gera um briefing executivo de 1 página para o closer entrar na call bem preparado. Roda automaticamente após confirmação da reunião.

## Input

- Dados do lead do CRM (nome, empresa, cargo, LinkedIn URL se disponível)
- booking_confirmation.json com data/hora da reunião
- Acesso a ferramentas de enriquecimento (Apollo, Clay ou alternativa configurada)

## Output

- Briefing pré-reunião em markdown: perfil do decisor, contexto da empresa, possíveis dores/oportunidades identificadas, sugestão de abertura personalizada, histórico de interações anteriores com a empresa
- Enviado ao closer via CRM + notificação (email ou Slack)
- Artefato: pre_meeting_brief.md

## Trigger

Agendamento confirmado (confirmation_status = CONFIRMED). Reunião em menos de 24h sem briefing gerado.

## Knowledge base (o que o executor consulta)

- Acesso a Apollo/Clay para dados de empresa e contato, templates de briefing por vertical/segmento, histórico de CRM da empresa/contato, playbook de abertura de reuniões por tipo de cliente, ICP detalhado com sinais de dor por segmento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados do lead do CRM (nome, empresa, cargo, LinkedIn URL se disponível)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Briefing pré-reunião em markdown: perfil do decisor, contexto da empresa, possíveis dores/oportunidades identificadas,…) e persistir no artefato do squad.
4. Entregar ao critic Sentinela; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Briefing pré-reunião em markdown: perfil do decisor, contexto da empresa, possíveis dores/oportunidades identificadas, sugestão de abertura personalizada, hist…
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

- **to:** Pulse
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
