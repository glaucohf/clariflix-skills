---
task: anomalyAlertDetector()
responsavel: "Anomaly & Alert Detector"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Snapshot diário das métricas críticas + baseline histórico + thresholds configurados pelo founder + calendário de eventos esperados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Digest diário de anomalias (zero se nada relevante) + alertas classificados por severidade + hipóteses de causa + queries sugeridas para investigar mais fundo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job diario automatico (6h da manha) + disparo sob demanda quando founder pergunta sobre anomalias ou variações inesperadas. Alertas criticos geram notificacao imediata via Slack."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SQL & Semantic Verifier antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível pois altera definições que afetam todas as queries futuras)"
    - "[ ] HITL: Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a oficial — L3)"
    - "[ ] HITL: Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no setup inicial, L2 depois)"
    - "[ ] HITL: Confirmação de decisão tomada com base em dados para o Clío registrar (founder confirma que vai agir — não é automático para evitar log de decisões não tomadas)"
    - "[ ] HITL: Acesso a novas fontes de dados não mapeadas (conectar novo banco, nova planilha, nova API ao schema — L3 por impacto na governança)"
---

# Detectar Anomalias Estatísticas

**Task ID:** `anomalyAlertDetector()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Anomalias Estatísticas |
| **status** | `pending` |
| **responsible_executor** | Anomaly & Alert Detector (Cassandra (Anomaly & Alert Detector)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora proativamente as métricas críticas em busca de anomalias estatísticas (desvio > 2 sigma, quedas abruptas, tendências de deterioração). Não espera ser perguntada — roda em batch diário e gera alertas quando detecta sinal. Classifica alertas por severidade (crítico/atenção/informativo) e sugere hipóteses de causa raiz. Também responde perguntas do tipo 'teve alguma anomalia essa semana?'.

## Input

- Snapshot diário das métricas críticas + baseline histórico + thresholds configurados pelo founder + calendário de eventos esperados

## Output

- Digest diário de anomalias (zero se nada relevante) + alertas classificados por severidade + hipóteses de causa + queries sugeridas para investigar mais fundo

## Trigger

Job diario automatico (6h da manha) + disparo sob demanda quando founder pergunta sobre anomalias ou variações inesperadas. Alertas criticos geram notificacao imediata via Slack.

## Knowledge base (o que o executor consulta)

- Histórico de todas as métricas (24 meses), definição de thresholds por métrica (configurável pelo founder), log de anomalias anteriores e suas causas confirmadas, calendário de sazonalidade do negócio

## Action Items

1. Confirmar o gatilho e carregar a entrada (Snapshot diário das métricas críticas + baseline histórico + thresholds configurados pelo founder + calendário de event…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Digest diário de anomalias (zero se nada relevante) + alertas classificados por severidade + hipóteses de causa + queri…) e persistir no artefato do squad.
4. Entregar ao critic SQL & Semantic Verifier; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Digest diário de anomalias (zero se nada relevante) + alertas classificados por severidade + hipóteses de causa + queries sugeridas para investigar mais fundo
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SQL & Semantic Verifier registrado
- [ ] Gate HITL respeitado: Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível…
- [ ] Gate HITL respeitado: Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a o…
- [ ] Gate HITL respeitado: Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível pois altera definiç… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a oficial — L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no setup inicial, L2 d… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Confirmação de decisão tomada com base em dados para o Clío registrar (founder confirma que vai agir — não é automático para evitar log de decisões não tomadas) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Acesso a novas fontes de dados não mapeadas (conectar novo banco, nova planilha, nova API ao schema — L3 por impacto na governança) | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic SQL & Semantic Verifier | BLOQUEIA entrega |

## Handoff

- **to:** Strategic Query Analyst
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
