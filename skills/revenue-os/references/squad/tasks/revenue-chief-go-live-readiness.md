---
task: Go-Live Revenue Readiness
responsavel: "@revenue-chief"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - launch_scope: Escopo do lancamento (oferta, canais, volume esperado)
  - system_status: Estado de funil, CRM, tracking e stack comercial
Saida: |
  - readiness_report: PASS/FAIL por gate com razoes
  - critical_fixes: Ajustes obrigatorios antes de go-live
  - go_no_go_decision: Decisao final GO ou DELAY
Checklist:
  - "[ ] Oferta final aprovada (ICP + pricing + garantias)"
  - "[ ] Funil funcional (LP carrega + checkout processa teste)"
  - "[ ] CRM com pipeline ativo + follow-up automatizado"
  - "[ ] Tracking ativo (UTM, events, attribution)"
  - "[ ] Contingencia para volume 3x acima do esperado"
---

# *go-live-readiness

Valida se o sistema comercial esta pronto para entrar no ar sem gerar caos operacional.

## Step-by-Step

1. **Executar checklist funcional** — LP carrega <3s, checkout processa R$1 real, dashboard atualiza em tempo real, CRM recebe lead.
2. **Testar ponta-a-ponta** — Simular jornada: anuncio → LP → lead capture → email sequence → demo booking → pagamento.
3. **Validar tracking** — UTM parameters chegando no CRM + dashboard, events critical sendo capturados, attribution minima funcionando.
4. **Verificar contingencias** — Se volume 3x maior que esperado, sistema aguenta? Se um canal cair, funil ainda funciona?
5. **Revisar rollback plan** — Se algo der errado nas primeiras 4h, como voltar pro estado anterior?
6. **Gerar readiness_report** — PASS/FAIL por gate com razoes especificas.
7. **Decidir GO/DELAY** — PASS em todos gates criticos = GO. Qualquer FAIL em gate critico = DELAY.

## Veto Conditions

- VETO se qualquer gate critico estiver FAIL (oferta, checkout, CRM, tracking) → DELAY obrigatorio
- VETO se rollback plan nao existir → sem plano B, ir ao ar e risco desnecessario
- VETO se time de suporte comercial nao souber responder objecoes basicas → treinar antes de go-live

## Output Example

```yaml
readiness_report:
  data: "2026-05-13"
  gates:
    - gate: "Oferta aprovada"
      status: PASS
      razao: "ICP + pricing + garantias documentados e assinados"

    - gate: "Funil funcional"
      status: PASS
      teste: "Jornada completa executada 3x sem erro"

    - gate: "Checkout processa pagamento real"
      status: PASS
      teste: "R$ 1 debitado e confirmado via webhook"

    - gate: "CRM recebe leads"
      status: FAIL
      razao: "Integracao LP->CRM perdendo 20% dos leads"
      impacto: critico

    - gate: "Tracking ativo"
      status: PASS

    - gate: "Contingencia 3x volume"
      status: PASS
      teste: "Load test com 150 leads/min sem degradacao"

    - gate: "Rollback plan"
      status: PASS

critical_fixes:
  - fix: "Corrigir integracao LP->CRM"
    owner: "@revops-automation-engineer"
    deadline: "2026-05-14"
    impacto_se_nao_corrigido: "20% dos leads perdidos = perda de ~R$ 15k MRR no primeiro mes"

go_no_go_decision:
  decisao: DELAY
  nova_data_proposta: "2026-05-16"
  razao: "Gate CRM em FAIL com impacto critico"
```

## Completion Criteria

- Todos os 7 gates avaliados com PASS/FAIL e razao
- Se algum FAIL em gate critico: critical_fixes com owner + deadline
- Decisao GO ou DELAY clara com nova data se DELAY
- Rollback plan validado

## Handoff

Se GO → handoff para `*orchestrate-commercial-stack` para ativacao final. Se DELAY → critical_fixes distribuidos, reagendamento automatico.
