---
task: generateSocialProofAssets()
agent: ce-image-creator
description: "EXCLUSIVO: gerar assets de social proof — fotos de avatares de depoimentos, thumbnails de VSL, trust badges base"
elicit: false
responsavel: "Flash"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: testimonials
    tipo: file
    obrigatorio: false
    descricao: "Dados dos testimonials para gerar avatares"

Saida:
  - nome: socialProofAssets
    tipo: file
    obrigatorio: true
    descricao: "Assets de social proof: avatares fotorrealistas, thumbnails de VSL e trust badges base"

Checklist:
  pre-conditions:
    - "[ ] Dados de testimonials coletados pelo ce-social-proof"
  post-conditions:
    - "[ ] Avatares gerados para cada testimonial"
    - "[ ] Thumbnail de VSL criado"
    - "[ ] Trust badges prontos"
---

# Task: generateSocialProofAssets()

## Objetivo
Produzir os assets visuais que compõem a prova social da landing page: avatares fotorrealistas para depoimentos de clientes, thumbnail otimizada para o VSL e trust badges visuais. Estes assets são críticos para credibilidade — provas sociais com foto real têm 35% mais impacto que sem foto.

## Inputs Necessários
- `social-proof-audit.md` (output do ce-social-proof — lista de depoimentos e clientes)
- `vsl-script.md` (se VSL ativo — para criar thumbnail alinhada com o script)
- `design-system-decision.md` (paleta, estilo visual)
- `audience-profile.md` (persona — os avatares devem representar o público)
- `product-brief.md` (credenciais, parceiros, certificações para trust badges)

## Processo
1. **Avatares de depoimentos** — Gerar fotos de pessoas que representam os clientes reais:

   Para cada depoimento que NÃO tem foto real fornecida pelo cliente:
   - Criar avatar fotorrealista correspondente à persona descrita (nome, cargo, contexto)
   - O avatar deve representar demograficamente o cliente real: gênero, faixa etária, contexto profissional
   - Expressão: natural, sorriso genuíno, confiante (não excessivamente feliz — parece fake)
   - Background: neutro (cor sólida ou levemente desfocado) para não competir com o depoimento
   - Enquadramento: busto/ombros, rosto levemente virado para a câmera

   Prompt base para avatar:
   ```
   Professional headshot photo, [gênero] [faixa etária] [etnia representativa do público],
   natural genuine smile, [característica do contexto profissional], soft neutral background,
   shoulder-up framing, warm natural lighting, authentic non-stock feeling, ultra-realistic,
   high resolution, sharp focus on face.
   Negative: stock photo, fake smile, overly perfect, watermark, illustration.
   ```

   Gerar 2 variações por avatar e selecionar a mais autêntica.

   **IMPORTANTE:** Quando o cliente fornece fotos reais, usar as fotos reais. Os avatares gerados são apenas para casos onde o cliente não tem foto do depoente.

2. **Thumbnail do VSL** — Se flag VSL ativa, criar thumbnail que maximize a taxa de play:

   Elementos de uma thumbnail de alta conversão:
   - **Rosto humano com emoção clara** (surpresa, entusiasmo, curiosidade) — 30-40% da área
   - **Headline de curiosidade** sobreposta (2-5 palavras, tipografia bold, alto contraste)
   - **Ícone de play** claramente visível no centro-baixo
   - **Paleta alinhada** com o design system da LP (consistência visual)
   - **Sem excesso de texto** — a thumbnail deve ser legível em 100×56px (preview mobile)

   Gerar 3 versões com variações de:
   - V1: Rosto do apresentador + headline de dor
   - V2: Resultado visual (gráfico, antes/depois) + headline de curiosidade
   - V3: Rosto + elemento do produto + headline de promessa

   Dimensões: 1280×720px (16:9), exportar em WebP + JPEG

   Texto sobreposto deve ser criado via CSS/design, não embutido na imagem — para facilitar A/B testing do copy da thumbnail.

3. **Trust badges e credibilidade visual** — Gerar ou montar badges que aumentam credibilidade:

   **Tipos de trust badge:**
   - **Garantia:** Ícone de shield + "Garantia de X dias" (circulo com detalhes da garantia)
   - **Número de clientes:** Ícone de pessoas + "X+ clientes satisfeitos"
   - **Certificação/Parceria:** Logo ou ícone relevante ao nicho
   - **Segurança de pagamento:** Ícones de SSL, criptografia, métodos de pagamento
   - **Mídia:** "Como visto em" + logos de veículos de mídia (se houver)
   - **Awards/Recognition:** Selos de prêmios ou reconhecimentos do setor

   Para cada badge:
   - Estilo SVG vetorial (escala sem perda de qualidade)
   - Cores alinhadas com paleta do design system
   - Versão light e dark mode
   - Tamanhos: 80×80px (individual), 160×40px (horizontal/inline)

   **Geração:** Usar prompts para criar ícones base e refinar, ou especificar para o ce-frontend-dev implementar como SVG puro com Lucide + Tailwind.

4. **Barra de logos de clientes/parceiros** — Se há logos disponíveis:
   - Solicitar logos originais do cliente (SVG ou PNG de alta qualidade)
   - Padronizar altura (40px) e espaçamento
   - Versão monocromática (cinza) para parecer mais imparcial e profissional
   - Versão colorida para casos especiais
   - Criar variante grayscale via CSS filter para consistência

5. **Stars rating visual** — Elemento de avaliação:
   - Ícone de 5 estrelas preenchidas (amarelo dourado ou primária)
   - Variante com avaliação parcial (4.8/5.0)
   - SVG puro para máxima performance

## Veto Conditions
- Avatar gerado que parece obviamente AI (olhos estranhos, mãos distorcidas) → regerar até qualidade convincente
- Thumbnail do VSL sem rosto humano visível → adicionar elemento humano
- Trust badges sem versão SVG (apenas raster) → converter ou especificar SVG
- Avatares demograficamente inconsistentes com o público real → corrigir representação

## Output Esperado
- Pasta `/public/images/social-proof/` com:
  - `avatar-[nome].webp` para cada depoimento
  - `vsl-thumbnail-v1.webp`, `vsl-thumbnail-v2.webp`, `vsl-thumbnail-v3.webp`
  - `badge-garantia.svg`, `badge-clientes.svg`, `badge-seguranca.svg` (e outros)
  - `stars-rating.svg`
- Arquivo `social-proof-assets-manifest.md` com inventário completo

## Completion Criteria
- [ ] Avatar gerado para cada depoimento sem foto real do cliente
- [ ] Qualidade de avatar verificada (aparência autêntica, não-AI perceptível)
- [ ] 3 variações de thumbnail VSL geradas (se flag VSL ativa)
- [ ] Trust badges criados em SVG (light + dark mode)
- [ ] Stars rating SVG criado
- [ ] Todos os assets exportados em WebP/SVG com fallbacks
- [ ] Manifest com inventário completo criado
- [ ] Nenhum avatar acima de 50KB (busto, dimensão 96×96px a 2x)
