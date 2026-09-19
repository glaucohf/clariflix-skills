---
task: alarme()
responsavel: "Alarme"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Output do Cronos com breach_window_open=true + árvore de escalonamento configurada (quem notificar em qual sequência por qual tier de risco) + perfil do ticket (id, titulo, agente responsável, cliente, SLA deadline) + disponibilidade dos supervisores de plantão (calendário integrado)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Evidências de escalonamento: (1) Sub-task criada no ClickUp com campos: escalation_timestamp, triggered_by (Cronos score), notified_parties, escalation_channel, recommended_action"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Mensagem Slack enviada com template padronizado incluindo breach_probability, tempo_restante, complexity_score e link direto para o ticket"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Log de escalonamento gravado no Supabase para auditoria e cálculo de KPIs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Status do ticket atualizado no helpdesk"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato verificável: sub-task de escalonamento com timestamp anterior ao breach"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado exclusivamente pelo Sentinela-Mor quando Cronos retorna breach_window_open=true e confidence_level HIGH ou MEDIUM. NUNCA disparado diretamente por outros agents. Requer aprovação humana (HI…"
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

# Escalonar Tickets

**Task ID:** `alarme()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de SLA & Health Monitoring Operacional

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Escalonar Tickets |
| **status** | `pending` |
| **responsible_executor** | Alarme (Alarme — Agente de Escalonamento Proativo) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executor cirúrgico: quando Cronos diz 'vai brechar', Alarme age. Implementa a árvore de escalonamento configurada para o cliente: (1) Atualiza o status do ticket no ClickUp para VERMELHO com justificativa do Cronos; (2) Cria uma sub-task de escalonamento vinculada ao ticket-pai com checklist padronizado (quem foi notificado, quando, por qual canal, qual ação esperada); (3) Notifica o supervisor de plantão via Slack com briefing completo (ticket, SLA deadline, breach probability, complexity score, ação recomendada); (4) Se configurado, reatribui ou adiciona co-responsável ao ticket para aumentar velocidade de resolução; (5) Para P1 com >90% breach probability, cria task de war-room no ClickUp e convoca canal de incidentes. Alarme nunca escala desnecessariamente — opera apenas quando Cronos confirma breach_window_open=true.

## Input

- Output do Cronos com breach_window_open=true + árvore de escalonamento configurada (quem notificar em qual sequência por qual tier de risco) + perfil do ticket (id, titulo, agente responsável, cliente, SLA deadline) + disponibilidade dos supervisores de plantão (calendário integrado)

## Output

- Evidências de escalonamento: (1) Sub-task criada no ClickUp com campos: escalation_timestamp, triggered_by (Cronos score), notified_parties, escalation_channel, recommended_action
- (2) Mensagem Slack enviada com template padronizado incluindo breach_probability, tempo_restante, complexity_score e link direto para o ticket
- (3) Log de escalonamento gravado no Supabase para auditoria e cálculo de KPIs
- (4) Status do ticket atualizado no helpdesk
- Artefato verificável: sub-task de escalonamento com timestamp anterior ao breach

## Trigger

Disparado exclusivamente pelo Sentinela-Mor quando Cronos retorna breach_window_open=true e confidence_level HIGH ou MEDIUM. NUNCA disparado diretamente por outros agents. Requer aprovação humana (HITL L3) para: reatribuição de ticket, convocação de war-room P1, escalonamento para C-level.

## Knowledge base (o que o executor consulta)

- Árvore de escalonamento do cliente (quem é supervisor de cada fila, hierarquia de plantão, canais preferenciais por tier), templates de notificação por severidade (personalizados por cliente), regras de anti-spam de escalonamento (não notificar o mesmo supervisor mais de 1x por ticket a cada 30min), IDs de canais Slack e workspaces ClickUp do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Output do Cronos com breach_window_open=true + árvore de escalonamento configurada (quem notificar em qual sequência po…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Evidências de escalonamento: (1) Sub-task criada no ClickUp com campos: escalation_timestamp, triggered_by (Cronos scor…) e persistir no artefato do squad.
4. Entregar ao critic Cético de SLA; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Evidências de escalonamento: (1) Sub-task criada no ClickUp com campos: escalation_timestamp, triggered_by (Cronos score), notified_parties, escalation_channel…
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

- **to:** Histos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
