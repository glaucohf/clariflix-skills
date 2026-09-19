---
task: lyra()
responsavel: "Lyra"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Top-10 tendências priorizadas do Orion com dados completos (volume, delta, sentimento, verbatims, correlações, breakdown por segmento) + histórico dos últimos 4 relatórios semanais para comparação de tendências no tempo + alertas de emergência da semana do Rapid + métricas de pipeline do Haruki e Yara da semana + templates de relatório versionados no Supabase"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio semanal completo em markdown persistido no Supabase e postado no Notion (tabela: voc_weekly_reports): titulo com data, sumario executivo, top-5 tendencias com evidencias citadas, alertas, declinos, sugestoes de acao e metricas"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Versao resumida formatada para Slack (< 300 palavras)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Tasks de acao geradas no ClickUp para o Atlas criar apos aprovacao HITL"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Historico de relatorios indexado para busca por tema"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron semanal segunda-feira 09h00 após Orion confirmar ranking semanal disponível; acionado sob demanda pelo PM ou Head de CS via comando no ClickUp ('*gerar-relatório-voc agora'); acionado automatica…"
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

# Sintetizar Relatório Executivo

**Task ID:** `lyra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Relatório Executivo |
| **status** | `pending` |
| **responsible_executor** | Lyra (Lyra — Sintetizadora de Relatório e Narrativa) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Transforma o ranking de tendencias priorizadas pelo Orion em um relatorio executivo semanal legivel, acionavel e com fontes citadas — o artefato principal entregue ao PM, Head de Produto e Head de CS. O relatorio segue estrutura fixa: (1) SUMARIO EXECUTIVO (200 palavras max) — 3-5 bullets com os insights mais criticos da semana, comparando com semana anterior; (2) TOP-5 TENDENCIAS PRIORIZADAS — para cada tendencia: nome do tema, score de priorizacao, volume de mencoes, variacao vs semana anterior, sentimento medio, breakdown por segmento, 3-5 verbatims representativos com canal e data de origem (sem PII), correlacao com evento de produto se existir; (3) ALERTAS DE EMERGENCIA — tendencias que cruzaram threshold na semana com destaque e urgencia; (4) TENDENCIAS EM DECLINIO — o que melhorou: validacao de acoes anteriores; (5) SUGESTOES DE ACAO — para cada tendencia top-5: uma recomendacao especifica de acao (bug para engenharia, gap de KB para CS, feature request para PM, processo para ops) com justificativa baseada em volume e segmento; (6) METRICAS DO PIPELINE — volume total processado por canal, distribucao de sentimento geral, NPS medio da semana se disponivel. Gera duas versoes: resumo executivo em Slack (< 300 palavras + link para relatorio completo) e relatorio completo em markdown no Notion/ClickUp.

## Input

- Top-10 tendências priorizadas do Orion com dados completos (volume, delta, sentimento, verbatims, correlações, breakdown por segmento) + histórico dos últimos 4 relatórios semanais para comparação de tendências no tempo + alertas de emergência da semana do Rapid + métricas de pipeline do Haruki e Yara da semana + templates de relatório versionados no Supabase

## Output

- Relatorio semanal completo em markdown persistido no Supabase e postado no Notion (tabela: voc_weekly_reports): titulo com data, sumario executivo, top-5 tendencias com evidencias citadas, alertas, declinos, sugestoes de acao e metricas
- Versao resumida formatada para Slack (< 300 palavras)
- Tasks de acao geradas no ClickUp para o Atlas criar apos aprovacao HITL
- Historico de relatorios indexado para busca por tema

## Trigger

Cron semanal segunda-feira 09h00 após Orion confirmar ranking semanal disponível; acionado sob demanda pelo PM ou Head de CS via comando no ClickUp ('*gerar-relatório-voc agora'); acionado automaticamente quando Rapid confirma alerta de emergência que requer briefing imediato fora do ciclo semanal

## Knowledge base (o que o executor consulta)

- Historico dos ultimos 4 relatorios semanais (para identificar temas que persisem, surgem ou somem), templates de relatorio aprovados (2 versoes: executiva para Slack, completa para Notion/ClickUp), criterios de selecao de verbatims representativos (diversidade de canal, segmento e intencao
- nunca usar verbatim de empresa identificavel), regras de recomendacao de acao por tipo de tendencia (bug recorrente -> engenharia
- lacuna de documentacao -> CS/KB
- feature request com volume alto -> PM backlog
- processo falho -> ops), historico de acoes tomadas em resposta a relatorios anteriores para evitar repeticao de sugestao ja implementada

## Action Items

1. Confirmar o gatilho e carregar a entrada (Top-10 tendências priorizadas do Orion com dados completos (volume, delta, sentimento, verbatims, correlações, breakdow…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio semanal completo em markdown persistido no Supabase e postado no Notion (tabela: voc_weekly_reports): titulo…) e persistir no artefato do squad.
4. Entregar ao critic Cassandra; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio semanal completo em markdown persistido no Supabase e postado no Notion (tabela: voc_weekly_reports): titulo com data, sumario executivo, top-5 tende…
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

- **to:** Rapid
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
