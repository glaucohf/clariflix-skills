# Due Diligence / M&A Screening

> Triagem de aquisições em 48h com inteligência de Opus — red flags, tese e memo prontos antes do primeiro call.

**Área:** Founder Office · **TopSquad:** F5 Investor Relations, Fundraising & M&A · **Prioridade:** avançado · **Agentes:** 10 (8 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Triagem manual de targets de M&A consome 3-6 semanas de analistas sênior, custa R$40-120k por target e ainda assim deixa passar red flags críticos que só aparecem no due diligence aprofundado. O squad automatiza 80% da coleta e análise preliminar, reduzindo o ciclo para 48h e elevando a taxa de detecção de red flags materiais de ~55% para >90% antes do primeiro call com o target.

## Impacto esperado

ROI estimado: redução de custo por triagem de R$40k para R$4k (90% de redução). Para um founder que avalia 12 targets/ano, economia de R$432k/ano em fees de assessoria + tempo de equipe. Aumento de velocidade de 6 semanas para 48h = vantagem competitiva em processos disputados. KPI monetário central: % de red flags materiais identificados na fase de screening vs due diligence aprofundado (meta: >90% capturados antes do deep dive pago).

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · Nexus | Nexus — O Estrategista de Aquisições | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `argus` · Argus | Argus — O Detetive de Dados | L1 · worker autônomo | `coletar-dados-abertos.md` |
| `fenix` · Fenix | Fênix — O Analista Financeiro | L1 · worker autônomo | `analisar-metricas-financeiras.md` |
| `themis` · Themis | Themis — A Analista Jurídica | L1 · worker autônomo | `analisar-processos-judiciais.md` |
| `sigma` · Sigma | Sigma — O Analista de Mercado | L1 · worker autônomo | `analisar-mercado-competitivo.md` |
| `atlas` · Atlas | Atlas — O Analista de Tech e Produto | L1 · worker autônomo | `analisar-maturidade-tecnologica.md` |
| `vox` · Vox | Vox — O Analista de Pessoas e Cultura | L1 · worker autônomo | `avaliar-cultura-organizacional.md` |
| `eco` · Eco | Eco — O Clône Estratégico do Founder | L2 · orquestra / decide | `reescrever-tese.md` |
| `columbo` · Columbo | Columbo — O Cético Verificador | L2 · orquestra / decide | `verificar-claims-fontes.md` |
| `columbo-2` · Columbo 2 | Columbo — O Cético Verificador | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-due-diligence-ma-screening:nexus` (ou instale via `npx squads add ./founder-due-diligence-ma-screening`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-due-diligence-ma-screening-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complementa com dados adicionais (especialmente se completude < 60). Criticidade: ALTA — avançar com dados incompletos invalida todo o pipeline.
- HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFIED/DISPUTED para decisão: aceitar o risco e prosseguir, solicitar pesquisa adicional (re-ativa workers específicos), ou cancelar a triagem do target.
- HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20% do valuation estimado, irregularidade fiscal grave) pausa o pipeline e exige confirmação do founder antes de prosseguir. Pode levar ao cancelamento imediato da triagem.
- HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilhamento com advisors, bancos, co-investidores ou o próprio target. Ações irreversíveis (envio externo) sempre requerem aprovação humana explícita.
- HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados pontos. Eco re-executa com instruções específicas. Não é irreversível, mas é um checkpoint de qualidade importante.
- HITL Gate L1 — Configuração Inicial do Target: O founder define a intenção estratégica (por que este target, qual a tese inicial, quais setores/mercados são relevantes) antes do início do pipeline. Isso calibra os pesos do Scorecard e o foco dos workers.

## KPIs

- Targets triados por ciclo mensal (baseline: 2-3 manuais → meta: 8-12 com o squad)
- % de red flags materiais identificados no screening vs due diligence aprofundado (meta: >90%)
- Tempo médio de triagem por target (baseline: 3-6 semanas → meta: 24-48h)
- Custo por triagem em tokens/API (meta: < R$200 por target em custos de infra)
- Score de confianca medio do Columbo por ciclo (meta: > 80 antes de entregar ao founder)
- % de Investment Memos aprovados sem revisão maior pelo founder (meta: > 70% aprovados com ajustes mínimos)
- Taxa de conversão screening → due diligence aprofundado (meta: só targets com score >= 7/12 no Scorecard M&A avançam)
- Redução de custo de assessoria externa por triagem (meta: 90% de redução vs linha de base)
- NPS do founder com o memo (pesquisa pós-entrega, meta: > 8/10)
- Número de red flags Critical corretamente identificados que teriam passado no processo manual (métrica de aprendizado contínuo)

## Integrações

- ClickUp — Gerenciamento de tasks e prova de trabalho: cada triagem e uma task com sub-tasks por agente, status tracking e entrega do artefato final linkado
- Notion / Obsidian — Knowledge base do founder (corpus de decisões, memos anteriores, teses) que alimenta o Eco (Clone Agent)
- Vector DB (Pinecone / Supabase pgvector) — Embeddings do corpus do founder e histórico de triagens anteriores para o Eco e o Columbo aprenderem com cada ciclo
- DataJud (CNJ) — Processos judiciais públicos via API para o Themis
- Receita Federal / CNPJ.info — Dados societários e CNPJ para o Argus
- LinkedIn Sales Navigator — Histórico profissional, tenure de C-level, headcount para Vox e Atlas
- Crunchbase API — Funding history, exits, investors para Fênix e Sigma
- Glassdoor / Blind (scraping) — Cultura e reviews para Vox
- BuiltWith / Wappalyzer — Stack tecnológico para Atlas
- Google News API — Cobertura de mídia para Argus e Vox
- Langfuse — Observabilidade OTEL: tracing de tokens, custo por triagem, latência por agente, task success rate por fase
- Slack — Notificações de status do pipeline ao founder (Target Profile pronto, Deep Dive completo, Memo disponível para revisão, gates L3 aguardando aprovação)
- Gmail / Email — Entrega do Investment Memo final em PDF após aprovacao L3
- INPI — Consulta de patentes e marcas registradas para Themis e Atlas
- BACEN (SCR/API) — Regularidade financeira e dados de crédito para Fenix e Themis

## Entregável (prova de trabalho)

Pacote M&A Screening completo por target: (1) Target Profile v0 JSON (dados normalizados de fontes abertas); (2) 5 Sub-relatorios de workers (Financeiro, Juridico, Mercado, Tech, Pessoas) com claims 100% rastreados; (3) Relatorio de Verificacao do Columbo com score de confianca; (4) Scorecard M&A (12 dimensoes, 0-10); (5) Red Flag Register com severidade e evidencia; (6) Tese de Aquisicao com hipoteses de valor e sinergias; (7) Investment Memo personalizado na voz do founder (PDF + Markdown) com recomendacao Go/Conditional Go/No-Go. Tudo gravado no ClickUp como prova de trabalho e no knowledge base do squad para aprendizado continuo.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 ag, inteligência estratégica) — base de paralelização de workers de pesquisa e síntese estratégica. Reutilizar o padrão de fan-out de workers independentes e consolidação pelo orquestrador, adaptando as 5 trilhas específicas de M&A (Financeiro, Jurídico, Mercado, Tech, Pessoas).
- Skeptic Protocol (5 ag, red-team/QA) — base direta para o Columbo (Critic). O padrão de agente cético que desafia claims, verifica fontes e marca alucinações e o core deste squad. Adaptar o protocolo de verificação para o contexto de M&A (fontes financeiras, jurídicas, competitivas).
- Genius Athena Strange (5 ag, decisão sob incerteza) — base para o layer de síntese e recomendação do Nexus. O padrão de tomada de decisão estruturada sob incerteza (scorecard, tese, recomendação com confiança explicitada) mapeia diretamente para o Investment Memo e o Scorecard M&A.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F5 · TopSquad de Investor Relations, Fundraising & M&A** — Tudo que toca capital: board, captação e aquisições.

- **Missão:** O squad do capital: gere a relação com board e investidores (updates, comunicação), opera o fundraising (pipeline de investidores, data room) e conduz o screening de due diligence/M&A. Tudo que envolve dinheiro de fora, num motor só.
- **Por que consolidar:** Os três giram em torno do mesmo público — investidores e capital — e da mesma fonte de verdade (métricas, data room, cap table). O update de board usa os mesmos números do fundraising; o due diligence consome o mesmo data room. Separados, mantinham três cópias da verdade financeira; unidos, uma só.
- **Squads irmãos:** Board & Investor Relations, Investor & Fundraising Ops, Due Diligence / M&A Screening

## Estrutura

```
founder-due-diligence-ma-screening/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
