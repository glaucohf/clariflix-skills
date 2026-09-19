---
task: echo()
responsavel: "Echo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Histórico de health scores de todas as contas (Supabase: account_health_scores, últimos 90 dias) + registro de tasks de retenção criadas e resolvidas (ClickUp API) + dados de churn e saves confirmados (CRM) + eventos de produto relevantes (releases, incidentes, downtime) do log do time de produto"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório semanal de saúde da base (markdown + gráficos exportados): distribuição de scores, contas em deterioração acelerada, correlações sistêmicas detectadas, taxa de save das intervenções da semana, ROI de retenção calculado (MRR salvo vs custo das ações)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alerta especial quando detecta padrão sistemico (> 5 contas de mesmo segmento caindo simultaneamente)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Lista de 'contas em watchlist' (MEDIO risco com velocity negativa) para monitoramento preventivo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron semanal (segunda-feira 07h) para relatório completo; cron diário (08h) para detecção de padrões sistêmicos; evento de save confirmado (CSM fecha task como 'Salvo') para cálculo de impacto da int…"
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

# Monitorar Health Score

**Task ID:** `echo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Health Score |
| **status** | `pending` |
| **responsible_executor** | Echo (Echo — Monitor de Saúde Continua e Tendências) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora a evolucao do health score de toda a base ao longo do tempo, detecta tendencias sistemicas (ex: degradacao de saude em todas as contas de um segmento especifico, correlacionada com uma atualizacao de produto ou problema de infra), gera relatorio semanal de saude da base para o Head de CS, e mede o impacto das intervencoes (antes e depois do save: variacao do health score de contas onde o CSM agiu). Tambem detecta 'churn silencioso' — contas que reduziram uso mas nao estao no radar de CRITICO ainda, e que sem intervencao preventiva chegarao la em 30-45 dias.

## Input

- Histórico de health scores de todas as contas (Supabase: account_health_scores, últimos 90 dias) + registro de tasks de retenção criadas e resolvidas (ClickUp API) + dados de churn e saves confirmados (CRM) + eventos de produto relevantes (releases, incidentes, downtime) do log do time de produto

## Output

- Relatório semanal de saúde da base (markdown + gráficos exportados): distribuição de scores, contas em deterioração acelerada, correlações sistêmicas detectadas, taxa de save das intervenções da semana, ROI de retenção calculado (MRR salvo vs custo das ações)
- Alerta especial quando detecta padrão sistemico (> 5 contas de mesmo segmento caindo simultaneamente)
- Lista de 'contas em watchlist' (MEDIO risco com velocity negativa) para monitoramento preventivo

## Trigger

Cron semanal (segunda-feira 07h) para relatório completo; cron diário (08h) para detecção de padrões sistêmicos; evento de save confirmado (CSM fecha task como 'Salvo') para cálculo de impacto da intervenção

## Knowledge base (o que o executor consulta)

- Histórico completo de health scores no Supabase (90 dias), log de intervenções e outcomes (save/churn confirmado), eventos de produto (release notes, incidentes) para correlação de causa, benchmarks setoriais de churn rate por segmento, modelo de detecção de deterioração acelerada (regressão sobre velocity de scores), templates de relatório semanal para Head de CS

## Action Items

1. Confirmar o gatilho e carregar a entrada (Histórico de health scores de todas as contas (Supabase: account_health_scores, últimos 90 dias) + registro de tasks de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório semanal de saúde da base (markdown + gráficos exportados): distribuição de scores, contas em deterioração ace…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório semanal de saúde da base (markdown + gráficos exportados): distribuição de scores, contas em deterioração acelerada, correlações sistêmicas detectada…
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

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
