---
task: maestroPipeline()
responsavel: "Maestro"
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
    descricao: "Plano de projeto estruturado publicado no ClickUp (com fases, marcos, tasks, owners e critérios de aceite) + Delivery Status Report semanal com semáforo RAG + Health Score Report dos primeiros 90 dias + Log de alertas e ações tomadas"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Prova de trabalho: dashboard de delivery público para o cliente com % de conclusão em tempo real e histórico de status por marco"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do squad. Recebe o gatilho de novo cliente (SOW uploadado ou deal fechado no CRM), gerencia o pipeline completo de Discovery > Deep Dive > Framework, delega tarefas para os agent…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)"
    - "[ ] HITL: Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)"
    - "[ ] HITL: Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro"
    - "[ ] HITL: Aprovação do Delivery Status Report semanal antes do envio ao cliente"
    - "[ ] HITL: Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente"
---

# Orquestrar Pipeline do Onboarding & Implementação

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Onboarding & Implementação |
| **status** | `pending` |
| **responsible_executor** | Maestro (Maestro — Orquestrador PSA) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do squad. Recebe o gatilho de novo cliente (SOW uploadado ou deal fechado no CRM), gerencia o pipeline completo de Discovery > Deep Dive > Framework, delega tarefas para os agentes workers, consolida outputs, decide escalações para HITL e emite o Delivery Status Report semanal. Opera como gerente de projeto sênior que nunca dorme.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Plano de projeto estruturado publicado no ClickUp (com fases, marcos, tasks, owners e critérios de aceite) + Delivery Status Report semanal com semáforo RAG + Health Score Report dos primeiros 90 dias + Log de alertas e ações tomadas
- Prova de trabalho: dashboard de delivery público para o cliente com % de conclusão em tempo real e histórico de status por marco

## Trigger

Orquestrador central do squad. Recebe o gatilho de novo cliente (SOW uploadado ou deal fechado no CRM), gerencia o pipeline completo de Discovery > Deep Dive > Framework, delega tarefas para os agentes workers, consolida outputs, decide escalações para HITL e emite o Delivery Status Report semanal. Opera como gerente de projeto sênior que nunca dorme.

## Knowledge base (o que o executor consulta)

- ClickUp (MCP nativo)
- hub de tasks, marcos, status e prova de trabalho
- espelha estrutura AIOX
- CRM (HubSpot ou Salesforce via MCP)
- webhook de deal closed-won para trigger de onboarding
- dados de conta e contatos
- WhatsApp Business API
- notificações proativas e follow-ups de pendências do cliente
- alertas internos, notificações de risco, aprovações HITL via workflow de aprovação
- Google Drive / Notion
- ingestão de SOW e documentos de kickoff via connector ou URL
- Calendário (Google Calendar / Outlook via MCP)
- leitura de calls agendadas para trigger de relatório pré-reunião
- Produto SaaS do cliente (API de uso)
- dados de engajamento e ativação para health score
- Supabase / Postgres
- estado dos agentes, histórico de onboardings, health scores, risk matrix
- observabilidade OTEL, tracing de chamadas, quality gates (dev 70% / staging 85% / prod 95%)
- Email (SMTP/SendGrid)
- envio de relatórios de delivery e notificações formais
- Rocketlane (referência de arquitetura PSA)
- benchmark de fluxo de onboarding e estrutura de portal do cliente

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argus antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Plano de projeto estruturado publicado no ClickUp (com fases, marcos, tasks, owners e critérios de aceite) + Delivery Status Report semanal com semáforo RAG +…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)
- [ ] Gate HITL respeitado: Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)
- [ ] Gate HITL respeitado: Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação do Delivery Status Report semanal antes do envio ao cliente | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Decisão de go/no-go para go-live quando health score < 60 ou mais de 2 marcos críticos em Red | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Átlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
