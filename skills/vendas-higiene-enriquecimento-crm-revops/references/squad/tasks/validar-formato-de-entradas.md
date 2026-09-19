---
task: validadorDeEntradas()
responsavel: "Validador de Entradas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Payload de novo contato ou empresa (JSON do webhook do CRM ou formulário)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mesmo payload com campos validados anotados: { field, value, valid: bool, confidence: 0-1, issue: string }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato gravado no ClickUp como 'Validação #ID'"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de novo contato/empresa criado no CRM; importação em batch via CSV; formulário de landing page convertido."
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

# Validar Formato De Entradas

**Task ID:** `validadorDeEntradas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validar Formato De Entradas |
| **status** | `pending` |
| **responsible_executor** | Validador de Entradas (Argos (Validador de Entradas)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Intercepta todo novo registro antes de persistir no CRM. Valida formato de email (regex + MX record check), formato de telefone (E.164 + DDD válido no Brasil), CNPJ/CPF (dígito verificador), URL de empresa (domínio ativo). Marca campos inválidos com flag e confidence score. Não bloqueia — apenas anota para enriquecimento posterior.

## Input

- Payload de novo contato ou empresa (JSON do webhook do CRM ou formulário)

## Output

- Mesmo payload com campos validados anotados: { field, value, valid: bool, confidence: 0-1, issue: string }
- Artefato gravado no ClickUp como 'Validação #ID'

## Trigger

Webhook de novo contato/empresa criado no CRM; importação em batch via CSV; formulário de landing page convertido.

## Knowledge base (o que o executor consulta)

- Regex patterns para BR (telefone, CNPJ, CEP, email)
- Lista de domínios de email temporário (blocklist)
- Tabela de DDDs válidos por estado
- Regras de formato por campo do CRM do cliente (schema do HubSpot/Pipedrive mapeado no onboarding)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Payload de novo contato ou empresa (JSON do webhook do CRM ou formulário)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mesmo payload com campos validados anotados: { field, value, valid: bool, confidence: 0-1, issue: string }) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mesmo payload com campos validados anotados: { field, value, valid: bool, confidence: 0-1, issue: string }
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

- **to:** Detector de Duplicatas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
