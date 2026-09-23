# Revenue OS as Replicable Model

## Objetivo

Usar o `revenue-os` como blueprint replicavel para qualquer ideia de produto.

## Passos de replicacao

1. Defina o nome da oferta, ICP e dor principal.
2. Execute `wf-cro-command-chain.yaml` para ativar a cadeia de comando completa.
3. Execute `wf-zero-to-revenue.yaml` para estruturar o sistema base.
4. Execute `wf-commercial-stack-activation.yaml` para ativar LP, checkout, dashboard, criativos e email.
5. Rode o ciclo semanal com `wf-weekly-revenue-optimization.yaml`.

## Squads complementares recomendados

- `design`: UX/UI da LP e experiencia de conversao
- `brandcraft`: criativos e materiais visuais
- `n8n-builder`: automacoes e webhooks de pagamentos
- `content-os` / `content-engine`: calendario de conteudo, criativos e email
- `project-management-clickup`: operacao e governanca de execucao

## Resultado esperado

Em vez de um plano abstrato, voce termina com:
- oferta e pricing ativos
- stack comercial implantada
- canal de aquisicao em operacao
- dashboard de receita com cadencia de decisao
- governanca executiva ativa (CRO + diretores + operacao)

## Escalabilidade por novos squads

Quando houver demanda fora da capacidade atual, o CRO executa:
- `cro-oracle-capability-gap-and-squad-scaling.md`

Resultado:
- gap report
- decisao de escalonamento
- brief para criacao de novo squad via `@squad-creator`
