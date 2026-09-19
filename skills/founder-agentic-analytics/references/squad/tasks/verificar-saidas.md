---
task: sqlSemanticVerifierVerificar()
responsavel: "SQL & Semantic Verifier"
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
    - "[ ] HITL: Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível pois altera definições que afetam todas as queries futuras)"
    - "[ ] HITL: Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a oficial — L3)"
    - "[ ] HITL: Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no setup inicial, L2 depois)"
    - "[ ] HITL: Confirmação de decisão tomada com base em dados para o Clío registrar (founder confirma que vai agir — não é automático para evitar log de decisões não tomadas)"
    - "[ ] HITL: Acesso a novas fontes de dados não mapeadas (conectar novo banco, nova planilha, nova API ao schema — L3 por impacto na governança)"
---

# Verificar Saídas do Ágentic Analytics

**Task ID:** `sqlSemanticVerifierVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Ágentic Analytics (Pergunte aos Seus Dados)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Ágentic Analytics |
| **status** | `pending` |
| **responsible_executor** | SQL & Semantic Verifier (Themis (SQL & Semantic Verifier)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Themis (SQL & Semantic Verifier) — Valida toda resposta antes de ser entregue ao founder. Verifica: (1) o SQL gerado esta correto e nao ha risco de retornar dado errado por join incorreto ou filtro invertido; (2) a metrica consultada esta sendo usada conforme sua definicao formal no schema semantico (sem reinterpretacao); (3) a interpretacao narrativa e consistente com os numeros apresentados; (4) nao ha alucinacao — todo numero na resposta e rastreavel a uma linha do resultado da query; (5) o nivel de confianca declarado e justo. Se encontrar problema, devolve para o worker responsavel com feedback especifico antes de liberar para o founder.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Themis (SQL & Semantic Verifier)
- Valida toda resposta antes de ser entregue ao founder
- Verifica: (1) o SQL gerado esta correto e nao ha risco de retornar dado errado por join incorreto ou filtro invertido
- (2) a metrica consultada esta sendo usada conforme sua definicao formal no schema semantico (sem reinterpretacao)
- (3) a interpretacao narrativa e consistente com os numeros apresentados
- (4) nao ha alucinacao
- todo numero na resposta e rastreavel a uma linha do resultado da query
- (5) o nivel de confianca declarado e justo
- Se encontrar problema, devolve para o worker responsavel com feedback especifico antes de liberar para o founder

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Orquestrador Analítico para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível…
- [ ] Gate HITL respeitado: Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a o…
- [ ] Gate HITL respeitado: Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível pois altera definiç… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a oficial — L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no setup inicial, L2 d… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Confirmação de decisão tomada com base em dados para o Clío registrar (founder confirma que vai agir — não é automático para evitar log de decisões não tomadas) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Acesso a novas fontes de dados não mapeadas (conectar novo banco, nova planilha, nova API ao schema — L3 por impacto na governança) | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic SQL & Semantic Verifier | BLOQUEIA entrega |

## Handoff

- **to:** Orquestrador Analítico
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
