---
task: nemesisVerificar()
responsavel: "Nemesis"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] L3: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora da empresa"
    - "[ ] L3: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM"
    - "[ ] L2: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa"
    - "[ ] L2: Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle"
    - "[ ] L1: Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal"
---

# Verificar Saídas do Forecast de Pipeline e Risco de Deal

**Task ID:** `nemesisVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Forecast de Pipeline e Risco de Deal |
| **status** | `pending` |
| **responsible_executor** | Nemesis (Nemesis — Verificador de Alertas) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Nemesis — Verificador de Alertas — Critic/Verifier que intercepta TODOS os alertas antes do envio externo. Verifica: (1) o score de risco está matematicamente coerente com os dados do deal? (2) o alerta não é duplicado ou dentro da janela de silêncio? (3) o tom da mensagem é apropriado para o canal e stakeholder? (4) a ação recomendada é factível no contexto atual do deal? (5) o alerta pode criar constrangimento ou comprometer negociação em andamento? Bloqueia ou solicita revisão antes de qualquer notificação sair.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Verificador de Alertas
- Critic/Verifier que intercepta TODOS os alertas antes do envio externo
- Verifica: (1) o score de risco está matematicamente coerente com os dados do deal? (2) o alerta não é duplicado ou dentro da janela de silêncio? (3) o tom da mensagem é apropriado para o canal e stakeholder? (4) a ação recomendada é factível no contexto atual do deal? (5) o alerta pode criar constrangimento ou comprometer negociação em andamento? Bloqueia ou solicita revisão antes de qualquer notificação sair

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Cassandra para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate L3 respeitado: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem…
- [ ] Gate L3 respeitado: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM
- [ ] Gate L2 respeitado: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora d… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM | BLOQUEIA até decisão humana |
| VETO-003 | L2 — Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Nemesis | BLOQUEIA entrega |

## Handoff

- **to:** Cassandra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
