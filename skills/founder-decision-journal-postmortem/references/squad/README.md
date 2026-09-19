# Decision Journal & Postmortem — Calibrador de Julgamento do Founder

> Cada decisao registrada e uma licao que o clone aprende — cada postmortem e calibracao que dinheiro nao compra.

**Área:** Founder Office · **TopSquad:** F2 Performance, KPIs & Calibração de Decisões · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Founders tomam decisoes de alto impacto sem registrar as premissas que as sustentaram. Seis meses depois, quando o resultado e conhecido, nenhuma retrospectiva acontece: a decisao foi boa por competencia ou sorte? A premissa estava certa ou errada? Sem esse loop fechado, o julgamento nao melhora — e o clone nunca aprende o que o founder pensava NO MOMENTO da decisao, apenas o que ele diz ter pensado depois (memoria revisada). Mensuravel por: % de decisoes de alto impacto com premissas registradas antes do resultado (baseline tipico: < 10%, meta: > 80% em 60 dias) e taxa de premissas revisitadas em postmortem estruturado (baseline: ~0%, meta: > 70% das decisoes de 90+ dias revisadas nos primeiros 6 meses de operacao).

## Impacto esperado

Decisoes de alto impacto em empresas de R$2-20M ARR costumam envolver alocacao de capital (R$50k-500k por ciclo), contratacoes estrategicas, pivots de posicionamento e acordos comerciais. Uma unica decisao mal calibrada — ex: contratar o perfil errado de VP de Vendas por falhar em validar a premissa de ICP — pode custar R$150k-400k entre salario, rescisao e oportunidade perdida. O squad fecha o loop de aprendizado que transforma experiencia em sabedoria sistematizada: ao forcar o registro de premissas PRE-decisao e o postmortem POST-resultado, o founder desenvolve calibracao real de julgamento. Para o clone: cada postmortem e dado de treino de alta qualidade — o clone aprende NAO SO a decisao mas O RACIOCINIO no momento em que ele aconteceu, sem revisao de memoria. ROI estimado: prevencao de 1-2 decisoes mal calibradas por trimestre em empresas de medio porte representa R$200k-800k/ano de capital e oportunidade preservados, contra um custo de squad de R$3k-6k/mes.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `verdict` · VERDICT | VERDICT — O Arquivista-Mor de Decisoes | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `archivist` · ARCHIVIST | ARCHIVIST — O Capturador de Premissas | L1 · worker autônomo | `capturar-decisoes.md` |
| `skeptic` · SKEPTIC | SKEPTIC — O Red-Team de Premissas | L2 · orquestra / decide | `desafiar-premissas-declarativas.md` |
| `scout` · SCOUT | SCOUT — O Pesquisador de Benchmarks e Base Rates | L1 · worker autônomo | `pesquisar-dados-referenciais.md` |
| `radar` · RADAR | RADAR — O Monitor de Premissas em Tempo Real | L1 · worker autônomo | `monitorar-premissas-decisoes.md` |
| `oracle` · ORACLE | ORACLE — O Analista de Postmortem | L2 · orquestra / decide | `analisar-decisoes-postmortem.md` |
| `calibrador` · CALIBRADOR | CALIBRADOR — O Sintetizador do Clone | L3 · aprovação humana | `calibrar-julgamento.md` |
| `sentinel-dj` · SENTINEL-DJ | SENTINEL-DJ — O Guardiao de Integridade do Journal | L0 · worker determinístico | `verificar-integridade-temporal.md` |
| `mirror` · MIRROR | MIRROR — O Verificador de Calibracao e Anti-Viés | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-decision-journal-postmortem:verdict` (ou instale via `npx squads add ./founder-decision-journal-postmortem`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-decision-journal-postmortem-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder antes de ser persistida — o clone nunca evolui seus principios nucleares sem consentimento explicito do dono do conhecimento
- L3 — ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirmacao do founder de que quer registrar — nenhum trigger automatico substitui a intencao explicita para eventos deste nivel
- L3 — SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu prosseguir, ou que discorda do SKEPTIC com justificativa registrada — garante accountability do processo, nao apenas do resultado
- L2 — ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao capturou antes do relatorio ser finalizado e enviado ao CALIBRADOR
- L2 — CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima custo de integracao — recomendamos adicionar gate obrigatorio de validacao tecnica antes de fechar contratos acima de R$X'): founder aprova ou rejeita a mudanca de processo antes de ser codificada
- L1 — RADAR ao detectar sinal de refutacao FORTE de premissa critica em decisao de alto impacto ANTES da janela de postmortem: notificacao imediata ao founder com sumario do sinal e pergunta direta — 'voce quer antecipar o postmortem ou tem informacao adicional sobre este sinal?'
- L1 — Configuracao inicial de thresholds (Discovery): founder define pessoalmente os criterios de disparo automatico, as janelas de revisao por tipo de decisao e o nivel de detalhe requerido por categoria — nenhum default e assumido sem validacao explicita

## KPIs

- Taxa de cobertura de decisoes: % de decisoes de alto impacto (acima do threshold configurado) com Decision Journal Entry criada ANTES do resultado ser conhecido — baseline tipico < 10%, meta > 80% em 60 dias de operacao
- Taxa de postmortem completado: % de decisoes que atingiram a janela de revisao (30/90/180 dias) e tiveram postmortem estruturado realizado — meta > 70% das decisoes elegíveis revisadas em 6 meses
- Score de calibracao do founder (por tipo de decisao): metrica composta calculada pelo ORACLE — o founder estava correto em que % das premissas declaradas, com que nivel de confianca calibrado? evolucao trimestral esperada de pelo menos 10 pontos percentuais por categoria ativa
- Qualidade de captura (SENTINEL-DJ): % de entries aprovadas sem ressalvas na primeira passagem — meta > 85%; % de entries com premissas especificas e criterio de validacao observavel — meta > 90%
- Velocidade de captura: tempo medio entre a tomada da decisao e a criacao da entry no journal — meta < 24h para decisoes de alto impacto, < 72h para media
- Taxa de atualizacao do Calibration Corpus: numero de premissas testadas adicionadas ou atualizadas por mes com base em postmortems concluidos — indicador de saude do loop de aprendizado do clone
- Integridade do journal: numero de violacoes de imutabilidade detectadas pelo SENTINEL-DJ — meta: zero; qualquer edicao retroativa detectada e alertada e documentada para auditoria
- Utilidade dos alertas do RADAR: % de alertas de premissa enviados ao founder que foram classificados por ele como RELEVANTE ou ACIONAVEL — meta > 65% (evitar fadiga de notificacao)
- Score de aderencia do Red-Team (MIRROR): % de Red-Team Reports do SKEPTIC classificados como GENUINAMENTE DESAFIADOR pelo MIRROR — meta > 80% (evitar que o SKEPTIC vire validador complacente)

## Integrações

- Slack (MCP): canal principal de captura conversacional pelo ARCHIVIST, entrega de Red-Team Reports pelo SKEPTIC, alertas do RADAR, notificacoes de postmortem pendente — inbox central do VERDICT para o squad
- WhatsApp Business API: canal de alta urgencia para alertas L3 do SENTINEL-DJ (violacao de imutabilidade), sinais CRITICOS do RADAR, e aprovacoes do CALIBRADOR para atualizacoes de corpus — founder responde APROVAR/REJEITAR diretamente
- Notion (MCP): repositorio primario do Decision Journal — database estruturado com todas as entries, postmortems vinculados, Calibration Corpus e Calibration Briefs mensais. Schema rigido com campos imutaveis (pre-resultado) e campos de postmortem separados
- ClickUp (MCP): prova de trabalho verificavel — cada decisao e uma task com status (Capturada / Red-Team Feito / Monitorando / Postmortem Pendente / Calibracao Aplicada / Concluida), subtasks por agente, historico de outputs e timestamps de cada etapa do ciclo
- Gmail / Google Workspace (MCP): monitoramento de emails estrategicos pelo RADAR (sinais de resultado de decisoes abertas), ingestao de documentos e comunicacoes para o ARCHIVIST em decisoes identificadas via email
- HubSpot / CRM (MCP): fonte de metricas de resultado para decisoes relacionadas a vendas, pipeline, contratacoes de vendas e expansao de contas — RADAR conecta resultados de CRM a premissas abertas do journal
- EXA MCP (via Docker): busca web em tempo real para o SCOUT (base rates, benchmarks) e o RADAR (sinais externos de premissas de mercado) — toda afirmacao vem com citacao de fonte
- Apify (via Docker): scraping de relatorios setoriais, benchmarks de VCs, estudos de caso e publicacoes de mercado para o SCOUT — fontes estruturadas para base rates de premissas
- Langfuse (OTEL): observabilidade completa — tracing de cada ciclo de decisao (captura → red-team → monitoramento → postmortem → calibracao), score de qualidade do MIRROR por etapa, custo de tokens por tipo de decisao, latencia de cada worker, quality gates por ambiente (dev 70% / staging 85% / prod 95% task success)
- LangGraph / Claude Agent SDK: orquestracao stateful do pipeline de decisao — controle de estado por decision ID ao longo de meses (uma decisao pode estar em monitoramento por 180 dias), paralelismo do SKEPTIC + SCOUT para red-team, retry logic para falhas de captura
- Supabase (pgvector): base vetorial para busca semantica de decisoes analogas — quando o ORACLE analisa um postmortem, busca os 5 casos mais similares do historico para analise de padroes; tambem para o SKEPTIC identificar decisoes passadas com premissas similares e seus outcomes

## Entregável (prova de trabalho)

Pacote do Decision Intelligence System — conjunto de artefatos verificaveis e auditaveis: (1) Decision Journal Ativo no Notion — database estruturado com todas as entries, premissas declaradas com timestamp imutavel, Red-Team Reports vinculados, status de cada decisao no ciclo, postmortems associados e links para evidencias de resultado; (2) Calibration Corpus do Founder — banco de premissas testadas com historico de acerto/erro, nivel de confianca calibrado por contexto e referencia ao postmortem de origem; cada entrada e dado de treino de alta qualidade para o clone; (3) Calibration Brief Mensal — relatorio executivo de 1 pagina: score de calibracao do mes por categoria de decisao, top 3 aprendizados com implicacoes acionaveis, evolucao do julgamento vs historico, vieses mais ativos e plano de melhoria; (4) Dashboard de Cobertura no ClickUp — tasks por decisao com pipeline visual: Capturada / Red-Team / Monitorando / Postmortem Pendente / Calibracao Aplicada, com SLA de cada etapa e historico de outputs por agente; (5) Relatorio de Integridade Semanal (SENTINEL-DJ) — taxa de cobertura, decisoes nao capturadas identificadas, violacoes de imutabilidade, score de qualidade das entries; (6) Painel Langfuse — observabilidade em tempo real de custo por ciclo de decisao, latencia por agente, quality gates e score do MIRROR por tipo de postmortem.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Genius Athena Strange (5 agentes, decisao sob incerteza) — logica de arvore de decisao, pre-mortem estruturado e desafio de premissas aplicavel diretamente ao SKEPTIC; framework de separacao de processo vs resultado (Thinking in Bets) e calibracao de confianca por claim reutilizavel como base do ORACLE
- Skeptic Protocol (5 agentes, red-team/QA) — arquitetura de verificacao adversarial e checagem de claims com citacao de fonte diretamente aplicavel ao SKEPTIC e ao MIRROR; padrao de challenge-response estruturado e scoring de solidez de argumento reutilizavel para o red-team de premissas
- Athenaeum (11 agentes, inteligencia estrategica) — modulo de pesquisa paralela com proveniencia de fontes aplicavel ao SCOUT para base rates setoriais; padrao de sintese hierarquica com grau de confiabilidade por claim reutilizavel para o relatorio de benchmarks

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F2 · TopSquad de Performance, KPIs & Calibração de Decisões** — Pergunte aos dados, acompanhe as metas e calibre o próprio julgamento ao longo do tempo.

- **Missão:** O squad que mede e aprende: responde perguntas em linguagem natural sobre os dados, monitora KPIs/OKRs com alertas, e registra decisões + postmortems para calibrar o julgamento do founder ao longo do tempo.
- **Por que consolidar:** Os três giram o mesmo ciclo: medir (analytics), comparar com a meta (KPI/OKR) e refletir sobre a decisão (journal). O KPI Pulse lê os mesmos dados do analytics; o decision journal precisa do resultado dos KPIs para o postmortem. Unidos, formam um loop fechado de decisão informada → resultado medido → aprendizado.
- **Squads irmãos:** Agentic Analytics (Pergunte aos Seus Dados), KPI/OKR Pulse, Decision Journal & Postmortem

## Estrutura

```
founder-decision-journal-postmortem/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
