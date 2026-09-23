---
task: Execute Content Email Creative
responsavel: "@marketing-senior-analyst"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - campaign_ops_plan: Plano operacional de campanhas (saida do manager)
  - weekly_asset_queue: Fila de assets a produzir/publicar na semana
  - brand_guidelines: Guidelines de marca (tom, cores, logos)
Saida: |
  - content_email_delivery_log: Log de entregas (criativos publicados, emails disparados)
  - performance_per_asset: Performance de cada asset (CTR, open rate, conversao)
  - asset_library_update: Biblioteca de assets atualizada
Checklist:
  - "[ ] Publicar criativos conforme calendario"
  - "[ ] Disparar sequencias de email no horario otimizado"
  - "[ ] Medir performance por asset"
  - "[ ] Atualizar biblioteca com winning assets"
---

# *execute-content-email-creative

Executa producao e publicacao de criativos, content e email marketing.

## Step-by-Step

1. **Revisar fila do dia** — Ler `weekly_asset_queue` e identificar o que precisa sair hoje.
2. **Producao/edicao** — Criar ou adaptar criativo/email/post conforme brand_guidelines + pilares narrativos.
3. **Review interno** — Self-check + opcional review de manager em cases criticos (nova campanha, novo angle).
4. **Agendar publicacao** — Horarios otimos por canal (Instagram 19h, LinkedIn 9h, email terca/quinta 10h).
5. **Publicar/disparar** — Executar publicacao/envio pelo tool correto.
6. **Medir primeiras 24h** — CTR, open rate, engagement. Registrar no tracker de performance.
7. **Atualizar biblioteca** — Assets com performance top 20% viram template reutilizavel.

## Veto Conditions

- VETO se asset nao seguir brand_guidelines → volta para ajuste
- VETO se publicar sem tracking (UTM, event) → asset cego, impossivel medir
- VETO se disparar email fora do horario otimo sem razao (ex: meia-noite) → baixa open rate garantido
- VETO se biblioteca nao for atualizada apos 4 semanas → perde aprendizado acumulado

## Output Example

```yaml
content_email_delivery_log:
  data: "2026-05-06"
  owner: "@marketing-senior-analyst"

  publicados_dia:
    - asset: "creative-carousel-04"
      canal: "Instagram Paid"
      horario: "19:00"
      utm: "utm_source=ig&utm_medium=paid&utm_campaign=case-14d"
      status: publicado

    - asset: "linkedin-post-15"
      canal: "Linkedin organic"
      horario: "09:00"
      utm: "utm_source=linkedin&utm_medium=organic"
      status: publicado

    - asset: "email-onboarding-email3"
      canal: "Email"
      horario: "10:00"
      audiencia: "236 leads em dia 3 de sequencia"
      status: disparado

performance_per_asset:
  "creative-carousel-04":
    impressoes: 12400
    cliques: 186
    ctr: "1.5%"
    cpc: "R$ 2.80"
    leads_gerados: 8

  "linkedin-post-15":
    views: 4500
    reactions: 120
    comments: 18
    clicks_to_profile: 45

  "email-onboarding-email3":
    enviados: 236
    abertos: 128
    open_rate: "54%"
    clicks: 28
    ctr: "11.9%"

asset_library_update:
  promovido_para_template:
    - "creative-carousel-04 (CTR 2x acima da media)"
  flaged_underperformer:
    - "creative-video-02 (CTR 0.8%, abaixo do threshold)"
```

## Completion Criteria

- Todos os assets do dia publicados/disparados no horario certo
- Cada asset tem UTM e event tracking
- Performance primeiras 24h registrada
- Biblioteca atualizada (winners promovidos, losers flagged)

## Handoff

Performance alimenta dashboard. Top performers viram pilares de proximas campanhas. Reporta para `@marketing-senior-manager` no standup.
