---
task: ecoEvento()
responsavel: "Eco Evento"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de leads Score C + leads Score B sem resposta após cadência inicial"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Configuração da sequência de nurture (cadência, conteúdos, CTA por etapa)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Sinais de comportamento do lead (email tracking, cliques)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Conteúdos de nurture enviados com registro de entrega e taxa de abertura/clique no CRM"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "leads reativados (sinal de comportamento detectado) passados de volta ao Argos Evento para qualificação"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "leads que solicitam descadastro imediatamente processados como opt-out"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Nurture Pos-Evento Ativo"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "{nome do evento}' com pipeline de leads por etapa da sequência e taxa de reativação"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Leads Score C recebidos do Recon (SLA: primeiro conteúdo em até 24h pós-evento). Leads Score B sem resposta após 96h da cadência Score B. Sinal de reativação detectado em lead inativo (abertura de em…"
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

# Gerenciar Leads Baixo Engajamento

**Task ID:** `ecoEvento()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerenciar Leads Baixo Engajamento |
| **status** | `pending` |
| **responsible_executor** | Eco Evento (Eco Evento — Worker de Nurture Pos-Evento de Longo Prazo) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerência os leads Score C (baixo engajamento, apenas se inscreveu) e os Score B que não responderam após a cadência inicial. Em vez de descartar esses contatos, executa uma sequência de nurture educativo de 4-8 semanas ancorada no tópico do evento: conteúdos progressivos, casos de uso, convites para próximos eventos, alertas de benchmark do setor. Detecta sinais de reativação (abertura de email, clique em link, nova interação) e re-roteia o lead para qualificação ativa. Opera em paralelo sem consumir atenção do time comercial.

## Input

- Lista de leads Score C + leads Score B sem resposta após cadência inicial
- Configuração da sequência de nurture (cadência, conteúdos, CTA por etapa)
- Sinais de comportamento do lead (email tracking, cliques)

## Output

- Conteúdos de nurture enviados com registro de entrega e taxa de abertura/clique no CRM
- leads reativados (sinal de comportamento detectado) passados de volta ao Argos Evento para qualificação
- leads que solicitam descadastro imediatamente processados como opt-out
- Artefato ClickUp: task 'Nurture Pos-Evento Ativo
- {nome do evento}' com pipeline de leads por etapa da sequência e taxa de reativação

## Trigger

Leads Score C recebidos do Recon (SLA: primeiro conteúdo em até 24h pós-evento). Leads Score B sem resposta após 96h da cadência Score B. Sinal de reativação detectado em lead inativo (abertura de email 3x em 7 dias, clique em link de preço, visita à página de produto).

## Knowledge base (o que o executor consulta)

- Biblioteca de conteúdos de nurture por tópico de evento e setor do lead (artigos, estudos de caso, ferramentas gratuitas, benchmarks de setor)
- regras de espaçamento de nurture (1x/semana máxima para não saturar)
- critérios de reativação (quais comportamentos indicam lead aquecido novamente)
- política de opt-out e LGPD
- templates de convite para próximos eventos do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de leads Score C + leads Score B sem resposta após cadência inicial).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Conteúdos de nurture enviados com registro de entrega e taxa de abertura/clique no CRM) e persistir no artefato do squad.
4. Entregar ao critic Vigilia; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Conteúdos de nurture enviados com registro de entrega e taxa de abertura/clique no CRM
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

- **to:** Atlas Evento
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
