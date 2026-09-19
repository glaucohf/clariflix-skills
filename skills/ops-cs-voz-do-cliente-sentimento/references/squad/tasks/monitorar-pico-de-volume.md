---
task: rapid()
responsavel: "Rapid"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stream de registros analisados do Supabase das últimas 12h (tabela: voc_analyzed_feedback, filtrado por data_ingestão) + thresholds de alerta configurados por tema e segmento + histórico de alertas disparados nas últimas 48h (para evitar spam de alertas repetidos para o mesmo tema) + baseline de volume por tema e por hora do dia (para ajuste de sazonalidade"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "segunda-feira tem mais feedback que sábado)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem formatada de alerta em Slack para o canal #voc-alertas com: tipo de alerta, tema afetado, números concretos (X menções em Y horas, crescimento de Z%), 2-3 verbatims representativos, segmentos afetados e sugestão de ação imediata"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registro do alerta no Supabase (tabela: voc_alerts) com timestamp, tipo, tema, volume, verbatims e status (DISPARADO / RESPONDIDO / FALSO_POSITIVO)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Caso alerta de emergência seja classificado como CRÍTICO pelo Orion: trigger para Lyra gerar briefing imediato fora do ciclo semanal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron a cada 4 horas (00h, 04h, 08h, 12h, 16h, 20h); webhook imediato quando Haruki detecta pico anômalo de volume em ingestão; suprimido para o mesmo tema por 12h após alerta recente para evitar spam…"
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

# Monitorar Pico De Volume

**Task ID:** `rapid()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Pico De Volume |
| **status** | `pending` |
| **responsible_executor** | Rapid (Rapid — Agente de Alerta e Monitoramento em Tempo Real) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Vela continuamente sobre o pipeline de feedback em busca de situações que não podem esperar o ciclo semanal. Roda a cada 4 horas verificando: (1) PICO DE VOLUME — qualquer tema com crescimento > 200% em 12h vs baseline diário; (2) EMERGÊNCIA DE SENTIMENTO — qualquer tema com sentimento médio caindo abaixo de -0.7 em 24h (linguagem muito crítica, indica possível crise); (3) CLUSTER ENTERPRISE — 3 ou mais clientes Enterprise mencionando o mesmo tema em 24h (alto impacto de receita); (4) MENCÃO DE CONCORRENTE COM CHURN — combinação de flag_concorrente + flag_churn em mesmo registro ou conta (sinal de substituição ativa); (5) BUG CRÍTICO EMERGENTE — volume de bug_reportado crescendo > 150% em 4h para mesmo tema de feature; (6) ANOMALIA DE VOLUME DE CANAL — queda > 50% no volume de qualquer canal (possível falha de integração reportada pelo Haruki). Para cada alerta disparado: formata mensagem com contexto (tema, volume, delta, 2-3 verbatims exemplares, contas afetadas se identificável por segmento), envia para canal Slack dedicado (#voc-alertas), cria notificação urgente para o PM e Head de CS, e registra o alerta no Supabase para tracking de resposta.

## Input

- Stream de registros analisados do Supabase das últimas 12h (tabela: voc_analyzed_feedback, filtrado por data_ingestão) + thresholds de alerta configurados por tema e segmento + histórico de alertas disparados nas últimas 48h (para evitar spam de alertas repetidos para o mesmo tema) + baseline de volume por tema e por hora do dia (para ajuste de sazonalidade
- segunda-feira tem mais feedback que sábado)

## Output

- Mensagem formatada de alerta em Slack para o canal #voc-alertas com: tipo de alerta, tema afetado, números concretos (X menções em Y horas, crescimento de Z%), 2-3 verbatims representativos, segmentos afetados e sugestão de ação imediata
- Registro do alerta no Supabase (tabela: voc_alerts) com timestamp, tipo, tema, volume, verbatims e status (DISPARADO / RESPONDIDO / FALSO_POSITIVO)
- Caso alerta de emergência seja classificado como CRÍTICO pelo Orion: trigger para Lyra gerar briefing imediato fora do ciclo semanal

## Trigger

Cron a cada 4 horas (00h, 04h, 08h, 12h, 16h, 20h); webhook imediato quando Haruki detecta pico anômalo de volume em ingestão; suprimido para o mesmo tema por 12h após alerta recente para evitar spam (cooldown configurável por tema)

## Knowledge base (o que o executor consulta)

- Thresholds de alerta por tema e por segmento (configurados no Deep Dive e ajustáveis pelo PM via painel), baseline de volume por tema, por dia da semana e por hora (sazonalidade semanal e diária calculada nos primeiros 30 dias em produção), histórico de alertas e classificação de falso positivo (para auto-ajuste de thresholds), mapa de canais Slack e destinatários por tipo e severidade de alerta, cooldown periods por tema para evitar sobrecarga de notificações

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stream de registros analisados do Supabase das últimas 12h (tabela: voc_analyzed_feedback, filtrado por data_ingestão)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagem formatada de alerta em Slack para o canal #voc-alertas com: tipo de alerta, tema afetado, números concretos (X…) e persistir no artefato do squad.
4. Entregar ao critic Cassandra; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagem formatada de alerta em Slack para o canal #voc-alertas com: tipo de alerta, tema afetado, números concretos (X menções em Y horas, crescimento de Z%),…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
