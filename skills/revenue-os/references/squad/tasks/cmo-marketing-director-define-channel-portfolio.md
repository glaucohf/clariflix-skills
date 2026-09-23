---
task: Define Channel Portfolio
responsavel: "@cmo-marketing-director"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - demand_target: Meta de demanda (SQLs/mes)
  - marketing_masterplan: Masterplan com pilares narrativos
  - historic_channel_performance: Performance historica por canal (se disponivel)
Saida: |
  - channel_portfolio: Portfolio de canais priorizados com role de cada um
  - kill_list: Canais testados e descontinuados com razao
  - experiment_list: Canais em fase de teste com budget limitado
Checklist:
  - "[ ] Canal primario definido (>50% dos SQLs)"
  - "[ ] Canal secundario definido (20-30% dos SQLs)"
  - "[ ] 1-2 canais em experimentacao (budget <10%)"
  - "[ ] Kill list com canais que ja falharam e razao"
---

# *define-channel-portfolio

Define o portfolio de canais com hierarquia clara: primario, secundario, experimentacao.

## Step-by-Step

1. **Listar canais candidatos** — Todos os canais relevantes para o ICP (paid social, SEO, outbound, parcerias, eventos, PR, etc).
2. **Classificar por maturidade** — Testado+funciona / testado+nao-funciona / nao-testado.
3. **Definir canal primario** — O que ja funciona e escala. Responsavel por >50% dos SQLs.
4. **Definir canal secundario** — O que funciona mas menor, ou aposta comprovavel. 20-30%.
5. **Selecionar experimentacao** — 1-2 canais nao-testados com budget limitado (<10% total).
6. **Montar kill list** — Canais testados que nao funcionaram. Registrar razao para nao repetir.
7. **Definir thresholds de kill** — Condicoes que fazem um canal ser descontinuado (ex: CAC 2x acima de target por 8 semanas).

## Veto Conditions

- VETO se canal primario for experimentacao → primario tem que ter historico comprovado
- VETO se >3 canais simultaneos em experimentacao → foco perdido
- VETO se kill list ficar vazia em um squad com >3 meses → provavel que falta honestidade na avaliacao

## Output Example

```yaml
channel_portfolio:
  primario:
    canal: "Paid social Instagram"
    share_target: "60% dos SQLs"
    razao: "Ja validado com CAC R$ 375, escalavel ate R$ 30k/mes"
    owner: "@marketing-senior-manager"
    kill_threshold: "CAC > R$ 750 por 8 semanas"

  secundario:
    canal: "Linkedin organic (autor)"
    share_target: "25% dos SQLs"
    razao: "Alto engajamento no ICP, sem custo de aquisicao"
    owner: "@marketing-senior-analyst"
    kill_threshold: "N/A (custo zero)"

  terciario:
    canal: "Content SEO blog"
    share_target: "10% dos SQLs"
    razao: "Aposta de longo prazo, 6-12 meses de payback"

experiment_list:
  - canal: "X/Twitter threads"
    budget_mes: "R$ 5.000"
    hipotese: "Thread style atrai founders tech"
    duracao_teste: "8 semanas"
    kill_threshold: "<10 SQLs em 8 semanas"
  - canal: "Cold outbound LinkedIn"
    budget_mes: "R$ 3.000 (tooling)"
    hipotese: "Segmento agencias responde melhor a outbound"
    duracao_teste: "4 semanas"

kill_list:
  - canal: "Facebook Ads"
    razao: "ICP nao presente na plataforma, CAC 3x maior que Instagram"
    data_descontinuado: "2026-03-15"
  - canal: "Google Ads search"
    razao: "Termos chave muito caros (CPC R$ 8+), volume baixo"
    data_descontinuado: "2026-02-28"
```

## Completion Criteria

- Primario + secundario cobrem ≥80% da meta de SQLs
- Todo canal tem kill threshold definido
- Experimentacao limitada a 1-2 canais com duracao e kill threshold
- Kill list documentada com razao

## Handoff

Portfolio distribuido para `@demand-gen-architect` operacionalizar campanhas. Revisao mensal em `*run-monthly-planning-cycle`.
