---
task: generateHeroImage()
agent: ce-image-creator
description: "Gerar imagem hero com prompt engenheirado para o produto/audiência específicos"
elicit: false
responsavel: "Flash"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing do produto com contexto visual"
  - nome: heroCopy
    tipo: string
    obrigatorio: true
    descricao: "Copy do hero para contextualizar a imagem"

Saida:
  - nome: heroImage
    tipo: file
    obrigatorio: true
    descricao: "Imagem hero gerada com 3 variações para teste"

Checklist:
  pre-conditions:
    - "[ ] Copy do hero disponível"
  post-conditions:
    - "[ ] 3 variações geradas"
    - "[ ] Imagem coerente com produto"
    - "[ ] Formato otimizado (WebP)"
---

# Task: generateHeroImage()

## Objetivo
Produzir a imagem hero da landing page — o elemento visual de maior impacto acima da dobra. A imagem hero deve comunicar a transformação do produto em frações de segundo, antes mesmo que o visitante leia qualquer texto.

## Inputs Necessários
- `product-brief.md` (produto, público, transformação prometida)
- `audience-profile.md` (persona primária, desejos visuais)
- `design-system-decision.md` (paleta de cores, estilo visual)
- `sections-design-spec.md` (dimensões da hero image, aspect ratio)
- `intelligence-brief.md` (estilo visual predominante no nicho)

## Processo
1. **Definição do conceito visual** — Responder antes de gerar:
   - O hero deve mostrar: o produto em uso, o resultado/transformação, a persona ideal, ou abstração do benefício?
   - Deve ter pessoa(s)? Se sim: gênero, faixa etária, expressão emocional (alegria/confiança/foco), contexto (escritório/casa/externo)
   - Deve ser fotorrealista, ilustrado, 3D render, ou misto?
   - Paleta de cores deve seguir os tokens definidos — quais cores dominam?
   - Direção do olhar (se houver pessoa): para dentro da tela/para o texto

2. **Engenharia do prompt principal** — Construir prompt com todas as dimensões:

   Estrutura do prompt:
   ```
   [Tipo de imagem] + [Assunto principal] + [Contexto] + [Estilo visual] +
   [Iluminação] + [Composição/enquadramento] + [Paleta de cores] +
   [Emoção/mood] + [Qualidade técnica] + [Negative prompts]
   ```

   Exemplo para produto SaaS de produtividade:
   ```
   Professional product photography, confident Brazilian woman in her 30s
   working on a laptop in a bright modern home office, looking at the screen
   with focused satisfaction, clean minimal aesthetic, soft natural window
   light with subtle warm glow, shallow depth of field, desktop and mobile
   mockup visible on screen, color palette: deep blue #1e40af and white,
   modern corporate lifestyle photography, high resolution 4K, sharp focus,
   no clutter, no stock photo feel, authentic candid moment.
   Negative: watermark, cartoon, illustration, ugly, blurry, distorted,
   oversaturated, stock photo clichés, arms crossed.
   ```

3. **Variações de prompt** — Gerar 3 variações do prompt para testar:
   - V1: Foco na persona (pessoa em destaque)
   - V2: Foco no produto/resultado (produto ou resultado em destaque)
   - V3: Abstrato/Emocional (metáfora visual do benefício)

4. **Geração e seleção** — Gerar imagens com cada variação. Avaliar cada resultado contra critérios:
   - Comunicação da transformação em < 3 segundos?
   - Alinhamento com paleta de cores do design system?
   - Direção do olhar correta (para o texto/CTA)?
   - Qualidade técnica adequada para web (nitidez, sem artefatos)?
   - Ausência de elementos distrativos?

5. **Pós-processamento e otimização** — Após seleção da melhor imagem:
   - Crop para aspect ratio definido na spec (ex: 1:1 mobile, 16:9 desktop, ou 4:3)
   - Ajuste de brilho/contraste se necessário para integrar com o design
   - Exportação em WebP (qualidade 85%) + JPEG fallback
   - Versão mobile: crop específico com sujeito centralizado
   - Verificar que nenhum elemento crítico fica oculto em mobile

6. **Variante com overlay** — Gerar versão com overlay semitransparente da cor primária caso o design requeira texto sobre a imagem.

## Veto Conditions
- Imagem com pessoa olhando para fora da tela (direita) → gerar nova versão
- Imagem com elementos que contradizem a mensagem do produto → descartar
- Qualidade insuficiente para resolução retina (2x) → regerar em qualidade maior
- Imagem com texto embutido (não gerado pelo copy) → remover ou regerar
- Paleta completamente divergente do design system → ajustar ou regerar

## Output Esperado
- `hero-image-desktop.webp` — Dimensão definida na spec, optimizado
- `hero-image-mobile.webp` — Crop mobile específico
- `hero-image-desktop.jpg` — Fallback JPEG
- `hero-image-mobile.jpg` — Fallback JPEG mobile
- `hero-image-alt.txt` — Alt text descritivo para acessibilidade
- Arquivo `hero-image-prompts.md` com prompts usados e razões de seleção

## Completion Criteria
- [ ] 3 variações de prompt geradas e testadas
- [ ] Imagem selecionada com justificativa documentada
- [ ] Direção do olhar verificada (para dentro/para o texto)
- [ ] Alinhamento de paleta de cores verificado
- [ ] Versão desktop e mobile geradas com crops corretos
- [ ] Exportação WebP + JPEG em ambas as resoluções
- [ ] Alt text descritivo escrito
- [ ] Arquivo de prompts documentado para referência futura
