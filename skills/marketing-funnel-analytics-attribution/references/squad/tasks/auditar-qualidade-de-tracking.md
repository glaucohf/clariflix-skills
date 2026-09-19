---
task: lumen()
responsavel: "Lumen"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de campanhas ativas com URLs de destino (do Google Ads, Meta Ads, LinkedIn), sample de URLs sendo compartilhadas em canais orgânicos (Slack/email capturado via MCP), eventos de GA4/Segment das últimas 24h, histórico de UTM patterns aprovados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório diário de UTM Health Score (0-100) com lista de URLs sem UTM ou com UTM malformado, match rate entre conversões GA4 e CRM (%), alertas de campanha bloqueada (requer aprovação L3) com causa específica, sugestões de UTM correto para cada caso detectado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Em modo de auditoria: relatório completo de coverage por canal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Pré-lançamento de qualquer campanha (gate obrigatório antes de ir ao ar); schedule diário as 7h para auditoria de campanhas ativas; quando Coverage Score do Hermes cai abaixo de 85%; quando Nexus det…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Skeptic antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar ou corrigir antes do go-live. SLA: 30min para resposta, após isso o sistema notifica o gestor direto."
    - "[ ] L3: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor de media antes de execucao. O squad gera o racional completo, humano aprova ou rejeita com comentario."
    - "[ ] L3: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing de 5 linhas e aguarda confirmação de que foi visto (acknowledgment) antes de escalar para investigação automática mais profunda."
    - "[ ] L2: Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta. Previne drift de sensibilidade ao longo do tempo."
    - "[ ] L2: Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP de Marketing. Revisão trimestral."
---

# Auditar Qualidade De Tracking

**Task ID:** `lumen()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Funnel Analytics & Attribution Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Auditar Qualidade De Tracking |
| **status** | `pending` |
| **responsible_executor** | Lumen (Lúmen — Agente de Qualidade de Tracking e UTM) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de higiene de dados. Audita continuamente a qualidade do tracking: verifica se todas as campanhas ativas têm UTMs completos e padronizados, detecta URLs sem UTM sendo compartilhadas, identifica tráfego direto suspeito (que na verdade é dark social ou UTM quebrado), valida eventos de conversão no GA4/Segment contra o CRM (match rate) e gera score de saúde de tracking. Bloqueia lançamento de campanha se UTM checker falhar (gate L3 — requer aprovação humana para sobrescrever).

## Input

- Lista de campanhas ativas com URLs de destino (do Google Ads, Meta Ads, LinkedIn), sample de URLs sendo compartilhadas em canais orgânicos (Slack/email capturado via MCP), eventos de GA4/Segment das últimas 24h, histórico de UTM patterns aprovados

## Output

- Relatório diário de UTM Health Score (0-100) com lista de URLs sem UTM ou com UTM malformado, match rate entre conversões GA4 e CRM (%), alertas de campanha bloqueada (requer aprovação L3) com causa específica, sugestões de UTM correto para cada caso detectado
- Em modo de auditoria: relatório completo de coverage por canal

## Trigger

Pré-lançamento de qualquer campanha (gate obrigatório antes de ir ao ar); schedule diário as 7h para auditoria de campanhas ativas; quando Coverage Score do Hermes cai abaixo de 85%; quando Nexus detecta spike de tráfego 'direct' inexplicável (>15% acima do baseline).

## Knowledge base (o que o executor consulta)

- Taxonomia de UTM aprovada da empresa (source/medium/campaign naming conventions), lista de campanhas ativas e URLs de destino aprovadas, histórico de UTM patterns por canal, regras de validação de UTM (quais campos são obrigatórios por canal), mapeamento de IDs de conversão GA4 para etapas do CRM

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de campanhas ativas com URLs de destino (do Google Ads, Meta Ads, LinkedIn), sample de URLs sendo compartilhadas…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório diário de UTM Health Score (0-100) com lista de URLs sem UTM ou com UTM malformado, match rate entre conversõ…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório diário de UTM Health Score (0-100) com lista de URLs sem UTM ou com UTM malformado, match rate entre conversões GA4 e CRM (%), alertas de campanha bl…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Skeptic registrado
- [ ] Gate L3 respeitado: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de cam…
- [ ] Gate L3 respeitado: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovaca…
- [ ] Gate L3 respeitado: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor d… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta.… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão de relatório executivo antes de envio ao board: Oracle gera, Skeptic valida, mas um humano (CMO ou analista sênior) faz leitura final antes de envio ao… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Skeptic | BLOQUEIA entrega |

## Handoff

- **to:** Oracle
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
