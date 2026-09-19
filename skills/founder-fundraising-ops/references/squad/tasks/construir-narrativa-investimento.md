---
task: pallas()
responsavel: "Pallas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Contexto completo da empresa: problema, solução, mercado (TAM/SAM/SOM com fontes), modelo de negócio, métricas de tração (MRR/ARR, growth rate, churn, CAC, LTV, burn, runway), equipe e diferencial competitivo"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Investor Universe Map e Intelligence Briefs do Vega (teses dos investidores alvo)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Deck atual do founder (se existir) para análise e refinamento"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Feedback de reuniões anteriores com investidores (se disponível)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Parâmetros da rodada (ticket, valuation target, uso dos recursos)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pitch Narrative Framework: (1) One-liner de empresa (1 frase, testado contra padrões de clareza)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Elevator pitch (90 segundos, escrito e roteirizado)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Estrutura narrativa completa do deck (slide por slide com headline, conteúdo sugerido e dado de suporte para cada slide)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Versões adaptadas da narrativa por perfil de investidor (early vs growth, estratégico vs financeiro)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(5) Análise crítica do deck atual vs framework recomendado (se deck existir) com sugestões concretas de mudança ordenadas por impacto"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Documento Notion com versão controlada da narrativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Início do processo de captação (narrative framework inicial). Founder recebe feedback de reunião com investidor (narrativa atualizada com os aprendizados). Vega identifica novo investidor tier-1 na l…"
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

# Construir Narrativa Investimento

**Task ID:** `pallas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Construir Narrativa Investimento |
| **status** | `pending` |
| **responsible_executor** | Pallas (Pallas — Narrative Architect & Pitch Strategist) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Constrói e itera a narrativa de captação da empresa — do one-liner até o deck completo. Parte do problema real, da solução diferenciada, do tamanho de mercado documentado, das métricas de tração e do plano de uso dos recursos para construir uma narrativa que responde às perguntas que o VC inevitavelmente fará. Testa a narrativa contra as teses declaradas dos top 20 investidores da lista (via briefs do Vega): o que ressoa, o que conflita, o que precisa ser reposicionado para cada perfil. Gera variações da narrativa por tipo de investidor (VC early-stage vs growth, estratégico vs financeiro, investidor de tese vs investidor de tração).

## Input

- Contexto completo da empresa: problema, solução, mercado (TAM/SAM/SOM com fontes), modelo de negócio, métricas de tração (MRR/ARR, growth rate, churn, CAC, LTV, burn, runway), equipe e diferencial competitivo
- Investor Universe Map e Intelligence Briefs do Vega (teses dos investidores alvo)
- Deck atual do founder (se existir) para análise e refinamento
- Feedback de reuniões anteriores com investidores (se disponível)
- Parâmetros da rodada (ticket, valuation target, uso dos recursos)

## Output

- Pitch Narrative Framework: (1) One-liner de empresa (1 frase, testado contra padrões de clareza)
- (2) Elevator pitch (90 segundos, escrito e roteirizado)
- (3) Estrutura narrativa completa do deck (slide por slide com headline, conteúdo sugerido e dado de suporte para cada slide)
- (4) Versões adaptadas da narrativa por perfil de investidor (early vs growth, estratégico vs financeiro)
- (5) Análise crítica do deck atual vs framework recomendado (se deck existir) com sugestões concretas de mudança ordenadas por impacto
- Documento Notion com versão controlada da narrativa

## Trigger

Início do processo de captação (narrative framework inicial). Founder recebe feedback de reunião com investidor (narrativa atualizada com os aprendizados). Vega identifica novo investidor tier-1 na lista com tese diferente dos anteriores (variante de narrativa gerada). Mudança nos fundamentos da empresa (nova métrica de tração, novo cliente âncora, pivot de posicionamento). Crítico (Hades) sinaliza vulnerabilidade na narrativa.

## Knowledge base (o que o executor consulta)

- Frameworks de pitch reconhecidos publicamente (Y Combinator, NFX, First Round biblioteias públicas de conselhos de pitch)
- Inteligência de tese dos investidores alvo (output do Vega)
- Métricas reais da empresa (output do Atlas e dados financeiros)
- Benchmarks de setor para contextualizar tração (crescimento, churn, NPS comparáveis)
- Histórico de pitches anteriores do founder (se documentados)
- Vector DB com narrativas de empresas comparáveis (dados públicos de pitch decks divulgados)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Contexto completo da empresa: problema, solução, mercado (TAM/SAM/SOM com fontes), modelo de negócio, métricas de traçã…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pitch Narrative Framework: (1) One-liner de empresa (1 frase, testado contra padrões de clareza)) e persistir no artefato do squad.
4. Entregar ao critic Hades; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pitch Narrative Framework: (1) One-liner de empresa (1 frase, testado contra padrões de clareza)
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

- **to:** Brutus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
