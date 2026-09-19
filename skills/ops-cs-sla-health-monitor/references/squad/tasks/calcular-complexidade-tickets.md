---
task: decifra()
responsavel: "Decifra"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ticket do manifesto do Radar + histórico de resolução dos últimos 90 dias para tickets do mesmo tipo (segmentado por intenção L2 + módulo) + perfil do agente responsável (tempo médio de resolução histórico por tipo) + flags de dependência externa (campo no ClickUp: awaiting_third_party, awaiting_approval, awaiting_customer_data)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON por ticket: {complexity_score (1-5), complexity_multiplier (0.5-3.0), complexity_breakdown: {reopening_rate, external_deps_flag, module_complexity, investigation_depth, agent_velocity_score}, adjusted_remaining_time_min (= tempo_restante / complexity_multiplier), complexity_rationale (texto de 1 frase)}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Sentinela-Mor em paralelo com Cálculo de Ritmo para cada ticket no manifesto do Radar. Re-executado quando agente responsável é trocado (reatribuição muda o velocity_score)."
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

# Calcular Complexidade Tickets

**Task ID:** `decifra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de SLA & Health Monitoring Operacional

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Complexidade Tickets |
| **status** | `pending` |
| **responsible_executor** | Decifra (Decifra — Analisadora de Complexidade) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Enriquece cada ticket com um score de complexidade real — o componente que o SLA padrão ignora e que é a causa #1 de breaches surpresa. Avalia 5 dimensões: (1) Histórico de reabertura: este tipo de ticket costuma ser reaberto? (2) Dependências externas: ticket está aguardando aprovação, terceiro, ou dado do cliente? (3) Módulo/componente afetado: qual a complexidade histórica de tickets deste módulo? (4) Profundidade de investigação necessária: bug de prod vs. dúvida de uso vs. configuração? (5) Agente atual: qual o tempo médio de resolução do agente responsável para este tipo? Combina as 5 dimensões em um Complexity Multiplier (0.5x a 3.0x) que é aplicado ao tempo restante nominal — um ticket com SLA de 4h mas Complexity Multiplier 2.0x efetivamente tem 2h de 'trabalho real' disponível.

## Input

- Ticket do manifesto do Radar + histórico de resolução dos últimos 90 dias para tickets do mesmo tipo (segmentado por intenção L2 + módulo) + perfil do agente responsável (tempo médio de resolução histórico por tipo) + flags de dependência externa (campo no ClickUp: awaiting_third_party, awaiting_approval, awaiting_customer_data)

## Output

- JSON por ticket: {complexity_score (1-5), complexity_multiplier (0.5-3.0), complexity_breakdown: {reopening_rate, external_deps_flag, module_complexity, investigation_depth, agent_velocity_score}, adjusted_remaining_time_min (= tempo_restante / complexity_multiplier), complexity_rationale (texto de 1 frase)}

## Trigger

Disparado pelo Sentinela-Mor em paralelo com Cálculo de Ritmo para cada ticket no manifesto do Radar. Re-executado quando agente responsável é trocado (reatribuição muda o velocity_score).

## Knowledge base (o que o executor consulta)

- Base histórica de resolução segmentada por tipo de intenção + módulo + agente (Supabase), score de complexidade por módulo do produto (mantido pelo ops lead), perfis de velocidade dos agentes (anonimizados para feedback, identificados para roteamento interno), taxas históricas de reabertura por categoria de ticket

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ticket do manifesto do Radar + histórico de resolução dos últimos 90 dias para tickets do mesmo tipo (segmentado por in…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON por ticket: {complexity_score (1-5), complexity_multiplier (0.5-3.0), complexity_breakdown: {reopening_rate, exter…) e persistir no artefato do squad.
4. Entregar ao critic Cético de SLA; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON por ticket: {complexity_score (1-5), complexity_multiplier (0.5-3.0), complexity_breakdown: {reopening_rate, external_deps_flag, module_complexity, invest…
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

- **to:** Cronos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
