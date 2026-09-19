---
task: strategicQueryAnalyst()
responsavel: "Strategic Query Analyst"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pergunta estratégica complexa + contexto do negócio + semantic layer + dados históricos + OKRs atuais"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Análise estruturada com: decomposição da pergunta, dados de cada sub-query, síntese estratégica, nível de confiança, premissas assumidas, recomendação de ação com trade-offs"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Perguntas classificadas pelo Sigma como 'estrategicas' ou que contenham palavras-chave como 'por que', 'qual devo', 'melhor', 'projecao', 'impacto de', 'comparar'. Tambem disparado por solicitacao ex…"
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

# Sintetizar Respostas Analíticas

**Task ID:** `strategicQueryAnalyst()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Respostas Analíticas |
| **status** | `pending` |
| **responsible_executor** | Strategic Query Analyst (Athena (Strategic Query Analyst)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em perguntas estrategicas complexas que requerem multiples queries encadeadas, cruzamento de datasets e raciocinio analitico. Exemplos: 'qual cohort de cliente tem maior LTV e o que eles tem em comum?', 'se eu dobrar investimento em canal X, qual o impacto projetado no CAC?', 'qual produto tem maior margem de contribuicao por hora de CS gasta?'. Decompoe a pergunta em sub-hipoteses, executa cada uma, e sintetiza uma resposta estrategica com nivel de confianca.

## Input

- Pergunta estratégica complexa + contexto do negócio + semantic layer + dados históricos + OKRs atuais

## Output

- Análise estruturada com: decomposição da pergunta, dados de cada sub-query, síntese estratégica, nível de confiança, premissas assumidas, recomendação de ação com trade-offs

## Trigger

Perguntas classificadas pelo Sigma como 'estrategicas' ou que contenham palavras-chave como 'por que', 'qual devo', 'melhor', 'projecao', 'impacto de', 'comparar'. Tambem disparado por solicitacao explicita do founder.

## Knowledge base (o que o executor consulta)

- Semantic layer completo + histórico de análises anteriores + contexto estratégico da empresa (OKRs, iniciativas, hipóteses do founder) + benchmarks competitivos + modelos financeiros básicos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pergunta estratégica complexa + contexto do negócio + semantic layer + dados históricos + OKRs atuais).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Análise estruturada com: decomposição da pergunta, dados de cada sub-query, síntese estratégica, nível de confiança, pr…) e persistir no artefato do squad.
4. Entregar ao critic SQL & Semantic Verifier; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Análise estruturada com: decomposição da pergunta, dados de cada sub-query, síntese estratégica, nível de confiança, premissas assumidas, recomendação de ação…
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

- **to:** Semantic Layer Guardian
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
