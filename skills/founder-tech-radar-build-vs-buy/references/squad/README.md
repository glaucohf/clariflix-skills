# Tech Radar & Build-vs-Buy Intelligence

> Nunca mais pague lock-in com juros — cada decisao de tecnologia e vendor passa pelo crivo sistemico de maturidade, custo total e risco antes de chegar ao founder, transformando escolhas tecnicas em alavancagem estrategica mensuravel.

**Área:** Founder Office · **TopSquad:** F3 Inteligência Competitiva & de Mercado · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Decisoes de tecnologia e selecao de vendors sao tomadas por impulso, urgencia ou recomendacao de terceiros sem interesse alinhado — sem visao sistematica de riscos, custo total de propriedade, maturidade da solucao e alternativas disponiveis. O resultado acumulado e um stack repleto de lock-in nao intencional, divida tecnica oculta e vendors criticos sem alternativa qualificada. Nao existe processo que monitore continuamente a evolucao do ecossistema tecnico (novas solucoes que tornam vendors atuais obsoletos, emergencia de concorrentes open-source de vendors pagos, deprecated frameworks na stack atual), avalie sistematicamente o tradeoff build-vs-buy para cada decisao de componente relevante, e produza recomendacoes rastreavais com criterios explicitos para o founder ou CTO aprovar. Mensuravel por: (1) numero de decisoes de tech e selecao de vendor no trimestre que foram embasadas por Tech Radar ou Build-vs-Buy Analysis — meta 100% das decisoes de alto impacto versus baseline tipico abaixo de 20%; (2) percentual de vendors criticos com risco avaliado (lock-in score, alternativas mapeadas, custo de migracao estimado) — meta 100% de Tier 1 e Tier 2 versus baseline tipico inferior a 30%; (3) indice de divida tecnica oculta — quantidade de componentes na stack com score de maturidade abaixo de threshold sem plano de substituicao versus componentes com plano documentado. O squad funciona como um Chief Architect e Technology Intelligence Officer dedicado ao founder: monitora continuamente o ecossistema tecnico relevante, alimenta um Tech Radar vivo com quadrantes de Adopt/Trial/Assess/Hold, executa Build-vs-Buy Analysis rigorosa para cada decisao de componente acima de threshold de criticidade, e entrega recomendacoes acionaveis com evidencias rastreavels — nao 'achismos' de CTO que chegou semana passada.

## Impacto esperado

Empresas que operam sem processo sistematico de Tech Radar e avaliacao de vendor acumulam lock-in e divida tecnica que representa tipicamente 20-40% do custo de desenvolvimento em retrabalho e integracao nao planejada. Para uma empresa com time tecnico de 5-10 engenheiros, isso equivale a R$300k-R$900k/ano de capacidade desperdicada em manutencao de escolhas ruins do passado. Alem do custo direto de retrabalho, decisoes de vendor sem avaliacao sistematica de lock-in criam dependencias de alto custo de saida: substituir um ERP ou CRM mal selecionado em producao custa tipicamente 3-5x o custo de selecao cuidadosa anterior. Uma unica decisao de build errada (construir internamente o que existe como produto maduro no mercado) representa 6-18 meses de desenvolvimento desperdicado — custo de oportunidade entre R$500k e R$2M para times medios. O squad opera como um departamento de Technology Intelligence a custo de R$5-12k/mes versus Head of Architecture senior (R$25-40k/mes CLT) que ainda assim nao tem acesso ao ecossistema de inteligencia continua que o squad fornece. ROI direto mensuravel: (1) cada Build-vs-Buy Analysis que resulta em escolha 'Buy' para componente que levaria 4 meses de build representa R$200-400k em custo de oportunidade preservado; (2) cada lock-in evitado por Tech Radar Assess/Hold em vendor critico preserva tipicamente R$100-500k em custo futuro de migracao forcada; (3) reducao de 60-80% no tempo de due diligence tecnica de novas ferramentas (de semanas para dias) libera tempo do founder e CTO para decisoes de maior valor. Meta de ROI declarado para o cliente: o squad se paga integralmente se evitar um unico lock-in de vendor ou uma unica decisao de build incorreta no primeiro semestre de operacao.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `lens` · Lens | Lens — Oraculo de Tecnologia & Estrategia | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `nox` · Nox | Nox — Cartografo do Stack & Tech Radar Keeper | L2 · orquestra / decide | `manter-tech-radar-atualizado.md` |
| `vera` · Vera | Vera — Scout de Ecossistema Tecnico | L2 · orquestra / decide | `monitorar-ecossistema-tecnico.md` |
| `kai` · Kai | Kai — Arquiteto de Decisoes Build-vs-Buy | L2 · orquestra / decide | `analisar-decisoes-tecnologicas.md` |
| `vox` · Vox | Vox — Founder Clone Tech Advisor | L1 · worker autônomo | `responder-perguntas-tecnicas.md` |
| `aegis` · Aegis | Aegis — Assessor de Risco de Vendor & Compliance | L2 · orquestra / decide | `avaliar-risco-vendor.md` |
| `aria` · ARIA | ARIA — Adversarial Risk Intelligence Assessor | L3 · aprovação humana | `avaliar-riscos-tecnologicos.md` |
| `gaia` · Gaia | Gaia — HITL Gate & Decision Registry | L3 · aprovação humana | `registrar-decisao-tecnica.md` |
| `aria-2` · ARIA 2 | ARIA — Adversarial Risk Intelligence Assessor | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-tech-radar-build-vs-buy:lens` (ou instale via `npx squads add ./founder-tech-radar-build-vs-buy`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-tech-radar-build-vs-buy-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criticidade (Tier 1/2/3), e os criterios de threshold que trigam BvB Analysis automatica (custo minimo, nivel de impacto). Gate L3 obrigatorio — sem esta aprovacao o squad nao opera em producao. Define o escopo de toda a operacao
- Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/Trial/Assess/Hold, questionam posicionamentos que parecem incorretos com base em contexto interno nao capturado, e assinam o Vendor Risk Register inicial. Gate L3 — este documento se torna a linha de base de toda decisao futura
- Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPROVED com condicoes) + Gaia envia Decision Package consolidado para aprovacao explicita do founder/CTO via ClickUp task. Irreversivel por natureza: contratos assinados, integracao implementada e dados migrados sao difficeis e caros de desfazer
- Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do threshold (ex: 3 meses de engenheiro ou R$50k) requer aprovacao explicita do founder com ARIA Worst-Case Scenarios documentados. Irreversivel: capacidade de engenheiro desviada nao pode ser recuperada
- Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology Roadmap Recommendations para os proximos 2 trimestres. Gate L3: founder/CTO aprovam as recomendacoes antes de se tornarem diretriz tecnica do squad. Incluido no calendario de governanca do founder
- Revisao de Vendor Risk Alerts gerados por Aegis para vendors Tier 1 ativos — quando Aegis detecta mudanca em ToS, DPA ou historico de incidente de seguranca em vendor Tier 1 ativo, Gaia cria gate L3 com prazo de 48h para o founder revisar e decidir: aceitar o risco com registro formal, iniciar due diligence adicional, ou triggar BvB Analysis de substituicao
- Aprovacao de movimentos de quadrante com impacto em sistemas Tier 1 — quando Nox propoe mover componente Tier 1 para HOLD ou Tier 1/2 para ADOPT, gate L2 (CTO pode aprovar autonomamente) ou L3 (requer founder quando envolve custo ou risco acima de threshold) antes do movimento ser registrado como decisao oficial
- Conditions Review Reminder de Gaia — quando as condicoes de revisao de um ADR sao atingidas (preco do vendor ultrapassou threshold, data de revisao chegou, Lock-in Score mudou apos renegociacao contratual), Gaia dispara gate L1 para o founder confirmar ciencia e decidir se aciona nova BvB Analysis ou mantem decisao anterior com registro atualizado

## KPIs

- Cobertura de decisoes tecnicas embasadas por radar: percentual de decisoes de tech e selecao de vendor de alto impacto no trimestre que tiveram BvB Analysis e/ou posicionamento no Tech Radar como input formal — meta 100% das decisoes Tier 1 versus baseline tipico abaixo de 20%
- Percentual de vendors Tier 1 com risco avaliado: percentual do Vendor Risk Register Tier 1 com Vendor Risk Assessment completo de Aegis e Lock-in Score atualizado nos ultimos 90 dias — meta 100% de Tier 1 e 80% de Tier 2
- Latencia de URGENT Alert: tempo entre Vera detectar CVE critico, EOL ou mudanca de preco acima de 30% em vendor Tier 1 e o alerta chegar ao founder via Slack — meta abaixo de 4h (SLA de deteccao e notificacao)
- Taxa de aprovacao de BvB Analyses sem revisao de ARIA: zero tolerancia — 100% das BvB Analyses de Tier 1 devem passar pelo gate de ARIA antes de entrega ao founder. KPI de processo nao de qualidade — qualquer analise entregue sem gate de ARIA e violacao do protocolo
- Qualidade de premissas de TCO: percentual de premissas de TCO de BvB Analyses historicas que se materializaram dentro de +/- 30% do estimado versus o que realmente aconteceu — revisado trimestralmente pelo ciclo de aprendizado de ARIA. Meta acima de 70% de premissas dentro da banda de 30%
- Tech Radar Freshness Score: percentual de componentes do Tech Radar com avaliacao atualizada nos ultimos 90 dias (pelo menos um sinal processado por Vera, mesmo que a posicao nao tenha mudado) — meta 100% de Tier 1, 80% de Tier 2
- Decisoes de lock-in evitadas: numero de componentes movidos para HOLD pelo Tech Radar com plano de migracao formalmente aprovado versus componentes que foram forcados a migrar de emergencia por problema de vendor (crise de lock-in nao antecipada) — meta de zero migracoes emergenciais nao antecipadas no trimestre
- Technology Decision Log completeness: percentual de decisoes tecnicas de Tier 1 implementadas nos ultimos 12 meses que tem ADR registrado no Technology Decision Log com todas as secoes obrigatorias preenchidas — meta 100%
- Tempo de BvB Analysis para decisoes prioritarias: tempo entre Lens triggar BvB Analysis urgente (decisao ad-hoc de alta urgencia) e entrega do Decision Package completo (Kai + Aegis + ARIA) ao founder — meta abaixo de 72h para decisoes prioritarias, 10 dias uteis para analises regulares

## Integrações

- ClickUp — prova de trabalho central: tasks de aprovacao de gates HITL com deadlines e artefatos anexados, Tech Radar Changelog como documento vivo, BvB Analysis Reports linkados a tasks de decisao, Technology Decision Log como pasta de ADRs, dashboard de vendor risk por tier e status de aprovacao
- Notion — repositorio de conhecimento do squad: Tech Radar Diagram embeddado (formato SVG/JSON atualizado mensalmente), Vendor Risk Register completo, Technology Decision Log (ADRs), Tech Strategy Quarterly Reports, Corpus do Founder Tecnico (base de Vox), BvB Analyses historicas com outcomes
- Slack — canal #tech-radar-decisions para: URGENT Alerts de Vera (CVE critico, EOL, mudanca de preco acima de 30%), gates HITL para aprovacao de decisoes criticas, Tech Radar Monthly Update toda primeira segunda-feira do mes, notificacoes de Compliance Monitoring de Aegis
- GitHub (via MCP ou webhook) — monitoramento de releases e changelogs de todos os frameworks e bibliotecas open-source no stack (Vera), deteccao de Issues criticas em repositorios de dependencias, monitoramento de velocidade de contribuicao e saude da comunidade como indicador de maturidade
- Crunchbase (API ou scraping via Apify) — monitoramento de saude financeira de vendors Tier 1 e Tier 2: novas rodadas de investimento, aquisicoes, mudancas de lideranca, sinais de runway critico
- Product Hunt — deteccao de launches de novos produtos em categorias tecnicas monitoradas (alternativas emergentes a vendors atuais, novas ferramentas em categorias de ASSESS)
- G2 / Capterra (scraping via Apify) — monitoramento de reviews de vendors no Vendor Risk Register para detectar degradacao de suporte, mudancas de preco percebidas por clientes, problemas recorrentes reportados
- Hacker News (API) — posts com 100+ points sobre ferramentas tecnicas monitoradas (criticas de vendors, lancamentos relevantes, deprecacoes de frameworks, casos de lock-in documentados por outros founders/CTOs)
- Langfuse — observabilidade OTEL completa: tracing de custo e tokens por agente, quality gates (dev 70% / staging 85% / prod 95% task success), latencia de entrega de BvB Analyses e URGENT Alerts, evals de qualidade de recomendacoes de Kai versus outcomes reais, custo por analise gerada
- n8n — orquestracao de workflows de monitoramento: crons de Vera por tier e frequencia, webhooks de mudanca em paginas de preco e changelogs, roteamento de sinais classificados entre agentes, agendamento de ciclos mensais e trimestrais
- Apify (via MCP Docker) — scraping estruturado de: paginas de preco de vendors (diff automatico para detectar mudancas), job postings de vendors monitorados (sinais de crescimento ou crise), reviews em G2/Capterra/Reclame Aqui, blog posts e changelogs de vendors sem RSS, perfis publicos de founders de vendors para sinais de estrategia
- EXA (via MCP Docker) — pesquisa web para: due diligence de vendors em processo de avaliacao por Aegis (historico de incidentes, litigios, press coverage), background de novas ferramentas em ASSESS identificadas por Vera, benchmarks de TCO por categoria para calibrar estimativas de Kai
- Linear / Jira (opcional) — sincronizacao de items do Tech Radar HOLD com issues de divida tecnica no backlog de engenharia, tasks de BvB Analysis linkadas ao roadmap tecnico do time, tracking de progresso em migracoes de componentes aprovadas

## Entregável (prova de trabalho)

Tech Radar Monthly Pack entregue na primeira segunda-feira de cada mes no ClickUp (task fechada por Lens com todos os artefatos anexados) e no canal Slack #tech-radar-decisions, contendo: (1) Tech Radar Diagram atualizado — versao SVG do mes com todos os movimentos de quadrante destacados versus versao anterior, exportavel e embed-ready para Notion/Confluence; (2) Tech Radar Changelog do mes — lista completa de movimentos de quadrante com item, quadrante anterior, quadrante novo, justificativa em 2-3 frases e link para artefatos de suporte; (3) Vendor Risk Register update — Lock-in Score e Vendor Health Score atualizados para todos os Tier 1, novos Vendor Risk Assessments de Aegis concluidos no mes, Red Flags identificados; (4) BvB Analyses concluidas no mes — lista de todas as analises finalizadas com recomendacao, veredicto de ARIA, status de aprovacao do founder e ADR criado por Gaia; (5) Ecosystem Signals Summary — top 10 sinais de Vera do mes por relevancia (CVEs criticos, EOLs, mudancas de preco, alternativas emergentes promissoras); (6) URGENT Alerts do mes — lista de todos os alertas criticos disparados, canal de entrega, tempo de resposta do founder e acao tomada; (7) Quality Metrics do mes — cobertura do radar, latencia media de alert, taxa de premissas de TCO validadas, custo por analise (via Langfuse). ADICIONAL TRIMESTRAL: Tech Strategy Quarterly com Technology Roadmap Recommendations e gate L3 do founder. SOB DEMANDA: BvB Analysis Report prioritario com Decision Package consolidado e gate HITL via Gaia. Artefato verificavel: task no ClickUp com numero sequencial, timestamp de entrega, assinatura digital de Lens e links para todos os documentos — rastreavel por mes, por componente e por tipo de decisao.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligencia estrategica) — base direta para a arquitetura de coleta e sintese de Vera (Scout de Ecossistema): o pipeline de ingestao de multiplas fontes heterogeneas, classificacao por relevancia e producao de briefings hierarquizados ja implementado pode ser customizado para monitoramento de ecossistema tecnico em vez de inteligencia de mercado, reduzindo significativamente o tempo de setup de Vera e de Nox para o Tech Radar Changelog
- Skeptic Protocol (5 agentes, red-team/QA) — acelera a construcao de ARIA (Adversarial Risk Intelligence Assessor): o framework de questionamento adversarial, deteccao de premissas inflatadas e exigencia de cenarios alternativos ja estruturados pode ser adaptado para o contexto especifico de decisoes tecnicas, com enfase em Worst-Case TCO e lock-in scenarios em vez de claims genericos
- Genius Athena Strange (5 agentes, decisao sob incerteza) — base para o modo de Decision Prep de Vox (Founder Clone Tech Advisor): o framework de raciocinio estruturado sob incerteza, consideracao de alternativas e construcao de cenarios de decisao ja implementados acelera a customizacao do agente de clone cognitivo para o contexto tecnico especifico do founder

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F3 · TopSquad de Inteligência Competitiva & de Mercado** — Onde estão as oportunidades, os concorrentes e as tecnologias que importam.

- **Missão:** O radar externo do founder: monitora concorrentes continuamente, dimensiona mercados e detecta oportunidades, e mantém um tech radar com decisões de build-vs-buy. A inteligência de "onde jogar" e "com o quê".
- **Por que consolidar:** Os três escaneiam o ambiente externo por lentes que se cruzam: concorrente, mercado e tecnologia. O tech radar informa o build-vs-buy que depende do tamanho do mercado que depende do que o concorrente faz. Separados, repetiam a varredura externa; juntos, um radar estratégico único.
- **Squads irmãos:** Inteligência Competitiva Contínua, Market Sizing & Opportunity Scout, Tech Radar & Build-vs-Buy

## Estrutura

```
founder-tech-radar-build-vs-buy/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
