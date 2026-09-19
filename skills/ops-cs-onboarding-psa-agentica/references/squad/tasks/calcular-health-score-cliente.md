---
task: vitor()
responsavel: "Vitor"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Status de marcos no ClickUp"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "dados de uso do produto (logins, features ativadas, via API/MCP)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "histórico de tickets de suporte (volume, severidade, tempo de resolução)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "participação em calls (frequência, presença do sponsor)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "sentimento extraído de comunicações (via NLP simples)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "benchmarks de health score de clientes similares"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "health-score-report.json semanal com score composto, sub-scores por dimensão, tendência (melhorando/estável/deteriorando), risco de churn (low/medium/high/critical) e next-best-action recomendada para o CSM"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "alerta crítico quando score < 40 ou queda de >15 pontos em 7 dias"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo semanal automático (toda segunda-feira às 09h); marco crítico concluído ou atrasado; ticket de suporte de severidade alta; queda de engajamento no produto >30% em 7 dias; solicitação manual do…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)"
    - "[ ] HITL: Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)"
    - "[ ] HITL: Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro"
    - "[ ] HITL: Aprovação do Delivery Status Report semanal antes do envio ao cliente"
    - "[ ] HITL: Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente"
---

# Calcular Health Score Cliente

**Task ID:** `vitor()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Health Score Cliente |
| **status** | `pending` |
| **responsible_executor** | Vitor (Vitor — Agente de Health Score e Churn Prevention) |
| **execution_type** | `Agent` |
| **input** | 6 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analista de saúde do cliente durante os primeiros 90 dias. Agrega sinais de múltiplas fontes (engajamento no produto, tickets de suporte, ativações completadas, participação em calls, marcos concluídos vs. pendentes, sentimento em comunicações) e calcula um health score composto (0-100) com sub-scores por dimensão. Identifica clientes em risco de churn precoce e gera next-best-action para o CSM. Atualiza o score semanalmente e emite alertas quando score cai abaixo de threshold definido.

## Input

- Status de marcos no ClickUp
- dados de uso do produto (logins, features ativadas, via API/MCP)
- histórico de tickets de suporte (volume, severidade, tempo de resolução)
- participação em calls (frequência, presença do sponsor)
- sentimento extraído de comunicações (via NLP simples)
- benchmarks de health score de clientes similares

## Output

- health-score-report.json semanal com score composto, sub-scores por dimensão, tendência (melhorando/estável/deteriorando), risco de churn (low/medium/high/critical) e next-best-action recomendada para o CSM
- alerta crítico quando score < 40 ou queda de >15 pontos em 7 dias

## Trigger

Ciclo semanal automático (toda segunda-feira às 09h); marco crítico concluído ou atrasado; ticket de suporte de severidade alta; queda de engajamento no produto >30% em 7 dias; solicitação manual do CSM

## Knowledge base (o que o executor consulta)

- Modelo de health score da empresa (pesos por dimensão), benchmarks de health score por segmento/produto/semana do onboarding, padrões históricos de clientes que churned vs
- expandiram nos primeiros 90 dias, playbooks de intervenção por nível de risco

## Action Items

1. Confirmar o gatilho e carregar a entrada (Status de marcos no ClickUp).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (health-score-report.json semanal com score composto, sub-scores por dimensão, tendência (melhorando/estável/deteriorand…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: health-score-report.json semanal com score composto, sub-scores por dimensão, tendência (melhorando/estável/deteriorando), risco de churn (low/medium/high/crit…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)
- [ ] Gate HITL respeitado: Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)
- [ ] Gate HITL respeitado: Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação do Delivery Status Report semanal antes do envio ao cliente | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Decisão de go/no-go para go-live quando health score < 60 ou mais de 2 marcos críticos em Red | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Crono
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
