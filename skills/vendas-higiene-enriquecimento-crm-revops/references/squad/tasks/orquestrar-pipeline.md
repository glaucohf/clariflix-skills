---
task: nexusPipeline()
responsavel: "Nexus"
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
    descricao: "Golden Record Dashboard: relatório semanal exportado para ClickUp e enviado ao operador RevOps com: score agregado da base (Gold/Silver/Bronze distribution), top 20 registros Bronze com deal aberto (prioritários para ação manual), log de merges da semana (quantidade, campos afetados, revertidos), custo de enriquecimento consumido vs budget, alertas de Cassandra pendentes de ação, e gráficos de tendência de qualidade ao longo do tempo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Cada ciclo de processamento gera um artefato imutável de auditoria no ClickUp com hash de integridade"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe triggers de entrada de novos registros, mudanças de estágio ou varreduras agendadas. Decompõe em subtarefas (validar, deduplicar, enriquecer, sincronizar), roteia para workers especializados,…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)"
    - "[ ] HITL: Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)"
    - "[ ] HITL: Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)"
    - "[ ] HITL: Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal)"
    - "[ ] HITL: Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente)"
---

# Orquestrar Pipeline do Higiene e Enriquecimento de CRM

**Task ID:** `nexusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Higiene e Enriquecimento de CRM |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus (Orquestrador de Integridade de Dados)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe triggers de entrada de novos registros, mudanças de estágio ou varreduras agendadas. Decompõe em subtarefas (validar, deduplicar, enriquecer, sincronizar), roteia para workers especializados, consolida resultados em golden record, registra prova de trabalho no ClickUp e emite alertas de qualidade. Mantém estado do pipeline no LangGraph e define ordem de execução por dependência (validação antes de enriquecimento, deduplicação antes de merge).

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Golden Record Dashboard: relatório semanal exportado para ClickUp e enviado ao operador RevOps com: score agregado da base (Gold/Silver/Bronze distribution), top 20 registros Bronze com deal aberto (prioritários para ação manual), log de merges da semana (quantidade, campos afetados, revertidos), custo de enriquecimento consumido vs budget, alertas de Cassandra pendentes de ação, e gráficos de tendência de qualidade ao longo do tempo
- Cada ciclo de processamento gera um artefato imutável de auditoria no ClickUp com hash de integridade

## Trigger

Recebe triggers de entrada de novos registros, mudanças de estágio ou varreduras agendadas. Decompõe em subtarefas (validar, deduplicar, enriquecer, sincronizar), roteia para workers especializados, consolida resultados em golden record, registra prova de trabalho no ClickUp e emite alertas de qualidade. Mantém estado do pipeline no LangGraph e define ordem de execução por dependência (validação antes de enriquecimento, deduplicação antes de merge).

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce
- source of truth de contatos e companies
- Enriquecimento: Apollo.io (275M+ contatos B2B), Clay (waterfall multi-source), Clearbit (dados de empresa)
- Email validation: ZeroBounce ou NeverBounce (verificação de MX record e caixa ativa)
- WhatsApp Business API: sync de numero validado e opt-in status
- Plataforma de email (ActiveCampaign / Mailchimp / RD Station): sync de contatos e status de bounce
- ClickUp: artefatos verificáveis por task, fila HITL, dashboard de qualidade de CRM
- Langfuse (OTEL): observabilidade de cada agente, quality gates dev 70% / staging 85% / prod 95%
- Slack: alertas de anomalia, fila HITL para aprovação de merges
- LangGraph: orquestração do pipeline com estado persistente entre etapas
- N8N (opcional): webhook receiver para fontes de entrada não-nativas (ex: formulário do site, planilha do SDR)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Sentinel antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Golden Record Dashboard: relatório semanal exportado para ClickUp e enviado ao operador RevOps com: score agregado da base (Gold/Silver/Bronze distribution), t…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)
- [ ] Gate HITL respeitado: Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)
- [ ] Gate HITL respeitado: Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez) | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de integração de nova fonte de dados ao pipeline (ex: adicionar novo formulário ou importação de lista de parceiro) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Validador de Entradas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
