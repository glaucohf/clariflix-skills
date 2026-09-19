---
task: sherlockEvento()
responsavel: "Sherlock Évento"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de leads novos e existentes segmentada pelo Recon, com email corporativo e nome da empresa"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Recebido do Orchestrator em paralelo ao início do processamento de segmentação"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossie estruturado (JSON) por contato: empresa (nome, setor, porte, receita estimada, cidade), cargo e seniority do participante, score de fit com ICP (0-100), sinais de intencao recentes (job postings, noticias, mudancas de lideranca), stack tecnologico relevante, outros contatos da empresa no CRM"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registrado como nota enriquecida no contato/conta do CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Enriquecimento Concluido"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "{nome do evento}' com score medio de completude dos dossies"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lista segmentada recebida do Recon. Re-acionado para leads já existentes quando mudança de cargo/empresa e detectada durante processamento."
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

# Enriquecer Dossiê Contato

**Task ID:** `sherlockEvento()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dossiê Contato |
| **status** | `pending` |
| **responsible_executor** | Sherlock Évento (Sherlock Évento — Worker de Enriquecimento de Conta) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Para cada lead novo (nao existente no CRM) identificado pelo Recon, constroi o dossie completo da conta e do contato: empresa, setor, porte, receita estimada, cargo e seniority do participante, sinais de intencao recentes, presenca digital, stack tecnologico (para empresas tech), outros contatos relevantes na empresa. Para leads existentes, atualiza o dossie com eventuais mudancas de cargo ou empresa detectadas. O dossie alimenta tanto o scoring quanto a personalizacao das mensagens pos-evento.

## Input

- Lista de leads novos e existentes segmentada pelo Recon, com email corporativo e nome da empresa
- Recebido do Orchestrator em paralelo ao início do processamento de segmentação

## Output

- Dossie estruturado (JSON) por contato: empresa (nome, setor, porte, receita estimada, cidade), cargo e seniority do participante, score de fit com ICP (0-100), sinais de intencao recentes (job postings, noticias, mudancas de lideranca), stack tecnologico relevante, outros contatos da empresa no CRM
- Registrado como nota enriquecida no contato/conta do CRM
- Artefato ClickUp: task 'Enriquecimento Concluido
- {nome do evento}' com score medio de completude dos dossies

## Trigger

Lista segmentada recebida do Recon. Re-acionado para leads já existentes quando mudança de cargo/empresa e detectada durante processamento.

## Knowledge base (o que o executor consulta)

- Criterios de ICP do cliente (setor, porte, cargo, região, budget estimado)
- integração com Clay e Apollo para busca de dados (275M+ contatos)
- critérios de scoring de fit por dimensão
- histórico de deals ganhos no CRM para calibração do modelo de fit
- playbook de identificação de sinais de intenção por setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de leads novos e existentes segmentada pelo Recon, com email corporativo e nome da empresa).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossie estruturado (JSON) por contato: empresa (nome, setor, porte, receita estimada, cidade), cargo e seniority do par…) e persistir no artefato do squad.
4. Entregar ao critic Vigilia; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossie estruturado (JSON) por contato: empresa (nome, setor, porte, receita estimada, cidade), cargo e seniority do participante, score de fit com ICP (0-100),…
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

- **to:** Alta Intenção
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
