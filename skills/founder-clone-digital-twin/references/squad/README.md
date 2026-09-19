# Clône Estratégico do Founder — Digital Twin

> Seu conhecimento tácito responde 24/7 — sem precisar de vócê.

**Área:** Founder Office · **TopSquad:** F1 Chief of Staff & Clone do Founder · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

O founder e o gargalo operacional e estratégico da organização: cada decisão relevante, cada direcionamento de time, cada resposta a uma pergunta de alto nível passa por ele. Frameworks mentais, tom de voz, critérios de priorização e modelos de raciocínio existem apenas na cabeça do founder e não escalam. O custo invisível: decisões atrasadas, oportunidades perdidas, equipe em espera constante. Mensurável por: % de perguntas estratégicas respondidas sem intervenção direta do founder (baseline típico: 10-20%, meta com squad: 60-80%) e tempo médio de resposta a demandas estratégicas (baseline: 24-72h, meta: < 2h para 70% dos casos).

## Impacto esperado

Para um founder que ganha R$50k/mês e divide seu tempo em 40% de decisões operacionais/repetitivas que poderiam ser delegadas a um clône, o squad libera R$20k/mês de capacidade de alta alavancagem. Empresas de consultoria e serviço com founder como principal ativo intelectual (R$2-20M ARR) reportam gargalo de escala como motivo #1 de estagnação. Com o Digital Twin operacional: redução estimada de 60-70% das interrupções ao founder, 3-5x mais velocidade de resposta em decisões de média complexidade, capacidade de onboarding de novos clientes e colaboradores sem depender do founder para transferência de conhecimento. ROI estimado: 15-25x o custo do squad quando medido em horas de founder recuperadas x valor horário x oportunidades desbloqueadas no primeiro semestre.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · ORION | ÓRION — O Chief of Staff Cognitivo | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `echo` · ECHO | ECHO — O Clone Cognitivo do Founder | L2 · orquestra / decide | `responder-perguntas.md` |
| `atlas` · ATLAS | ATLAS — O Deep Research Worker | L1 · worker autônomo | `conduzir-pesquisa-multi-fonte.md` |
| `chronicle` · CHRONICLE | CHRONICLE — O Agente de Ingestão e Knowledge Graph | L1 · worker autônomo | `ingerir-fontes-de-conhecimento.md` |
| `strategos` · STRATEGOS | STRATEGOS — O Agente de Cenários e Wargaming | L2 · orquestra / decide | `simular-cenarios-futuros.md` |
| `herald` · HERALD | HERALD — O Agente de Comunicação e Board Intelligence | L3 · aprovação humana | `gerar-drafts-de-board-packs.md` |
| `vigil` · VIGIL | VIGIL — O Monitor de Inteligência Competitiva | L1 · worker autônomo | `monitorar-sinais-competitivos.md` |
| `gate` · GATE | GATE — O Agente HITL e Guardião de Fronteiras | L0 · worker determinístico | `controlar-acoes-l3.md` |
| `sentinel` · SENTINEL | SENTINEL — O Verificador de Fidelidade Cognitiva | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-clone-digital-twin:orion` (ou instale via `npx squads add ./founder-clone-digital-twin`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-clone-digital-twin-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 – HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio – o squad nunca envia comunicação externa autonomamente
- L3 – GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política interna – founder aprova com opções claras antes da execução
- L3 — Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao de pensamento antes de ser persistida no corpus canônico
- L2 – ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma aproximação e pode escalonar
- L2 — STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer caminho seja comunicado como recomendacao oficial do squad
- L1 — VIGIL ao detectar sinal competitivo CRÍTICO fora do ciclo semanal: notificação imediata ao founder com proposta de contra-jogada — founder decide se ativa resposta ou aguarda mais informações
- L1 — CHRONICLE ao identificar gap crítico no corpus que impacta a confiabilidade do ECHO em categoria de alto volume: agenda sessão de captura de conhecimento com o founder antes de continuar respondendo naquela categoria

## KPIs

- Taxa de autonomia do clone: % de demandas estratégicas respondidas pelo ECHO sem intervenção do founder — baseline típico 10-20%, meta 60-80% em 90 dias de operação
- Tempo médio de resposta a demandas estratégicas: baseline 24-72h (aguardando founder), meta < 2h para 70% das demandas em Clone Mode e Research Mode
- Score de fidelidade cognitiva (SENTINEL): % de respostas classificadas como FIEL pelo SENTINEL na primeira passagem — meta > 85% em staging / > 92% em produção
- Taxa de aprovação em L3 (GATE): % de ações L3 aprovadas vs rejeitadas — meta de rejeição < 5% (indica que o squad está gerando propostas bem calibradas, não forçando aprovação)
- Cobertura do corpus: score de completude do Knowledge Graph por categoria (operacional / estratégica / cultural / técnica) medido pelo CHRONICLE — meta > 80% de cobertura em categorias de alto volume
- Redução de interrupções ao founder: número de interrupções diretas (Slack DM, WhatsApp urgente) por semana — meta redução de 60% em 60 dias vs baseline
- Qualidade do VIGIL: % de alertas competitivos classificados como RELEVANTE ou CRITICO que o founder confirmou como acionaveis — meta > 70% de precision (evitar fadiga de alertas)
- Latência de geração de comunicação (HERALD): tempo do disparo ao draft aprovado pelo SENTINEL — meta < 15 minutos para board updates padrão
- Loop de aprendizado: número de atualizações válidas do Knowledge Graph por semana via feedback do founder — indicador de saúde do sistema de melhoria contínua

## Integrações

- Slack (MCP): canal principal de recepção de demandas ao squad e entrega de respostas — inbox do ORION, notificações do VIGIL, alertas do GATE
- Gmail / Google Workspace (MCP): ingestão de emails estratégicos para o CHRONICLE, entrega de drafts do HERALD para revisão do founder, leitura de threads para contexto de demandas
- WhatsApp Business API: canal prioritário para alertas L3 do GATE e sinais CRÍTICOS do VIGIL — founder responde APROVAR/REJEITAR diretamente no WhatsApp
- Notion: repositório primário do Knowledge Graph estruturado, storage de drafts do HERALD, documentação de decisões estratégicas — integração via MCP ou Notion API
- Sembly / Fireflies.ai: transcrição automática de reuniões e calls do founder para ingestão pelo CHRONICLE — fonte primária de conhecimento tácito não documentado
- Google Calendar (MCP): leitura de agenda do founder para pre-briefings do ORION, disparo do HERALD para preparação de reuniões importantes, monitoramento de compromissos estratégicos
- ClickUp: gestão de todas as tarefas do squad como prova de trabalho verificável — cada demanda, pesquisa e comunicação gera uma task auditável com status, output e histórico de aprovações
- Supabase (pgvector): base vetorial para recuperação semântica do Knowledge Graph do founder — busca por similaridade semântica em corpus de alta dimensão
- EXA MCP (via Docker): busca web em tempo real para o ATLAS e o VIGIL — pesquisa profunda com fontes verificáveis
- Apífy (via Docker): scraping estruturado de concorrentes, LinkedIn, G2/Capterra para o VIGIL e ATLAS
- Langfuse (OTEL): observabilidade completa de todas as execuções — tracing de cada resposta do ECHO, score de fidelidade pelo SENTINEL, latência por worker, custo de tokens por tipo de demanda, quality gates por ambiente (dev 70% / staging 85% / prod 95%)
- LangGraph / Claude Agent SDK: orquestração stateful do pipeline — controle de estado de demandas complexas, paralelismo do ATLAS em swarm mode, retry logic para falhas de worker
- ElevenLabs (opcional): voz sintetizada do founder para respostas em áudio — digital twin executivo completo para reuniões assíncronas ou conteúdo em vídeo

## Entregável (prova de trabalho)

Pacote do Digital Twin Operacional — conjunto de artefatos verificáveis no ClickUp e Notion: (1) Knowledge Graph do Founder v{N} — grafo estruturado e auditável com frameworks, princípios, decisões e vocabulário do founder, com score de completude por categoria; (2) Log de Demandas Atendidas — histórico completo de cada pergunta recebida, modo de resposta ativado, output gerado, veredicto do SENTINEL e decisão de HITL quando aplicável; (3) Relatório Semanal de Inteligência (VIGIL) — movimentos competitivos, oportunidades e alertas da semana com fontes; (4) Relatório Mensal do Clone — métricas de autonomia, score de fidelidade, gaps identificados e plano de melhoria do corpus para o próximo mês; (5) Drafts de Comunicação (HERALD) — board packs, memos e comunicados com histórico de versões e aprovações; (6) Dashboard Langfuse — observabilidade em tempo real de custo, latência, quality gates e taxa de aprovação do SENTINEL por tipo de demanda.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Cognitive Fusion Lab (clone cognitivo) — arquitetura base de digital twin e ingestão de corpus pessoal diretamente aplicável ao ECHO e ao CHRONICLE; padrão de mapeamento de frameworks mentais e recuperação semântica reutilizável como ponto de partida para o Knowledge Graph do founder
- Athenaeum (11 agentes, inteligência estratégica) — arquitetura de multi-worker para pesquisa paralela com citação de fontes aplicável ao ATLAS em swarm mode; padrão de síntese hierárquica e verificação de claims reutilizável pelo SENTINEL
- Genius Athena Strange (5 agentes, decisao sob incerteza) — logica de arvore de decisao e simulacao de cenarios adversariais diretamente aplicavel ao STRATEGOS; framework de wargaming competitivo e estimativa de probabilidades por caminho reutilizavel como base do modulo de cenarios

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F1 · TopSquad de Chief of Staff & Clone do Founder** — O braço executivo: agenda, reuniões, memória institucional e um twin que decide no estilo do founder.

- **Missão:** A extensão operacional do founder: gere agenda e prioridades (chief of staff), captura e processa reuniões (meeting intelligence), mantém a memória institucional e opera o digital twin que rascunha decisões/respostas no estilo e nos valores do founder.
- **Por que consolidar:** Os quatro compartilham o ativo mais raro — o contexto do founder. O clone só funciona com a memória institucional; o chief of staff age sobre as decisões das reuniões; meeting intelligence abastece a memória. Separados, cada um reconstruía o contexto do founder do zero. Unidos, há um único cérebro do founder.
- **Squads irmãos:** AI Chief of Staff, Meeting Intelligence, Clone Estratégico do Founder (Digital Twin), Knowledge Base Institucional do Founder

## Estrutura

```
founder-clone-digital-twin/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
