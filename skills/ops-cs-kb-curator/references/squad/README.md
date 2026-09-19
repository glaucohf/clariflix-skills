# KB Curator Squad

> Sua base de conhecimento nunca mais fica velha: o KB Curator detecta gaps, escreve artigos e resolve conflitos antes que o cliente perceba.

**Área:** Operações & CS · **TopSquad:** O2 Qualidade, Voz do Cliente & Knowledge Base · **Prioridade:** must‑have · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

A base de conhecimento envelhece silenciosamente: tickets sem resposta se acumulam, agentes de IA alucinam por falta de fonte e atendentes humanos recebem escalonamentos evitáveis. O KB Curator le cada ticket não resolvido pela KB, identifica a intenção não coberta, gera ou atualiza o artigo correspondente, detecta contradições entre documentos e sinaliza conflitos para revisão. Alimenta diretamente o Tier-1 Resolver com cobertura verificada.

## Impacto esperado

Redução de 40-60% em tickets escalonados por falta de documentação (base: 20-30% dos tickets sem fonte confirmada). Taxa de resolução no Tier-1 sobe de 55% para 80%+ com KB atualizada. Estimativa de ROI: cada ponto percentual de redução de escalonamento economiza 8-15h/mês de atendente sênior. Em 6 meses, payback total do investimento no squad. KPI âncora: cobertura da KB (% de intenções com artigo) saindo de 55% para 90%+.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `kael` · Kael | Kael — O Curador-Chefe | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `milo` · Milo | Milo — O Pesquisador de Contexto | L1 · worker autônomo | `extrair-intencoes-nao-cobertas.md` |
| `vera` · Vera | Véra — A Escritora de Artigos | L2 · orquestra / decide | `escrever-artigo-de-kb.md` |
| `lex` · Lex | Lex — O Revisor de Qualidade | L2 · orquestra / decide | `validar-draft.md` |
| `clio` · Clio | Clio — A Verificadora de Consistência | L1 · worker autônomo | `verificar-consistencia-documental.md` |
| `petra` · Petra | Petra — A Monitora de Impacto | L1 · worker autônomo | `monitorar-impacto-artigos.md` |
| `arco` · Arco | Arco — O Archivista de Versoes | L0 · worker determinístico | `controlar-versao-artigo.md` |
| `lex-2` · Lex 2 | Lex — O Revisor de Qualidade | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-kb-curator:kael` (ou instale via `npx squads add ./ops-cs-kb-curator`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-kb-curator-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Publicação de artigo novo ou update em produção: Kael agrega o pacote (artigo + gap de origem + diff + scores do Lex + badge do Clio) e envia para aprovação humana via ClickUp task com preview. SLA de resposta: 24h. Se não aprovado em 24h, artigo fica em staging e Kael notifica no Slack.
- L3 — Deprecação de artigo existente: Clio detecta artigo órfão ou conflitante que deve ser removido. Requer aprovação explícita do gestor de CS antes de despublicar.
- L3 — Resolução de conflito entre artigos: quando Clio identifica contradição direta entre dois artigos e não consegue determinar automaticamente qual é a fonte de verdade (ex: ambos recentes, ambos com alto uso), escala para SME humano com Conflict Report estruturado.
- L2 — Reescrita após 2 iterações Lex/Véra: se após dois ciclos de revisão o artigo não atingiu score mínimo (7/10 em compliance e acionabilidade), Kael escala para editor humano com histórico completo das iterações.
- L1 — Validação do Gap Priority Report semanal: Milo gera o ranking de gaps, humano (CS lead) confirma ou reordena as prioridades antes do ciclo de produção começar. Não bloqueia execução, mas calibra o roadmap da KB.

## KPIs

- Cobertura da KB: % de intenções identificadas nos tickets com artigo correspondente (meta: 55% -> 90% em 6 meses)
- Taxa de resolução Tier-1 com fonte KB: % de tickets resolvidos pelo agente IA citando artigo da KB (meta: 55% -> 80%+)
- Redução de tickets escalonados por falta de documentação: tickets/mês sem fonte (meta: -50% em 90 dias)
- Taxa de artigos aprovados no primeiro ciclo HITL: % de artigos que passam em L3 sem revisão adicional (meta: > 75%)
- Tempo médio gap-to-published: horas entre detectar gap e artigo em produção (meta: < 48h para gaps críticos, < 7 dias para gaps normais)
- Resolução pós-publicação: % de tickets com intenção equivalente resolvidos na semana seguinte ao artigo (meta: > 70% por artigo)
- Taxa de conflitos detectados antes da publicação: % de contradições flagradas pelo Clio antes do HITL vs. descobertas pós-publicação (meta: > 90% pré-publicação)
- Score medio de qualidade Lex: media dos scores de aprovacao por dimensao (meta: > 8.0/10 em compliance e acionabilidade)

## Integrações

- Zendesk / Intercom — fonte primária de tickets sem match KB, webhooks de feedback de resolução do Tier-1, tags de intenção
- ClickUp — task por artigo (prova de trabalho), status do pipeline (Gap Identified -> Draft -> QA -> HITL -> Published -> Monitored), integracao com AIOX
- Confluence / Notion / GitBook / Freshdesk KB — destino de publicação dos artigos (configurável por cliente), API de CRUD de artigos
- Supabase / Postgres — estado do pipeline (gap_id, artigo_id, versão, scores, status), vetorização da KB (pgvector), log de aprovações HITL
- Slack — notificações de HITL pendente, alertas de artigo em estado CRÍTICO (Petra), resumo semanal do Impact Report para canal #kb-updates
- OpenAI Embeddings / Anthropic Claude — geração de embeddings da KB para similarity search, geração de drafts (Vera), fact-check (Lex)
- Langfuse — tracing de cada ciclo de produção (gap -> draft -> revisões -> publicação), evals automatizados por dimensão, quality gates (dev 70% / staging 85% / prod 95% task success)
- Tier-1 Resolver (squad interno) — recebe atualizações da KB via webhook pós-publicação, envia sinal KB_NÃO_RESOLVEU para Petra

## Entregável (prova de trabalho)

Pacote de publicação por artigo (prova de trabalho): (1) artigo publicado na KB no formato padrão, (2) Gap Card vinculado — ticket(s) de evidência + intenção identificada + volume impactado, (3) Lex QA Report — scores por dimensão + veredicto, (4) Clio Conflict Badge — LIMPO ou CONFLITO_RESOLVIDO, (5) ClickUp task fechada com histórico completo do ciclo (agentes, timestamps, iterações), (6) baseline de resolução pré-publicação para comparação pelo Petra na semana seguinte.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 ag) — arquitetura de detecção de anomalias e validação de qualidade diretamente aplicável ao pipeline de verificação de consistência da KB (Clio). Reutilizar o padrão de cross-check e conflict detection.
- Skeptic Protocol (5 ag, red-team/QA) — padrao de critic/verifier multi-dimensao reutilizavel diretamente no Lex. O protocolo de 5 dimensoes de validacao e o loop de reescrita (max 2 iteracoes) espelham o Skeptic Protocol.
- Apex Context Supreme (5 ag, context engineering) — técnicas de compressão e retrieval de contexto para o Milo ao trabalhar com grandes volumes de tickets e KB vetorizada. Otimiza o custo de embedding search em bases grandes.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O2 · TopSquad de Qualidade, Voz do Cliente & Knowledge Base** — Audita 100% das conversas, ouve o que o cliente sente e devolve isso à base.

- **Missão:** A camada de aprendizado da operação: audita 100% das conversas (não amostra), extrai sentimento e tendências da voz do cliente, e converte tudo em atualizações da base de conhecimento. Fecha o loop qualidade → insight → conhecimento.
- **Por que consolidar:** Os três processam o mesmo material — as conversas de atendimento — para fins encadeados: auditar, entender e documentar. O QA descobre lacunas, a voz do cliente explica o porquê e o KB Curator corrige a fonte. Separados, ninguém fechava o loop; juntos, é um ciclo de melhoria contínua.
- **Squads irmãos:** QA de Conversas 100% (Quality Verifier), Voz do Cliente — Sentimento & Tendências, KB Curator

## Estrutura

```
ops-cs-kb-curator/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
