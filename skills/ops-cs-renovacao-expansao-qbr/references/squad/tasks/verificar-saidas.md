---
task: verityVerificar()
responsavel: "Verity"
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
    - "[ ] HITL: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de expansao com status 'Aguardando Aprovacao do CSM/Manager' antes de incluir a proposta no deck final para o cliente"
    - "[ ] HITL: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CSM (deck e gerado, nunca enviado automaticamente ao cliente)"
    - "[ ] HITL: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar qualquer contato de renovacao"
    - "[ ] HITL: Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de entrada antes de reprocessar"
    - "[ ] HITL: Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer alinhamento com equipe comercial (AE ou CSM sênior) antes de abordar o cliente"
---

# Verificar Saídas do Renovacao, Expansao e QBR Automatizado

**Task ID:** `verityVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Renovacao, Expansao e QBR Automatizado |
| **status** | `pending` |
| **responsible_executor** | Verity (Verity — Critic de Evidencia e Proporcionalidade) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Verity — Critic de Evidencia e Proporcionalidade — Valida todos os artefatos gerados pelo squad antes de qualquer disparo externo (criacao de task no ClickUp, envio de notificacao, geracao de deck) em tres dimensoes: (A) INTEGRIDADE DE DADOS — cada numero, metrica ou afirmacao no brief tem uma fonte rastreavel no Supabase ou no CRM; nenhum dado foi interpolado, estimado sem base ou inventado; campos faltantes sao sinalizados como 'dado nao disponivel' em vez de omitidos silenciosamente. (B) PROPORCIONALIDADE — a urgencia e o tipo de acao recomendada sao proporcionais ao Renewal Readiness Score e ao MRR da conta: nao recomenda reuniao de executive sponsor para conta SMB de baixo MRR; nao gera deck completo de 12 slides para renovacao de R$5k; nao sinaliza oportunidade de expansao para conta que usa menos de 60% do tier atual. (C) COMPLETUDE PARA ACAO — o CSM pode entrar na reuniao ou fazer o contato de renovacao usando apenas o brief, sem precisar buscar informacao adicional; agenda proposta esta completa com tempos; objecoes previstas tem resposta pronta; proximos passos estao claros. Score de aprovacao: minimo 36/40 (9/10 em cada dimensao). Abaixo do threshold: devolve ao Briefer com feedback especifico por dimensao. Maximo de 2 iteracoes antes de escalar para humano. Tambem valida o Renewal Readiness Score do Compass: score nao pode variar mais de 20 pontos em 48h sem evento documentado (protecao contra anomalia de dados de entrada).

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Critic de Evidencia e Proporcionalidade
- Valida todos os artefatos gerados pelo squad antes de qualquer disparo externo (criacao de task no ClickUp, envio de notificacao, geracao de deck) em tres dimensoes: (A) INTEGRIDADE DE DADOS
- cada numero, metrica ou afirmacao no brief tem uma fonte rastreavel no Supabase ou no CRM
- nenhum dado foi interpolado, estimado sem base ou inventado
- campos faltantes sao sinalizados como 'dado nao disponivel' em vez de omitidos silenciosamente
- (B) PROPORCIONALIDADE
- a urgencia e o tipo de acao recomendada sao proporcionais ao Renewal Readiness Score e ao MRR da conta: nao recomenda reuniao de executive sponsor para conta SMB de baixo MRR
- nao gera deck completo de 12 slides para renovacao de R$5k
- nao sinaliza oportunidade de expansao para conta que usa menos de 60% do tier atual
- (C) COMPLETUDE PARA ACAO
- o CSM pode entrar na reuniao ou fazer o contato de renovacao usando apenas o brief, sem precisar buscar informacao adicional
- agenda proposta esta completa com tempos
- objecoes previstas tem resposta pronta
- proximos passos estao claros
- Score de aprovacao: minimo 36/40 (9/10 em cada dimensao)
- Abaixo do threshold: devolve ao Briefer com feedback especifico por dimensao
- Maximo de 2 iteracoes antes de escalar para humano
- Tambem valida o Renewal Readiness Score do Compass: score nao pode variar mais de 20 pontos em 48h sem evento documentado (protecao contra anomalia de dados de entrada)

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Maestro para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pu…
- [ ] Gate HITL respeitado: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e…
- [ ] Gate HITL respeitado: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS a…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CS… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de ent… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer ali… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Comprometimento pendente do fornecedor detectado pelo Memory como nao entregue no periodo anterior — brief inclui o item mas Pulse cria subtask de 'Resolucao d… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Conta com Renewal Readiness Score CRITICO (< 50) e renovacao em < 30 dias — escalacao imediata para Head de CS e Account Executive senior com brief de situacao… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de Memory indicando que CSM fez edicao significativa no deck (> 30% do conteudo alterado) — Maestro abre HITL para CSM documentar o motivo da edicao e… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Verity | BLOQUEIA entrega |

## Handoff

- **to:** Maestro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
