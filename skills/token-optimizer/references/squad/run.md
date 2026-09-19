---
task: run()
responsavel: "Orchestrator"
responsavel_type: Agente
atomic_layer: Orchestration
Entrada:
  - nome: command
    tipo: string
    descricao: "Comando a executar"
    obrigatorio: true
  - nome: args
    tipo: string[]
    descricao: "Argumentos posicionais"
    obrigatorio: true
  - nome: flags
    tipo: string[]
    descricao: "Flags opcionais"
    obrigatorio: false
Saida:
  - nome: pipelineExecution
    tipo: void
    descricao: "-> execucao direta sem perguntas"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] Comando valido fornecido"
    - "[ ] Argumentos obrigatorios presentes"
  post-conditions:
    - "[ ] Pipeline executado"
    - "[ ] Resultado entregue ao usuario"
---

# run()

/sqopt:run <command> <args> [flags]

Direct execution. Zero questions.

## Sintaxe

/sqopt:run <command> <squadPath> [--priority <value>]

## Comandos disponiveis

| Comando | Workflow | Descricao | Args obrigatorios |
|---------|----------|-----------|-------------------|
| `optimize` | squad_optimization_pipeline | Pipeline completo de otimizacao | `<squadPath>` |
| `audit` | squad_audit_only | Auditoria rapida sem modificacao | `<squadPath>` |
| `scan` | scan_phase only | Apenas escanear e produzir inventario | `<squadPath>` |
| `plan` | scan + detect + plan | Escanear, detectar e planejar (sem executar) | `<squadPath>` |
| `execute` | full pipeline | Alias de optimize | `<squadPath>` |

## Flags opcionais

| Flag | Valores | Default | Descricao |
|------|---------|---------|-----------|
| `--priority` | quality, speed, cost, balanced | balanced | Prioridade de otimizacao |
| `--output` | caminho | ./optimized/ | Diretorio de saida para arquivos otimizados |
| `--verbose` | - | false | Exibir progresso detalhado |

## Exemplos

```bash
# Otimizacao completa com prioridade em qualidade
/sqopt:run optimize ./meu-squad --priority quality

# Auditoria rapida sem modificar nada
/sqopt:run audit /caminho/absoluto/do/squad

# Apenas escanear a estrutura do squad
/sqopt:run scan ./squad-alvo

# Planejar otimizacoes sem executar
/sqopt:run plan ./squad-alvo --priority cost

# Otimizacao com output customizado
/sqopt:run execute ./squad-alvo --output ./squad-alvo-v2
```

## Validacao de Entrada

| Erro | Mensagem |
|------|----------|
| Comando invalido | "Comando '{cmd}' nao reconhecido. Disponiveis: optimize, audit, scan, plan, execute" |
| squadPath ausente | "Argumento obrigatorio: <squadPath>. Ex: /sqopt:run optimize ./meu-squad" |
| squad.yaml nao encontrado | "squad.yaml nao encontrado em '{path}'. Verifique o caminho." |
| --priority invalido | "Prioridade '{val}' invalida. Valores: quality, speed, cost, balanced" |

## Regras

1. Zero perguntas — tudo vem dos argumentos
2. Falhar rapido — validar antes de executar
3. Output limpo — progresso minimo, resultado claro
4. Idioma do usuario
