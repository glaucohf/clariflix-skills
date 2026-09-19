---
task: slides()
responsavel: "Slides"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "QBR Brief validado pelo Critic Verity + template de deck da empresa (Google Slides ou PPTX template armazenado no drive corporativo) + logo e dados da conta do CRM + preferencias de deck por segmento (numero de slides, nivel de detalhe) + historico de decks anteriores da conta para manter consistencia visual"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Deck de QBR gerado e salvo no Google Drive (ou SharePoint) na pasta do CSM responsavel, com link compartilhavel"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Notificacao Slack para o CSM com link direto ao deck e ao brief original no ClickUp"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Log de geracao no Supabase com conta, CSM, data de geracao, link do deck e versao do brief utilizado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro apos Briefer entregar o QBR Brief aprovado pelo Verity para conta com renovacao em janela <= 60 dias; acionado sob demanda quando CSM solicita deck via ClickUp para reuniao ad-h…"
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

# Gerar Deck De Apresentacao

**Task ID:** `slides()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Deck De Apresentacao |
| **status** | `pending` |
| **responsible_executor** | Slides (Slides — Agente de Deck de QBR) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Converte o QBR Brief gerado pelo Briefer em um deck de apresentacao estruturado e visualmente coerente, pronto para ser usado pelo CSM na reuniao sem necessidade de edicao manual. Recebe o brief em markdown e gera via API (Google Slides ou PowerPoint via Microsoft Graph) um deck padronizado com o template visual da empresa. Estrutura padrao do deck: (1) Slide de capa com nome da conta, data e nome do CSM; (2) Slide de agenda; (3) Slide de 'Seu resultado no trimestre' com as 3-5 metricas de valor mais relevantes para o segmento; (4) Slide de adocao — grafico de uso com comparativo trimestral; (5) Slide de marcos entregues — timeline visual; (6) Slide de 'O que esta funcionando' — sinais positivos; (7) Slide de proximo trimestre — roadmap e compromissos; (8) Slide de expansao (se aplicavel) — oportunidade qualificada pelo Scout com visual simples; (9) Slide de proximos passos com campos editaveis. Garante que nenhum dado ficticio seja incluído — cada numero no deck e rastreavel ao brief validado pelo Verity.

## Input

- QBR Brief validado pelo Critic Verity + template de deck da empresa (Google Slides ou PPTX template armazenado no drive corporativo) + logo e dados da conta do CRM + preferencias de deck por segmento (numero de slides, nivel de detalhe) + historico de decks anteriores da conta para manter consistencia visual

## Output

- Deck de QBR gerado e salvo no Google Drive (ou SharePoint) na pasta do CSM responsavel, com link compartilhavel
- Notificacao Slack para o CSM com link direto ao deck e ao brief original no ClickUp
- Log de geracao no Supabase com conta, CSM, data de geracao, link do deck e versao do brief utilizado

## Trigger

Acionado pelo Maestro apos Briefer entregar o QBR Brief aprovado pelo Verity para conta com renovacao em janela <= 60 dias; acionado sob demanda quando CSM solicita deck via ClickUp para reuniao ad-hoc

## Knowledge base (o que o executor consulta)

- Templates de deck por segmento e por tipo de reuniao (QBR, Renewal Review, Expansion Pitch) armazenados no Google Drive
- especificacoes de layout por tipo de slide (campos de dados, posicoes, formatacao condicional para metricas positivas/negativas)
- mapeamento de metricas por segmento (quais graficos cada perfil de decisor valoriza)
- credenciais de API do Google Slides / Microsoft Graph
- pasta de destino por CSM no Drive

## Action Items

1. Confirmar o gatilho e carregar a entrada (QBR Brief validado pelo Critic Verity + template de deck da empresa (Google Slides ou PPTX template armazenado no drive…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Deck de QBR gerado e salvo no Google Drive (ou SharePoint) na pasta do CSM responsavel, com link compartilhavel) e persistir no artefato do squad.
4. Entregar ao critic Verity; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Deck de QBR gerado e salvo no Google Drive (ou SharePoint) na pasta do CSM responsavel, com link compartilhavel
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

- **to:** Pulse
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
