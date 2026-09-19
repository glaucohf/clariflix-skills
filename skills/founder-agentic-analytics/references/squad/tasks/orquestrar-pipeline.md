---
task: orquestradorAnaliticoPipeline()
responsavel: "Orquestrador Analítico"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta analítica source-grounded: número preciso + SQL transparente + interpretação contextualizada + nível de confiança + recomendação de ação"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "tudo rastreável à fonte de dados governada"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefatos secundários: (1) Semantic Layer Glossary (documento vivo com todas as métricas definidas formalmente)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(2) Daily Anomaly Digest (email/Slack diário com sinais relevantes ou confirmação de normalidade)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Decision Audit Trail no ClickUp (histórico de todas as decisões tomadas com dados)"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(4) Monthly Analytics Health Report (cobertura, acurácia, gaps, evolução de adoção)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe a pergunta em linguagem natural do founder, classifica a intencao (exploratoria, operacional, estrategica, anomalia), decompoe em sub-queries se necessario, roteia para o worker correto (SQL p…"
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

# Orquestrar Pipeline do Ágentic Analytics

**Task ID:** `orquestradorAnaliticoPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Ágentic Analytics |
| **status** | `pending` |
| **responsible_executor** | Orquestrador Analítico (Sigma (Orquestrador Analítico)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe a pergunta em linguagem natural do founder, classifica a intencao (exploratoria, operacional, estrategica, anomalia), decompoe em sub-queries se necessario, roteia para o worker correto (SQL puro, enriquecimento semantico, contexto historico ou alerta), agrega os resultados parciais, solicita validacao do Critic antes de entregar, e formata a resposta final com dados + interpretacao + recomendacao de acao. Mantém o estado da sessao para perguntas encadeadas ('e no mes passado?', 'e por canal?').

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Resposta analítica source-grounded: número preciso + SQL transparente + interpretação contextualizada + nível de confiança + recomendação de ação
- tudo rastreável à fonte de dados governada
- Artefatos secundários: (1) Semantic Layer Glossary (documento vivo com todas as métricas definidas formalmente)
- (2) Daily Anomaly Digest (email/Slack diário com sinais relevantes ou confirmação de normalidade)
- (3) Decision Audit Trail no ClickUp (histórico de todas as decisões tomadas com dados)
- (4) Monthly Analytics Health Report (cobertura, acurácia, gaps, evolução de adoção)

## Trigger

Recebe a pergunta em linguagem natural do founder, classifica a intencao (exploratoria, operacional, estrategica, anomalia), decompoe em sub-queries se necessario, roteia para o worker correto (SQL puro, enriquecimento semantico, contexto historico ou alerta), agrega os resultados parciais, solicita validacao do Critic antes de entregar, e formata a resposta final com dados + interpretacao + recomendacao de acao. Mantém o estado da sessao para perguntas encadeadas ('e no mes passado?', 'e por canal?').

## Knowledge base (o que o executor consulta)

- WrenAI ou equivalente open-source (camada semântica governada, contexto semântico sobre SQL, suporte a 20+ fontes)
- PostgreSQL / MySQL / BigQuery / Snowflake (banco de dados transacional ou warehouse da empresa)
- HubSpot ou Salesforce CRM (métricas de pipeline, conversão, receita por fonte)
- Stripe / Conta Azul / Omie (métricas financeiras: MRR, churn, LTV, inadimplência)
- Google Ads / Meta Ads (CAC por canal, ROAS, CPC, impressões)
- Google Sheets / Notion (fontes de dados semi-estruturadas do founder)
- ClickUp (registro de decisões, audit trail, follow-ups do Clio)
- Slack (entrega de alertas críticos da Cassandra, interface conversacional opcional)
- Langfuse (observabilidade OTEL: rastreamento de cada query, custo de tokens, latência, acurácia)
- Claude Agent SDK + LangGraph (orquestração stateful das sessões analíticas multi-turno)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic SQL & Semantic Verifier antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta analítica source-grounded: número preciso + SQL transparente + interpretação contextualizada + nível de confiança + recomendação de ação
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

- **to:** Text-to-SQL Worker
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
