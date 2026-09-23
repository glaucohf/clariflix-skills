---
task: Orchestrate Commercial Stack
responsavel: "@revenue-chief"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - product_offer: Oferta e precificacao aprovadas
  - go_live_date: Data alvo de go-live
  - roadmap_90_days: Roadmap com sprints e owners
Saida: |
  - stack_plan: Plano integrado de LP, checkout, dashboard, criativos, email, operacao
  - squad_handoffs: Handoffs formais para squads do ecossistema com briefs
  - raci_matrix: RACI de cada componente da stack
Checklist:
  - "[ ] Handoff para design/brandcraft com brief"
  - "[ ] Handoff para n8n-builder com workflows de automacao"
  - "[ ] Handoff para content-os/content-engine com editorial plan"
  - "[ ] RACI completo (Responsible/Accountable/Consulted/Informed)"
  - "[ ] Cronograma integrado com go_live_date"
---

# *orchestrate-commercial-stack

Orquestra a fase final de monetizacao ativando squads complementares do ecossistema AIOS.

## Step-by-Step

1. **Validar oferta e data** — Sem oferta aprovada ou sem data de go-live, impossivel orquestrar.
2. **Inventariar squads do ecossistema** — Listar squads disponiveis e suas capacidades.
3. **Mapear componentes da stack comercial** — LP, checkout/billing, dashboard, criativos, email, CRM.
4. **Atribuir cada componente a 1 squad primario + 0-2 squads de apoio.**
5. **Gerar brief por handoff** — Cada squad recebe: contexto, expected output, deadline, criterio de aceite.
6. **Montar RACI** — Para cada componente: Responsible (quem faz), Accountable (quem responde), Consulted (quem opina), Informed (quem recebe update).
7. **Definir cronograma integrado** — Calendario com dependencias entre squads ate go_live_date.

## Veto Conditions

- VETO se data de go-live for em <5 dias → muito pouco tempo para orquestrar 5-6 squads, escalar para `@cro-oracle-guardian`
- VETO se algum componente critico (checkout ou LP) nao tiver squad atribuido → escalar para `*capability-gap-and-squad-scaling`
- VETO se RACI tiver >1 Accountable por componente → um unico responsavel final, sempre

## Output Example

```yaml
stack_plan:
  go_live_date: "2026-05-15"
  componentes:
    - componente: "Sales LP"
      squad_primario: "design"
      apoio: ["brandcraft"]
      deadline: "2026-05-10"
      expected_output: "LP responsiva, carregamento <3s, CTA unico"

    - componente: "Checkout + Billing"
      squad_primario: "n8n-builder"
      apoio: ["@revops-automation-engineer"]
      deadline: "2026-05-12"
      expected_output: "Stripe integrado + webhooks + email de confirmacao"

    - componente: "Revenue Dashboard"
      squad_primario: "@revops-automation-engineer"
      apoio: []
      deadline: "2026-05-13"
      expected_output: "MRR, churn, CAC, conversao funil por canal"

    - componente: "Email + Criativos"
      squad_primario: "content-os"
      apoio: ["content-engine"]
      deadline: "2026-05-10"
      expected_output: "5 criativos paid social + 1 sequencia email 7 touches"

    - componente: "CRM + Pipeline"
      squad_primario: "@sales-system-operator"
      apoio: ["project-management-clickup"]
      deadline: "2026-05-11"
      expected_output: "Pipeline com 5 estagios + SLA + automacoes de follow-up"

squad_handoffs:
  - para: "design"
    brief: "LP de vendas revenue-os/stretch, CTA unico 'agendar demo', visual brandcraft"
    deadline: "2026-05-10"
    criterio_aceite: "LP passa em Lighthouse >90 performance + acessibilidade"

raci_matrix:
  sales_lp:
    R: "design"
    A: "@revenue-chief"
    C: ["brandcraft", "@cmo-marketing-director"]
    I: ["@cro-oracle-guardian"]
  checkout_billing:
    R: "n8n-builder"
    A: "@revops-automation-engineer"
    C: ["@revenue-chief"]
    I: ["@cro-oracle-guardian"]
```

## Completion Criteria

- Cada componente da stack tem squad primario atribuido
- Todo handoff tem brief + deadline + criterio de aceite
- RACI com 1 Accountable unico por componente
- Cronograma integrado mostra caminho critico ate go_live_date

## Handoff

Briefs enviados para cada squad. `@revenue-chief` mantem sync semanal ate go-live. Apos go-live, handoff para `*control-weekly-metrics`.
