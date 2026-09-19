# Tech Stack — token-optimizer

## Runtime
| Tecnologia | Uso |
|---|---|
| **Claude Code Agent Teams** | Execucao multi-agente com roteamento por complexidade |
| **AIOS Protocol** | Formato padrao de squads (agents/, tasks/, workflows/, squad.yaml) |

## Modelos (Roteamento Assimetrico)
| Modelo | Uso no token-optimizer |
|---|---|
| **Opus** | Orquestrador como router puro (despacho e context-pack) |
| **Sonnet** | OptimizationPlanner e QualityAuditor (raciocinio moderado) |
| **Haiku** | SquadScanner e AntiPatternDetector (tarefas previsíveis) |

## Base de Conhecimento
| Recurso | Descricao |
|---|---|
| **TOKEN-OPTIMIZATION-GUIDE.md** | Guia completo de otimizacao de tokens, custo e latencia |

## Dependencias externas
Nenhuma. Squad puramente baseado em analise de arquivos e raciocinio.
