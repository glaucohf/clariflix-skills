---
task: semanticLayerGuardian()
responsavel: "Semantic Layer Guardian"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lóg de queries falhadas ou com baixa confiança + proposta de nova métrica (nome, fórmula, fonte, granularidade, owner) + changelog atual do schema"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Proposta formal de nova métrica para aprovação humana + relatório de gaps recorrentes (top 10 perguntas sem cobertura) + alertas de inconsistência de definição + changelog atualizado após aprovacao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Falha do Hermes (métrica não encontrada) + confiança < 70% em 3 queries consecutivas sobre o mesmo tema + detecção de definições conflitantes entre métricas existentes + solicitação mensal de revisão…"
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

# Registrar Gap Semantico

**Task ID:** `semanticLayerGuardian()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Registrar Gap Semantico |
| **status** | `pending` |
| **responsible_executor** | Semantic Layer Guardian (Ariadné (Semantic Layer Guardian)) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsavel pela integridade e evolucao da camada semantica. Quando o Hermes falha em responder (metrica nao mapeada, pergunta sobre dado inexistente), Ariadne registra o gap, propoe a definicao formal da nova metrica, e encaminha para aprovacao humana antes de adicionar ao schema. Tambem detecta quando duas metricas existentes parecem conflitantes e gera alertas de inconsistencia para resolucao. Mantem o changelog do schema semantico.

## Input

- Lóg de queries falhadas ou com baixa confiança + proposta de nova métrica (nome, fórmula, fonte, granularidade, owner) + changelog atual do schema

## Output

- Proposta formal de nova métrica para aprovação humana + relatório de gaps recorrentes (top 10 perguntas sem cobertura) + alertas de inconsistência de definição + changelog atualizado após aprovacao

## Trigger

Falha do Hermes (métrica não encontrada) + confiança < 70% em 3 queries consecutivas sobre o mesmo tema + detecção de definições conflitantes entre métricas existentes + solicitação mensal de revisão do schema.

## Knowledge base (o que o executor consulta)

- Schema semântico atual completo + changelog de versões + log de queries falhadas (últimos 90 dias) + definições aprovadas e rejeitadas historicamente + documentação das fontes de dados

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lóg de queries falhadas ou com baixa confiança + proposta de nova métrica (nome, fórmula, fonte, granularidade, owner)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Proposta formal de nova métrica para aprovação humana + relatório de gaps recorrentes (top 10 perguntas sem cobertura)…) e persistir no artefato do squad.
4. Entregar ao critic SQL & Semantic Verifier; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Proposta formal de nova métrica para aprovação humana + relatório de gaps recorrentes (top 10 perguntas sem cobertura) + alertas de inconsistência de definição…
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

- **to:** Decision Logger
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
