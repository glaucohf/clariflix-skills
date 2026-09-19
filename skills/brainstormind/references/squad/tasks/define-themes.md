---
task: defineThemes()
responsavel: "ThemeDefiner"
responsavel_type: Agente
atomic_layer: Atom

Entrada:
  - nome: topicText
    tipo: string
    descricao: "usuario -> ThemeDefiner"
    obrigatorio: true

Saida:
  - nome: themesJson
    tipo: JSON
    descricao: "-> generateIdeas()"
    obrigatorio: true
  - nome: themesTable
    tipo: string
    descricao: "-> usuario (display)"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Topico extraido dos argumentos do skill"
    - "[ ] Diretorio .brainstorm-tmp/ criado"
  post-conditions:
    - "[ ] 10 tipos de associacao definidos"
    - "[ ] themes.json salvo em .brainstorm-tmp/"
    - "[ ] Tabela apresentada ao usuario"
---

# defineThemes()

```
[topic] --> [ThemeDefiner] --> [themes.json + tabela]
```

Decompoe o topico em 10 tipos de associacao diversos, selecionados do pool ou inventados. Output maximo ~200 tokens.
