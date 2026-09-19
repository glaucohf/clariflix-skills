# IDEATION — token-optimizer

## Racional de Design

### Problema
Squads AIOS sao frequentemente criados sem otimizacao de tokens. Um pipeline naive de 10 agentes Opus consome 50.000+ tokens por execucao. A maioria dos squads sofre de: fat orchestrator, model overkill, double-reads, ghost tokens e sequential launch.

### Solucao
Um meta-squad que analisa qualquer squad existente e produz uma versao otimizada, aplicando patterns comprovados do TOKEN-OPTIMIZATION-GUIDE.md. Foco triplo: qualidade > velocidade > custo.

### Decisoes Arquiteturais

1. **5 agentes especializados em pipeline sequencial** — cada agente tem responsabilidade unica e atomica. Scanner nao detecta patterns. Detector nao planeja. Planner nao executa. Separacao de concerns total.

2. **2 workflows (full + audit-only)** — nem sempre o usuario quer otimizar. O modo audit-only permite diagnostico rapido sem modificacao, pulando planner e executor.

3. **Guardian-heavy (3 Guardians, 1 Balancer, 1 Builder)** — a natureza do squad e analise/validacao. Apenas o executor e Builder (cria/modifica arquivos). O planner e Balancer (equilibra prioridades de ROI).

4. **TOKEN-OPTIMIZATION-GUIDE.md como Single Source of Truth** — todas as tecnicas, anti-patterns e formulas vem do guia. Agentes referenciam secoes especificas por numero. Sem invencao de patterns.

5. **Files as Contracts entre fases** — squad-inventory.json, anti-patterns-report.json, optimization-plan.json, changelog.json. Cada agente le o artefato da fase anterior e produz o artefato da proxima. Zero retornos verbosos.

6. **Roteamento assimetrico** — Scanner e Detector sao tarefas previsiveis (Haiku). Planner e Auditor exigem raciocinio moderado (Sonnet). Orquestrador e router puro (Opus, tokens minimos).

7. **Diretorio optimized/ separado** — nunca sobrescrever originais. Permite comparacao before/after e rollback seguro.

### Anti-Patterns Evitados no Proprio Squad
- Router Puro: orquestrador so despacha, nunca gera/julga
- Retornos Minimos: agentes retornam "Done: {path}"
- Files as Contracts: toda comunicacao via JSON intermediario
- Ler 1x Usar N: inventario lido uma vez, consumido por 3 agentes downstream
- Modelo Certo: Haiku para scan/detect, Sonnet para plan/audit, Opus so roteia
