---
name: "Update Status Page"
description: "Atualização de status page conduzida pelo StatusUpdater: recebe os detalhes do incidente e a severidade, seleciona o template de comunicação (investigating, identified, monitoring, resolved), compõe e publica a mensagem no status page externo e no canal interno, notifica stakeholders conforme a matriz de severidade, registra o notification-log.json, agenda a próxima atualização e mantém o status-update.md com o histórico."

inputs:
  - name: incidentDetails
    type: json
    description: "Detalhes do incidente (alerta, descrição, serviços afetados) — do pipeline de incidente"
    required: true
  - name: remediationStatus
    type: string
    description: "Status da remediação — do runbook-executor (executeRunbook())"
    required: false
  - name: severityLevel
    type: string
    description: "Nível de severidade — triagem inicial ou root-cause-correlator"
    required: true

outputs:
  - name: statusUpdate
    type: file
    description: "status-update.md com o histórico de atualizações, para postmortem-writer"
    required: true
  - name: notificationLog
    type: json
    description: "Log de notificações enviadas, para postmortem-writer"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Status page atualizado dentro do SLA de resposta"
  - blocker: true
    criteria: "Stakeholders corretos notificados para o nível de severidade"
  - blocker: false
    criteria: "Linguagem empática e profissional na comunicação"
---

# Update Status Page

## Flow

```
1. Receber detalhes do incidente e severidade
2. Selecionar template de comunicação apropriado
3. Compor mensagem de status (investigating/identified/monitoring/resolved)
4. Publicar atualização no status page externo
5. Publicar atualização no canal interno (#incidents)
6. Notificar stakeholders conforme matriz de severidade
7. Logar notificação no notification-log.json
8. Agendar próxima atualização conforme frequência da severidade
9. Atualizar status-update.md com histórico
```

## Status Transitions

```
investigating → identified → monitoring → resolved
     ↓              ↓
  escalated     partial_fix → monitoring → resolved
```

## Elicitation

- "Qual o nível de severidade? (SEV1, SEV2, SEV3, SEV4)"
- "Qual o impacto atual nos usuários?"
- "Já foi identificada a causa raiz?"
- "Qual o status atual da remediação?"

## Performance

- **Duração esperada:** 2-5 minutos por atualização
- **Custo estimado:** ~0
- **Cacheável:** não
- **Paralelizável:** sim

## Error Handling

- **Estratégia:** retry (máx. 3 tentativas, backoff exponencial base=2s, max=15s)
- **Fallback:** se o status page estiver indisponível, notificar via Slack/email diretamente
- **Notificação:** root-cause-correlator
