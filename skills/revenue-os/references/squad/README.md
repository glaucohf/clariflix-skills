# revenue-os

> **Criado por:** Rodrigo Feldman
> **Criado em:** 2026-02-25
> **Ultima atualizacao:** 2026-04-23
> **Versao atual:** 1.0.0
> **Status:** active · Pipeline squad (17 agents, 39 tasks, 7 workflows)
> **Licenca de uso:** interno AIOS Cohort — cite o autor ao replicar ou adaptar

Sistema operacional de monetizacao para produtos AI-first: Marketing + Comercial + RevOps, com governanca executiva via CRO Oracle Guardian.

---

## Autoria e origem

Este squad foi concebido e estruturado por **Rodrigo Feldman** dentro do workspace `aios-cohort-alan` como resposta a uma dor especifica: squads AIOS resolvem construcao, mas nao resolvem monetizacao. O `revenue-os` fecha esse gap com uma cadeia de comando completa (CRO → C-level → managers → analysts) e uma celula especialista de execucao operacional.

**Proposito autoral:**
- Transformar produto pronto em receita previsivel, sem depender de um unico framework (como Hormozi)
- Ser o "departamento comercial em formato de squad" para qualquer produto AIOS
- Permitir dogfooding: vender o proprio `revenue-os` usando o `revenue-os`

**Ao usar ou adaptar este squad:** mantenha o credito de autoria e registre mudancas relevantes na secao Changelog ao final deste README.


## Problema que resolve

Com AIOS e agentes, o gargalo nao e mais construir. O gargalo virou monetizar com previsibilidade.
O `revenue-os` fecha o gap entre "produto pronto" e "receita recorrente".

## Diferenca para hormozi

`hormozi`:
- framework-first (oferta, copy, growth na escola Hormozi)
- profundidade metodologica de uma linha de pensamento

`revenue-os`:
- operating-system-first (empresa comercial completa)
- integra estrategia, execucao, CRM, checkout, dashboard e governanca
- possui cadeia de comando corporativa (CRO -> C-level -> managers -> analysts)

Use os dois juntos quando fizer sentido:
- `hormozi` para engenharia de oferta/mensagem
- `revenue-os` para operar e escalar receita no dia a dia

## Governanca (cadeia de comando)

### 1) CRO Oracle Guardian (comandante principal)
- `cro-oracle-guardian`
- recebe demanda do usuario
- define plano macro e metas
- direciona CCO/CMO/CGO
- aciona criacao de novos squads quando houver gap de capacidade

### 2) Diretores executivos
- `cco-commercial-director` (vendas, parcerias, estrategia comercial)
- `cmo-marketing-director` (demanda, branding, canais)
- `cgo-growth-director` (integracao marketing+vendas+growth)

### 3) Gerentes senior
- `commercial-senior-manager`
- `marketing-senior-manager`
- `growth-senior-manager`

### 4) Analistas senior (execucao)
- `commercial-senior-analyst`
- `marketing-senior-analyst`
- `growth-senior-analyst`

### 5) Célula especialista Revenue OS
- `revenue-chief`
- `monetization-strategist`
- `demand-gen-architect`
- `funnel-conversion-engineer`
- `sales-system-operator`
- `revops-automation-engineer`
- `experimentation-analyst`

## Como funciona

1. CRO recebe a demanda e define meta macro.
2. Diretores desenham estrategia por area.
3. Gerentes transformam estrategia em operacao.
4. Analistas executam rotina supervisionada.
5. Célula especialista entrega stack comercial final.
6. CRO controla metricas semanais e planejamento mensal.
7. Se faltar capacidade, CRO manda escalar com novos squads.

## Workflows principais

- `wf-kickoff-7-days.yaml` (kickoff operacional intensivo de 7 dias)
- `wf-cro-command-chain.yaml` (governanca corporativa completa)
- `wf-zero-to-revenue.yaml`
- `wf-demand-to-close-loop.yaml`
- `wf-commercial-stack-activation.yaml`
- `wf-weekly-revenue-optimization.yaml`
- `wf-revenue-os-self-launch.yaml`

## Stack comercial final

O `revenue-os` cobre explicitamente:

1. LP de vendas
- especificacao funcional da LP e fluxo de checkout
- handoff para `design`/`brandcraft`

2. Pagamento online
- setup de checkout e billing (Stripe ou equivalente)
- webhooks de sucesso/falha/assinatura
- handoff tecnico para `n8n-builder` quando necessario

3. Dashboard de receita e assinaturas
- KPI de receita (MRR, churn, conversao, CAC)
- dono por indicador e alertas operacionais

4. Criativos e distribuicao
- plano de criativos por canal
- handoff para `content-os`/`content-engine`

5. Email marketing
- sequencias por etapa do funil
- cadencia de aquecimento, conversao e follow-up

6. Operacao comercial
- pipeline CRM
- scripts de fechamento
- automacao de follow-up por estagio

## Modelo replicavel para outras ideias

1. Defina oferta + ICP
2. Rode `wf-cro-command-chain.yaml`
3. Rode `wf-commercial-stack-activation.yaml`
4. Entre em cadencia com `wf-weekly-revenue-optimization.yaml`

Referencias:
- `docs/REPLICABLE-MODEL.md`
- `docs/TESTE-RAPIDO-REVENUE-OS.md`
- `docs/PROJECT-SETUP-RECOMMENDATION.md`
- `docs/KICKOFF-7-DIAS-REVENUE-OS.md`
- `data/self-launch-blueprint-v1.yaml`
- `data/kickoff-7-days-v1.yaml`

## Exemplo real (dogfooding)

Caso final do proprio squad:
- usar `revenue-os` para vender o proprio `revenue-os`
- ativar LP + checkout + dashboard + criativos + email + operacao comercial
- medir MRR inicial e ajustar semanalmente

Workflow dedicado:
- `wf-revenue-os-self-launch.yaml`

Exemplos:
- `docs/SELF-LAUNCH-EXAMPLE-REVENUE-OS.md`
- `docs/SELF-LAUNCH-ARTIFACT-V1.md`

## Comandos nucleares

- `@cro-oracle-guardian *intake-and-route`
- `@cro-oracle-guardian *build-macro-revenue-plan`
- `@cro-oracle-guardian *capability-gap-and-squad-scaling`
- `@cro-oracle-guardian *run-7-day-kickoff`
- `@revenue-chief *orchestrate-commercial-stack`
- `@revenue-chief *run-self-launch`
- `@revops-automation-engineer *setup-checkout-and-billing`

---

## Metadata do squad

| Campo | Valor |
|---|---|
| Nome | `revenue-os` |
| Versao | 1.0.0 |
| Autor | Rodrigo Feldman |
| Criado em | 2026-02-25 |
| Ultima atualizacao | 2026-04-23 |
| Tipo | Pipeline |
| Entry agent | `cro-oracle-guardian` |
| Agents | 17 |
| Tasks | 39 |
| Workflows | 7 |
| Checklists | 5 |
| Quality Gates | 5 (QG-REV-001..005) |
| Score atual (validate-squad) | 8.2 / 10 projetado (PASS, pos brownfield round 3) |

## Changelog

### 2026-04-23 — Brownfield upgrade round 3 (focus=agents)
- **Autor:** Rodrigo Feldman
- **Escopo:** Normalizacao dos 16 agents restantes para schema AIOS completo
- **Mudancas:**
  - Todos os 17 agents (incluindo cro-oracle-guardian do round 1) agora tem:
    - `ACTIVATION-NOTICE` header
    - `activation-instructions:` com 4 STEPS (Read + Adopt + Greet + HALT)
    - `persona` expandida com role/style/identity/focus
    - `core_principles` (3-5 items relevantes)
    - `commands` com prefixo `*` + `*help` + `*exit`
    - `command_to_task` mapping explicito
    - `handoff_to` list
  - Tamanho medio: ~27 linhas → 68 linhas (+150%)
  - Todos os commands/tasks existentes foram preservados, apenas encapsulados no schema
- **Impacto:** Score 7.7 → 8.2 projetado (confirmacao PASS + elevacao em T4 orchestrator_completeness)
- **Report:** `outputs/squad_upgrade/revenue-os/upgrade-report-round3.yaml`

### 2026-04-23 — Brownfield upgrade round 2 (focus=tasks)
- **Autor:** Rodrigo Feldman
- **Escopo:** Expansao das 37 tasks restantes (mais 2 ja expandidas no round 1 = 39 de 39)
- **Mudancas:**
  - Todas as 39 tasks agora seguem Task Anatomy completa: frontmatter (entrada/saida/checklist) + Step-by-Step + Veto Conditions + Output Example + Completion Criteria + Handoff
  - Media de linhas por task: 19 → 113 (+94 linhas por task em media)
  - Total adicionado: ~3.600 linhas de conteudo operacional
  - Cada task agora contem output examples YAML concretos, nao mais stubs
- **Impacto:** Score 5.6 → 7.7 projetado (CONDITIONAL → PASS)
- **Report:** `outputs/squad_upgrade/revenue-os/upgrade-report-round2.yaml`

### 2026-04-23 — Brownfield upgrade (critical-only)
- **Autor:** Rodrigo Feldman
- **Mudancas:**
  - `agents/cro-oracle-guardian.md`: adicionado `ACTIVATION-NOTICE` + `activation-instructions` + comando `*help` + `core_principles` + `handoff_to` (52 → 92 linhas)
  - `tasks/cro-oracle-intake-and-route.md`: expandida com 7 steps + 3 veto conditions + output example YAML + completion criteria (20 → 81 linhas)
  - `tasks/cro-oracle-build-macro-revenue-plan.md`: expandida com 7 steps + 4 veto conditions + output example detalhado + completion criteria (20 → 100 linhas)
  - README: adicionada secao de autoria, metadata e changelog
- **Impacto:** Veto V2 desbloqueado · Score 3.8 → 5.6 (projetado)
- **Report:** `outputs/squad_upgrade/revenue-os/upgrade-report.yaml`

### 2026-02-25 — Criacao inicial
- **Autor:** Rodrigo Feldman
- **Entregas:** estrutura base com 17 agents em 5 tiers, 39 tasks (stubs), 7 workflows, 5 checklists, 5 quality gates, README com positioning vs hormozi.
