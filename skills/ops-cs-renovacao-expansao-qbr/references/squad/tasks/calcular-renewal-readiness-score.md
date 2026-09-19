---
task: compass()
responsavel: "Compass"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinais do Radar por conta (uso, sentimento, sinais de expansao) + dados do CRM (historico de interacoes do CSM, QBRs realizados, compromissos, executive sponsor) + NPS e CSAT coletados pelo pipeline de ingestao + modelo de pesos por segmento carregado do Supabase + historico de scores anteriores da conta para calculo de tendencia"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Renewal Readiness Score (0-100) com breakdown das 5 dimensoes, Renewal Risk Index (CRITICO/ALTO/MEDIO/BAIXO), tendencia de score (melhora/piora/estavel vs ultimo calculo), e lista priorizada de 'dimensoes mais frageis' para o Briefer focar no brief"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Persistido no Supabase (tabela: renewal_readiness_scores) com historico para trending"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro para toda conta que o Radar colocar na fila diaria; acionado em modo urgente quando Radar detecta renovacao em < 30 dias sem score calculado nos ultimos 7 dias"
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

# Calcular Renewal Readiness Score

**Task ID:** `compass()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Renewal Readiness Score |
| **status** | `pending` |
| **responsible_executor** | Compass (Compass — Calculador de Renewal Readiness Score) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Calcula o Renewal Readiness Score (0-100) para cada conta na janela de renovacao, usando o modelo calibrado no Deep Dive. Dimensoes e pesos: (1) Uso Ativo (0-25): DAU/MAU ratio, breadth de features usadas vs contratadas, usuarios ativos vs licencas, frequencia de uso por usuario; (2) Sentimento (0-20): NPS recente, CSAT medio, verbatim sentiment score, tendencia de satisfacao vs periodo anterior; (3) Valor Percebido (0-20): marcos de onboarding entregues, ROI documentado em interacoes do CSM, outcomes reportados pelo cliente, participacao em QBRs anteriores; (4) Relacionamento (0-20): frequencia de contato CSM x conta, executive sponsor ativo, compromissos do fornecedor cumpridos, dias desde ultimo contato significativo; (5) Sinais de Expansao (0-15): numero e forca dos sinais de expansao detectados pelo Radar — contas com sinais fortes recebem bonus que eleva o score de renovacao pois indicam satisfacao alta. Calcula tambem o 'Renewal Risk Index' — combinacao de Score com prazo: conta CRITICA = score < 50 com renovacao em < 60 dias; conta em alerta = score 50-65 com renovacao em < 90 dias.

## Input

- Sinais do Radar por conta (uso, sentimento, sinais de expansao) + dados do CRM (historico de interacoes do CSM, QBRs realizados, compromissos, executive sponsor) + NPS e CSAT coletados pelo pipeline de ingestao + modelo de pesos por segmento carregado do Supabase + historico de scores anteriores da conta para calculo de tendencia

## Output

- Renewal Readiness Score (0-100) com breakdown das 5 dimensoes, Renewal Risk Index (CRITICO/ALTO/MEDIO/BAIXO), tendencia de score (melhora/piora/estavel vs ultimo calculo), e lista priorizada de 'dimensoes mais frageis' para o Briefer focar no brief
- Persistido no Supabase (tabela: renewal_readiness_scores) com historico para trending

## Trigger

Acionado pelo Maestro para toda conta que o Radar colocar na fila diaria; acionado em modo urgente quando Radar detecta renovacao em < 30 dias sem score calculado nos ultimos 7 dias

## Knowledge base (o que o executor consulta)

- Modelo de pesos por segmento (SMB/Mid/Enterprise) e por produto (calibrado no Deep Dive e versionado no Supabase)
- historico de scores e renovacoes (quais scores correlacionaram com renovacao saudavel vs com atrito vs com churn)
- dados de Account, Activity, Contract do CRM
- historico de QBRs e commitments
- benchmark de Renewal Readiness Score medio por cohort e por segmento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinais do Radar por conta (uso, sentimento, sinais de expansao) + dados do CRM (historico de interacoes do CSM, QBRs re…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Renewal Readiness Score (0-100) com breakdown das 5 dimensoes, Renewal Risk Index (CRITICO/ALTO/MEDIO/BAIXO), tendencia…) e persistir no artefato do squad.
4. Entregar ao critic Verity; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Renewal Readiness Score (0-100) com breakdown das 5 dimensoes, Renewal Risk Index (CRITICO/ALTO/MEDIO/BAIXO), tendencia de score (melhora/piora/estavel vs ulti…
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

- **to:** Scout
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
