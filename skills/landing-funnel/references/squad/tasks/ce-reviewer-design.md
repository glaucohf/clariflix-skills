---
task: reviewDesignConsistency()
agent: ce-reviewer
description: "Revisar design: consistência de tokens, responsividade, dark/light mode, hierarquia visual, CRO principles. Score: 0-100"
elicit: false
responsavel: "Audit"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: implementedDesign
    tipo: file
    obrigatorio: true
    descricao: "Design implementado no frontend"

Saida:
  - nome: designReviewScore
    tipo: file
    obrigatorio: true
    descricao: "Score de design 0-100: consistência de tokens, responsividade, dark/light e hierarquia visual"

Checklist:
  pre-conditions:
    - "[ ] Página implementada"
  post-conditions:
    - "[ ] Score calculado"
    - "[ ] Inconsistências de design listadas"
    - "[ ] Mobile review realizado"
---

# Task: reviewDesignConsistency()

## Objetivo
Auditar a consistência visual e técnica do design implementado, verificando se o design system foi aplicado corretamente, a responsividade está perfeita em todos os breakpoints e os princípios de CRO foram preservados na implementação. Score 0-100.

## Inputs Necessários
- Landing page rodando em ambiente de preview (não produção)
- `design-system-decision.md` e `design-tokens.md` (referência de design)
- `cro-design-audit.md` (princípios de CRO aprovados)
- `sections-design-spec.md` (especificações de cada seção)
- `component-library.md` (componentes e variantes)
- Acesso a Chrome DevTools para inspeção

## Processo
1. **Verificação de consistência de tokens** — Inspecionar no DevTools:
   - Todas as cores usadas são variáveis CSS (tokens)? `var(--primary)` vs `#1e40af` hardcoded?
   - Todos os espaçamentos seguem a escala de 4px? (8px, 16px, 24px, 32px...)
   - Fontes usam a escala tipográfica definida?
   - Border-radius consistente (não misturando `rounded-md` e `rounded-xl` aleatoriamente)?
   - Shadows consistentes com o nível de elevação correto?

2. **Rubrica de avaliação de design (100 pontos):**

   **Consistência de tokens (25 pontos):**
   - 0-10: Muitas cores/espaçamentos hardcoded, tokens ignorados
   - 11-18: Maioria usa tokens, algumas exceções não justificadas
   - 19-22: Uso consistente de tokens com raras exceções justificadas
   - 23-25: 100% de tokens — zero valores hardcoded não justificados

   **Responsividade (25 pontos):**
   - Testar em 320px, 375px, 768px, 1024px, 1280px, 1536px
   - 0-10: Quebras de layout em mobile ou desktop
   - 11-17: Funcional mas não otimizado em algum breakpoint
   - 18-22: Boa responsividade com pequenos ajustes necessários
   - 23-25: Perfeito em todos os breakpoints — mobile-first impecável

   **Dark/Light mode (15 pontos):**
   - 0-5: Dark mode quebrado (cores incorretas, texto ilegível)
   - 6-9: Dark mode funcional mas com inconsistências
   - 10-12: Dark mode bom com pequenos ajustes
   - 13-15: Dark mode perfeito — cada elemento correto em ambos os modos

   **Hierarquia visual (20 pontos):**
   - 0-10: Hierarquia confusa — olho não sabe para onde ir
   - 11-14: Hierarquia existe mas não guia para o CTA
   - 15-17: Boa hierarquia com desvios pontuais
   - 18-20: Hierarquia impecável — olho conduzido naturalmente do headline ao CTA

   **Princípios CRO no design implementado (15 pontos):**
   - CTA acima da dobra em mobile (375px)? (+5)
   - CTA com contraste adequado e shadow-glow no hover? (+3)
   - Whitespace suficiente ao redor dos CTAs? (+3)
   - Imagens direcionando olhar para o texto/CTA? (+2)
   - Friction visual eliminada (sem nav links de escape)? (+2)

3. **Checklist específica por breakpoint:**

   **320px (iPhone SE):**
   - [ ] CTA visível sem scroll
   - [ ] Texto legível sem zoom (≥ 14px)
   - [ ] Nenhum overflow horizontal
   - [ ] Inputs acessíveis com teclado mobile

   **375px (iPhone padrão):**
   - [ ] Hero completa no viewport inicial
   - [ ] Botões com área de toque ≥ 44×44px
   - [ ] Grid colapsado para 1 coluna

   **768px (Tablet):**
   - [ ] Layout intermediário correto (não mobile nem desktop)
   - [ ] Grid de 2 colunas onde aplicável

   **1280px (Desktop padrão):**
   - [ ] Layout de 2 colunas no hero
   - [ ] Grid de 3 colunas em testimonials
   - [ ] Container com max-width respeitado

4. **Verificação de animações:**
   - Animações de entrada disparando corretamente ao scroll?
   - Animações respeitando `prefers-reduced-motion`?
   - Nenhuma animação "travando" (janking) — testar em CPU throttled (DevTools)?

5. **Verificação de acessibilidade visual:**
   - Contraste de texto verificado via DevTools Accessibility panel
   - Focus rings visíveis em todos os elementos interativos ao navegar por teclado
   - Nenhum elemento interativo apenas por cor (sem outro indicador visual)

## Veto Conditions
- CTA não visível acima da dobra em 375px → BLOQUEANTE — não lançar
- Overflow horizontal em qualquer breakpoint → BLOQUEANTE — não lançar
- Dark mode com texto ilegível → BLOQUEANTE — não lançar
- Score < 75 → retornar ao ce-frontend-dev com lista de correções

## Output Esperado
Arquivo `review-design.md` contendo:
- Score por critério (tokens, responsividade, dark mode, hierarquia, CRO)
- Checklist de breakpoints com resultado
- Problemas encontrados por nível de prioridade (bloqueante / significativo / estético)
- Screenshots ou descrições de problemas visuais
- Score total (0-100)
- Veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO

## Completion Criteria
- [ ] Tokens verificados via DevTools (zero hardcoded justificados)
- [ ] 6 breakpoints testados (320 / 375 / 768 / 1024 / 1280 / 1536)
- [ ] Dark mode verificado em todos os breakpoints
- [ ] Hierarquia visual avaliada (olho guiado ao CTA)
- [ ] 5 princípios CRO verificados no design implementado
- [ ] Animações testadas com reduced-motion
- [ ] Acessibilidade visual verificada (contraste + foco)
- [ ] Score calculado (0-100) com justificativa por critério
- [ ] Veredicto emitido
- [ ] Arquivo `review-design.md` criado
