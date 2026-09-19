---
task: penna()
responsavel: "Penna"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê de conta completo (Sherlock)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Score e prioridade (Magnus)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Playbook de mensagens por vertical/sinal/cargo"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Canal de envio determinado pelo Nexus"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Instruções de tom da empresa (voz da marca configurada no onboarding)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pack de outreach: 2 variações de mensagem por canal ativo, com subject line (email), preview text, corpo, CTA e P.S"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "quando aplicável"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Cada draft inclui metadados: personalização_score (quantos elementos do dossiê foram usados), compliance_flags (campos a verificar), estimated_read_time"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Formato JSON + Markdown para o Critic consumir"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Nexus após Magnus classificar o lead como HOT ou WARM e o dossiê estar completo. Re-trigger se o Critic reprovar o draft (max 2 reescrituras automáticas antes de escalar para HITL)."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo."
    - "[ ] HITL: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial."
    - "[ ] HITL: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual."
    - "[ ] HITL: Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo."
    - "[ ] HITL: Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach."
---

# Redigir Mensagens Personalizadas

**Task ID:** `penna()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Redigir Mensagens Personalizadas |
| **status** | `pending` |
| **responsible_executor** | Penna (Penna — Copywriter de Outreach Multicanal) |
| **execution_type** | `Agent` |
| **input** | 5 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Redige os drafts de mensagem personalizados para cada canal (email, LinkedIn InMail, WhatsApp, script de voz) usando o dossiê do Sherlock e o ângulo de personalização mais forte. Gera 2 variações de cada mensagem (A/B) para teste. Adapta tom, comprimento e call-to-action ao canal e ao cargo do decisor. Nunca envia — entrega ao Critic para validação.

## Input

- Dossiê de conta completo (Sherlock)
- Score e prioridade (Magnus)
- Playbook de mensagens por vertical/sinal/cargo
- Canal de envio determinado pelo Nexus
- Instruções de tom da empresa (voz da marca configurada no onboarding)

## Output

- Pack de outreach: 2 variações de mensagem por canal ativo, com subject line (email), preview text, corpo, CTA e P.S
- quando aplicável
- Cada draft inclui metadados: personalização_score (quantos elementos do dossiê foram usados), compliance_flags (campos a verificar), estimated_read_time
- Formato JSON + Markdown para o Critic consumir

## Trigger

Ativado pelo Nexus após Magnus classificar o lead como HOT ou WARM e o dossiê estar completo. Re-trigger se o Critic reprovar o draft (max 2 reescrituras automáticas antes de escalar para HITL).

## Knowledge base (o que o executor consulta)

- Biblioteca de playbooks de mensagem por vertical (agência digital, imobiliária, SaaS, serviços profissionais, indústria)
- Templates por tipo de sinal (job posting, mudança de liderança, expansão, engajamento com conteúdo)
- Guia de voz da marca do cliente (tom, vocabulário permitido/proibido, nível de formalidade)
- Exemplos de mensagens que geraram resposta (biblioteca de vencedores por segmento)
- Regras de compliance LGPD para comunicação comercial no Brasil

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossiê de conta completo (Sherlock)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pack de outreach: 2 variações de mensagem por canal ativo, com subject line (email), preview text, corpo, CTA e P.S) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pack de outreach: 2 variações de mensagem por canal ativo, com subject line (email), preview text, corpo, CTA e P.S
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
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

- **to:** Vox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
