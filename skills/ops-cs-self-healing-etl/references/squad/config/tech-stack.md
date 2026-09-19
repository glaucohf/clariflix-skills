# Tech stack (integrações da especificação)

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

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
