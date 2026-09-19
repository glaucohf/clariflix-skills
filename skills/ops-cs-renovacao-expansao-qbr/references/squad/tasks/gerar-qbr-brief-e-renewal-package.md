---
task: briefer()
responsavel: "Briefer"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Renewal Readiness Score com breakdown do Compass + Expansion Signal Report do Scout + sinais brutos do Radar + dados completos do CRM (historico de QBRs, notas do CSM, compromissos, interacoes, executive sponsor) + dados de uso da plataforma de produto (90 dias, com comparativo) + NPS/CSAT/verbatims dos ultimos 90 dias + historico de tickets e resolucoes do helpdesk + base de QBRs anteriores da conta (se existir)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "QBR Brief em markdown estruturado (max 600 palavras) com secoes: Resumo Executivo de Valor, Metricas de Adocao, Marcos Entregues, Status de Compromissos Anteriores, Pontos de Tensao, Agenda Proposta"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Renewal Package em markdown com: Renewal Readiness Score interpretado, Top-5 Evidencias de ROI, Proposta de Expansao (se aplicavel), Objecoes e Respostas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Ambos armazenados no Supabase e entregues ao Slides para geracao do deck e ao Pulse para criacao de task no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro para toda conta com Renewal Readiness Score calculado e renovacao em janela (< 90 dias) ou com Expansion Signal Report com oportunidade qualificada de alto valor; acionado sob d…"
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

# Gerar Qbr Brief E Renewal Package

**Task ID:** `briefer()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Qbr Brief E Renewal Package |
| **status** | `pending` |
| **responsible_executor** | Briefer (Briefer — Gerador de QBR Brief e Renewal Package) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Cerebro de geracao de conteudo do squad: agrega todos os dados disponíveis (score do Compass, relatorio do Scout, dados brutos do Radar, historico do CRM e verbatims de sentimento) para gerar dois artefatos por conta: (A) QBR BRIEF — documento de preparacao para o CSM conduzir a reuniao de QBR, contendo: resumo executivo de valor entregue no trimestre (uso, outcomes, marcos), metricas de adocao com comparativo vs trimestre anterior, problemas resolvidos com impacto calculado, compromissos do fornecedor no trimestre anterior e seu status (entregue/pendente), agenda proposta de QBR com tempo por topico, pontos de tensao previstos baseados em sentimento e tickets recentes, e materiais de apoio sugeridos. (B) RENEWAL PACKAGE — material para a conversa de renovacao contendo: Renewal Readiness Score com breakdown e interpretacao, evidencias de ROI documentado em linguagem do decisor, comparativo de uso atual vs periodo anterior, benchmark anonimizado do setor (conta esta acima/abaixo da media?), proposta de renovacao ou expansao embasada nos sinais do Scout, respostas preparadas para objecoes previstas. Usa RAG sobre historico de QBRs anteriores da conta e sobre exemplos de briefs bem-avaliados pelos CSMs.

## Input

- Renewal Readiness Score com breakdown do Compass + Expansion Signal Report do Scout + sinais brutos do Radar + dados completos do CRM (historico de QBRs, notas do CSM, compromissos, interacoes, executive sponsor) + dados de uso da plataforma de produto (90 dias, com comparativo) + NPS/CSAT/verbatims dos ultimos 90 dias + historico de tickets e resolucoes do helpdesk + base de QBRs anteriores da conta (se existir)

## Output

- QBR Brief em markdown estruturado (max 600 palavras) com secoes: Resumo Executivo de Valor, Metricas de Adocao, Marcos Entregues, Status de Compromissos Anteriores, Pontos de Tensao, Agenda Proposta
- Renewal Package em markdown com: Renewal Readiness Score interpretado, Top-5 Evidencias de ROI, Proposta de Expansao (se aplicavel), Objecoes e Respostas
- Ambos armazenados no Supabase e entregues ao Slides para geracao do deck e ao Pulse para criacao de task no ClickUp

## Trigger

Acionado pelo Maestro para toda conta com Renewal Readiness Score calculado e renovacao em janela (< 90 dias) ou com Expansion Signal Report com oportunidade qualificada de alto valor; acionado sob demanda por CSM via ClickUp para preparacao de QBR ad-hoc; acionado automaticamente 45 dias antes de cada data de renovacao mesmo sem sinais criticos

## Knowledge base (o que o executor consulta)

- Templates de QBR Brief e Renewal Package por segmento (SMB/Mid/Enterprise) e por tipo de produto
- historico de QBRs anteriores por conta (notas, agenda, outcomes
- carregados do CRM e de arquivos de documentacao)
- exemplos de briefs de alta qualidade avaliados positivamente pelos CSMs (few-shot para geracao)
- base de ROI calculado e outcomes documentados por conta (CRM: notas, calls, emails)
- benchmark anonimizado de metricas de uso por setor e cohort (para comparativo no brief)
- catálogo de objecoes comuns de renovacao e expansao com respostas validadas pela equipe comercial

## Action Items

1. Confirmar o gatilho e carregar a entrada (Renewal Readiness Score com breakdown do Compass + Expansion Signal Report do Scout + sinais brutos do Radar + dados co…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (QBR Brief em markdown estruturado (max 600 palavras) com secoes: Resumo Executivo de Valor, Metricas de Adocao, Marcos…) e persistir no artefato do squad.
4. Entregar ao critic Verity; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: QBR Brief em markdown estruturado (max 600 palavras) com secoes: Resumo Executivo de Valor, Metricas de Adocao, Marcos Entregues, Status de Compromissos Anteri…
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

- **to:** Slides
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
