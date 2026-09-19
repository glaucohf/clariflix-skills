---
task: scout()
responsavel: "SCOUT"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Query de benchmark gerada pelo SKEPTIC (para red-team de premissa especifica) ou pelo ORACLE (para postmortem com dados externos), tipo de decisao e setor do founder, lista de premissas especificas que precisam de base rate externo, decisoes abertas no journal com premissas que podem ser monitoradas por dados publicos"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio de Benchmarks com: (1) Base rates encontrados por premissa pesquisada (ex: 'taxa de sucesso de contratacao de VP de Vendas em SaaS B2B: 58% nos primeiros 12 meses"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "fonte: First Round Capital State of Startups 2024'), (2) Casos analogos identificados (decisoes similares em empresas comparaveis e seus resultados), (3) Dados de mercado relevantes para premissas abertas, (4) Cada claim com fonte + URL + data + grau de confiabilidade (VERIFICADO / INFERIDO / ESTIMATIVA SETORIAL), (5) Sinalizacao de quando a base rate contradiz significativamente a premissa do founder (flag para SKEPTIC ou ORACLE)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Entregue ao agente solicitante em formato estruturado para incorporacao ao Red-Team Report ou Postmortem Analysis"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo SKEPTIC para pesquisa de base rates de premissas especificas durante red-team. Acionado pelo ORACLE durante analise de postmortem para contextualizar resultado com dados setoriais. Cron…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic MIRROR antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder antes de ser persistida — o clone nunca evolui seus principios nucleares sem consentimento explicito do dono do conhecimento"
    - "[ ] L3: ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirmacao do founder de que quer registrar — nenhum trigger automatico substitui a intencao explicita para eventos deste nivel"
    - "[ ] L3: SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu prosseguir, ou que discorda do SKEPTIC com justificativa registrada — garante accountability do processo, nao apenas do resultado"
    - "[ ] L2: ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao capturou antes do relatorio ser finalizado e enviado ao CALIBRADOR"
    - "[ ] L2: CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima custo de integracao — recomendamos adicionar gate obrigatorio de validacao tecnica antes de fechar contratos acima de R$X'): founder aprova ou rejeita a mudanca de processo antes de ser codificada"
---

# Pesquisar Dados Referenciais

**Task ID:** `scout()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Pesquisar Dados Referenciais |
| **status** | `pending` |
| **responsible_executor** | SCOUT (SCOUT — O Pesquisador de Benchmarks e Base Rates) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de pesquisa externa especializado em dados de referencia para calibracao de premissas. Quando uma decisao envolve premissas que podem ser verificadas contra dados de mercado (ex: 'o ICP X tem capacidade de pagar Y', 'o tempo de ramp de um VP de Vendas em SaaS e Z meses', 'taxa de churn neste modelo de negocio e W%'), o SCOUT pesquisa fontes confiáveis e retorna base rates, benchmarks setoriais e casos analogos com citacao de fonte. Tambem monitora continuamente — via alertas configurados — dados e estudos que podem impactar premissas de decisoes abertas no journal. Quando encontra dado relevante para uma decisao em andamento, notifica o VERDICT proativamente. Todo claim retornado pelo SCOUT vem com fonte, data e grau de confiabilidade.

## Input

- Query de benchmark gerada pelo SKEPTIC (para red-team de premissa especifica) ou pelo ORACLE (para postmortem com dados externos), tipo de decisao e setor do founder, lista de premissas especificas que precisam de base rate externo, decisoes abertas no journal com premissas que podem ser monitoradas por dados publicos

## Output

- Relatorio de Benchmarks com: (1) Base rates encontrados por premissa pesquisada (ex: 'taxa de sucesso de contratacao de VP de Vendas em SaaS B2B: 58% nos primeiros 12 meses
- fonte: First Round Capital State of Startups 2024'), (2) Casos analogos identificados (decisoes similares em empresas comparaveis e seus resultados), (3) Dados de mercado relevantes para premissas abertas, (4) Cada claim com fonte + URL + data + grau de confiabilidade (VERIFICADO / INFERIDO / ESTIMATIVA SETORIAL), (5) Sinalizacao de quando a base rate contradiz significativamente a premissa do founder (flag para SKEPTIC ou ORACLE)
- Entregue ao agente solicitante em formato estruturado para incorporacao ao Red-Team Report ou Postmortem Analysis

## Trigger

Acionado pelo SKEPTIC para pesquisa de base rates de premissas especificas durante red-team. Acionado pelo ORACLE durante analise de postmortem para contextualizar resultado com dados setoriais. Cron job semanal para monitorar dados e publicacoes que impactam premissas de decisoes abertas no journal (ex: relatorios de mercado, dados de benchmark setorial publicados). Tambem acionado manualmente pelo founder para pesquisa pontual de base rates antes de tomar uma decisao nao estruturada.

## Knowledge base (o que o executor consulta)

- EXA MCP (busca web em tempo real com citacao de fonte), Apify (scraping de relatorios setoriais, benchmarks de VCs, estudos de caso publicos), base de fontes confiáveis curada por setor do founder (relatorios de VCs, associacoes setoriais, estudos academicos aplicados), historico de benchmarks ja pesquisados (para evitar retrabalho e detectar evolucao de dados), taxonomia de tipos de decisao mapeada no Discovery para selecionar fontes adequadas por tipo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Query de benchmark gerada pelo SKEPTIC (para red-team de premissa especifica) ou pelo ORACLE (para postmortem com dados…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio de Benchmarks com: (1) Base rates encontrados por premissa pesquisada (ex: 'taxa de sucesso de contratacao de…) e persistir no artefato do squad.
4. Entregar ao critic MIRROR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio de Benchmarks com: (1) Base rates encontrados por premissa pesquisada (ex: 'taxa de sucesso de contratacao de VP de Vendas em SaaS B2B: 58% nos prime…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic MIRROR registrado
- [ ] Gate L3 respeitado: CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao ex…
- [ ] Gate L3 respeitado: ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e…
- [ ] Gate L3 respeitado: SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar q…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder a… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirm… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima cus… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — RADAR ao detectar sinal de refutacao FORTE de premissa critica em decisao de alto impacto ANTES da janela de postmortem: notificacao imediata ao founder com su… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — Configuracao inicial de thresholds (Discovery): founder define pessoalmente os criterios de disparo automatico, as janelas de revisao por tipo de decisao e o n… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic MIRROR | BLOQUEIA entrega |

## Handoff

- **to:** RADAR
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
