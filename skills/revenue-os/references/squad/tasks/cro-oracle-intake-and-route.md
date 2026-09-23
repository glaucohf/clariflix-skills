---
task: CRO Intake and Route
responsavel: "@cro-oracle-guardian"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - user_demand: Demanda bruta do usuario (texto livre, objetivo macro, dor, urgencia)
  - business_context: Contexto do projeto (produto, estagio, publico, metas existentes)
Saida: |
  - executive_brief: Brief executivo em 1 pagina (objetivo, meta, restricoes, owners propostos)
  - command_chain_route: Roteamento estruturado para CCO/CMO/CGO com handoffs
  - revenue_target: Meta de receita numerica com prazo
Checklist:
  - "[ ] Objetivo macro clarificado e validado com o usuario"
  - "[ ] Meta de receita definida (numero + prazo)"
  - "[ ] Diretores corretos identificados (CCO/CMO/CGO)"
  - "[ ] Handoff para cada diretor registrado com contexto especifico"
---

# *intake-and-route

Recebe a demanda do usuario e inicia a cadeia de comando do Revenue OS.

## Step-by-Step

1. **Coletar demanda** — Ler `user_demand` e `business_context`. Se algum campo estiver vago (ex: "quero vender mais"), fazer ate 3 perguntas de clarificacao antes de prosseguir.
2. **Clarificar objetivo macro** — Responder: qual problema de receita estamos resolvendo? Escalar, estabilizar ou destravar?
3. **Definir meta** — Traduzir objetivo em numero + prazo (ex: "R$ 100k MRR ate 90 dias"). Sem meta numerica, VETO.
4. **Mapear restricoes** — Listar time, budget, canais disponiveis, deadlines externos.
5. **Identificar diretores necessarios** — Regras:
   - CCO: se envolve pipeline, closing, CRM
   - CMO: se envolve canais, campanhas, criativo, aquisicao
   - CGO: se envolve experimentacao, retention, LTV, conversao
6. **Montar command_chain_route** — Para cada diretor selecionado, registrar: contexto, primeira tarefa, handoff criteria.
7. **Gerar executive_brief** — Sintetizar itens 2-6 em 1 pagina.

## Veto Conditions

- VETO se `user_demand` for vaga apos 3 perguntas de clarificacao → retornar ao usuario pedindo briefing mais especifico
- VETO se nenhuma meta numerica puder ser definida → retornar com "meta indefinida, impossivel rotear"
- VETO se demanda nao se encaixar em nenhum dos 3 diretores (CCO/CMO/CGO) → escalar para `*capability-gap-and-squad-scaling`

## Output Example

```yaml
executive_brief:
  objetivo_macro: "Escalar MRR de R$ 20k para R$ 100k em 90 dias"
  meta: "R$ 100k MRR em 90 dias"
  restricoes:
    - "Time atual: 3 pessoas"
    - "Budget ads: R$ 15k/mes"
    - "Canais ativos: organico + paid social"

command_chain_route:
  - director: cmo-marketing-director
    contexto: "Escalar aquisicao paga sem perder CAC payback"
    primeira_tarefa: cmo-marketing-director-design-marketing-masterplan
    handoff_criteria: "Plano de canais aprovado + budget por canal definido"
  - director: cco-commercial-director
    contexto: "Processo de closing atual nao suporta 5x o volume"
    primeira_tarefa: cco-commercial-director-design-commercial-strategy
    handoff_criteria: "Playbook + SLA de resposta definido"

revenue_target:
  valor: 100000
  moeda: BRL
  unidade: MRR
  prazo: 90_dias
```

## Completion Criteria

- `executive_brief` gerado e aprovado pelo usuario
- `command_chain_route` com 2-4 diretores (nao mais que 4 — cada diretor adicionado aumenta coordenacao em O(n²))
- `revenue_target` com valor numerico + prazo
- Handoff efetivo: cada diretor recebeu contexto + primeira tarefa + criterio de conclusao

## Handoff

Apos PASS, o CRO Oracle Guardian entrega o `command_chain_route` para os diretores identificados e ativa o proximo passo (`*build-macro-revenue-plan`).
