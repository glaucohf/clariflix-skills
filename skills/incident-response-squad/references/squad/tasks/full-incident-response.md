---
name: "Full Incident Response"
description: "Pipeline completo de resposta a incidentes como decision-support, orquestrado pelo Correlator: encadeia em sequência análise dos logs fornecidos, correlação de causa raiz, geração do runbook de remediação como spec executável, redação das mensagens de status e post-mortem blameless, consolidando todos os artefatos num incident response package. A execução das ações de remediação e a publicação dos status ficam a cargo do operador. Em falha de qualquer fase compõe o status parcial e escala para engenharia sênior, respeitando os timeline targets por severidade."

inputs:
  - name: incidentAlert
    type: string
    description: "Descrição do alerta — do usuário ou do sistema de monitoramento"
    required: true
  - name: severity
    type: string
    description: "Nível de severidade (SEV1, SEV2, SEV3, SEV4) — do usuário ou da triagem automática"
    required: true

outputs:
  - name: incidentResponsePackage
    type: json
    description: "Pacote consolidado da resposta ao incidente, para usuário e stakeholders"
    required: true
  - name: logAnalysisReport
    type: file
    description: "log-analysis-report.md"
    required: true
  - name: rootCauseReport
    type: file
    description: "root-cause-report.md"
    required: true
  - name: executionLog
    type: file
    description: "execution-log.md — plano/spec de remediação para o operador executar, não registro de ações já executadas"
    required: false
  - name: statusUpdate
    type: file
    description: "status-update.md — drafts das mensagens de status prontas para publicação pelo operador"
    required: true
  - name: postmortemDocument
    type: file
    description: "postmortem.md"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Causa raiz identificada com confidence score >= 50%"
  - blocker: true
    criteria: "Runbook de remediação especificado e validado (execução pelo operador)"
  - blocker: true
    criteria: "Mensagens de status compostas dentro do SLA (publicação pelo operador)"
  - blocker: true
    criteria: "Post-mortem completo com action items"
  - blocker: false
    criteria: "Tempo total de resposta dentro do target para a severidade"
---

# Full Incident Response

## Pipeline

```
Fase 1: Análise de Logs      → @log-analyzer          → analyzeIncidentLogs()
Fase 2: Causa Raiz            → @root-cause-correlator → correlateRootCause()
Fase 3: Spec de Remediação    → @runbook-executor      → buildRemediationRunbook()
Fase 4: Drafts de Status      → @status-page-updater   → composeStatusUpdates()
Fase 5: Post-Mortem           → @postmortem-writer     → writePostMortem()
```

## Elicitation

### Fase 1 — Alerta
- "Qual o alerta ou descrição do incidente?"
- "Qual a severidade? (SEV1, SEV2, SEV3, SEV4)"
- "Quando o problema começou (ou foi detectado)?"
- "Quais serviços ou componentes são suspeitos?"

### Fase 2 — Contexto
- "Quais ferramentas de monitoramento estão disponíveis?"
- "Houve algum deploy ou mudança recente?"
- "Existe mapa de dependências dos serviços?"

### Fase 3 — Remediação
- "Qual runbook de remediação devo especificar para você aplicar?"
- "Qual ambiente será afetado? (staging, production)"
- "Há restrições de janela de mudança a refletir no plano?"

### Fase 5 — Post-Mortem
- "Quem deve ser owner dos action items?"
- "Qual o prazo para publicação do post-mortem?"
- "Há impacto financeiro a ser documentado?"

## Timeline Targets por Severidade

| Severidade | Detecção | Resposta | Comunicação | Resolução |
|---|---|---|---|---|
| SEV1 | < 5 min | < 15 min | < 5 min | < 1h |
| SEV2 | < 15 min | < 30 min | < 15 min | < 4h |
| SEV3 | < 30 min | < 1h | < 30 min | < 24h |
| SEV4 | < 4h | < 8h | < 4h | < 1 semana |

## Performance

- **Duração esperada:** 30-90 minutos
- **Custo estimado:** variável conforme as ações de remediação
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** escalate (retry máx. 2 tentativas, backoff exponencial base=10s, max=60s)
- **Fallback:** se qualquer fase falhar, comunicar status parcial e escalar para engenharia sênior
- **Notificação:** status-page-updater
