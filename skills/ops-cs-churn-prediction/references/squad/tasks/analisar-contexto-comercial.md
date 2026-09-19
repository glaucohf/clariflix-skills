---
task: lumen()
responsavel: "Lumen"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados completos da conta do CRM (Account, Opportunity, Contract, Activity history, NPS history) + histórico de interações do CSM + dados públicos de mudanças na empresa (news alerts via API ou feed configurado) + pipeline de expansão/renovação da conta"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Perfil de churn provável da conta (DESVALOR / PROBLEMA_NÃO_RESOLVIDO / BUDGET_CUT / SUBSTITUIÇÃO / INATIVIDADE) com confiança percentual, contexto comercial resumido em 5 bullets, executive sponsor status (ativo/inativo/mudou), flags de risco comercial (renovação contested, desconto máximo já aplicado, decision maker novo sem relacionamento)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Entregue como contexto adicional para o Mira na geração do brief"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orchestrator Nexus para toda conta classificada como CRÍTICO ou ALTO risco antes da geração do brief pelo Mira; acionado sob demanda quando CSM solicita contexto expandido via ClickUp"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica"
    - "[ ] HITL: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato"
    - "[ ] HITL: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados"
    - "[ ] HITL: Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch"
    - "[ ] HITL: Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar"
---

# Analisar Contexto Comercial

**Task ID:** `lumen()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Contexto Comercial |
| **status** | `pending` |
| **responsible_executor** | Lumen (Lumen — Agente de Contexto Comercial e Expansão) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Enriquece a analise de churn com contexto comercial que nao aparece nos dados de produto. Para cada conta em risco, cruza: (1) Historico de renovacoes (quantas renovacoes, houve negociacao de preco, desconto concedido); (2) Historico de expansao e contracao de MRR; (3) QBRs realizados (frequencia, ultima data, commitments pendentes do fornecedor); (4) Executive Sponsor ativo ou inativo; (5) Mudancas recentes na conta (novo decisor, M&A, reducao de headcount detectada via LinkedIn/noticias); (6) Pipeline de expansao existente ou bloqueado. Identifica o perfil de churn provavel: por desvalor percebido, por problema nao resolvido, por budget cut, ou por substituicao por concorrente — cada perfil tem um playbook de retencao diferente.

## Input

- Dados completos da conta do CRM (Account, Opportunity, Contract, Activity history, NPS history) + histórico de interações do CSM + dados públicos de mudanças na empresa (news alerts via API ou feed configurado) + pipeline de expansão/renovação da conta

## Output

- Perfil de churn provável da conta (DESVALOR / PROBLEMA_NÃO_RESOLVIDO / BUDGET_CUT / SUBSTITUIÇÃO / INATIVIDADE) com confiança percentual, contexto comercial resumido em 5 bullets, executive sponsor status (ativo/inativo/mudou), flags de risco comercial (renovação contested, desconto máximo já aplicado, decision maker novo sem relacionamento)
- Entregue como contexto adicional para o Mira na geração do brief

## Trigger

Acionado pelo Orchestrator Nexus para toda conta classificada como CRÍTICO ou ALTO risco antes da geração do brief pelo Mira; acionado sob demanda quando CSM solicita contexto expandido via ClickUp

## Knowledge base (o que o executor consulta)

- Dados de Account, Contract, Opportunity e Activity do CRM (HubSpot/Salesforce), histórico de QBRs e commitments (notas do CSM), histórico de negociações de preço e descontos aplicados, modelo de classificação de perfil de churn por comportamento histórico, dados de mudanças organizacionais (fontes públicas configuradas por setor), benchmark de taxa de retenção por perfil de churn e por ação tomada

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados completos da conta do CRM (Account, Opportunity, Contract, Activity history, NPS history) + histórico de interaçõ…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Perfil de churn provável da conta (DESVALOR / PROBLEMA_NÃO_RESOLVIDO / BUDGET_CUT / SUBSTITUIÇÃO / INATIVIDADE) com con…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Perfil de churn provável da conta (DESVALOR / PROBLEMA_NÃO_RESOLVIDO / BUDGET_CUT / SUBSTITUIÇÃO / INATIVIDADE) com confiança percentual, contexto comercial re…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cri…
- [ ] Gate HITL respeitado: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de…
- [ ] Gate HITL respeitado: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguarda… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualque… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analis… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo b… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de rela… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Echo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
