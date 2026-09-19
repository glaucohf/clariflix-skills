---
task: generatePost()
responsavel: "Ghost"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: topic
    tipo: string
    obrigatorio: true
  - nome: format
    tipo: string
    obrigatorio: true
  - nome: length
    tipo: string
    obrigatorio: false
  - nome: angle
    tipo: string
    obrigatorio: false
  - nome: context
    tipo: string
    obrigatorio: false
Saida:
  - nome: post_content
    tipo: string
    obrigatorio: true
  - nome: hook_options
    tipo: string
    obrigatorio: true
  - nome: hashtags_and_notes
    tipo: string
    obrigatorio: true
Checklist:
  - "[ ] Post soa autêntico no estilo do Sid (não como bot)"
  - "[ ] Hook forte nas primeiras 2 linhas"
  - "[ ] Sem clichês corporativos, CTA natural"
---


# Task: Generate LinkedIn Post

**Task ID:** generate-post
**Agent:** @ghostwriter
**Priority:** HIGH
**Tools Required:** Read

---

## Objetivo

Gerar post completo para LinkedIn no estilo de escrita do Sid, pronto para publicação ou com mínimas edições.

> **Regra de ouro:** O post deve soar como se o Sid tivesse escrito. Se parecer genérico ou "AI-generated", falhou.

---

## Inputs

| Parameter | Description | Example |
|-----------|-------------|---------|
| TOPIC | Tema do post | `AI agents em pentest` |
| FORMAT | Tipo de post | `insight`, `storytelling`, `tutorial`, `opinion`, `list` |
| LENGTH | Tamanho desejado | `short` (150-300), `medium` (300-600), `long` (600-900) |
| ANGLE | Ângulo específico (opcional) | `como usei claude para automatizar recon` |
| CONTEXT | Contexto adicional (opcional) | Experiência real, situação específica |

---

## Workflow

### Step 1: Carregar Estilo

Ler `data/writing-style.md` e internalizar:
- Tom casual e direto
- Frases curtas
- Exemplos concretos
- Mistura formal/informal
- Reflexões pessoais

### Step 2: Definir Estrutura

Com base no FORMAT escolhido:

**Insight/Opinion:**
```
Hook → Contexto → Opinião + argumentos → Reflexão → CTA
```

**Storytelling:**
```
Hook (in medias res) → Setup → Conflito → Resolução → Lição → CTA
```

**Tutorial/How-to:**
```
Hook (resultado) → Problema → Passo 1 → Passo 2 → ... → Resultado → CTA
```

**List:**
```
Hook (número + promessa) → Item 1 → Item 2 → ... → Conclusão → CTA
```

### Step 3: Escrever Hook

Gerar 3 opções de hook e selecionar a mais forte:
- Deve funcionar nas primeiras 2 linhas (antes do "ver mais")
- Deve criar curiosidade ou identificação
- Não pode ser clickbait vazio

### Step 4: Escrever Post Completo

Seguir regras:
- [ ] Frases curtas (máximo 15-20 palavras)
- [ ] Quebras de linha frequentes (espaçamento visual)
- [ ] Exemplos concretos do dia a dia
- [ ] Sem jargão corporativo
- [ ] Máximo 2-3 emojis estratégicos
- [ ] CTA natural no final
- [ ] 3-5 hashtags relevantes

### Step 5: Revisão de Qualidade

Checklist antes de entregar:
- [ ] Soa como o Sid escreveu? (não como um bot)
- [ ] Entrega valor real? (leitor aprende algo)
- [ ] Hook prende nos 2 primeiros segundos?
- [ ] Tamanho adequado para o formato?
- [ ] Sem clichês de LinkedIn ("sinergia", "mindset", "game-changer")?
- [ ] CTA é natural, não forçado?

---

## Output

```markdown
# Post LinkedIn — {{TOPIC}}

**Formato:** {{FORMAT}}
**Pilar:** {{PILLAR}}
**Tamanho:** {{WORD_COUNT}} palavras

---

## Hook Options

1. {{hook_option_1}}
2. {{hook_option_2}}
3. {{hook_option_3}}

**Selecionado:** #{{N}}

---

## Post (pronto para copiar)

{{POST_CONTENT}}

---

## Hashtags

{{HASHTAGS}}

---

## Notas para o autor

- Melhor horário para postar: {{HORARIO}}
- Sugestão de imagem/visual: {{VISUAL_SUGGESTION}}
- Responder comentários nas primeiras 2h
```

---

## Success Criteria

- [ ] Post soa autêntico (estilo Sid)
- [ ] Hook forte nas primeiras 2 linhas
- [ ] Valor tangível para o leitor
- [ ] Dentro do tamanho solicitado
- [ ] Sem clichês ou linguagem genérica
- [ ] CTA natural
- [ ] Hashtags relevantes (3-5)

---

*Task Version: 1.0*
*Created: 2026-03-11*
