---
task: orion2()
responsavel: "Orion 2"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Registros analisados dos últimos 30 dias da tabela voc_analyzed_feedback (Supabase) + histórico de scores de tendência por tema (últimos 60 dias) + calendário de eventos do produto (releases, incidentes) via ClickUp/Jira API + pesos de priorização configurados no Deep Dive + thresholds de alerta por tema e segmento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tabela de tendências priorizadas persistida no Supabase (tabela: voc_trends_daily): {tema_id, tema_nome, volume_7d, volume_14d, volume_30d, delta_7d_pct, delta_14d_pct, velocidade_24h, score_priorização, status_tendência (EMERGINDO/CRESCENDO/ESTÁVEL/DECLINANDO), sentimento_médio, top_3_subtemas, correlação_evento (bool + descrição), breakdown_segmentos (JSON), exemplos_verbatim (3-5 citações representativas com account_id anonimizado)}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alertas de emergência enviados ao Rapid para temas que cruzaram threshold"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Ranking das top-10 tendências da semana prontas para o Lyra gerar o relatório"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diário 08h30 após Yara confirmar processamento; cron a cada 4h para detecção de emergência (verifica apenas os últimos registros vs threshold); webhook do produto quando evento crítico e registr…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Cassandra antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia lembrete; sem resposta em 8h, relatório é enviado com disclaimer 'pendente de revisão humana'"
    - "[ ] HITL: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para atendimento) antes de aparecer no backlog ativo; aprovação via bot no Slack com preview da task"
    - "[ ] HITL: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefing imediato e Atlas cria task de emergência; se falso positivo, threshold é ajustado automaticamente"
    - "[ ] HITL: Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-processar histórico; impacto estimado em registros afetados e apresentado antes da aprovação"
    - "[ ] HITL: Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; indica possível drift na linguagem dos clientes ou bug na ingestão"
---

# Detectar Tendências Acionáveis

**Task ID:** `orion2()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Tendências Acionáveis |
| **status** | `pending` |
| **responsible_executor** | Orion 2 (Orion — Detector de Tendências e Priorizador) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Opera como o cerebro analitico do squad — transforma dados classificados em tendencias acionaveis priorizadas. Roda diariamente sobre os ultimos 7, 14 e 30 dias de dados analisados pelo Yara para: (1) DETECCAO DE TENDENCIAS — para cada tema na taxonomia, calcula: volume absoluto do periodo (mencoes), % do total de feedback do periodo, variacao vs baseline do periodo anterior (delta%), velocidade de crescimento (mencoes nas ultimas 24h vs media diaria dos 7 dias anteriores); classifica cada tema como: EMERGINDO (crescimento > 50% em 7 dias), CRESCENDO (crescimento 20-50%), ESTAVEL, DECLINANDO; (2) PRIORIZACAO — aplica formula de score: score_tendencia = volume_relativo x (1 + delta_crescimento) x peso_sentimento x peso_segmento; peso_sentimento: NEGATIVO = 2.0, NEUTRO = 1.0, POSITIVO = 0.5; peso_segmento: Enterprise = 3x, Mid = 2x, SMB = 1x; (3) ALERTA DE EMERGENCIA — detecta temas que cruzam threshold de alerta configurado (ex: crescimento > 200% em 72h, ou volume > X mencoes de clientes Enterprise em 24h) e dispara para Rapid; (4) CORRELACOES — identifica se tendencia emergente tem correlacao temporal com evento do produto (release, incidente, mudanca de preco) cruzando com calendario de eventos do ClickUp/Jira; (5) SEGMENTACAO — quebra cada tendencia por segmento de cliente, canal de origem, cohort de maturidade e CSM responsavel.

## Input

- Registros analisados dos últimos 30 dias da tabela voc_analyzed_feedback (Supabase) + histórico de scores de tendência por tema (últimos 60 dias) + calendário de eventos do produto (releases, incidentes) via ClickUp/Jira API + pesos de priorização configurados no Deep Dive + thresholds de alerta por tema e segmento

## Output

- Tabela de tendências priorizadas persistida no Supabase (tabela: voc_trends_daily): {tema_id, tema_nome, volume_7d, volume_14d, volume_30d, delta_7d_pct, delta_14d_pct, velocidade_24h, score_priorização, status_tendência (EMERGINDO/CRESCENDO/ESTÁVEL/DECLINANDO), sentimento_médio, top_3_subtemas, correlação_evento (bool + descrição), breakdown_segmentos (JSON), exemplos_verbatim (3-5 citações representativas com account_id anonimizado)}
- Alertas de emergência enviados ao Rapid para temas que cruzaram threshold
- Ranking das top-10 tendências da semana prontas para o Lyra gerar o relatório

## Trigger

Cron diário 08h30 após Yara confirmar processamento; cron a cada 4h para detecção de emergência (verifica apenas os últimos registros vs threshold); webhook do produto quando evento crítico e registrado (incidente, hotfix, release major) para correlação imediata

## Knowledge base (o que o executor consulta)

- Histórico de scores de tendência por tema (60 dias no Supabase para cálculo de baseline e delta), fórmula de priorização e pesos por segmento (configurados no Deep Dive), thresholds de alerta por tema e por segmento de cliente, mapa de eventos do produto (releases, incidentes, mudanças de preço) com datas para correlação, benchmarks de volume mínimo por tema para considerar tendência estatisticamente significativa (depende do volume total de feedback da base), histórico de correlações tema-evento anteriores

## Action Items

1. Confirmar o gatilho e carregar a entrada (Registros analisados dos últimos 30 dias da tabela voc_analyzed_feedback (Supabase) + histórico de scores de tendência…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tabela de tendências priorizadas persistida no Supabase (tabela: voc_trends_daily): {tema_id, tema_nome, volume_7d, vol…) e persistir no artefato do squad.
4. Entregar ao critic Cassandra; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tabela de tendências priorizadas persistida no Supabase (tabela: voc_trends_daily): {tema_id, tema_nome, volume_7d, volume_14d, volume_30d, delta_7d_pct, delta…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Cassandra registrado
- [ ] Gate HITL respeitado: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação e…
- [ ] Gate HITL respeitado: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto…
- [ ] Gate HITL respeitado: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmad…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para at… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefin… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-proce… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; in… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Publicacao de insight que menciona concorrente especifico por nome — Lyra sinaliza e o Head de CS aprova antes de distribuir para evitar vazamento de informaca… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Re-calibração de thresholds de alerta após detecção de falsos positivos recorrentes — o Rapid documenta a sugestão de ajuste e aguarda aprovação do PM ou Head… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de canal com volume insuficiente para análise estatística identificado pós-Discovery — Haruki notifica e aguarda decisão humana sobre incluir ou exclu… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Cassandra | BLOQUEIA entrega |

## Handoff

- **to:** Lyra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
