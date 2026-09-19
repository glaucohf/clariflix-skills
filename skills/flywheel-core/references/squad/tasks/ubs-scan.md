---
task: ubsScan()
responsavel: HardeningSpecialist
responsavel_type: agent
atomic_layer: hardening
Entrada:
  - campo: request
    tipo: string
    origen: orchestrator
    obrigatorio: true
Saida:
  - campo: ubs_report
    tipo: path
    destino: workspace
    persistido: true
Checklist:
  - "Pre-condition: O sistema está em estado estável para scan."
  - "Post-condition: UBS_REPORT.md gerado com todos os bugs latentes encontrados."
---

# ubs scan
Executa o scanner de bugs definitivo (UBS) no projeto.

## Processo
1. Realizar análise estática e dinâmica profunda do repositório.
2. Buscar por erros de tipagem, vazamentos de memória e falhas de segurança.
3. Emitir relatório detalhado com classificação de severidade.
