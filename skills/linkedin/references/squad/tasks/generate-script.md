---
task: generateScript()
responsavel: "Cena"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: tema
    tipo: string
    obrigatorio: true
  - nome: formato
    tipo: string
    obrigatorio: true
  - nome: duracao_alvo
    tipo: string
    obrigatorio: false
  - nome: material_apoio
    tipo: string
    obrigatorio: false
  - nome: objetivo
    tipo: string
    obrigatorio: false
  - nome: restricoes
    tipo: string
    obrigatorio: false
Saida:
  - nome: roteiro_completo
    tipo: string
    obrigatorio: true
  - nome: titulo_opcoes
    tipo: string
    obrigatorio: true
  - nome: descricao_e_checklist
    tipo: string
    obrigatorio: true
Checklist:
  - "[ ] Roteiro dual-track (visual + áudio) com timestamps"
  - "[ ] Hook em 10s e pattern interrupts a cada 60-90s"
  - "[ ] 3-5 opções de título e checklist de gravação"
---


# Task: Generate Video Script

```yaml
task:
  name: generate-script
  description: "Gera roteiro completo de vídeo para YouTube ou Shorts/Reels"
  agent: scriptwriter
  elicit: true

inputs:
  required:
    - tema: "Assunto principal do vídeo"
    - formato: "long (5-15min) | shorts (15-60s)"
  optional:
    - duracao_alvo: "Duração desejada em minutos"
    - material_apoio: "GDD, docs, referências para o conteúdo"
    - objetivo: "Educacional | Showcase | Review | Storytelling | Challenge"
    - cta_desejado: "Ação que quer que o viewer tome"
    - restricoes: "Regras do concurso, requisitos técnicos, etc."

outputs:
  - roteiro_completo: "Roteiro dual-track (visual + áudio) com timestamps"
  - titulo_opcoes: "3-5 opções de título otimizado"
  - thumbnail_conceitos: "2-3 conceitos de thumbnail"
  - descricao: "Descrição do vídeo com timestamps e CTAs"
  - checklist_gravacao: "Lista do que preparar antes de gravar"
```

## Workflow

### Fase 1: Elicitation (elicit=true)

Perguntar ao usuário:

1. **Tema:** Sobre o que é o vídeo?
2. **Formato:** Long-form ou Shorts?
3. **Público:** Quem vai assistir? (técnico, iniciante, misto)
4. **Material:** Tem documentos/referências pra eu usar como base?
5. **Objetivo:** O que o viewer deve fazer/sentir depois de assistir?
6. **Restrições:** Tem regras (concurso, duração mínima, hashtags obrigatórias)?

### Fase 2: Outline

Gerar escaleta com:
- Blocos de ~90s com subtemas
- Timestamps estimados
- Tipo de cada bloco (facecam, screencast, b-roll, hybrid)
- Pattern interrupts planejados

**Apresentar outline e pedir aprovação antes de escrever o roteiro completo.**

### Fase 3: Script

Para cada bloco, escrever:
- 🎥 **VISUAL:** O que aparece na tela (específico, não genérico)
- 🎙️ **ÁUDIO:** O que o Sid fala (na voz dele, não formal)
- 💡 **NOTA:** Instruções de edição (zoom, corte, texto na tela, efeito sonoro)

### Fase 4: Metadata

Gerar:
- 3-5 opções de título (< 60 chars)
- 2-3 conceitos de thumbnail
- Descrição otimizada com timestamps
- Checklist de gravação (o que abrir no PC, mic, câmera, etc.)

## Regras de Geração

1. **Sempre dual-track** — nunca escrever ÁUDIO sem VISUAL correspondente
2. **Hook em 10s** — o roteiro começa com impacto, não com "Fala pessoal"
3. **Tom do Sid** — casual, direto, técnico sem ser chato (ref: writing-style.md)
4. **Pattern interrupts** — marcar a cada 60-90s
5. **CTA contextual** — conectado à história, nunca genérico
6. **Tempo realista** — 150 palavras ≈ 1 minuto de narração
7. **Mostrar > Falar** — se pode mostrar na tela, não descreva verbalmente

---

*Task Version: 1.0*
*Created: 2026-03-16*
