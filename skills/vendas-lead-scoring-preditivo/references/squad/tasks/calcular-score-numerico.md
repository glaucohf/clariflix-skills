---
task: vega()
responsavel: "Vega"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead Object enriquecido (Sherlock output) OU evento de re-scoring (engajamento, mudança de estágio, passagem de tempo)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Feature vector completo com os 15-20 campos definidos no Blueprint"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score Object: {lead_id, score_atual: 0-100, categoria: Hot|Warm|Cold|Disqualified, score_anterior, delta, top_3_features_explicativas[], probabilidade_conversão_pct, next_best_action, recomendação_canal, urgência_nível: 1-5, score_timestamp}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Grava no CRM e publica evento score_updated"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento lead_enriched do Sherlock. Evento engagement_detected (email aberto, link clicado, WhatsApp respondido, page view). Job diário de re-scoring de toda base ativa as 07h. Evento stage_changed no…"
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

# Calcular Score Numerico

**Task ID:** `vega()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Lead Scoring Preditivo e Priorização

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Score Numerico |
| **status** | `pending` |
| **responsible_executor** | Vega (Calculista de Score (Vega)) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de scoring preditivo. Aplica o modelo de scoring calibrado no Blueprint sobre o Lead Object enriquecido, gera o score numérico (0-100) e a categoria (Hot/Warm/Cold/Disqualified), calcula o delta em relação ao score anterior e identifica quais features mais contribuíram para o score (explicabilidade para o SDR).

## Input

- Lead Object enriquecido (Sherlock output) OU evento de re-scoring (engajamento, mudança de estágio, passagem de tempo)
- Feature vector completo com os 15-20 campos definidos no Blueprint

## Output

- Score Object: {lead_id, score_atual: 0-100, categoria: Hot|Warm|Cold|Disqualified, score_anterior, delta, top_3_features_explicativas[], probabilidade_conversão_pct, next_best_action, recomendação_canal, urgência_nível: 1-5, score_timestamp}
- Grava no CRM e publica evento score_updated

## Trigger

Evento lead_enriched do Sherlock. Evento engagement_detected (email aberto, link clicado, WhatsApp respondido, page view). Job diário de re-scoring de toda base ativa as 07h. Evento stage_changed no CRM.

## Knowledge base (o que o executor consulta)

- Modelo de scoring serializado (pickle/ONNX) treinado com histórico de closed-won e closed-lost do cliente
- Feature weights atualizados mensalmente
- Thresholds calibrados por segmento (SMB vs Enterprise podem ter thresholds distintos)
- Tabela de decaimento temporal (lead sem engajamento há X dias perde Y pontos)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead Object enriquecido (Sherlock output) OU evento de re-scoring (engajamento, mudança de estágio, passagem de tempo)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score Object: {lead_id, score_atual: 0-100, categoria: Hot|Warm|Cold|Disqualified, score_anterior, delta, top_3_feature…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score Object: {lead_id, score_atual: 0-100, categoria: Hot|Warm|Cold|Disqualified, score_anterior, delta, top_3_features_explicativas[], probabilidade_conversã…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
