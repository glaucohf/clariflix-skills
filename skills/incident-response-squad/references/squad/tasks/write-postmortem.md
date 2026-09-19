---
name: "Write Post-Mortem"
description: "Geração de post-mortem blameless conduzida pelo PostMortem: coleta todos os artefatos do incidente, constrói a timeline completa (alerta → detecção → resposta → resolução), escreve o resumo executivo, documenta a causa raiz em linguagem blameless, lista fatores contribuintes sistêmicos, quantifica o impacto técnico/negócio/usuário, registra o que funcionou e o que pode melhorar, define action items com prioridade/owner/prazo, extrai lições aprendidas e gera o postmortem.md final."

inputs:
  - name: logAnalysisReport
    type: file
    description: "Relatório de análise de logs — do log-analyzer (analyzeIncidentLogs())"
    required: true
  - name: rootCauseReport
    type: file
    description: "Root cause report — do root-cause-correlator (correlateRootCause())"
    required: true
  - name: executionLog
    type: file
    description: "Execution log de remediação — do runbook-executor (executeRunbook())"
    required: false
  - name: statusUpdates
    type: file
    description: "Histórico de status updates — do status-page-updater (updateStatusPage())"
    required: false
  - name: timelineEvents
    type: array
    description: "Eventos com timestamps de todos os agentes"
    required: true

outputs:
  - name: postmortemDocument
    type: file
    description: "postmortem.md completo com todas as seções obrigatórias"
    required: true
  - name: actionItems
    type: array
    description: "Lista estruturada de action items com owner, prioridade e prazo"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Post-mortem contém todas as seções obrigatórias"
  - blocker: true
    criteria: "Action items têm owner, prioridade e prazo definidos"
  - blocker: true
    criteria: "Linguagem é blameless — foco em sistemas, não indivíduos"
  - blocker: false
    criteria: "Impacto quantificado (usuários afetados, duração, custo)"
---

# Write Post-Mortem

## Flow

```
1. Coletar todos os artefatos do incidente
2. Construir timeline completa (alerta → detecção → resposta → resolução)
3. Escrever resumo executivo do incidente
4. Documentar causa raiz em linguagem blameless
5. Listar fatores contribuintes (sistêmicos)
6. Quantificar impacto (técnico, negócio, usuário)
7. Documentar resposta (o que funcionou, o que não funcionou)
8. Definir action items com prioridade, owner e prazo
9. Extrair lições aprendidas
10. Gerar postmortem.md final
```

## Estrutura do Post-Mortem

```markdown
# Post-Mortem: [Título do Incidente]

## Resumo
- Data: YYYY-MM-DD
- Duração: X horas Y minutos
- Severidade: SEVN
- Impacto: [resumo]

## Timeline
| Hora | Evento |
|------|--------|
| HH:MM | ... |

## Causa Raiz
[Análise técnica blameless]

## Fatores Contribuintes
- [Fator 1]
- [Fator 2]

## Impacto
- Usuários afetados: N
- Duração total: X
- Perda estimada: $Y

## O que funcionou bem
- [Item 1]

## O que pode melhorar
- [Item 1]

## Action Items
| Item | Owner | Prioridade | Prazo |
|------|-------|-----------|-------|
| ... | ... | P1/P2/P3 | YYYY-MM-DD |

## Lições Aprendidas
- [Lição 1]
```

## Performance

- **Duração esperada:** 15-45 minutos
- **Custo estimado:** ~0
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** retry (máx. 2 tentativas, delay fixo de 30s)
- **Fallback:** gerar post-mortem parcial com os dados disponíveis e marcar as seções incompletas
- **Notificação:** root-cause-correlator
