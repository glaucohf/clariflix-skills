---
task: Design Marketing Masterplan
responsavel: "@cmo-marketing-director"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - macro_plan: Plano macro CRO com meta trimestral
  - icp_profile: ICP validado
  - commercial_strategy: Estrategia comercial com segmentos
Saida: |
  - marketing_masterplan: Plano mestre (narrativa + demanda + canais + orcamento)
  - narrative_pillars: Pilares narrativos (3-5 temas editoriais)
  - demand_allocation: Distribuicao de demanda por canal
Checklist:
  - "[ ] Definir estrategia de demanda (inbound/outbound/organico/paid)"
  - "[ ] Definir narrativa de mercado (posicionamento + pilares)"
  - "[ ] Alocar budget por canal com expectativa"
  - "[ ] Mapear asset plan (content, criativos, landing pages)"
---

# *design-marketing-masterplan

Constroi plano mestre de marketing conectado a receita trimestral.

## Step-by-Step

1. **Traduzir meta de receita em meta de demanda** — Usar taxas de conversao para calcular SQLs necessarios.
2. **Definir narrativa de mercado** — Posicionamento vs concorrentes + 3-5 pilares narrativos editoriais.
3. **Escolher mix de canais** — Regra 70-20-10: 70% no canal que ja funciona, 20% em aposta comprovavel, 10% experimentacao.
4. **Alocar budget por canal** — Baseado em CAC esperado e payback.
5. **Definir asset plan** — Por canal, quais criativos/content/LPs precisam existir.
6. **Mapear owners** — Senior manager + analystas responsaveis por cada frente.
7. **Definir cadencia de revisao** — KPIs semanais leading (volume+CPC) + lagging (SQL+CAC).

## Veto Conditions

- VETO se estrategia apostar >50% em canal nao testado → risco alto, reduzir aposta
- VETO se narrativa for sobre o produto (features) ao inves do resultado (outcome) → reposicionar
- VETO se nenhum canal tiver owner humano nomeado
- VETO se budget total exceder 30% da receita esperada → CAC insustentavel

## Output Example

```yaml
marketing_masterplan:
  meta_sqls_trimestre: 400
  budget_trimestre: "R$ 45.000"

  narrative:
    posicionamento: "O unico squad AIOS que transforma produto pronto em receita previsivel"
    pilares:
      - "Case: founders que ativaram primeira venda em 14 dias"
      - "Stack comercial: sai de zero para LP+checkout+CRM em 7 dias"
      - "Governanca: CRO/CCO/CMO/CGO em formato squad"
      - "Dogfooding: vendemos o proprio Revenue OS usando o Revenue OS"

  canais:
    - canal: "Linkedin organic"
      budget: "R$ 0 (tempo)"
      expected_sqls: 120
      owner: "@marketing-senior-manager"

    - canal: "Paid social Instagram"
      budget: "R$ 30.000"
      expected_cac: "R$ 375 (CAC payback 3 meses)"
      expected_sqls: 200
      owner: "@marketing-senior-manager"

    - canal: "Content SEO (blog tecnico)"
      budget: "R$ 10.000"
      expected_sqls: 50
      owner: "@marketing-senior-analyst"

    - canal: "Experimentacao (X/Twitter threads)"
      budget: "R$ 5.000"
      expected_sqls: 30
      owner: "@marketing-senior-analyst"

demand_allocation:
  organic: 30%
  paid: 50%
  content: 12.5%
  experimentacao: 7.5%

asset_plan:
  sales_lp: 1
  criativos_paid: 15
  blog_posts: 8
  email_sequences: 2
```

## Completion Criteria

- Meta de SQLs derivada matematicamente da meta de receita
- Narrativa com posicionamento + 3-5 pilares editoriais
- Mix de canais com 70-20-10 (principal/aposta/experimentacao)
- Cada canal tem budget + CAC esperado + owner

## Handoff

Plano mestre passa para `@marketing-senior-manager` operacionalizar em campanhas. `@demand-gen-architect` desenha acquisition plan detalhado por canal.
