# Tech stack (integrações da especificação)

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

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
