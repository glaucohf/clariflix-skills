---
task: Design Offer Architecture
responsavel: "@monetization-strategist"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - icp_profile: Perfil de cliente ideal (dor, jobs-to-be-done, contexto)
  - problem_statement: Dor principal validada do ICP
  - competitive_landscape: Concorrentes e ofertas atuais
Saida: |
  - offer_stack: Oferta principal + complementares (tiers, add-ons, guarantees)
  - value_proposition: Mensagem central por segmento com unique mechanism
  - objection_matrix: Principais objecoes + contra-argumento estrutural
Checklist:
  - "[ ] Definir transformacao prometida (de X para Y em Z tempo)"
  - "[ ] Definir escopo, limites e o que NAO esta incluido"
  - "[ ] Definir estrutura de entrega (1-on-1, grupo, assincrono, hibrido)"
  - "[ ] Criar guarantees que reduzem risco percebido"
  - "[ ] Matriz de objecoes com respostas estruturais"
---

# *design-offer-architecture

Desenha a arquitetura de oferta para maximizar clareza de valor e reduzir ambiguidade comercial.

## Step-by-Step

1. **Absorver ICP + dor** — Ler `icp_profile` e `problem_statement`. Validar com entrevistas se necessario.
2. **Definir transformacao prometida** — Formato: "De [estado atual doloroso] para [estado desejado] em [prazo]".
3. **Mapear unique mechanism** — O que no seu metodo e diferente? Nao e o resultado, e COMO chega.
4. **Estruturar tiers** — 2-3 tiers: basico (entry), principal (mais vendido), premium (high-ticket). Regra 1-2-3 de pricing.
5. **Definir escopo e limites** — O que esta dentro e fora. Reduz expectativas erradas.
6. **Criar guarantees** — Reduzir risco percebido: garantia de resultado, trial, dinheiro de volta, etc.
7. **Montar objection matrix** — Top 5-8 objecoes esperadas + resposta estrutural (nao script, principio).

## Veto Conditions

- VETO se transformacao nao tiver prazo definido → vira promessa vaga
- VETO se unique mechanism for "temos o melhor time/produto" → generico, nao diferencia
- VETO se >3 tiers → paradoxo da escolha, reduz conversao
- VETO se nenhuma guarantee existir → risco todo no cliente, conversao cai

## Output Example

```yaml
offer_stack:
  transformacao: "De produto AIOS pronto sem vendas para R$ 20k+ MRR em 90 dias"
  unique_mechanism: "Squad de 17 agents com cadeia de comando CRO/CCO/CMO/CGO - voce nao executa sozinho"

  tiers:
    - tier: starter
      nome: "Revenue OS Starter"
      preco: "R$ 1.500/mes"
      target: "Founders solo fase 0-1"
      inclui: ["Squad completo", "5 workflows pre-configurados", "Suporte async"]
      limite: "Max 1 produto ativo"

    - tier: principal
      nome: "Revenue OS Standard"
      preco: "R$ 3.000/mes"
      target: "Founders com produto em trafego"
      inclui: ["Tudo do Starter", "LP + checkout assistidos", "2 sync mensais", "Dashboard custom"]
      most_popular: true

    - tier: premium
      nome: "Revenue OS Pro"
      preco: "R$ 8.000/mes"
      target: "Agencias ou founders com R$ 50k+ MRR"
      inclui: ["Tudo do Standard", "White-label", "Multi-produto", "Sync semanal"]

  guarantees:
    - tipo: "Performance"
      descricao: "Se em 14 dias LP+checkout+CRM nao estiverem ativos, devolvemos 100%"
    - tipo: "Trial"
      descricao: "Primeiros 7 dias gratis, cancelamento sem taxa"

value_proposition:
  por_segmento:
    founders_solo:
      headline: "Pare de construir o que ja construiu. Venda o que ja criou."
      subhead: "Squad completo CRO/CCO/CMO/CGO para transformar seu AIOS em receita previsivel"
    agencias:
      headline: "Revenda AIOS como servico premium, com stack comercial pronta"
      subhead: "White-label do Revenue OS para posicionar sua agencia como RevOps-as-a-Service"

objection_matrix:
  - objecao: "Nao tenho tempo para rodar squad"
    contra_argumento_estrutural: "O squad TE diz o proximo passo. Voce nao decide o que fazer, voce apenas executa 2-4h/semana."
  - objecao: "Preco alto pra minha fase"
    contra_argumento_estrutural: "Alternativas: contratar CCO (R$ 25k/mes), freelancers (R$ 8-15k + coordenacao), ou voce mesmo (custo de oportunidade muito maior)"
  - objecao: "Vou conseguir usar squad de IA?"
    contra_argumento_estrutural: "Onboarding assistido de 7 dias + suporte continuo. Se em 30 dias voce nao souber operar, devolucao integral."
```

## Completion Criteria

- Transformacao com prazo + unique mechanism nao generico
- 2-3 tiers com pricing, target e inclui/limite
- 1-2 guarantees reduzindo risco percebido
- Objection matrix com pelo menos 5 objecoes + contra-argumento estrutural

## Handoff

Oferta passa para `@demand-gen-architect` virar copy/criativo/LP. Objecoes alimentam treino do `@sales-system-operator`. Guarantees implementadas pelo `@revops-automation-engineer`.
