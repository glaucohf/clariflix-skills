# SELF-LAUNCH ARTIFACT V1 - Revenue OS

Este documento simula a execucao do `wf-revenue-os-self-launch.yaml` para vender o proprio Revenue OS.

## 1) Oferta (V1)

Produto: Revenue OS
Promessa: sair de produto pronto para stack comercial ativa com operacao semanal de receita.

Planos:
- Starter (R$ 3.500 setup):
  - ICP + oferta + pricing
  - LP spec
  - setup inicial de checkout
- Growth (R$ 1.500/mensal):
  - operacao semanal (experimentos + dashboard + ajustes de funil)
  - 4 ciclos mensais
- Scale (R$ 3.000/mensal):
  - Growth + automacoes avancadas + acompanhamento comercial

## 2) LP de vendas (estrutura)

Hero:
- "Seu produto ja existe. Agora transforme isso em receita previsivel."

Blocos:
- Dor atual: produto pronto sem maquina comercial
- Solucao: departamento completo Marketing + Comercial + RevOps
- Como funciona: 3 workflows + cadencia semanal
- Prova: checklist de stack ativa
- CTA: "Quero ativar meu Revenue OS"

FAQ minimo:
- "Serve para SaaS e servico?" -> sim, com ajuste de ICP e oferta
- "Preciso de time grande?" -> nao, operacao enxuta com agentes + automacao
- "Quando vejo resultado?" -> primeiras validacoes no ciclo de 7 a 14 dias

## 3) Checkout e billing (V1)

Provedor: Stripe

Produtos/precos:
- price_revenue_starter_one_time
- price_revenue_growth_monthly
- price_revenue_scale_monthly

Eventos obrigatorios:
- checkout.session.completed
- invoice.paid
- invoice.payment_failed
- customer.subscription.updated
- customer.subscription.deleted

Automacoes:
- pagamento aprovado -> criar oportunidade "Won" + onboarding
- falha de pagamento -> fluxo de recuperacao D+0, D+2, D+5

## 4) Dashboard de receita (V1)

KPIs diarios:
- visitantes qualificados
- leads gerados
- taxa lead -> call
- taxa call -> close

KPIs de receita:
- MRR
- novas assinaturas
- churn logo
- receita total semanal

Alerta operacional:
- queda > 20% em lead->call por 3 dias
- falha de pagamento > 8% na semana

## 5) Criativos + Email marketing (V1)

Criativos:
- Canal 1 (LinkedIn): 6 posts
- Canal 2 (Instagram): 4 carrosseis
- Canal 3 (YouTube shorts): 4 scripts

Email engine:
- Sequencia aquecimento (3 emails)
- Sequencia prova (3 emails)
- Sequencia fechamento (2 emails)
- Sequencia onboarding cliente (4 emails)

## 6) Operacao comercial (V1)

Pipeline:
- New lead -> Qualified -> Strategy call -> Proposal -> Won/Lost

SLA:
- primeira resposta em ate 30 minutos (horario comercial)
- follow-up D+1, D+3, D+7

Script de discovery:
- dor atual de monetizacao
- meta de receita 90 dias
- gargalo principal (oferta, demanda, conversao ou operacao)

## 7) Meta do teste interno

Janela: 30 dias

Targets:
- 10 calls qualificadas
- 3 fechamentos Starter
- 2 assinaturas Growth
- MRR inicial >= R$ 3.000

## 8) Proximo ciclo (apos semana 1)

- revisar gargalo dominante
- subir 3 experimentos de alto impacto
- ajustar LP e sequencias conforme dados reais
