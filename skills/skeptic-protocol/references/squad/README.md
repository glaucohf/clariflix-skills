# SKEPTIC Protocol

Implementação do SKEPTIC Protocol (Ceticismo Construtivo) em 5 fases rigorosas para engenharia de software preventiva.

## Instalação

1. Mova ou clone a pasta `skeptic-protocol` para dentro do seu diretório de squads no AIOX.
2. Certifique-se de que a CLI do AIOX reconhece o pacote.
3. Invoque os agentes utilizando o prefixo `/sk`.

## O que Faz

Este squad aplica o ceticismo construtivo, forçando a identificação de todas as falhas possíveis antes que a primeira linha de código de implementação seja escrita. O sistema substitui a abordagem ingênua de "construir e testar" por "prever falhas, prová-las com testes que falham e, só então, implementar a solução".

## Pipeline

| Fase | Agente | Papel | Modelo |
|------|--------|-------|--------|
| 1 | `failure-predictor` | Accusation Specialist | Guardian |
| 2 | `test-engineer` | Defense Specialist | Builder |
| 3 | `solution-implementer` | Trial Developer | Builder |
| 4 | `red-teamer` | Appeal Challenger | Balancer |
| 5 | `skeptic-orchestrator`| Verdict & Protocol Manager | Flow_Master |

## Agentes

| Agente | Título | Archetype | Descrição |
|--------|--------|-----------|-----------|
| `failure-predictor` | Accusation Specialist | Guardian | Identifica modos de falha exaustivamente sem produzir código. |
| `test-engineer` | Defense Specialist | Builder | Cria suítes de testes focadas nas acusações, exigindo que elas falhem (Red Phase). |
| `solution-implementer` | Trial Developer | Builder | Refatora e implementa código unicamente para passar na suíte de testes. |
| `red-teamer` | Appeal Challenger | Balancer | Atua como adversário para tentar quebrar a solução criada via edge cases. |
| `skeptic-orchestrator` | Verdict & Protocol Manager | Flow_Master | Garante fluidez do protocolo e redige o SKEPTIC_REPORT.md oficial. |

## Tasks

| Task | Responsável | Atomic Layer | Descrição |
|------|-------------|-------------|-----------|
| `generateAccusations()` | `FailurePredictor` | Organism | Levanta vulnerabilidades com severidade e probabilidade. |
| `writeFailingTests()` | `TestEngineer` | Organism | Transcreve vulnerabilidades para testes práticos negativos. |
| `implementTrialCode()` | `SolutionImplementer` | Organism | Codifica a solução para satisfazer as restrições da Defesa. |
| `executeAppeal()` | `RedTeamer` | Molecule | Desafia ativamente a codebase aprovada na fase Trial. |
| `generateVerdictReport()`| `SkepticOrchestrator` | Molecule | Avalia as estatísticas finais e gera a documentação. |

## Workflows

| Workflow | Pattern | Agentes | Descrição |
|----------|---------|---------|-----------|
| `skeptic_pipeline_execution` | Pipeline | Todos os 5 | A execução principal e linear das 5 Fases da metodologia. |
| `red_team_feedback_loop` | Evaluator-Optimizer | `red-teamer`, `failure-predictor`, `solution-implementer` | O loop adversarial engatilhado se o Apelo quebrar o código. |

## Configuração

- config/coding-standards.md
- config/tech-stack.md
- config/source-tree.md

## Uso

### Comandos Disponíveis

- `*generate-accusations`: Avalia requisitos e cria acusações em Markdown.
- `*write-failing-tests`: Constrói a test suite inicial baseada nas acusações.
- `*implement-trial-code`: Executa a rotina de código produtivo.
- `*execute-appeal`: Realiza um *pentest* interno ou revisão rígida de edge cases.
- `*generate-verdict-report`: Compila o relatório final do ciclo SKEPTIC.

### Exemplos

```bash
# Para iniciar o pipeline do zero
/sk:failure-predictor
*generate-accusations --objective="Desenvolver sistema de login com MFA"
```

## Autor

Marcio Bisognin

[Squads Platform](https://squads.sh/pt)
[Instagram @marciobisognin](https://www.instagram.com/marciobisognin/)

## Licença

MIT
