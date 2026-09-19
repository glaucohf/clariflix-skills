---
task: bolt()
responsavel: "Bolt"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Playbook selecionado por Nexus com tipo de sinal e contexto da conta, guidelines de brand voice e tom, templates de copy aprovados por categoria de playbook, histórico de copies com melhor CTR por segmento de ICP, restrições de compliance (Sigma checklist)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Copy de ad (headline + body + CTA) para aprovação, script de email de outreach personalizado com sinal como abertura, rascunho de post de LinkedIn com ângulo do macro-trend detectado por Vortex, variantes de criativo para teste A/B (mínimo 3 variações por asset), todo conteúdo em formato de rascunho pendente aprovação de Sigma antes de publicar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Nexus dispara Demand Surge Playbook ou Competitive Review Playbook (urgência alta = 2h SLA); Radar solicita conteúdo para campanha de retargeting de segmento aquecido; ciclo semanal de conteúdo basea…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sigma 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)"
    - "[ ] HITL: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)"
    - "[ ] HITL: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)"
    - "[ ] HITL: Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)"
    - "[ ] HITL: Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)"
---

# Gerar Anúncio Específico

**Task ID:** `bolt()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Anúncio Específico |
| **status** | `pending` |
| **responsible_executor** | Bolt (Bolt — Content & Copy Activation Agent) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gera o conteúdo e copy ativados pelos playbooks disparados por Nexus. Opera em modo reativo-rápido: quando um Demand Surge Playbook é ativado, Bolt produz em menos de 2h o anúncio específico para o segmento que demonstrou sinal de busca, o post de LinkedIn com ângulo educativo sobre o problema detectado, e o email de outreach personalizado com o contexto do sinal. Não é um copywriter generativo — e um ativador de conteúdo contextual: usa a evidência do sinal como gancho narrativo. Referência direta ao 'copy/ads/conteúdo/análise' do board.

## Input

- Playbook selecionado por Nexus com tipo de sinal e contexto da conta, guidelines de brand voice e tom, templates de copy aprovados por categoria de playbook, histórico de copies com melhor CTR por segmento de ICP, restrições de compliance (Sigma checklist)

## Output

- Copy de ad (headline + body + CTA) para aprovação, script de email de outreach personalizado com sinal como abertura, rascunho de post de LinkedIn com ângulo do macro-trend detectado por Vortex, variantes de criativo para teste A/B (mínimo 3 variações por asset), todo conteúdo em formato de rascunho pendente aprovação de Sigma antes de publicar

## Trigger

Nexus dispara Demand Surge Playbook ou Competitive Review Playbook (urgência alta = 2h SLA); Radar solicita conteúdo para campanha de retargeting de segmento aquecido; ciclo semanal de conteúdo baseado em Macro-Trend Report de Vortex; HITL aprova campanha paga e precisa de copies para teste

## Knowledge base (o que o executor consulta)

- Guidelines completos de brand voice e tom da empresa, biblioteca de copies históricos com performance (CTR, conversão) por segmento e tipo de sinal, templates aprovados por categoria de playbook, restrições legais e de compliance por canal (LGPD para email, políticas Meta/Google para ads), cases de copies que converteram em contextos similares de sinal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Playbook selecionado por Nexus com tipo de sinal e contexto da conta, guidelines de brand voice e tom, templates de cop…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Copy de ad (headline + body + CTA) para aprovação, script de email de outreach personalizado com sinal como abertura, r…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Copy de ad (headline + body + CTA) para aprovação, script de email de outreach personalizado com sinal como abertura, rascunho de post de LinkedIn com ângulo d…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sigma 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o…
- [ ] Gate HITL respeitado: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cad…
- [ ] Gate HITL respeitado: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squ… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprova… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3) | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Sigma
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
