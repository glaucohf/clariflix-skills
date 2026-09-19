---
task: argusVerificar()
responsavel: "Argus"
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
    - "[ ] HITL: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo."
    - "[ ] HITL: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial."
    - "[ ] HITL: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual."
    - "[ ] HITL: Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo."
    - "[ ] HITL: Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach."
---

# Verificar Saídas do AI SDR Outbound Signal-Based

**Task ID:** `argusVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do AI SDR Outbound Signal-Based |
| **status** | `pending` |
| **responsible_executor** | Argus (Argus — Verificador de Mensagens e Compliance) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Argus — Verificador de Mensagens e Compliance — Valida cada draft gerado pelo Penna ANTES de qualquer envio. Checklist de 8 pontos: (1) Personalizacao real — a mensagem usa pelo menos 2 elementos especificos do dossie do Sherlock (nao frases genericas)? (2) Factualidade — todas as afirmacoes sobre a empresa/lead sao verificaveis no dossie? (3) Tom adequado ao canal e cargo? (4) CTA claro e unico? (5) Compliance LGPD — tem mecanismo de opt-out, nao promete resultados garantidos, nao usa dados sensiveis? (6) Ausencia de red flags — sem pressao excessiva, sem promessas comerciais nao autorizadas, sem desconto nao aprovado? (7) Comprimento adequado ao canal (email: max 150 palavras no cold; WhatsApp: max 3 blocos curtos)? (8) Subject line tem menos de 50 caracteres e nao parece spam? Veredicto: APROVADO / REESCREVER (com instrucoes especificas) / BLOQUEAR_HITL (para casos que exigem revisao humana). Maximo 2 ciclos de reescritura automatica antes de escalar.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Verificador de Mensagens e Compliance
- Valida cada draft gerado pelo Penna ANTES de qualquer envio
- Checklist de 8 pontos: (1) Personalizacao real
- a mensagem usa pelo menos 2 elementos especificos do dossie do Sherlock (nao frases genericas)? (2) Factualidade
- todas as afirmacoes sobre a empresa/lead sao verificaveis no dossie? (3) Tom adequado ao canal e cargo? (4) CTA claro e unico? (5) Compliance LGPD
- tem mecanismo de opt-out, nao promete resultados garantidos, nao usa dados sensiveis? (6) Ausencia de red flags
- sem pressao excessiva, sem promessas comerciais nao autorizadas, sem desconto nao aprovado? (7) Comprimento adequado ao canal (email: max 150 palavras no cold
- WhatsApp: max 3 blocos curtos)? (8) Subject line tem menos de 50 caracteres e nao parece spam? Veredicto: APROVADO / REESCREVER (com instrucoes especificas) / BLOQUEAR_HITL (para casos que exigem revisao humana)
- Maximo 2 ciclos de reescritura automatica antes de escalar

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Nexus para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossi…
- [ ] Gate HITL respeitado: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do…
- [ ] Gate HITL respeitado: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação ant… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Unsubscribe ou resposta negativa agressiva: processado pelo Lumen, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
