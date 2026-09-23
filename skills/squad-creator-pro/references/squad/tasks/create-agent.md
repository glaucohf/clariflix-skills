# Task: Create Squad Agent (Extension Wrapper)

**Task ID:** create-agent
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto roteia a criação research-first de agentes para o workflow canônico do pack
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado do workflow pro `wf-research-then-create-agent`

---

## Purpose

Este arquivo existe para manter compatibilidade com workflows, handoffs e comandos do `squad-creator-pro` que ainda referenciam `create-agent` diretamente.

**Regra não negociável:** o `squad-creator-pro` é um upgrade-pack do `squad-creator`, não uma implementação paralela. No pro, a criação research-first de agentes vive no workflow:

- `workflows/wf-research-then-create-agent.yaml`

Este wrapper:

1. normaliza inputs legados do pack;
2. reconcilia a origem do agente (specialist, clone, research genérico);
3. delega a execução ao workflow canônico do pro;
4. devolve os outputs no formato esperado pelos chamadores.

**Importante:** dentro de `wf-research-then-create-agent.yaml`, `create-agent.md` aparece como dependência conceitual e ponto de handoff, não como um segundo pipeline monolítico a ser mantido aqui.

---

## Canonical Owners

- `workflows/wf-research-then-create-agent.yaml` -- owner canônico da criação de agentes research-first no pro
- `workflows/wf-clone-mind.yaml` -- upstream quando o agente nasce de DNA já clonado
- `workflows/wf-mind-research-loop.yaml` -- upstream quando a seleção de mentes precede a criação
- `tasks/create-task.md` -- downstream para tasks do agente, via wrapper que delega ao base

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `agent_purpose` | string | Yes | O que o agente deve fazer |
| `domain` | string | Yes | Domínio principal do agente |
| `squad_name` | string | No | Nome canônico do squad alvo |
| `pack_name` | string | No | Alias legado; deve ser normalizado para `squad_name` |
| `specialist_slug` | string | No | Slug do especialista, se houver |
| `specialist_name` | string | No | Nome legível do especialista |
| `mind_slug` | string | No | Slug do clone/dna já preparado |
| `dna_bundle_path` | path | No | Caminho para `mind_dna_complete.yaml` ou artefato equivalente |
| `research_artifacts` | list | No | Pesquisa, sínteses ou fontes já produzidas |
| `output_dir` | path | No | Diretório de saída para pesquisa auxiliar |

---

## Preconditions

- [ ] `workflows/wf-research-then-create-agent.yaml` existe
- [ ] O squad alvo existe em `squads/{squad_name}/` ou `squads/{pack_name}/`
- [ ] O chamador entende que este arquivo não possui pipeline monolítico próprio
- [ ] Qualquer DNA, research ou handoff upstream já foi produzido antes da delegação

---

## Workflow

### Step 1: Normalize Target Squad

```yaml
normalize_target:
  rules:
    - if: "squad_name is empty AND pack_name exists"
      then: "set squad_name = pack_name"
    - if: "both squad_name and pack_name exist AND differ"
      then: "block and reconcile target"
    - verify_path: "squads/{squad_name}/"
```

### Step 2: Reconcile Agent Source

```yaml
reconcile_source:
  rules:
    - if: "mind_slug exists OR dna_bundle_path exists"
      then: "agent_source = dna-backed"
    - if: "specialist_slug exists OR specialist_name exists"
      then: "agent_source = specialist-research"
    - else: "agent_source = domain-research"
  invariants:
    - "DNA-backed creation may reuse upstream clone artifacts"
    - "Specialist-based creation still runs through the pro research-first workflow"
    - "This wrapper does not define extraction, synthesis, or quality-gate logic locally"
```

### Step 3: Delegate to Canonical Pro Workflow

```yaml
delegate_to_pro_workflow:
  workflow: "workflows/wf-research-then-create-agent.yaml"
  execution_contract:
    - use_pro_research_loop: true
    - reuse_clone_mind_outputs_if_present: true
    - preserve_research_artifacts_traceability: true
    - use_create_task_wrapper_for_downstream_task_generation: true
  prohibition:
    - "Do NOT recreate research phases here"
    - "Do NOT fork agent-definition logic locally"
    - "Do NOT maintain a second monolithic create-agent implementation in the pro pack"
```

### Step 4: Reconcile Outputs for Pro Callers

```yaml
reconcile_outputs:
  primary_outputs:
    - "squads/{squad_name}/agents/{agent_id}.md"
    - "docs/research/{specialist_slug}-{topic}-research.md"
    - "squads/{squad_name}/tasks/{task_id}.md"
  enrichments:
    - if_dna_bundle: "Preserve provenance from clone-mind artifacts"
    - if_research_artifacts: "Carry citations and source traceability forward"
  return_shape:
    agent_file: "path to created agent"
    delegated_workflow: "workflows/wf-research-then-create-agent.yaml"
    execution_mode: "pro-delegated"
```

---

## Output

```yaml
output:
  name: delegated_agent_creation
  format: yaml
  structure:
    agent_file: "squads/{squad_name}/agents/{agent_id}.md"
    delegated_workflow: "workflows/wf-research-then-create-agent.yaml"
    normalized_squad_name: "{squad_name}"
    agent_source: "dna-backed | specialist-research | domain-research"
    inherited_context:
      dna_bundle_path: "{optional}"
      research_artifacts: ["optional artifacts"]
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] `pack_name` e `squad_name` são reconciliados corretamente
- [ ] A criação real do agente é roteada para `wf-research-then-create-agent.yaml`
- [ ] DNA, research e handoffs upstream do pro continuam preservados
- [ ] Não existe segunda implementação monolítica de `create-agent` no pack
- [ ] Chamadores como `wf-clone-mind` e `wf-mind-research-loop` continuam compatíveis

---

## Veto Conditions

- `squad-creator-pro` tentar reimplementar localmente as fases de research, extraction ou quality gate
- `squad_name` e `pack_name` apontarem para squads diferentes
- `workflows/wf-research-then-create-agent.yaml` não existir
- Algum chamador esperar uma fase antiga que agora pertence ao workflow canônico do pro

---

## Related Documents

- `workflows/wf-research-then-create-agent.yaml` -- owner canônico
- `workflows/wf-clone-mind.yaml` -- upstream de DNA clonado
- `workflows/wf-mind-research-loop.yaml` -- upstream de seleção de especialistas
- `tasks/create-task.md` -- downstream delegado ao pipeline atômico do base
- `squads/squad-creator/tasks/create-agent.md` -- owner canônico do fluxo base não research-first

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed create-agent output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
