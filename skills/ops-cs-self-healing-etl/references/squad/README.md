# Self-Healing ETL Squad

> Pipelines que quebram silenciosamente custam decisoes: o Self-Healing ETL detecta a anomalia, diagnostica a causa raiz e recupera a ingestao antes do dashboard mentir.

**Área:** Operações & CS · **TopSquad:** O5 Operações Técnicas: SRE, SLA & Data Pipelines · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Pipelines de dados falham silenciosamente — schema drift de fornecedor, fonte fora do ar, campo nulo inesperado — e a equipe só descobre quando o dashboard exibe número errado ou ausente. O tempo médio entre a falha e a descoberta (MTTD) é de 6-24h em equipes sem monitoramento dedicado, e o MTTR pode ultrapassar 48h quando o engenheiro responsável está em outra prioridade. O Self-Healing ETL monitora continuamente cada etapa do pipeline, detecta anomalias estatísticas e estruturais em tempo real, executa diagnóstico automático de root cause (schema drift vs. source down vs. data quality vs. volume anomaly) e aplica recuperação automática para falhas de baixa severidade (L0/L1/L2). Para falhas de alta severidade ou ações irreversíveis (reprocessamento massivo, alteração de schema em produção, rollback de tabela), propõe o fix com contexto completo e aguarda aprovação humana (L3). Prova de trabalho: task no ClickUp por incidente com alerta + diagnóstico + ação tomada + freshness restaurada.

## Impacto esperado

Redução de MTTR de 48h para < 2h em 80% dos incidentes (falhas L0-L2 auto-resolvidas). Redução de MTTD de 6-24h para < 15 minutos via monitoramento contínuo. Taxa de incidentes auto-resolvidos meta: 65-75% (sem intervenção humana). Custo evitado por incidente manual: 2-4h de engenheiro de dados (R$150-300/h) = R$300-1.200/incidente. Empresas com 20+ pipelines ativos experimentam 8-15 incidentes/mês — ROI direto: R$2.400-18.000/mês em horas de engenharia salvas. Impacto indireto: decisões de negócio baseadas em dados confiáveis (freshness garantida), redução de retrabalho analítico e eliminação de alertas de dashboard incorreto que geram desconfiança da liderança nos dados.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — O Maestro de Confiabilidade | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `argus` · Argus | Argus — O Vigia de Pipelines | L0 · worker determinístico | `monitorar-pipelines.md` |
| `remi` · Remi | Rémi — O Diagnosticador de Root Cause | L1 · worker autônomo | `testar-hipoteses-sequenciais.md` |
| `finn` · Finn | Finn — O Curador de Recuperação | L2 · orquestra / decide | `curar-falhas-reversiveis.md` |
| `coda` · Coda | Códa — O Arquiteto de Fíx | L1 · worker autônomo | `gerar-plano-de-remediacao.md` |
| `nexus` · Nexus | Nexus — O Calibrador de Baseline | L1 · worker autônomo | `calibrar-thresholds-baseline.md` |
| `vega` · Vega | Vega — O Verificador de Ações | L1 · worker autônomo | `verificar-acoes-automaticas.md` |
| `loki` · Loki | Loki — O Chronicler de Incidentes | L0 · worker determinístico | `documentar-incidente.md` |
| `vega-2` · Vega 2 | Vega – O Verificador de Ações | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-self-healing-etl:orion` (ou instale via `npx squads add ./ops-cs-self-healing-etl`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-self-healing-etl-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 – Ações irreversíveis ou P1-P2: qualquer ação que altere schema em produção, reprocesse mais de 24h de dados, faça rollback de tabela ou envolva custo de compute significativo requer aprovação explícita. Loki cria task no ClickUp com Fix Plan do Coda (checklist de aprovação) e notifica via Slack. SLA de resposta: P1 = 30min, P2 = 2h. Se SLA expirar sem resposta, Orion escala para gestor do pipeline.
- L3 — Vega emite BLOCKED: quando a verificacao do Vega reprova qualquer dimensao (proporcionalidade, reversibilidade, scope, precedente), a acao e bloqueada independente da classificacao original. Requer override explicito humano com justificativa registrada.
- L3 – Schema drift complexo: quando Remi identifica schema drift que não se enquadra nos patches automáticos seguros (ex: renomeação ambígua, remoção de campo usado downstream, mudança de tipo com perda de dados), o Coda prepara o plano de migração DDL completo para aprovação humana antes de qualquer alteração.
- L2 – Revisão do Calibration Report semanal do Nexus: humano (engenheiro de dados responsável) revisa os thresholds recalibrados antes da aplicação. Não bloqueia operação, mas permite ajuste fino de sensibilidade por pipeline crítico.
- L2 — Onboarding de novo pipeline: antes de iniciar monitoramento de um pipeline novo, humano valida o anomaly_config.json gerado pelo Nexus (thresholds, criticidade, recovery_policy) e confirma os assignees responsáveis por incidentes HITL.
- L1 — Weekly Incident Report: gestor de dados recebe o relatório semanal do Loki e pode re-classificar incidentes (true/false positive), ajustar prioridades e confirmar o cálculo de ROI para reportar para o cliente.

## KPIs

- MTTR (Mean Time to Recovery): tempo médio entre detecção da anomalia e freshness restaurada (meta: < 2h para 80% dos incidentes, baseline típico: 24-48h)
- MTTD (Mean Time to Detection): tempo entre a falha ocorrer e o Argus gerar o alerta (meta: < 15 minutos para pipelines P1-P2, < 30 minutos para P3-P4)
- Taxa de incidentes auto-resolvidos (L0-L2): % de incidentes resolvidos sem intervenção humana (meta: 65-75% em 90 dias)
- Taxa de falsos positivos do Argus: % de alertas que não eram anomalias reais (meta: < 15% após calibração, monitorado pelo Nexus)
- Taxa de falsos negativos do Vega: % de ações bloqueadas incorretamente (meta: < 10%, balanceado com taxa de falsos positivos < 1%)
- Freshness SLA compliance: % de pipelines que entregam dados dentro do SLA de freshness contratado (meta: > 99% para P1, > 95% para P2)
- Custo de horas de engenharia salvas: horas/mês que seriam gastas em investigação e recuperação manual (meta: 20-40h/mês em clientes com 15+ pipelines ativos)
- Pipeline Health Score médio: média dos health scores de todos os pipelines monitorados (0-100, meta: > 85 em 90 dias)
- Tempo de onboarding de novo pipeline: horas para onboarding completo de um novo pipeline (baseline + thresholds + recovery_policy + assignees) (meta: < 4h por pipeline)

## Integrações

- Airbyte / Matillion / Workato / Peliqan — ETL tools principais: webhooks de execução (success/failure), API para reexecução de runs (Finn), acesso a logs de run, configuração de schedules
- Supabase / Postgres / BigQuery / Snowflake — destinos de dados: acesso de leitura para schema inspection (Argus, Rémi), acesso de escrita limitado a staging para patches (Finn), schema history e fingerprints (Nexus)
- ClickUp (Brain² / Super Agents / Autopilot Agents + MCP) — hub de tasks e prova de trabalho: task por incidente (Loki), HITL L³ approval flow, Weekly Reports, integração com AIOX via espelhamento de workflow
- Slack — notificações em tempo real: P1/P2 alertas imediatos com context card (pipeline, root cause, ação tomada ou pendente), HITL L3 aprovação urgente, Weekly Incident Report no canal #data-reliability
- Langfuse — observabilidade OTEL: tracing de cada incidente (deteccao -> diagnostico -> validacao -> recuperacao), evals automatizados por tipo de root cause, quality gates (dev 70% / staging 85% / prod 95% task success), dashboard de MTTR e MTTD por pipeline
- PagerDuty / Datadog / incident.io — AIOps integration: receber alertas de infra correlacionados (ex: source database down confirmado pelo Datadog antes do Remi investigar), escalonamento de P1 para on-call engineer via PagerDuty quando HITL nao responde no SLA
- GitHub / GitLab — acesso de leitura ao repositório de transformações (Coda para identificar linha exata do bug), PR automático com fix sugerido para aprovação humana em casos de transformation bug
- dbt (se aplicável) — acesso a manifests e lineage graph para mapeamento de dependências downstream (Rémi/Coda), identificação de modelos afetados por schema drift
- Claude Agent SDK / LangGraph — orquestração multi-agente (Orion coordenando Argus, Rémi, Finn, Coda, Nexus, Vega, Loki), state management do pipeline de incidentes
- MCP Servers (camada de integração universal) — ClickUp MCP, Supabase MCP, GitHub MCP para acesso padronizado sem implementação custom por cliente

## Entregável (prova de trabalho)

Incident Card no ClickUp por anomalia detectada (prova de trabalho verificavel): (1) Alerta estruturado do Argus — pipeline, timestamp, anomaly_type, severity, evidencia bruta; (2) Root Cause Report do Remi — root cause confirmado, confidence score, evidence chain, recommended action; (3) Verification Report do Vega — verdict APPROVED/BLOCKED com justificativa por dimensao; (4) Recovery Action Record do Finn (para auto-resolucao) OU Fix Plan do Coda (para HITL L3) — acao tomada, resultado, rows recovered, freshness restored at; (5) Post-recovery freshness timestamp confirmando que o pipeline voltou ao SLA; (6) Task fechada no ClickUp com historico completo de timestamps por etapa (MTTD e MTTR calculados automaticamente). Bonus semanal: Weekly Incident Report com metricas agregadas de confiabilidade e ROI de horas salvas.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Incident Response Squad (5 ag, squads.sh) — arquitetura de detecção -> diagnóstico -> remediação diretamente aplicável ao core loop do Self-Healing ETL. Reutilizar o padrão de severity classification (P1-P4), o escalation flow para HITL e o post-mortem template (base para o Incident Card do Loki).
- Data Quality Guardian (5 ag, squads.sh) — padrão de validação multi-dimensão e anomaly detection reutilizável pelo Argus e Rémi. O pipeline de schema validation, null rate monitoring e volume anomaly detection do DQG pode ser adaptado diretamente como módulo de detecção do Argus.
- Skeptic Protocol (5 ag, red-team/QA, myclaude) — padrão de critic/verifier adversarial com multi-dimensão de validação reutilizável pelo Vega. O protocolo de verificação de proporcionalidade, reversibilidade e blast radius espelha o Skeptic Protocol adaptado para ações automáticas de recuperação.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O5 · TopSquad de Operações Técnicas: SRE, SLA & Data Pipelines** — Mantém a operação de pé: incidentes, SLAs e pipelines que se curam sozinhos.

- **Missão:** A espinha dorsal técnica: detecta e gere incidentes (SRE), monitora SLAs e saúde operacional, e mantém pipelines de dados que se auto-corrigem. Garante que toda a operação agêntica continue rodando — e confiável.
- **Por que consolidar:** Os três respondem ao mesmo evento — "algo quebrou ou vai quebrar" — em camadas distintas (serviço, SLA, dados). Monitoramento detecta, SRE responde, ETL se cura; é o mesmo loop de observabilidade → ação. Unidos, compartilham telemetria e runbooks em vez de três sistemas de alerta concorrentes.
- **Squads irmãos:** AI SRE — Incident Management, SLA & Health Monitoring Operacional, Self-Healing ETL

## Estrutura

```
ops-cs-self-healing-etl/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
