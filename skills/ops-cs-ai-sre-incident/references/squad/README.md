# AI SRE — Incident Management Squad

> De tempestade de alertas a root cause em minutos: o SRE que nao dorme, nao esquece e documenta tudo.

**Área:** Operações & CS · **TopSquad:** O5 Operações Técnicas: SRE, SLA & Data Pipelines · **Prioridade:** avançado · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Incidentes operacionais geram dezenas de alertas desconexos simultaneamente. O time de SRE gasta 60-80% do tempo de um incidente apenas correlacionando evidencias e replicando contexto entre ferramentas — enquanto o downtime cresce e o cliente sangra. O squad correlaciona todos os alertas em tempo real, traça o root cause com evidencias verificaveis, propoe ou aplica o fix com autonomia graduada (L2/L3) e entrega um post-mortem completo sem esforco humano. MTTR medio no mercado: 4-8h para incidentes P1. Meta do squad: <30 min para proposta de fix confirmada.

## Impacto esperado

Reducao de MTTR de 4-8h para menos de 30 min em incidentes correlacionados (ROI direto: custo de downtime x horas economizadas). Triagem automatica de 70-80% dos alertas elimina ruido e libera SREs para trabalho de engenharia real. Post-mortem automatico reduz 3-5h de documentacao manual por incidente. Para SaaS com SLA de 99.9%, cada minuto de downtime evitado preserva credito de SLA e NPS. Estimativa conservadora: squad paga seu custo com o primeiro incidente P1 evitado ou acelerado no mes.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `ic` · IC | Incident Commander (IC) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `alert-correlator` · Alert Correlator | Alert Correlator — 'Nexus' | L0 · worker determinístico | `correlacionar-alertas.md` |
| `root-cause-investigator` · Root Cause Investigator | Root Cause Investigator — 'Sherlock' | L1 · worker autônomo | `analisar-logs-incidente.md` |
| `fix-proposer` · Fix Proposer | Fix Proposer — 'MacGyver' | L2 · orquestra / decide | `gerar-propostas-de-fix.md` |
| `fix-executor` · Fix Executor | Fix Executor — 'Forge' | L2 · orquestra / decide | `executar-acoes-l2.md` |
| `incident-communicator` · Incident Communicator | Incident Communicator — 'Herald' | L1 · worker autônomo | `comunicar-incidentes.md` |
| `post-mortem-writer` · Post-Mortem Writer | Post-Mortem Writer — 'Chrono' | L3 · aprovação humana | `analisar-incidentes.md` |
| `fix-guardian` · Fix Guardian | Fix Guardian — 'Aegis' | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-ai-sre-incident:ic` (ou instale via `npx squads add ./ops-cs-ai-sre-incident`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-ai-sre-incident-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Toda acao irreversivel ou de alto risco requer aprovacao explicita do SRE on-call antes de execucao pelo Forge: rollback de deploy em producao, failover de banco de dados primario, mudanca de configuracao de infraestrutura critica, escalonamento de recursos com impacto financeiro significativo, qualquer acao em banco de dados (DELETE, DROP, ALTER em producao)
- L3 — Publicacao do post-mortem final: o Chrono gera o draft, mas um humano revisa e aprova antes de publicar para o time ou para clientes
- L3 — Comunicacao externa para clientes afetados: o Herald gera o rascunho, o CS Manager aprova antes do envio
- HITL emergencial — Se o Aegis retornar veredicto BLOCKED_ESCALATE em qualquer momento, o incidente entra em modo manual ate que um SRE sênior retome o controle via canal Slack do war room
- HITL emergencial — Se o Forge encontrar falha em acao L2 ou resultado inesperado apos execucao, pausa automaticamente e notifica o SRE on-call antes de prosseguir
- L2 confirmado — Declaracao de severidade P1 pelo Orchestrator notifica imediatamente o SRE on-call e o Engineering Lead via PagerDuty/Slack, mesmo sendo L2 (execucao autonoma), para que humanos possam assumir controle a qualquer momento
- HITL de degradacao — Se MTTR ultrapassar 2x o ETR estimado sem resolucao, o Orchestrator automaticamente escala para modo assistido e solicita intervencao humana explicita

## KPIs

- MTTR (Mean Time to Resolution): meta < 30 min para incidentes P1 correlacionados (baseline do cliente medido no Deep Dive)
- Alert Noise Ratio: percentual de alertas agrupados como sintomas vs root causes unicos — meta: reduzir ruido em 60-80% nas primeiras 4 semanas
- % Incidentes Triados Automaticamente: meta 70% dos incidentes P2/P3 sem intervencao humana na fase de triagem
- % Post-Mortems Completados em < 24h apos resolucao: meta 95% (vs media do mercado de 3-7 dias)
- % Fix Plans aprovados sem revisao pelo Aegis (proxy de qualidade do MacGyver): meta > 80% na maturidade
- False Positive Rate do Sherlock (root causes propostos incorretos): meta < 15% medido em revisao humana dos post-mortems
- Action Items de Post-Mortem com due date cumprido: meta 75% em 30 dias (prevencao de recorrencia)
- MTTA (Mean Time to Acknowledge): tempo entre alerta e declaracao de incidente pelo Orchestrator — meta < 2 min
- Recurring Incidents Rate: incidentes com mesmo root cause em 30 dias — meta reducao de 40% em 90 dias de operacao

## Integrações

- PagerDuty — recepcao de alertas via webhook, criacao e atualizacao de incidents, escalonamento on-call
- Datadog — consulta de metricas, alertas, traces, service map e dashboards via API/MCP
- CloudWatch — logs e metricas de infra AWS
- Sentry — erros de aplicacao, releases e performance issues
- Grafana — dashboards de metricas e alertas (Prometheus/Loki)
- GitHub Actions / ArgoCD — historico de deploys para correlacao com root cause
- Elastic / Splunk / Loki — consulta de logs durante investigacao
- Jaeger / Tempo — traces distribuidos para analise de latencia e falhas
- ClickUp — hub de prova de trabalho: cada incidente = task com timeline, artefatos e action items
- Slack — war room automatico, notificacoes de stakeholders, canal de HITL
- Supabase / Postgres — estado dos incidentes, historico de correlacoes, base de runbooks e post-mortems
- Langfuse — observabilidade OTEL do squad, tracing de chamadas de agentes, quality gates e evals de acuracia de root cause
- Terraform / AWS SSM / HashiCorp Vault — acesso seguro a credenciais para execucao de acoes L2
- ServiceNow — opcional: sincronizacao de incidents para empresas com ITSM legado
- Statuspage.io — atualizacao de status page publica durante incidentes que afetam clientes

## Entregável (prova de trabalho)

Incident Response Package — artefato completo por incidente, entregue automaticamente no ClickUp e Slack: (1) Incident Cluster Report com correlacao de alertas e noise score; (2) Root Cause Analysis com event timeline e evidencias; (3) Fix Plan executado com execution log e evidencias; (4) Post-Mortem blameless draft completo com action items criados no ClickUp; (5) Metricas do incidente (MTTA, MTTR, blast radius, servicos afetados). O conjunto destes artefatos e a 'prova de trabalho' verificavel que o squad gera — o cliente pode auditar cada incidente e ver exatamente o que o squad fez, em quanto tempo e qual foi o impacto.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Incident Response Squad (5 ag) — squad gratuito de referencia direta: estrutura de triagem, investigacao e resposta a incidentes que pode ser usado como base do pipeline e adaptado para o contexto AIOps com as integracoes especificas
- Five Vitals (diagnostico de sistemas) — squad gratuito para health check de sistemas: logica de deteccao de anomalias e diagnostico pode acelerar o desenvolvimento do Sherlock (Root Cause Investigator) e do Nexus (Alert Correlator)
- Skeptic Protocol (5 ag, red-team/QA) — squad gratuito de verificacao adversarial: arquitetura do critic/verifier pode ser adaptada diretamente para o Aegis (Fix Guardian), especialmente as logicas de checklist de 7 pontos e veredictos APPROVED/NEEDS_REVISION/BLOCKED

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O5 · TopSquad de Operações Técnicas: SRE, SLA & Data Pipelines** — Mantém a operação de pé: incidentes, SLAs e pipelines que se curam sozinhos.

- **Missão:** A espinha dorsal técnica: detecta e gere incidentes (SRE), monitora SLAs e saúde operacional, e mantém pipelines de dados que se auto-corrigem. Garante que toda a operação agêntica continue rodando — e confiável.
- **Por que consolidar:** Os três respondem ao mesmo evento — "algo quebrou ou vai quebrar" — em camadas distintas (serviço, SLA, dados). Monitoramento detecta, SRE responde, ETL se cura; é o mesmo loop de observabilidade → ação. Unidos, compartilham telemetria e runbooks em vez de três sistemas de alerta concorrentes.
- **Squads irmãos:** AI SRE — Incident Management, SLA & Health Monitoring Operacional, Self-Healing ETL

## Estrutura

```
ops-cs-ai-sre-incident/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
