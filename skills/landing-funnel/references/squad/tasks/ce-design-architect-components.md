---
task: createAtomicComponents()
agent: ce-design-architect
description: "Criar átomos, moléculas e organismos do design system com variantes"
elicit: false
responsavel: "Canvas"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: designTokens
    tipo: file
    obrigatorio: true
    descricao: "Design tokens definidos"

Saida:
  - nome: atomicComponents
    tipo: file
    obrigatorio: true
    descricao: "Átomos, moléculas e organismos do design system com todas as variantes"

Checklist:
  pre-conditions:
    - "[ ] Design tokens disponíveis"
  post-conditions:
    - "[ ] Átomos definidos (botões, inputs, badges)"
    - "[ ] Moléculas compostas"
    - "[ ] Organismos de seção prontos"
---

# Task: createAtomicComponents()

## Objetivo
Definir a biblioteca de componentes da landing page em três níveis de atomic design (átomos, moléculas, organismos). Esta especificação garante que o ce-frontend-dev implemente componentes consistentes, reutilizáveis e alinhados com o design system definido.

## Inputs Necessários
- `design-system-decision.md` (design system, paleta, tipografia)
- `design-tokens.md` (todos os tokens)
- `cro-design-audit.md` (requisitos de CRO que impactam componentes)
- `scope.md` (lista de seções — define quais componentes são necessários)
- `copy-review-report.md` (tipos de conteúdo que os componentes precisam suportar)

## Processo
1. **Definição de Átomos** — Componentes indivisíveis com todas as suas variantes:

   **Button:**
   - Variantes: primary, secondary, ghost, outline, destructive, link
   - Tamanhos: sm (32px), md (40px), lg (48px), xl (56px)
   - Estados: default, hover, active, disabled, loading (spinner)
   - Dark mode: versões para cada variante em dark
   - Acessibilidade: foco visível, aria-label, role adequado
   - CRO: primary button com shadow-glow no hover para aumentar clique

   **Input/Form field:**
   - Tipos: text, email, phone, textarea, select
   - Estados: default, focus, filled, error, disabled
   - Com e sem label flutuante
   - Microcopy de validação inline (não em alert genérico)

   **Badge/Tag:**
   - Variantes: default, primary, success, warning, destructive, outline
   - Uso: "NOVO", "MAIS POPULAR", "ECONOMIZE X%", trust signals

   **Avatar:**
   - Variantes: image, initials, icon
   - Tamanhos: xs (24px), sm (32px), md (40px), lg (48px), xl (64px)
   - Com indicador de status (online/offline)

   **Icon:**
   - Biblioteca: Lucide React (tree-shakeable)
   - Tamanhos: 16px, 20px, 24px, 32px
   - Animações opcionais: spin, pulse, bounce

   **Separator/Divider:**
   - Horizontal e vertical
   - Com e sem label central

2. **Definição de Moléculas** — Combinações de átomos com propósito específico:

   **TestimonialCard:**
   - Avatar + Nome + Cargo/Empresa + Texto + Estrelas (rating)
   - Variantes: vertical (card), horizontal (inline), featured (com foto grande)
   - Dark/Light mode

   **PricingCard:**
   - Nome do plano + Preço + Período + Lista de benefícios + CTA + Badge "Recomendado"
   - Variantes: basic, featured (destaque), enterprise
   - Animação: scale no hover para o plano recomendado

   **FormSection:**
   - Título + Subtítulo + Campos + CTA + Microcopy de privacidade/garantia
   - Variantes: inline (horizontal), stacked (vertical), modal

   **StatCard:**
   - Número em destaque + Label + Ícone opcional
   - Variante com contador animado (count-up ao entrar no viewport)

   **FeatureItem:**
   - Ícone + Título + Descrição
   - Variantes: vertical (grid), horizontal (list), com imagem

   **SocialProofBar:**
   - Linha com avatares empilhados + "X pessoas já [resultado]" + Stars rating

3. **Definição de Organismos** — Seções completas e auto-suficientes:

   **HeroSection:**
   - Badge "Como funciona" + Headline H1 + Subheadline + CTA pair (primary + secondary) + Hero image/VSL + Social proof bar
   - Variante sem VSL e com VSL

   **TestimonialsSection:**
   - Título de seção + Grid de TestimonialCards + Navegação (se carousel)
   - Variante: masonry layout, carousel, grid 3 colunas

   **PricingSection:**
   - Título + Toggle mensal/anual (se aplicável) + Grid de PricingCards + FAQ inline de preço + Garantia

   **FAQSection:**
   - Título + Accordion de perguntas/respostas
   - Cada item: Question + Answer (expandível) + animação smooth

   **CTASection:**
   - Fundo de cor contrastante + Headline + Subheadline + Form ou botão + Microcopy de garantia

4. **Documentação de uso** — Para cada componente: quando usar, quando não usar, exemplos de código JSX básico, props API.

## Veto Conditions
- Componente sem variante de dark mode → adicionar antes de fechar
- Componente sem estado de loading ou disabled → adicionar estados faltantes
- Button primary sem contraste 7:1 → ajustar cor
- Componente sem especificação de acessibilidade (aria, foco) → adicionar

## Output Esperado
Arquivo `component-library.md` contendo:
- Especificação completa de cada átomo com variantes, estados e API de props
- Especificação de cada molécula com composição e variantes
- Especificação de cada organismo com composição completa
- Guia de uso de cada componente
- Dependências entre componentes mapeadas

## Completion Criteria
- [ ] Mínimo 6 átomos especificados com todos os estados e variantes
- [ ] Mínimo 6 moléculas especificadas com composição
- [ ] Mínimo 5 organismos especificados com composição
- [ ] Dark mode especificado para todos os componentes
- [ ] Estados de acessibilidade (foco, aria) especificados
- [ ] CRO: CTA com shadow-glow e animação de hover especificados
- [ ] Arquivo `component-library.md` criado e disponível para ce-frontend-dev
