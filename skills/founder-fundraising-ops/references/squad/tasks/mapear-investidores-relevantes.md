---
task: vega()
responsavel: "Vega"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Perfil da empresa (estágio, setor, ticket alvo, geografias de interesse, métricas atuais de tração)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Critérios de fit configurados pelo founder (ticket mínimo/máximo, estágios investidos, setores de foco, restrições de conflito com portfólio atual)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Network do founder (LinkedIn exportado ou lista manual de conexões de 1º grau) para identificar warm intro paths"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Lista de investidores já contatados ou descartados pelo founder"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Investor Universe Map: spreadsheet/database com 80–150 investidores ranqueados por score de fit (0–10), incluindo nome, fundo, ticket médio, estágios, tese resumida, portfólio relevante, contato e warm intro path"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Investor Intelligence Brief individual (1 página por investidor nos top 20): tese, portfólio pattern, perguntas típicas conhecidas, sinais de atividade recente, melhor abordagem de contato"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Mapa de conflitos de portfólio (investidores a evitar por sobreposição direta com portfólio existente)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Início do processo de captação (founder define parâmetros da rodada). Atualização semanal automática dos top 20 investidores (sinais de atividade). Founder adiciona novo investidor para pesquisa. Reu…"
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

# Mapear Investidores Relevantes

**Task ID:** `vega()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Mapear Investidores Relevantes |
| **status** | `pending` |
| **responsible_executor** | Vega (Vega — Investor Intelligence & Universe Mapper) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mapeia e ranqueia o universo completo de investidores relevantes para o perfil da empresa. Cruza bases públicas de VCs, anjos e fundos com critérios de fit configurados pelo founder (ticket, estágio, setor, geografia, portfólio atual para detectar conflito). Para cada investidor tier-1, gera um Investor Intelligence Brief: tese declarada publicamente, empresas do portfólio com análise de padrão de investimento, histórico de perguntas em eventos e podcasts públicos, forma preferida de contato (cold email vs intro vs evento), rede de warm intro path (quem do network do founder pode conectar). Atualiza a base semanalmente com sinais de atividade (novo fundo levantado, check escrito recente, post público sobre tese).

## Input

- Perfil da empresa (estágio, setor, ticket alvo, geografias de interesse, métricas atuais de tração)
- Critérios de fit configurados pelo founder (ticket mínimo/máximo, estágios investidos, setores de foco, restrições de conflito com portfólio atual)
- Network do founder (LinkedIn exportado ou lista manual de conexões de 1º grau) para identificar warm intro paths
- Lista de investidores já contatados ou descartados pelo founder

## Output

- Investor Universe Map: spreadsheet/database com 80–150 investidores ranqueados por score de fit (0–10), incluindo nome, fundo, ticket médio, estágios, tese resumida, portfólio relevante, contato e warm intro path
- Investor Intelligence Brief individual (1 página por investidor nos top 20): tese, portfólio pattern, perguntas típicas conhecidas, sinais de atividade recente, melhor abordagem de contato
- Mapa de conflitos de portfólio (investidores a evitar por sobreposição direta com portfólio existente)

## Trigger

Início do processo de captação (founder define parâmetros da rodada). Atualização semanal automática dos top 20 investidores (sinais de atividade). Founder adiciona novo investidor para pesquisa. Reunião com investidor agendada (brief detalhado pré-meeting é gerado automaticamente com 48h de antecedência). Mudança nos critérios da rodada (ticket, estágio, foco setorial).

## Knowledge base (o que o executor consulta)

- Base de VCs e fundos ativos Brasil/global (Distrito, ABVCAP, Crunchbase, PitchBook dados públicos)
- Portfolio de cada fundo (via Crunchbase/LinkedIn)
- Transcrições públicas de palestras, podcasts e entrevistas de GPs (para extrair teses e perguntas típicas)
- LinkedIn do network do founder (warm intro paths)
- EXA/Perplexity MCP para pesquisa em tempo real de atividade recente
- Vector DB com histórico de Intelligence Briefs anteriores

## Action Items

1. Confirmar o gatilho e carregar a entrada (Perfil da empresa (estágio, setor, ticket alvo, geografias de interesse, métricas atuais de tração)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Investor Universe Map: spreadsheet/database com 80–150 investidores ranqueados por score de fit (0–10), incluindo nome,…) e persistir no artefato do squad.
4. Entregar ao critic Hades; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Investor Universe Map: spreadsheet/database com 80–150 investidores ranqueados por score de fit (0–10), incluindo nome, fundo, ticket médio, estágios, tese res…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
