# Teste Rapido - Revenue OS

Objetivo: ver o `revenue-os` funcionando na pratica em 60-90 minutos (modo MVP).

## O que ja esta pronto

- Estrutura completa do squad (`agents`, `tasks`, `workflows`, `checklists`).
- Fluxo de ativacao comercial (`wf-commercial-stack-activation.yaml`).
- Fluxo de dogfooding (`wf-revenue-os-self-launch.yaml`).
- Blueprint preenchido do self-launch (`data/self-launch-blueprint-v1.yaml`).

## O que falta para teste real (externo ao repo)

1. Pagamentos
- Conta Stripe (ou equivalente) com chaves de teste.
- 3 produtos/precos criados (Starter, Growth, Scale).

2. LP de vendas
- Uma pagina publicada (mesmo simples) com CTA para checkout.
- Pode ser no seu stack atual ou via squad de design + implementacao.

3. CRM
- Pipeline com estagios minimos configurado (New -> Qualified -> Call -> Proposal -> Won/Lost).

4. Canal de ativacao
- Pelo menos 1 canal ativo (LinkedIn recomendado para iniciar).

## Passo a passo minimo

1. Validar squad localmente
- `python3 squads/squad-creator/scripts/validate-squad-structure.py revenue-os`

2. Carregar blueprint V1
- Arquivo: `squads/revenue-os/data/self-launch-blueprint-v1.yaml`
- Ajustar apenas 4 campos para sua realidade:
  - `owner`
  - `target_mrr_30d_brl`
  - `pricing`
  - `channels`

3. Rodar o fluxo de self-launch (operacional)
- Referencia: `squads/revenue-os/workflows/wf-revenue-os-self-launch.yaml`
- Ordem sugerida:
  - cadeia executiva CRO (`wf-cro-command-chain.yaml`)
  - oferta/pricing
  - LP/checkout/dashboard
  - criativos/email
  - operacao comercial

4. Publicar LP + checkout de teste
- Confirmar que o CTA abre checkout e fecha compra teste.

5. Validar webhooks e dashboard
- Simular `payment_succeeded` e `payment_failed`.
- Verificar se MRR e eventos aparecem no dashboard.

6. Rodar micro-campanha de validacao
- 1 semana com volume pequeno (ex.: 6 posts + 3 emails).
- Objetivo: captar primeiros leads e validar funil.

## Evidencias que voce deve ver

- 1 compra teste concluida no checkout.
- 1 lead andando no pipeline ate "Won".
- Dashboard com pelo menos:
  - leads
  - conversoes por etapa
  - MRR inicial
- Log de pelo menos 1 experimento na semana.

## Critico para nao travar

- Nao esperar stack perfeita para iniciar.
- Rodar com uma LP simples e um canal principal.
- Aprender no ciclo semanal e iterar.
