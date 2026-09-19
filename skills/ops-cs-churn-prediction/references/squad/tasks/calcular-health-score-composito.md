---
task: prism()
responsavel: "Prism"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinais normalizados do Vega (JSON por conta) + modelo de pesos calibrado por segmento (carregado do Supabase) + histórico de scores anteriores da conta para cálculo de velocity"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Health score (0-100) por conta com breakdown das 4 dimensoes, velocity de deterioracao, classificacao de risco (CRITICO/ALTO/MEDIO/BAIXO), e ranking priorizado de contas em risco"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "persistido no Supabase (tabela: account_health_scores)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Historico de scores para trending"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orchestrator Nexus após Vega concluir ingestão diária; acionado em tempo real quando Vega dispara alerta de evento crítico para conta específica"
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

# Calcular Health Score Compósito

**Task ID:** `prism()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Health Score Compósito |
| **status** | `pending` |
| **responsible_executor** | Prism (Prism — Calculador de Health Score) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe os sinais normalizados do Vega e calcula o health score composto (0-100) para cada conta usando o modelo calibrado no Deep Dive. Aplica pesos diferenciados por segmento (SMB/Mid/Enterprise) e calcula as 4 dimensoes do score: (1) Engajamento de Produto (0-25): DAU/MAU ratio, breadth de features, sessoes semanais; (2) Satisfacao do Cliente (0-25): NPS, CSAT media, verbatim sentiment score; (3) Saude de Suporte (0-25): frequencia de tickets, tempo de resolucao, CSAT pos-ticket; (4) Risco Comercial (0-25): dias ate renovacao, historico de expansao/contracao, absenteismo em QBRs. Calcula tambem o 'velocity de deterioracao' — taxa de queda do score nos ultimos 7 e 30 dias para identificar contas em queda acelerada mesmo que ainda em zona amarela.

## Input

- Sinais normalizados do Vega (JSON por conta) + modelo de pesos calibrado por segmento (carregado do Supabase) + histórico de scores anteriores da conta para cálculo de velocity

## Output

- Health score (0-100) por conta com breakdown das 4 dimensoes, velocity de deterioracao, classificacao de risco (CRITICO/ALTO/MEDIO/BAIXO), e ranking priorizado de contas em risco
- persistido no Supabase (tabela: account_health_scores)
- Historico de scores para trending

## Trigger

Acionado pelo Orchestrator Nexus após Vega concluir ingestão diária; acionado em tempo real quando Vega dispara alerta de evento crítico para conta específica

## Knowledge base (o que o executor consulta)

- Modelo de pesos por segmento (calibrado no Deep Dive e versionado no Supabase), thresholds de classificação (CRÍTICO < 45, ALTO 45-59, MÉDIO 60-74, BAIXO >= 75), histórico de scores por conta (últimos 90 dias), benchmark de health score por segmento e cohort de maturidade de conta

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinais normalizados do Vega (JSON por conta) + modelo de pesos calibrado por segmento (carregado do Supabase) + históri…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Health score (0-100) por conta com breakdown das 4 dimensoes, velocity de deterioracao, classificacao de risco (CRITICO…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Health score (0-100) por conta com breakdown das 4 dimensoes, velocity de deterioracao, classificacao de risco (CRITICO/ALTO/MEDIO/BAIXO), e ranking priorizado…
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

- **to:** Mira
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
