---
task: vega()
responsavel: "Vega"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Cron diário (06h) ou webhook de evento crítico + lista de IDs de contas monitoradas + credenciais MCP para cada fonte de dados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON estruturado por conta com todos os sinais normalizados e métricas derivadas persistido no Supabase (tabela: churn_signals_daily)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alertas em tempo real via webhook interno para o Orchestrator Nexus quando evento crítico é detectado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron job 06h00 diário para batch completo; webhook de evento crítico (NPS Detrator submetido, ticket com keyword de cancelamento, primeiro login após 21 dias de inatividade, MRR contraction detectada…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica"
    - "[ ] HITL: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato"
    - "[ ] HITL: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados"
    - "[ ] HITL: Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch"
    - "[ ] HITL: Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar"
---

# Monitorar Sinais De Uso E Sentimento

**Task ID:** `vega()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais De Uso E Sentimento |
| **status** | `pending` |
| **responsible_executor** | Vega (Vega — Sensor de Sinais de Uso e Sentimento) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Coleta, normaliza e persiste diariamente os sinais brutos de todas as contas monitoradas. Conecta-se via MCP a: plataforma de produto (eventos de login, features usadas, sessões, DAU/MAU), helpdesk (volume de tickets, CSAT, categorias de problema), CRM (dados de renovação, MRR, segmento, CSM) e fontes de NPS/feedback (scores, verbatims). Calcula métricas derivadas: queda percentual de DAU nos ùltimos 7 e 14 dias, variação de CSAT média móvel 30d, frequência de tickets por categoria, dias até renovação, variação de MRR. Detecta eventos críticos em tempo real via webhook: primeiro sinal de cancelamento, NPS Detrator, ticket com palavra-chave de risco.

## Input

- Cron diário (06h) ou webhook de evento crítico + lista de IDs de contas monitoradas + credenciais MCP para cada fonte de dados

## Output

- JSON estruturado por conta com todos os sinais normalizados e métricas derivadas persistido no Supabase (tabela: churn_signals_daily)
- Alertas em tempo real via webhook interno para o Orchestrator Nexus quando evento crítico é detectado

## Trigger

Cron job 06h00 diário para batch completo; webhook de evento crítico (NPS Detrator submetido, ticket com keyword de cancelamento, primeiro login após 21 dias de inatividade, MRR contraction detectada no CRM)

## Knowledge base (o que o executor consulta)

- Schema de eventos da plataforma de produto (Mixpanel/Amplitude/Segment event taxonomy), mapeamento de campos do CRM por objeto (Account, Opportunity, Renewal), estrutura de tickets do helpdesk (campos, tags, categorias), lista de keywords de risco para detecção em tempo real, mapa de IDs de conta entre sistemas (account_id cross-system mapping)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Cron diário (06h) ou webhook de evento crítico + lista de IDs de contas monitoradas + credenciais MCP para cada fonte d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON estruturado por conta com todos os sinais normalizados e métricas derivadas persistido no Supabase (tabela: churn_…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON estruturado por conta com todos os sinais normalizados e métricas derivadas persistido no Supabase (tabela: churn_signals_daily)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cri…
- [ ] Gate HITL respeitado: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de…
- [ ] Gate HITL respeitado: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguarda… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualque… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analis… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo b… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de rela… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Prism
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
