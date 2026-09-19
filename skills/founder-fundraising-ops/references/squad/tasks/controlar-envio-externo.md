---
task: gate()
responsavel: "Gate"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem de outreach ou follow-up rascunhada pelo Hermes"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Data room link ou documento para compartilhamento solicitado por qualquer agente"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Contexto do envio (destinatário, canal, estágio no funil, histórico de interação)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Score de status do data room do Atlas (versão atual sendo compartilhada está auditada?)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Lista de NDAs assinados por investidor"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tela de confirmação para o founder: (1) destinatário e histórico resumido, (2) mensagem exata que será enviada, (3) nível de acesso de data room sendo concedido (se aplicável), (4) status de NDA (assinado / não assinado / em processo), (5) 2–3 pontos de atenção do Gate antes do envio"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Após aprovação: execução do envio + registro no ClickUp (timestamp, versão do artefato, destinatário, canal)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Após recusa ou modificação: atualiza rascunho e volta ao founder"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "NUNCA pode ser bypassado"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "é o único ponto de saída do sistema para o mundo externo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Qualquer ação de envio externo solicitada por qualquer agente do squad (Hermes, Atlas, Pallas). Compartilhamento de link de data room. Agendamento de reunião com confirmação de detalhes. Acionado aut…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Hades antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível"
    - "[ ] HITL: Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão do documento, nível de acesso)"
    - "[ ] HITL: Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades abordar proativamente vs deixar sem abordar"
    - "[ ] HITL: Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta priorização"
    - "[ ] HITL: Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente vs delegar à IA para rascunho"
---

# Controlar Envio Externo

**Task ID:** `gate()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Controlar Envio Externo |
| **status** | `pending` |
| **responsible_executor** | Gate (Gate — HITL Compliance & External Send Controller) |
| **execution_type** | `Hybrid` |
| **input** | 5 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Intercepta 100% das ações de comunicação externa antes de executar. Nenhum email, mensagem, link de data room ou qualquer outra comunicação chega a um investidor real sem passar por este agente. Apresenta ao founder um resumo de revisão final: destinatário, mensagem completa, contexto (estágio no funil, histórico de interação), e exige confirmação explícita antes de qualquer envio. Para envio de data room ou documentos financeiros, ativa checklist de confirmação dupla (L3): confirma o investidor, o NDA status, a versão do documento e o nível de acesso sendo concedido. Registra audit trail completo de todo outreach realizado.

## Input

- Mensagem de outreach ou follow-up rascunhada pelo Hermes
- Data room link ou documento para compartilhamento solicitado por qualquer agente
- Contexto do envio (destinatário, canal, estágio no funil, histórico de interação)
- Score de status do data room do Atlas (versão atual sendo compartilhada está auditada?)
- Lista de NDAs assinados por investidor

## Output

- Tela de confirmação para o founder: (1) destinatário e histórico resumido, (2) mensagem exata que será enviada, (3) nível de acesso de data room sendo concedido (se aplicável), (4) status de NDA (assinado / não assinado / em processo), (5) 2–3 pontos de atenção do Gate antes do envio
- Após aprovação: execução do envio + registro no ClickUp (timestamp, versão do artefato, destinatário, canal)
- Após recusa ou modificação: atualiza rascunho e volta ao founder
- NUNCA pode ser bypassado
- é o único ponto de saída do sistema para o mundo externo

## Trigger

Qualquer ação de envio externo solicitada por qualquer agente do squad (Hermes, Atlas, Pallas). Compartilhamento de link de data room. Agendamento de reunião com confirmação de detalhes. Acionado automaticamente pelo Hermes quando mensagem está pronta para envio. Compartilhamento de documentos financeiros (L3 — confirmação dupla obrigatória).

## Knowledge base (o que o executor consulta)

- Lista de investidores com status de NDA (assinado/não)
- Histórico completo de comunicações enviadas por investidor (para contexto de follow-up e evitar duplicatas)
- Política de compartilhamento de data room configurada pelo founder (quem pode ver o quê, em qual estágio do funil)
- Versão atual auditada do data room (output do Atlas)
- Configurações de compliance do squad definidas pelo founder na onboarding

## Action Items

1. Confirmar o gatilho e carregar a entrada (Mensagem de outreach ou follow-up rascunhada pelo Hermes).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tela de confirmação para o founder: (1) destinatário e histórico resumido, (2) mensagem exata que será enviada, (3) nív…) e persistir no artefato do squad.
4. Entregar ao critic Hades; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tela de confirmação para o founder: (1) destinatário e histórico resumido, (2) mensagem exata que será enviada, (3) nível de acesso de data room sendo concedid…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Hades registrado
- [ ] Gate HITL respeitado: Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass p…
- [ ] Gate HITL respeitado: Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto,…
- [ ] Gate HITL respeitado: Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide qua…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão d… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta p… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação da Pitch Narrative Framework pelo founder antes de qualquer variante ser usada em meeting — founder valida o posicionamento, o use of funds e o valua… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do Knowledge Graph do Mnemo — founder autoriza explicitamente quais fontes de dados históricos (emails, transcrições) podem ser ingeridas… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança nos termos da rodada refletida nos artefatos (ticket, valuation, estrutura) requer aprovação explícita antes de Hermes atualizar mensagens de… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Hades | BLOQUEIA entrega |

## Handoff

- **to:** Hades
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
