---
task: generateCarousel()
responsavel: "Slide"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: topic
    tipo: string
    obrigatorio: true
  - nome: type
    tipo: string
    obrigatorio: true
  - nome: slides
    tipo: integer
    obrigatorio: false
  - nome: context
    tipo: string
    obrigatorio: false
Saida:
  - nome: slides_content
    tipo: string
    obrigatorio: true
  - nome: visual_structure
    tipo: string
    obrigatorio: true
  - nome: companion_post
    tipo: string
    obrigatorio: true
Checklist:
  - "[ ] Cada slide tem exatamente 1 ideia central"
  - "[ ] Capa atrativa com título claro"
  - "[ ] Post de acompanhamento com hook forte e CTA"
---


# Task: Generate LinkedIn Carousel

**Task ID:** generate-carousel
**Agent:** @carousel-designer
**Priority:** HIGH
**Tools Required:** Read

---

## Objetivo

Gerar conteúdo completo para carrossel LinkedIn — textos de cada slide, estrutura visual sugerida e post de acompanhamento.

---

## Inputs

| Parameter | Description | Example |
|-----------|-------------|---------|
| TOPIC | Tema do carrossel | `5 ferramentas de recon que uso em todo pentest` |
| TYPE | Tipo de carrossel | `tutorial`, `list`, `comparison`, `storytelling` |
| SLIDES | Quantidade de slides | `8-12` (default: 10) |
| CONTEXT | Contexto adicional | Experiência real, dados específicos |

---

## Workflow

### Step 1: Definir Estrutura

Com base no TYPE:

| Tipo | Estrutura |
|------|-----------|
| **Tutorial** | Capa → Problema → Passos (1 por slide) → Resultado → CTA → Autor |
| **List** | Capa → Contexto → Items (1 por slide) → Resumo → CTA → Autor |
| **Comparison** | Capa → Contexto → Antes → Depois → Diferenças → Recomendação → CTA → Autor |
| **Storytelling** | Capa → Setup → Conflito → Desenvolvimento → Resolução → Lição → CTA → Autor |

### Step 2: Escrever Conteúdo por Slide

Para cada slide:
- **Título:** Máximo 6-8 palavras
- **Corpo:** Máximo 3-4 bullets ou 2-3 frases curtas
- **Destaque:** Palavra-chave em **negrito**
- **Visual:** Sugestão de ícone/emoji como marcador

### Step 3: Escrever Post de Acompanhamento

O post que acompanha o carrossel no feed:
- Hook forte (2 linhas)
- Contexto breve do que o carrossel cobre
- CTA para swipe
- Hashtags

### Step 4: Revisão

- [ ] 1 ideia por slide (não sobrecarregado)
- [ ] Flow lógico (cada slide puxa o próximo)
- [ ] Capa com título impactante
- [ ] Último slide tem CTA + info do autor
- [ ] Estilo alinhado com tom do Sid

---

## Output

```markdown
# Carrossel LinkedIn — {{TOPIC}}

**Tipo:** {{TYPE}}
**Slides:** {{COUNT}}
**Pilar:** {{PILLAR}}

---

## Slide 1 — CAPA

**Título:** {{título impactante}}
**Subtítulo:** {{contexto breve}}
**Autor:** F0livora
**Visual:** Fundo escuro, texto cyan/branco

---

## Slide 2 — CONTEXTO

**Título:** {{por que isso importa}}
**Corpo:**
- Ponto 1
- Ponto 2
- Ponto 3

---

## Slide 3-N — CONTEÚDO

**Título:** {{título do slide}}
**Corpo:**
{{conteúdo principal}}

**Destaque:** {{frase-chave em negrito}}

---

## Slide N+1 — RESUMO

**Título:** Recapitulando
**Corpo:**
1. Ponto 1
2. Ponto 2
3. ...

---

## Slide N+2 — CTA

**Título:** Gostou? Tem mais.
**Corpo:**
- 🔒 Siga para mais conteúdo de CyberSec + AI
- 💾 Salve para consultar depois
- 🔄 Compartilhe com quem precisa ver isso

---

## Post de Acompanhamento

{{POST_TEXT}}

{{HASHTAGS}}
```

---

## Success Criteria

- [ ] Cada slide tem exatamente 1 ideia central
- [ ] Flow lógico do primeiro ao último slide
- [ ] Capa atrativa com título claro
- [ ] Conteúdo no estilo do Sid (direto, prático)
- [ ] Post de acompanhamento com hook forte
- [ ] CTA slide com ação clara

---

*Task Version: 1.0*
*Created: 2026-03-11*
