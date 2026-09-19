---
task: optimizePerformance()
agent: ce-frontend-dev
description: "EXCLUSIVO: audit e otimização de performance — PageSpeed 100, LCP < 1.2s, CLS < 0.1, imagens otimizadas, code splitting"
elicit: false
responsavel: "Turbo"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: assembledPage
    tipo: file
    obrigatorio: true
    descricao: "Página montada antes da otimização"

Saida:
  - nome: optimizedPage
    tipo: file
    obrigatorio: true
    descricao: "Página otimizada com PageSpeed 100, LCP < 1.2s, CLS < 0.1 e FID < 100ms"

Checklist:
  pre-conditions:
    - "[ ] Página montada e funcional"
  post-conditions:
    - "[ ] PageSpeed Score >= 95"
    - "[ ] LCP < 1.2s"
    - "[ ] CLS < 0.1"
    - "[ ] Imagens em WebP/AVIF"
---

# Task: optimizePerformance()

## Objetivo
Atingir e manter pontuação PageSpeed 100 (ou próximo) em mobile e desktop, com LCP < 1.2s, CLS < 0.1 e FID/INP < 100ms. Performance não é opcional — cada segundo de carregamento reduz a taxa de conversão em 7%. Esta é a task EXCLUSIVA que diferencia LPs de alta conversão de LPs lentas.

## Inputs Necessários
- Landing page com todas as seções construídas (`buildSection()` concluído para todas)
- Todos os assets de imagens gerados
- `traffic-data-analysis.md` (mobile/desktop split — prioridade de otimização)
- `sections-design-spec.md` (imagens planejadas e suas dimensões)

## Processo
1. **Baseline measurement** — Antes de otimizar, medir:
   - Rodar `npm run build` e `npm start` (não dev)
   - Abrir Chrome DevTools → Lighthouse → Mobile + Desktop
   - Registrar scores iniciais: Performance, LCP, CLS, FID/INP, TBT
   - Registrar tamanho total de JS, CSS, imagens
   - Usar WebPageTest.org para medição mais precisa (com throttling real)

2. **Otimização de imagens** — Principal causa de LCP alto:

   **Hero image (LCP crítico):**
   ```tsx
   <Image
     src="/images/hero/hero-desktop.webp"
     alt="..."
     width={1280}
     height={720}
     priority={true}          // Carrega eager (não lazy)
     quality={85}
     sizes="100vw"
   />
   ```

   **Preload do hero image** no head:
   ```tsx
   // Em layout.tsx ou page.tsx
   <link rel="preload" as="image" href="/images/hero/hero-desktop.webp" />
   ```

   **Todas as outras imagens:**
   - `loading="lazy"` (padrão do next/image)
   - `quality={80}` para imagens de seção
   - `sizes` prop correto para evitar download de imagem maior que necessário

   **Converter todas as imagens para WebP:**
   ```bash
   # Se há imagens ainda em PNG/JPEG
   npx sharp-cli --input public/images/**/*.jpg --output public/images/ --format webp
   ```

3. **Eliminação de render-blocking resources:**

   **Fonts:**
   - Usar `next/font` (já configurado no setup) — preloads automáticos
   - Adicionar `display: swap` para text rendering durante load
   - Self-host fonts se necessário para latência zero de DNS lookup

   **CSS crítico:**
   - Tailwind purge já remove CSS não utilizado automaticamente
   - Verificar que `globals.css` não importa bibliotecas CSS pesadas desnecessárias

   **JavaScript:**
   - Next.js App Router já faz code splitting automático por página
   - Verificar bundle size com: `npm run build -- --debug` ou `@next/bundle-analyzer`
   - Remover imports não utilizados em cada componente

4. **Code splitting e lazy loading de componentes:**
   ```tsx
   import dynamic from 'next/dynamic'

   // Componentes abaixo do fold: lazy load
   const TestimonialsSection = dynamic(
     () => import('@/components/organisms/TestimonialsSection'),
     { loading: () => <SectionSkeleton />, ssr: true }
   )

   // Componentes pesados (mapas, vídeos, editores): lazy com ssr: false
   const VideoPlayer = dynamic(
     () => import('@/components/atoms/VideoPlayer'),
     { ssr: false }
   )
   ```

5. **Minimização de CLS (Cumulative Layout Shift):**
   - Sempre definir `width` e `height` em `next/image` (evita layout shift)
   - Fontes: `next/font` já previne CLS de fonte
   - Skeleton placeholders para conteúdo dinâmico (depoimentos carregados via API)
   - Evitar inserção de elementos acima de conteúdo existente no DOM
   - Ads ou embeds com dimensão reservada via aspect-ratio CSS

6. **Otimização de JavaScript (TBT/INP):**
   - Mover lógica pesada para Web Workers quando possível
   - Evitar `useEffect` com dependências que re-executam frequentemente
   - Debounce em scroll handlers e resize listeners
   - Usar `requestAnimationFrame` para animações manuais
   - Preferir CSS animations sobre JS animations quando possível

7. **Configurações de Next.js para produção:**
   ```typescript
   // next.config.ts
   const config = {
     compress: true,
     images: {
       formats: ['image/avif', 'image/webp'],
       minimumCacheTTL: 60 * 60 * 24 * 365, // 1 ano
     },
     headers: async () => [{
       source: '/(.*)',
       headers: [
         { key: 'X-Content-Type-Options', value: 'nosniff' },
         { key: 'X-Frame-Options', value: 'DENY' },
         { key: 'X-XSS-Protection', value: '1; mode=block' },
       ],
     }],
   }
   ```

8. **Cache e CDN** — Verificar configurações:
   - Assets estáticos: Cache-Control max-age=31536000, immutable
   - HTML: no-cache ou curto (10-60s para invalidação rápida pós-deploy)
   - Configurar vercel.json ou plataforma de deploy equivalente

9. **Medição final** — Após todas as otimizações:
   - Lighthouse Mobile: ≥ 90 (ideal 100)
   - Lighthouse Desktop: ≥ 95 (ideal 100)
   - LCP: < 1.2s (mobile LTE, P75)
   - CLS: < 0.1
   - INP: < 100ms
   - Total JS transferido: < 150KB gzipped
   - Total CSS: < 30KB gzipped

## Veto Conditions
- LCP > 2.5s após otimizações → investigar e resolver antes de lançar
- CLS > 0.25 → identificar causa e corrigir (geralmente image sem dimensão ou font)
- Bundle JS > 300KB → analisar e eliminar dependências pesadas
- Hero image sem `priority` prop → adicionar

## Output Esperado
- Landing page com PageSpeed ≥ 90 (mobile) e ≥ 95 (desktop)
- Arquivo `performance-report.md` com: scores antes e depois, ações tomadas, métricas finais
- `next.config.ts` otimizado
- Bundle analyzer report (se usado)

## Completion Criteria
- [ ] Baseline medido com Lighthouse antes das otimizações
- [ ] Hero image com `priority={true}` e preload
- [ ] Todas as imagens em WebP com `sizes` correto
- [ ] Components abaixo do fold com dynamic import
- [ ] CLS < 0.1 verificado (imagens com width/height, sem layout shift)
- [ ] Bundle JS < 150KB gzipped verificado com bundle analyzer
- [ ] Headers de segurança configurados
- [ ] Lighthouse Mobile ≥ 90 e Desktop ≥ 95
- [ ] LCP < 1.2s (ou < 2.5s mínimo aceitável)
- [ ] Arquivo `performance-report.md` com métricas antes/depois
