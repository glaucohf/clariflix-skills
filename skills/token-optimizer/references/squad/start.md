---
task: start()
responsavel: "Orchestrator"
responsavel_type: Agente
atomic_layer: Orchestration
Entrada:
  - nome: userTrigger
    tipo: string
    descricao: "usuario -> /sqopt ou /sqopt <input>"
    obrigatorio: true
Saida:
  - nome: configJson
    tipo: JSON
    descricao: "-> .sqopt-tmp/config.json com todas as escolhas"
    obrigatorio: true
  - nome: pipelineExecution
    tipo: void
    descricao: "-> execucao completa do pipeline principal"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] Skill /sqopt invocada"
  post-conditions:
    - "[ ] config.json salvo"
    - "[ ] Pipeline executado ate o final"
    - "[ ] Resultado entregue ao usuario"
---

# start()

```
[/sqopt] ──▶ [Coleta Interativa] ──▶ [config.json] ──▶ [Pipeline] ──▶ [optimization-report.md]
```

Entry point interativo do token-optimizer. Coleta informacoes sobre o squad alvo, escopo de otimizacao e prioridades, depois executa o pipeline correspondente.

## FASE 0 — Apresentacao

Apresentar ao usuario:

```
╔══════════════════════════════════════════════════╗
║  Squad Optimizer                                  ║
║  Analisa e otimiza squads AIOS para              ║
║  qualidade, velocidade e economia de tokens      ║
╠══════════════════════════════════════════════════╣
║  Pipeline:                                        ║
║  1. Scan — inventario completo do squad           ║
║  2. Detect — anti-patterns de tokens              ║
║  3. Plan — otimizacoes priorizadas por ROI        ║
║  4. Execute — reescrita otimizada                 ║
║  5. Audit — relatorio before/after                ║
╚══════════════════════════════════════════════════╝

Vamos configurar sua sessao.
```

## FASE 1 — Coleta Interativa (via AskUserQuestion)

### Pergunta 1 — Squad alvo (obrigatoria)

AskUserQuestion(
  question: "Qual o caminho do squad que voce quer otimizar? (caminho absoluto ou relativo ao diretorio atual)",
)

→ Salvar como `squadPath`. Validar que o diretorio existe e contem `squad.yaml`.

### Pergunta 2 — Escopo de execucao

AskUserQuestion(
  question: "Qual escopo de execucao?",
  options: ["Otimizacao completa (scan + detect + plan + execute + audit)", "Auditoria apenas (scan + detect + audit, sem modificar arquivos)"]
)

→ Mapear para `scope`: "full" ou "audit-only".

### Pergunta 3 — Prioridade de otimizacao

AskUserQuestion(
  question: "Qual a prioridade principal da otimizacao?",
  options: ["Qualidade dos outputs (competicao, recycling, validacao inline)", "Velocidade de resposta (paralelismo, waves, menos round-trips)", "Economia de tokens (router puro, modelo certo, compressao)", "Balanceado (qualidade > velocidade > custo)"]
)

→ Mapear para `optimizationPriority`: "quality" | "speed" | "cost" | "balanced".

### Pergunta 4 — Contexto adicional (opcional)

AskUserQuestion(
  question: "Ha algum contexto adicional sobre este squad? (ex: pontos de dor especificos, restricoes, areas prioritarias)",
  options: ["Sim, quero adicionar contexto", "Nao, seguir com as configuracoes acima"]
)

→ Se "Sim": AskUserQuestion(question: "Descreva o contexto adicional:")
→ Salvar como `additionalContext` ou null.

## FASE 1.5 — Setup e Confirmacao

1. Criar diretorio `.sqopt-tmp/`
2. Salvar config.json:
```json
{
  "squadPath": "{resposta 1}",
  "scope": "{full|audit-only}",
  "optimizationPriority": "{quality|speed|cost|balanced}",
  "additionalContext": "{resposta 4 ou null}",
  "timestamp": "{ISO timestamp}"
}
```
3. Exibir resumo das escolhas
4. Iniciar execucao imediatamente — SEM pedir confirmacao extra

## FASE 2 — Execucao do Pipeline

- Se `scope` = "full" → executar workflow `squad_optimization_pipeline`
- Se `scope` = "audit-only" → executar workflow `squad_audit_only`

## Regras

1. Apresentacao primeiro
2. Uma pergunta por vez — NUNCA todas de uma vez
3. SEMPRE usar AskUserQuestion com options para multipla escolha
4. squadPath obrigatorio — sem ele nao ha pipeline
5. Zero confirmacao pos-setup — coletou, configurou, executa
6. Respeitar scope — executar apenas o workflow correspondente
7. Idioma do usuario — perguntas no mesmo idioma da interacao
8. Cleanup ao final — remover .sqopt-tmp/
