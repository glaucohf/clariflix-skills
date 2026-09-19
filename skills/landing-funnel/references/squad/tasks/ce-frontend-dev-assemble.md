---
task: assemblePage()
agent: ce-frontend-dev
description: "Montar página final: todas as seções, metadata SEO, JSON-LD, Open Graph, sitemap"
elicit: false
responsavel: "Turbo"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: sectionComponents
    tipo: file
    obrigatorio: true
    descricao: "Todos os componentes de seção implementados"

Saida:
  - nome: assembledPage
    tipo: file
    obrigatorio: true
    descricao: "Página completa com metadata SEO, JSON-LD, Open Graph e sitemap"

Checklist:
  pre-conditions:
    - "[ ] Todas as seções implementadas"
  post-conditions:
    - "[ ] Meta tags completas"
    - "[ ] JSON-LD estruturado"
    - "[ ] Open Graph configurado"
    - "[ ] Sitemap gerado"
---

# Task: assemblePage()

## Objetivo
Montar a landing page completa compondo todas as seções na ordem correta, implementar metadata SEO completa (title, description, Open Graph, Twitter Card), estruturar JSON-LD para rich results e gerar sitemap. Esta task entrega a página pronta para deploy e indexação.

## Inputs Necessários
- Todos os componentes de seção implementados (`buildSection()` concluído)
- `scope.md` (ordem das seções)
- `copy-review-report.md` (copy final — para metadata)
- `product-brief.md` (nome, URL, domínio)
- Performance otimizada (`optimizePerformance()` concluído)
- Integrações conectadas (`connectFrontendBackend()` concluído, se backend ativo)

## Processo
1. **Composição da página principal** — `src/app/(landing)/page.tsx`:
   ```tsx
   import { HeroSection } from '@/components/organisms/HeroSection'
   import { BenefitsSection } from '@/components/organisms/BenefitsSection'
   import { HowItWorksSection } from '@/components/organisms/HowItWorksSection'
   import { TestimonialsSection } from '@/components/organisms/TestimonialsSection'
   import { PricingSection } from '@/components/organisms/PricingSection'
   import { FAQSection } from '@/components/organisms/FAQSection'
   import { CTASection } from '@/components/organisms/CTASection'
   import { Footer } from '@/components/layout/Footer'

   export default function LandingPage() {
     return (
       <main id="main-content">
         {/* Skip link para acessibilidade */}
         <a href="#main-content" className="sr-only focus:not-sr-only">
           Pular para o conteúdo
         </a>
         <HeroSection />
         <BenefitsSection />
         <HowItWorksSection />
         <TestimonialsSection />
         <PricingSection />
         <FAQSection />
         <CTASection />
         <Footer />
       </main>
     )
   }
   ```

2. **Metadata SEO completa** — `src/app/(landing)/page.tsx` ou layout:
   ```tsx
   import { type Metadata } from 'next'

   export const metadata: Metadata = {
     title: '[Produto] | [Promessa principal em < 60 caracteres]',
     description: '[Descrição clara da oferta em 120-160 caracteres. Inclui CTA implícito.]',
     keywords: ['keyword1', 'keyword2', 'keyword3'],
     authors: [{ name: '[Empresa]' }],
     robots: 'index, follow',
     canonical: 'https://[dominio].com.br',

     openGraph: {
       type: 'website',
       url: 'https://[dominio].com.br',
       title: '[Título para compartilhamento — pode ser diferente do <title>]',
       description: '[Descrição para compartilhamento — pode ser mais impactante]',
       images: [{
         url: 'https://[dominio].com.br/og-image.png',
         width: 1200,
         height: 630,
         alt: '[Alt text descritivo do OG image]',
       }],
       locale: 'pt_BR',
       siteName: '[Nome do produto]',
     },

     twitter: {
       card: 'summary_large_image',
       title: '[Título Twitter]',
       description: '[Descrição Twitter]',
       images: ['https://[dominio].com.br/og-image.png'],
     },
   }
   ```

3. **Open Graph image** — Criar `/public/og-image.png` (1200×630px):
   - Fundo com cor primária ou imagem hero
   - Logo do produto
   - Headline principal
   - CTA ("Acesse gratuitamente" ou similar)
   - Pode ser gerada via `next/og` API (imagem dinâmica):
   ```typescript
   // src/app/og/route.tsx (usando @vercel/og)
   import { ImageResponse } from 'next/og'
   ```

4. **JSON-LD Structured Data** — Implementar schemas relevantes:

   **WebPage:**
   ```json
   {
     "@context": "https://schema.org",
     "@type": "WebPage",
     "name": "[Nome da página]",
     "description": "[Descrição]",
     "url": "https://[dominio].com.br",
     "publisher": {
       "@type": "Organization",
       "name": "[Empresa]",
       "url": "https://[dominio].com.br",
       "logo": "https://[dominio].com.br/logo.png"
     }
   }
   ```

   **Product (se há pricing):**
   ```json
   {
     "@type": "Product",
     "name": "[Nome do produto]",
     "description": "[Descrição]",
     "offers": {
       "@type": "Offer",
       "price": "[Preço]",
       "priceCurrency": "BRL",
       "availability": "https://schema.org/InStock"
     },
     "aggregateRating": {
       "@type": "AggregateRating",
       "ratingValue": "4.9",
       "reviewCount": "[Número real de reviews]"
     }
   }
   ```

   **FAQPage (se há FAQ):**
   ```json
   {
     "@type": "FAQPage",
     "mainEntity": [
       {
         "@type": "Question",
         "name": "[Pergunta]",
         "acceptedAnswer": {
           "@type": "Answer",
           "text": "[Resposta]"
         }
       }
     ]
   }
   ```

   Implementar via componente `<JsonLd>` em `src/lib/schema.ts`.

5. **Sitemap** — `src/app/sitemap.ts`:
   ```typescript
   import { type MetadataRoute } from 'next'

   export default function sitemap(): MetadataRoute.Sitemap {
     return [
       {
         url: 'https://[dominio].com.br',
         lastModified: new Date(),
         changeFrequency: 'monthly',
         priority: 1,
       },
     ]
   }
   ```

6. **Robots.txt** — `src/app/robots.ts`:
   ```typescript
   import { type MetadataRoute } from 'next'

   export default function robots(): MetadataRoute.Robots {
     return {
       rules: { userAgent: '*', allow: '/' },
       sitemap: 'https://[dominio].com.br/sitemap.xml',
     }
   }
   ```

7. **Favicon e PWA icons** — Verificar presença de:
   - `/public/favicon.ico`
   - `/public/apple-touch-icon.png` (180×180)
   - `/public/icon-192.png` e `/public/icon-512.png` (para PWA)
   - Metadata de ícones no root layout

8. **Teste final de montagem** — Verificar:
   - Ordem das seções conforme `scope.md`
   - Todas as seções renderizando corretamente
   - Sem quebras de layout em mobile e desktop
   - Dark/light mode funcionando na página completa
   - JSON-LD válido (usar Google Rich Results Test)
   - OG tags corretas (usar OpenGraph.xyz ou Facebook Debugger)

## Veto Conditions
- `<title>` com mais de 60 caracteres → cortar
- `<meta description>` com menos de 120 ou mais de 160 caracteres → ajustar
- OG image ausente ou com dimensão incorreta → criar/corrigir
- JSON-LD com erro de validação → corrigir antes de lançar
- Sitemap não gerado → criar antes de lançar

## Output Esperado
- `src/app/(landing)/page.tsx` completo e funcional
- Metadata SEO completa (title, description, OG, Twitter)
- JSON-LD implementado (WebPage + Product/FAQ conforme aplicável)
- Sitemap.xml gerado
- Robots.txt configurado
- OG image criada (1200×630)

## Completion Criteria
- [ ] Todas as seções do scope montadas na ordem correta
- [ ] `<title>` entre 30-60 caracteres com keyword principal
- [ ] `<meta description>` entre 120-160 caracteres com CTA implícito
- [ ] Open Graph tags completas (url, title, description, image, locale)
- [ ] Twitter Card configurado
- [ ] JSON-LD válido (testado no Google Rich Results Test)
- [ ] Sitemap gerado e acessível em /sitemap.xml
- [ ] Robots.txt configurado corretamente
- [ ] OG image 1200×630px criada e referenciada
- [ ] Página funcionando em dark e light mode
- [ ] `npm run build` sem erros
