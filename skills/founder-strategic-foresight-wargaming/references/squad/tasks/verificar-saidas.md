---
task: ajaxVerificar()
responsavel: "Ajax"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificação de stakes, estimativa de custo de tokens). Para decisões classificadas como Alto (R$100k-500k) ou Crítico (R$500k+), aprovação explícita do founder é obrigatória antes de disparar workers. Inclui confirmação do escopo, dos concorrentes a simular e do nível de profundidade desejado."
    - "[ ] HITL: PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e founder recebe notificação urgente com evidências contrárias. O founder deve decidir: (a) revisar a tese antes de prosseguir, (b) validar a premissa com dado adicional, ou (c) aceitar o risco explicitamente e autorizar o prosseguimento. Sem aprovação explícita, Atlas não gera recomendação de GO."
    - "[ ] HITL: PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloqueia automaticamente a recomendação de GO e escalona para o founder. O relatório apresenta: narrativa do caminho de falha, premissas que o geram e opções de mitigação. O founder deve responder com ação concreta (mitigar, aceitar, desistir) antes de qualquer recomendação final."
    - "[ ] HITL: BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento gerado vai primeiro para Notion como draft. Somente após founder marcar como aprovado o envio é permitido. Este gate é inviolável e não pode ser desabilitado."
    - "[ ] HITL: WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades financeiras ou decisões internas), o output é marcado como confidencial e apresentado ao founder antes de ser incluído em qualquer documento compartilhável. Dados de origem não-verificada são explicitamente rotulados."
---

# Verificar Saídas do Strategic Foresight & Wargaming

**Task ID:** `ajaxVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Strategic Foresight & Wargaming |
| **status** | `pending` |
| **responsible_executor** | Ajax (Ajax — O Crítico de Guerra) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Ajax — O Crítico de Guerra — Ajax é o agente critic/red-team do squad. Executa verificação adversarial em quatro camadas após os três workers (Cassandra, Brutus, Chisel) concluírem: (1) CONSISTÊNCIA CRUZADA — verifica se as reações dos adversários (Brutus) são coerentes com os cenários gerados (Cassandra) e com as premissas estressadas (Chisel); inconsistências são sinalizadas e retornam para retrabalho. (2) PRE-MORTEM ESTRUTURADO — assume que a decisão falhou em 12 meses e constrói a narrativa causal mais plausível com base nos outputs dos workers; força o squad a encarar a falha antes que ela aconteça. (3) COBERTURA DE PREMISSAS — verifica se todas as premissas críticas da Árvore receberam stress-test do Chisel; premissas não cobertas são retornadas como gap. (4) TESTE DE ROBUSTEZ — verifica se a recomendação de GO/NO-GO ainda se sustenta se as 2 premissas mais frágeis falharem simultaneamente. Se Pre-Mortem revelar caminho de falha com probabilidade > 30%, bloqueia recomendação de GO e escalona para HITL gate obrigatório.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- O Crítico de Guerra
- Ajax é o agente critic/red-team do squad
- Executa verificação adversarial em quatro camadas após os três workers (Cassandra, Brutus, Chisel) concluírem: (1) CONSISTÊNCIA CRUZADA
- verifica se as reações dos adversários (Brutus) são coerentes com os cenários gerados (Cassandra) e com as premissas estressadas (Chisel)
- inconsistências são sinalizadas e retornam para retrabalho
- (2) PRE-MORTEM ESTRUTURADO
- assume que a decisão falhou em 12 meses e constrói a narrativa causal mais plausível com base nos outputs dos workers
- força o squad a encarar a falha antes que ela aconteça
- (3) COBERTURA DE PREMISSAS
- verifica se todas as premissas críticas da Árvore receberam stress-test do Chisel
- premissas não cobertas são retornadas como gap
- (4) TESTE DE ROBUSTEZ
- verifica se a recomendação de GO/NO-GO ainda se sustenta se as 2 premissas mais frágeis falharem simultaneamente
- Se Pre-Mortem revelar caminho de falha com probabilidade > 30%, bloqueia recomendação de GO e escalona para HITL gate obrigatório

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Atlas para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Pr…
- [ ] Gate HITL respeitado: PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o war…
- [ ] Gate HITL respeitado: PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificaç… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e found… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloque… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades fi… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — DECISÃO DE MONITORAMENTO CONTÍNUO (L2): Após wargaming concluído, Atlas apresenta lista de tripwires sugeridos para aprovação do founder antes de ativar Tripwi… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Ajax | BLOQUEIA entrega |

## Handoff

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
