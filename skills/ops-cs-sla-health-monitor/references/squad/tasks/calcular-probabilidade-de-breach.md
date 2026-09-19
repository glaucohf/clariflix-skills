---
task: cronos()
responsavel: "Cronos"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Output do Radar (tempo_restante, pct_sla_consumido) + output do Decifra (adjusted_remaining_time, complexity_multiplier) + velocidade de progresso do ticket nas últimas 2h (frequência e qualidade de updates no ClickUp/helpdesk) + carga da fila: quantos outros tickets P1/P2 o mesmo agente tem abertos agora + dados históricos de breach para combinação similar de variáveis"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON por ticket: {breach_probability (0-1), risk_status (VERDE/AMARELO/VERMELHO), estimated_resolution_time_min, sla_deadline, breach_window_open (boolean: true se probabilidade >= threshold configurado), escalation_urgency (IMEDIATA/PROATIVA/MONITORAR), prediction_rationale (texto de 2-3 frases explicando o score), confidence_level (HIGH/MEDIUM/LOW"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "LOW quando dados insuficientes)}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Sentinela-Mor após receber outputs do Radar e do Decifra. É o gate que decide se Agente de Escalonamento será ativado: apenas tickets com breach_window_open=true e confidence_level !=…"
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

# Calcular Probabilidade De Breach

**Task ID:** `cronos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de SLA & Health Monitoring Operacional

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Probabilidade De Breach |
| **status** | `pending` |
| **responsible_executor** | Cronos (Cronos — Motor de Previsão de Breach) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

O cérebro preditivo do squad. Combina 4 inputs — tempo restante nominal, adjusted_remaining_time (pós-Decifra), ritmo de progresso nas últimas 2h (velocidade de atualizações no ticket) e carga atual da fila do agente responsável — para calcular a 'probabilidade de breach' com um modelo de scoring ponderado. Cronos não usa ML pesado: usa uma função determinística calibrada com pesos históricos (mais interpretável, mais auditável, mais confiável para o cliente ver). Output principal: status de risco (VERDE < 40%, AMARELO 40-70%, VERMELHO >70%) + tempo estimado de resolução vs. deadline + janela de escalonamento recomendada ('você tem 2h para agir antes do ponto sem retorno').

## Input

- Output do Radar (tempo_restante, pct_sla_consumido) + output do Decifra (adjusted_remaining_time, complexity_multiplier) + velocidade de progresso do ticket nas últimas 2h (frequência e qualidade de updates no ClickUp/helpdesk) + carga da fila: quantos outros tickets P1/P2 o mesmo agente tem abertos agora + dados históricos de breach para combinação similar de variáveis

## Output

- JSON por ticket: {breach_probability (0-1), risk_status (VERDE/AMARELO/VERMELHO), estimated_resolution_time_min, sla_deadline, breach_window_open (boolean: true se probabilidade >= threshold configurado), escalation_urgency (IMEDIATA/PROATIVA/MONITORAR), prediction_rationale (texto de 2-3 frases explicando o score), confidence_level (HIGH/MEDIUM/LOW
- LOW quando dados insuficientes)}

## Trigger

Disparado pelo Sentinela-Mor após receber outputs do Radar e do Decifra. É o gate que decide se Agente de Escalonamento será ativado: apenas tickets com breach_window_open=true e confidence_level != LOW são passados para escalonamento.

## Knowledge base (o que o executor consulta)

- Pesos calibrados do modelo de previsão (armazenados no Supabase, recalibrados mensalmente), histórico de breaches reais com variáveis de contexto (dataset de treino/validação), threshold de escalonamento por tier de SLA (configurável: default P1=70%, P2=65%, P3=60%), perfis de carga histórica da fila por dia da semana e horário

## Action Items

1. Confirmar o gatilho e carregar a entrada (Output do Radar (tempo_restante, pct_sla_consumido) + output do Decifra (adjusted_remaining_time, complexity_multiplier…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON por ticket: {breach_probability (0-1), risk_status (VERDE/AMARELO/VERMELHO), estimated_resolution_time_min, sla_de…) e persistir no artefato do squad.
4. Entregar ao critic Cético de SLA; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON por ticket: {breach_probability (0-1), risk_status (VERDE/AMARELO/VERMELHO), estimated_resolution_time_min, sla_deadline, breach_window_open (boolean: tru…
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

- **to:** Alarme
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
