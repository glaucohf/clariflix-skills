---
task: implementDesignSystem()
agent: ce-frontend-dev
description: "Implementar design system: tokens CSS, componentes base, dark/light mode toggle"
elicit: false
responsavel: "Turbo"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: designTokens
    tipo: file
    obrigatorio: true
    descricao: "Design tokens do Canvas"
  - nome: atomicComponents
    tipo: file
    obrigatorio: true
    descricao: "Especificação de componentes atômicos"

Saida:
  - nome: implementedDesignSystem
    tipo: file
    obrigatorio: true
    descricao: "Design system implementado: CSS custom properties, componentes base e dark/light mode toggle"

Checklist:
  pre-conditions:
    - "[ ] Design tokens disponíveis"
  post-conditions:
    - "[ ] CSS variables configuradas"
    - "[ ] Dark mode funcional"
    - "[ ] Componentes base implementados"
---

# Task: implementDesignSystem()

## Objetivo
Implementar o design system completo como código — tokens CSS convertidos em variáveis CSS e extensões Tailwind, componentes base criados com todas as variantes especificadas e dark/light mode toggle funcional sem Flash of Unstyled Content (FOUC).

## Inputs Necessários
- `design-tokens.md` (todos os tokens)
- `component-library.md` (especificação de átomos, moléculas, organismos)
- `design-system-decision.md` (design system base, fontes, paleta)
- Setup do projeto completo (`setupFrontendProject()` concluído)

## Processo
1. **Implementação dos tokens CSS** — Converter `design-tokens.md` em arquivos CSS:

   `src/styles/tokens/colors.css`:
   ```css
   :root {
     /* Primitives */
     --color-blue-50: #eff6ff;
     /* ... todos os primitivos ... */

     /* Semantics - Light */
     --background: 0 0% 100%;
     --foreground: 222.2 84% 4.9%;
     --primary: 221.2 83.2% 53.3%;
     /* ... */
   }

   .dark {
     --background: 222.2 84% 4.9%;
     --foreground: 210 40% 98%;
     --primary: 217.2 91.2% 59.8%;
     /* ... todos redefinidos ... */
   }
   ```

   Usar formato HSL para cores (compatível com Shadcn/UI e permite manipulação de opacidade via Tailwind).

2. **Importação no globals.css:**
   ```css
   @import './tokens/colors.css';
   @import './tokens/typography.css';
   @import './tokens/spacing.css';
   @import './tokens/effects.css';

   @layer base {
     * { @apply border-border; }
     body { @apply bg-background text-foreground; }
   }
   ```

3. **Implementação de componentes atômicos** — Para cada átomo do `component-library.md`:

   **Button** (`src/components/atoms/Button.tsx`):
   ```typescript
   import { cva, type VariantProps } from 'class-variance-authority'
   import { cn } from '@/lib/utils'

   const buttonVariants = cva(
     'inline-flex items-center justify-center rounded-md text-sm font-medium transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50',
     {
       variants: {
         variant: {
           primary: 'bg-primary text-primary-foreground hover:bg-primary/90 hover:shadow-glow hover:scale-[1.02]',
           secondary: '...',
           ghost: '...',
           outline: '...',
         },
         size: {
           sm: 'h-8 px-3 text-xs',
           md: 'h-10 px-4 py-2',
           lg: 'h-12 px-6 text-base',
           xl: 'h-14 px-8 text-lg',
         }
       },
       defaultVariants: { variant: 'primary', size: 'md' }
     }
   )
   ```

   Implementar todos os átomos com CVA (class-variance-authority) para variantes type-safe.

4. **Implementação de moléculas** — Composições de átomos:

   **TestimonialCard** (`src/components/molecules/TestimonialCard.tsx`):
   - Props: `quote`, `author`, `role`, `company`, `avatarSrc`, `rating`
   - Variantes: `vertical` | `horizontal` | `featured`
   - Dark mode: automático via CSS variables

   **StatCard** com count-up animation:
   ```typescript
   // Hook useCountUp para animação de número ao entrar no viewport
   // Usar react-intersection-observer para trigger
   ```

   Implementar todas as moléculas da especificação.

5. **Dark/Light mode toggle** — Implementar sem FOUC:

   `src/components/atoms/ThemeToggle.tsx`:
   ```typescript
   'use client'
   import { useTheme } from 'next-themes'
   import { Sun, Moon } from 'lucide-react'
   import { Button } from './Button'

   export function ThemeToggle() {
     const { theme, setTheme } = useTheme()
     return (
       <Button
         variant="ghost"
         size="sm"
         onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
         aria-label="Alternar tema"
       >
         <Sun className="h-4 w-4 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
         <Moon className="absolute h-4 w-4 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
       </Button>
     )
   }
   ```

   Prevenção de FOUC no root layout:
   ```html
   <!-- Script inline no <head> para aplicar tema antes de render -->
   <script>
     if (localStorage.theme === 'dark' || (!('theme' in localStorage) &&
       window.matchMedia('(prefers-color-scheme: dark)').matches)) {
       document.documentElement.classList.add('dark')
     }
   </script>
   ```

6. **Fonte sem CLS (Cumulative Layout Shift)** — Via `next/font`:
   ```typescript
   import { Inter } from 'next/font/google'
   const inter = Inter({ subsets: ['latin'], variable: '--font-body' })
   ```
   Aplicar variáveis CSS de fonte no root layout.

7. **Storybook (opcional mas recomendado)** — Se escopo permite, configurar Storybook para documentação visual dos componentes:
   ```bash
   npx storybook@latest init
   ```

## Veto Conditions
- Dark mode com FOUC → implementar script inline no head
- Componente sem aria-label ou role adequado → adicionar antes de fechar
- Tokens não importados no `globals.css` → importar antes de implementar componentes
- Cores de componentes hardcoded (não usando tokens) → substituir por variáveis CSS

## Output Esperado
- `src/styles/tokens/` com todos os arquivos CSS de tokens
- `src/components/atoms/` com todos os átomos implementados
- `src/components/molecules/` com todas as moléculas implementadas
- `src/components/atoms/ThemeToggle.tsx` funcional
- Dark/light mode funcionando sem FOUC
- `npm run build` sem erros de TypeScript

## Completion Criteria
- [ ] Tokens CSS implementados em arquivos separados e importados em globals.css
- [ ] Todos os átomos implementados com CVA (variantes type-safe)
- [ ] Todas as moléculas implementadas com composição correta
- [ ] Dark mode funcionando sem FOUC em 3 testes consecutivos (reload forçado)
- [ ] ThemeToggle funcional com ícone animado
- [ ] Fontes carregadas via next/font sem CLS
- [ ] `npm run build` sem erros TypeScript
- [ ] `npm run lint` sem warnings de acessibilidade
