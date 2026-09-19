---
task: histos()
responsavel: "Histos"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Log completo de tickets dos últimos 30/90 dias com todos os campos (tempo de resolução, breach flag, complexity score, agente, tipo, módulo, tier) + resultados de escalonamentos anteriores (o Alarme escalou e o breach foi evitado? ou escalou mas breach aconteceu mesmo assim?) + dados de carga de fila histórica por hora do dia"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório semanal em Markdown no ClickUp: Top 5 causas raiz de breach (com exemplos), agentes ou filas que precisam de atenção, tickets breachados esta semana com análise de causa, tendências de complexidade por módulo, recomendações de ajuste de SLA ou processo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "+ Dataset de recalibração para o Cronos (JSON com novos exemplos rotulados)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "+ Alert automático se breach rate semanal > threshold configurado (ex: >5 breaches/semana = alerta imediato para ops manager)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Trigger automático diário às 7h (resumo do dia anterior) e semanal às segunda-feira 8h (relatório da semana). Trigger imediato se breach rate nas últimas 24h ultrapassar threshold crítico (ex: 3 brea…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Cético de SLA antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade baixa (interrompe o fluxo do agente atual)."
    - "[ ] HITL: Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders. Ação de alto impacto e irreversível em termos de alarme organizacional."
    - "[ ] HITL: Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes do envio. Toda comunicação com cliente é revisada por humano."
    - "[ ] HITL: Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. Ocorre quando dados são ambíguos ou incompletos."
    - "[ ] HITL: Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para avaliação manual do risco de breach. Cronos não especula sem dados."
---

# Analisar Dados De SLA

**Task ID:** `histos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de SLA & Health Monitoring Operacional

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Dados De SLA |
| **status** | `pending` |
| **responsible_executor** | Histos (Histos — Analista de Padrões e Tendências) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

O agente que transforma dados de SLA em inteligência operacional. Não opera no ciclo de 15 minutos — roda em batch diário e semanal. Analisa padrões históricos de breach para identificar causas raiz recorrentes: quais tipos de ticket breacham mais? qual agente tem velocidade abaixo do benchmark? qual módulo do produto gera mais tickets complexos? qual dia da semana tem pior aderência ao SLA? Produz dois artefatos: (1) Relatório semanal de SLA Health com tendências e recomendações operacionais; (2) Atualizações para o modelo de pesos do Cronos (dataset de novos exemplos de breach/não-breach para recalibração mensal).

## Input

- Log completo de tickets dos últimos 30/90 dias com todos os campos (tempo de resolução, breach flag, complexity score, agente, tipo, módulo, tier) + resultados de escalonamentos anteriores (o Alarme escalou e o breach foi evitado? ou escalou mas breach aconteceu mesmo assim?) + dados de carga de fila histórica por hora do dia

## Output

- Relatório semanal em Markdown no ClickUp: Top 5 causas raiz de breach (com exemplos), agentes ou filas que precisam de atenção, tickets breachados esta semana com análise de causa, tendências de complexidade por módulo, recomendações de ajuste de SLA ou processo
- + Dataset de recalibração para o Cronos (JSON com novos exemplos rotulados)
- + Alert automático se breach rate semanal > threshold configurado (ex: >5 breaches/semana = alerta imediato para ops manager)

## Trigger

Trigger automático diário às 7h (resumo do dia anterior) e semanal às segunda-feira 8h (relatório da semana). Trigger imediato se breach rate nas últimas 24h ultrapassar threshold crítico (ex: 3 breaches em 1 dia quando baseline é <1/semana).

## Knowledge base (o que o executor consulta)

- Banco de dados histórico completo de tickets com SLA (Supabase
- mínimo 90 dias), log de escalonamentos do Alarme com resultado (breach evitado: sim/não), pesos atuais do modelo do Cronos, benchmarks de SLA do setor do cliente, metas de SLA compliance acordadas contratualmente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Log completo de tickets dos últimos 30/90 dias com todos os campos (tempo de resolução, breach flag, complexity score,…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório semanal em Markdown no ClickUp: Top 5 causas raiz de breach (com exemplos), agentes ou filas que precisam de…) e persistir no artefato do squad.
4. Entregar ao critic Cético de SLA; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório semanal em Markdown no ClickUp: Top 5 causas raiz de breach (com exemplos), agentes ou filas que precisam de atenção, tickets breachados esta semana…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Cético de SLA registrado
- [ ] Gate HITL respeitado: Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executa…
- [ ] Gate HITL respeitado: Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar mú…
- [ ] Gate HITL respeitado: Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade b… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. O… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para a… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Histos detecta breach rate semanal acima do threshold crítico: relatório é revisado por ops manager antes de publicação, que decide se aciona revisão de proces… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Recalibração mensal do modelo do Cronos (Histos gera novo dataset): pesos atualizados são revisados por ops lead antes de ir para produção. Mudança no modelo p… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Cético de SLA | BLOQUEIA entrega |

## Handoff

- **to:** Âncora
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
