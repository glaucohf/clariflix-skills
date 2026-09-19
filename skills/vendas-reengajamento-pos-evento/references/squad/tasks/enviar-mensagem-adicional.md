---
task: engajamentoMedio()
responsavel: "Engajamento Médio"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de contatos Scóre B com dossiê de enriquecimento + metadados de engajamento (replay assistido, material baixado, páginas visitadas no site pós-evento)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Templates de abordagem Scóre B calibrados no setup"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens enviadas com confirmação de entrega e registro no CRM"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "leads responsivos passados ao Argos para qualificação"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "leads sem resposta após cadência B passados ao Worker de Nurture Pos-Evento para sequência de longo prazo"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Cadência Score B"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "{nome do evento}' com totalizadores de envio, abertura e resposta"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lista Score B recebida do Recon. SLA: primeiro envio em ate 6h pos-recebimento da lista. Re-acionado quando lead Score B abre email repetidamente sem responder (sinal de interesse latente — escala pa…"
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

# Enviar Mensagem Adicional

**Task ID:** `engajamentoMedio()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagem Adicional |
| **status** | `pending` |
| **responsible_executor** | Engajamento Médio (Nova — Worker de Outreach Score B (Engajamento Médio)) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia o outreach para contatos Score B — participantes que demonstraram interesse mas sem sinal de alta intenção (assistiu replay, baixou material, ficou 40-79% do webinar, passou pelo estande brevemente). Redige mensagens que entregam valor adicional ligado ao tópico do evento (insight extra, estudo de caso relevante, ferramenta gratuita) antes de fazer o pitch de reunião. Cadencia Score B: contato 1 (email com valor agregado, 6h pós-evento) -> contato 2 (WhatsApp educativo, 48h) -> contato 3 (email com CTA de reunião, 96h) -> entra em nurture de longo prazo se sem resposta.

## Input

- Lista de contatos Scóre B com dossiê de enriquecimento + metadados de engajamento (replay assistido, material baixado, páginas visitadas no site pós-evento)
- Templates de abordagem Scóre B calibrados no setup

## Output

- Mensagens enviadas com confirmação de entrega e registro no CRM
- leads responsivos passados ao Argos para qualificação
- leads sem resposta após cadência B passados ao Worker de Nurture Pos-Evento para sequência de longo prazo
- Artefato ClickUp: task 'Cadência Score B
- {nome do evento}' com totalizadores de envio, abertura e resposta

## Trigger

Lista Score B recebida do Recon. SLA: primeiro envio em ate 6h pos-recebimento da lista. Re-acionado quando lead Score B abre email repetidamente sem responder (sinal de interesse latente — escala para Score A approach).

## Knowledge base (o que o executor consulta)

- Templates de abordagem Score B por tipo de evento com hooks de valor (conteúdo extra ligado ao tópico, caso de uso relevante para o setor do contato, ferramenta ou checklist gratuito)
- regras de upgrade de Score B para Score A baseado em comportamento pós-envio (abriu 3x? visitou página de preço?)
- biblioteca de conteúdos de valor por tópico de evento
- política de desistência Score B (máximo de tentativas antes de entrada em nurture)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de contatos Scóre B com dossiê de enriquecimento + metadados de engajamento (replay assistido, material baixado,…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens enviadas com confirmação de entrega e registro no CRM) e persistir no artefato do squad.
4. Entregar ao critic Vigilia; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens enviadas com confirmação de entrega e registro no CRM
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

- **to:** Argos Evento
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
