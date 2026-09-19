# Meeting Intelligence — Decisões que Nunca se Perdem

> Toda reunião vira um ativo estratégico: decisões extraídas, ações no ClickUp e a KB institucional alimentada automaticamente — do áudio bruto ao artefato rastreável em menos de 10 minutos.

**Área:** Founder Office · **TopSquad:** F1 Chief of Staff & Clone do Founder · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Decisões e ações acordadas em reuniões se dissolvem: ficam na memória do founder, em cadernos, em gravações que ninguém assiste. O resultado é retrabalho (mesmos problemas rediscutidos), ações que não viram tarefas, e uma base institucional que nunca aprende com as reuniões. Mensurável por: % de reuniões com decisões e ações formalmente extraídas (baseline < 15% → meta 100%), taxa de ações capturadas que viram tarefas rastreadas no ClickUp (baseline ~ 20% → meta >= 90%), tempo do founder em follow-up manual pós-reunião (baseline 45-90 min/reunião → meta < 5 min), e número de decisões estratégicas recuperáveis na KB institucional (baseline ~ 0 → meta 100% das reuniões do founder).

## Impacto esperado

ROI direto: founder com 8-12 reuniões/semana poupa 6-9 horas de follow-up manual semanal (R$9.000-13.500/semana a R$1.500/h). Com taxa de ações rastreadas de 20% para 90%, elimina o retrabalho de reuniões repetidas: estimativa de 2-3 reuniões redundantes/mês eliminadas = R$18.000-27.000/mês em custo oculto recuperado. Para a consultoria Lendar[IA]: squad posicionado no pilar Dados & Tecnologia do Diagnóstico; ROI é imediato e perceptível na primeira semana, o que acelera a decisão de implementação dos squads subsequentes. Ticket de implementação R$25-60k + recorrência R$4.500-9.800/mês como serviço gerenciado. NPS esperado >= 9.5 por impacto imediato e tangível na rotina do founder.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Maestro — O Diretor de Orquestra Institucional | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `vox` · Vox | Vox — O Transcritor de Precisão | L0 · worker determinístico | `transcrever-video.md` |
| `pulse` · Pulse | Pulse — O Enriquecedor de Contexto | L1 · worker autônomo | `enriquecer-contexto-transcricao.md` |
| `quill` · Quill | Quill — O Extrator Estruturado | L2 · orquestra / decide | `extrair-decisoes.md` |
| `vector` · Vector | Vector — O Conector da KB | L1 · worker autônomo | `conectar-outputs-extracao.md` |
| `hermes` · Hermes | Hermes — O Despachante de Ações | L3 · aprovação humana | `despachar-artefatos-sistemas-cliente.md` |
| `echo` · Echo | Echo — O Guardião de Follow-Up | L2 · orquestra / decide | `monitorar-action-items.md` |
| `argos` · Argos | Argos — O Crítico de Completude | L1 · worker autônomo | `verificar-completeness.md` |
| `argos-2` · Argos 2 | Argos — O Crítico de Completude | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-meeting-intelligence:maestro` (ou instale via `npx squads add ./founder-meeting-intelligence`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-meeting-intelligence-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB — Maestro pausa o pipeline e notifica o founder com a contradição detalhada (decisão antiga vs. nova decisão). O founder confirma qual prevalece antes de Hermes atualizar a KB e criar tasks. Sem confirmação em 4h, o item fica em quarentena.
- ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founder com os itens em destaque para atribuição manual antes de Hermes criar as tasks. Prazo de resposta: 2h (reuniões urgentes) ou 24h (demais).
- DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Proposal) — o founder deve aprovar as atualizações antes do envio. Qualquer mudança de stage ou valor estimado requer aprovação explícita via Slack (botão Aprovar/Rejeitar).
- BOARD MEMO PARA ENVIO EXTERNO (L3): Hermes pode criar o draft do Board Memo no Notion automaticamente (L2), mas o envio para membros do board, investidores ou parceiros externos é sempre bloqueado até aprovação explícita do founder. Nenhum email ou comunicação sai sem revisão humana.
- INFORMAÇÃO SENSÍVEL FLAGUEADA (L3): Quando Argos detecta informações sensíveis na transcrição (valores de negociação, dados de saúde financeira, informações sobre demissões ou reestruturações, dados pessoais de terceiros) — o trecho é isolado e o founder decide: (a) incluir na KB com controle de acesso restrito, (b) incluir no sumário interno apenas, ou (c) excluir do registro. Sem decisão do founder, o trecho fica em quarentena.
- OVERDUE CRÍTICO COM ESCALADA (L2→HITL): Quando Echo identifica action item de reunião estratégica com mais de 7 dias de atraso e o assignee não respondeu a lembretes — Maestro escala para o founder com contexto completo (o que foi acordado, quando, por quem) para decisão de realocar, cancelar ou intervir diretamente.
- CUSTO DE PROCESSAMENTO ACIMA DE THRESHOLD (L3): Se estimativa de custo de tokens de uma reunião longa (> 3h) superar limite configurado (default: U$2 por reunião) — Maestro apresenta opções ao founder: processar completo, processar apenas segmentos marcados como críticos, ou processar com nível de detalhe reduzido.

## KPIs

- % de reuniões processadas com decisões e ações extraídas (target 100% das reuniões do founder com gravação disponível)
- Taxa de action items com owner E deadline presentes no output (target >= 95% — Argos bloqueia se < 85%)
- Taxa de ações capturadas que viram tasks rastreadas no ClickUp (target >= 90% vs. baseline ~20%)
- Tempo médio de processamento por reunião de 60 min (target < 10 min end-to-end)
- Taxa de tasks criadas pelo squad com status 'Concluída' no prazo (proxy de accountability real — target >= 75%)
- Número de contradições com KB histórica detectadas e resolvidas por mês (indicador de valor da memória institucional — meta crescente)
- Tempo poupado do founder em follow-up manual por semana (target >= 6h/semana — calculado por pesquisa quinzenal com o founder)
- NPS do founder com o Meeting Intelligence Report (pesquisa pós-entrega das primeiras 4 semanas — target >= 9/10)
- Taxa de reuniões recorrentes com Pre-Meeting Brief gerado e aprovado pelo founder (target >= 90%)
- Custo médio por reunião processada em tokens (target < U$1 para reuniões de até 60 min)

## Integrações

- Google Meet / Zoom / Microsoft Teams (captura de gravações automática via webhooks ou API — intake direto de reuniões gravadas)
- Google Calendar / Outlook Calendar (enriquecimento de metadados — participantes, recorrência, tipo de reunião; trigger automático por evento de calendário com gravação)
- ClickUp (criação de tasks com owner, deadline, prioridade e contexto — core output do squad; leitura de tasks existentes para deduplicação e follow-up)
- Notion (KB institucional — armazenamento permanente de Decision Records, Knowledge Snippets e Meeting Intelligence Reports; busca semântica via Vector DB)
- Slack (intake de reuniões via upload/link no canal #meetings-intel + entrega de sumários + notificações de action items + alertas de deadline + confirmações HITL)
- HubSpot (atualização de deals e contatos quando reunião envolve cliente/prospect — next steps, mudança de stage, notas de reunião)
- Claude Agent SDK + LangGraph (orquestração stateful do pipeline multi-agente — gerencia sequência Vox→Pulse→Quill→Vector→Argos→Hermes e estado da sessão por reunião)
- Langfuse (observabilidade OTEL — tracing completo por reunião, custo por agente/token, eval de qualidade de extração, dashboard de KPIs do squad)
- Whisper API / AssemblyAI (transcrição de áudio com diarização de alta qualidade — Vox usa como motor de transcrição com fallback entre providers)
- Vector DB — Pinecone ou Qdrant (armazenamento e busca semântica de decisões históricas, sumários e conhecimento tácito do founder)
- Gmail / Email SMTP (notificações de action items para participantes externos; envio de Meeting Intelligence Report para stakeholders aprovados)
- MCP Servers (camada de integração universal — ClickUp MCP, Notion MCP, Slack MCP, Google Calendar MCP expostos como tools para os agents)

## Entregável (prova de trabalho)

Meeting Intelligence Report — documento estruturado gerado por reunião, salvo permanentemente na KB (Notion) e enviado ao founder via Slack. Contém: (1) Executive Summary com 5 bullets (decisões, ações, insights chave, próximos passos, riscos identificados); (2) Decision Log — tabela de todas as decisões formais com statement, owner, rationale, alternativas rejeitadas e link para contexto histórico na KB; (3) Action Items com formato pronto para ClickUp (título, assignee, deadline, prioridade, contexto executável) e link para task criada; (4) Strategic Insights — Knowledge Snippets para alimentar KB institucional com frameworks, hipóteses e conhecimento tácito extraído; (5) Consistency Report — lista de alinhamentos e contradições com decisões históricas; (6) Audit Trail completo (quais agentes processaram, timestamps, custo de tokens, versão do report); (7) Link permanente para transcrição original. Para reuniões classificadas como 'board' ou 'estratégica nível 1': Board Memo Draft adicional (executive one-pager para compartilhamento com stakeholders após aprovação do founder). Toda ação executada por Hermes é rastreada com ID de task no ClickUp como prova de trabalho auditável.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base para o pipeline de extração multi-dimensional e síntese estruturada do Quill; reaproveitar a arquitetura de workers paralelos com synthesis final para o padrão Quill→Argos→Maestro
- Skeptic Protocol (5 agentes, red-team/QA) — mapeia diretamente para o papel do Argos: protocolo de verificação adversarial de completude, detecção de lacunas lógicas e items implícitos não capturados — integrar como camada de validação antes do despacho
- Apex Context Supreme (5 agentes, context engineering) — base para o Pulse (enriquecimento contextual): arquitetura de recuperação e injeção de contexto histórico relevante antes do processamento principal, exatamente o que o Pulse faz com a KB institucional

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F1 · TopSquad de Chief of Staff & Clone do Founder** — O braço executivo: agenda, reuniões, memória institucional e um twin que decide no estilo do founder.

- **Missão:** A extensão operacional do founder: gere agenda e prioridades (chief of staff), captura e processa reuniões (meeting intelligence), mantém a memória institucional e opera o digital twin que rascunha decisões/respostas no estilo e nos valores do founder.
- **Por que consolidar:** Os quatro compartilham o ativo mais raro — o contexto do founder. O clone só funciona com a memória institucional; o chief of staff age sobre as decisões das reuniões; meeting intelligence abastece a memória. Separados, cada um reconstruía o contexto do founder do zero. Unidos, há um único cérebro do founder.
- **Squads irmãos:** AI Chief of Staff, Meeting Intelligence, Clone Estratégico do Founder (Digital Twin), Knowledge Base Institucional do Founder

## Estrutura

```
founder-meeting-intelligence/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
