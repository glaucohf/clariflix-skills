---
task: guardiaoDoCrm()
responsavel: "Guardião do CRM"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Snapshot periódico do CRM (HubSpot export via MCP)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Regras de qualidade de dados definidas no onboarding (campos obrigatórios, formatos válidos, SLAs por stage)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Log de atividades dos outros workers"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio de saude do CRM: n"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "de duplicatas fundidas, campos preenchidos, deals re-ativados, alertas de SLA violado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dados corrigidos escritos de volta no HubSpot"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato: crm_health_report_YYYYMMDD.json salvo no ClickUp com link no canal do gestor"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron: executa toda segunda-feira 07h00 para relatório semanal. Também disparado em tempo real quando Orchestrator detecta anomalia (ex: mesmo lead criado duas vezes por fontes diferentes)."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Censor Comercial antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comercial aprova batch antes do disparo."
    - "[ ] HITL: HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por desconto, Vera responde 'vou verificar com nosso especialista' e escala ao closer via notificação imediata."
    - "[ ] HITL: HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes de qualquer ação automática adicional. Closer decide se assume a conversa ou deixa o squad continuar."
    - "[ ] HITL: HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada."
    - "[ ] HITL: HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor responde o que fazer; resposta é adicionada ao playbook para aprendizado."
---

# Auditar Saúde Do Pipeline

**Task ID:** `guardiaoDoCrm()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Auditar Saúde Do Pipeline |
| **status** | `pending` |
| **responsible_executor** | Guardião do CRM (Guardião do CRM — Clio) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de Higiene e Enriquecimento de CRM (RevOps). Roda em background auditando a saúde do pipeline: detecta duplicatas, campos críticos vazios, deals sem atividade há mais de X dias, contatos sem telefone válido, stages inconsistentes. Executa deduplicação automática, dispara requalificação de leads estagnados e gera relatório semanal de saúde do funil para o gestor comercial.

## Input

- Snapshot periódico do CRM (HubSpot export via MCP)
- Regras de qualidade de dados definidas no onboarding (campos obrigatórios, formatos válidos, SLAs por stage)
- Log de atividades dos outros workers

## Output

- Relatorio de saude do CRM: n
- de duplicatas fundidas, campos preenchidos, deals re-ativados, alertas de SLA violado
- Dados corrigidos escritos de volta no HubSpot
- Artefato: crm_health_report_YYYYMMDD.json salvo no ClickUp com link no canal do gestor

## Trigger

Cron: executa toda segunda-feira 07h00 para relatório semanal. Também disparado em tempo real quando Orchestrator detecta anomalia (ex: mesmo lead criado duas vezes por fontes diferentes).

## Knowledge base (o que o executor consulta)

- Schema de campos obrigatorios do CRM do cliente
- Regras de deduplicacao (match por telefone, email, CNPJ)
- SLAs por stage (ex: lead em 'New' por mais de 2h sem contato = alerta)
- Formato valido de telefone brasileiro (E.164 +55)
- Regras de merge de duplicatas (qual registro prevalece)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Snapshot periódico do CRM (HubSpot export via MCP)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio de saude do CRM: n) e persistir no artefato do squad.
4. Entregar ao critic Censor Comercial; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio de saude do CRM: n
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Censor Comercial registrado
- [ ] Gate HITL respeitado: HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputaci…
- [ ] Gate HITL respeitado: HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se l…
- [ ] Gate HITL respeitado: HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comerci… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por des… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada. | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor res… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL-6 (L1): Relatório semanal do Eco com sugestões de ajuste de prompt — gestor revisa e aprova antes de qualquer alteração ser aplicada nos prompts da Vera o… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Censor Comercial | BLOQUEIA entrega |

## Handoff

- **to:** Analista de Conversas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
