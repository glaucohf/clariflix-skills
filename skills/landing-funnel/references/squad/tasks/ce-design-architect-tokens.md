---
task: defineDesignTokens()
agent: ce-design-architect
description: "Definir tokens: cores, tipografia, espaçamentos, border-radius, shadows para light e dark mode"
elicit: false
responsavel: "Canvas"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: designSystemChoice
    tipo: file
    obrigatorio: true
    descricao: "Design system e paleta selecionados"

Saida:
  - nome: designTokens
    tipo: file
    obrigatorio: true
    descricao: "Tokens completos: cores, tipografia, espaçamentos, border-radius e shadows para light/dark"

Checklist:
  pre-conditions:
    - "[ ] Design system selecionado"
  post-conditions:
    - "[ ] Tokens CSS exportados"
    - "[ ] Light mode completo"
    - "[ ] Dark mode completo"
---

# Task: defineDesignTokens()

## Objetivo
Traduzir as decisões de design em tokens concretos e implementáveis que o ce-frontend-dev irá consumir. Os tokens são a fonte única da verdade para toda a implementação visual — garantem consistência, facilitam manutenção e permitem a troca completa entre light e dark mode sem refatoração.

## Inputs Necessários
- `design-system-decision.md` (output de `selectDesignSystem()`)
- `scope.md` (dark mode obrigatório, breakpoints mobile/desktop)
- Framework definido (Next.js 14 + Tailwind CSS v3/v4)

## Processo
1. **Definição de tokens de cor** — Estruturar em 3 camadas:

   **Camada 1 — Primitivos (valores absolutos, sem semântica):**
   ```
   --color-blue-50: #eff6ff
   --color-blue-100: #dbeafe
   ...
   --color-blue-950: #172554
   (repetir para cada cor da paleta: primary, gray, green, red, yellow, etc.)
   ```

   **Camada 2 — Semânticos (referências a primitivos, com semântica):**
   ```
   /* Light mode */
   --background: var(--color-gray-50)
   --foreground: var(--color-gray-950)
   --primary: var(--color-blue-600)
   --primary-foreground: var(--color-white)
   --secondary: var(--color-gray-100)
   --secondary-foreground: var(--color-gray-900)
   --muted: var(--color-gray-100)
   --muted-foreground: var(--color-gray-500)
   --accent: var(--color-blue-50)
   --accent-foreground: var(--color-blue-900)
   --destructive: var(--color-red-600)
   --border: var(--color-gray-200)
   --input: var(--color-gray-200)
   --ring: var(--color-blue-600)
   --card: var(--color-white)
   --card-foreground: var(--color-gray-950)
   ```

   **Camada 3 — Dark mode (overrides dos semânticos):**
   ```
   .dark {
     --background: var(--color-gray-950)
     --foreground: var(--color-gray-50)
     --primary: var(--color-blue-400)
     ... (todos os tokens redefinidos para dark)
   }
   ```

2. **Definição de tokens tipográficos** — Estabelecer:
   ```
   --font-display: 'Inter', sans-serif
   --font-body: 'Inter', sans-serif
   --font-mono: 'JetBrains Mono', monospace

   /* Font sizes */
   --text-xs: 0.75rem (12px)
   --text-sm: 0.875rem (14px)
   --text-base: 1rem (16px)
   --text-lg: 1.125rem (18px)
   --text-xl: 1.25rem (20px)
   --text-2xl: 1.5rem (24px)
   --text-3xl: 1.875rem (30px)
   --text-4xl: 2.25rem (36px)
   --text-5xl: 3rem (48px)
   --text-6xl: 3.75rem (60px)

   /* Line heights */
   --leading-tight: 1.25
   --leading-snug: 1.375
   --leading-normal: 1.5
   --leading-relaxed: 1.625
   --leading-loose: 2

   /* Font weights */
   --font-normal: 400
   --font-medium: 500
   --font-semibold: 600
   --font-bold: 700
   --font-extrabold: 800
   ```

3. **Definição de tokens de espaçamento** — Escala baseada em 4px:
   ```
   --space-1: 0.25rem (4px)
   --space-2: 0.5rem (8px)
   --space-3: 0.75rem (12px)
   --space-4: 1rem (16px)
   --space-5: 1.25rem (20px)
   --space-6: 1.5rem (24px)
   --space-8: 2rem (32px)
   --space-10: 2.5rem (40px)
   --space-12: 3rem (48px)
   --space-16: 4rem (64px)
   --space-20: 5rem (80px)
   --space-24: 6rem (96px)
   --space-32: 8rem (128px)
   ```

4. **Definição de tokens de border-radius:**
   ```
   --radius-none: 0px
   --radius-sm: 4px
   --radius-md: 8px (padrão)
   --radius-lg: 12px
   --radius-xl: 16px
   --radius-2xl: 24px
   --radius-full: 9999px
   --radius: var(--radius-md) (variável do design system)
   ```

5. **Definição de tokens de shadow:**
   ```
   --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05)
   --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)
   --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)
   --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)
   --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)
   --shadow-glow: 0 0 20px rgb(var(--primary) / 0.3)
   ```

6. **Definição de breakpoints:**
   ```
   --breakpoint-sm: 640px
   --breakpoint-md: 768px
   --breakpoint-lg: 1024px
   --breakpoint-xl: 1280px
   --breakpoint-2xl: 1536px
   ```

7. **Exportação para tailwind.config.ts** — Gerar extensão do tema Tailwind com todos os tokens.

8. **Exportação para globals.css** — Gerar arquivo CSS com todas as CSS custom properties.

## Veto Conditions
- Tokens de cor sem validação de contraste → verificar antes de finalizar
- Dark mode sem tokens completos (algum token em falta) → completar todos
- Tokens que contradizem `design-system-decision.md` → alinhar

## Output Esperado
- Arquivo `tokens/colors.css` com camadas primitiva + semântica + dark
- Arquivo `tokens/typography.css` com todos os tokens tipográficos
- Arquivo `tokens/spacing.css` com escala de espaçamento
- Arquivo `tokens/effects.css` com radius e shadows
- `tailwind.config.ts` atualizado com todos os tokens
- `globals.css` integrado com @import de todos os arquivos de token
- Arquivo `design-tokens.md` com documentação dos tokens

## Completion Criteria
- [ ] Tokens de cor em 3 camadas (primitivos, semânticos, dark mode)
- [ ] Dark mode com todos os tokens semânticos redefinidos
- [ ] Tokens tipográficos completos (sizes, weights, line-heights, families)
- [ ] Escala de espaçamento baseada em 4px definida
- [ ] Tokens de border-radius definidos
- [ ] Tokens de shadow definidos incluindo glow para CTA
- [ ] Breakpoints definidos
- [ ] `tailwind.config.ts` atualizado
- [ ] `globals.css` integrado
- [ ] Documentação `design-tokens.md` criada para referência do frontend-dev
