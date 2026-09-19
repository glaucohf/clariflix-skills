---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Cron diario (05h30) + webhook de evento critico (renovacao criada/alterada no CRM, feature premium testada, solicitacao de upgrade registrada em ticket) + lista completa de contratos ativos com datas de renovacao do CRM + dados de uso da plataforma de produto (feature adoption, DAU, usuarios ativos) dos ultimos 30 e 90 dias"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON estruturado por conta com: (1) status de renovacao (dias_para_renovacao, mrr_em_risco, brief_ja_gerado: sim/nao, urgencia: CRITICA/ALTA/MEDIA/BAIXA)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) sinais de expansao detectados com valor concreto por sinal (ex: 'usuarios_ativos: 87% de licencas contratadas', 'feature_premium_x: 34 eventos em 7 dias')"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) sinais negativos que bloqueiam expansao"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) prioridade calculada (MRR * urgencia_renovacao + score_expansao) para ordenacao da fila pelo Maestro"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Persistido no Supabase (tabela: renewal_expansion_queue)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron job 05h30 diario para batch completo; webhook de renovacao criada/alterada no CRM; webhook de evento de produto acima de threshold (usuarios ativos, feature usage); flag de renovacao em < 30 dia…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Verity antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de expansao com status 'Aguardando Aprovacao do CSM/Manager' antes de incluir a proposta no deck final para o cliente"
    - "[ ] HITL: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CSM (deck e gerado, nunca enviado automaticamente ao cliente)"
    - "[ ] HITL: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar qualquer contato de renovacao"
    - "[ ] HITL: Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de entrada antes de reprocessar"
    - "[ ] HITL: Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer alinhamento com equipe comercial (AE ou CSM sênior) antes de abordar o cliente"
---

# Detectar Sinais De Expansão

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Sinais De Expansão |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Sensor de Janelas de Renovacao e Sinais de Expansao) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente toda a base de contas para identificar duas categorias de evento: (A) RENOVACAO — contas entrando na janela de 90, 60 e 30 dias antes da data de renovacao de contrato, com flag de urgencia crescente; contas com renovacao programada que ainda nao tem brief gerado; renovacoes cujo contrato foi alterado ou que tem MRR em risco (downgrade solicitado, nota de cancelamento registrada no CRM). (B) EXPANSAO — sinais de propensao a upgrade: percentual de usuarios ativos vs licencas contratadas acima de 80% (pressao de limite), adocao de feature disponivel apenas no plano superior acima de X eventos em 7 dias, novo departamento ou filial usando a conta principal, solicitacao de feature paga via ticket de suporte ou nota do CSM, aumento de DAU acima de 40% em 30 dias sem aumento de licencas, integracao enterprise testada mas nao contratada. Tambem detecta sinais negativos que impedem expansao: baixo uso do tier atual, feature core nunca ativada, onboarding incompleto.

## Input

- Cron diario (05h30) + webhook de evento critico (renovacao criada/alterada no CRM, feature premium testada, solicitacao de upgrade registrada em ticket) + lista completa de contratos ativos com datas de renovacao do CRM + dados de uso da plataforma de produto (feature adoption, DAU, usuarios ativos) dos ultimos 30 e 90 dias

## Output

- JSON estruturado por conta com: (1) status de renovacao (dias_para_renovacao, mrr_em_risco, brief_ja_gerado: sim/nao, urgencia: CRITICA/ALTA/MEDIA/BAIXA)
- (2) sinais de expansao detectados com valor concreto por sinal (ex: 'usuarios_ativos: 87% de licencas contratadas', 'feature_premium_x: 34 eventos em 7 dias')
- (3) sinais negativos que bloqueiam expansao
- (4) prioridade calculada (MRR * urgencia_renovacao + score_expansao) para ordenacao da fila pelo Maestro
- Persistido no Supabase (tabela: renewal_expansion_queue)

## Trigger

Cron job 05h30 diario para batch completo; webhook de renovacao criada/alterada no CRM; webhook de evento de produto acima de threshold (usuarios ativos, feature usage); flag de renovacao em < 30 dias sem brief gerado (verificacao horaria)

## Knowledge base (o que o executor consulta)

- Contratos ativos com datas de renovacao e valores de MRR por conta (CRM)
- schema de eventos da plataforma de produto com mapeamento de features por tier/plano
- thresholds de sinais de expansao por produto e por segmento (calibrados no Deep Dive)
- historico de expansoes realizadas com sinais que as precederam
- lista de features disponíveis apenas em planos superiores por produto

## Action Items

1. Confirmar o gatilho e carregar a entrada (Cron diario (05h30) + webhook de evento critico (renovacao criada/alterada no CRM, feature premium testada, solicitacao…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON estruturado por conta com: (1) status de renovacao (dias_para_renovacao, mrr_em_risco, brief_ja_gerado: sim/nao, u…) e persistir no artefato do squad.
4. Entregar ao critic Verity; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON estruturado por conta com: (1) status de renovacao (dias_para_renovacao, mrr_em_risco, brief_ja_gerado: sim/nao, urgencia: CRITICA/ALTA/MEDIA/BAIXA)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Verity registrado
- [ ] Gate HITL respeitado: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pu…
- [ ] Gate HITL respeitado: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e…
- [ ] Gate HITL respeitado: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS a…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CS… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de ent… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer ali… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Comprometimento pendente do fornecedor detectado pelo Memory como nao entregue no periodo anterior — brief inclui o item mas Pulse cria subtask de 'Resolucao d… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Conta com Renewal Readiness Score CRITICO (< 50) e renovacao em < 30 dias — escalacao imediata para Head de CS e Account Executive senior com brief de situacao… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de Memory indicando que CSM fez edicao significativa no deck (> 30% do conteudo alterado) — Maestro abre HITL para CSM documentar o motivo da edicao e… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Verity | BLOQUEIA entrega |

## Handoff

- **to:** Compass
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
