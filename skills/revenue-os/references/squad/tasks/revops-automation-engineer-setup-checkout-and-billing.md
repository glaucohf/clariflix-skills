---
task: Setup Checkout and Billing
responsavel: "@revops-automation-engineer"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - pricing_ladder: Planos e precos (saida do monetization)
  - billing_policy: Regras de cobranca (recorrencia, trial, garantia)
  - checkout_flow_spec: Especificacao do fluxo de checkout
Saida: |
  - checkout_stack: Arquitetura tecnica (provedor + webhooks + integracoes)
  - billing_automation_map: Mapa de automacoes (sucesso/falha/recuperacao)
  - tax_and_compliance_config: Configuracao fiscal e compliance
Checklist:
  - "[ ] Provedor definido e configurado (Stripe ou equivalente)"
  - "[ ] Produtos e precos configurados no provedor"
  - "[ ] Webhooks de pagamento configurados"
  - "[ ] Fluxo de falha + dunning + recuperacao definido"
  - "[ ] Compliance fiscal (NF-e, impostos) implementado"
---

# *setup-checkout-and-billing

Configura checkout online e stack de cobranca para pagamentos recorrentes e avulsos.

## Step-by-Step

1. **Escolher provedor** — Stripe (global), Pagar.me (Brasil), Lastlink (info-produto). Criterios: fees, recorrencia, webhooks, compliance fiscal.
2. **Configurar produtos e precos** — Criar no provedor os tiers + pricing mensal e anual.
3. **Configurar checkout** — Stripe Checkout (hospedado) ou custom. Integrar com LP.
4. **Configurar webhooks** — payment.succeeded, payment.failed, subscription.created, subscription.cancelled.
5. **Fluxo de falha + dunning** — Se cartao falha, automacao tenta novamente em 1, 3, 7 dias. Apos 14 dias, cancelar.
6. **Implementar compliance fiscal** — Integracao NF-e + calculo de impostos + emissao automatica.
7. **Testar end-to-end** — Rodar checkout real com cartao de teste + cancelamento + webhook.

## Veto Conditions

- VETO se webhook nao for idempotente → duplica registro ao receber mesma notificacao
- VETO se cartao expirado nao disparar dunning → perde cliente por gap operacional
- VETO se fluxo de cancelamento exigir >3 passos → friccao desnecessaria gera churn forcado
- VETO se NF-e nao for emitida automaticamente → problema fiscal escalado depois

## Output Example

```yaml
checkout_stack:
  provedor: "Stripe"
  razao: "Melhor DX, webhooks robustos, integracao nativa com Brasil via Stripe BR"

  produtos_configurados:
    - product_id: "prod_starter"
      nome: "Revenue OS Starter"
      prices:
        - id: "price_starter_monthly"
          amount: 150000  # R$ 1.500 em centavos
          interval: "month"
        - id: "price_starter_annual"
          amount: 1500000  # R$ 15.000 em centavos
          interval: "year"
    - product_id: "prod_standard"
      # ...
    - product_id: "prod_pro"
      # ...

  checkout_config:
    tipo: "Stripe Checkout (hospedado)"
    success_url: "/checkout-success"
    cancel_url: "/checkout-cancel"
    payment_methods: ["card", "pix", "boleto"]

  webhooks:
    - event: "checkout.session.completed"
      endpoint: "/api/stripe/checkout-completed"
      acoes: ["Criar usuario", "Enviar welcome email", "Notificar Slack"]
    - event: "invoice.payment_succeeded"
      endpoint: "/api/stripe/payment-succeeded"
      acoes: ["Registrar pagamento", "Emitir NF-e"]
    - event: "invoice.payment_failed"
      endpoint: "/api/stripe/payment-failed"
      acoes: ["Disparar dunning email", "Criar task retry"]
    - event: "customer.subscription.deleted"
      endpoint: "/api/stripe/subscription-cancelled"
      acoes: ["Atualizar status usuario", "Email offboarding", "NPS survey"]

billing_automation_map:
  pagamento_sucesso:
    - "Usuario criado/ativado no sistema"
    - "Welcome email enviado"
    - "NF-e emitida automaticamente"
    - "Onboarding call agendada via Calendly"

  pagamento_falha:
    - dia_0: "Email 'Problema com pagamento' + link atualizar cartao"
    - dia_3: "Retry automatico + email lembrete"
    - dia_7: "Retry automatico + email urgencia"
    - dia_14: "Ultimo retry + email final"
    - dia_15: "Cancelar assinatura + email 'conta suspensa'"

  cancelamento:
    - "Email de confirmacao de cancelamento"
    - "NPS survey automatica"
    - "Offboarding email com acesso ate fim do periodo pago"
    - "CRM: mover para 'churned' + razao"

tax_and_compliance_config:
  nf_e:
    provider: "NFE.io ou Omie"
    emissao: "Automatica apos payment_succeeded"
    regime_tributario: "Simples Nacional (confirmar com contador)"

  compliance:
    - "LGPD: consentimento na checkout + politica de privacidade"
    - "Termos de servico aceitos obrigatorio"
    - "CNPJ/CPF coletado no form"
```

## Completion Criteria

- Checkout funcional end-to-end (teste com cartao real R$ 1)
- Webhooks configurados e testados para sucesso, falha e cancelamento
- Dunning flow com 4 tentativas em 14 dias
- NF-e emitida automaticamente
- LGPD compliance na checkout

## Handoff

`@funnel-conversion-engineer` testa UX do checkout. `@sales-system-operator` recebe notificacoes no CRM. Dashboard de revenue integrado via webhook.
