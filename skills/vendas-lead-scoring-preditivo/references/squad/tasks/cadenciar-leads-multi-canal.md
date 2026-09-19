---
task: nexus()
responsavel: "Nexus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Fila_do_Dia do Atlas com categoria e next_best_action"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Lead Object completo com firmograficos e trigger events"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Templates de cadência configurados por segmento/persona"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Score e top features explicativas do Vega"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Para Cold/Warm: rascunho de mensagem personalizada (email/WhatsApp) passado pelo Critic antes do envio"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Sequência de follow-up agendada no CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para Hot: Briefing do Lead em PDF/Notion (empresa, cargo, trigger events, histórico de interações, ângulos de abertura sugeridos, objeções previstas) + Task urgente no ClickUp para SDR"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Log de cada ação no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Fila_do_Dia gerada pelo Atlas. Evento score_category_changed para Cold->Warm ou Warm->Hot. Evento lead_unresponded após 3 tentativas (escala para gestor). Timer de cadência (D+1, D+3, D+7, D+14 confi…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes do disparo. SLA de aprovação: 2h."
    - "[ ] HITL: HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do Closer ou Gerente Comercial."
    - "[ ] HITL: HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos."
    - "[ ] HITL: HITL-4 (L3): Alerta de deal em risco alto — gestor recebe notificação e deve confirmar qual ação tomar (intervir diretamente, escalar para diretor, ajustar proposta) antes de qualquer comunicação automatizada."
    - "[ ] HITL: HITL-5 (L2): Ajuste manual de score por SDR — SDR pode adicionar nota qualitativa (ex: 'falei com o CEO, orçamento confirmado') que sobe o score manualmente, com registro no log de auditoria."
---

# Cadenciar Leads Multi Canal

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Lead Scoring Preditivo e Priorização

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Cadenciar Leads Multi Canal |
| **status** | `pending` |
| **responsible_executor** | Nexus (Cadenciador Inteligente (Nexus)) |
| **execution_type** | `Hybrid` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de outreach e nurture. Para leads Warm e Cold, executa cadências automatizadas multi-canal (email, WhatsApp) com personalização baseada nos dados do Sherlock e do score. Para leads Hot, prepara briefing personalizado e cria tarefa urgente para o SDR humano. Nunca envia mensagem para Hot sem aprovação humana (L3 gate).

## Input

- Fila_do_Dia do Atlas com categoria e next_best_action
- Lead Object completo com firmograficos e trigger events
- Templates de cadência configurados por segmento/persona
- Score e top features explicativas do Vega

## Output

- Para Cold/Warm: rascunho de mensagem personalizada (email/WhatsApp) passado pelo Critic antes do envio
- Sequência de follow-up agendada no CRM
- Para Hot: Briefing do Lead em PDF/Notion (empresa, cargo, trigger events, histórico de interações, ângulos de abertura sugeridos, objeções previstas) + Task urgente no ClickUp para SDR
- Log de cada ação no CRM

## Trigger

Fila_do_Dia gerada pelo Atlas. Evento score_category_changed para Cold->Warm ou Warm->Hot. Evento lead_unresponded após 3 tentativas (escala para gestor). Timer de cadência (D+1, D+3, D+7, D+14 configurável).

## Knowledge base (o que o executor consulta)

- Biblioteca de templates por segmento (imobiliária, agência, B2B serviços) e persona (CEO, Diretor Comercial, SDR)
- Histórico de taxa de resposta por template x segmento para A/B selection
- Regras de horário de envio por canal (WhatsApp: 9h-18h seg-sex)
- Blacklist de contatos opt-out
- Limite diário de mensagens por conta para evitar spam

## Action Items

1. Confirmar o gatilho e carregar a entrada (Fila_do_Dia do Atlas com categoria e next_best_action).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Para Cold/Warm: rascunho de mensagem personalizada (email/WhatsApp) passado pelo Critic antes do envio) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Para Cold/Warm: rascunho de mensagem personalizada (email/WhatsApp) passado pelo Critic antes do envio
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes d…
- [ ] Gate HITL respeitado: HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do…
- [ ] Gate HITL respeitado: HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes do disparo. SLA de ap… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do Closer ou Gerente C… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL-4 (L3): Alerta de deal em risco alto — gestor recebe notificação e deve confirmar qual ação tomar (intervir diretamente, escalar para diretor, ajustar pro… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL-5 (L2): Ajuste manual de score por SDR — SDR pode adicionar nota qualitativa (ex: 'falei com o CEO, orçamento confirmado') que sobe o score manualmente, c… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL-6 (L1): Calibração mensal do modelo de scoring — analista de RevOps revisa os feature weights sugeridos pelo sistema e aprova ou ajusta antes do re-treino. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Oracle
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
