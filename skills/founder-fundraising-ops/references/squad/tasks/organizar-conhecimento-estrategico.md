---
task: mnemo()
responsavel: "Mnemo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcrições de meetings com investidores (Sembly/Fireflies ou upload manual)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Notas e feedbacks do founder após cada reunião"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Histórico de comunicações por email com investidores (Gmail via MCP, com permissão explícita do founder)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Documentos de rodadas anteriores (term sheets, investment memos)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Decisões estratégicas documentadas"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Output dos outros agentes (Intelligence Briefs, Objection Playbook, versões da narrativa)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Knowledge Graph consultável de toda a operação de captação (relações entre investidores, perguntas, respostas, decisões e artefatos)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Respostas a consultas em linguagem natural do founder sobre o histórico de captação"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Briefing pré-meeting automático (48h antes de qualquer reunião com investidor: resumo do histórico de interações, última conversa, o que ficou pendente, perguntas previstas baseadas no histórico)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Síntese periódica de aprendizados da rodada (o que mudou no entendimento do mercado, quais objeções dominaram, qual perfil de investidor engajou mais)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Transcrição de meeting com investidor disponível (ingestão imediata). Founder registra feedback pós-meeting (estruturado e adicionado ao grafo). 48h antes de reunião com investidor (briefing pré-meet…"
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

# Organizar Conhecimento Estratégico

**Task ID:** `mnemo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Organizar Conhecimento Estratégico |
| **status** | `pending` |
| **responsible_executor** | Mnemo (Mnemo — Knowledge Graph & Founder Memory) |
| **execution_type** | `Worker` |
| **input** | 6 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Estrutura o conhecimento estratégico e tácito do founder em um grafo consultável que alimenta todos os outros agentes. Ingere e organiza: transcrições de meetings com investidores (o que foi perguntado, o que foi respondido, qual foi a reação), feedbacks recebidos, aprendizados de rodadas anteriores, teses e hipóteses do founder sobre o mercado, decisões estratégicas tomadas e as razões por trás delas. Responde a consultas como 'qual foi o principal feedback da Astella no último meeting?', 'quais objeções o XYZ sempre levanta?', 'o que prometemos para o Sequoia em 2023?'. É a memória institucional da operação de captação.

## Input

- Transcrições de meetings com investidores (Sembly/Fireflies ou upload manual)
- Notas e feedbacks do founder após cada reunião
- Histórico de comunicações por email com investidores (Gmail via MCP, com permissão explícita do founder)
- Documentos de rodadas anteriores (term sheets, investment memos)
- Decisões estratégicas documentadas
- Output dos outros agentes (Intelligence Briefs, Objection Playbook, versões da narrativa)

## Output

- Knowledge Graph consultável de toda a operação de captação (relações entre investidores, perguntas, respostas, decisões e artefatos)
- Respostas a consultas em linguagem natural do founder sobre o histórico de captação
- Briefing pré-meeting automático (48h antes de qualquer reunião com investidor: resumo do histórico de interações, última conversa, o que ficou pendente, perguntas previstas baseadas no histórico)
- Síntese periódica de aprendizados da rodada (o que mudou no entendimento do mercado, quais objeções dominaram, qual perfil de investidor engajou mais)

## Trigger

Transcrição de meeting com investidor disponível (ingestão imediata). Founder registra feedback pós-meeting (estruturado e adicionado ao grafo). 48h antes de reunião com investidor (briefing pré-meeting gerado automaticamente). Consulta ad-hoc do founder sobre histórico. Encerramento de rodada (síntese completa de aprendizados gerada para documentação).

## Knowledge base (o que o executor consulta)

- Vector DB com todas as transcrições de meetings de investidores
- Histórico de emails com investidores (Gmail/Outlook via MCP, com autorização)
- Notas do founder (Notion, arquivos de texto)
- Knowledge Graph (Neo4j ou equivalente) com relações entre investidores, perguntas, artefatos e decisões
- Histórico de todas as versões da narrativa e do data room (para comparação temporal)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcrições de meetings com investidores (Sembly/Fireflies ou upload manual)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Knowledge Graph consultável de toda a operação de captação (relações entre investidores, perguntas, respostas, decisões…) e persistir no artefato do squad.
4. Entregar ao critic Hades; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Knowledge Graph consultável de toda a operação de captação (relações entre investidores, perguntas, respostas, decisões e artefatos)
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

- **to:** Gate
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
