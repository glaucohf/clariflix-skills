---
task: scout()
responsavel: "Scout"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinais de expansao do Radar por conta (features usadas, usuarios ativos vs licencas, requests) + dados de uso historico da plataforma de produto (90 dias) + catalogo de produtos e planos com features por tier + historico de expansoes bem-sucedidas e rejeitadas no CRM por segmento e perfil de uso similar + Renewal Readiness Score do Compass (conta saudavel tem mais propensao a expansao)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Expansion Signal Report por conta: (1) oportunidade principal qualificada (tipo: upsell/cross-sell/seat expansion, produto/modulo alvo, MRR incremental estimado)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) evidencias do uso atual que suportam a oportunidade com valores concretos"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) timing recomendado para a conversa com justificativa"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) script de abertura sugerido para o CSM"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(5) objecoes previstas com respostas preparadas"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(6) flag de 'nao-expansion-ready' se conta ainda nao maximizou tier atual"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro em paralelo ao Compass para toda conta com sinais de expansao detectados pelo Radar (score_expansao > 0); acionado sob demanda quando CSM solicita analise de expansao para conta…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Verity antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de expansao com status 'Aguardando Aprovacao do CSM/Manager' antes de incluir a proposta no deck final para o cliente"
    - "[ ] HITL: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CSM (deck e gerado, nunca enviado automaticamente ao cliente)"
    - "[ ] HITL: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar qualquer contato de renovacao"
    - "[ ] HITL: Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de entrada antes de reprocessar"
    - "[ ] HITL: Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer alinhamento com equipe comercial (AE ou CSM sênior) antes de abordar o cliente"
---

# Analisar Propensão a Expansão

**Task ID:** `scout()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Propensão a Expansão |
| **status** | `pending` |
| **responsible_executor** | Scout (Scout — Analista de Propensao a Expansao) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em cruzar sinais de uso com o modelo de propensao a upgrade para identificar e qualificar oportunidades de expansao (upsell e cross-sell) por conta. Para cada conta com sinais detectados pelo Radar, analisa: (1) Qual o proximo plano ou modulo logico para esta conta com base no padrao de uso atual; (2) Quais features do plano superior ja sao usadas ou solicitadas (evidencia de demanda latente); (3) Qual o timing ideal para a conversa de expansao: antes da renovacao (bundle na renovacao), em milestone de sucesso (apos atingir ROI documentado), ou em evento de crescimento (novo time adotando o produto); (4) Qual a estimativa de MRR incremental (ARR de expansao projetado); (5) Qual o risco de rejeicao — contas que nao maximizaram o tier atual tem baixa propensao. Diferencia upsell (upgrade de tier) de cross-sell (modulo adicional) de seat expansion (mais licencas). Gera o Expansion Signal Report com oportunidade qualificada, racional, timing recomendado e objecoes previstas.

## Input

- Sinais de expansao do Radar por conta (features usadas, usuarios ativos vs licencas, requests) + dados de uso historico da plataforma de produto (90 dias) + catalogo de produtos e planos com features por tier + historico de expansoes bem-sucedidas e rejeitadas no CRM por segmento e perfil de uso similar + Renewal Readiness Score do Compass (conta saudavel tem mais propensao a expansao)

## Output

- Expansion Signal Report por conta: (1) oportunidade principal qualificada (tipo: upsell/cross-sell/seat expansion, produto/modulo alvo, MRR incremental estimado)
- (2) evidencias do uso atual que suportam a oportunidade com valores concretos
- (3) timing recomendado para a conversa com justificativa
- (4) script de abertura sugerido para o CSM
- (5) objecoes previstas com respostas preparadas
- (6) flag de 'nao-expansion-ready' se conta ainda nao maximizou tier atual
- com lista de acoes para maximizar adocao antes de propor upgrade
- Persistido no Supabase e entregue ao Briefer para inclusao no QBR Brief

## Trigger

Acionado pelo Maestro em paralelo ao Compass para toda conta com sinais de expansao detectados pelo Radar (score_expansao > 0); acionado sob demanda quando CSM solicita analise de expansao para conta especifica via comando ClickUp

## Knowledge base (o que o executor consulta)

- Catalogo completo de produtos e planos com features por tier e preco (atualizado manualmente a cada nova versao de pricing)
- historico de expansoes realizadas com sinais predecessores e taxa de sucesso por tipo de expansao e segmento
- historico de expansoes rejeitadas com motivos registrados no CRM
- modelo de propensao a expansao calibrado sobre historico (regressao logistica ou scoring por regras)
- dados de uso de features por conta (90 dias)
- playbook de conversa de expansao por tipo de oportunidade e por perfil de decisor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinais de expansao do Radar por conta (features usadas, usuarios ativos vs licencas, requests) + dados de uso historico…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Expansion Signal Report por conta: (1) oportunidade principal qualificada (tipo: upsell/cross-sell/seat expansion, prod…) e persistir no artefato do squad.
4. Entregar ao critic Verity; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Expansion Signal Report por conta: (1) oportunidade principal qualificada (tipo: upsell/cross-sell/seat expansion, produto/modulo alvo, MRR incremental estimad…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Verity registrado
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

- **to:** Briefer
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
