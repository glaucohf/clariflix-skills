<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**Analisa squads AIOS existentes e produz otimizacoes priorizadas por ROI — qualidade, velocidade e economia de tokens.**

Pipeline sequencial de 5 agentes que escaneia, detecta anti-patterns, planeja, executa e audita otimizacoes usando TOKEN-OPTIMIZATION-GUIDE.md como base de conhecimento.

`/sqopt`

</div>

---

## Seu squad consome 10x mais tokens do que deveria?

Voce construiu um squad funcional. Ele roda, entrega resultados, resolve o problema. Mas toda execucao custa **$0.28** e voce sabe que metade desses tokens esta sendo desperdicada em prompts redundantes, retornos verbosos que ninguem le, e Opus fazendo trabalho de Haiku.

O pior? Voce nao sabe **onde** estao os gargalos. Sao dezenas de arquivos, multiplos agentes, workflows encadeados — e cada um esconde anti-patterns invisiveis a olho nu. Context Bloat, Double-Read, Ghost Tokens, Model Overkill. O custo se acumula silenciosamente, execucao apos execucao.

E se eu te dissesse que **12 tecnicas comprovadas** podem reduzir seu custo em ate 78%, aumentar a qualidade dos outputs em 34%, e que tudo isso pode ser aplicado de forma automatica — sem quebrar nada?

---

## O Antes e o Depois

| | Sem Otimizacao | Com token-optimizer |
|---|---|---|
| **Tokens Opus** | 100% | 2-5% (Router Puro) |
| **Custo por execucao** | $0.28 | $0.06 (-78%) |
| **Qualidade output** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns detectados** | 0 | 100% catalogados |

---

## Como Funciona

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

O pipeline completo percorre 5 fases sequenciais. Cada agente le o output do anterior via arquivo (Files as Contracts), retorna apenas `"Done: {path}"` ao orquestrador, e o proximo agente continua de onde o anterior parou. Zero tokens desperdicados em transicoes.

---

## Por que token-optimizer?

- **12 tecnicas comprovadas** — Nao e achismo. Cada otimizacao e mapeada a uma secao numerada do TOKEN-OPTIMIZATION-GUIDE.md, com fundamentacao tecnica e metricas de impacto documentadas.

- **Priorizacao por ROI** — Qualidade primeiro, velocidade segundo, custo terceiro. O planner ordena as acoes pelo maior retorno real, nao pela reducao mais facil. Voce melhora o output antes de cortar custos.

- **Deteccao automatica de 10+ anti-patterns** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — cada um com scoring de severidade 1-10 e estimativa de tokens desperdicados.

- **Modo audit-only** — Quer apenas um diagnostico sem modificar nenhum arquivo? O workflow `squad_audit_only` escaneia, detecta e reporta — zero alteracoes, visibilidade total.

---

## Agentes

| | Nome | Arquetipo | Papel |
|---|---|---|---|
| | **SquadScanner** | Guardian | Le e cataloga a estrutura completa de um squad alvo, produzindo um inventario estruturado |
| | **AntiPatternDetector** | Guardian | Identifica anti-patterns de tokens, scores de severidade e impacto estimado |
| | **OptimizationPlanner** | Balancer | Cria plano de otimizacao priorizado por ROI, mapeando anti-patterns a tecnicas comprovadas |
| | **OptimizationExecutor** | Builder | Executa o plano, reescrevendo versoes otimizadas dos arquivos do squad |
| | **QualityAuditor** | Guardian | Valida o squad otimizado, compara metricas antes/depois e garante compliance AIOS |

---

## Tasks

| Task | Agente Responsavel | Camada Atomica |
|---|---|---|
| `scanSquad()` | SquadScanner | Escaneia squad alvo e produz squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | Cruza inventario com lista de anti-patterns do guia |
| `planOptimization()` | OptimizationPlanner | Gera plano priorizado por ROI com acoes atomicas |
| `executeOptimization()` | OptimizationExecutor | Aplica otimizacoes e gera arquivos em optimized/ |
| `auditQuality()` | QualityAuditor | Valida compliance AIOS e produz relatorio before/after |

---

## Workflows

| Nome | Padrao | Descricao |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | Pipeline completo: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | Auditoria rapida: scan, detect, audit — sem modificar arquivos |

---

## Comandos

| Comando | O que faz |
|---|---|
| `/sqopt` | Inicia o pipeline interativo com coleta de configuracao |
| `/sqopt:run` | Execucao direta sem perguntas |
| `*sqopt-scan` | Escaneia squad alvo e produz inventario JSON |
| `*sqopt-detect` | Detecta anti-patterns e produz relatorio de severidade |
| `*sqopt-plan` | Gera plano de otimizacao priorizado por ROI |
| `*sqopt-execute` | Aplica otimizacoes planejadas nos arquivos do squad |
| `*sqopt-audit` | Audita squad otimizado e gera relatorio de metricas |

---

## Tech Stack

| Tecnologia | Uso |
|---|---|
| **Claude Code Agent Teams** | Orquestracao multi-agente com roteamento Haiku/Sonnet/Opus |
| **AIOS 2.1+** | Framework de squads — formato padrao de agents, tasks, workflows |
| **Markdown/YAML** | Definicao de agentes, tarefas, workflows e configuracoes |
| **JSON** | Files as Contracts — comunicacao inter-agente via arquivos estruturados |

---

<details>
<summary><strong>FAQ</strong></summary>

### Funciona com qualquer squad?

Sim. O token-optimizer analisa qualquer squad no formato AIOS padrao. Basta apontar o caminho do diretorio e o scanner cataloga automaticamente todos os agents, tasks, workflows e configs. Nao importa o dominio — se segue o formato AIOS, pode ser otimizado.

### Modifica meus arquivos?

Depende do modo escolhido. No pipeline completo (`squad_optimization_pipeline`), o executor gera versoes otimizadas em um diretorio separado `optimized/` — seus originais nunca sao sobrescritos. No modo `squad_audit_only`, e 100% read-only: apenas diagnostico e relatorio, zero alteracoes.

### Quanto economiza?

Entre 65% e 98% de reducao de tokens, dependendo dos anti-patterns encontrados. O caso mais comum — squads com Model Overkill e Context Bloat — costuma ter reducao de 78% no custo por execucao. O relatorio final do QualityAuditor mostra projecoes detalhadas de tokens, custo e latencia antes/depois.

</details>

---

<div align="center">

**Criado por [Renato Medeiros](https://github.com/Renat0z)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>
