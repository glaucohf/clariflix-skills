---
task: sherlock()
responsavel: "Sherlock"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Alerta de sinal do Radar (lead_id, company, signal_type)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Acesso a APIs de enriquecimento (Clay, Apollo, Clearbit, LinkedIn)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Domínio da empresa e nomes dos decisores (quando disponíveis no CRM)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê de conta em Markdown estruturado: seções de Contexto da Empresa, Decisores Identificados (nome/cargo/LinkedIn/email verificado), Stack Tecnológica, Notícias Recentes (max 3 relevantes), Dores Inferidas do Sinal, Ângulos de Personalização Sugeridos (3 opções ranqueadas), Score de Confiança do Dossiê (0-100)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato salvo no ClickUp e linkado ao lead no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Nexus imediatamente após validação do sinal pelo Radar. Reativado se o sinal for atualizado (ex: nova notícia sobre a empresa emerge 24h depois)."
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

# Construir Dossiê Completo

**Task ID:** `sherlock()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Construir Dossiê Completo |
| **status** | `pending` |
| **responsible_executor** | Sherlock (Sherlock — Pesquisador de Conta) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Dado um lead/conta ativado pelo Radar, constroi um dossiê completo e verificado: contexto da empresa, decisores identificados, stack tecnológica atual, notícias recentes relevantes, possíveis dores inferidas do sinal detectado, conexões em comum e ângulos de personalização para o outreach. Entrega o contexto que faz a mensagem soar como se o SDR tivesse pesquisado 2 horas.

## Input

- Alerta de sinal do Radar (lead_id, company, signal_type)
- Acesso a APIs de enriquecimento (Clay, Apollo, Clearbit, LinkedIn)
- Domínio da empresa e nomes dos decisores (quando disponíveis no CRM)

## Output

- Dossiê de conta em Markdown estruturado: seções de Contexto da Empresa, Decisores Identificados (nome/cargo/LinkedIn/email verificado), Stack Tecnológica, Notícias Recentes (max 3 relevantes), Dores Inferidas do Sinal, Ângulos de Personalização Sugeridos (3 opções ranqueadas), Score de Confiança do Dossiê (0-100)
- Artefato salvo no ClickUp e linkado ao lead no CRM

## Trigger

Ativado pelo Nexus imediatamente após validação do sinal pelo Radar. Reativado se o sinal for atualizado (ex: nova notícia sobre a empresa emerge 24h depois).

## Knowledge base (o que o executor consulta)

- Templates de dossie por vertical (agencia, imobiliaria, SaaS, servicos)
- Playbook de angulos de personalizacao por tipo de sinal (ex: mudanca de lideranca -> desafio de onboarding
- expansao de headcount -> escalabilidade de processos)
- Mapeamento de tecnologias concorrentes e posicionamento de diferenciacoes
- Historico de dossies de contas similares que converteram

## Action Items

1. Confirmar o gatilho e carregar a entrada (Alerta de sinal do Radar (lead_id, company, signal_type)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossiê de conta em Markdown estruturado: seções de Contexto da Empresa, Decisores Identificados (nome/cargo/LinkedIn/em…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossiê de conta em Markdown estruturado: seções de Contexto da Empresa, Decisores Identificados (nome/cargo/LinkedIn/email verificado), Stack Tecnológica, Notí…
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

- **to:** Magnus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
