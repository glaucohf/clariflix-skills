---
task: recon()
responsavel: "Recon"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista bruta de participantes (CSV, XLSX, JSON via webhook) com metadados de engajamento do evento"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Configuração de segmentação (limiares de score A/B/C) definida no setup do squad"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso ao CRM para dedup"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lista segmentada e normalizada (JSON estruturado) com: contatos deduplicados, score de engajamento (A/B/C) com justificativa, flag de lead novo vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "existente vs"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "cliente, campos enriquecidos com metadados do evento (nome do evento, data, tipo, tópico)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Registros criados/atualizados no CRM com tag 'evento: {nome} {data}'"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Lista Processada"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "{nome do evento}' com totalizadores (total, novos, existentes, por score A/B/C)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Upload de planilha de participantes pelo cliente; webhook recebido de plataforma de webinar (Zoom, Hotmart, Sympla) indicando fim do evento; chamada manual do Orchestrator Radar para iniciar processa…"
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

# Processar Lista De Participantes

**Task ID:** `recon()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Processar Lista De Participantes |
| **status** | `pending` |
| **responsible_executor** | Recon (Recon — Worker de Ingestão e Segmentação de Lista) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Processa a lista bruta de participantes do evento assim que ela chega (planilha CSV/XLSX, webhook da plataforma de webinar, exportação do sistema de badge). Normaliza campos (nome, email, empresa, cargo, telefone), executa dedup contra o CRM (lead novo vs. conta existente vs. cliente atual), classifica cada contato por score de engajamento (A/B/C) com base nos metadados disponíveis do evento (tempo de sessão, perguntas feitas, downloads, visitas ao estande, cliques em links). Cria ou atualiza registros no CRM com tag de origem do evento e score de engajamento. Alimenta o Orchestrator Radar com a lista segmentada e pronta para ação.

## Input

- Lista bruta de participantes (CSV, XLSX, JSON via webhook) com metadados de engajamento do evento
- Configuração de segmentação (limiares de score A/B/C) definida no setup do squad
- Acesso ao CRM para dedup

## Output

- Lista segmentada e normalizada (JSON estruturado) com: contatos deduplicados, score de engajamento (A/B/C) com justificativa, flag de lead novo vs
- existente vs
- cliente, campos enriquecidos com metadados do evento (nome do evento, data, tipo, tópico)
- Registros criados/atualizados no CRM com tag 'evento: {nome} {data}'
- Artefato ClickUp: task 'Lista Processada
- {nome do evento}' com totalizadores (total, novos, existentes, por score A/B/C)

## Trigger

Upload de planilha de participantes pelo cliente; webhook recebido de plataforma de webinar (Zoom, Hotmart, Sympla) indicando fim do evento; chamada manual do Orchestrator Radar para iniciar processamento pós-evento.

## Knowledge base (o que o executor consulta)

- Schema de normalização de campos por fonte (Zoom Webinar, Hotmart, Sympla, Eventbrite, planilha manual, badge scan)
- regras de dedup contra CRM (match por email, por empresa+nome, por telefone)
- critérios de scoring de engajamento por tipo de evento (webinar: tempo de sessão, perguntas, downloads
- feira: tempo no estande, materiais solicitados, reuniões agendadas)
- mapa de campos do CRM do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista bruta de participantes (CSV, XLSX, JSON via webhook) com metadados de engajamento do evento).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lista segmentada e normalizada (JSON estruturado) com: contatos deduplicados, score de engajamento (A/B/C) com justific…) e persistir no artefato do squad.
4. Entregar ao critic Vigilia; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lista segmentada e normalizada (JSON estruturado) com: contatos deduplicados, score de engajamento (A/B/C) com justificativa, flag de lead novo vs
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

- **to:** Sherlock Évento
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
