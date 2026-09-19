---
task: generateSectionImages()
agent: ce-image-creator
description: "Gerar imagens de suporte para cada seção relevante"
elicit: false
responsavel: "Flash"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: sectionDesigns
    tipo: file
    obrigatorio: true
    descricao: "Design de cada seção que requer imagem"

Saida:
  - nome: sectionImages
    tipo: file
    obrigatorio: true
    descricao: "Imagens geradas para cada seção relevante"

Checklist:
  pre-conditions:
    - "[ ] Designs das seções disponíveis"
  post-conditions:
    - "[ ] Imagem gerada por seção que necessita"
    - "[ ] Consistência visual entre imagens"
    - "[ ] Arquivos otimizados"
---

# Task: generateSectionImages()

## Objetivo
Produzir todas as imagens de suporte necessárias para as seções da landing page que requerem elementos visuais além do hero. Cada imagem deve reforçar a mensagem da seção, manter coesão visual com o hero e otimizar para performance.

## Inputs Necessários
- `sections-design-spec.md` (lista de seções com imagens necessárias e dimensões)
- `hero-image-prompts.md` (style guide de prompts — para manter coesão visual)
- `design-system-decision.md` (paleta, estilo visual)
- `product-brief.md` (produto, contexto)
- `scope.md` (seções ativas)

## Processo
1. **Inventário de imagens necessárias** — Varrer `sections-design-spec.md` e listar:
   - Seção → Tipo de imagem → Dimensões → Propósito → Prioridade
   Categorizar por tipo:
   - **Imagens de processo/features:** Screenshots do produto, diagramas de fluxo, mockups
   - **Imagens de resultado:** Before/after, gráficos de crescimento, dashboards com dados
   - **Imagens de pessoas/contexto:** Pessoas usando o produto, situações de uso
   - **Ilustrações:** Ícones grandes, elementos decorativos, diagramas
   - **Mockups de device:** Laptop, mobile, tablet com o produto em tela

2. **Geração por categoria:**

   **Screenshots e mockups de produto:**
   - Se produto digital: capturar screenshots reais ou solicitar ao cliente
   - Inserir em mockup de device (usar ferramenta como Smartmockups ou gerar via prompt)
   - Prompt base: "Clean [device] mockup with [product screenshot], floating on white background, soft shadow, angle [frontal/slight tilt], [device color], ultra-realistic"

   **Imagens de processo/steps:**
   - Para seções "Como funciona" com 3-4 steps
   - Estilo consistente (ícone vetorial flat vs fotorrealista vs 3D)
   - Gerar ícones ou ilustrações que representam cada step
   - Prompt base: "Minimal flat vector icon, [ação do step], [cor primária] accent, clean white background, no outline, geometric style"

   **Imagens de pessoas em contexto:**
   - Manter consistência demográfica com hero (mesma persona)
   - Variar contexto e emoção por seção (aprendendo, celebrando resultado, trabalhando)
   - Prompt base: Adaptar do hero mantendo "[mesmo estilo visual, paleta e qualidade]"

   **Imagens de resultado/prova:**
   - Gráficos de crescimento (se produto gera resultados mensuráveis)
   - Antes/depois visual
   - Prompt base: "Clean data visualization, upward trend chart, [cor primária], minimal design, no labels visible, success metric visualization"

3. **Manutenção de coesão visual** — Para garantir que todas as imagens pareçam de uma mesma campanha:
   - Usar o mesmo estilo de iluminação do hero
   - Manter paleta de cores consistente
   - Mesmo nível de saturação e temperatura de cor
   - Mesmo estilo fotográfico ou ilustrativo
   Adicionar sufixo ao final de todos os prompts: "[mesmo estilo visual do hero, coeso com paleta {cor primária} e {cor secundária}]"

4. **Otimização para performance** — Para cada imagem:
   - Gerar na maior qualidade e redimensionar para o tamanho exato da spec
   - Exportar em WebP (qualidade 80-85%) + JPEG fallback
   - Verificar que nenhuma imagem supera 200KB sem necessidade
   - Gerar versão @2x para displays retina quando necessário

5. **Nomenclatura e organização** — Seguir convenção:
   - `section-[nome-da-secao]-[tipo]-[variante].webp`
   - Exemplos: `section-how-it-works-step-1.webp`, `section-benefits-laptop-mockup.webp`

## Veto Conditions
- Imagem sem coesão visual com o hero (estilo completamente diferente) → regerar com ajuste de prompt
- Imagem com texto embutido que conflita com o copy da LP → remover texto ou regerar
- Imagem acima de 200KB para suporte de seção → comprimir ou redimensionar
- Mockup de produto sem screenshot real do produto → solicitar ao cliente ou criar mockup simplificado

## Output Esperado
- Todos os arquivos de imagem em WebP e JPEG, organizados em `/public/images/sections/`
- Arquivo `section-images-manifest.md` com: nome do arquivo, seção correspondente, dimensões, alt text, tamanho em KB
- Prompts usados documentados para referência

## Completion Criteria
- [ ] Inventário de imagens necessárias criado
- [ ] 100% das imagens listadas no inventário geradas
- [ ] Coesão visual verificada entre hero e imagens de seção
- [ ] Exportação WebP + JPEG para cada imagem
- [ ] Nenhuma imagem de seção acima de 200KB
- [ ] Alt texts descritivos escritos para todas as imagens
- [ ] Nomenclatura consistente aplicada
- [ ] Arquivo manifest criado com inventário completo
