---
task: argus()
responsavel: "Argus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stream de métricas normalizadas do Nexus (impressões, cliques, CTR, CVR por etapa, CPC, CPL, volume de MQL/SQL, taxa de no-show), thresholds de anomalia configurados (ou aprendidos automaticamente com 30d de histórico), calendário de eventos de negócio (lançamentos, feriados, sazonalidade) para suprimir falsos positivos"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alertas de anomalia estruturados (severidade, metrica afetada, canal/campanha, magnitude do desvio, timestamp de inicio, impacto estimado em R$ de pipeline, hipoteses provavies de causa, acoes recomendadas imediatas)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Canal de notificacao: Slack webhook (P1 imediato), email digest (P2/P3 a cada 4h)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "JSON de status de saude do funil atualizado a cada ciclo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Schedule a cada 30min para métricas P1 (CVR, CPC, volume de leads); schedule horário para métricas P2 (CTR, bounce rate, tempo de qualificação); trigger imediato quando Nexus reporta queda de volume…"
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

# Detectar Anomalias KPIs

**Task ID:** `argus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Funnel Analytics & Attribution Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Anomalias KPIs |
| **status** | `pending` |
| **responsible_executor** | Argus (Argus — Agente de Detecção de Anomalias) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de vigilância contínua. Monitora em tempo quase-real (schedule a cada 30min para métricas críticas, horário para métricas secundárias) todos os KPIs do funil e detecta desvios estatisticamente significativos usando z-score com janela deslizante, Prophet para sazonalidade e regras heurísticas de negócio (ex: 'se CPC de Google sobe >40% em <2h, é anomalia'). Classifica anomalias por severidade (P1: impacto imediato em receita, P2: degradação de eficiência, P3: alerta informativo) e dispara alertas com contexto suficiente para ação imediata.

## Input

- Stream de métricas normalizadas do Nexus (impressões, cliques, CTR, CVR por etapa, CPC, CPL, volume de MQL/SQL, taxa de no-show), thresholds de anomalia configurados (ou aprendidos automaticamente com 30d de histórico), calendário de eventos de negócio (lançamentos, feriados, sazonalidade) para suprimir falsos positivos

## Output

- Alertas de anomalia estruturados (severidade, metrica afetada, canal/campanha, magnitude do desvio, timestamp de inicio, impacto estimado em R$ de pipeline, hipoteses provavies de causa, acoes recomendadas imediatas)
- Canal de notificacao: Slack webhook (P1 imediato), email digest (P2/P3 a cada 4h)
- JSON de status de saude do funil atualizado a cada ciclo

## Trigger

Schedule a cada 30min para métricas P1 (CVR, CPC, volume de leads); schedule horário para métricas P2 (CTR, bounce rate, tempo de qualificação); trigger imediato quando Nexus reporta queda de volume >30% em qualquer fonte; início de campanha nova (baseline period de 48h com thresholds mais permissivos).

## Knowledge base (o que o executor consulta)

- Histórico de métricas por canal (90 dias) para calibração de z-score, calendário de sazonalidade e eventos da empresa (para suprimir falsos positivos), playbooks de resposta por tipo de anomalia (queda de CVR, spike de CPC, queda de volume, aumento de CPL), SLAs de tempo de resposta por severidade, benchmarks de variação normal por canal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stream de métricas normalizadas do Nexus (impressões, cliques, CTR, CVR por etapa, CPC, CPL, volume de MQL/SQL, taxa de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alertas de anomalia estruturados (severidade, metrica afetada, canal/campanha, magnitude do desvio, timestamp de inicio…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alertas de anomalia estruturados (severidade, metrica afetada, canal/campanha, magnitude do desvio, timestamp de inicio, impacto estimado em R$ de pipeline, hi…
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

- **to:** Cassandra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
