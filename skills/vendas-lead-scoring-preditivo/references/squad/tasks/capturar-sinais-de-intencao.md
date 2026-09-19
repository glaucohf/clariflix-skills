---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Webhook de novo lead (HubSpot/Pipedrive form submit, Facebook Lead Ads, WhatsApp opt-in, LinkedIn Lead Gen Form)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Payload bruto: nome, email, telefone, empresa, fonte, UTMs, paginas visitadas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead Object normalizado em JSON: {lead_id, source_channel, ica_score_raw, firmographics{setor, porte_estimado, cargo}, behavioral_signals[], intent_signals[], data_completeness_pct, created_at}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Publicado no event bus para o Orquestrador"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook POST de qualquer fonte de aquisição configurada. Também roda em batch diário às 06h para re-normalizar leads com dados atualizados de enriquecimento."
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

# Capturar Sinais De Intencao

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Lead Scoring Preditivo e Priorização

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Capturar Sinais De Intencao |
| **status** | `pending` |
| **responsible_executor** | Radar (Scout de Sinais (Radár)) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de captura e normalizacao de sinais de intencao. Monitora todas as fontes de entrada (formularios, ads, WhatsApp, LinkedIn, site) e normaliza os dados brutos em um Lead Object padronizado antes de qualquer scoring. Detecta sinais de intent implicitos: visita a pagina de preco, download de case study, clique em email de oferta.

## Input

- Webhook de novo lead (HubSpot/Pipedrive form submit, Facebook Lead Ads, WhatsApp opt-in, LinkedIn Lead Gen Form)
- Payload bruto: nome, email, telefone, empresa, fonte, UTMs, paginas visitadas

## Output

- Lead Object normalizado em JSON: {lead_id, source_channel, ica_score_raw, firmographics{setor, porte_estimado, cargo}, behavioral_signals[], intent_signals[], data_completeness_pct, created_at}
- Publicado no event bus para o Orquestrador

## Trigger

Webhook POST de qualquer fonte de aquisição configurada. Também roda em batch diário às 06h para re-normalizar leads com dados atualizados de enriquecimento.

## Knowledge base (o que o executor consulta)

- Dicionário de normalização de cargos (mapeamento de 200+ variações para 12 personas-alvo), lookup table de setores CNAE vs ICP, regras de intent scoring por URL visitada, tabela de UTM-to-channel attribution, histórico de conversão por fonte para calibração de prior

## Action Items

1. Confirmar o gatilho e carregar a entrada (Webhook de novo lead (HubSpot/Pipedrive form submit, Facebook Lead Ads, WhatsApp opt-in, LinkedIn Lead Gen Form)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead Object normalizado em JSON: {lead_id, source_channel, ica_score_raw, firmographics{setor, porte_estimado, cargo},…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead Object normalizado em JSON: {lead_id, source_channel, ica_score_raw, firmographics{setor, porte_estimado, cargo}, behavioral_signals[], intent_signals[],…
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

- **to:** Sherlock
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
