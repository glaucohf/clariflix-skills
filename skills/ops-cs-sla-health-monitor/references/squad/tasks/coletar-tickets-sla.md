---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Polling periódico (trigger de 15min pelo Sentinela-Mor) → chamada às APIs do ClickUp e helpdesk integrado (Zendesk/Intercom) buscando tickets com campo sla_deadline não-nulo e status != 'closed'"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Parâmetros de configuração: lista de status que pausam o clock SLA (ex: 'awaiting_customer'), timezone do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON list de tickets-ativos-com-SLA: [{ticket_id, titulo, tipo_intencao, tier_cliente, agente_responsavel, sla_deadline, tempo_restante_min, pct_sla_consumido, status_clock (RUNNING/PAUSED), ultimo_update_timestamp, canal_origem}]"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tickets com pct_sla_consumido >= 50% são marcados como PRIORITY para processamento imediato pelos workers seguintes"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Trigger automático a cada 15 minutos pelo Sentinela-Mor via scheduler interno. Re-trigger imediato quando novo ticket P1 é criado no ClickUp (webhook). Re-trigger manual por supervisor via comando no…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Cético de SLA antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade baixa (interrompe o fluxo do agente atual)."
    - "[ ] HITL: Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders. Ação de alto impacto e irreversível em termos de alarme organizacional."
    - "[ ] HITL: Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes do envio. Toda comunicação com cliente é revisada por humano."
    - "[ ] HITL: Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. Ocorre quando dados são ambíguos ou incompletos."
    - "[ ] HITL: Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para avaliação manual do risco de breach. Cronos não especula sem dados."
---

# Coletar Tickets Sla

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de SLA & Health Monitoring Operacional

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coletar Tickets Sla |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Varredor de Fila SLA) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em coleta e normalização de estado: a cada ciclo de 15 minutos, faz o pull de todos os tickets abertos com SLA ativo dos sistemas de origem (ClickUp + helpdesk integrado), normaliza os dados em um schema padronizado (id, tipo, tier, tempo_aberto, sla_deadline, agente_responsável, status, último_update, status_de_espera), e calcula os campos derivados básicos: tempo_decorrido, tempo_restante, porcentagem_consumida do SLA. Filtra tickets sem SLA configurado e tickets em status 'aguardando cliente' (pausa o clock conforme regra contratual). Produz o manifesto de tickets-sob-risco que alimenta os demais workers.

## Input

- Polling periódico (trigger de 15min pelo Sentinela-Mor) → chamada às APIs do ClickUp e helpdesk integrado (Zendesk/Intercom) buscando tickets com campo sla_deadline não-nulo e status != 'closed'
- Parâmetros de configuração: lista de status que pausam o clock SLA (ex: 'awaiting_customer'), timezone do cliente

## Output

- JSON list de tickets-ativos-com-SLA: [{ticket_id, titulo, tipo_intencao, tier_cliente, agente_responsavel, sla_deadline, tempo_restante_min, pct_sla_consumido, status_clock (RUNNING/PAUSED), ultimo_update_timestamp, canal_origem}]
- Tickets com pct_sla_consumido >= 50% são marcados como PRIORITY para processamento imediato pelos workers seguintes

## Trigger

Trigger automático a cada 15 minutos pelo Sentinela-Mor via scheduler interno. Re-trigger imediato quando novo ticket P1 é criado no ClickUp (webhook). Re-trigger manual por supervisor via comando no Slack ('!sla-scan-now').

## Knowledge base (o que o executor consulta)

- Configuração de SLA por tier de cliente e tipo de intenção (documento vivo no ClickUp), regras de pausa de clock (quais status congelam o SLA), lista de tickets excluídos do monitoramento (edge cases contratualmente acordados), mapeamento de IDs de campos customizados no ClickUp/Zendesk para o schema interno

## Action Items

1. Confirmar o gatilho e carregar a entrada (Polling periódico (trigger de 15min pelo Sentinela-Mor) → chamada às APIs do ClickUp e helpdesk integrado (Zendesk/Inte…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON list de tickets-ativos-com-SLA: [{ticket_id, titulo, tipo_intencao, tier_cliente, agente_responsavel, sla_deadline…) e persistir no artefato do squad.
4. Entregar ao critic Cético de SLA; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON list de tickets-ativos-com-SLA: [{ticket_id, titulo, tipo_intencao, tier_cliente, agente_responsavel, sla_deadline, tempo_restante_min, pct_sla_consumido,…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Cético de SLA registrado
- [ ] Gate HITL respeitado: Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executa…
- [ ] Gate HITL respeitado: Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar mú…
- [ ] Gate HITL respeitado: Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade b… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. O… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para a… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Histos detecta breach rate semanal acima do threshold crítico: relatório é revisado por ops manager antes de publicação, que decide se aciona revisão de proces… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Recalibração mensal do modelo do Cronos (Histos gera novo dataset): pesos atualizados são revisados por ops lead antes de ir para produção. Mudança no modelo p… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Cético de SLA | BLOQUEIA entrega |

## Handoff

- **to:** Decifra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
