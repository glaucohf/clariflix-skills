---
task: Create Campaign Briefs
responsavel: "@demand-gen-architect"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - acquisition_plan: Plano de aquisicao com canais e calendario
  - offer_message: Mensagem da oferta com value_proposition e unique mechanism
  - pilares_narrativos: Pilares editoriais do marketing_masterplan
Saida: |
  - campaign_briefs: Briefs prontos para execucao (1 por campanha)
  - creative_angle_list: Angulos criativos por segmento/persona
  - success_criteria_per_brief: Metricas de sucesso por brief
Checklist:
  - "[ ] Definir promessa unica por campanha"
  - "[ ] Definir CTA unico (nada de multiplos CTAs)"
  - "[ ] Listar angulos criativos por persona"
  - "[ ] Definir criterio de sucesso mensuravel"
---

# *create-campaign-briefs

Gera briefs detalhados de campanhas para acelerar execucao sem perder consistencia narrativa.

## Step-by-Step

1. **Pegar campanha do calendario** — Uma campanha por vez, seguindo `campaign_calendar`.
2. **Definir promessa unica** — Uma frase que resume o outcome prometido para o ICP alvo.
3. **Criar angulos criativos** — 3-5 angulos diferentes para testar (headline + visual + proof).
4. **Definir CTA unico** — Uma acao clara: "Agendar demo", "Baixar playbook", "Ler case". Nada de multiplos CTAs.
5. **Mapear audiencia** — Segmento + interesses + comportamentos + plataforma.
6. **Definir success criteria** — CPL, CTR, CPC ranges + conversao esperada.
7. **Empacotar brief** — Template padrao que executor (analyst ou squad externo) consegue acionar.

## Veto Conditions

- VETO se brief tiver >1 CTA → dispersao mata conversao
- VETO se promessa for generica ("melhore seu negocio") → sem especificidade, ninguem converte
- VETO se nenhum angulo trouxer proof (case, numero, depoimento) → promessa sem proof e hype
- VETO se success criteria nao tiver range numerico → impossivel avaliar depois

## Output Example

```yaml
campaign_briefs:
  - brief_id: CB-01-mai
    campanha: "Case: 14 dias ate primeira venda"
    semana: "S1-S2 Mai"
    canal: "Paid Instagram"
    budget: "R$ 7.500"

    promessa_unica: "Seu produto AIOS pronto vira primeira venda em 14 dias com Revenue OS"

    audiencia:
      segmento: "Founders AIOS solo"
      interesses: ["AIOS", "AI agents", "SaaS founder", "indie hacker"]
      comportamentos: "Frequenta comunidades tech, consumiu conteudo Hormozi/Koe"
      exclude: "Agencias (segmento diferente)"

    angulos_criativos:
      - angulo: "Case visual (screenshot de dashboard real)"
        headline: "R$ 6k MRR em 14 dias usando Revenue OS"
        proof: "Screenshot do dashboard com transacoes reais"
        formato: "Carousel 5 slides"

      - angulo: "Contrast (antes/depois)"
        headline: "Construi em 6 meses. Vendi em 14 dias."
        proof: "Timeline visual construcao -> primeira venda"
        formato: "Video 30s"

      - angulo: "Authority (cadeia de comando)"
        headline: "CRO + CCO + CMO + CGO em squad de IA"
        proof: "Diagrama da hierarquia"
        formato: "Single image"

    cta_unico: "Agendar demo de 30 min"
    landing_page: "lp-case-14-dias"

    success_criteria:
      cpl_target: "R$ 50-80"
      ctr_target: "1.5%-3%"
      cpc_target: "R$ 2-4"
      sqls_esperados: 50
      conversao_lp_target: ">3%"

  - brief_id: CB-02-mai
    campanha: "Stack comercial completa"
    semana: "S3-S4 Mai"
    # ... (mesmo formato)

creative_angle_list:
  founders_solo:
    pain_angles: ["Sei construir, nao sei vender", "Produto pronto sem receita", "Solo sem time comercial"]
    transformation_angles: ["Produto -> receita em 14 dias", "De developer para founder"]
    authority_angles: ["Cadeia de comando executiva em IA", "Case R$ 6k em 14 dias"]

  agencias:
    pain_angles: ["Revenda servicos sem stack propria", "Clientes pedindo RevOps"]
    transformation_angles: ["De agencia de entrega para RevOps-as-a-Service"]

success_criteria_per_brief:
  CB-01-mai: { cpl: "R$ 50-80", ctr: "1.5-3%", sqls: 50 }
  CB-02-mai: { cpl: "R$ 60-90", ctr: "1.3-2.5%", sqls: 40 }
```

## Completion Criteria

- Brief por campanha ativa do calendario
- 1 CTA unico + 3-5 angulos criativos por brief
- Success criteria com ranges numericos
- Lista de angulos por segmento para reuso futuro

## Handoff

Briefs passam para `@marketing-senior-analyst` produzir assets. `@marketing-senior-manager` monitora performance contra success criteria.
