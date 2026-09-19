# Squad de Inteligência de Conta e Battlecards

> Seu vendedor entra na reunião sabendo mais sobre o prospect do que ele mesmo.

**Área:** Vendas · **TopSquad:** V5 Sales Enablement & Conversation Intelligence · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Vendedores entram em reuniões despreparados — sem contexto da conta, sem mapeamento de stakeholders, sem conhecer os concorrentes em jogo nem as dores específicas do setor. A pesquisa manual consome 2-4 horas por conta e ainda fica incompleta, fragmentada entre LinkedIn, site, notícias e CRM. O resultado é um discurso genérico que não ressoa, perda de credibilidade e taxa de avanço de deal abaixo do potencial.

## Impacto esperado

Redução de 80-90% no tempo de preparo por reunião (de 2-4h para 15-20 min de revisão humana). Aumento estimado de 25-40% na taxa de avanço de deal (discovery-to-proposal) pela personalização do discurso. Para uma operação com 5 vendedores fazendo 4 reuniões/semana, isso representa 100-160h/mês recuperadas e convertidas em mais reuniões ou fechamentos. ROI estimado: 8-15x sobre o custo do squad no primeiro trimestre de operação em full-scale.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · NEXUS | NEXUS — O Estrategista de Conta | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `scout` · SCOUT | SCOUT — O Investigador de Empresa | L1 · worker autônomo | `investigar-empresa-completa.md` |
| `iris` · IRIS | IRÍS — A Mapeadora de Stakeholders | L1 · worker autônomo | `mapear-stakeholders.md` |
| `warfare` · WARFARE | WARFARE — O Especialista em Battlecards | L1 · worker autônomo | `montar-battlecard-competitiva.md` |
| `oracle` · ORACLE | ORACLE — O Analista de Sêtor e Dores | L0 · worker determinístico | `analisar-dores-setoriais.md` |
| `herald` · HERALD | HERALD — O Formatador e Entregador | L2 · orquestra / decide | `entregar-artefatos-formatados.md` |
| `memoria` · MEMORIA | MEMÓRIA — O Gestor de CRM e Histórico | L3 · aprovação humana | `persistir-contexto-no-crm.md` |
| `sentinel` · SENTINEL | SENTINEL — O Verificador de Inteligência | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-inteligencia-conta-battlecards:nexus` (ou instale via `npx squads add ./vendas-inteligencia-conta-battlecards`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-inteligencia-conta-battlecards-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM de produção
- L3 — Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio automático sem leitura humana
- L2 — Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta o que não se aplica
- L1 — Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão parcial ou aguardar correção
- L1 — Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes de qualquer ação

## KPIs

- Tempo de geracao do dossie completo: meta < 8 minutos do disparo ao entregavel validado pelo SENTINEL
- Taxa de aprovação do SENTINEL na primeira passagem: meta > 85% (staging) / > 95% (produção)
- Tempo de preparo do vendedor (pesquisa manual eliminada): redução de 2-4h para 15-20 min de revisão — medido por survey quinzenal com o time de vendas
- Taxa de avanco de deal pos-uso do dossie: comparar deals com dossie vs sem dossie no CRM — meta +25% de discovery-to-proposal
- Cobertura de reuniões: % de reuniões que tiveram dossiê gerado e entregue antes do horário — meta > 90%
- Frescor dos dados: % de informações no dossiê com fonte datada nos últimos 90 dias — meta > 80%
- Adesão do vendedor: % de vendedores que abriram o dossiê antes da reunião (tracking de abertura) — meta > 75%
- Enriquecimento de CRM pelo MEMÓRIA: % de campos críticos preenchidos após cada reunião — meta > 70% de completude por conta

## Integrações

- CRM: HubSpot (MCP disponível) ou Pipedrive — leitura de histórico e escrita de atualizações via MEMÓRIA
- Calendário: Google Calendar ou Outlook (MCP) — leitura de reuniões agendadas para disparo automático do pipeline
- LinkedIn: Clay ou Apollo para enriquecimento de perfis de stakeholders (IRIS)
- Dados de empresa: Apollo.io (275M+ contatos e firmografia), Clearbit Enrichment (SCOUT)
- Stack tecnológica: BuiltWith API ou Wappalyzer (SCOUT — detecção de tecnologias do prospect)
- Notícias e sinais: Google News API, RSS feeds setoriais (SCOUT e ORACLE)
- ClickUp: gestão de tarefas e armazenamento de artefatos como prova de trabalho verificável (HERALD)
- Slack: notificação push do dossiê finalizado ao vendedor (HERALD)
- WhatsApp Business API: entrega alternativa do resumo executivo para vendedores mobile-first (HERALD)
- Observabilidade: Langfuse (OTEL) — rastreamento de cada execução, latência por worker, taxa de aprovação do SENTINEL, quality gates por ambiente
- Orquestração: LangGraph ou Claude Agent SDK — controle de estado do pipeline, paralelismo dos workers, retry logic
- Armazenamento de battlecards: base vetorial (Supabase pgvector ou Pinecone) para recuperação semântica de battlecards análogos

## Entregável (prova de trabalho)

Pacote de Inteligência Pre-Reunião — composto por dois artefatos verificáveis no ClickUp: (1) Dossiê de Conta (versão executiva 1 página + versão completa): Visão Geral da Empresa, Momento Atual, Mapa de Stakeholders com abordagem por perfil, Dores Previstas, Perguntas de Discovery Recomendadas, Red Flags e Oportunidades; (2) Battlecard Competitivo: tabela comparativa com até 3 concorrentes, objeções previstas com respostas prontas, ângulo de ataque recomendado. Entregues ao vendedor via Slack/WhatsApp/email com resumo de 5 bullets até 30 minutos antes da reunião (ou em < 8 minutos para reuniões ad-hoc).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligencia estrategica) — arquitetura de multi-worker para pesquisa paralela de fontes heterogeneas diretamente aplicavel ao SCOUT e ORACLE; padrao de sintese hierarquica reusavel para o HERALD
- Win Proposal Deal (4 agentes, propostas comerciais) — logica de construcao de argumentacao comercial e estrutura de battlecard competitivo reusavel pelo WARFARE; padrao de critic/verifier pre-entrega reusavel pelo SENTINEL
- Apex Context Supreme (5 agentes, context engineering) — tecnicas de compressao e priorizacao de contexto para garantir que o dossie final seja denso e acionavel sem ruido; padrao de formatacao adaptativa por tempo disponivel (versao executiva vs completa) reusavel pelo HERALD

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V5 · TopSquad de Sales Enablement & Conversation Intelligence** — O copiloto do closer: contexto antes, respostas durante, coaching depois.

- **Missão:** Tudo que torna o vendedor humano melhor: prepara o contexto da conta e battlecards antes da call, sugere respostas a objeções durante, e analisa a gravação para coaching depois. Um cérebro de enablement do pré ao pós-call.
- **Por que consolidar:** Os três bebem da mesma fonte: a base de conhecimento de produto, concorrência e conversas reais. Battlecards alimentam o objection handling, que alimenta o coaching, que descobre novas objeções para os battlecards. Era um ciclo partido em três; unido, ele se retroalimenta.
- **Squads irmãos:** Conversation Intelligence & Coaching, Objection Handling & Q&A em Tempo Real, Inteligência de Conta & Battlecards

## Estrutura

```
vendas-inteligencia-conta-battlecards/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
