---
task: altaIntencao()
responsavel: "Alta Intenção"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de contatos Score A com dossiê de enriquecimento + metadados específicos de engajamento no evento (pergunta exata feita, tópico assistido, material baixado, tempo no estande)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Templates de abordagem Score A calibrados no setup"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Autorização do Orchestrator após validação do Critic Vigília"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens enviadas por canal (WhatsApp, email, LinkedIn) com confirmação de entrega"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "registro de cada interação no CRM com timestamp e canal"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "leads responsivos passados ao Argos para qualificação"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "leads sem resposta após cadência A passados ao Follow-up Persistente"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task por contato Score A com log de cadência completo e status (respondeu/agendou/sem resposta)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lista Score A recebida do Recon e processada. SLA: primeiro envio em até 2h pós-recebimento da lista. Acionado pelo Orchestrator Radar com confirmação de que o Critic Vigília aprovou os templates."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vigilia antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer aprovação do closer responsável antes do primeiro envio"
    - "[ ] HITL: Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento"
    - "[ ] HITL: Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática"
    - "[ ] HITL: Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana"
    - "[ ] HITL: Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação"
---

# Agendar Reuniao Demo

**Task ID:** `altaIntencao()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Agendar Reuniao Demo |
| **status** | `pending` |
| **responsible_executor** | Alta Intenção (Cypher — Worker de Outreach Score A (Alta Intencao)) |
| **execution_type** | `Hybrid` |
| **input** | 3 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável exclusivo pelos contatos Score A — participantes com alta intenção detectada (fez pergunta ao vivo, ficou 80%+ da sessão, solicitou demo, interagiu ativamente no chat, visitou o estande múltiplas vezes). Redige e envia mensagens hiperpersonalizadas que referenciam o momento específico do evento (a pergunta que o contato fez, o tópico da talk que ele assistiu, o produto que ele demonstrou interesse no estande). Objetivo: agendar reunião/demo em até 24h. Cadência Score A: contato 1 (WhatsApp, 2h pós-evento) -> contato 2 (email, 24h) -> contato 3 (LinkedIn DM, 48h) -> escala para Closer se sem resposta.

## Input

- Lista de contatos Score A com dossiê de enriquecimento + metadados específicos de engajamento no evento (pergunta exata feita, tópico assistido, material baixado, tempo no estande)
- Templates de abordagem Score A calibrados no setup
- Autorização do Orchestrator após validação do Critic Vigília

## Output

- Mensagens enviadas por canal (WhatsApp, email, LinkedIn) com confirmação de entrega
- registro de cada interação no CRM com timestamp e canal
- leads responsivos passados ao Argos para qualificação
- leads sem resposta após cadência A passados ao Follow-up Persistente
- Artefato ClickUp: task por contato Score A com log de cadência completo e status (respondeu/agendou/sem resposta)

## Trigger

Lista Score A recebida do Recon e processada. SLA: primeiro envio em até 2h pós-recebimento da lista. Acionado pelo Orchestrator Radar com confirmação de que o Critic Vigília aprovou os templates.

## Knowledge base (o que o executor consulta)

- Templates de abordagem Score A por tipo de evento (webinar proprio, feira de setor, evento de parceiro) com hooks de personalizacao especificos ({{pergunta_feita}}, {{topico_assistido}}, {{material_baixado}})
- regras de espacamento de cadencia A
- limiares para escala direta ao closer sem qualificacao adicional (ex: lead Score A de empresa que ja esta em negociacao ativa no CRM)
- politica de opt-out imediato

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de contatos Score A com dossiê de enriquecimento + metadados específicos de engajamento no evento (pergunta exata…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens enviadas por canal (WhatsApp, email, LinkedIn) com confirmação de entrega) e persistir no artefato do squad.
4. Entregar ao critic Vigilia; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens enviadas por canal (WhatsApp, email, LinkedIn) com confirmação de entrega
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vigilia registrado
- [ ] Gate HITL respeitado: Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) —…
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento
- [ ] Gate HITL respeitado: Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Lead que solicita opt-out ou demonstra irritação com o contato — intervenção humana obrigatória, registro de opt-out e revisão da cadência | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Inconsistência crítica detectada entre dados do evento e CRM (ex: lead do evento e cliente com contrato ativo cancelado) — revisão humana antes de qualquer con… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Volume de lista acima de 1.000 contatos em evento único — revisão humana da segmentação antes do disparo em massa | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Vigilia | BLOQUEIA entrega |

## Handoff

- **to:** Engajamento Médio
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
