---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de Score Objects atualizados"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Calendário e capacidade de cada rep (via integração CRM/Google Calendar)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Histórico de tentativas de contato por lead"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Regras de território e segmento configuradas pelo gestor"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Fila_do_Dia por rep em formato ClickUp Task List: ordenada por (score * urgência * dias_sem_contato)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Cada item contém: lead_id, nome, empresa, score, categoria, next_best_action, canal_recomendado, contexto_resumido (3 bullets do Sherlock), link direto para CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alerta de leads Hot sem contato em 24h enviado via WhatsApp/Slack para o gestor"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job diário as 08h após ciclo de re-scoring. Evento score_updated para Hot leads (rebalanceia fila imediatamente). Evento lead_uncontacted_48h. Solicitação manual do gestor via comando no Slack/WhatsA…"
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

# Priorizar Fila De Contato

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Lead Scoring Preditivo e Priorização

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Priorizar Fila De Contato |
| **status** | `pending` |
| **responsible_executor** | Atlas (Estrategista de Prioridade (Atlas)) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de roteamento e priorização. Recebe todos os scores atualizados e monta a fila priorizada do dia para cada SDR/Closer considerando: score do lead, disponibilidade do rep, território/segmento, stage do funil, SLA de próximo contato. Redistribui leads parados há mais de 48h sem tentativa de contato.

## Input

- Lista de Score Objects atualizados
- Calendário e capacidade de cada rep (via integração CRM/Google Calendar)
- Histórico de tentativas de contato por lead
- Regras de território e segmento configuradas pelo gestor

## Output

- Fila_do_Dia por rep em formato ClickUp Task List: ordenada por (score * urgência * dias_sem_contato)
- Cada item contém: lead_id, nome, empresa, score, categoria, next_best_action, canal_recomendado, contexto_resumido (3 bullets do Sherlock), link direto para CRM
- Alerta de leads Hot sem contato em 24h enviado via WhatsApp/Slack para o gestor

## Trigger

Job diário as 08h após ciclo de re-scoring. Evento score_updated para Hot leads (rebalanceia fila imediatamente). Evento lead_uncontacted_48h. Solicitação manual do gestor via comando no Slack/WhatsApp.

## Knowledge base (o que o executor consulta)

- Regras de território e segmento do cliente
- Capacidade diária por rep (ex: SDR faz max 40 tentativas/dia)
- Histórico de conversão por rep x tipo de lead para otimização de matching
- SLAs de contato por categoria (Hot: contato em max 2h, Warm: max 24h, Cold: nurture automático)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de Score Objects atualizados).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Fila_do_Dia por rep em formato ClickUp Task List: ordenada por (score * urgência * dias_sem_contato)) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Fila_do_Dia por rep em formato ClickUp Task List: ordenada por (score * urgência * dias_sem_contato)
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
