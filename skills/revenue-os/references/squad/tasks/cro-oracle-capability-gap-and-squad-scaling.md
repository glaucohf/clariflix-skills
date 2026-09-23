---
task: Capability Gap and Squad Scaling
responsavel: "@cro-oracle-guardian"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - current_capabilities: Inventario de squads/agents ativos e suas competencias
  - project_complexity: Complexidade e escopo do desafio atual
  - demand_that_failed_route: Demandas que nao tiveram handoff claro em *intake-and-route
Saida: |
  - gap_report: Gaps criticos de capacidade identificados
  - scaling_decision: Decisao (expandir squad atual, criar novo squad, contratar humano, outsourcear)
  - squad_creation_brief: Brief para @squad-chief quando decisao for criar novo squad
Checklist:
  - "[ ] Listar capacidades atuais vs demanda projetada"
  - "[ ] Detectar lacunas nao cobertas por nenhum squad/agent"
  - "[ ] Avaliar impacto e custo de manter gap"
  - "[ ] Decidir acao (expandir/criar/outsourcear)"
  - "[ ] Se criar: preparar brief para @squad-chief"
---

# *capability-gap-and-squad-scaling

Avalia se os squads atuais sao suficientes e aciona criacao de novos squads quando o projeto exigir.

## Step-by-Step

1. **Inventariar capacidades atuais** — Listar agents ativos no Revenue OS + squads do ecossistema (design, content, automation, ops).
2. **Mapear demanda projetada** — A partir de macro_revenue_plan, listar capacidades necessarias nos proximos 30-90 dias.
3. **Identificar gaps** — Capacidades demandadas que nao tem owner claro em nenhum squad.
4. **Classificar gap** — Para cada gap: frequencia (unica/recorrente), criticidade (baixa/alta), tempo para resolver (dias/semanas).
5. **Decidir acao** — Regras:
   - Gap pontual + baixa criticidade → outsourcear (freelancer, consultoria)
   - Gap recorrente + alta criticidade → criar novo squad via `@squad-chief`
   - Gap recorrente + baixa criticidade → expandir squad existente com 1-2 agents
   - Gap pontual + alta criticidade → contratar humano full-time
6. **Se criar squad** — Preparar `squad_creation_brief` com: dominio, problema, expected outputs, ecossistema handoffs.
7. **Registrar decisao** — Log com rationale + data de revisao (todo gap deve ser revisado em 30 dias).

## Veto Conditions

- VETO se decisao for "criar novo squad" sem brief completo → sem brief, squad nasce vago
- VETO se gap identificado for coberto por squad existente mas owner nao foi acionado → acionar owner primeiro
- VETO se >3 gaps forem classificados como "alta criticidade" simultaneamente → escalar para revisao executiva humana, squad nao escala tudo em paralelo

## Output Example

```yaml
gap_report:
  - gap: "Videocasts comerciais para pauta de vendas"
    frequencia: recorrente
    criticidade: alta
    owner_atual: nenhum
    impacto_se_gap_persistir: "Vendas sem material de warm-up, conversao cai ~10%"

  - gap: "Traducao para ingles de LP"
    frequencia: pontual
    criticidade: baixa
    owner_atual: nenhum
    impacto_se_gap_persistir: "Bloqueia expansao internacional fase 1, nao critico agora"

scaling_decision:
  - gap: "Videocasts comerciais"
    acao: criar_squad
    justificativa: "Recorrente + alta criticidade + ecossistema content-os nao cobre videocast comercial"

  - gap: "Traducao LP"
    acao: outsourcear
    justificativa: "Pontual + baixa criticidade = custo de criar squad > custo de freelance"

squad_creation_brief:
  dominio: "Videocast comercial (sales-driven video content)"
  problema: "Time de vendas nao tem material audiovisual de pre-venda que converta prospect em demo qualificada"
  expected_outputs:
    - Scripts de videocast por estagio do funil (awareness/consideration/decision)
    - Setup tecnico (gravacao, edicao leve, distribuicao)
    - Metricas (watch rate, conversao demo)
  ecossistema_handoffs:
    - content-os (pautas editoriais)
    - design (thumbnails)
    - revops (tracking)
  sugestao_nome: "sales-videocast"
```

## Completion Criteria

- Gap report cobre todos os gaps identificados nas ultimas 4 semanas de `*control-weekly-metrics`
- Cada gap tem classificacao (frequencia + criticidade) e decisao (expandir/criar/outsourcear/contratar)
- Se acao for "criar squad", brief completo com dominio + problema + outputs + handoffs
- Todos os gaps agendados para revisao em 30 dias

## Handoff

Se decisao for criar squad → handoff para `@squad-chief *create-squad-smart` com brief pronto. Se outsourcear → handoff para owner humano (usuario). Se expandir → handoff para owner do squad existente.
