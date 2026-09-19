---
task: oracle()
responsavel: "Oracle"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Todos os deals em estágio Proposta e Negociação do CRM"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Histórico de atividades (emails, calls, reuniões) com timestamps"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Score atual e histórico de delta de score dos últimos 14 dias"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Benchmark de ciclo de vendas por segmento/tamanho de deal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Deal Risk Report semanal (Sexta 17h): lista de deals com risco ALTO/MEDIO/BAIXO com justificativa"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alerta imediato via Slack/WhatsApp para o gestor quando deal score cai >15 pontos em 48h ou quando há silêncio >5 dias em deal Hot"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Forecast de revenue com P50/P75/P90 para o mês corrente e próximo"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Recomendação de ação por deal em risco"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job semanal Sexta 17h. Evento score_delta_high (queda > 15 pontos). Evento deal_silence_detected (sem atividade em deal avançado por X dias). Solicitação manual do gestor."
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

# Detectar Risco Deal

**Task ID:** `oracle()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Lead Scoring Preditivo e Priorização

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Risco Deal |
| **status** | `pending` |
| **responsible_executor** | Oracle (Analista de Risco de Deal (Oracle)) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de forecast e detecção de risco. Monitora deals em estágio avançado (Proposta/Negociação) e emite alertas quando sinais indicam risco de churn do deal: ausência de engajamento, mudança de stakeholder, ciclo alongado vs benchmark, redução de frequência de contato. Também gera forecast semanal de revenue com intervalo de confiança.

## Input

- Todos os deals em estágio Proposta e Negociação do CRM
- Histórico de atividades (emails, calls, reuniões) com timestamps
- Score atual e histórico de delta de score dos últimos 14 dias
- Benchmark de ciclo de vendas por segmento/tamanho de deal

## Output

- Deal Risk Report semanal (Sexta 17h): lista de deals com risco ALTO/MEDIO/BAIXO com justificativa
- Alerta imediato via Slack/WhatsApp para o gestor quando deal score cai >15 pontos em 48h ou quando há silêncio >5 dias em deal Hot
- Forecast de revenue com P50/P75/P90 para o mês corrente e próximo
- Recomendação de ação por deal em risco

## Trigger

Job semanal Sexta 17h. Evento score_delta_high (queda > 15 pontos). Evento deal_silence_detected (sem atividade em deal avançado por X dias). Solicitação manual do gestor.

## Knowledge base (o que o executor consulta)

- Histórico de closed-won e closed-lost com timeline de atividades (para calcular benchmark de ciclo saudável)
- Sinais de churn de deal validados historicamente (ex: 3 emails sem resposta em proposta = 72% chance de perda)
- Modelo de forecast (pipeline-based weighting por score e estágio)
- Contatos de stakeholders por deal para detectar mudança

## Action Items

1. Confirmar o gatilho e carregar a entrada (Todos os deals em estágio Proposta e Negociação do CRM).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Deal Risk Report semanal (Sexta 17h): lista de deals com risco ALTO/MEDIO/BAIXO com justificativa) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Deal Risk Report semanal (Sexta 17h): lista de deals com risco ALTO/MEDIO/BAIXO com justificativa
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

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
