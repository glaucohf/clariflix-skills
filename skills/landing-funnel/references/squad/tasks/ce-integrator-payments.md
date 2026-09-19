---
task: integratePayments()
agent: ce-integrator
description: "EXCLUSIVO: integração Stripe para checkout direto na LP — one-time ou subscription"
elicit: true
responsavel: "Link"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: stripeConfig
    tipo: object
    obrigatorio: true
    descricao: "Stripe Secret Key e Price ID do produto"

Saida:
  - nome: paymentsIntegration
    tipo: file
    obrigatorio: true
    descricao: "Checkout Stripe Embedded direto na landing page com webhook de confirmação"

Checklist:
  pre-conditions:
    - "[ ] Conta Stripe configurada"
    - "[ ] Produto criado no Stripe"
  post-conditions:
    - "[ ] Checkout Embedded funcional"
    - "[ ] Webhook de pagamento ativo"
    - "[ ] Página de sucesso configurada"
---

# Task: integratePayments()

## Objetivo
Integrar Stripe para processamento de pagamentos diretamente na landing page, suportando cobrança única (one-time) ou recorrente (subscription). Checkout direto na LP elimina a fricção de redirecionar para outra página, aumentando a taxa de conversão em até 20%.

## Inputs Necessários
- `scope.md` (flag `payments` ativa)
- `product-brief.md` (preço, modelo de cobrança)
- Stripe API Keys (Publishable Key + Secret Key)
- Produto e preço configurados no Stripe Dashboard
- Domínio final da LP (para webhook endpoint)

## Processo
1. **Elicitação de configuração:**
   - Stripe Secret Key e Publishable Key
   - Price ID do produto no Stripe
   - Modelo: one-time (`payment`) ou recorrente (`subscription`)
   - Moeda: BRL
   - URL de sucesso e cancelamento após checkout
   - Webhook secret para verificação de eventos

2. **Instalação:**
   ```bash
   pip install stripe  # Backend
   npm install @stripe/stripe-js @stripe/react-stripe-js  # Frontend
   ```

3. **Backend Stripe** — `src/services/stripe_service.py`:
   ```python
   import stripe

   stripe.api_key = settings.STRIPE_SECRET_KEY

   async def create_checkout_session(
       lead: Lead,
       price_id: str,
       mode: str = "payment",  # ou "subscription"
   ) -> str:
       session = stripe.checkout.Session.create(
           payment_method_types=["card"],
           line_items=[{"price": price_id, "quantity": 1}],
           mode=mode,
           customer_email=lead.email,
           client_reference_id=str(lead.id),
           success_url=f"{settings.APP_URL}/sucesso?session_id={{CHECKOUT_SESSION_ID}}",
           cancel_url=f"{settings.APP_URL}/#pricing",
           metadata={
               "lead_id": str(lead.id),
               "utm_source": lead.source or "",
               "utm_campaign": lead.campaign or "",
           },
           # Para checkout embutido (Embedded Checkout)
           ui_mode="embedded",
           return_url=f"{settings.APP_URL}/sucesso?session_id={{CHECKOUT_SESSION_ID}}",
       )
       return session.client_secret  # Para embedded checkout

   async def create_payment_intent(amount: int, currency: str = "brl") -> str:
       """Para checkout customizado (sem redirecionamento)"""
       intent = stripe.PaymentIntent.create(
           amount=amount,  # Em centavos (R$97 = 9700)
           currency=currency,
           payment_method_types=["card"],
           metadata={"product": settings.PRODUCT_NAME},
       )
       return intent.client_secret
   ```

4. **Webhook handler** — `src/api/routes/webhooks.py`:
   ```python
   @router.post("/webhooks/stripe")
   async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
       payload = await request.body()
       sig_header = request.headers.get("stripe-signature")

       try:
           event = stripe.Webhook.construct_event(
               payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
           )
       except stripe.error.SignatureVerificationError:
           raise HTTPException(status_code=400, detail="Invalid signature")

       if event["type"] == "checkout.session.completed":
           session = event["data"]["object"]
           lead_id = session.get("client_reference_id")
           lead = await db.get(Lead, lead_id)
           if lead:
               lead.status = "converted"
               await db.commit()
               # Ações pós-compra: acesso ao produto, email de boas-vindas, CRM update
               await handle_successful_payment(lead, session)

       elif event["type"] == "payment_intent.payment_failed":
           # Notificar lead sobre falha e oferecer ajuda
           pass

       return {"status": "ok"}
   ```

5. **Frontend — Stripe Elements** — Componente de checkout embutido:
   ```tsx
   // src/components/molecules/CheckoutForm.tsx
   'use client'
   import { loadStripe } from '@stripe/stripe-js'
   import { EmbeddedCheckoutProvider, EmbeddedCheckout } from '@stripe/react-stripe-js'
   import { useCallback } from 'react'

   const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!)

   export function CheckoutForm({ priceId }: { priceId: string }) {
     const fetchClientSecret = useCallback(async () => {
       const response = await fetch('/api/checkout', {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify({ priceId }),
       })
       const data = await response.json()
       return data.clientSecret
     }, [priceId])

     return (
       <EmbeddedCheckoutProvider stripe={stripePromise} options={{ fetchClientSecret }}>
         <EmbeddedCheckout />
       </EmbeddedCheckoutProvider>
     )
   }
   ```

6. **API Route Next.js** — `src/app/api/checkout/route.ts`:
   ```typescript
   import { NextRequest, NextResponse } from 'next/server'

   export async function POST(req: NextRequest) {
     const { priceId } = await req.json()
     const response = await fetch(`${process.env.BACKEND_URL}/api/v1/payments/checkout`, {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify({ price_id: priceId }),
     })
     const data = await response.json()
     return NextResponse.json(data)
   }
   ```

7. **Página de sucesso** — `src/app/sucesso/page.tsx`:
   - Confirmar compra ao usuário
   - Instruções de próximo passo (acesso ao produto)
   - Tracking de conversão (server-side via GA4 + Meta CAPI)
   - Oferta de upsell (se aplicável)

## Veto Conditions
- Webhook sem verificação de assinatura Stripe → vulnerabilidade crítica — obrigatório
- Chaves Stripe hardcoded no código → mover para .env
- Sem tratamento de pagamento recusado → implementar feedback ao usuário
- Stripe Publishable Key no backend (nunca) → apenas no frontend

## Output Esperado
- `src/services/stripe_service.py` com checkout e payment intent
- Webhook handler com verificação de assinatura
- Componente React de checkout embutido
- Página de sucesso implementada
- Tracking de conversão pós-compra

## Completion Criteria
- [ ] Stripe configurado com API Keys via .env
- [ ] Checkout session criado com Price ID correto
- [ ] Embedded Checkout funcionando no frontend
- [ ] Webhook endpoint com verificação de assinatura
- [ ] Evento `checkout.session.completed` atualizando lead para "converted"
- [ ] Página de sucesso com próximos passos
- [ ] Tracking de conversão server-side após compra
- [ ] Teste de pagamento com cartão de teste Stripe (4242 4242 4242 4242)
- [ ] Teste de pagamento recusado (4000 0000 0000 0002)
