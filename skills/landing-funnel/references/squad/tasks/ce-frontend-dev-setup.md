---
task: setupFrontendProject()
agent: ce-frontend-dev
description: "Setup Next.js 14+, TypeScript, Tailwind, estrutura de pastas, configuração de SEO base"
elicit: false
responsavel: "Turbo"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: projectScope
    tipo: file
    obrigatorio: true
    descricao: "Escopo com flags condicionais definidas"

Saida:
  - nome: frontendProject
    tipo: file
    obrigatorio: true
    descricao: "Projeto Next.js 14+ configurado com TypeScript, Tailwind e estrutura de pastas"

Checklist:
  pre-conditions:
    - "[ ] Escopo definido com flags"
  post-conditions:
    - "[ ] Next.js 14+ instalado"
    - "[ ] TypeScript em strict mode"
    - "[ ] Tailwind configurado com design tokens"
---

# Task: setupFrontendProject()

## Objetivo
Inicializar o projeto frontend com a stack definida (Next.js 14+, TypeScript, Tailwind CSS), estrutura de pastas escalável e configurações base de SEO. O setup deve ser production-ready desde o início — sem dívida técnica de configuração.

## Inputs Necessários
- `scope.md` (flags ativas, seções, integrações necessárias)
- `design-system-decision.md` (design system selecionado)
- `product-brief.md` (nome do produto, domínio, idioma)
- `design-tokens.md` (para configurar tailwind.config.ts)
- Node.js 18+ e npm/pnpm instalados

## Processo
1. **Inicialização do projeto** — Criar projeto Next.js 14+ com App Router:
   ```bash
   npx create-next-app@latest [nome-do-projeto] \
     --typescript \
     --tailwind \
     --eslint \
     --app \
     --src-dir \
     --import-alias "@/*"
   ```

2. **Instalação de dependências** — Instalar e configurar:

   **UI e Design System:**
   ```bash
   npx shadcn@latest init
   # Selecionar: TypeScript=yes, style=default, baseColor=slate, cssVariables=yes
   npx shadcn@latest add button input form label card separator badge avatar
   ```

   **Animações:**
   ```bash
   npm install framer-motion
   # ou: npm install @formkit/auto-animate (mais leve para animações simples)
   ```

   **Ícones:**
   ```bash
   npm install lucide-react
   ```

   **Fonts:**
   ```bash
   # Next.js font optimization (no next.config.js)
   # Usando next/font para zero layout shift
   ```

   **Utilities:**
   ```bash
   npm install clsx tailwind-merge class-variance-authority
   npm install @radix-ui/react-intersection-observer
   # ou: npm install react-intersection-observer
   ```

   **SEO e Metadata:**
   ```bash
   # Built-in no Next.js 14 via Metadata API
   npm install schema-dts  # TypeScript types para JSON-LD
   ```

3. **Estrutura de pastas** — Organizar conforme:
   ```
   src/
   ├── app/
   │   ├── (landing)/
   │   │   ├── page.tsx          # Página principal da LP
   │   │   └── layout.tsx        # Layout da LP
   │   ├── layout.tsx            # Root layout (fonts, theme provider)
   │   ├── globals.css           # CSS global + tokens
   │   └── robots.ts             # Robots.txt dinâmico
   ├── components/
   │   ├── ui/                   # Shadcn components (auto-gerados)
   │   ├── atoms/                # Componentes atômicos customizados
   │   ├── molecules/            # Moléculas (TestimonialCard, StatCard, etc.)
   │   ├── organisms/            # Seções completas (HeroSection, etc.)
   │   ├── providers/            # Context providers (ThemeProvider, etc.)
   │   └── layout/               # Header, Footer, Nav (se aplicável)
   ├── hooks/
   │   ├── use-intersection.ts   # Intersection Observer para animações
   │   ├── use-scroll.ts         # Scroll position tracking
   │   └── use-media-query.ts    # Mobile/desktop detection
   ├── lib/
   │   ├── utils.ts              # cn() helper e utilities
   │   ├── constants.ts          # Constantes do projeto (URLs, textos fixos)
   │   ├── schema.ts             # JSON-LD schemas
   │   └── validations.ts        # Zod schemas para forms
   ├── types/
   │   └── index.ts              # TypeScript types globais
   └── styles/
       └── tokens/               # Arquivos de design tokens CSS
   public/
   ├── images/
   │   ├── hero/                 # Imagens hero
   │   ├── sections/             # Imagens de seção
   │   ├── social-proof/         # Avatares e thumbnails
   │   └── logos/                # Logos de clientes/parceiros
   ├── fonts/                    # Self-hosted fonts (se aplicável)
   ├── favicon.ico
   ├── apple-touch-icon.png      # 180x180
   ├── og-image.png              # 1200x630 para Open Graph
   └── sitemap.xml               # (ou gerado dinamicamente)
   ```

4. **Configuração do Tailwind** — Aplicar tokens do design system:
   - Substituir `tailwind.config.ts` padrão pelo gerado em `design-tokens.md`
   - Adicionar plugins: `tailwindcss-animate` para animações suaves
   - Configurar `darkMode: 'class'`
   - Adicionar fontes via `fontFamily` extend

5. **Configuração do Next.js** — `next.config.ts`:
   ```typescript
   const config = {
     images: {
       formats: ['image/webp'],
       deviceSizes: [375, 640, 768, 1024, 1280, 1536],
       imageSizes: [16, 32, 48, 64, 96, 128, 256],
     },
     compress: true,
     poweredByHeader: false,
     // Outras otimizações de performance
   }
   ```

6. **Configuração de SEO base** — `src/app/layout.tsx`:
   - Metadata base (title template, description, keywords)
   - Open Graph (og:title, og:description, og:image, og:url, og:type)
   - Twitter Card metadata
   - Canonical URL
   - Viewport meta
   - Idioma e locale

7. **ThemeProvider** — Configurar dark/light mode:
   ```typescript
   // next-themes para gerenciamento de tema sem flash
   npm install next-themes
   ```
   Implementar `ThemeProvider` sem FOUC (Flash of Unstyled Content).

8. **ESLint + Prettier** — Configurar qualidade de código:
   - `.eslintrc.json` com regras de acessibilidade (`eslint-plugin-jsx-a11y`)
   - `.prettierrc` com configuração consistente

## Veto Conditions
- Setup sem TypeScript strict mode → ativar `"strict": true` no tsconfig
- Sem configuração de dark mode → implementar antes de avançar
- Sem estrutura de pastas organizada por atomic design → reorganizar
- Instalação de dependências com conflitos de versão → resolver antes de avançar

## Output Esperado
Projeto Next.js funcional com:
- `npm run dev` rodando sem erros
- `npm run build` completando sem erros
- `npm run lint` sem erros
- Dark/light mode funcionando
- Estrutura de pastas criada
- Todos os tokens de design importados

## Completion Criteria
- [ ] `create-next-app` executado com App Router, TypeScript, Tailwind
- [ ] Shadcn/UI inicializado e componentes base adicionados
- [ ] Framer Motion e Lucide instalados
- [ ] Estrutura de pastas criada conforme especificação
- [ ] `tailwind.config.ts` com todos os tokens do design system
- [ ] `next.config.ts` com otimização de imagens configurada
- [ ] Metadata SEO base configurada no root layout
- [ ] ThemeProvider instalado e dark mode funcionando sem FOUC
- [ ] ESLint com jsx-a11y configurado
- [ ] `npm run dev`, `build` e `lint` passando sem erros
