---
task: sigma()
responsavel: "Sigma"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Rascunho de copy ou mensagem de Bolt/Nexus, Signal Evidence Trail da conta (quais sinais justificam a abordagem), histórico de abordagens anteriores na conta, checklist de conformidade LGPD/GDPR, guidelines de brand voice, threshold de frequência configurado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa específica, lista de ajustes necessários se NEEDS_REVISION (com sugestões concretas, não apenas críticas), flag de risco LGPD se o uso do sinal como contexto é problemático, Quality Score da abordagem (0-10 com breakdown: relevância do sinal, adequação do tom, personalização, timing)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: SEMPRE antes de qualquer envio de outreach externo (gate obrigatório — Nexus não envia sem aprovação de Sigma), antes de publicação de campanha paga (gate L3), antes de escalar abordagem de conta de…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sigma 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)"
    - "[ ] HITL: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)"
    - "[ ] HITL: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)"
    - "[ ] HITL: Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)"
    - "[ ] HITL: Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)"
---

# Verificar Conformidade E Qualidade

**Task ID:** `sigma()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Conformidade E Qualidade |
| **status** | `pending` |
| **responsible_executor** | Sigma (Sigma — Crític & Compliance Verifier) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gate de qualidade e conformidade antes de qualquer acao externa irreversivel. Valida: (1) Alinhamento com brand voice e tom (copy nao parece robotico ou generico demais), (2) Conformidade LGPD/GDPR para uso do sinal como contexto de abordagem (ex: mencionar que 'vimos que voce esta contratando X' pode ser invasivo em alguns contextos), (3) Threshold de frequencia por conta (nao abordar a mesma conta mais de X vezes em Y dias), (4) Consistencia do sinal como contexto (o angulo usado no copy realmente faz sentido para o sinal detectado), (5) Quality check do playbook selecionado versus os dados disponiveis (Nexus escolheu o playbook certo?). Implementa padrao Skeptic Protocol para o squad.

## Input

- Rascunho de copy ou mensagem de Bolt/Nexus, Signal Evidence Trail da conta (quais sinais justificam a abordagem), histórico de abordagens anteriores na conta, checklist de conformidade LGPD/GDPR, guidelines de brand voice, threshold de frequência configurado

## Output

- Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa específica, lista de ajustes necessários se NEEDS_REVISION (com sugestões concretas, não apenas críticas), flag de risco LGPD se o uso do sinal como contexto é problemático, Quality Score da abordagem (0-10 com breakdown: relevância do sinal, adequação do tom, personalização, timing)

## Trigger

SEMPRE antes de qualquer envio de outreach externo (gate obrigatório — Nexus não envia sem aprovação de Sigma), antes de publicação de campanha paga (gate L3), antes de escalar abordagem de conta de Warm para ação de tier 1, quando Bolt entrega copy para revisão

## Knowledge base (o que o executor consulta)

- Checklist de conformidade LGPD/GDPR para uso de dados de intent em outreach B2B, guidelines completos de brand voice e tom, historico de abordagens anteriores por conta com resultado (para aprender o que funcionou), regras de frequencia e espacamento por canal, biblioteca de exemplos de abordagem aprovados versus rejeitados como referencia

## Action Items

1. Confirmar o gatilho e carregar a entrada (Rascunho de copy ou mensagem de Bolt/Nexus, Signal Evidence Trail da conta (quais sinais justificam a abordagem), histó…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa específica, lista de ajustes necessários se NEEDS_REVISION…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa específica, lista de ajustes necessários se NEEDS_REVISION (com sugestões concretas, não apenas crí…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sigma 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o…
- [ ] Gate HITL respeitado: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cad…
- [ ] Gate HITL respeitado: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squ… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprova… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3) | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Sigma 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
