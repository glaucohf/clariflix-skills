---
task: cipher()
responsavel: "Cipher"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefato final aprovado pelo founder (board pack PDF, investor update email, IC memo)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Source Manifest do ciclo (output do Vera)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Lista de destinatários (board members, investidores)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Metadados do ciclo (tipo de comunicação, data, contexto)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Versão arquivada no data room com metadados completos"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Audit trail entry no ClickUp: versão enviada, quem aprovou, quando, destinatários"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Diff de ciclo (Notion page): métricas que mudaram, narrativa que mudou, novos riscos adicionados"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Notificação ao founder e Cassidy confirmando archival completo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Founder aprova artefato no HITL Gate (trigger imediato). Check mensal de integridade do data room. Solicitação de histórico por founder, board member ou due diligence de nova rodada."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Axiom antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção"
    - "[ ] HITL: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores"
    - "[ ] HITL: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%"
    - "[ ] HITL: Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)"
    - "[ ] HITL: Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final"
---

# Manter Data Room Atualizado

**Task ID:** `cipher()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Manter Data Room Atualizado |
| **status** | `pending` |
| **responsible_executor** | Cipher (Cipher — Data Room & Versioning Keeper) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mantém o data room da empresa atualizado e versionado. Ao final de cada ciclo, arquiva o board pack aprovado com metadados (versão, data de envio, lista de destinatários, Source Manifest do ciclo). Cria audit trail completo: qual versão foi enviada para quem, em que data, com quais dados. Gera diff entre ciclos (o que mudou em métricas e narrativa vs ciclo anterior). Responde a consultas históricas ('qual era o ARR que reportamos no Q3?').

## Input

- Artefato final aprovado pelo founder (board pack PDF, investor update email, IC memo)
- Source Manifest do ciclo (output do Vera)
- Lista de destinatários (board members, investidores)
- Metadados do ciclo (tipo de comunicação, data, contexto)

## Output

- Versão arquivada no data room com metadados completos
- Audit trail entry no ClickUp: versão enviada, quem aprovou, quando, destinatários
- Diff de ciclo (Notion page): métricas que mudaram, narrativa que mudou, novos riscos adicionados
- Notificação ao founder e Cassidy confirmando archival completo

## Trigger

Founder aprova artefato no HITL Gate (trigger imediato). Check mensal de integridade do data room. Solicitação de histórico por founder, board member ou due diligence de nova rodada.

## Knowledge base (o que o executor consulta)

- Data room estruturado (Notion database ou Google Drive com estrutura padronizada)
- Histórico de board packs e investor updates arquivados por ciclo
- Audit log de versões
- Cap table e documentos de rodada anteriores para referência

## Action Items

1. Confirmar o gatilho e carregar a entrada (Artefato final aprovado pelo founder (board pack PDF, investor update email, IC memo)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Versão arquivada no data room com metadados completos) e persistir no artefato do squad.
4. Entregar ao critic Axiom; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Versão arquivada no data room com metadados completos
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Axiom registrado
- [ ] Gate HITL respeitado: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- [ ] Gate HITL respeitado: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao b…
- [ ] Gate HITL respeitado: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90% | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa nã… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downr… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser r… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Axiom | BLOQUEIA entrega |

## Handoff

- **to:** Gate
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
