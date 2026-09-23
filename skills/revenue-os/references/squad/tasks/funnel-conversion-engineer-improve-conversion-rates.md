---
task: Improve Conversion Rates
responsavel: "@funnel-conversion-engineer"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - funnel_metrics: Conversao atual por etapa do funil
  - friction_log: Gargalos mapeados em *design-funnel-journey
  - benchmark_targets: Benchmarks da industria por etapa
Saida: |
  - cvr_action_plan: Plano de melhoria priorizado
  - test_hypotheses: Hipoteses de teste com desenho experimental
  - quick_wins: Acoes de baixo esforco + alto impacto para executar imediatamente
Checklist:
  - "[ ] Priorizar gargalos por impacto na receita"
  - "[ ] Separar quick wins de testes estruturados"
  - "[ ] Definir 3 testes iniciais com hipotese clara"
  - "[ ] Definir metrica de sucesso por teste"
---

# *improve-conversion-rates

Prioriza e executa melhorias de conversao com foco nos maiores gargalos do funil.

## Step-by-Step

1. **Comparar conversao vs benchmark** — Para cada etapa, calcular gap.
2. **Ranquear por impacto na receita** — Gap * volume da etapa = receita potencial recuperada.
3. **Separar quick wins vs testes** — Quick wins: <4h de implementacao + certeza de melhora. Testes: precisa de hipotese + amostra + analise.
4. **Listar hipoteses de teste** — Para cada gargalo, 2-3 hipoteses de solucao.
5. **Desenhar experimento por hipotese** — Variante A/B, metrica, duracao, amostra minima.
6. **Executar quick wins primeiro** — Ganhar velocidade em 1-2 semanas antes dos testes longos.
7. **Rodar testes em paralelo quando possivel** — Se testes afetam etapas diferentes, podem rodar juntos.

## Veto Conditions

- VETO se melhorar etapa que tem conversao >benchmark → atacar gargalo maior primeiro
- VETO se teste nao tiver hipotese falseavel → experimento e teatro
- VETO se quick win tiver >4h de implementacao → nao e quick win, e projeto
- VETO se rodar >3 testes na mesma etapa simultaneamente → efeitos se sobrepoem

## Output Example

```yaml
cvr_action_plan:
  gargalos_priorizados:
    - etapa: "SQL -> Demo"
      conversao_atual: "15%"
      benchmark: "40%"
      gap: "25 pp"
      impacto_receita_potencial: "R$ 30k MRR/mes recuperados"
      acoes:
        - tipo: quick_win
          acao: "Automatizar resposta de primeira mensagem em 15 min"
          esforco: "2h"
          impacto_estimado: "+10pp"

        - tipo: teste
          hipotese: "Agendamento direto via Calendly reduz friccao vs 'entro em contato'"
          variante_a: "CTA 'Entrar em contato' (controle)"
          variante_b: "CTA 'Agendar demo 30min aqui' com Calendly embutido"

    - etapa: "LP -> Lead"
      conversao_atual: "1.8%"
      benchmark: "3-5%"
      gap: "1.2-3.2 pp"
      impacto_receita_potencial: "R$ 15k MRR/mes"
      acoes:
        - tipo: quick_win
          acao: "Remover 3 dos 4 CTAs da LP, deixar apenas 1"
          esforco: "1h"
          impacto_estimado: "+0.5pp"

        - tipo: teste
          hipotese: "Video de case reduz barreira vs texto apenas"

test_hypotheses:
  - id: TEST-CVR-01
    etapa: "SQL -> Demo"
    hipotese: "Calendly embutido eleva SQL->demo de 15% para 30%"
    variante_a: "CTA 'Entrar em contato'"
    variante_b: "Calendly embutido"
    metrica_primaria: "% SQLs que agendam demo"
    metrica_secundaria: "Tempo medio SQL->demo agendada"
    amostra_minima: "300 SQLs por variante"
    duracao_estimada: "4 semanas"
    kill_criteria: "Variante B <5% acima de A apos amostra minima"

  - id: TEST-CVR-02
    etapa: "LP -> Lead"
    hipotese: "Video de case eleva conversao LP de 1.8% para 3%"
    variante_a: "LP texto + imagens (controle)"
    variante_b: "LP com video de case no topo"
    metrica_primaria: "% visitantes que viram lead"
    amostra_minima: "5000 visitas por variante"
    duracao_estimada: "2 semanas"

quick_wins:
  - acao: "Automatizar resposta de primeira mensagem em 15 min"
    owner: "@sales-system-operator"
    deadline: "2026-05-07"

  - acao: "Remover CTAs concorrentes da LP"
    owner: "@funnel-conversion-engineer"
    deadline: "2026-05-06"

  - acao: "Adicionar trust badges no checkout"
    owner: "@funnel-conversion-engineer"
    deadline: "2026-05-08"
```

## Completion Criteria

- Gargalos priorizados por impacto na receita (nao por "dor")
- Quick wins identificados com owner + deadline (max 1 semana)
- Pelo menos 2 testes desenhados com hipotese + metrica + amostra minima
- Nao mais que 3 testes simultaneos na mesma etapa

## Handoff

Quick wins executados imediatamente. Testes passam para `@growth-senior-analyst *execute-experiment-backlog`. Resultados alimentam proxima iteracao em 30 dias.
