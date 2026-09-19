---
task: decomposeBeads()
responsavel: FlywheelArchitect
responsavel_type: agent
atomic_layer: reasoning
Entrada:
  - campo: plan_file
    tipo: path
    origen: task.generatePlan
    obrigatorio: true
Saida:
  - campo: beads_file
    tipo: path
    destino: workspace
    persistido: true
Checklist:
  - "Pre-condition: PLAN_SPACE.md existe e foi validado."
  - "Post-condition: O arquivo BEADS.md contém uma lista inicial de unidades executáveis."
  - "Post-condition: Cada Bead possui ID, Título e Intenção definidos."
---

# Decompose Beads
Transforma o PLAN_SPACE.md em uma lista inicial de Beads (BEADS.md).

## Processo
1. Ler o PLAN_SPACE.md em busca de marcos e tarefas técnicas.
2. Criar registros de Beads com ID, Título e Intenção.
3. Mapear dependências iniciais entre os Beads.
4. Escrever o arquivo BEADS.md inicial.
