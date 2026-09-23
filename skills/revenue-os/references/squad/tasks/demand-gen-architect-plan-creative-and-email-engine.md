---
task: Plan Creative and Email Engine
responsavel: "@demand-gen-architect"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - acquisition_plan: Plano com canais ativos
  - campaign_briefs: Briefs com angulos criativos
  - funnel_stages: Estagios do funil (awareness, consideration, decision, post-sale)
Saida: |
  - creative_engine_plan: Plano de producao + refresh de criativos
  - email_engine_plan: Sequencias de email por estagio do funil
  - production_cadence: Cadencia de producao + revisao
Checklist:
  - "[ ] Matriz de criativos por canal (quantidade + formato + vida util)"
  - "[ ] Sequencia de aquecimento (lead magnet -> SQL)"
  - "[ ] Sequencia de conversao (SQL -> cliente)"
  - "[ ] Sequencia pos-venda (cliente -> ativacao -> retention)"
  - "[ ] Cadencia de disparo otimizada por horario/dia"
---

# *plan-creative-and-email-engine

Planeja maquina de criativos e email marketing para sustentar demanda e conversao continuamente.

## Step-by-Step

1. **Mapear volume de criativos necessario** — Por canal, baseado em refresh cycle (3-4 semanas de vida util).
2. **Definir matriz de formatos** — Carousel, video, single image, UGC, etc por canal.
3. **Desenhar sequencia de aquecimento** — Lead magnet -> 3-5 emails construindo valor -> qualificacao SQL.
4. **Desenhar sequencia de conversao** — SQL nao-fechado em 7 dias -> nurturing com cases, objecoes, urgencia.
5. **Desenhar sequencia pos-venda** — Welcome -> ativacao 7 dias -> retention 30 dias.
6. **Definir cadencia de disparo** — Horarios otimos por segmento + dia da semana.
7. **Configurar producao** — Quem produz, quem revisa, SLA de entrega.

## Veto Conditions

- VETO se producao nao acompanhar refresh cycle → fadiga de criativo mata performance
- VETO se nenhuma sequencia de conversao para SQLs nao-fechados → 70%+ dos SQLs morrem sem follow-up
- VETO se pos-venda tiver apenas email de boas-vindas → ativacao e retention sofrem
- VETO se cadencia disparar email >3x/semana para mesmo contato → unsubscribe disparado

## Output Example

```yaml
creative_engine_plan:
  volume_mensal:
    paid_instagram: 8 criativos/mes (2/semana, vida util 3 semanas)
    linkedin_organic: 12 posts/mes (3/semana)
    content_blog: 4 posts/mes

  matriz_por_canal:
    paid_instagram:
      formatos: ["carousel", "video_30s", "single_image", "ugc"]
      proporcao: "40% carousel, 30% video, 20% single, 10% UGC"
    linkedin:
      formatos: ["post_texto_longo", "post_carousel", "video_native"]
      proporcao: "60% texto, 30% carousel, 10% video"

  refresh_cycle:
    vida_util_padrao: "3 semanas"
    fadiga_trigger: "CTR cai >20%"
    pipeline_de_producao: "Sempre 2 em producao + 2 em teste + 2 rodando"

email_engine_plan:
  sequencia_aquecimento:
    trigger: "Download lead magnet"
    duracao: "7 dias"
    emails:
      - dia: 0
        assunto: "Seu playbook + pergunta rapida"
        objetivo: "Iniciar dialogo + qualificar"
      - dia: 2
        assunto: "Case: R$ 6k em 14 dias"
        objetivo: "Proof + aspiracao"
      - dia: 4
        assunto: "O erro que 80% dos founders fazem"
        objetivo: "Pain + setup para oferta"
      - dia: 7
        assunto: "Quer agendar uma call de 15 min?"
        objetivo: "CTA demo"

  sequencia_conversao_sql_nao_fechado:
    trigger: "SQL sem movimento por 3 dias"
    duracao: "14 dias"
    emails:
      - dia: 3
        assunto: "Alguma duvida sobre a proposta?"
        objetivo: "Re-engajar"
      - dia: 7
        assunto: "Objecao comum: 'nao tenho tempo'"
        objetivo: "Tratar objecao estrutural"
      - dia: 14
        assunto: "Ultima chamada antes de fecharmos esta semana"
        objetivo: "Urgencia + CTA final"

  sequencia_pos_venda:
    trigger: "Checkout completo"
    duracao: "30 dias"
    emails:
      - dia: 0
        assunto: "Bem-vindo - 3 passos pra ativar"
        objetivo: "Welcome + setup inicial"
      - dia: 3
        assunto: "Primeiro milestone: setup do squad"
        objetivo: "Checkpoint ativacao dia 3"
      - dia: 7
        assunto: "Primeiro resultado: quick win"
        objetivo: "Dopamina de primeira conquista"
      - dia: 14
        assunto: "Como foi a primeira semana?"
        objetivo: "Check NPS + desbloqueio"
      - dia: 30
        assunto: "Retrospectiva do primeiro mes"
        objetivo: "Retention + upsell soft"

production_cadence:
  semanal:
    segunda: "Planning criativos da semana"
    quarta: "Review de criativos em producao"
    sexta: "Retrospectiva performance + lessons"

  sla_producao:
    criativo_novo: "3 dias uteis"
    email_novo: "2 dias uteis"
    iteracao_asset_existente: "1 dia util"
```

## Completion Criteria

- Matriz de criativos cobre refresh cycle sem gaps
- 3 sequencias de email (aquecimento + conversao + pos-venda) implementadas
- Cada email tem objetivo claro
- Cadencia de producao com SLAs

## Handoff

Plano passa para `@marketing-senior-analyst` executar producao diaria. `@revops-automation-engineer` configura automacoes de email no CRM.
