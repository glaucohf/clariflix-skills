---
task: nexus()
responsavel: "Nexus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Credenciais de API configuradas (Google Ads, Meta Ads, HubSpot/Salesforce, GA4/Segment, LinkedIn Ads), janela de tempo da coleta e lista de events de interesse (lead, MQL, SQL, opportunity, closed-won)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tabela normalizada de touchpoints (JSON/Parquet) no formato canônico com schema versionado, log de qualidade de ingestão (% de registros com UTM completo, fontes ativas/inativas, volume por fonte vs baseline) e alertas de desvio de volume (>20% vs média móvel 7d)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Schedule horário automático para dados de ads e conversões; schedule diário para sync completo de CRM (oportunidades, fechamentos, valores); webhook imediato quando GA4/Segment emite evento de conver…"
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

# Coletar ETL Dados

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Funnel Analytics & Attribution Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coletar ETL Dados |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Agente de Coleta e Unificação de Dados) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de ETL/ingestão. Conecta a todas as fontes de dados (ads platforms, CRM, website analytics, CRM de vendas) via MCP servers e APIs, normaliza schemas heterogêneos para um modelo canônico de evento (source, medium, campaign, touchpoint_ts, user_id, event_type, value), deduplica touchpoints e persiste no data warehouse. Executa em schedule horário para dados de anomalia e diário para dados de atribuição completa. Alerta Atlas se qualquer fonte ficou offline ou com volume anômalo.

## Input

- Credenciais de API configuradas (Google Ads, Meta Ads, HubSpot/Salesforce, GA4/Segment, LinkedIn Ads), janela de tempo da coleta e lista de events de interesse (lead, MQL, SQL, opportunity, closed-won)

## Output

- Tabela normalizada de touchpoints (JSON/Parquet) no formato canônico com schema versionado, log de qualidade de ingestão (% de registros com UTM completo, fontes ativas/inativas, volume por fonte vs baseline) e alertas de desvio de volume (>20% vs média móvel 7d)

## Trigger

Schedule horário automático para dados de ads e conversões; schedule diário para sync completo de CRM (oportunidades, fechamentos, valores); webhook imediato quando GA4/Segment emite evento de conversão de alto valor (>R$X configurável); alerta manual de Atlas quando suspeita de anomalia de dados.

## Knowledge base (o que o executor consulta)

- Schema canônico de eventos do squad, mapeamento de UTM parameters por plataforma, dicionário de IDs de campanhas ativas, SLAs de latência por fonte, lista de eventos de conversão válidos por etapa do funil, histórico de volumes diários por fonte (90d) para baseline de anomalia

## Action Items

1. Confirmar o gatilho e carregar a entrada (Credenciais de API configuradas (Google Ads, Meta Ads, HubSpot/Salesforce, GA4/Segment, LinkedIn Ads), janela de tempo…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tabela normalizada de touchpoints (JSON/Parquet) no formato canônico com schema versionado, log de qualidade de ingestã…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tabela normalizada de touchpoints (JSON/Parquet) no formato canônico com schema versionado, log de qualidade de ingestão (% de registros com UTM completo, font…
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

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
