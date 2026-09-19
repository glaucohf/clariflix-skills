# Tech Stack — Convert Engine Squad

> Referência canônica da stack tecnológica utilizada pelo squad `convert-engine` para geração de landing pages de alta conversão. Todos os agentes devem consultar este documento antes de scaffoldar, configurar ou recomendar tecnologias.

---

## Frontend

### Framework Principal
- **Next.js 14+** com App Router
  - Server Components por padrão (RSC)
  - Streaming e Suspense nativos
  - Metadata API para SEO
  - `next/image` obrigatório para todas as imagens
  - `next/font` para carregamento de fontes sem layout shift

### Linguagem
- **TypeScript 5+**
  - Modo `strict` obrigatório (`"strict": true` no `tsconfig.json`)
  - `noUncheckedIndexedAccess: true`
  - `exactOptionalPropertyTypes: true`
  - Proibido uso de `any` — use `unknown` com type guards

### Estilização
- **Tailwind CSS 3+**
  - Design tokens via CSS Custom Properties (`:root { --color-brand: ... }`)
  - `tailwind.config.ts` com `content` paths e `theme.extend` para tokens
  - Classes utilitárias diretamente nos componentes (sem CSS-in-JS)
  - `clsx` + `tailwind-merge` para composição condicional de classes

### Componentes UI
- **Shadcn/ui** (base Radix UI + Tailwind)
  - Instalação via CLI (`npx shadcn-ui@latest add`)
  - Customização via `components.json` e CSS variables
  - Componentes copiados para `components/ui/` (não são dependência externa)

### Animações
- **Framer Motion 11+**
  - `AnimatePresence` para transições de página
  - `useInView` para animações on-scroll
  - `LazyMotion` + `domAnimation` para reduzir bundle size
  - Respeitar `prefers-reduced-motion` via `useReducedMotion()`

---

## Backend

### Framework
- **Python 3.11+ / FastAPI**
  - Async-first (`async def` em todos os endpoints)
  - Dependency Injection nativa do FastAPI
  - `APIRouter` para modularização de rotas
  - Middleware: CORS, rate limiting, request ID, logging

### ORM e Banco de Dados
- **SQLAlchemy 2.0+** (async com `asyncpg`)
  - Models declarativos com `DeclarativeBase`
  - Sessões async via `AsyncSession`
  - **Alembic** para migrations versionadas
  - Banco padrão: **PostgreSQL 15+**

### Validação e Schemas
- **Pydantic v2**
  - `model_config = ConfigDict(from_attributes=True)` para ORM mode
  - Validators customizados com `@field_validator`
  - Schemas separados: `Create`, `Update`, `Response` por entidade

### Autenticação
- **JWT** via `python-jose` + `passlib[bcrypt]`
  - Access token: 15min
  - Refresh token: 7 dias (rotativo)
  - Dependency `get_current_user` injetada nas rotas protegidas

### Servidor
- **Uvicorn** com workers Gunicorn em produção
  - `uvicorn app.main:app --host 0.0.0.0 --port 8000`
  - Workers: `(2 * CPU) + 1`

---

## Analytics e Tracking

### Tag Management
- **Google Tag Manager (GTM)**
  - Snippet instalado via `app/layout.tsx` (Script com `strategy="afterInteractive"`)
  - Todos os demais pixels e scripts carregados via GTM (exceto GTM próprio)
  - DataLayer tipado com TypeScript

### Analytics
- **Google Analytics 4 (GA4)**
  - Configurado via GTM
  - Eventos customizados: `lead_captured`, `cta_clicked`, `section_viewed`, `form_submitted`
  - Enhanced Measurement ativo
  - Conversions configuradas no GA4 + Google Ads (se aplicável)

### Advertising Pixels
- **Meta Pixel (Facebook/Instagram)**
  - Eventos padrão: `PageView`, `Lead`, `InitiateCheckout`, `Purchase`
  - Parâmetros customizados por nicho (valor, currency, content_name)
- **Meta Conversions API (CAPI)**
  - Server-side via endpoint FastAPI `/api/events/meta`
  - Deduplicação por `event_id` (pixel + CAPI simultâneos)
  - Hashing SHA-256 obrigatório para PII (email, telefone, nome)

### Heatmaps e Sessões
- **Hotjar** (padrão) **ou Microsoft Clarity** (alternativa gratuita)
  - Gravação de sessão habilitada
  - Heatmaps por viewport (desktop, mobile)
  - Funis de conversão configurados
  - Seleção via variável de ambiente `NEXT_PUBLIC_HEATMAP_PROVIDER`

---

## A/B Testing

Provedor configurável via variável de ambiente `NEXT_PUBLIC_AB_PROVIDER`:

| Provedor | Quando usar | Configuração |
|---|---|---|
| **Google Optimize** | Integrado ao GA4, gratuito | `gtag('set', 'optimize_id', 'OPT-XXXXX')` |
| **VWO** | Testes avançados, multivariate | Script via GTM |
| **Optimizely** | Enterprise, edge experimentation | SDK server-side no Next.js middleware |

**Padrão de implementação:**
```typescript
// lib/ab-testing.ts
export function getVariant(experimentId: string): 'control' | 'variant-a' | 'variant-b' {
  // Implementação específica do provedor ativo
}
```

Todos os resultados de testes devem ser registrados em `docs/ab-test-log.md`.

---

## Email Marketing

Provedor configurável via variável de ambiente `EMAIL_PROVIDER`:

| Provedor | SDK | Melhor para |
|---|---|---|
| **SendGrid** | `@sendgrid/mail` | Transacional + marketing |
| **Brevo** (ex-Sendinblue) | `@getbrevo/brevo` | Custo-benefício, LGPD-friendly |
| **Mailchimp** | `@mailchimp/mailchimp_marketing` | Grandes listas, automações |

**Interface unificada** em `backend/app/services/email_service.py`:
```python
class EmailService(Protocol):
    async def send_welcome(self, lead: Lead) -> bool: ...
    async def add_to_list(self, lead: Lead, list_id: str) -> bool: ...
    async def send_sequence(self, lead: Lead, sequence_id: str) -> bool: ...
```

---

## CRM

Provedor configurável via variável de ambiente `CRM_PROVIDER`:

| Provedor | SDK/API | Melhor para |
|---|---|---|
| **HubSpot** | `@hubspot/api-client` | Mercado internacional, B2B |
| **ActiveCampaign** | REST API v3 | Automação avançada |
| **RD Station** | REST API v2 | Mercado brasileiro |

**Interface unificada** em `backend/app/services/crm_service.py`:
```python
class CRMService(Protocol):
    async def create_contact(self, lead: Lead) -> str: ...  # returns CRM ID
    async def update_contact(self, crm_id: str, data: dict) -> bool: ...
    async def add_to_pipeline(self, crm_id: str, stage: str) -> bool: ...
```

---

## Pagamentos

- **Stripe**
  - `stripe` (Python SDK) no backend
  - `@stripe/stripe-js` + `@stripe/react-stripe-js` no frontend
  - Webhooks verificados via `stripe.webhooks.construct_event()`
  - Checkout Sessions (hosted page) como padrão
  - Payment Intents para checkout customizado (quando necessário)
  - Produtos e preços gerenciados via Dashboard do Stripe

---

## WhatsApp

- **evolution-api** (self-hosted ou cloud)
  - REST API para envio de mensagens
  - Webhook para recebimento e processamento
  - Casos de uso: confirmação de lead, follow-up automatizado, suporte
  - Endpoint interno: `backend/app/api/webhooks/whatsapp.py`

---

## Geração de Imagens

### Provedor Primário: nano-banana-pro MCP
- Ferramenta MCP `mcp__nano-banana-pro__generate_image`
- Geração de hero images, banners e ilustrações sob demanda
- Prompt engineering otimizado para landing pages de conversão
- Output: URLs temporárias → download e armazenamento local/CDN

### Provedor Opcional: DALL-E 3
- Via OpenAI API (`openai` Python SDK)
- Fallback quando nano-banana-pro não disponível
- `response_format: "url"`, tamanho padrão `1792x1024` (landscape)

---

## Deploy e Infraestrutura

### Frontend
- **Vercel**
  - Deploy automático via Git integration (GitHub/GitLab)
  - Preview deployments por PR
  - Edge Network (CDN global)
  - Environment variables por ambiente (preview, production)
  - `vercel.json` com headers de cache e redirects

### Backend
- **Railway** (padrão) ou **Render** (alternativa)
  - Deploy via Dockerfile ou Nixpacks
  - PostgreSQL provisionado pelo próprio provider
  - Health check endpoint: `GET /health`
  - Autoscaling habilitado em produção

### Variáveis de Ambiente
Arquivo `.env.example` obrigatório na raiz do projeto com todas as variáveis documentadas (sem valores reais).

---

## Metas de Performance

| Métrica | Meta | Ferramenta de medição |
|---|---|---|
| PageSpeed Score (mobile) | **100** | Google PageSpeed Insights |
| LCP (Largest Contentful Paint) | **< 1.2s** | Core Web Vitals / Lighthouse |
| CLS (Cumulative Layout Shift) | **< 0.1** | Core Web Vitals / Lighthouse |
| FID / INP (Interaction to Next Paint) | **< 100ms** | Core Web Vitals / Lighthouse |
| TTFB (Time to First Byte) | **< 200ms** | WebPageTest |
| Bundle JS (client-side) | **< 100kb** gzipped | next build + analyze |

### Estratégias para atingir as metas
- `next/image` com `priority` no hero (elimina LCP delay)
- Fontes carregadas via `next/font` (elimina CLS de fontes)
- CSS crítico inline (Tailwind gera apenas classes usadas — purge automático)
- Lazy loading de seções below-the-fold com `React.lazy` + `Suspense`
- Code splitting automático por rota (App Router)
- Imagens em formato **WebP** (padrão) e **AVIF** (suportado pelo `next/image`)
- `rel="preconnect"` para domínios externos críticos (GTM, fonts)

---

*Versão: 1.0.0 — Convert Engine Squad*
