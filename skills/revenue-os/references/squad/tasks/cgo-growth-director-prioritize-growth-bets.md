---
task: Prioritize Growth Bets
responsavel: "@cgo-growth-director"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - growth_backlog: Backlog de iniciativas (experimentos, features, otimizacoes)
  - growth_system: Sistema AARRR ativo com metricas atuais
  - available_capacity: Horas/semana dos executores (analysts + managers)
Saida: |
  - prioritized_bets: Top 5-10 apostas priorizadas com score
  - test_window_per_bet: Janela de teste definida por aposta
  - kill_criteria_per_bet: Criterio de kill se aposta nao validar
Checklist:
  - "[ ] Rankear por Impacto x Esforco x Confianca (ICE score)"
  - "[ ] Definir janela de teste por aposta"
  - "[ ] Definir kill criteria (o que cancela a aposta)"
  - "[ ] Limitar a 3-5 apostas simultaneas (foco)"
---

# *prioritize-growth-bets

Prioriza apostas de crescimento usando ICE score e regras de foco.

## Step-by-Step

1. **Coletar backlog** — Listar todas as iniciativas propostas (por qualquer fonte: produto, vendas, marketing, dados).
2. **Avaliar cada aposta em ICE** — Impact (1-10), Confidence (1-10), Ease (1-10). Score = media.
3. **Mapear estagio AARRR afetado** — Cada aposta impacta 1+ estagios. Balancear portfolio (nao concentrar tudo em aquisicao).
4. **Calcular capacidade** — Horas disponiveis vs horas estimadas por aposta.
5. **Priorizar top 3-5** — Pela ICE score, respeitando capacidade e balanco AARRR.
6. **Definir janela de teste** — 2-6 semanas por aposta. Definir antes, nao durante.
7. **Definir kill criteria** — Quando a aposta e considerada fracassada e cortada.

## Veto Conditions

- VETO se ICE score de uma aposta for baseado em opiniao sem dados → deve ter evidencia minima
- VETO se >5 apostas simultaneas → foco diluido, reduzir
- VETO se todas as apostas concentrarem no mesmo estagio AARRR → sistema nao evolui balanceado
- VETO se uma aposta nao tiver kill criteria → vira zumbi ate alguem perceber que esta morta

## Output Example

```yaml
prioritized_bets:
  - id: BET-01
    nome: "Implementar chat AI no onboarding"
    estagio_aarrr: ativacao
    ice:
      impact: 8
      confidence: 7
      ease: 6
      score: 7.0
    owner: "@growth-senior-manager"
    janela_teste: "4 semanas"
    kill_criteria: "Ativacao em 14 dias nao sobe de 60% para 75%"
    effort_horas: 40

  - id: BET-02
    nome: "Paid social carousel com case real"
    estagio_aarrr: aquisicao
    ice:
      impact: 7
      confidence: 8
      ease: 9
      score: 8.0
    owner: "@marketing-senior-analyst"
    janela_teste: "2 semanas"
    kill_criteria: "CTR <1.5% ou CPC >R$ 5 apos R$ 3k investidos"
    effort_horas: 16

  - id: BET-03
    nome: "Email de onboarding - sequencia 5 emails"
    estagio_aarrr: ativacao
    ice:
      impact: 6
      confidence: 9
      ease: 8
      score: 7.7
    owner: "@marketing-senior-analyst"
    janela_teste: "3 semanas"
    kill_criteria: "Open rate <40% ou CTR <8%"
    effort_horas: 24

  - id: BET-04
    nome: "Programa de referral ativo"
    estagio_aarrr: referral
    ice:
      impact: 9
      confidence: 5
      ease: 4
      score: 6.0
    owner: "@sales-system-operator"
    janela_teste: "6 semanas"
    kill_criteria: "<5% dos clientes ativam referral em 6 semanas"
    effort_horas: 60

balanco_aarrr:
  aquisicao: 1 aposta
  ativacao: 2 apostas
  retencao: 0 apostas
  revenue: 0 apostas
  referral: 1 aposta

capacidade_total:
  horas_disponiveis_mes: 160
  horas_alocadas: 140
  buffer: 20
```

## Completion Criteria

- Top 3-5 apostas priorizadas com ICE score completo
- Cada aposta tem janela de teste + kill criteria + owner
- Balanco AARRR sem concentracao excessiva em 1 estagio
- Capacidade respeitada (sem overcommit)

## Handoff

Apostas distribuidas para `@growth-senior-manager` e `@growth-senior-analyst` executarem. Kill criteria monitorados em `*control-weekly-metrics`.
