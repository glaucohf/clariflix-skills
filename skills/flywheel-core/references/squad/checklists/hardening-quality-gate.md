# --- Identity ---
checklist:
  id: hardening-quality-gate
  name: "Hardening Quality Gate"
  title: "Portão de Qualidade do Hardening"
  description: "Critérios obrigatórios para aprovação final de um ciclo Flywheel."

# --- Validation Levels ---
levels:
  - id: L1
    name: "Sintaxe & Estrutura"
    checks:
      - "O código passa em todos os linters configurados?"
      - "A estrutura de pastas e arquivos segue o padrão do projeto?"
      - "Todos os imports são absolutos conforme Artigo VI?"

  - id: L2
    name: "Lógica & Regras"
    checks:
      - "Nenhuma regra crítica do BR.js foi violada?"
      - "O Blunder Hunter não detectou erros lógicos graves?"
      - "A lógica de negócios está 100% coberta por testes?"

  - id: L3
    name: "Comportamento & Performance"
    checks:
      - "O UBS-Scan não detectou anomalias comportamentais?"
      - "O tempo de execução está dentro dos limites aceitáveis?"
      - "O consumo de tokens foi otimizado?"

# --- Blocking Policy ---
blocking:
  - L1: true
  - L2: true
  - L3: false
