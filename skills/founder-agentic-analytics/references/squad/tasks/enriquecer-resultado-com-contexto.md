---
task: contextEnricher()
responsavel: "Context Enricher"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Resultado bruto da query (numero/tabela) + metrica consultada + periodo + knowledge base de eventos corporativos"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resultado contextualizado com comparações históricas + interpretação narrativa em linguagem natural + identificação de tendência (subindo/caindo/estável) + eventos explicativos se relevante"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado automaticamente após Hermes retornar resultado. Sempre ativo exceto para queries de lookup simples (ex: 'qual o email do cliente X')."
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

# Enriquecer Resultado Com Contexto

**Task ID:** `contextEnricher()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Resultado Com Contexto |
| **status** | `pending` |
| **responsible_executor** | Context Enricher (Mnemosyne (Context Enricher)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Enriquece o resultado bruto do Hermes com contexto histórico e narrativa. Compara o número atual com média móvel, mesmo período ano anterior, meta do período, benchmarks do setor. Identifica se o número é bom, ruim ou neutro dado o contexto. Gera a interpretação em 2-3 frases que um founder entende sem ser analista. Também busca no knowledge base corporativo eventos que explicam anomalias (campanha, lançamento, sazonalidade).

## Input

- Resultado bruto da query (numero/tabela) + metrica consultada + periodo + knowledge base de eventos corporativos

## Output

- Resultado contextualizado com comparações históricas + interpretação narrativa em linguagem natural + identificação de tendência (subindo/caindo/estável) + eventos explicativos se relevante

## Trigger

Disparado automaticamente após Hermes retornar resultado. Sempre ativo exceto para queries de lookup simples (ex: 'qual o email do cliente X').

## Knowledge base (o que o executor consulta)

- Séries históricas das métricas (12 meses rolling), calendário de eventos corporativos (lançamentos, campanhas, crises), metas e OKRs do período, benchmarks setoriais atualizados trimestralmente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Resultado bruto da query (numero/tabela) + metrica consultada + periodo + knowledge base de eventos corporativos).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resultado contextualizado com comparações históricas + interpretação narrativa em linguagem natural + identificação de…) e persistir no artefato do squad.
4. Entregar ao critic SQL & Semantic Verifier; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resultado contextualizado com comparações históricas + interpretação narrativa em linguagem natural + identificação de tendência (subindo/caindo/estável) + eve…
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

- **to:** Anomaly & Alert Detector
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
