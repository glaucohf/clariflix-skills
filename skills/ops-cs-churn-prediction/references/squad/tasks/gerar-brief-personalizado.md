---
task: mira()
responsavel: "Mira"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Health score com breakdown de dimensões + histórico de sinais 90 dias + dados completos da conta do CRM (CSM, histórico de interações, QBRs, expansões) + playbook de retenção por segmento + histórico de saves similares para benchmarking"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Brief de retenção estruturado em markdown (max 400 palavras) com score atual, breakdown de sinais, next-best-action prioritária, ações alternativas rankeadas e script de abertura"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Pronto para ser anexado como task no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orchestrator Nexus para toda conta com score CRÍTICO (automático) ou ALTO risco com velocity de queda > 10 pontos/semana; acionado sob demanda pelo CSM via comando ClickUp"
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

# Gerar Brief Personalizado

**Task ID:** `mira()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Brief Personalizado |
| **status** | `pending` |
| **responsible_executor** | Mira (Míra — Geradora de Brief e Next-Best-Action) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Para cada conta classificada como CRÍTICO ou ALTO risco, gera um brief de retenção personalizado e a next-best-action prioritária para o CSM. O brief contém: (1) Resumo executivo do risco em 3 bullets (o que mudou, quando, impacto); (2) Sinais que compõem o risco com valores concretos ('DAU caiu 52% em 14 dias', 'CSAT 2.8 nos últimos 3 tickets', 'renovação em 23 dias'); (3) Contexto histórico da conta (expansão ou contração recente, QBR anterior, compromissos pendentes do CSM); (4) Next-best-action recomendada com justificativa (ex: 'Ligar hoje — oferecer sessão de onboarding do recurso X que nunca foi ativado: 67% de saves em contas similares'); (5) Ações alternativas rankeadas por taxa de sucesso histórica no segmento; (6) Script de abertura de conversa sugerido para o CSM. Usa RAG sobre playbook de retenção e histórico de saves bem-sucedidos.

## Input

- Health score com breakdown de dimensões + histórico de sinais 90 dias + dados completos da conta do CRM (CSM, histórico de interações, QBRs, expansões) + playbook de retenção por segmento + histórico de saves similares para benchmarking

## Output

- Brief de retenção estruturado em markdown (max 400 palavras) com score atual, breakdown de sinais, next-best-action prioritária, ações alternativas rankeadas e script de abertura
- Pronto para ser anexado como task no ClickUp

## Trigger

Acionado pelo Orchestrator Nexus para toda conta com score CRÍTICO (automático) ou ALTO risco com velocity de queda > 10 pontos/semana; acionado sob demanda pelo CSM via comando ClickUp

## Knowledge base (o que o executor consulta)

- Playbook de retenção por segmento e por tipo de risco predominante (risco de produto vs risco de satisfação vs risco comercial), histórico de saves bem-sucedidos com features da conta e ação tomada, histórico de interações do CRM (notes, calls, emails), dados de feature adoption por cohort (quais features estão correlacionadas com retenção), templates de script por tipo de abordagem (valor, suporte, expansão, executive sponsor)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Health score com breakdown de dimensões + histórico de sinais 90 dias + dados completos da conta do CRM (CSM, histórico…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Brief de retenção estruturado em markdown (max 400 palavras) com score atual, breakdown de sinais, next-best-action pri…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Brief de retenção estruturado em markdown (max 400 palavras) com score atual, breakdown de sinais, next-best-action prioritária, ações alternativas rankeadas e…
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

- **to:** Spark
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
