---
task: iris()
responsavel: "Iris"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Arquivos de SOW (PDF/DOCX/URL), transcrições de calls de kickoff (texto ou áudio), emails de negociação, contrato assinado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "project-brief.json com campos normalizados: client_id, product_contracted, modules[], milestones[], owners{}, client_dependencies[], acceptance_criteria{}, go_live_date, special_conditions[], risk_flags[]"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "confiança por campo (low/medium/high) para guiar revisão HITL"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Upload de arquivo de SOW no canal designado; webhook de deal 'closed-won' no CRM; comando manual do CSM via Slack; transcrição de call de kickoff disponível no sistema"
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

# Processar Documentos SOW

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Processar Documentos SOW |
| **status** | `pending` |
| **responsible_executor** | Iris (Iris — Agente de Ingestão e Parsing de SOW) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em extração estruturada de informações de documentos não-estruturados de onboarding. Processa SOW (PDF, Notion, Google Docs, Word), contratos, notas de calls (transcrições) e emails de kickoff. Extrai e normaliza: escopo contratado, módulos/features incluídos, marcos e datas, responsáveis nomeados, dependências do cliente, critérios de aceite, restrições técnicas, SLAs e condições especiais. Produz o project-brief.json canônico que alimenta todo o pipeline.

## Input

- Arquivos de SOW (PDF/DOCX/URL), transcrições de calls de kickoff (texto ou áudio), emails de negociação, contrato assinado

## Output

- project-brief.json com campos normalizados: client_id, product_contracted, modules[], milestones[], owners{}, client_dependencies[], acceptance_criteria{}, go_live_date, special_conditions[], risk_flags[]
- confiança por campo (low/medium/high) para guiar revisão HITL

## Trigger

Upload de arquivo de SOW no canal designado; webhook de deal 'closed-won' no CRM; comando manual do CSM via Slack; transcrição de call de kickoff disponível no sistema

## Knowledge base (o que o executor consulta)

- Glossário de termos contratuais da empresa, mapeamento de módulos/features por produto, templates de SOW históricos para aprendizado de padrões, lista de dependências técnicas comuns por tipo de integração

## Action Items

1. Confirmar o gatilho e carregar a entrada (Arquivos de SOW (PDF/DOCX/URL), transcrições de calls de kickoff (texto ou áudio), emails de negociação, contrato assin…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (project-brief.json com campos normalizados: client_id, product_contracted, modules[], milestones[], owners{}, client_de…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: project-brief.json com campos normalizados: client_id, product_contracted, modules[], milestones[], owners{}, client_dependencies[], acceptance_criteria{}, go_…
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

- **to:** Vitor
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
