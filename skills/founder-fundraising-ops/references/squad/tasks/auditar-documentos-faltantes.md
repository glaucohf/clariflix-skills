---
task: atlas()
responsavel: "Atlas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Acesso ao repositório atual do data room (Google Drive, Notion, Dropbox, Dealroom)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Dados financeiros da empresa (via integração com sistema contábil/financeiro)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Dados de CRM (clientes, churn, expansão"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "para cohort analysis)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Dados do produto (DAU/MAU, NPS"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "para métricas de engajamento)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Data Room Gap Report: lista completa de documentos requeridos com status (pronto / desatualizado / faltante / rascunho disponível), criticidade (blocker para due diligence vs nice-to-have) e owner designado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Rascunhos de documentos faltantes para aprovação do founder (financial model template preenchido, cohort analysis gerada a partir dos dados, unit economics calculados, team bios padronizados)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Data Room Readiness Score (0–100%) por categoria de documento"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Audit log de versões e acessos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Início do processo de captação (auditoria completa inicial). Reunião de due diligence agendada com investidor específico (gera checklist customizado para o perfil daquele investidor). Atualização men…"
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

# Auditar Documentos Faltantes

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Auditar Documentos Faltantes |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Data Room Builder & Compliance Auditor) |
| **execution_type** | `Worker` |
| **input** | 8 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mantém o data room da empresa em estado de due diligence pronto 100% do tempo. Faz a auditoria completa dos documentos requeridos por VCs tier-1 (financial model, cap table, deck, team bios, customer references, LOIs/contratos, cohort analysis, unit economics, product roadmap, legal docs, IP assignments, GDPR/LGPD compliance, employment agreements). Identifica gaps, documentos desatualizados e inconsistências entre documentos. Quando autorizado pelo founder, gera rascunhos dos documentos faltantes a partir dos dados da empresa para revisão. Versiona tudo e mantém audit trail de quem acessou o quê.

## Input

- Acesso ao repositório atual do data room (Google Drive, Notion, Dropbox, Dealroom)
- Dados financeiros da empresa (via integração com sistema contábil/financeiro)
- Dados de CRM (clientes, churn, expansão
- para cohort analysis)
- Dados do produto (DAU/MAU, NPS
- para métricas de engajamento)
- Cap table atual (Carta/Captable.io)
- Checklist de due diligence padrão por estágio (Seed, Série A, Série B) configurado para o perfil da empresa

## Output

- Data Room Gap Report: lista completa de documentos requeridos com status (pronto / desatualizado / faltante / rascunho disponível), criticidade (blocker para due diligence vs nice-to-have) e owner designado
- Rascunhos de documentos faltantes para aprovação do founder (financial model template preenchido, cohort analysis gerada a partir dos dados, unit economics calculados, team bios padronizados)
- Data Room Readiness Score (0–100%) por categoria de documento
- Audit log de versões e acessos

## Trigger

Início do processo de captação (auditoria completa inicial). Reunião de due diligence agendada com investidor específico (gera checklist customizado para o perfil daquele investidor). Atualização mensal automática do Readiness Score. Founder sinaliza novo documento criado (Atlas versiona e cataloga). Alerta quando documento crítico fica desatualizado (ex: financial model com dados >45 dias).

## Knowledge base (o que o executor consulta)

- Checklist de due diligence padrão por estágio (Seed/A/B) baseado em templates públicos de VCs (Y Combinator, Andreessen, Kaszek equivalentes)
- Dados financeiros da empresa (Stripe/QuickBooks/Conta Azul via MCP)
- CRM (HubSpot/Salesforce
- cohort de clientes)
- Cap table (Carta/Captable.io)
- Produto (Mixpanel/Amplitude
- métricas de engajamento)
- Dados de equipe (Gupy/Lever
- headcount, hiring plan)
- Google Drive/Notion (repositório do data room)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Acesso ao repositório atual do data room (Google Drive, Notion, Dropbox, Dealroom)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Data Room Gap Report: lista completa de documentos requeridos com status (pronto / desatualizado / faltante / rascunho…) e persistir no artefato do squad.
4. Entregar ao critic Hades; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Data Room Gap Report: lista completa de documentos requeridos com status (pronto / desatualizado / faltante / rascunho disponível), criticidade (blocker para d…
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

- **to:** Pallas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
