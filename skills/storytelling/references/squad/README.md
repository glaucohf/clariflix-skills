# Storytelling Squad

**Version:** 1.0.0
**Author:** AIOX Team
**Icon:** 📖

---

## Overview

Time de mestres em storytelling organizados por Tiers para criar narrativas poderosas. Cada agente é baseado em uma mente de referência mundial com frameworks documentados.

## Quick Start

```bash
# Ativar o coordenador
@story

# Inicializar contexto ativo
node squads/storytelling/scripts/set-active-context.cjs --business=aiox --product=cohort_advanced --narrative-type=brand_story

# Gerar greeting contextual
node squads/storytelling/scripts/generate-story-greeting.cjs

# Inspecionar preload
node squads/storytelling/scripts/show-context.cjs

# Comandos disponíveis
*help              # Ver todos comandos
*apply-heros-journey # Aplicar Jornada do Herói
*create-brandscript  # Framework StoryBrand (SB7)
*apply-story-circle  # Story Circle de Dan Harmon
```

## Agents (12)

### Tier 0 - Foundational (Framework Creators)

| Agent | Mind | Framework |
|-------|------|-----------|
| `@joseph-campbell` | Joseph Campbell | Hero's Journey, Monomyth |
| `@shawn-coyne` | Shawn Coyne | Story Grid, Genre Analysis |

### Tier 1 - Masters (Proven Methodologies)

| Agent | Mind | Framework |
|-------|------|-----------|
| `@donald-miller` | Donald Miller | StoryBrand (SB7) |
| `@nancy-duarte` | Nancy Duarte | Resonate, Sparkline |
| `@dan-harmon` | Dan Harmon | Story Circle (8 beats) |
| `@blake-snyder` | Blake Snyder | Save the Cat (15 beats) |

### Tier 2 - Specialists

| Agent | Mind | Framework |
|-------|------|-----------|
| `@oren-klaff` | Oren Klaff | Pitch Anything (STRONG) |
| `@kindra-hall` | Kindra Hall | Stories That Stick |
| `@matthew-dicks` | Matthew Dicks | Storyworthy |
| `@marshall-ganz` | Marshall Ganz | Story of Self, Us, Now |
| `@park-howell` | Park Howell | Business of Story (ABT) |
| `@keith-johnstone` | Keith Johnstone | Impro, Status Theory |

## Use Cases

### For Marketing & Sales
```
@donald-miller
"Crie uma narrativa StoryBrand para [produto]"

@oren-klaff
"Estruture um pitch para investidores sobre [startup]"
```

### For Presentations
```
@nancy-duarte
"Transforme esta apresentação em uma narrativa com Sparkline"

@marshall-ganz
"Crie uma narrativa de liderança usando Story of Self, Us, Now"
```

### For Content & Scripts
```
@dan-harmon
"Estruture este episódio usando Story Circle"

@blake-snyder
"Analise este roteiro usando Save the Cat beats"
```

### For Personal Stories
```
@matthew-dicks
"Ajude-me a encontrar a história dentro desta experiência"

@kindra-hall
"Transforme este case em uma história que gruda"
```

## Framework Quick Reference

| Framework | Creator | Best For |
|-----------|---------|----------|
| **Hero's Journey** | Campbell | Transformação pessoal, branding |
| **Story Grid** | Coyne | Análise de gênero, estrutura |
| **StoryBrand (SB7)** | Miller | Marketing, websites, messaging |
| **Sparkline** | Duarte | Apresentações, keynotes |
| **Story Circle** | Harmon | TV, séries, conteúdo episódico |
| **Save the Cat** | Snyder | Filmes, roteiros longos |
| **STRONG/Pitch** | Klaff | Pitch, vendas, persuasão |
| **Stories That Stick** | Hall | Business storytelling |
| **Storyworthy** | Dicks | Histórias pessoais, moth-style |
| **Self-Us-Now** | Ganz | Liderança, movimentos |
| **ABT** | Howell | Brand storytelling |
| **Impro** | Johnstone | Improviso, status, espontaneidade |

## Integration

- **Related Squads:**
  - `copy` - Para narrativas de vendas e copywriting
  - `mmos` - Para clonar mentes de storytellers adicionais

## Workspace Integration

`storytelling` opera como `controlled_runtime_consumer`.

- owner do readiness: `COO`
- resolver canônico: `squads/c-level/scripts/resolve-squad-workspace-readiness.cjs`
- contexto ativo da sessão: `.aiox/squad-runtime/storytelling/story-chief/session-context.yaml`
- preload mínimo:
  - `workspace/businesses/{business}/company/icp.yaml`
  - `workspace/businesses/{business}/company/brand.yaml`
  - `workspace/businesses/{business}/brand/strategic-positioning.yaml`
  - `workspace/businesses/{business}/products/{product}/offerbook.yaml`
  - `workspace/businesses/{business}/products/{product}/proof.yaml`
  - fonte de pricing canônica do produto
- artefatos narrativos compartilhados:
  - templates em `workspace/_templates/product-narrative/`
  - instâncias product-specific em `workspace/businesses/{business}/products/{product}/narrative/`
  - instâncias company-wide em `workspace/businesses/{business}/company/`

## Structure

```
storytelling/
├── agents/          # 12 storytelling masters
├── tasks/           # Story creation workflows
├── research/        # Mind research outputs
├── logs/            # Session logs
├── checklists/      # Story validation
├── templates/       # Story templates
├── workflows/       # Multi-phase workflows
└── config.yaml      # Squad configuration
```

---

_Version: 1.0.0_
_Compatible with: AIOX-FULLSTACK v4+_
