# Coding Standards — Convert Engine Squad

> Padrões de código obrigatórios para todos os agentes do squad `convert-engine`. Estes padrões garantem consistência, manutenibilidade e performance máxima nas landing pages geradas.

---

## TypeScript

### Configuração Base (`tsconfig.json`)

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

### Regras de Tipagem

**PROIBIDO:**
```typescript
// NEVER — any apaga o sistema de tipos
const data: any = fetchData()
function process(input: any) { ... }

// NEVER — as any para silenciar erros
const el = document.getElementById('id') as any
```

**OBRIGATÓRIO:**
```typescript
// Use unknown com type guards
async function fetchData(): Promise<unknown> { ... }

function isLead(value: unknown): value is Lead {
  return typeof value === 'object' && value !== null && 'email' in value
}

// Non-null assertion apenas quando a existência é garantida pelo contexto
const el = document.getElementById('cta-button')!  // OK em event handlers após verificação

// Prefer satisfies para validação sem widening
const config = {
  provider: 'sendgrid',
  apiKey: process.env.SENDGRID_API_KEY,
} satisfies EmailConfig
```

### Interfaces vs Types

```typescript
// PREFIRA interfaces para objetos públicos (APIs, props, contratos)
interface Lead {
  id: string
  email: string
  name: string
  createdAt: Date
  source: TrafficSource
}

interface HeroProps {
  headline: string
  subheadline?: string
  ctaText: string
  onCtaClick: () => void
}

// Use type para unions, intersections, primitivos e utilitários
type TrafficSource = 'organic' | 'paid' | 'email' | 'direct' | 'referral'
type LeadStatus = 'new' | 'contacted' | 'qualified' | 'converted'
type Nullable<T> = T | null
type ApiResponse<T> = { data: T; error: null } | { data: null; error: string }
```

### Organização de Imports

```typescript
// 1. Imports do Node/runtime
import { headers } from 'next/headers'

// 2. Imports de terceiros
import { z } from 'zod'
import { motion } from 'framer-motion'

// 3. Imports internos absolutos (alias @/)
import { Button } from '@/components/ui/button'
import { Lead } from '@/types/lead'
import { cn } from '@/lib/utils'

// 4. Imports relativos (apenas quando absolutamente necessário)
import { heroVariants } from './hero.variants'
```

**Alias obrigatório em `tsconfig.json`:**
```json
{
  "paths": {
    "@/*": ["./src/*"]
  }
}
```

---

## Componentes React / Next.js

### Server Components por Padrão

```typescript
// CORRETO — Server Component (padrão, sem 'use client')
// app/components/organisms/TestimonialsSection.tsx
import { getTestimonials } from '@/lib/data/testimonials'

export async function TestimonialsSection() {
  const testimonials = await getTestimonials()
  return (
    <section aria-labelledby="testimonials-heading">
      <h2 id="testimonials-heading">O que nossos clientes dizem</h2>
      {testimonials.map((t) => (
        <TestimonialCard key={t.id} testimonial={t} />
      ))}
    </section>
  )
}
```

```typescript
// 'use client' apenas quando necessário
// components/atoms/CountdownTimer.tsx
'use client'

import { useState, useEffect } from 'react'

export function CountdownTimer({ targetDate }: { targetDate: Date }) {
  const [timeLeft, setTimeLeft] = useState(calculateTimeLeft(targetDate))
  // ...
}
```

### Nomenclatura e Exports

```typescript
// SEMPRE named exports — nunca default export em componentes
export function HeroSection({ headline, ctaText }: HeroProps) { ... }

// NUNCA:
export default function HeroSection() { ... }  // dificulta refactoring e tree-shaking

// Nome do componente SEMPRE igual ao nome do arquivo
// components/organisms/HeroSection.tsx → export function HeroSection
// components/atoms/LoadingSpinner.tsx  → export function LoadingSpinner
```

### Props e Tipos

```typescript
// Props sempre com interface nomeada — nunca objeto inline anônimo
interface CtaButtonProps {
  text: string
  href?: string
  onClick?: () => void
  variant?: 'primary' | 'secondary' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  isLoading?: boolean
  className?: string  // sempre opcional para extensibilidade
}

export function CtaButton({
  text,
  href,
  onClick,
  variant = 'primary',
  size = 'md',
  isLoading = false,
  className,
}: CtaButtonProps) { ... }
```

### Atomic Design — Hierarquia de Componentes

```
components/
├── atoms/         # Menor unidade: Button, Badge, Input, Icon, Label
├── molecules/     # Composição de atoms: FormField, TestimonialCard, PricingCard
└── organisms/     # Seções completas: HeroSection, PricingSection, FaqSection
```

**Regra:** atoms não importam molecules ou organisms. Molecules não importam organisms.

---

## CSS e Tailwind

### Classes Utilitárias

```tsx
// CORRETO — Tailwind classes diretamente
<button className="rounded-lg bg-brand-600 px-6 py-3 text-sm font-semibold text-white shadow-sm hover:bg-brand-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand-600 active:scale-95 transition-all duration-150">
  Quero começar agora
</button>

// CORRETO — clsx + twMerge para composição condicional
import { cn } from '@/lib/utils'

<button className={cn(
  'rounded-lg px-6 py-3 text-sm font-semibold transition-all duration-150',
  variant === 'primary' && 'bg-brand-600 text-white hover:bg-brand-700',
  variant === 'secondary' && 'bg-white text-brand-600 ring-1 ring-brand-600',
  isLoading && 'cursor-not-allowed opacity-60',
  className,
)}>
```

```typescript
// lib/utils.ts
import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### Design Tokens via CSS Custom Properties

```css
/* styles/globals.css */
:root {
  --color-brand-50: #eff6ff;
  --color-brand-600: #2563eb;
  --color-brand-700: #1d4ed8;
  --color-accent: #f59e0b;
  --color-background: #ffffff;
  --color-surface: #f8fafc;
  --color-text-primary: #0f172a;
  --color-text-secondary: #64748b;

  --font-sans: var(--font-inter), system-ui, sans-serif;
  --font-display: var(--font-cal-sans), var(--font-sans);

  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;

  --shadow-brand: 0 4px 14px 0 rgb(37 99 235 / 0.25);
}
```

```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: 'var(--color-brand-50)',
          600: 'var(--color-brand-600)',
          700: 'var(--color-brand-700)',
        },
        accent: 'var(--color-accent)',
      },
      fontFamily: {
        sans: ['var(--font-sans)'],
        display: ['var(--font-display)'],
      },
      boxShadow: {
        brand: 'var(--shadow-brand)',
      },
    },
  },
}

export default config
```

---

## Python / FastAPI

### Type Hints Obrigatórios

```python
# CORRETO — type hints completos
from typing import Optional
from datetime import datetime

async def create_lead(
    lead_data: LeadCreate,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user),
) -> LeadResponse:
    ...

# NUNCA omitir tipos
async def create_lead(lead_data, db):  # PROIBIDO
    ...
```

### Pydantic v2 para Validação

```python
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from datetime import datetime

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    source: TrafficSource = TrafficSource.DIRECT
    utm_campaign: Optional[str] = None

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        # Remover formatação, manter apenas dígitos
        digits = ''.join(filter(str.isdigit, v))
        if len(digits) < 10:
            raise ValueError('Telefone deve ter pelo menos 10 dígitos')
        return digits

class LeadResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    email: str
    created_at: datetime
```

### Endpoints Async

```python
# CORRETO — todos os endpoints async
@router.post('/leads', response_model=LeadResponse, status_code=201)
async def create_lead(
    lead_data: LeadCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
) -> LeadResponse:
    lead = await lead_service.create(db, lead_data)
    background_tasks.add_task(crm_service.sync_lead, lead)
    background_tasks.add_task(email_service.send_welcome, lead)
    return lead

# Tratamento de erros consistente
from fastapi import HTTPException

@router.get('/leads/{lead_id}', response_model=LeadResponse)
async def get_lead(lead_id: str, db: AsyncSession = Depends(get_db)) -> LeadResponse:
    lead = await lead_service.get_by_id(db, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail='Lead não encontrado')
    return lead
```

### Estrutura de Services

```python
# Lógica de negócio SEMPRE em services — nunca diretamente em routers
# backend/app/services/lead_service.py

class LeadService:
    async def create(self, db: AsyncSession, data: LeadCreate) -> Lead:
        existing = await self._get_by_email(db, data.email)
        if existing:
            return existing  # Idempotente — não duplica leads

        lead = Lead(**data.model_dump())
        db.add(lead)
        await db.commit()
        await db.refresh(lead)
        return lead

    async def _get_by_email(self, db: AsyncSession, email: str) -> Optional[Lead]:
        result = await db.execute(select(Lead).where(Lead.email == email))
        return result.scalar_one_or_none()

lead_service = LeadService()
```

---

## Commits — Conventional Commits

### Formato Obrigatório

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Quando usar |
|---|---|
| `feat` | Nova funcionalidade ou seção na landing page |
| `fix` | Correção de bug |
| `perf` | Melhoria de performance (LCP, CLS, bundle size) |
| `style` | Ajustes visuais sem mudança de comportamento |
| `refactor` | Refactoring sem nova funcionalidade ou fix |
| `test` | Adição ou modificação de testes |
| `docs` | Documentação (README, inline docs, ADRs) |
| `chore` | Build, dependencies, configurações |
| `analytics` | Tracking, pixels, eventos de conversão |
| `ab` | Configuração ou resultado de A/B test |

### Exemplos

```bash
feat(hero): add animated countdown timer for urgency
fix(form): validate phone field before lead submission
perf(images): convert hero to AVIF format, LCP 2.1s → 0.9s
analytics(meta): implement CAPI server-side deduplication
ab(pricing): setup VWO test for annual vs monthly default
chore(deps): upgrade next from 14.1 to 14.2
```

### Scopes Recomendados

`hero`, `pricing`, `faq`, `form`, `testimonials`, `social-proof`, `footer`, `analytics`, `ab`, `email`, `crm`, `payments`, `whatsapp`, `api`, `db`, `deploy`

---

## Performance

### Imagens

```tsx
// SEMPRE next/image — nunca <img> nativo em Next.js
import Image from 'next/image'

// Hero image — priority para eliminar LCP delay
<Image
  src="/hero-image.webp"
  alt="Descrição detalhada da imagem para acessibilidade e SEO"
  width={1200}
  height={630}
  priority  // OBRIGATÓRIO para imagens above-the-fold
  quality={85}
  placeholder="blur"
  blurDataURL={heroBlurDataUrl}
/>

// Imagens below-the-fold — lazy loading (padrão do next/image)
<Image
  src="/testimonial-avatar.webp"
  alt="Foto de João Silva, CEO da Empresa X"
  width={64}
  height={64}
  // Sem priority — lazy por padrão
/>
```

### Formatos de Imagem

- **WebP**: padrão para todas as imagens
- **AVIF**: quando suporte do browser é suficiente e ganho de tamanho justifica
- `next/image` gera automaticamente WebP/AVIF via `formats` em `next.config.ts`

```typescript
// next.config.ts
const config: NextConfig = {
  images: {
    formats: ['image/avif', 'image/webp'],
    minimumCacheTTL: 60 * 60 * 24 * 30, // 30 dias
  },
}
```

### Code Splitting

```typescript
// Lazy loading de seções pesadas (carregadas após LCP)
import dynamic from 'next/dynamic'

const VideoSection = dynamic(() => import('@/components/organisms/VideoSection'), {
  loading: () => <VideoSkeleton />,
  ssr: false,  // Evita hydration mismatch para conteúdo dinâmico
})

const ChatWidget = dynamic(() => import('@/components/organisms/ChatWidget'), {
  ssr: false,
})
```

### Preconnect para Recursos Externos

```tsx
// app/layout.tsx — preconnect obrigatório para domínios críticos
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://www.googletagmanager.com" />
  <link rel="preconnect" href="https://connect.facebook.net" />
</head>
```

---

## Acessibilidade (a11y)

### ARIA Labels Obrigatórios

```tsx
// Elementos interativos SEMPRE com aria-label ou aria-labelledby
<button aria-label="Fechar modal de bônus">
  <XIcon aria-hidden="true" />
</button>

// Seções com landmarks semânticos
<section aria-labelledby="pricing-heading">
  <h2 id="pricing-heading">Escolha seu plano</h2>
</section>

<nav aria-label="Navegação principal">
  ...
</nav>
```

### Contraste — WCAG AAA

| Contexto | Ratio mínimo |
|---|---|
| Texto normal | **7:1** (AAA) |
| Texto grande (18px+ ou 14px+ bold) | **4.5:1** (AA) — AAA = 7:1 |
| Componentes UI e gráficos | **3:1** (AA) |

Ferramentas de verificação: WebAIM Contrast Checker, Figma A11y Plugin, `axe-core` (integrado ao Cypress/Playwright).

### Navegação por Teclado

```tsx
// Focus visible sempre visível — nunca remover outline sem substituição
// globals.css
:focus-visible {
  outline: 2px solid var(--color-brand-600);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

// Skip link obrigatório em todas as páginas
// app/layout.tsx
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-brand-600 focus:px-4 focus:py-2 focus:text-white"
>
  Pular para o conteúdo principal
</a>

// ...

<main id="main-content">
  ...
</main>
```

### Formulários Acessíveis

```tsx
// Label explicitamente associado a input
<div className="flex flex-col gap-1.5">
  <label htmlFor="email" className="text-sm font-medium text-text-primary">
    E-mail <span aria-hidden="true">*</span>
    <span className="sr-only">(obrigatório)</span>
  </label>
  <input
    id="email"
    type="email"
    name="email"
    required
    aria-required="true"
    aria-describedby={hasError ? 'email-error' : undefined}
    className="..."
  />
  {hasError && (
    <p id="email-error" role="alert" className="text-sm text-red-600">
      {errorMessage}
    </p>
  )}
</div>
```

### Animações com `prefers-reduced-motion`

```typescript
// hooks/useReducedMotion.ts
import { useReducedMotion as useFramerReducedMotion } from 'framer-motion'

export function useAnimationConfig() {
  const shouldReduceMotion = useFramerReducedMotion()

  return {
    transition: shouldReduceMotion ? { duration: 0 } : { duration: 0.4, ease: 'easeOut' },
    initial: shouldReduceMotion ? {} : { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
  }
}
```

---

## Qualidade e Validação

### Scripts Obrigatórios (`package.json`)

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint && tsc --noEmit",
    "lint:fix": "next lint --fix",
    "typecheck": "tsc --noEmit",
    "test": "jest --passWithNoTests",
    "test:coverage": "jest --coverage",
    "analyze": "ANALYZE=true next build"
  }
}
```

### Gate de Qualidade

Antes de marcar qualquer tarefa como concluída:

1. `npm run lint` — zero warnings ou errors
2. `npm run typecheck` — zero erros de tipo
3. `npm run build` — build de produção sem erros
4. Lighthouse score >= 90 em todas as categorias (Performance, Accessibility, Best Practices, SEO)
5. PageSpeed Insights: LCP < 1.2s, CLS < 0.1, INP < 100ms

---

*Versão: 1.0.0 — Convert Engine Squad*
