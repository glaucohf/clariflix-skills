---
task: cassandra()
responsavel: "Cassandra"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Histórico de pipeline e receita fechada (12 meses mínimo do CRM), dados de spend planejado por canal (planilha/ClickUp), métricas de funil atuais do Nexus, eventos futuros conhecidos (lançamentos, feriados, high-seasons), metas de pipeline por período"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de forecast semanal: pipeline esperado (P50), range de confiança (P20-P80), gap vs meta com semáforo (verde/amarelo/vermelho), top-3 riscos ao forecast com probabilidade, cenários what-if solicitados pelo usuário e recomendações de ajuste de budget para atingir meta"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Formato: JSON estruturado + narrativa executiva em português"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Todo domingo as 18h (forecast semanal automático); primeiro dia útil do mês (forecast mensal); quando Atlas recebe pergunta de forecast ou what-if; quando Argus detecta anomalia P1 (refaz forecast co…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Skeptic antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar ou corrigir antes do go-live. SLA: 30min para resposta, após isso o sistema notifica o gestor direto."
    - "[ ] L3: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor de media antes de execucao. O squad gera o racional completo, humano aprova ou rejeita com comentario."
    - "[ ] L3: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing de 5 linhas e aguarda confirmação de que foi visto (acknowledgment) antes de escalar para investigação automática mais profunda."
    - "[ ] L2: Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta. Previne drift de sensibilidade ao longo do tempo."
    - "[ ] L2: Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP de Marketing. Revisão trimestral."
---

# Gerar Forecast Pipeline

**Task ID:** `cassandra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Funnel Analytics & Attribution Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Forecast Pipeline |
| **status** | `pending` |
| **responsible_executor** | Cassandra (Cassandra — Agente de Forecast de Pipelíne) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de previsao. Gera forecast semanal e mensal de pipeline e receita usando modelos de serie temporal (Prophet + regressao com features externas: spend planejado, sazonalidade historica, dados de intent de mercado). Calcula intervalo de confianca de 80% e 95%, identifica os principais drivers de variacao (quais campanhas/canais tem maior impacto no forecast) e alerta quando o pipeline projetado estiver abaixo da meta. Tambem gera cenarios 'what-if' para perguntas como 'se cortarmos 20% do budget de Google, qual o impacto no pipeline?'.

## Input

- Histórico de pipeline e receita fechada (12 meses mínimo do CRM), dados de spend planejado por canal (planilha/ClickUp), métricas de funil atuais do Nexus, eventos futuros conhecidos (lançamentos, feriados, high-seasons), metas de pipeline por período

## Output

- Relatório de forecast semanal: pipeline esperado (P50), range de confiança (P20-P80), gap vs meta com semáforo (verde/amarelo/vermelho), top-3 riscos ao forecast com probabilidade, cenários what-if solicitados pelo usuário e recomendações de ajuste de budget para atingir meta
- Formato: JSON estruturado + narrativa executiva em português

## Trigger

Todo domingo as 18h (forecast semanal automático); primeiro dia útil do mês (forecast mensal); quando Atlas recebe pergunta de forecast ou what-if; quando Argus detecta anomalia P1 (refaz forecast com cenário pessimista).

## Knowledge base (o que o executor consulta)

- Histórico de pipeline e receita (CRM, 12+ meses), modelos treinados de Prophet por segmento/canal, elasticidade de spend por canal (quanto pipeline gera R$1k adicional por canal), sazonalidade histórica por segmento ICP, metas de pipeline por período (ClickUp/CRM), benchmarks de velocity por etapa do funil

## Action Items

1. Confirmar o gatilho e carregar a entrada (Histórico de pipeline e receita fechada (12 meses mínimo do CRM), dados de spend planejado por canal (planilha/ClickUp)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de forecast semanal: pipeline esperado (P50), range de confiança (P20-P80), gap vs meta com semáforo (verde/a…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de forecast semanal: pipeline esperado (P50), range de confiança (P20-P80), gap vs meta com semáforo (verde/amarelo/vermelho), top-3 riscos ao foreca…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Skeptic registrado
- [ ] Gate L3 respeitado: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de cam…
- [ ] Gate L3 respeitado: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovaca…
- [ ] Gate L3 respeitado: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor d… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta.… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão de relatório executivo antes de envio ao board: Oracle gera, Skeptic valida, mas um humano (CMO ou analista sênior) faz leitura final antes de envio ao… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Skeptic | BLOQUEIA entrega |

## Handoff

- **to:** Lumen
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
