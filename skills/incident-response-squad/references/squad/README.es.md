# incident-response-squad

Squad especialista en respuesta a incidentes para DevOps/SRE.

## Descripción General

El **incident-response-squad** es un squad completo que cubre todo el pipeline de respuesta a incidentes:

1. **Análisis de Logs** — Agregación y análisis de logs de múltiples fuentes (CloudWatch, ELK, Splunk, Datadog)
2. **Correlación de Causa Raíz** — Correlación de señales de 20-45 herramientas de monitoreo, mapeo de blast radius
3. **Ejecución de Runbooks** — Runbooks automatizados para rollback, scaling, restart y remediación
4. **Comunicación de Estado** — Actualización de status pages y notificación a stakeholders
5. **Post-Mortem** — Generación de documentos blameless con timeline, action items y lecciones aprendidas

**Pain Point:** El 65% del tiempo de resolución se gasta diagnosticando la causa raíz; las empresas gestionan 20-45 herramientas de monitoreo.

## Agentes

| Agente | ID | Rol |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | Analizador de logs multi-fuente |
| 🔍 Correlator | `root-cause-correlator` | Correlacionador de causa raíz y blast radius |
| ⚡ RunbookExec | `runbook-executor` | Ejecutor de runbooks de remediación |
| 📢 StatusUpdater | `status-page-updater` | Gestor de comunicación y status page |
| 📝 PostMortem | `postmortem-writer` | Generador de post-mortem blameless |

## Flujos de Trabajo

| Workflow | Comando | Descripción | Duración |
|---|---|---|---|
| Full Incident Response | `*respond-incident` | Pipeline completo: de la alerta al post-mortem | 30-90 min |
| Rapid Triage | `*triage-incident` | Triaje rápido: análisis, causa raíz, comunicación | 10-20 min |

## Comandos Disponibles

| Comando | Agente | Descripción |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | Analizar logs de un incidente |
| `*search-logs` | LogAnalyzer | Buscar patrón específico en los logs |
| `*correlate-signals` | Correlator | Correlacionar señales de múltiples fuentes |
| `*find-root-cause` | Correlator | Identificar causa raíz más probable |
| `*execute-runbook` | RunbookExec | Ejecutar runbook de remediación |
| `*list-runbooks` | RunbookExec | Listar runbooks disponibles |
| `*update-status` | StatusUpdater | Actualizar status page |
| `*notify-stakeholders` | StatusUpdater | Notificar stakeholders |
| `*write-postmortem` | PostMortem | Generar post-mortem blameless |
| `*generate-timeline` | PostMortem | Generar timeline del incidente |

## Inicio Rápido

```
# Activar el correlacionador (orquestador principal)
/irs:agents:root-cause-correlator

# Pipeline completo de respuesta a incidente
*respond-incident

# Triaje rápido
*triage-incident

# Solo análisis de logs
*analyze-logs

# Solo post-mortem
*write-postmortem
```

## Usuarios Objetivo

- SREs (Site Reliability Engineers)
- Ingenieros de DevOps
- Ingenieros de guardia (on-call)
- CTOs y líderes técnicos

## Requisitos

- Acceso a herramientas de monitoreo (Datadog, Prometheus, Grafana)
- Acceso a plataformas de log (ELK, Splunk, CloudWatch)
- Acceso al status page (Statuspage.io, Atlassian)
- Canal de comunicación configurado (Slack #incidents)

## Autoría

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.
