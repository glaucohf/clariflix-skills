---
task: sherlock()
responsavel: "Sherlock"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead Object do Scout com data_completeness_pct < 70%"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Mínimo necessário: nome da empresa OU CNPJ OU email corporativo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead Object enriquecido: +CNPJ validado, +LinkedIn URL da empresa e do contato, +headcount estimado, +receita anual estimada, +tech stack detectado (via BuiltWith/Apollo), +trigger_events[] (ex: rodada Série A anunciada, nova filial aberta), +contatos_adicionais[] na conta"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Score de completude atualizado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Tudo gravado no CRM como propriedades customizadas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento lead_normalized do Scout com completude < 70%. Também: evento account_trigger_detected (ex: monitoramento de LinkedIn/news de conta em pipeline ativo)."
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

# Enriquecer Dados Firmográficos

**Task ID:** `sherlock()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Lead Scoring Preditivo e Priorização

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dados Firmográficos |
| **status** | `pending` |
| **responsible_executor** | Sherlock (Detetive de Conta (Sherlock)) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de enriquecimento de dados. Recebe Lead Object com completude baixa e dispara consultas em fontes externas para completar firmográficos, descobrir contatos adicionais na mesma conta, validar email/telefone e buscar trigger events (financiamento recente, expansão, vaga aberta de cargo relevante).

## Input

- Lead Object do Scout com data_completeness_pct < 70%
- Mínimo necessário: nome da empresa OU CNPJ OU email corporativo

## Output

- Lead Object enriquecido: +CNPJ validado, +LinkedIn URL da empresa e do contato, +headcount estimado, +receita anual estimada, +tech stack detectado (via BuiltWith/Apollo), +trigger_events[] (ex: rodada Série A anunciada, nova filial aberta), +contatos_adicionais[] na conta
- Score de completude atualizado
- Tudo gravado no CRM como propriedades customizadas

## Trigger

Evento lead_normalized do Scout com completude < 70%. Também: evento account_trigger_detected (ex: monitoramento de LinkedIn/news de conta em pipeline ativo).

## Knowledge base (o que o executor consulta)

- Credenciais Apollo/Clay via MCP
- Mapeamento de tech stack indicativo de fit (ex: empresa usa HubSpot = maturidade digital maior = score +5)
- Lista de trigger events positivos e negativos com peso no score
- CNPJ Receita Federal para validação

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead Object do Scout com data_completeness_pct < 70%).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead Object enriquecido: +CNPJ validado, +LinkedIn URL da empresa e do contato, +headcount estimado, +receita anual est…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead Object enriquecido: +CNPJ validado, +LinkedIn URL da empresa e do contato, +headcount estimado, +receita anual estimada, +tech stack detectado (via BuiltW…
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

- **to:** Vega
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
