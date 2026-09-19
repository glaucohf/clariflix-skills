---
task: decisionLogger()
responsavel: "Decision Logger"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Resposta entregue ao founder + confirmação de que decisão foi tomada + descrição da ação + prazo esperado de resultado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ticket no ClickUp com audit trail da decisão + notificação de follow-up na data de resultado + relatório mensal de 'decisões baseadas em dados: acertamos?' com taxa de acerto"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Founder confirma ação após receber resposta analítica. Também disparado automaticamente na chegada da data de resultado de decisões registradas para coletar feedback."
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

# Registrar Decisões Baseadas em Dados

**Task ID:** `decisionLogger()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Registrar Decisões Baseadas em Dados |
| **status** | `pending` |
| **responsible_executor** | Decision Logger (Clio (Decision Logger)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Registra cada decisão tomada pelo founder com base em dados do squad, criando um audit trail verificável. Para cada resposta entregue ao founder, se ele indicar que vai agir com base nela, Clio cria um ticket no ClickUp com: a pergunta, a resposta, os dados usados, a decisão tomada, e a data esperada de resultado. Em follow-ups futuros, compara o resultado real com o esperado (feedback loop de qualidade das decisões baseadas em dados).

## Input

- Resposta entregue ao founder + confirmação de que decisão foi tomada + descrição da ação + prazo esperado de resultado

## Output

- Ticket no ClickUp com audit trail da decisão + notificação de follow-up na data de resultado + relatório mensal de 'decisões baseadas em dados: acertamos?' com taxa de acerto

## Trigger

Founder confirma ação após receber resposta analítica. Também disparado automaticamente na chegada da data de resultado de decisões registradas para coletar feedback.

## Knowledge base (o que o executor consulta)

- Histórico de decisões registradas + resultados confirmados + métricas de acurácia preditiva das análises anteriores + calendário de follow-ups pendentes

## Action Items

1. Confirmar o gatilho e carregar a entrada (Resposta entregue ao founder + confirmação de que decisão foi tomada + descrição da ação + prazo esperado de resultado).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ticket no ClickUp com audit trail da decisão + notificação de follow-up na data de resultado + relatório mensal de 'dec…) e persistir no artefato do squad.
4. Entregar ao critic SQL & Semantic Verifier; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ticket no ClickUp com audit trail da decisão + notificação de follow-up na data de resultado + relatório mensal de 'decisões baseadas em dados: acertamos?' com…
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

- **to:** SQL & Semantic Verifier
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
