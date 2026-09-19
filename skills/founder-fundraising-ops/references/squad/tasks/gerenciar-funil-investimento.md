---
task: hermes()
responsavel: "Hermes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Investor Universe Map ranqueado do Vega"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Intelligence Briefs individuais dos top 20 investidores"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Pitch Narrative Framework do Pallas (para personalizar mensagem de acordo com a tese do investidor)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Network do founder para identificar warm intro paths"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Status atual de cada contato (quem foi contactado, quem respondeu, qual etapa do funil)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Parâmetros de timing do roadshow definidos pelo founder"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens de outreach personalizadas por investidor (cold email ou intro request)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "rascunhadas para aprovação do founder antes de qualquer envio"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Sequência de follow-up por investidor (timing e mensagem adaptados ao estágio no funil)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Roadshow Tracker no ClickUp: dashboard de funil completo com status, próximos passos, datas e notas de cada reunião"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Relatório semanal de funil (quantos em cada etapa, taxa de conversão, projeção de fechamento baseada no funil atual)"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Alertas de follow-up vencido (investidor sem contato há X dias sem motivo registrado)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Investor Universe Map finalizado e aprovado pelo founder (inicia sequência de outreach). Founder aprova mensagem no HITL Gate (executa envio e registra no tracker). Investidor responde (Hermes atuali…"
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

# Gerenciar Funil Investimento

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerenciar Funil Investimento |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — Outreach Sequencer & Pipeline Tracker) |
| **execution_type** | `Agent` |
| **input** | 6 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Opera o pipeline de outreach aos investidores com precision cirúrgica. Personaliza cada mensagem de primeiro contato com base no Intelligence Brief do Vega — nunca manda um cold email genérico. Mapeia e gerencia os warm intro paths (quem pode conectar o founder com quem, em qual plataforma, qual a melhor forma de pedir a intro sem queimar o relacionamento). Gerencia o funil de captação completo no ClickUp: primeiro contato → resposta → first meeting → second meeting → term sheet → fechamento. Gera follow-ups automáticos baseados no estágio e no silêncio (sem resposta em X dias → follow-up Y). Entrega relatório semanal de funil para o founder.

## Input

- Investor Universe Map ranqueado do Vega
- Intelligence Briefs individuais dos top 20 investidores
- Pitch Narrative Framework do Pallas (para personalizar mensagem de acordo com a tese do investidor)
- Network do founder para identificar warm intro paths
- Status atual de cada contato (quem foi contactado, quem respondeu, qual etapa do funil)
- Parâmetros de timing do roadshow definidos pelo founder

## Output

- Mensagens de outreach personalizadas por investidor (cold email ou intro request)
- rascunhadas para aprovação do founder antes de qualquer envio
- Sequência de follow-up por investidor (timing e mensagem adaptados ao estágio no funil)
- Roadshow Tracker no ClickUp: dashboard de funil completo com status, próximos passos, datas e notas de cada reunião
- Relatório semanal de funil (quantos em cada etapa, taxa de conversão, projeção de fechamento baseada no funil atual)
- Alertas de follow-up vencido (investidor sem contato há X dias sem motivo registrado)

## Trigger

Investor Universe Map finalizado e aprovado pelo founder (inicia sequência de outreach). Founder aprova mensagem no HITL Gate (executa envio e registra no tracker). Investidor responde (Hermes atualiza status no tracker e prepara próximo passo). X dias sem resposta após envio (follow-up automático rascunhado para aprovação). Meeting concluído (Hermes solicita feedback do founder para atualizar tracker e playbook de objeções). Novo investidor adicionado à lista.

## Knowledge base (o que o executor consulta)

- Investor Intelligence Briefs do Vega (personalização de mensagens)
- Pitch Narrative Framework do Pallas (alinhamento de messaging)
- Network do founder (LinkedIn, conexões diretas para warm intros)
- Histórico de respostas e conversas anteriores com cada investidor (para contexto em follow-ups)
- Templates de cold email e intro request validados por estágio (base pública de melhores práticas)
- ClickUp (estado do pipeline de captação)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Investor Universe Map ranqueado do Vega).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens de outreach personalizadas por investidor (cold email ou intro request)) e persistir no artefato do squad.
4. Entregar ao critic Hades; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens de outreach personalizadas por investidor (cold email ou intro request)
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

- **to:** Mnemo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
