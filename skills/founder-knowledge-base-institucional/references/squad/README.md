# Squad Knowledge Base Institucional do Founder

> O conhecimento que vive na cabeça do founder vira grafo consultável, clone estratégico e vantagem competitiva permanente.

**Área:** Founder Office · **TopSquad:** F1 Chief of Staff & Clone do Founder · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

O conhecimento crítico da empresa — frameworks de decisão, teses de mercado, lógica por trás de cada escolha estratégica, modelos mentais do founder — vive disperso em conversas de Slack, emails, reuniões não gravadas e na própria memória do founder. Quando o founder não está disponível, a empresa trava. Quando alguém novo entra, o onboarding é incompleto. Quando um investidor pergunta a tese, o memo é reescrito do zero. O custo real não é só o tempo perdido — é a perda de coerência estratégica quando decisões são tomadas sem acesso ao raciocínio original do fundador. Mensurável por: % de conhecimento tácito ingerido e estruturado (meta: 80% dos tópicos críticos em 90 dias), taxa de reuso do grafo em respostas de outros squads (meta: > 60% das consultas estratégicas respondidas sem interromper o founder), e tempo médio de resposta a perguntas estratégicas internas (de dias para minutos).

## Impacto esperado

Redução de 70-85% nas interrupções do founder por perguntas já respondidas antes — liberando 8-15h/semana para trabalho de alta alavancagem. Aceleração de onboarding de liderança de 4-8 semanas para 3-5 dias via acesso ao corpus estruturado. Memos de board e investor updates gerados em 2-4h em vez de 2-3 dias de escrita manual. Para consultorias como a Lendar[IA], o squad é o próprio produto-prova: o founder demonstra ao vivo que seu conhecimento foi capturado, estruturado e pode ser consultado por qualquer membro do time — provando o valor de IA institucional. ROI estimado: 10-20x sobre o custo do squad considerando apenas o tempo do founder recuperado (a R$2.000-5.000/hora de oportunidade). Para clientes do diagnóstico, o squad justifica sozinho o investimento de R$18-40k na implementação.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · ORION | ORION — O Guardião do Segundo Cerebro | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `scribe` · SCRIBE | SCRIBE — O Ingestor de Conhecimento Tácito | L1 · worker autônomo | `transformar-conhecimento-tacito.md` |
| `cartographer` · CARTOGRAPHER | CARTOGRAPHER — O Construtor do Grafo | L1 · worker autônomo | `construir-grafo-conhecimento.md` |
| `persona-forge` · PERSONA FORGE | PERSONA FORGE — O Clone Estratégico | L2 · orquestra / decide | `sintetizar-respostas-confidentes.md` |
| `scrivener` · SCRIVENER | SCRIVENER — O Motor de Mémos | L2 · orquestra / decide | `gerar-drafts-narrativos.md` |
| `radar` · RADAR | RADAR — O Monitor de Inteligência Estratégica | L2 · orquestra / decide | `monitorar-sinais-estrategicos.md` |
| `chief-of-staff` · CHIEF OF STAFF | CHIEF OF STAFF — O Agente de Alta Alavancagem | L2 · orquestra / decide | `preparar-reunioes-importantes.md` |
| `wargame` · WARGAME | WARGAME — O Simulador de Cenários | L1 · worker autônomo | `simular-cenarios-futuros.md` |
| `auditor` · AUDITOR | AUDITOR — O Verificador de Fidelidade ao Corpus | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-knowledge-base-institucional:orion` (ou instale via `npx squads add ./founder-knowledge-base-institucional`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-knowledge-base-institucional-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automaticamente — pausa e apresenta ao founder os dois claims com contexto (data, situacao) para ele determinar qual e a posicao atual e por que evoluiu. Irreversivel porque altera permanentemente o grafo canônico.
- L3 — Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída para fora da empresa exige leitura e aprovação explícita do founder. O clone fala pela empresa — erro de representação e irreversível reputacionalmente.
- L3 — Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com anotações de contexto por seção para facilitar a revisão, mas o envio nunca é automático.
- L2 — Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para reunião'. O founder decide o que fazer com o sinal, não o squad.
- L2 — Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao ha ingestao forçada — o founder controla o ritmo de captura do proprio conhecimento.
- L1 — Revisão do mapa de lacunas gerado no Discovery: antes de priorizar quais tópicos capturar, o founder valida se a taxonomia e as lacunas identificadas fazem sentido. Ele pode adicionar tópicos críticos não detectados ou reclassificar prioridades.

## KPIs

- Cobertura do grafo: % de tópicos críticos identificados no Discovery com pelo menos 3 fontes convergentes no grafo — meta 80% em 90 dias de operação
- Taxa de reuso pelo clone: % de consultas estratégicas respondidas pelo Persona Forge sem interrupção do founder — meta > 60% das consultas em 60 dias
- Frequência de interrupções do founder: número de vezes por semana que o founder é interrompido por perguntas estratégicas respondidas no grafo — meta redução de 70% em 90 dias (baseline medido na semana 1)
- Taxa de aprovação do Auditor na primeira passagem: meta > 80% para chunks de ingestão, > 90% para outputs do Persona Forge
- Tempo de geração de memo: da solicitação ao draft aprovado pelo Auditor — meta < 4 horas para board pack padrão, < 45 minutos para memo interno
- Frescor do corpus: % de nós do grafo com fonte datada nos últimos 180 dias — meta > 70% dos nós ativos
- Acurácia do Wargame: % de cenários gerados que o founder avalia como 'plausível e útil' (survey quinzenal) — meta > 75%
- Cobertura de briefings pré-reunião: % de reuniões importantes com briefing entregue 24h antes — meta > 85%
- Contradições resolvidas: % de contradições sinalizadas pelo Cartographer que receberam validação do founder em < 48h — meta > 90% (indica que o HITL está fluindo bem)

## Integrações

- Notion MCP — fonte primária de documentos, local de entrega de memos e briefings, armazenamento do grafo legível por humanos
- Slack MCP — ingestão de threads estratégicos exportados, entrega de alertas do Radar e digest do Chief of Staff, interface /clone para consultas ao Persona Forge
- Google Calendar / Outlook MCP — leitura de agenda pelo Chief of Staff para disparo de briefings pré-reunião e detecção de datas críticas (board, investors)
- Gmail MCP — ingestão de emails estratégicos exportados pelo SCRIBE, monitoramento de follow-ups pelo Chief of Staff
- Sembly / Fireflies API — ingestão automática de transcrições de reuniões gravadas para o SCRIBE
- ClickUp MCP — registro de tarefas e artefatos como prova de trabalho verificável, gestão de follow-ups pelo Chief of Staff
- ElevenLabs API — opcional: voz do clone para versão de áudio do Persona Forge (digital twin executivo para podcasts internos ou mensagens de voz)
- Supabase pgvector — vector store para embeddings do grafo (nós, arestas, corpus do clone), recuperação semântica de alta performance
- LangGraph / Claude Agent SDK — orquestração stateful dos workers, controle de paralelismo (SCRIBE + Cartographer + Radar em paralelo), retry logic e gerenciamento de estado do grafo
- Langfuse — observabilidade OTEL completa: tracing de cada ingestão e consulta, custo por worker, taxa de aprovação do Auditor, quality gates (dev 70% / staging 85% / prod 95% task success)
- EXA Web Search MCP — pesquisa de sinais externos pelo Radar e contextualização de mercado pelo Wargame
- Google Drive — fonte de documentos históricos (decks, board packs, docs estratégicos) para ingestão pelo SCRIBE

## Entregável (prova de trabalho)

Corpus Institucional Vivo — conjunto de artefatos verificáveis entregues pelo squad: (1) Grafo de Conhecimento Estruturado (Notion + vector store): taxonomia completa com nós, arestas, fontes e nível de confiança por claim — consultável por qualquer membro autorizado do time; (2) Clone Estratégico Ativo (Persona Forge): interface /clone no Slack que responde perguntas estratégicas com a lógica do founder, com citação de fonte e nível de confiança; (3) Memo Engine Configurado (Scrivener): capacidade de gerar board packs e investor updates em < 4h com rastreabilidade total ao grafo; (4) Intelligence Feed Ativo (Radar): alertas contextualizados de movimentos competitivos e de mercado conectados ao grafo; (5) Relatório de Cobertura Mensal: dashboard no ClickUp mostrando % de tópicos cobertos, taxa de reuso, interrupções evitadas e valor estimado de tempo do founder liberado. Prova de trabalho: toda consulta, ingestão e memo registrado no Langfuse com trace completo e no ClickUp com artefato verificável.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligencia estrategica) — arquitetura de multi-worker para pesquisa e sintese hierarquica diretamente reusavel pelo Radar e pelo Wargame; padrao de verificacao de claims com citacao de fonte reusavel pelo Auditor; logica de grafo de conhecimento consultavel adaptavel ao Cartographer
- Cognitive Fusion Lab (clone cognitivo) — estrutura de construção de clone a partir de corpus próprio diretamente aplicável ao Persona Forge; técnicas de captura de estilo, tom e frameworks recorrentes de um expert específico; padrão de resposta com nível de confiança e citação de fonte
- Genius Athena Strange (5 agentes, decisao sob incerteza) — logica de simulacao de cenarios adversariais e wargaming competitivo reusavel pelo Wargame; padrao de Critic/Verifier para outputs de alta stakes adaptavel ao Auditor; framework de escalada para HITL em decisoes irreversiveis

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F1 · TopSquad de Chief of Staff & Clone do Founder** — O braço executivo: agenda, reuniões, memória institucional e um twin que decide no estilo do founder.

- **Missão:** A extensão operacional do founder: gere agenda e prioridades (chief of staff), captura e processa reuniões (meeting intelligence), mantém a memória institucional e opera o digital twin que rascunha decisões/respostas no estilo e nos valores do founder.
- **Por que consolidar:** Os quatro compartilham o ativo mais raro — o contexto do founder. O clone só funciona com a memória institucional; o chief of staff age sobre as decisões das reuniões; meeting intelligence abastece a memória. Separados, cada um reconstruía o contexto do founder do zero. Unidos, há um único cérebro do founder.
- **Squads irmãos:** AI Chief of Staff, Meeting Intelligence, Clone Estratégico do Founder (Digital Twin), Knowledge Base Institucional do Founder

## Estrutura

```
founder-knowledge-base-institucional/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
