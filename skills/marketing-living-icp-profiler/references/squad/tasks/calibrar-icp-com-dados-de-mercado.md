---
task: nox()
responsavel: "Nox"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Segmentos candidatos do ICP Canvas (Atlas output), descrição atual do produto/serviço, wins e losses recentes anotados no CRM, verticais de mercado a investigar"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "PMF Score por segmento (1-10 com justificativa), TAM/SAM/SOM estimado por segmento, Dores primárias x secundárias mapeadas por segmento, Adjacency Map (novos segmentos com fit potencial), recomendação de priorização de segmentos para o ICP"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo trimestral de revisao de ICP; novo produto/feature lancado; Maestro detecta queda de conversion rate em segmento especifico; solicitacao manual do CMO/CEO"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vera 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3)"
    - "[ ] HITL: Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3)"
    - "[ ] HITL: Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)"
    - "[ ] HITL: Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3)"
    - "[ ] HITL: Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1)"
---

# Calibrar Icp Com Dados De Mercado

**Task ID:** `nox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Living ICP Profiler

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calibrar Icp Com Dados De Mercado |
| **status** | `pending` |
| **responsible_executor** | Nox (Nóx — PMF Deep Research Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em Product-Market Fit research para calibrar o ICP com dados de mercado total. Executa pesquisas estruturadas sobre TAM/SAM/SOM por segmento, analisa fit entre o produto atual e as dores dos segmentos mapeados, identifica adjacências de mercado não exploradas. Referência direta ao 'Profiling de PMF -> Deepresearch / Researchs do Alan' citado pelo board.

## Input

- Segmentos candidatos do ICP Canvas (Atlas output), descrição atual do produto/serviço, wins e losses recentes anotados no CRM, verticais de mercado a investigar

## Output

- PMF Score por segmento (1-10 com justificativa), TAM/SAM/SOM estimado por segmento, Dores primárias x secundárias mapeadas por segmento, Adjacency Map (novos segmentos com fit potencial), recomendação de priorização de segmentos para o ICP

## Trigger

Ciclo trimestral de revisao de ICP; novo produto/feature lancado; Maestro detecta queda de conversion rate em segmento especifico; solicitacao manual do CMO/CEO

## Knowledge base (o que o executor consulta)

- Descrição completa do produto com features e benefícios, base de wins/losses com motivo de compra e rejeição, relatórios de mercado por vertical, histórico de NPS e entrevistas de cliente, dados de churn com motivo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Segmentos candidatos do ICP Canvas (Atlas output), descrição atual do produto/serviço, wins e losses recentes anotados…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (PMF Score por segmento (1-10 com justificativa), TAM/SAM/SOM estimado por segmento, Dores primárias x secundárias mapea…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: PMF Score por segmento (1-10 com justificativa), TAM/SAM/SOM estimado por segmento, Dores primárias x secundárias mapeadas por segmento, Adjacency Map (novos s…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vera 2 registrado
- [ ] Gate HITL respeitado: Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento…
- [ ] Gate HITL respeitado: Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (…
- [ ] Gate HITL respeitado: Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3) | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de integração com nova fonte de dados de enriquecimento que implica custo adicional — qualquer nova ferramenta paga requer validação financeira (L3) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Vera 2 | BLOQUEIA entrega |

## Handoff

- **to:** Rex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
