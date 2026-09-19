---
task: scanSquad()
responsavel: "SquadScanner"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: squadPath
    tipo: string
    descricao: "usuario → caminho absoluto do squad alvo"
    obrigatorio: true
  - nome: scope
    tipo: string
    descricao: "config.json → nivel de escaneamento (full|structure-only)"
    obrigatorio: false
Saida:
  - nome: squadInventory
    tipo: JSON
    descricao: "→ squad-inventory.json consumido por AntiPatternDetector e QualityAuditor"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] squadPath aponta para diretorio valido com squad.yaml"
    - "[ ] Diretorios agents/, tasks/, workflows/ existem"
  post-conditions:
    - "[ ] squad-inventory.json salvo no diretorio de trabalho"
    - "[ ] Todos os arquivos do squad catalogados com metadados"
    - "[ ] Estimativa de tokens por agente calculada"
---
# scanSquad()
```
[squadPath] ──▶ [SquadScanner] ──▶ [squad-inventory.json]
```

Le recursivamente a estrutura do squad alvo. Para cada arquivo: extrai YAML frontmatter, identifica tipo (agent/task/workflow/config), cataloga metadados relevantes. Calcula estimativa de tokens por agente baseada no tamanho do system prompt e context size. Mapeia dependencias inter-task usando contratos Entrada/Saida. Grava inventario completo em squad-inventory.json.
