---
task: start()
responsavel: "Orchestrator"
responsavel_type: Agente
atomic_layer: Strategy

Entrada:
  - nome: userTrigger
    tipo: string
    descricao: "usuario -> /brain ou /brain <topic>"
    obrigatorio: true

Saida:
  - nome: configJson
    tipo: JSON
    descricao: "-> .brainstorm-tmp/config.json com todas as escolhas"
    obrigatorio: true
  - nome: pipelineExecution
    tipo: void
    descricao: "-> execucao completa do brain-pipeline"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Skill /brain invocada"
  post-conditions:
    - "[ ] config.json salvo em .brainstorm-tmp/"
    - "[ ] Pipeline executado ate o final"
    - "[ ] brain_report.md entregue ao usuario"
    - "[ ] .brainstorm-tmp/ limpo"
---

# start()

```
[user] --> [Perguntas Interativas] --> [config.json] --> [Pipeline Completo]
```

Ponto de entrada do Brain Squad. Coleta parametros via perguntas de multipla escolha e executa o pipeline completo.

---

## FASE 0 — Coleta Interativa

Faca as perguntas abaixo **uma por vez**, usando a ferramenta `AskUserQuestion` (selecao interativa com setas cima/baixo). **NUNCA exiba opcoes como texto formatado no chat** — sempre use a ferramenta interativa. Se o usuario ja forneceu o topico no comando (ex: `/brain como monetizar uma skill`), pule a Pergunta 1.

### Pergunta 1 — Topico

```
Qual o topico ou desafio que voce quer explorar?

(Digite livremente)
```

> Se vazio, nao prossiga. Repita a pergunta.

### Pergunta 2 — Objetivo

```
Qual seu objetivo com este brainstorming?

A) Explorar ideias novas — quero descobrir o que nao sei
B) Resolver um problema — tenho um desafio especifico
C) Tomar uma decisao — preciso comparar caminhos
D) Inovar — quero conexoes inesperadas e provocativas
```

> Salvar como `objective` no config. Influencia os tipos de associacao do ThemeDefiner.

### Pergunta 3 — Profundidade

```
Ate onde quer ir?

A) Diverge + Converge (Recomendado) — gera 200 ideias, filtra Top 3, depois refina o melhor em design completo
B) Apenas Diverge — gera 200 ideias e filtra Top 3, sem fase de design
C) Rapido — 1 rodada so (100 ideias, Top 3)
```

> Salvar como `depth`. Determina qual workflow executar:
> - A → brain-pipeline.yaml (completo)
> - B → diverge-only.yaml
> - C → diverge-only.yaml com skip de Round 2

### Pergunta 4 — Contexto adicional (opcional)

```
Quer adicionar contexto? (opcional — pode pular)

A) Sim — quero descrever restricoes, publico-alvo ou contexto
B) Nao — seguir direto
```

> Se A, pedir texto livre e salvar como `context`. Se B, `context = null`.

---

## FASE 0.5 — Setup e Confirmacao

Apos coletar as respostas:

### 1. Criar diretorio

```bash
mkdir -p .brainstorm-tmp/r1 .brainstorm-tmp/r2
```

### 2. Salvar config

Escrever `.brainstorm-tmp/config.json`:

```json
{
  "topic": "...",
  "objective": "explore | solve | decide | innovate",
  "depth": "full | diverge | quick",
  "context": "..." | null,
  "timestamp": "ISO-8601"
}
```

### 3. Salvar topico

```bash
echo "{TOPIC}" > .brainstorm-tmp/topic.txt
```

### 4. Confirmar e iniciar

Apresentar resumo compacto ao usuario:

```
--- Brain Session ---
Topico:      {topic}
Objetivo:    {objective}
Profundidade: {depth}
Contexto:    {context ou "nenhum"}

Iniciando pipeline...
```

**NAO pedir confirmacao adicional. Iniciar imediatamente.**

---

## FASE 1+ — Execucao do Pipeline

Com base no `depth` escolhido, executar o workflow correspondente:

| depth | workflow | fases |
|-------|----------|-------|
| `full` | brain-pipeline.yaml | Todas (Diverge + Gate + Converge + Report) |
| `diverge` | diverge-only.yaml | Fase 1 apenas (Diverge + Synthesize + Cleanup) |
| `quick` | diverge-only.yaml | Round 1 apenas (skip Round 2) |

### Mapeamento objetivo → tipos de associacao

O `objective` influencia a selecao de tipos pelo ThemeDefiner:

| objective | tipos priorizados |
|-----------|-------------------|
| `explore` | Conexoes inesperadas, Analogias, Tendencias, Perguntas provocativas |
| `solve` | Dores e problemas, Causas raiz, Ferramentas/Recursos, Contextos de aplicacao |
| `decide` | Opostos e tensoes, Consequencias, Principios, Perfis/Personas |
| `innovate` | Conexoes inesperadas, Analogias, Opostos e tensoes, Perguntas provocativas |

> Passar este mapeamento como hint para o ThemeDefiner, nao como restricao rigida.

### Se `context` fornecido

Incluir no prompt de cada agente gerador:

```
Context: {context}
```

---

## Regras

1. **Uma pergunta por vez** — nunca enviar todas de uma vez
2. **Multipla escolha sempre que possivel** — reduz fricao
3. **Topico obrigatorio** — sem topico nao ha pipeline
4. **Zero confirmacao pos-setup** — coletou, configurou, executa
5. **Respeitar depth** — se o usuario escolheu "rapido", nao sugira "completo"
6. **Idioma do usuario** — perguntas no mesmo idioma do topico/interacao
