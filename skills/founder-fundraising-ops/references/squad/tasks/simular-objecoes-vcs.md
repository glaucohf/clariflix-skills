---
task: brutus()
responsavel: "Brutus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pitch Narrative Framework do Pallas"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Data Room atual do Atlas (métricas, financial model, cohort analysis)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Investor Intelligence Briefs do Vega (histórico de perguntas típicas de cada investidor alvo)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Estágio da empresa e benchmarks de setor (para identificar onde as métricas estão abaixo do padrão esperado para o estágio)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Feedback real de reuniões anteriores com investidores (se disponível)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Objection Playbook completo: 25–40 objeções organizadas por categoria (mercado, tração, time, competição, modelo de negócio, governança/legal, valuation, uso de recursos), cada uma com (1) pergunta exata no tom do VC, (2) dado que o VC usaria para embasar a objeção, (3) nível de risco para a rodada, (4) contra-argumento recomendado com fonte de dado de suporte, (5) o que NÃO dizer"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Top 5 'buracos da tese'"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "vulnerabilidades objetivas que precisam ser corrigidas antes do roadshow (com plano de mitigação)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Relatório de Stress Test por seção da narrativa (qual parte do pitch gera mais objeções)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Pitch Narrative v1 disponível (rodada inicial de stress test). Founder recebe objeção real em meeting (objeção adicionada ao playbook com análise). Vega identifica novo investidor alvo com histórico…"
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

# Simular Objeções VCs

**Task ID:** `brutus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Simular Objeções VCs |
| **status** | `pending` |
| **responsible_executor** | Brutus (Brutus — VC Objection Simulator & Stress Tester) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Simula os VCs mais difíceis e testa a narrativa, o data room e o founder com as objeções mais duras do mercado. Opera como um painel de 5 personas adversariais de investidor (o VC de tese que questiona o mercado, o VC de tração que questiona os números, o VC de portfolio que compara com empresas similares, o VC legal que questiona governança e cap table, o VC de time que questiona a equipe). Para cada objeção, entrega a pergunta exata como seria feita no meeting, o dado que o VC provavelmente vai citar para embasar a objeção, o nível de risco para a rodada (blocker / alto / médio / baixo) e a melhor contra-resposta possível com os dados disponíveis. Identifica os 'buracos da tese' — onde a narrativa ou os dados são objetivamente fracos.

## Input

- Pitch Narrative Framework do Pallas
- Data Room atual do Atlas (métricas, financial model, cohort analysis)
- Investor Intelligence Briefs do Vega (histórico de perguntas típicas de cada investidor alvo)
- Estágio da empresa e benchmarks de setor (para identificar onde as métricas estão abaixo do padrão esperado para o estágio)
- Feedback real de reuniões anteriores com investidores (se disponível)

## Output

- Objection Playbook completo: 25–40 objeções organizadas por categoria (mercado, tração, time, competição, modelo de negócio, governança/legal, valuation, uso de recursos), cada uma com (1) pergunta exata no tom do VC, (2) dado que o VC usaria para embasar a objeção, (3) nível de risco para a rodada, (4) contra-argumento recomendado com fonte de dado de suporte, (5) o que NÃO dizer
- Top 5 'buracos da tese'
- vulnerabilidades objetivas que precisam ser corrigidas antes do roadshow (com plano de mitigação)
- Relatório de Stress Test por seção da narrativa (qual parte do pitch gera mais objeções)

## Trigger

Pitch Narrative v1 disponível (rodada inicial de stress test). Founder recebe objeção real em meeting (objeção adicionada ao playbook com análise). Vega identifica novo investidor alvo com histórico de perguntas específicas (objeções customizadas para aquele investidor geradas). Hades (critic) sinaliza vulnerabilidade na narrativa ou no data room. 72h antes de cada meeting importante (briefing de objeções específicas para aquele investidor gerado).

## Knowledge base (o que o executor consulta)

- Padrões de objeção de VCs por estágio e setor (pesquisa pública em blogs, podcasts e entrevistas de GPs)
- Benchmarks de métricas por estágio (growth rate, churn, CAC payback, LTV/CAC esperados para Seed/A/B em SaaS, marketplace, etc.)
- Histórico de objeções recebidas em meetings reais (alimentado pelo founder após cada reunião)
- Financial model e métricas reais da empresa (para calibrar onde os números são vulneráveis)
- Intelligence Briefs dos investidores alvo (objeções específicas por persona)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pitch Narrative Framework do Pallas).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Objection Playbook completo: 25–40 objeções organizadas por categoria (mercado, tração, time, competição, modelo de neg…) e persistir no artefato do squad.
4. Entregar ao critic Hades; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Objection Playbook completo: 25–40 objeções organizadas por categoria (mercado, tração, time, competição, modelo de negócio, governança/legal, valuation, uso d…
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

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
