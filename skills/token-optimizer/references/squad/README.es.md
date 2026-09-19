<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**Analiza squads AIOS existentes y produce optimizaciones priorizadas por ROI — calidad, velocidad y ahorro de tokens.**

Pipeline secuencial de 5 agentes que escanea, detecta anti-patterns, planifica, ejecuta y audita optimizaciones usando TOKEN-OPTIMIZATION-GUIDE.md como base de conocimiento.

`/sqopt`

</div>

---

## Tu squad consume 10x mas tokens de lo que deberia?

Construiste un squad funcional. Corre, entrega resultados, resuelve el problema. Pero cada ejecucion cuesta **$0.28** y sabes que la mitad de esos tokens se desperdician en prompts redundantes, retornos verbosos que nadie lee, y Opus haciendo el trabajo de Haiku.

Lo peor? No sabes **donde** estan los cuellos de botella. Son decenas de archivos, multiples agentes, workflows encadenados — y cada uno esconde anti-patterns invisibles a simple vista. Context Bloat, Double-Read, Ghost Tokens, Model Overkill. El costo se acumula silenciosamente, ejecucion tras ejecucion.

Y si te dijera que **12 tecnicas comprobadas** pueden reducir tu costo hasta un 78%, aumentar la calidad de los outputs en un 34%, y que todo esto se puede aplicar de forma automatica — sin romper nada?

---

## El Antes y el Despues

| | Sin Optimizacion | Con token-optimizer |
|---|---|---|
| **Tokens Opus** | 100% | 2-5% (Router Puro) |
| **Costo por ejecucion** | $0.28 | $0.06 (-78%) |
| **Calidad del output** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns detectados** | 0 | 100% catalogados |

---

## Como Funciona

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

El pipeline completo recorre 5 fases secuenciales. Cada agente lee el output del anterior via archivo (Files as Contracts), retorna solo `"Done: {path}"` al orquestador, y el siguiente agente continua donde el anterior termino. Cero tokens desperdiciados en transiciones.

---

## Por que token-optimizer?

- **12 tecnicas comprobadas** — No es adivinanza. Cada optimizacion esta mapeada a una seccion numerada del TOKEN-OPTIMIZATION-GUIDE.md, con fundamentacion tecnica y metricas de impacto documentadas.

- **Priorizacion por ROI** — Calidad primero, velocidad segundo, costo tercero. El planner ordena las acciones por mayor retorno real, no por la reduccion mas facil. Mejoras el output antes de recortar costos.

- **Deteccion automatica de 10+ anti-patterns** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — cada uno con scoring de severidad 1-10 y estimacion de tokens desperdiciados.

- **Modo audit-only** — Quieres solo un diagnostico sin modificar ningun archivo? El workflow `squad_audit_only` escanea, detecta y reporta — cero alteraciones, visibilidad total.

---

## Agentes

| | Nombre | Arquetipo | Rol |
|---|---|---|---|
| | **SquadScanner** | Guardian | Lee y cataloga la estructura completa de un squad objetivo, produciendo un inventario estructurado |
| | **AntiPatternDetector** | Guardian | Identifica anti-patterns de tokens con scores de severidad e impacto estimado |
| | **OptimizationPlanner** | Balancer | Crea plan de optimizacion priorizado por ROI, mapeando anti-patterns a tecnicas comprobadas |
| | **OptimizationExecutor** | Builder | Ejecuta el plan, reescribiendo versiones optimizadas de los archivos del squad |
| | **QualityAuditor** | Guardian | Valida el squad optimizado, compara metricas antes/despues y garantiza compliance AIOS |

---

## Tasks

| Task | Agente Responsable | Capa Atomica |
|---|---|---|
| `scanSquad()` | SquadScanner | Escanea squad objetivo y produce squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | Cruza inventario con lista de anti-patterns de la guia |
| `planOptimization()` | OptimizationPlanner | Genera plan priorizado por ROI con acciones atomicas |
| `executeOptimization()` | OptimizationExecutor | Aplica optimizaciones y genera archivos en optimized/ |
| `auditQuality()` | QualityAuditor | Valida compliance AIOS y produce reporte before/after |

---

## Workflows

| Nombre | Patron | Descripcion |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | Pipeline completo: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | Auditoria rapida: scan, detect, audit — sin modificar archivos |

---

## Comandos

| Comando | Que hace |
|---|---|
| `/sqopt` | Inicia el pipeline interactivo con recoleccion de configuracion |
| `/sqopt:run` | Ejecucion directa sin preguntas |
| `*sqopt-scan` | Escanea squad objetivo y produce inventario JSON |
| `*sqopt-detect` | Detecta anti-patterns y produce reporte de severidad |
| `*sqopt-plan` | Genera plan de optimizacion priorizado por ROI |
| `*sqopt-execute` | Aplica optimizaciones planificadas en los archivos del squad |
| `*sqopt-audit` | Audita squad optimizado y genera reporte de metricas |

---

## Tech Stack

| Tecnologia | Uso |
|---|---|
| **Claude Code Agent Teams** | Orquestacion multi-agente con ruteo Haiku/Sonnet/Opus |
| **AIOS 2.1+** | Framework de squads — formato estandar de agents, tasks, workflows |
| **Markdown/YAML** | Definicion de agentes, tareas, workflows y configuraciones |
| **JSON** | Files as Contracts — comunicacion inter-agente via archivos estructurados |

---

<details>
<summary><strong>FAQ</strong></summary>

### Funciona con cualquier squad?

Si. token-optimizer analiza cualquier squad en formato AIOS estandar. Solo apunta la ruta del directorio y el scanner cataloga automaticamente todos los agents, tasks, workflows y configs. No importa el dominio — si sigue el formato AIOS, se puede optimizar.

### Modifica mis archivos?

Depende del modo elegido. En el pipeline completo (`squad_optimization_pipeline`), el executor genera versiones optimizadas en un directorio separado `optimized/` — tus originales nunca se sobrescriben. En modo `squad_audit_only`, es 100% read-only: solo diagnostico y reporte, cero alteraciones.

### Cuanto ahorra?

Entre 65% y 98% de reduccion de tokens, dependiendo de los anti-patterns encontrados. El caso mas comun — squads con Model Overkill y Context Bloat — tipicamente muestra una reduccion del 78% en costo por ejecucion. El reporte final del QualityAuditor muestra proyecciones detalladas de tokens, costo y latencia antes/despues.

</details>

---

<div align="center">

**Creado por [NSCL Pipeline](https://github.com/nscl-pipeline)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>
