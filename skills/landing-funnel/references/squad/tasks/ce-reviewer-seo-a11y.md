---
task: reviewSeoAccessibility()
agent: ce-reviewer
description: "Revisar SEO (meta tags, JSON-LD, canonical, sitemap) e acessibilidade WCAG AAA (contraste 7:1, ARIA, keyboard nav). Score: 0-100"
elicit: false
responsavel: "Audit"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: assembledPage
    tipo: file
    obrigatorio: true
    descricao: "Página completa montada"

Saida:
  - nome: seoA11yScore
    tipo: file
    obrigatorio: true
    descricao: "Score SEO/A11y 0-100: meta tags, JSON-LD, canonical, WCAG AAA, ARIA e keyboard navigation"

Checklist:
  pre-conditions:
    - "[ ] Página montada e acessível"
  post-conditions:
    - "[ ] Score calculado"
    - "[ ] Meta tags validadas"
    - "[ ] Contraste WCAG AAA confirmado (7:1)"
---

# Task: reviewSeoAccessibility()

## Objetivo
Auditar SEO técnico e acessibilidade da landing page contra padrões WCAG AAA. SEO garante que a LP possa ser encontrada organicamente e compartilhada corretamente. Acessibilidade garante que nenhum usuário seja excluído e protege contra riscos legais crescentes.

## Inputs Necessários
- Landing page em URL de preview acessível
- `assemblePage()` output — metadata e JSON-LD implementados
- Chrome DevTools, Lighthouse, axe DevTools (extensão)
- Google Rich Results Test (para JSON-LD)
- OpenGraph.xyz (para OG tags)

## Processo
1. **Rubrica de avaliação (100 pontos):**

   **SEO Técnico (50 pontos):**

   **Meta tags (20 pontos):**
   - `<title>` presente, 30-60 chars, palavra-chave principal → 0-8 pts
   - `<meta description>` presente, 120-160 chars, com CTA implícito → 0-7 pts
   - `<meta robots>` correto (index, follow) → 0-2 pts
   - `<link rel="canonical">` apontando para URL correta → 0-3 pts

   **Open Graph / Social (15 pontos):**
   - `og:title`, `og:description`, `og:image`, `og:url`, `og:type` presentes → 0-8 pts
   - Imagem OG com dimensão 1200×630px → 0-3 pts
   - `og:image:alt` presente → 0-2 pts
   - Twitter Card configurado → 0-2 pts

   **JSON-LD Structured Data (10 pontos):**
   - JSON-LD presente e válido (sem erros no Google Rich Results Test) → 0-6 pts
   - Schema type adequado ao produto (WebPage, Product, FAQPage, etc.) → 0-4 pts

   **Sitemap e Robots (5 pontos):**
   - `/sitemap.xml` acessível e válido → 0-3 pts
   - `/robots.txt` correto (não bloqueando indexação) → 0-2 pts

   **Acessibilidade WCAG AAA (50 pontos):**

   **Contraste (15 pontos):**
   - Texto normal: contraste ≥ 7:1 (AAA) — verificar via DevTools Accessibility → 0-8 pts
   - Texto grande (18px+): contraste ≥ 4.5:1 (AA) → 0-4 pts
   - Componentes de UI (botões, inputs): contraste ≥ 4.5:1 → 0-3 pts

   **Estrutura semântica (15 pontos):**
   - Apenas 1 `<h1>` por página → 0-3 pts
   - Hierarquia de headings correta (h1→h2→h3, sem pular níveis) → 0-4 pts
   - Landmarks ARIA corretos (`<main>`, `<nav>`, `<header>`, `<footer>`) → 0-4 pts
   - `<article>`, `<section>` com labels quando necessário → 0-4 pts

   **Navegação por teclado (10 pontos):**
   - Skip link "Pular para o conteúdo" funcionando → 0-3 pts
   - Todos os elementos interativos acessíveis por Tab → 0-4 pts
   - Focus ring visível em todos os elementos focáveis → 0-3 pts

   **Imagens e media (10 pontos):**
   - Todas as imagens informativas com `alt` descritivo → 0-5 pts
   - Imagens decorativas com `alt=""` → 0-3 pts
   - Vídeos com closed captions ou transcrição (se VSL) → 0-2 pts

2. **Verificação com ferramentas:**

   **Lighthouse Accessibility:**
   ```
   Chrome DevTools → Lighthouse → Accessibility → Run audit
   Score ≥ 90 esperado
   ```

   **axe DevTools:**
   ```
   Instalar extensão axe DevTools
   Executar "Analyze" na página
   Verificar: zero "Critical" e zero "Serious" violations
   ```

   **Verificação manual de contraste:**
   ```
   Chrome DevTools → Elements → Computed → Accessibility
   → Color Contrast ratio
   Para cada cor de texto sobre fundo relevante
   ```

   **Google Rich Results Test:**
   ```
   Acessar: search.google.com/test/rich-results
   Inserir URL da LP
   Verificar: JSON-LD válido sem erros
   ```

   **Facebook Sharing Debugger:**
   ```
   Acessar: developers.facebook.com/tools/debug
   Scrape URL para verificar OG tags
   ```

3. **Verificações manuais de teclado:**
   - Abrir a LP sem mouse
   - Pressionar Tab repetidamente verificando que foco se move em ordem lógica
   - Pressionar Enter/Space nos botões e links — devem funcionar
   - Verificar que modal/dropdown fecha com Escape
   - Verificar que não há "armadilhas de foco" (foco preso em elemento)

4. **Verificação de atributos ARIA:**
   - Botões sem texto visível têm `aria-label`?
   - Ícones decorativos têm `aria-hidden="true"`?
   - Formulários têm `<label>` associado a cada input?
   - Elementos de status/alert têm `role="alert"` e `aria-live`?
   - Imagens de links têm `alt` descritivo (não o URL)?

## Veto Conditions
- JSON-LD com erro de validação → BLOQUEANTE — corrigir antes de lançar (afeta indexação)
- Canonical apontando para URL errada → BLOQUEANTE — página pode ser desindexada
- Axe retornando violação "Critical" → BLOQUEANTE — risco legal e de exclusão de usuários
- Nenhum `<h1>` na página → BLOQUEANTE — crítico para SEO
- Score Lighthouse Accessibility < 70 → retornar ao frontend com lista de correções

## Output Esperado
Arquivo `review-seo-a11y.md` contendo:
- Score por critério (meta tags, OG, JSON-LD, contraste, semântica, teclado, imagens)
- Resultado de cada ferramenta (Lighthouse, axe, Rich Results Test)
- Lista de violações por nível (bloqueante / significativo / menor)
- Score total (0-100)
- Veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO

## Completion Criteria
- [ ] Todas as meta tags verificadas (title, description, robots, canonical)
- [ ] Open Graph e Twitter Card verificados (via Facebook Debugger)
- [ ] JSON-LD válido (via Google Rich Results Test, zero erros)
- [ ] Sitemap acessível e válido
- [ ] Contraste verificado para todos os textos principais
- [ ] Lighthouse Accessibility score calculado
- [ ] axe DevTools: zero Critical e Serious violations
- [ ] Navegação por teclado testada manualmente
- [ ] Atributos ARIA verificados
- [ ] Score total calculado (0-100)
- [ ] Veredicto emitido
- [ ] Arquivo `review-seo-a11y.md` criado
