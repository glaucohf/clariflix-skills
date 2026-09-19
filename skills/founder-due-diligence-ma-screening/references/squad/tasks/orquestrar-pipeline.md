---
task: nexusPipeline()
responsavel: "Nexus"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote M&A Screening completo por target: (1) Target Profile v0 JSON (dados normalizados de fontes abertas)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) 5 Sub-relatorios de workers (Financeiro, Juridico, Mercado, Tech, Pessoas) com claims 100% rastreados"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Relatorio de Verificacao do Columbo com score de confianca"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Scorecard M&A (12 dimensoes, 0-10)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(5) Red Flag Register com severidade e evidencia"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(6) Tese de Aquisicao com hipoteses de valor e sinergias"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do pipeline M&A. Recebe a intenção do founder (nome do target ou lista de targets), decompõe em trilhas de pesquisa paralelas, roteia para workers especializados, controla depend…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Columbo 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complementa com dados adicionais (especialmente se completude < 60). Criticidade: ALTA — avançar com dados incompletos invalida todo o pipeline."
    - "[ ] HITL: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFIED/DISPUTED para decisão: aceitar o risco e prosseguir, solicitar pesquisa adicional (re-ativa workers específicos), ou cancelar a triagem do target."
    - "[ ] HITL: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20% do valuation estimado, irregularidade fiscal grave) pausa o pipeline e exige confirmação do founder antes de prosseguir. Pode levar ao cancelamento imediato da triagem."
    - "[ ] HITL: HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilhamento com advisors, bancos, co-investidores ou o próprio target. Ações irreversíveis (envio externo) sempre requerem aprovação humana explícita."
    - "[ ] HITL: HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados pontos. Eco re-executa com instruções específicas. Não é irreversível, mas é um checkpoint de qualidade importante."
---

# Orquestrar Pipeline do Due Diligence / M&A Screening

**Task ID:** `nexusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Due Diligence / M&A Screening

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Due Diligence / M&A Screening |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — O Estrategista de Aquisições) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do pipeline M&A. Recebe a intenção do founder (nome do target ou lista de targets), decompõe em trilhas de pesquisa paralelas, roteia para workers especializados, controla dependências entre fases, agrega resultados, aciona o Critic e entrega o pacote final. Opera em L2: executa autonomamente o pipeline inteiro, mas solicita aprovação humana em gates L3 antes de ações irreversíveis (envio de memo, contato externo, aprovação de gasto). Persona: diretor de M&A experiente que sabe o que o founder precisa antes que ele pergunte.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote M&A Screening completo por target: (1) Target Profile v0 JSON (dados normalizados de fontes abertas)
- (2) 5 Sub-relatorios de workers (Financeiro, Juridico, Mercado, Tech, Pessoas) com claims 100% rastreados
- (3) Relatorio de Verificacao do Columbo com score de confianca
- (4) Scorecard M&A (12 dimensoes, 0-10)
- (5) Red Flag Register com severidade e evidencia
- (6) Tese de Aquisicao com hipoteses de valor e sinergias
- (7) Investment Memo personalizado na voz do founder (PDF + Markdown) com recomendacao Go/Conditional Go/No-Go
- Tudo gravado no ClickUp como prova de trabalho e no knowledge base do squad para aprendizado continuo

## Trigger

Orquestrador central do pipeline M&A. Recebe a intenção do founder (nome do target ou lista de targets), decompõe em trilhas de pesquisa paralelas, roteia para workers especializados, controla dependências entre fases, agrega resultados, aciona o Critic e entrega o pacote final. Opera em L2: executa autonomamente o pipeline inteiro, mas solicita aprovação humana em gates L3 antes de ações irreversíveis (envio de memo, contato externo, aprovação de gasto). Persona: diretor de M&A experiente que sabe o que o founder precisa antes que ele pergunte.

## Knowledge base (o que o executor consulta)

- Gerenciamento de tasks e prova de trabalho: cada triagem e uma task com sub-tasks por agente, status tracking e entrega do artefato final linkado
- Notion / Obsidian
- Knowledge base do founder (corpus de decisões, memos anteriores, teses) que alimenta o Eco (Clone Agent)
- Vector DB (Pinecone / Supabase pgvector)
- Embeddings do corpus do founder e histórico de triagens anteriores para o Eco e o Columbo aprenderem com cada ciclo
- DataJud (CNJ)
- Processos judiciais públicos via API para o Themis
- Receita Federal / CNPJ.info
- Dados societários e CNPJ para o Argus
- LinkedIn Sales Navigator
- Histórico profissional, tenure de C-level, headcount para Vox e Atlas
- Crunchbase API
- Funding history, exits, investors para Fênix e Sigma
- Glassdoor / Blind (scraping)
- Cultura e reviews para Vox
- BuiltWith / Wappalyzer
- Stack tecnológico para Atlas
- Google News API
- Cobertura de mídia para Argus e Vox
- Observabilidade OTEL: tracing de tokens, custo por triagem, latência por agente, task success rate por fase
- Notificações de status do pipeline ao founder (Target Profile pronto, Deep Dive completo, Memo disponível para revisão, gates L3 aguardando aprovação)
- Gmail / Email
- Entrega do Investment Memo final em PDF após aprovacao L3
- Consulta de patentes e marcas registradas para Themis e Atlas
- BACEN (SCR/API)
- Regularidade financeira e dados de crédito para Fenix e Themis

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Columbo 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote M&A Screening completo por target: (1) Target Profile v0 JSON (dados normalizados de fontes abertas)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Columbo 2 registrado
- [ ] Gate HITL respeitado: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude…
- [ ] Gate HITL respeitado: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a list…
- [ ] Gate HITL respeitado: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passiv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complem… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFI… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20%… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilham… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados po… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL Gate L1 — Configuração Inicial do Target: O founder define a intenção estratégica (por que este target, qual a tese inicial, quais setores/mercados são re… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Columbo 2 | BLOQUEIA entrega |

## Handoff

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
