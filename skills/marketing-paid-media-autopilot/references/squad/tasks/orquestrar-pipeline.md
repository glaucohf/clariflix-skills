---
task: orionPipeline()
responsavel: "Orion"
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
    descricao: "Paid Media Autopilot Report"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "relatório consolidado diário (gerado automaticamente às 08h) contendo: (1) Performance snapshot D-1 (ROAS, CAC, pacing, CPL por campanha/canal), (2) Ações autônomas executadas no período (rotações de criativo, ajustes de bid/budget com antes/depois), (3) Ações pendentes de aprovação L3 (aguardando OK humano), (4) Score de saúde do banco de criativos (quantos ativos, quantos fatigados, quantos em produção), (5) Alertas de oportunidade da semana (sinais do Sentinel), (6) Projeção de performance para próximos 7 dias com recomendações proativas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Formato: PDF executivo + JSON estruturado para integração + ClickUp board com todas as tasks auditáveis"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central (Opus lead) que decompoe a meta de aquisicao do periodo em sub-tarefas, delega a workers especializados, consolida insights, toma decisoes de realocacao dentro das bandas L2 e es…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de ROAS para escala, orçamento máximo em risco por ciclo) — sem essa aprovação o squad não opera"
    - "[ ] HITL: Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget total ou pausar campanha inteira) requer aprovação explícita via Slack/WhatsApp antes de execução pelo Midas"
    - "[ ] HITL: Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos de mensagem sem histórico) requer aprovação humana — irreversível em termos de impressão inicial"
    - "[ ] HITL: Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de threshold) requerem OK do gestor antes de ativação automática"
    - "[ ] HITL: Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com os guardrails mais recentes aprovados"
---

# Orquestrar Pipeline do Paid Media Autopilot

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Paid Media Autopilot |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Orquestrador de Mídia Paga) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central (Opus lead) que decompoe a meta de aquisicao do periodo em sub-tarefas, delega a workers especializados, consolida insights, toma decisoes de realocacao dentro das bandas L2 e escalona para aprovacao humana (L3) quando thresholds financeiros sao atingidos. Mantém o estado do ciclo de otimizacao, aciona workers na sequencia correta e sintetiza o relatorio de performance consolidado.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Paid Media Autopilot Report
- relatório consolidado diário (gerado automaticamente às 08h) contendo: (1) Performance snapshot D-1 (ROAS, CAC, pacing, CPL por campanha/canal), (2) Ações autônomas executadas no período (rotações de criativo, ajustes de bid/budget com antes/depois), (3) Ações pendentes de aprovação L3 (aguardando OK humano), (4) Score de saúde do banco de criativos (quantos ativos, quantos fatigados, quantos em produção), (5) Alertas de oportunidade da semana (sinais do Sentinel), (6) Projeção de performance para próximos 7 dias com recomendações proativas
- Formato: PDF executivo + JSON estruturado para integração + ClickUp board com todas as tasks auditáveis

## Trigger

Orquestrador central (Opus lead) que decompoe a meta de aquisicao do periodo em sub-tarefas, delega a workers especializados, consolida insights, toma decisoes de realocacao dentro das bandas L2 e escalona para aprovacao humana (L3) quando thresholds financeiros sao atingidos. Mantém o estado do ciclo de otimizacao, aciona workers na sequencia correta e sintetiza o relatorio de performance consolidado.

## Knowledge base (o que o executor consulta)

- Google Ads API (MCP server)
- leitura de métricas e execução de ajustes de bid/budget/status de criativo
- Meta Marketing API (MCP server)
- leitura de métricas e execução de ações em campanhas Facebook/Instagram Ads
- HubSpot CRM (MCP server)
- closed-loop attribution (lead source, deal value, lifecycle stage por campanha de origem)
- ClickUp (MCP server)
- registro de toda ação executada como task/prova de trabalho auditável, gestão do backlog de criativos solicitados
- Slack (MCP server)
- canal de alertas em tempo real, gate de aprovação L3 (aprovação via reaction/botão no próprio canal)
- WhatsApp Business API
- canal alternativo de alertas urgentes e aprovação L3 para gestores fora do escritório
- Google Trends API
- monitoramento de sinais de demanda pelo Sentinél
- Meta Ads Library API
- monitoramento de criativos de concorrentes pelo Sentinel
- Google Search Console API
- dados de demanda organica como proxy de intent pelo Sentinel
- Langfuse (observabilidade OTEL)
- rastreamento de todas as execuções de agentes, quality gates (dev 70% / staging 85% / prod 95%), evals de performance do squad
- Google Sheets / Looker Studio
- dashboard de KPIs compartilhado com cliente (visualização de ROAS, CAC, pacing, score de criativo em tempo real)
- orquestração de automações complementares (webhooks de conversão offline, sincronização de dados entre plataformas, notificações customizadas)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Aegis 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Paid Media Autopilot Report
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis 2 registrado
- [ ] Gate HITL respeitado: Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA…
- [ ] Gate HITL respeitado: Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: move…
- [ ] Gate HITL respeitado: Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos forma…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget to… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de thresh… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com o… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Onboarding de nova plataforma ou canal: qualquer expansão para nova plataforma de mídia (ex: adicionar TikTok Ads, Pinterest Ads, CTV) requer aprovação e confi… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Bloqueio por anomalia crítica: se Argos detectar anomalia CRITICAL (ex: ROAS caiu > 50% em 1h ou spend disparou 300% acima do target), o squad pausa todas as a… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Aegis 2 | BLOQUEIA entrega |

## Handoff

- **to:** Argos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
