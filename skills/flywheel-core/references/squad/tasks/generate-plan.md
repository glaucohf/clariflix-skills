---
task: generatePlan()
responsavel: FlywheelArchitect
responsavel_type: agent
atomic_layer: reasoning
Entrada:
  - campo: objective
    tipo: string
    origen: user
    obrigatorio: true
Saida:
  - campo: plan_file
    tipo: path
    destino: workspace
    persistido: true
Checklist:
  - "Pre-condition: O objetivo global do sistema está claro e definido."
  - "Post-condition: O arquivo PLAN_SPACE.md contém pelo menos 2000 linhas de raciocínio estruturado."
  - "Post-condition: Seção explícita para mitigação de riscos incluída no plano."
---

# Generate Plan Space
Cria um plano estratégico de alta densidade (Plan Space) para o objetivo global.

## Processo
1. Realizar síntese multi-modelo (GPT-4o, Claude 3.5, Gemini 1.5).
2. Identificar arquitetura, dependências e 'Hard Parts'.
3. Escrever PLAN_SPACE.md com justificativas técnicas.
4. Definir marcos de sucesso e critérios de validação.
