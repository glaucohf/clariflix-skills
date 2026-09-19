---
task: hermes()
responsavel: "Hermes"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Tabela canônica de touchpoints (do Nexus), tabela de oportunidades/closed-won com valor do CRM, janela de atribuição configurável (default: 30d para paid, 90d para orgânico), seleção de modelos a executar e pesos customizáveis para modelo híbrido se configurado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de atribuição multi-model (JSON + CSV): crédito por canal/campanha em cada modelo, CAC por canal/modelo, Attribution Coverage Score, top-3 discrepâncias entre modelos com explicação textual, e recomendação de modelo primário para o período com justificativa baseada em dados"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Após cada ingestão diária completa do Nexus; quando Atlas recebe pergunta de negócio sobre performance de canal; quando Coverage Score cai abaixo de 85% (alerta de degradação de tracking); início de…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Skeptic antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar ou corrigir antes do go-live. SLA: 30min para resposta, após isso o sistema notifica o gestor direto."
    - "[ ] L3: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor de media antes de execucao. O squad gera o racional completo, humano aprova ou rejeita com comentario."
    - "[ ] L3: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing de 5 linhas e aguarda confirmação de que foi visto (acknowledgment) antes de escalar para investigação automática mais profunda."
    - "[ ] L2: Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta. Previne drift de sensibilidade ao longo do tempo."
    - "[ ] L2: Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP de Marketing. Revisão trimestral."
---

# Calcular Atribuição Multi-Modelo

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Funnel Analytics & Attribution Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Atribuição Multi-Modelo |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — Agente de Atribuição Multi-Model) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de atribuição. Recebe o dataset canônico de touchpoints do Nexus e calcula atribuição de pipeline e receita para cada source/channel/campaign usando 4 modelos simultaneamente: last-touch, first-touch, linear e data-driven (modelo de Markov ou Shapley simplificado). Gera tabela comparativa de crédito por modelo, identifica discrepâncias relevantes (canal que perde >30% de crédito em data-driven vs last-touch) e calcula CAC real por canal e por modelo. Também calcula o 'Attribution Coverage Score' — % do pipeline com pelo menos um touchpoint rastreável.

## Input

- Tabela canônica de touchpoints (do Nexus), tabela de oportunidades/closed-won com valor do CRM, janela de atribuição configurável (default: 30d para paid, 90d para orgânico), seleção de modelos a executar e pesos customizáveis para modelo híbrido se configurado

## Output

- Relatório de atribuição multi-model (JSON + CSV): crédito por canal/campanha em cada modelo, CAC por canal/modelo, Attribution Coverage Score, top-3 discrepâncias entre modelos com explicação textual, e recomendação de modelo primário para o período com justificativa baseada em dados

## Trigger

Após cada ingestão diária completa do Nexus; quando Atlas recebe pergunta de negócio sobre performance de canal; quando Coverage Score cai abaixo de 85% (alerta de degradação de tracking); início de novo mês para relatório mensal comparativo.

## Knowledge base (o que o executor consulta)

- Algoritmos de atribuição (Markov chains, Shapley values simplificado, regras de last/first/linear), histórico de crédito por canal (6 meses) para identificar tendências, mapa de jornada do cliente por segmento ICP, benchmark de CAC por indústria/segmento, definições de conversão por etapa do funil da empresa

## Action Items

1. Confirmar o gatilho e carregar a entrada (Tabela canônica de touchpoints (do Nexus), tabela de oportunidades/closed-won com valor do CRM, janela de atribuição co…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de atribuição multi-model (JSON + CSV): crédito por canal/campanha em cada modelo, CAC por canal/modelo, Attr…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de atribuição multi-model (JSON + CSV): crédito por canal/campanha em cada modelo, CAC por canal/modelo, Attribution Coverage Score, top-3 discrepânc…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Skeptic registrado
- [ ] Gate L3 respeitado: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de cam…
- [ ] Gate L3 respeitado: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovaca…
- [ ] Gate L3 respeitado: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor d… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta.… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão de relatório executivo antes de envio ao board: Oracle gera, Skeptic valida, mas um humano (CMO ou analista sênior) faz leitura final antes de envio ao… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Skeptic | BLOQUEIA entrega |

## Handoff

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
