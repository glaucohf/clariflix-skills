---
task: designSections()
agent: ce-design-architect
description: "Design de cada seção com layout responsivo, dark/light mode, animações, micro-interactions"
elicit: false
responsavel: "Canvas"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: sectionCopy
    tipo: file
    obrigatorio: true
    descricao: "Copy de cada seção"
  - nome: atomicComponents
    tipo: file
    obrigatorio: true
    descricao: "Componentes atômicos do design system"

Saida:
  - nome: sectionDesigns
    tipo: file
    obrigatorio: true
    descricao: "Design de cada seção com layout responsivo, dark/light mode e micro-interactions"

Checklist:
  pre-conditions:
    - "[ ] Copy disponível"
    - "[ ] Componentes definidos"
  post-conditions:
    - "[ ] Todas as seções designadas"
    - "[ ] Responsividade mobile validada"
    - "[ ] Animações especificadas"
---

# Task: designSections()

## Objetivo
Produzir a especificação visual completa de cada seção da landing page — layouts responsivos, comportamentos de animação, micro-interactions e estados dark/light mode. Este documento é o blueprint que o ce-frontend-dev executa sem precisar tomar decisões visuais.

## Inputs Necessários
- `scope.md` (lista de seções em ordem)
- `cro-design-audit.md` (requisitos de CRO por seção)
- `component-library.md` (componentes disponíveis)
- `design-tokens.md` (tokens de design)
- `copy-review-report.md` (copy final por seção)
- `audience-profile.md` (mobile/desktop split para priorização)

## Processo
Para cada seção definida no `scope.md`, produzir a especificação completa:

1. **Hero Section** — A mais crítica. Especificar:
   - Layout: grid de 2 colunas em desktop (copy esquerda, visual direita) ou full-width com overlay
   - Mobile: stack vertical, copy antes do visual
   - Background: cor sólida, gradiente, imagem com overlay ou vídeo loop
   - Posição do CTA: sempre no viewport sem scroll em mobile (375px) e desktop (1280px)
   - Animações de entrada: fade-in staggered (headline 0ms, subheadline 200ms, CTA 400ms, visual 100ms)
   - Micro-interaction: CTA com scale(1.02) e shadow-glow no hover
   - Social proof bar: position below CTA, fade-in 600ms

2. **Especificação por seção** — Para CADA seção do scope, documentar:

   **Layout Desktop (1280px):**
   - Container max-width, padding horizontal e vertical
   - Grid ou flex layout com colunas e gaps
   - Posição e tamanho de cada elemento
   - Whitespace intencional (breathing room)

   **Layout Tablet (768px):**
   - Mudanças de grid (2 cols → 1 col, etc.)
   - Ajustes de padding e espaçamento
   - Reordenamento de elementos (se necessário)

   **Layout Mobile (375px):**
   - Layout linear, sem grid complexo
   - Padding mínimo para não sugar laterais
   - Tamanho de fonte móbile (escala diferente do desktop)
   - CTAs full-width (100% da largura)

   **Dark Mode:**
   - Mudanças além do simples swap de cor (backgrounds com gradientes, borders)
   - Imagens: versão dark vs overlay escuro na imagem existente
   - Shadows: mais visíveis em dark (inverted não funciona)

   **Animações e transições:**
   - Tipo: fade-in, slide-up, scale-in, stagger
   - Trigger: entrada no viewport (Intersection Observer) ou imediata
   - Duration e easing: especificar (ex: 400ms ease-out)
   - Delay para cada elemento (stagger de 100-200ms entre itens)
   - Sem animações em `prefers-reduced-motion`

   **Micro-interactions:**
   - Hover em cards: scale(1.02), shadow elevação
   - Hover em CTAs: cor + shadow-glow + scale(1.02)
   - Hover em links: underline animado
   - Input focus: ring animado, label float
   - Accordion: smooth expand com rotação do ícone chevron
   - Contadores: count-up ao entrar no viewport

3. **Especificação de imagens e media** — Para cada seção:
   - Dimensões exatas para desktop e mobile
   - Aspect ratio (ex: 16:9, 1:1, 4:3)
   - Comportamento de recorte (object-fit, object-position)
   - Lazy loading: sim/não (hero = eagerly loaded, demais = lazy)
   - Placeholder: blur-up, skeleton ou cor sólida
   - Formato recomendado: WebP com fallback JPEG

4. **Especificação de tipografia por seção** — Para cada elemento textual:
   - Tag HTML semântica (h1, h2, h3, p, span)
   - Tamanho desktop e mobile
   - Peso, cor, line-height
   - Máximo de caracteres por linha (para legibilidade ideal: 60-75 chars)

5. **Mapa de z-index e sobreposições** — Para elementos fixos, sticky e overlays:
   - Navbar sticky: z-50
   - Modais: z-100
   - Toast notifications: z-150
   - Overlays: z-90

## Veto Conditions
- Seção sem especificação mobile → adicionar antes de fechar
- Animação sem especificação de `prefers-reduced-motion` → adicionar fallback estático
- CTA não especificado acima da dobra em mobile para seção Hero → corrigir
- Imagem hero sem lazy-loading: false (deve ser eager) → corrigir

## Output Esperado
Arquivo `sections-design-spec.md` contendo, para CADA seção:
- Layout desktop, tablet e mobile com medidas
- Especificação de dark mode
- Lista de animações com tipo, trigger, duration, delay
- Micro-interactions especificadas
- Especificação de imagens e tipografia
- Componentes utilizados (referenciando `component-library.md`)

## Completion Criteria
- [ ] Todas as seções do scope especificadas
- [ ] Layout responsivo (desktop + tablet + mobile) para cada seção
- [ ] Dark mode especificado para cada seção
- [ ] Animações com type, trigger, duration e delay para cada elemento animado
- [ ] `prefers-reduced-motion` previsto para todas as animações
- [ ] Micro-interactions especificadas para todos os elementos interativos
- [ ] Imagens com dimensões, formato e lazy loading definidos
- [ ] Tipografia por elemento (tag, tamanho desktop/mobile, peso, cor)
- [ ] Arquivo `sections-design-spec.md` criado e entregue ao ce-frontend-dev
