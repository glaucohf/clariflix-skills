# Board & Investor Relations — Founder Office

> Board packs source-grounded em horas, não dias — cada número rastreável a uma fonte, cada narrativa alinhada à tese.

**Área:** Founder Office · **TopSquad:** F5 Investor Relations, Fundraising & M&A · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Preparar um board pack ou investor update consome 2–4 dias de trabalho manual por ciclo: coletar métricas de 5–8 fontes distintas, consolidar em narrativa coerente, revisar inconsistências e alinhar o story com a tese da rodada. O risco de números divergentes entre slides, relatório financeiro e email de update destrói credibilidade com investidores. Mensurável por: horas de preparo por ciclo (baseline: 16–32h manual) e % de afirmações com fonte rastreável no artefato (baseline: <30% na maioria dos board packs produzidos manualmente).

## Impacto esperado

Redução do ciclo de produção de board pack de 16–32h para 2–4h (economia de 14–28h por ciclo, ~12 ciclos/ano = 168–336h anuais do founder/CFO recuperadas). Se hora do founder/CFO vale R$800–2.000, ROI direto: R$134k–672k/ano em tempo recuperado. Meta de rastreabilidade: 95%+ das afirmações com fonte citada em 60 dias. Redução de rodadas de revisão pré-envio: de 3–5 iterações para 1–2. Credibilidade com board: 100% das métricas reconciliadas entre fontes antes de qualquer envio. Redução de risco de narrativa desalinhada (afirmação em slide x dado real): meta zero inconsistências detectadas pelo board.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `cassidy` · Cassidy | Cassidy — Board Relations Orchestrator | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `rex` · Rex | Rex — Analytics & Metrics Reconciler | L1 · worker autônomo | `reconciliar-metricas.md` |
| `marlowe` · Marlowe | Marlowe — Narrative & Market Context Worker | L1 · worker autônomo | `sintetizar-contexto-mercado.md` |
| `vera` · Vera | Vera — Provenance & Source Integrity Agent | L1 · worker autônomo | `auditar-fontes-primarias.md` |
| `sage` · Sage | Sage — Founder Clone & Narrative Aligner | L1 · worker autônomo | `alinhar-narrativa.md` |
| `quincy` · Quincy | Quincy — Board Q&A Simulator | L1 · worker autônomo | `simular-perguntas-board.md` |
| `cipher` · Cipher | Cipher — Data Room & Versioning Keeper | L0 · worker determinístico | `manter-data-room-atualizado.md` |
| `gate` · Gate | Gate — HITL Compliance & Send Controller | L3 · aprovação humana | `controlar-envio-externo.md` |
| `axiom` · Axiom | Axiom — Verifier, Hallucination Guard & Red-Team Analyst | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-board-investor-relations:cassidy` (ou instale via `npx squads add ./founder-board-investor-relations`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-board-investor-relations-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores
- Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%
- Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)
- Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final
- Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente
- Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa
- Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser refletida no board pack

## KPIs

- Horas de preparo por ciclo de board pack — baseline 16–32h, meta: <4h em 60 dias
- % de afirmações com fonte rastreável no artefato final (Vera score) — meta: 95%+ em 60 dias
- Número de rodadas de revisão pré-envio — baseline 3–5 iterações, meta: 1–2 em 90 dias
- % de métricas reconciliadas sem divergência entre fontes antes do draft (Rex) — meta: 100% em 30 dias
- Score de alinhamento narrativo do Sage (0–10) por ciclo — meta: >=8.5
- Hallucination rate detectado pelo Axiom (claims bloqueados por falta de fonte) — meta: <3% dos claims por ciclo
- Tempo de geração do Q&A Brief do Quincy — meta: <45 minutos end-to-end
- % de perguntas do board previstas corretamente pelo Quincy (validado pelo founder após o meeting) — meta: >=70% das top 10
- Completude do audit trail no data room (Cipher) — meta: 100% dos artefatos enviados arquivados com metadados completos
- Task success rate no Langfuse — meta: dev 70% / staging 85% / prod 95%
- NPS interno do squad avaliado pelo founder após cada ciclo — meta: >=8.5

## Integrações

- Stripe / QuickBooks / Conta Azul (receita, MRR/ARR, burn, runway — fonte primária para Rex)
- HubSpot / Salesforce CRM (pipeline, novos clientes, churn, expansão, CAC — fonte primária para Rex)
- Mixpanel / Amplitude / PostHog (métricas de produto, DAU/MAU, NPS, feature adoption)
- Gupy / Lever / Greenhouse (headcount, hiring, attrition — componente de board pack)
- Captable.io / Carta (cap table, ownership, opções — para seções de governance e rodada)
- Notion (data room estruturado, board packs arquivados, knowledge base do squad)
- Google Drive / Slides (geração e armazenamento de apresentações de board)
- Gmail / Outlook (envio controlado de investor updates via Gate Agent após aprovação HITL)
- Slack (entrega de drafts e alertas ao founder, interface conversacional com Cassidy)
- ClickUp (audit trail de ciclos, tasks de revisão, prova de trabalho do squad)
- WrenAI / Snowflake Cortex (camada semântica governada para text-to-SQL do Rex)
- EXA / Perplexity MCP (deep research externo para Marlowe — benchmarks e contexto de mercado)
- Langfuse (observabilidade OTEL — tracing de tokens, custo por agente, task success rate)
- Vector DB — Pinecone / Qdrant (corpus do founder para Sage, histórico de Source Manifests)
- Sembly / Fireflies (transcrições de board meetings e investor calls para alimentar Quincy e Sage)

## Entregável (prova de trabalho)

Board Pack Cycle Artifact — artefato verificável por ciclo composto de: (1) Board Pack ou Investor Update final em PDF/Notion com 95%+ de claims rastreáveis e Source Manifest anexo; (2) Metrics Table canônica do ciclo (todas as fontes, datas de extração, flags de inconsistência resolvidas); (3) Q&A Brief com top 10 perguntas previstas e respostas preparadas pelo founder; (4) Diff de ciclo (o que mudou vs comunicação anterior em métricas e narrativa); (5) Audit trail completo no ClickUp (versão enviada, aprovador, destinatários, timestamp); (6) Score de rastreabilidade do Axiom por seção. Tudo arquivado no data room com versionamento e auditável pelo board ou due diligence de futura rodada.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base para o pipeline de deep research do Marlowe (context de mercado, benchmarks, comparáveis) e para o modelo de síntese com citações inline do Vera
- Skeptic Protocol (5 agentes, red-team/QA) — base para a arquitetura do Axiom (critic adversarial, hallucination detection, consistency audit cross-seções) e para o Q&A simulation do Quincy
- Data Quality Guardian (5 agentes, qualidade de dados) — base para o pipeline de reconciliação e detecção de divergência entre fontes do Rex e para o modelo de audit trail do Cipher

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F5 · TopSquad de Investor Relations, Fundraising & M&A** — Tudo que toca capital: board, captação e aquisições.

- **Missão:** O squad do capital: gere a relação com board e investidores (updates, comunicação), opera o fundraising (pipeline de investidores, data room) e conduz o screening de due diligence/M&A. Tudo que envolve dinheiro de fora, num motor só.
- **Por que consolidar:** Os três giram em torno do mesmo público — investidores e capital — e da mesma fonte de verdade (métricas, data room, cap table). O update de board usa os mesmos números do fundraising; o due diligence consome o mesmo data room. Separados, mantinham três cópias da verdade financeira; unidos, uma só.
- **Squads irmãos:** Board & Investor Relations, Investor & Fundraising Ops, Due Diligence / M&A Screening

## Estrutura

```
founder-board-investor-relations/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
