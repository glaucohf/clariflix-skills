---
task: buildSection()
agent: ce-frontend-dev
description: "Construir uma seção completa: JSX semântico, responsive, animações, acessibilidade WCAG AAA"
elicit: false
responsavel: "Turbo"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: sectionDesign
    tipo: file
    obrigatorio: true
    descricao: "Design da seção específica"
  - nome: sectionCopy
    tipo: file
    obrigatorio: true
    descricao: "Copy da seção"

Saida:
  - nome: sectionComponent
    tipo: file
    obrigatorio: true
    descricao: "Componente React da seção: JSX semântico, responsive, com animações e WCAG AAA"

Checklist:
  pre-conditions:
    - "[ ] Design e copy da seção disponíveis"
  post-conditions:
    - "[ ] ARIA labels presentes"
    - "[ ] Responsividade mobile testada"
    - "[ ] Contraste WCAG AAA (7:1)"
---

# Task: buildSection()

## Objetivo
Implementar uma seção completa da landing page em código React/Next.js, traduzindo fielmente a especificação de design em componente funcional com semântica HTML correta, responsividade perfeita, animações suaves e conformidade WCAG AAA.

## Inputs Necessários
- `sections-design-spec.md` (especificação da seção a construir)
- `component-library.md` (componentes disponíveis)
- `copy-review-report.md` (copy final aprovado da seção)
- Imagens geradas pelo ce-image-creator para a seção
- Design system implementado (`implementDesignSystem()` concluído)
- Identificação da seção a construir

## Processo
1. **Análise da especificação** — Antes de escrever qualquer código:
   - Ler a especificação completa da seção em `sections-design-spec.md`
   - Identificar os componentes necessários (átomos e moléculas)
   - Mapear as animações e micro-interactions
   - Confirmar que todos os assets (imagens) estão disponíveis

2. **Estrutura HTML semântica** — Escolher tags HTML corretas:
   - `<section>` com `aria-labelledby` apontando para o heading da seção
   - `<h2>` para títulos de seção (h1 apenas no hero)
   - `<article>` para itens auto-suficientes (testimonials, cards)
   - `<ul>` + `<li>` para listas de benefícios (não `<div>` em série)
   - `<blockquote>` para depoimentos com `cite` adequado
   - `<figure>` + `<figcaption>` para imagens com legenda

3. **Layout responsivo** — Implementar com Tailwind seguindo mobile-first:
   ```tsx
   <section className="py-16 md:py-24 lg:py-32">
     <div className="container mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl">
       <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
         {/* items */}
       </div>
     </div>
   </section>
   ```
   - Mobile-first: estilos base sem prefixo, maiores com `md:`, `lg:`
   - Container com padding horizontal consistente
   - Grid responsivo que colapsa em mobile

4. **Animações com Framer Motion** — Implementar entrada ao scroll:
   ```tsx
   'use client'
   import { motion } from 'framer-motion'

   const fadeInUp = {
     initial: { opacity: 0, y: 24 },
     animate: { opacity: 1, y: 0 },
     transition: { duration: 0.4, ease: 'easeOut' }
   }

   // Com Intersection Observer para trigger no scroll:
   import { useInView } from 'react-intersection-observer'

   const { ref, inView } = useInView({ triggerOnce: true, threshold: 0.1 })
   <motion.div ref={ref} initial="initial" animate={inView ? 'animate' : 'initial'} variants={fadeInUp}>
   ```

   Para stagger de múltiplos itens:
   ```tsx
   const container = {
     animate: { transition: { staggerChildren: 0.1 } }
   }
   ```

   **prefers-reduced-motion:**
   ```tsx
   const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
   // Desabilitar animações se prefersReduced === true
   ```

5. **Acessibilidade WCAG AAA** — Verificar e implementar:
   - Contraste mínimo 7:1 para texto normal, 4.5:1 para texto grande (AAA)
   - Todos os elementos interativos com `aria-label` ou texto visível
   - Navegação por teclado: foco visível em todos os elementos interativos
   - Imagens com `alt` descritivo (ou `alt=""` para decorativas)
   - Não usar apenas cor para comunicar estado (ícone + texto)
   - Skip link no início da página: "Pular para o conteúdo principal"

6. **Performance da seção** — Implementar boas práticas:
   - `next/image` para todas as imagens com `width`, `height`, `alt`
   - `loading="lazy"` por padrão, `priority` apenas para hero image
   - `sizes` prop correto para imagens responsivas:
     ```tsx
     <Image sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw" />
     ```
   - Evitar `useEffect` desnecessários que causam re-renders

7. **Componente finalizado** — Estrutura de arquivo:
   ```tsx
   // src/components/organisms/[NomeDaSecao]Section.tsx
   import { type FC } from 'react'
   import { motion } from 'framer-motion'
   import { useInView } from 'react-intersection-observer'
   // ... imports de componentes

   interface [NomeDaSecao]SectionProps {
     // Props tipadas
   }

   export const [NomeDaSecao]Section: FC<[NomeDaSecao]SectionProps> = ({ ... }) => {
     // implementação
   }
   ```

## Veto Conditions
- Componente usando `<div>` onde existe tag semântica adequada → corrigir
- Imagem sem `alt` prop → adicionar alt descritivo
- Animação sem verificação de `prefers-reduced-motion` → adicionar
- Hardcode de cores (ex: `text-blue-600`) em vez de tokens (ex: `text-primary`) → corrigir
- Componente client-side sem `'use client'` directive → adicionar
- Layout que quebra em 320px → testar e corrigir

## Output Esperado
Arquivo `src/components/organisms/[NomeDaSecao]Section.tsx` com:
- Componente React funcional e exportado
- JSX semântico e acessível
- Layout responsivo mobile-first
- Animações com Framer Motion (com prefers-reduced-motion)
- Performance otimizada (next/image, lazy loading)
- TypeScript tipos definidos para props

## Completion Criteria
- [ ] Tags HTML semânticas corretas (section, h2, article, ul/li)
- [ ] Layout responsivo testado em 320px, 375px, 768px, 1280px, 1536px
- [ ] Animações de entrada com Intersection Observer implementadas
- [ ] `prefers-reduced-motion` verificado e respeitado
- [ ] Todas as imagens com `alt` descritivo e `next/image`
- [ ] Contraste de texto verificado (WCAG AAA 7:1)
- [ ] Todos os elementos interativos com foco visível
- [ ] Nenhum hardcode de cores — apenas tokens
- [ ] TypeScript sem erros
- [ ] Componente testado no browser em dark e light mode
