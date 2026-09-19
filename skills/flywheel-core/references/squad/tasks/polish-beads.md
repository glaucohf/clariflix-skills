---
task: polishBeads()
responsavel: BeadManager
responsavel_type: agent
atomic_layer: memory
Entrada:
  - campo: beads_list
    tipo: array
    origen: task.decomposeBeads
    obrigatorio: true
  - campo: iterations
    tipo: integer
    origen: config
    obrigatorio: false
Saida:
  - campo: polished_beads
    tipo: path
    destino: workspace
    persistido: true
Checklist:
  - "Pre-condition: Lista de Beads iniciais está disponível."
  - "Post-condition: Cada Bead contém 'Why', 'How' e 'Test Obligation'."
  - "Post-condition: Nenhum Bead excede 200 linhas de contexto operacional."
---

# Polish Beads
Ciclo iterativo (N=4 a 6) para remover ambiguidades e adicionar contexto aos Beads.

## Processo
1. Ler cada Bead e verificar consistência com o Plan Space.
2. Remover lacunas de contexto e ambiguidades na implementação.
3. Adicionar obrigações de teste explícitas para cada Bead.
4. Repetir o ciclo até que a convergência seja atingida.
