---
task: ancora()
responsavel: "Âncora"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Outputs de todos os agents do ciclo (Radar manifesto, Decifra complexity scores, Cronos breach probabilities, Alarme escalation records) + resultado final de cada ticket (breachado ou não, ao fechar o ticket) + configurações do dashboard (métricas a exibir, período de referência)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Por ticket monitorado: campo 'sla_monitor_log' atualizado no ClickUp com linha de log do ciclo atual (timestamp, breach_probability, status, ação_tomada)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Por escalonamento: sub-task de evidência criada/atualizada com todos os campos auditáveis"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard de KPIs atualizado em tempo real no ClickUp (widget ou view customizada): breach_rate_7d, avg_antecedencia_horas, sla_compliance_pct por tier, escalonamentos_disparados_vs_breaches_evitados"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Log estruturado no Supabase para auditoria e recalibração do Histos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Sentinela-Mor ao final de cada ciclo, após consolidar outputs de todos os workers. Também disparado ao fechar um ticket (resultado final para cálculo de KPIs). Trigger de dashboard ref…"
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

# Registrar Prova De Trabalho

**Task ID:** `ancora()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de SLA & Health Monitoring Operacional

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Registrar Prova De Trabalho |
| **status** | `pending` |
| **responsible_executor** | Âncora (Âncora — Registrador de Evidências e Prova de Trabalho) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Garante que cada ação do squad seja registrada como prova de trabalho auditável — o requisito não-negociável do modelo Lendar[IA]. Para cada ciclo de monitoramento, grava no ClickUp e no Supabase o log estruturado: qual ticket foi avaliado, qual score Cronos atribuiu, se escalonamento foi disparado, resultado final (breach evitado / breach ocorreu). Para cada escalonamento do Alarme, grava o artefato completo com timestamp, score que trigou, ação tomada e resultado. Produz o campo 'sla_monitor_log' em cada ticket monitorado — string legível que o supervisor pode ler para entender o que o squad fez. Também gerencia o dashboard de KPIs em tempo real no ClickUp (% breaches evitados, antecedência média dos alertas, SLA compliance por tier).

## Input

- Outputs de todos os agents do ciclo (Radar manifesto, Decifra complexity scores, Cronos breach probabilities, Alarme escalation records) + resultado final de cada ticket (breachado ou não, ao fechar o ticket) + configurações do dashboard (métricas a exibir, período de referência)

## Output

- Por ticket monitorado: campo 'sla_monitor_log' atualizado no ClickUp com linha de log do ciclo atual (timestamp, breach_probability, status, ação_tomada)
- Por escalonamento: sub-task de evidência criada/atualizada com todos os campos auditáveis
- Dashboard de KPIs atualizado em tempo real no ClickUp (widget ou view customizada): breach_rate_7d, avg_antecedencia_horas, sla_compliance_pct por tier, escalonamentos_disparados_vs_breaches_evitados
- Log estruturado no Supabase para auditoria e recalibração do Histos

## Trigger

Disparado pelo Sentinela-Mor ao final de cada ciclo, após consolidar outputs de todos os workers. Também disparado ao fechar um ticket (resultado final para cálculo de KPIs). Trigger de dashboard refresh a cada 1h para métricas agregadas.

## Knowledge base (o que o executor consulta)

- Schema do banco de logs no Supabase (estrutura dos registros de auditoria), IDs dos campos customizados no ClickUp para escrita de logs, template do artefato de prova de trabalho, metas de KPI configuradas pelo cliente (para colorir o dashboard: verde/amarelo/vermelho por threshold)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Outputs de todos os agents do ciclo (Radar manifesto, Decifra complexity scores, Cronos breach probabilities, Alarme es…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Por ticket monitorado: campo 'sla_monitor_log' atualizado no ClickUp com linha de log do ciclo atual (timestamp, breach…) e persistir no artefato do squad.
4. Entregar ao critic Cético de SLA; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Por ticket monitorado: campo 'sla_monitor_log' atualizado no ClickUp com linha de log do ciclo atual (timestamp, breach_probability, status, ação_tomada)
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

- **to:** Cético de SLA
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
