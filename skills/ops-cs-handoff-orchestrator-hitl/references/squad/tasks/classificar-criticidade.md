---
task: cassio()
responsavel: "Cassio"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Descrição da ação pendente + metadata (canal, valor monetário se aplicável, histórico do cliente, tipo de contrato, tier do cliente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON estruturado: {action_id, criticality_score, reversibility_class, autonomy_tier, risk_flags[], justification, confidence_pct, requires_human_review: bool}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda e qualquer acao solicitada por qualquer agente do ecossistema antes de ser executada. Tambem dispara quando Hieronimus detecta acao de alto risco em fila de tickets."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vitor antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de qualquer execução, sem exceção."
    - "[ ] HITL: L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cláusula contratual, bloqueio/banimento de usuário."
    - "[ ] HITL: L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que mencione termos legais ou rescisão."
    - "[ ] HITL: L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, respostas à imprensa."
    - "[ ] HITL: Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operações."
---

# Classificar Criticidade

**Task ID:** `cassio()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Handoff Orchestrator HITL

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Criticidade |
| **status** | `pending` |
| **responsible_executor** | Cassio (Cássio — Classificador de Criticidade) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em taxonomia de ações. Recebe a descrição de qualquer ação pendente e retorna: (1) score de criticidade 1-10 com justificativa, (2) classificação de reversibilidade (R/PR/IR), (3) tier de autonomia recomendado (L0/L1/L2/L3), (4) flags de risco ativo (financeiro, legal, reputacional, dados-sensiveis). Usa regras deterministicas para ações conhecidas (reembolso acima de X = sempre L3) e LLM para ações novas ou ambíguas.

## Input

- Descrição da ação pendente + metadata (canal, valor monetário se aplicável, histórico do cliente, tipo de contrato, tier do cliente)

## Output

- JSON estruturado: {action_id, criticality_score, reversibility_class, autonomy_tier, risk_flags[], justification, confidence_pct, requires_human_review: bool}

## Trigger

Toda e qualquer acao solicitada por qualquer agente do ecossistema antes de ser executada. Tambem dispara quando Hieronimus detecta acao de alto risco em fila de tickets.

## Knowledge base (o que o executor consulta)

- Matriz de classificação calibrada (produto do Deep Dive), políticas de reembolso e cancelamento do cliente, limites financeiros por perfil de agente, histórico de classificações anteriores com feedback humano, taxonomia de ações por pilar (Suporte/Entrega/Retenção/Dados)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Descrição da ação pendente + metadata (canal, valor monetário se aplicável, histórico do cliente, tipo de contrato, tie…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON estruturado: {action_id, criticality_score, reversibility_class, autonomy_tier, risk_flags[], justification, confi…) e persistir no artefato do squad.
4. Entregar ao critic Vitor; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON estruturado: {action_id, criticality_score, reversibility_class, autonomy_tier, risk_flags[], justification, confidence_pct, requires_human_review: bool}
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vitor registrado
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — hum…
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assin…
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qual…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cl… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, r… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operaçõe… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão humana quinzenal do Relatório de Auditoria do Vitor: supervisor CS assina o score de qualidade e valida as correções propostas. | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Gate humano na primeira semana pos-implantacao: humano revisa 100% das classificacoes (nao apenas L3) para construir confianca na matriz antes de operar em mod… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Vitor | BLOQUEIA entrega |

## Handoff

- **to:** Beatriz
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
