---
task: textToSqlWorker()
responsavel: "Text-to-SQL Worker"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pergunta em linguagem natural + contexto da sessão (filtros ativos, período, entidade) + schema semântico da empresa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "SQL gerado + resultado da query (tabela/número) + interpretação da métrica consultada + flag de confiança (alta/média/baixa)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Qualquer pergunta que referencie métricas numéricas, KPIs, comparações temporais ou segmentações. Disparado pelo Sigma após classificação de intenção como 'operacional' ou 'exploratória'."
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

# Traduzir Pergunta Para Sql

**Task ID:** `textToSqlWorker()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Traduzir Pergunta Para Sql |
| **status** | `pending` |
| **responsible_executor** | Text-to-SQL Worker (Hermes (Text-to-SQL Worker)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Traduz a pergunta em linguagem natural para SQL valido contra o schema da camada semantica governada. Usa a definicao formal das metricas (sem inventar joins ou filtros nao mapeados). Executa a query, retorna o resultado bruto + o SQL gerado (transparencia total). Se a pergunta e ambigua, gera 2-3 interpretacoes possiveis e aguarda disambiguation. Nunca acessa fontes fora da camada semantica aprovada.

## Input

- Pergunta em linguagem natural + contexto da sessão (filtros ativos, período, entidade) + schema semântico da empresa

## Output

- SQL gerado + resultado da query (tabela/número) + interpretação da métrica consultada + flag de confiança (alta/média/baixa)

## Trigger

Qualquer pergunta que referencie métricas numéricas, KPIs, comparações temporais ou segmentações. Disparado pelo Sigma após classificação de intenção como 'operacional' ou 'exploratória'.

## Knowledge base (o que o executor consulta)

- Semantic Layer completo da empresa (definições formais de métricas, schema SQL, glossário de jargão interno, histórico de queries anteriores para few-shot learning, lista de métricas proibidas/não-governadas)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pergunta em linguagem natural + contexto da sessão (filtros ativos, período, entidade) + schema semântico da empresa).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (SQL gerado + resultado da query (tabela/número) + interpretação da métrica consultada + flag de confiança (alta/média/b…) e persistir no artefato do squad.
4. Entregar ao critic SQL & Semantic Verifier; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: SQL gerado + resultado da query (tabela/número) + interpretação da métrica consultada + flag de confiança (alta/média/baixa)
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

- **to:** Context Enricher
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
