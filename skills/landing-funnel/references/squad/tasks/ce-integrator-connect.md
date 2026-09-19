---
task: connectFrontendBackend()
agent: ce-integrator
description: "Conectar frontend ao backend: API calls, error handling, loading states, success redirects"
elicit: false
responsavel: "Link"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: frontendProject
    tipo: file
    obrigatorio: true
    descricao: "Frontend Next.js montado"
  - nome: backendProject
    tipo: file
    obrigatorio: true
    descricao: "Backend FastAPI funcional"

Saida:
  - nome: connectedSystem
    tipo: file
    obrigatorio: true
    descricao: "Frontend conectado ao backend com API calls, error handling e loading states"

Checklist:
  pre-conditions:
    - "[ ] Frontend e backend funcionais"
  post-conditions:
    - "[ ] Formulário de lead enviando para API"
    - "[ ] Error handling implementado"
    - "[ ] Loading states configurados"
---

# Task: connectFrontendBackend()

## Objetivo
Implementar a camada de integração entre o frontend Next.js e o backend FastAPI, incluindo chamadas de API, tratamento de erros, estados de loading e fluxos de sucesso. A experiência de conversão deve ser fluida — o formulário é o momento mais crítico e qualquer friction técnica pode destruir a taxa de conversão.

## Inputs Necessários
- Frontend com formulário implementado
- Backend com endpoints de leads funcionais
- `scope.md` (quais integrações estão ativas)
- URL do backend (local e produção)

## Processo
1. **Configuração de API client** — `src/lib/api.ts`:
   ```typescript
   const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1'

   export async function apiRequest<T>(
     endpoint: string,
     options: RequestInit = {}
   ): Promise<{ data: T | null; error: string | null }> {
     try {
       const response = await fetch(`${API_BASE}${endpoint}`, {
         headers: { 'Content-Type': 'application/json', ...options.headers },
         ...options,
       })
       if (!response.ok) {
         const errorData = await response.json().catch(() => ({}))
         return { data: null, error: errorData.detail || `Erro ${response.status}` }
       }
       const data = await response.json()
       return { data, error: null }
     } catch (error) {
       return { data: null, error: 'Erro de conexão. Tente novamente.' }
     }
   }
   ```

2. **Hook de submissão de lead** — `src/hooks/use-lead-form.ts`:
   ```typescript
   'use client'
   import { useState, useCallback } from 'react'

   interface LeadFormData {
     name: string
     email: string
     phone?: string
     // Campos honeypot e UTM
     website?: string  // Honeypot — nunca visível, sempre vazio para humanos
     utm_source?: string
     utm_medium?: string
     utm_campaign?: string
   }

   type FormState = 'idle' | 'loading' | 'success' | 'error'

   export function useLeadForm() {
     const [state, setState] = useState<FormState>('idle')
     const [errorMessage, setErrorMessage] = useState<string>('')

     const submitLead = useCallback(async (formData: LeadFormData) => {
       setState('loading')
       setErrorMessage('')

       // Coletar UTM params da URL
       const params = new URLSearchParams(window.location.search)
       const enrichedData = {
         ...formData,
         utm_source: params.get('utm_source') || formData.utm_source,
         utm_medium: params.get('utm_medium') || formData.utm_medium,
         utm_campaign: params.get('utm_campaign') || formData.utm_campaign,
       }

       const { data, error } = await apiRequest<{ id: string; message: string }>(
         '/leads/',
         { method: 'POST', body: JSON.stringify(enrichedData) }
       )

       if (error) {
         setState('error')
         setErrorMessage(error)
         return false
       }

       setState('success')
       // Disparar evento de conversão no client-side (GA4 + Meta Pixel)
       trackConversion({ lead_id: data!.id, email: formData.email })
       return true
     }, [])

     return { state, errorMessage, submitLead }
   }
   ```

3. **Componente de formulário com estados** — `src/components/molecules/LeadForm.tsx`:
   ```tsx
   'use client'
   import { useForm } from 'react-hook-form'
   import { zodResolver } from '@hookform/resolvers/zod'
   import { z } from 'zod'
   import { useLeadForm } from '@/hooks/use-lead-form'

   const schema = z.object({
     name: z.string().min(2, 'Nome deve ter pelo menos 2 caracteres'),
     email: z.string().email('Email inválido'),
     phone: z.string().optional(),
     website: z.string().optional(),  // Honeypot
   })

   export function LeadForm({ onSuccess }: { onSuccess?: () => void }) {
     const { state, errorMessage, submitLead } = useLeadForm()
     const form = useForm({ resolver: zodResolver(schema) })

     if (state === 'success') {
       return (
         <div className="text-center py-8" role="alert" aria-live="polite">
           <div className="text-5xl mb-4">✅</div>
           <h3 className="text-xl font-bold">Recebemos seu contato!</h3>
           <p className="text-muted-foreground mt-2">[Próximo passo específico]</p>
         </div>
       )
     }

     return (
       <form onSubmit={form.handleSubmit(submitLead)} noValidate>
         {/* Campo honeypot — oculto para humanos, preenchido por bots */}
         <input
           {...form.register('website')}
           type="text"
           tabIndex={-1}
           aria-hidden="true"
           className="absolute -z-10 opacity-0 h-0 w-0"
         />

         {/* Campos visíveis */}
         <div className="space-y-4">
           <Input
             {...form.register('name')}
             placeholder="Seu nome completo"
             error={form.formState.errors.name?.message}
             disabled={state === 'loading'}
           />
           <Input
             {...form.register('email')}
             type="email"
             placeholder="Seu melhor email"
             error={form.formState.errors.email?.message}
             disabled={state === 'loading'}
           />

           {errorMessage && (
             <p className="text-destructive text-sm" role="alert">{errorMessage}</p>
           )}

           <Button
             type="submit"
             variant="primary"
             size="xl"
             className="w-full"
             disabled={state === 'loading'}
           >
             {state === 'loading' ? (
               <span className="flex items-center gap-2">
                 <Spinner className="h-4 w-4 animate-spin" />
                 Processando...
               </span>
             ) : '[Texto do CTA principal]'}
           </Button>
         </div>

         <p className="text-xs text-muted-foreground text-center mt-3">
           🔒 Seus dados estão seguros. Sem spam, jamais.
         </p>
       </form>
     )
   }
   ```

4. **Tracking de conversão client-side** — `src/lib/tracking.ts`:
   ```typescript
   declare global {
     interface Window {
       gtag?: (...args: any[]) => void
       fbq?: (...args: any[]) => void
     }
   }

   export function trackConversion({ lead_id, email }: { lead_id: string; email: string }) {
     // GA4 event
     window.gtag?.('event', 'generate_lead', {
       event_category: 'conversion',
       event_label: 'lead_form',
     })

     // Meta Pixel
     const eventId = `lead_${lead_id}_${Date.now()}`
     window.fbq?.('track', 'Lead', {}, { eventID: eventId })

     // Server-side tracking (para maior precisão)
     fetch('/api/v1/track', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify({
         event_name: 'lead_generated',
         client_id: getGA4ClientId(),
         fbp: getCookie('_fbp'),
         fbc: new URLSearchParams(window.location.search).get('fbclid'),
         event_id: eventId,
         page_url: window.location.href,
       }),
     }).catch(() => {}) // Não bloquear UX por falha de tracking
   }
   ```

5. **Variáveis de ambiente** — `.env.local` (frontend):
   ```env
   NEXT_PUBLIC_API_URL=https://api.seuproduto.com.br/api/v1
   NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...
   NEXT_PUBLIC_GA4_ID=G-XXXXXXXXXX
   NEXT_PUBLIC_META_PIXEL_ID=XXXXXXXXXXXXXXXXXX
   ```

## Veto Conditions
- Formulário sem honeypot implementado → adicionar antes de lançar
- Estado de loading ausente (usuário pode submeter múltiplas vezes) → implementar disabled no submit durante loading
- Tracking bloqueando UX em caso de falha → envolver em try/catch silencioso
- UTM params não coletados e enviados ao backend → implementar antes de lançar (perda de dados de atribuição)

## Output Esperado
- `src/lib/api.ts` com client de API type-safe
- `src/hooks/use-lead-form.ts` com estados idle/loading/success/error
- `src/components/molecules/LeadForm.tsx` com honeypot, loading, success e error states
- `src/lib/tracking.ts` com tracking client-side + dispatch server-side
- Variáveis de ambiente documentadas

## Completion Criteria
- [ ] API client com error handling centralizado
- [ ] Hook de formulário com 4 estados (idle/loading/success/error)
- [ ] Honeypot implementado (campo website oculto)
- [ ] UTM params coletados da URL e enviados ao backend
- [ ] Estado de loading com spinner e button desabilitado
- [ ] Estado de sucesso com mensagem positiva
- [ ] Estado de erro com mensagem específica (não genérica)
- [ ] Tracking GA4 + Meta Pixel disparando na conversão
- [ ] Tracking server-side (fetch para /api/v1/track) implementado
- [ ] Teste de fluxo completo: submit → loading → success → tracking verificado
