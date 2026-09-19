---
task: selectDesignSystem()
agent: ce-design-architect
description: "Selecionar design system base (Shadcn, Radix, custom) + paleta de cores com contraste WCAG AAA"
elicit: true
responsavel: "Canvas"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing do produto com identidade visual existente"

Saida:
  - nome: designSystemChoice
    tipo: file
    obrigatorio: true
    descricao: "Design system selecionado com paleta WCAG AAA e tipografia definida"

Checklist:
  pre-conditions:
    - "[ ] Product brief com referências visuais disponível"
  post-conditions:
    - "[ ] Design system base selecionado"
    - "[ ] Contraste WCAG AAA validado (7:1)"
    - "[ ] Light e dark mode planejados"
---

# Task: selectDesignSystem()

## Objetivo
Tomar decisões fundamentais de design que irão definir a identidade visual da landing page: o design system base, a paleta de cores, a tipografia e o estilo visual geral. Estas decisões devem equilibrar velocidade de implementação, consistência visual, acessibilidade e alinhamento com o posicionamento do produto.

## Inputs Necessários
- `product-brief.md` (posicionamento, nicho, público-alvo)
- `intelligence-brief.md` (estilo visual predominante no nicho, perfil de dispositivos)
- `competitive-analysis.md` (design systems usados pelos concorrentes)
- `scope.md` (dark/light mode obrigatório, flag de componentes necessários)
- Brand guidelines do cliente (se existir: logo, cores, fontes)
- Referências visuais do cliente (sites que admira, mood board)

## Processo
1. **Análise de requisitos visuais** — Coletar e documentar:
   - Cores da marca existentes (hex codes) ou "sem preferência"
   - Fontes existentes ou "sem preferência"
   - Estilo visual desejado (minimalista, bold/impactante, tecnológico, orgânico/natural, premium/luxury, acessível/popular)
   - Exemplos de sites que o cliente admira (coletar 3-5 referências)
   - Dark mode obrigatório? Light mode como padrão?

2. **Seleção do design system** — Avaliar opções com base nos critérios:

   | Critério | Shadcn/UI | Radix Primitives | Tailwind + Custom | MUI/Ant Design |
   |---------|-----------|-----------------|-------------------|----------------|
   | Velocidade | Alta | Média | Baixa-Média | Alta |
   | Customização | Alta | Total | Total | Média |
   | Acessibilidade | Muito Alta | Muito Alta | Depende do dev | Alta |
   | Dark Mode | Nativo | Manual | Manual | Nativo |
   | Bundle size | Leve | Muito Leve | Leve | Pesado |
   | Ideal para LP | Sim | Sim (projetos maiores) | Sim (LP simples) | Não recomendado |

   **Recomendação padrão:** Shadcn/UI (Radix + Tailwind) para o equilíbrio ideal de velocidade + acessibilidade + customização.
   **Quando escolher custom:** Cliente tem brand guidelines muito específicas que conflitam com design systems pré-construídos.

3. **Definição da paleta de cores** — Construir paleta com critérios WCAG AAA:
   - **Cor primária:** Tom dominante da marca → gera variações (50 ao 950 em Tailwind scale)
   - **Cor de ação/CTA:** A cor do botão principal (deve ter contraste mínimo 7:1 com texto — WCAG AAA)
   - **Cor de fundo:** Fundo principal da LP (light mode e dark mode)
   - **Cor de superfície:** Cards, sidebars, elementos elevados
   - **Cor de texto:** Primário, secundário, muted (3 níveis de hierarquia)
   - **Cor de acento:** Para highlights, badges, tags
   - **Cor semântica:** Sucesso (verde), alerta (amarelo), erro (vermelho), info (azul)

   Verificar contraste via WebAIM Contrast Checker para CADA combinação texto/fundo:
   - Texto normal: contraste mínimo 7:1 (WCAG AAA)
   - Texto grande (18px+): contraste mínimo 4.5:1 (WCAG AA)
   - Botão CTA: contraste mínimo 7:1

4. **Seleção de tipografia** — Definir stack tipográfico:
   - **Fonte display/headline:** Para títulos grandes. Critérios: legibilidade em tamanhos grandes, personalidade alinhada ao posicionamento, disponível no Google Fonts (performance) ou licença adequada.
   - **Fonte body:** Para texto corrido. Critérios: alta legibilidade em tamanhos pequenos, serif ou sans-serif adequado ao nicho, x-height adequado para mobile.
   - **Fonte mono (se necessário):** Para código, preços, destaque de números.
   Definir escala tipográfica: xs (12px), sm (14px), base (16px), lg (18px), xl (20px), 2xl (24px), 3xl (30px), 4xl (36px), 5xl (48px), 6xl (60px).

5. **Definição de estilo visual** — Determinar:
   - Radius: Sharp (0px), Subtle (4px), Rounded (8px), Very Rounded (16px), Full (9999px)
   - Shadow style: Flat (sem shadow), Subtle (shadow-sm), Pronounced (shadow-lg), Glow effects
   - Density: Compact, Comfortable, Spacious
   - Imagery style: Fotografia realista, ilustração vetorial, 3D rendering, misto

## Veto Conditions
- Paleta com combinação de texto/fundo abaixo de 7:1 de contraste para texto normal → ajustar até atingir WCAG AAA
- Fonte com licença não-comercial selecionada sem aviso → verificar licença antes de confirmar
- Design system incompatível com Next.js 14+ → rever seleção
- Cor de CTA igual ou muito próxima ao background → garantir que CTA se destaca

## Output Esperado
Arquivo `design-system-decision.md` contendo:
- Design system selecionado com justificativa
- Paleta de cores completa (hex codes) com scores de contraste verificados
- Stack tipográfico com fontes escolhidas e escala
- Estilo visual (radius, shadows, density, imagery)
- Configuração inicial do `tailwind.config.ts` com tokens
- Dark mode: paleta equivalente para dark
- Referências visuais aprovadas

## Completion Criteria
- [ ] Design system selecionado e justificado
- [ ] Paleta de cores definida com TODOS os pares texto/fundo verificados para WCAG AAA
- [ ] Cor de CTA com contraste 7:1 verificado
- [ ] Stack tipográfico definido (display + body) com licenças verificadas
- [ ] Escala tipográfica completa definida
- [ ] Estilo visual (radius, shadows, density) definido
- [ ] Dark mode paleta definida
- [ ] `tailwind.config.ts` base configurado com tokens
- [ ] Arquivo `design-system-decision.md` criado
