---
task: nexus()
responsavel: "Nexus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Hot Account com Signal Score > 70 (Pulse output), Context Card da conta (Vortex output), tipo de sinal dominante que ativou o status Hot, biblioteca de playbooks disponível, restrições de canal (opt-out, frequência máxima por conta, status atual no CRM)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Playbook selecionado com justificativa (por que este playbook para este sinal), rascunho de mensagem de abertura personalizada com o sinal como contexto (para aprovação de Sigma), sequência de toques planejada (canal + timing + mensagem por toque), task criada no ClickUp para o SDR/AE responsável pela conta, notificação no CRM com signal evidence trail para contexto do vendedor"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Radar confirma conta como Hot Account (score > 70 com pelo menos 2 categorias de sinal); Pulse detecta sinal urgente de categoria crítica (competitive review = janela de 72h); Radar solicita revisão…"
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

# Disparar Playbook Correto

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Disparar Playbook Correto |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Playbook Dispatcher Agent) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável por selecionar e disparar o playbook correto dado o tipo e a combinação de sinais detectados. Mantém biblioteca de playbooks por tipo de sinal: (1) Funding Playbook — sequência de outreach sobre expansão com uso do recurso captado, (2) Leadership Change Playbook — abordagem do novo executivo com contexto do problema que o antecessor não resolveu, (3) Competitive Review Playbook — conta pesquisando alternativa no G2/Capterra, janela de 72h para abordagem, (4) Demand Surge Playbook — pico de busca orgânica aciona campanha de retargeting + conteúdo educativo no LinkedIn, (5) Tech Adoption Playbook — conta adotou tecnologia complementar, abordagem com caso de integração. Personaliza a mensagem de abertura com o sinal específico como contexto. NUNCA envia sem aprovação de Sigma.

## Input

- Hot Account com Signal Score > 70 (Pulse output), Context Card da conta (Vortex output), tipo de sinal dominante que ativou o status Hot, biblioteca de playbooks disponível, restrições de canal (opt-out, frequência máxima por conta, status atual no CRM)

## Output

- Playbook selecionado com justificativa (por que este playbook para este sinal), rascunho de mensagem de abertura personalizada com o sinal como contexto (para aprovação de Sigma), sequência de toques planejada (canal + timing + mensagem por toque), task criada no ClickUp para o SDR/AE responsável pela conta, notificação no CRM com signal evidence trail para contexto do vendedor

## Trigger

Radar confirma conta como Hot Account (score > 70 com pelo menos 2 categorias de sinal); Pulse detecta sinal urgente de categoria crítica (competitive review = janela de 72h); Radar solicita revisão de playbook para conta reaquecida (era Hot, esfriou, voltou a aquecer)

## Knowledge base (o que o executor consulta)

- Biblioteca completa de playbooks por tipo de sinal (com exemplos de mensagens que converteram), histórico de abordagens anteriores por conta (para não repetir ângulo), CRM status da conta (já foi abordada? quando? qual resultado?), calendário de restrições por conta (opt-out, LGPD, frequência), cases de sucesso por tipo de sinal para referência na personalização

## Action Items

1. Confirmar o gatilho e carregar a entrada (Hot Account com Signal Score > 70 (Pulse output), Context Card da conta (Vortex output), tipo de sinal dominante que at…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Playbook selecionado com justificativa (por que este playbook para este sinal), rascunho de mensagem de abertura person…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Playbook selecionado com justificativa (por que este playbook para este sinal), rascunho de mensagem de abertura personalizada com o sinal como contexto (para…
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

- **to:** Sage
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
