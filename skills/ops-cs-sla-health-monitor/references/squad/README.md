# Squad de SLA & Health Monitoring Operacional

> SLA breach nunca mais — o squad prevê a violação horas antes e escala antes do prazo explodir.

**Área:** Operações & CS · **TopSquad:** O5 Operações Técnicas: SRE, SLA & Data Pipelines · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

SLAs são monitorados reativamente: a equipe só descobre a violação quando o prazo já estourou, gerando multas contratuais, clientes insatisfeitos e churn evitável. O problema raiz é triplo: (1) nenhum sistema calcula ritmo de resolução em tempo real — 'quantas horas de trabalho restam vs. quanto tempo tenho?'; (2) complexidade do ticket não é considerada no cálculo — um ticket P1 com 3 dependências externas consome 4x mais tempo que o SLA assume; (3) escalonamento é manual e baseado em memória dos supervisores. O SLA Monitor Agent corre uma engine de previsão contínua sobre cada ticket aberto: combina tempo decorrido, complexidade estimada, ritmo histórico de resolução por tipo de ticket, carga atual da fila e disponibilidade do agente responsável para calcular a 'probabilidade de breach' a cada 15 minutos. Quando a probabilidade cruza o threshold configurado (default 70%), dispara escalonamento automático no ClickUp — cria sub-task, notifica supervisor, reatribui ou convoca recurso adicional — antes que o prazo estoure.

## Impacto esperado

Para empresas com contratos de SLA (B2B SaaS, serviços gerenciados, implementação): multas contratuais por breach tipicamente variam de 0,5% a 5% do ARR mensal por incidente — evitar 10 breaches/mês em contratos de R$50k/mês = R$25-250k de proteção de receita. SLA compliance subindo de 72% para >95% (benchmark Zendesk 2024 para equipes sem monitoramento preditivo) representa redução de NPS detractor de 40-60% (clientes que reportam SLA violado têm 3x mais probabilidade de churn em 90 dias). ROI estimado: setup de R$20-40k com payback em 1-3 ciclos de cobrança se o cliente tiver histórico de multas. Para volume de 200 tickets/mês com SLA, custo operacional do squad (~R$800-2.000/mês em tokens) vs. valor de 1 multa evitada (R$5-25k) = ROI de 500-3.000% por evento. Métrica-âncora: % de breaches evitados (target: >90%), antecedência média do alerta (target: >2h antes do prazo), e aderência global ao SLA (target: >97%).

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `sentinela-mor-persona-vitor-analista-senior-de-operacoes-com-obsessao-por-sla` · Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA | Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SL… | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Radar — Varredor de Fila SLA | L0 · worker determinístico | `coletar-tickets-sla.md` |
| `decifra` · Decifra | Decifra — Analisadora de Complexidade | L1 · worker autônomo | `calcular-complexidade-tickets.md` |
| `cronos` · Cronos | Cronos — Motor de Previsão de Breach | L1 · worker autônomo | `calcular-probabilidade-de-breach.md` |
| `alarme` · Alarme | Alarme — Agente de Escalonamento Proativo | L3 · aprovação humana | `escalonar-tickets.md` |
| `histos` · Histos | Histos — Analista de Padrões e Tendências | L1 · worker autônomo | `analisar-dados-de-sla.md` |
| `ancora` · Âncora | Âncora — Registrador de Evidências e Prova de Trabalho | L0 · worker determinístico | `registrar-prova-de-trabalho.md` |
| `cetico-de-sla` · Cético de SLA | Cético de SLA — Cassandra | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-sla-health-monitor:sentinela-mor-persona-vitor-analista-senior-de-operacoes-com-obsessao-por-sla` (ou instale via `npx squads add ./ops-cs-sla-health-monitor`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-sla-health-monitor-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade baixa (interrompe o fluxo do agente atual).
- Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders. Ação de alto impacto e irreversível em termos de alarme organizacional.
- Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes do envio. Toda comunicação com cliente é revisada por humano.
- Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. Ocorre quando dados são ambíguos ou incompletos.
- Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para avaliação manual do risco de breach. Cronos não especula sem dados.
- Histos detecta breach rate semanal acima do threshold crítico: relatório é revisado por ops manager antes de publicação, que decide se aciona revisão de processo ou ajuste de SLAs contratuais.
- Recalibração mensal do modelo do Cronos (Histos gera novo dataset): pesos atualizados são revisados por ops lead antes de ir para produção. Mudança no modelo preditivo é sempre revisada por humano.

## KPIs

- % de breaches evitados: tickets que teriam breachado (Cronos detectou) mas foram resolvidos no prazo após escalonamento proativo do Alarme (target: >90%, baseline estimado 0% sem o squad — 100% reativo)
- Antecedência média do alerta: quantas horas antes do deadline o Alarme disparou o escalonamento (target: >2h para P1, >4h para P2; quanto mais cedo, mais tempo para agir)
- SLA compliance global: % de tickets fechados dentro do prazo contratual (target: >97%, baseline típico sem monitoramento preditivo: 65-80%)
- Taxa de falsos positivos: escalonamentos que o Alarme disparou mas o ticket seria resolvido no prazo sem intervenção (target: <15% — acima disso, supervisor perde confiança no squad)
- Taxa de falsos negativos: tickets que breacharam sem alerta do squad (target: <3% — este é o KPI mais crítico, medido pelo Cassandra)
- Acurácia do Cronos: correlação entre breach_probability previsto e resultado real (target: AUC >0.85, medido pelo Histos mensalmente)
- Tempo médio de resposta ao escalonamento: quanto tempo o supervisor leva para agir após notificação do Alarme (target: <30min para P1 — mede efetividade humana, não do squad)
- Multas contratuais evitadas por mês: valor financeiro de breaches que não ocorreram (calculado pelo Histos com base nos contratos — o KPI que mais vende o squad para o board)
- Custo por ciclo de monitoramento: tokens consumidos por ciclo de 15min × número de tickets ativos (target: <R$0,10 por ticket/ciclo para manter ROI positivo em qualquer volume)

## Integrações

- ClickUp (Brain2 / Autopilot Agents + API MCP): hub central do squad — campos customizados de SLA (sla_deadline, breach_probability, risk_status, sla_monitor_log), sub-tasks de escalonamento, dashboard de KPIs em tempo real, view de tickets-em-risco filtrada por VERMELHO/AMARELO
- Zendesk / Intercom (via MCP server): sistemas de helpdesk de onde o Radar coleta tickets em tempo real via API; campo de SLA deadline lido nativamente das configurações de SLA do helpdesk
- Slack (Webhooks + Slack MCP): canal dedicado '#sla-monitor-alertas' para notificações do Alarme com template estruturado (ticket, deadline, score, link direto) + canal '#sla-war-room' para P1 críticos + DM para supervisor de plantão
- HubSpot / Salesforce CRM (via MCP): dados de tier do cliente, ARR, data de renovação e cláusulas de SLA contratual — alimentam o cálculo de prioridade do Cronos e a definição de threshold de escalonamento por conta
- ChurnZero / Custify / Chargebee: health score do cliente e status de renovação — agravante de risco quando cliente em renovação tem ticket em breach risk (complexity multiplier adicional)
- Supabase / Postgres: banco de dados de estado persistente do squad — log de auditoria de todos os ciclos, histórico de breach/não-breach para recalibração do Cronos pelo Histos, pesos do modelo preditivo, perfis de velocidade dos agentes
- Langfuse (OTEL): observabilidade completa do squad — tracing de cada ciclo de 15min (latência total, tokens por agente, scores gerados, decisões tomadas), quality gates por ambiente (dev 70% / staging 85% / prod 95% de acurácia preditiva), dashboard de drift do modelo
- Google Calendar / Outlook Calendar (via API): disponibilidade dos supervisores de plantão para o Alarme saber quem notificar em qual escalonamento (integração com escala de plantão da equipe)
- PagerDuty / incident.io (opcional, para clientes com stack de AIOps): integração para tickets P1 que viram incidentes — o Alarme pode criar um PagerDuty incident além do war-room no ClickUp
- MCP Servers (camada de integração universal): MCP ClickUp, MCP Zendesk/Intercom, MCP CRM — abstraem chamadas de API para os workers e garantem rate limiting seguro

## Entregável (prova de trabalho)

Artefato de prova de trabalho auditável e verificável no ClickUp: para cada ticket com SLA ativo, campo 'sla_monitor_log' com histórico de todos os ciclos de avaliação (timestamp, breach_probability_score, risk_status, ação_tomada). Para cada escalonamento proativo, sub-task vinculada ao ticket-pai com: escalation_timestamp (anterior ao sla_deadline), triggered_by (Cronos score que atingiu threshold), notified_parties (supervisor + canal), recommended_action, resolution_outcome (breach evitado: sim/não, preenchido ao fechar o ticket). Dashboard de SLA Health em tempo real no ClickUp mostrando: breach_rate_7d, avg_antecedencia_horas, sla_compliance_pct por tier de cliente, top-3 causas de risco esta semana. Relatório semanal do Histos com tendências e recomendações. Este artefato é o que o cliente apresenta ao seu board para provar que SLA está sendo gerenciado proativamente — não de forma reativa.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Incident Response Squad (5 ag) — base direta para o módulo de war-room P1 do Alarme e a lógica de correlação de alertas; reutilizar o padrão de escalonamento em cascata e o state machine de incidentes (OPEN/INVESTIGATING/RESOLVED) adaptado para tickets em breach risk
- Five Vitals (diagnostico de sistemas) — arquitetura de health check contínuo que inspira o ciclo de 15min do Sentinela-Mor e o dashboard de 'vitais' operacionais; reutilizar o padrão de scoring multi-dimensional com semáforo VERDE/AMARELO/VERMELHO e alertas por threshold
- Skeptic Protocol (5 ag) — arquitetura de red-team/QA que inspira o papel da Cassandra; reutilizar o padrão de validação adversarial pré-ação (bloquear escalonamentos inconsistentes) e o loop de feedback para recalibração de thresholds com base em falsos positivos/negativos

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O5 · TopSquad de Operações Técnicas: SRE, SLA & Data Pipelines** — Mantém a operação de pé: incidentes, SLAs e pipelines que se curam sozinhos.

- **Missão:** A espinha dorsal técnica: detecta e gere incidentes (SRE), monitora SLAs e saúde operacional, e mantém pipelines de dados que se auto-corrigem. Garante que toda a operação agêntica continue rodando — e confiável.
- **Por que consolidar:** Os três respondem ao mesmo evento — "algo quebrou ou vai quebrar" — em camadas distintas (serviço, SLA, dados). Monitoramento detecta, SRE responde, ETL se cura; é o mesmo loop de observabilidade → ação. Unidos, compartilham telemetria e runbooks em vez de três sistemas de alerta concorrentes.
- **Squads irmãos:** AI SRE — Incident Management, SLA & Health Monitoring Operacional, Self-Healing ETL

## Estrutura

```
ops-cs-sla-health-monitor/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
