# Source Tree — Convert Engine Squad

> Estrutura de pastas canônica para projetos gerados pelo squad `convert-engine`. Todos os agentes devem seguir esta estrutura rigorosamente ao criar arquivos. Desvios requerem justificativa explícita no story file.

---

## Visão Geral

```
projeto/
├── frontend/                          # Next.js 14+ App Router
├── backend/                           # FastAPI (condicional — ver abaixo)
├── docs/                              # Documentação do projeto
├── .env.example                       # Template de variáveis de ambiente
├── .gitignore
├── docker-compose.yml                 # Dev environment (opcional)
└── README.md
```

> **Backend condicional:** a pasta `backend/` só é scaffoldada quando o projeto requer lógica server-side (captura de leads com CRM, webhooks, Conversions API server-side, autenticação). Projetos simples (landing estática com form para webhook externo) usam apenas `frontend/`.

---

## Frontend (`frontend/`)

```
frontend/
├── app/                               # Next.js App Router
│   ├── layout.tsx                     # Root layout: fonts, GTM, metadata global
│   ├── page.tsx                       # Home page (landing principal)
│   ├── globals.css                    # Design tokens, reset, base styles
│   ├── (landing)/                     # Route group — variantes de landing
│   │   ├── [variant]/
│   │   │   └── page.tsx               # Variante A/B (ex: /a, /b, /controle)
│   ├── obrigado/
│   │   └── page.tsx                   # Thank-you page pós-conversão
│   ├── api/                           # API Routes (Next.js)
│   │   ├── leads/
│   │   │   └── route.ts               # POST /api/leads (captura de lead)
│   │   └── events/
│   │       └── meta/
│   │           └── route.ts           # POST /api/events/meta (CAPI)
│   ├── robots.txt/
│   │   └── route.ts                   # robots.txt dinâmico
│   └── sitemap.ts                     # Sitemap automático
│
├── components/
│   ├── atoms/                         # Menores unidades UI
│   │   ├── Button.tsx                 # CTA principal — variantes: primary, secondary, ghost
│   │   ├── Badge.tsx                  # Badges: "Mais popular", "Desconto", "Novo"
│   │   ├── Input.tsx                  # Input com label, error state, aria
│   │   ├── Textarea.tsx
│   │   ├── Select.tsx
│   │   ├── Checkbox.tsx
│   │   ├── Icon.tsx                   # Wrapper para ícones (lucide-react)
│   │   ├── Avatar.tsx                 # Avatar com fallback inicial
│   │   ├── Skeleton.tsx               # Loading skeleton genérico
│   │   ├── Divider.tsx                # Separador visual com texto opcional
│   │   └── CountdownTimer.tsx         # Timer regressivo (client component)
│   │
│   ├── molecules/                     # Composições de atoms
│   │   ├── FormField.tsx              # Label + Input + ErrorMessage
│   │   ├── LeadForm.tsx               # Formulário de captura de lead
│   │   ├── TestimonialCard.tsx        # Card de depoimento individual
│   │   ├── PricingCard.tsx            # Card de plano/preço
│   │   ├── FaqItem.tsx                # Item de FAQ (accordion)
│   │   ├── FeatureCard.tsx            # Card de feature/benefício
│   │   ├── BonusCard.tsx              # Card de bônus/brinde
│   │   ├── GuaranteeBox.tsx           # Caixa de garantia
│   │   ├── SocialProofBar.tsx         # Barra com logos, números, awards
│   │   ├── VideoPlayer.tsx            # Player de vídeo (YouTube/Vimeo/nativo)
│   │   ├── StarRating.tsx             # Avaliação por estrelas
│   │   └── NotificationPop.tsx        # Pop-up de social proof (compra recente)
│   │
│   └── organisms/                     # Seções completas da landing page
│       ├── HeroSection.tsx            # Above-the-fold: headline + CTA + hero image
│       ├── SocialProofSection.tsx     # Logos de clientes/mídia, números, awards
│       ├── ProblemSection.tsx         # Seção problema/dor do cliente
│       ├── SolutionSection.tsx        # Apresentação da solução/produto
│       ├── FeaturesSection.tsx        # Grid de features/benefícios
│       ├── HowItWorksSection.tsx      # Passo a passo / processo
│       ├── TestimonialsSection.tsx    # Grid/carrossel de depoimentos
│       ├── VideoSection.tsx           # VSL ou vídeo de apresentação
│       ├── PricingSection.tsx         # Planos e preços
│       ├── BonusSection.tsx           # Bônus e brindes
│       ├── GuaranteeSection.tsx       # Garantia de satisfação
│       ├── FaqSection.tsx             # Perguntas frequentes
│       ├── CtaSection.tsx             # CTA final (repetição do hero)
│       ├── FooterSection.tsx          # Rodapé: legal, links, contato
│       ├── StickyCtaBar.tsx           # Barra CTA fixa no mobile
│       └── ExitIntentModal.tsx        # Pop-up de exit intent (client component)
│
├── lib/
│   ├── utils.ts                       # cn(), formatters, helpers genéricos
│   ├── validations.ts                 # Zod schemas para forms
│   ├── constants.ts                   # URLs, configs estáticas
│   ├── ab-testing.ts                  # Abstração do provedor de A/B test
│   ├── analytics/
│   │   ├── gtm.ts                     # DataLayer typesafe
│   │   ├── events.ts                  # Definição de todos os eventos de tracking
│   │   └── meta-capi.ts               # Helpers para Conversions API
│   ├── data/
│   │   ├── testimonials.ts            # Dados de depoimentos
│   │   ├── faq.ts                     # Dados de FAQ
│   │   ├── pricing.ts                 # Dados de preços/planos
│   │   └── features.ts                # Dados de features/benefícios
│   └── hooks/
│       ├── useLeadForm.ts             # Form state, validation, submission
│       ├── useScrollTracking.ts       # Track seções visitadas
│       ├── useExitIntent.ts           # Detecção de exit intent
│       ├── useCountdown.ts            # Lógica do countdown timer
│       └── useReducedMotion.ts        # Acessibilidade — motion preference
│
├── styles/
│   └── globals.css                    # CSS custom properties (design tokens)
│
├── public/
│   ├── images/
│   │   ├── hero/                      # Imagens do hero section
│   │   ├── testimonials/              # Fotos de depoimentos
│   │   ├── logos/                     # Logos de clientes/parceiros
│   │   └── product/                   # Screenshots/fotos do produto
│   ├── icons/
│   │   └── favicon.ico
│   └── og-image.png                   # Open Graph image (1200x630)
│
├── types/
│   ├── index.ts                       # Re-exports centralizados
│   ├── lead.ts                        # Lead, LeadCreate, LeadResponse
│   ├── analytics.ts                   # DataLayer events, GTM types
│   ├── ab-testing.ts                  # Experiment, Variant, ExperimentConfig
│   └── api.ts                         # ApiResponse<T>, ApiError
│
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
├── postcss.config.js
├── components.json                    # Shadcn/ui config
├── .env.local                         # (gitignored)
└── package.json
```

---

## Backend (`backend/`) — Condicional

```
backend/
├── app/
│   ├── main.py                        # FastAPI app factory, middleware, lifespan
│   ├── config.py                      # Settings via pydantic-settings
│   ├── dependencies.py                # Shared dependencies (db, auth, services)
│   │
│   ├── api/                           # Routers — agrupados por domínio
│   │   ├── __init__.py
│   │   ├── router.py                  # API root router — inclui todos os sub-routers
│   │   ├── leads/
│   │   │   ├── __init__.py
│   │   │   ├── router.py              # POST /leads, GET /leads/{id}
│   │   │   └── handlers.py            # Handler functions (thin — delegam a services)
│   │   ├── events/
│   │   │   ├── __init__.py
│   │   │   └── router.py              # POST /events/meta (CAPI), /events/track
│   │   ├── webhooks/
│   │   │   ├── __init__.py
│   │   │   ├── stripe.py              # POST /webhooks/stripe
│   │   │   └── whatsapp.py            # POST /webhooks/whatsapp
│   │   └── health/
│   │       └── router.py              # GET /health (liveness + readiness)
│   │
│   ├── models/                        # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── base.py                    # DeclarativeBase, TimestampMixin
│   │   ├── lead.py                    # Lead model
│   │   ├── conversion.py              # Conversion event model
│   │   └── ab_variant.py              # A/B test assignment model
│   │
│   ├── schemas/                       # Pydantic v2 schemas
│   │   ├── __init__.py
│   │   ├── lead.py                    # LeadCreate, LeadUpdate, LeadResponse
│   │   ├── event.py                   # MetaEvent, TrackEvent
│   │   └── common.py                  # Pagination, ApiResponse, ErrorDetail
│   │
│   ├── services/                      # Business logic layer
│   │   ├── __init__.py
│   │   ├── lead_service.py            # CRUD + deduplicação + validações
│   │   ├── email_service.py           # Interface + implementações (SendGrid, Brevo)
│   │   ├── crm_service.py             # Interface + implementações (HubSpot, RD Station)
│   │   ├── meta_capi_service.py       # Server-side Conversions API
│   │   ├── whatsapp_service.py        # evolution-api integration
│   │   └── payment_service.py         # Stripe checkout, webhooks
│   │
│   ├── core/                          # Infraestrutura transversal
│   │   ├── __init__.py
│   │   ├── database.py                # AsyncSession factory, get_db dependency
│   │   ├── security.py                # JWT encode/decode, password hashing
│   │   ├── exceptions.py              # Custom exceptions + exception handlers
│   │   ├── logging.py                 # Structured logging config (structlog)
│   │   └── middleware.py              # Request ID, timing, CORS
│   │
│   └── utils/
│       ├── __init__.py
│       ├── hashing.py                 # SHA-256 para PII (CAPI)
│       ├── phone.py                   # Normalização/validação de telefone
│       └── date.py                    # Helpers de data/timezone
│
├── migrations/                        # Alembic migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 0001_initial_schema.py
│
├── tests/
│   ├── conftest.py                    # Fixtures: async client, test db, factories
│   ├── unit/
│   │   ├── services/
│   │   │   ├── test_lead_service.py
│   │   │   ├── test_email_service.py
│   │   │   └── test_meta_capi_service.py
│   │   └── utils/
│   │       └── test_hashing.py
│   └── integration/
│       ├── test_leads_api.py
│       ├── test_webhooks_stripe.py
│       └── test_health.py
│
├── alembic.ini
├── pyproject.toml                     # uv/Poetry config, dependencies, linting
├── Dockerfile
├── .env.example
└── requirements.txt                   # Ou pyproject.toml com uv
```

---

## Documentação (`docs/`)

```
docs/
├── analytics-setup.md                 # Guia de configuração: GTM, GA4, Meta Pixel, CAPI
├── ab-test-log.md                     # Registro histórico de todos os testes A/B
├── conversion-report.md               # Relatório de conversão: funil, benchmarks, insights
├── deploy-guide.md                    # Passo a passo de deploy: Vercel + Railway/Render
├── environment-variables.md           # Documentação de todas as env vars
└── performance-audit.md               # Resultados de Lighthouse / PageSpeed por data
```

### Formato: `docs/ab-test-log.md`

```markdown
# A/B Test Log

## Teste #001 — Hero Headline
- **Período:** 2025-01-10 a 2025-01-24 (14 dias)
- **Ferramenta:** VWO
- **Hipótese:** Headline focada em resultado supera headline focada em processo
- **Controle:** "Aprenda a investir em 30 dias"
- **Variante A:** "Transforme R$1.000 em R$1.800 nos próximos 30 dias"
- **Tráfego:** 50/50
- **Resultado:** Variante A: 4.2% conv | Controle: 2.8% conv | +50% lift | p-value: 0.03
- **Decisão:** Implementar Variante A como novo controle
- **Próximo teste:** Subheadline / CTA text
```

### Formato: `docs/conversion-report.md`

```markdown
# Conversion Report

## Resumo Executivo
- **Taxa de conversão atual:** X.X%
- **Benchmark do nicho:** X.X%
- **Posição relativa:** Acima/Abaixo da média
- **Maior alavanca identificada:** [seção/elemento]

## Funil de Conversão
| Etapa | Sessões | % |
|---|---|---|
| Visitantes | 10.000 | 100% |
| Scroll > 50% | 6.200 | 62% |
| Formulário iniciado | 1.800 | 18% |
| Formulário enviado | 420 | 4.2% |
| Thank you page | 400 | 4.0% |

## Top Oportunidades
1. [Oportunidade + dados + hipótese de melhoria]
```

---

## Convenções de Nomenclatura

### Arquivos TypeScript/React

| Tipo | Convenção | Exemplo |
|---|---|---|
| Componentes | PascalCase | `HeroSection.tsx`, `LeadForm.tsx` |
| Hooks | camelCase com `use` | `useLeadForm.ts`, `useCountdown.ts` |
| Utilitários | camelCase | `utils.ts`, `analytics.ts` |
| Tipos | camelCase | `lead.ts`, `ab-testing.ts` |
| Constantes | camelCase | `constants.ts` |
| Config | kebab-case (config files) | `next.config.ts`, `tailwind.config.ts` |

### Arquivos Python

| Tipo | Convenção | Exemplo |
|---|---|---|
| Módulos | snake_case | `lead_service.py`, `meta_capi_service.py` |
| Classes | PascalCase | `LeadService`, `MetaCAPIService` |
| Funções/métodos | snake_case | `create_lead()`, `get_by_email()` |
| Constantes | UPPER_SNAKE_CASE | `MAX_RETRY_ATTEMPTS`, `JWT_ALGORITHM` |

### Variáveis de Ambiente

| Prefixo | Contexto | Exemplo |
|---|---|---|
| `NEXT_PUBLIC_` | Exposto ao browser | `NEXT_PUBLIC_GTM_ID`, `NEXT_PUBLIC_META_PIXEL_ID` |
| Sem prefixo | Server-only | `SENDGRID_API_KEY`, `DATABASE_URL`, `STRIPE_SECRET_KEY` |

---

## Regras de Importação

### Aliases Obrigatórios (TypeScript)

```typescript
// tsconfig.json paths
"@/*": ["./src/*"]           // raiz do frontend/src
"@/components/*"             // components/
"@/lib/*"                    // lib/
"@/types/*"                  // types/
"@/styles/*"                 // styles/
```

### Ordem de Importação (aplicada pelo ESLint)

1. Node built-ins
2. Next.js e React
3. Bibliotecas de terceiros
4. Imports internos absolutos (`@/`)
5. Imports relativos (`./`, `../`)

---

*Versão: 1.0.0 — Convert Engine Squad*
