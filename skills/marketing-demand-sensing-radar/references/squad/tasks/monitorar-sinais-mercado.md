---
task: pulse()
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de contas-alvo tier 1/2/3 (ICP validado), Signal Taxonomy Canvas com thresholds por categoria, credenciais de integração via MCP (Clay, Bombora, SEMrush, LinkedIn), janela de tempo de monitoramento por categoria de sinal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Signal Feed diário (JSON estruturado com todas as contas acima do threshold mínimo), Signal Score por conta (0-100 com breakdown por categoria), lista de Hot Accounts (score > 70) com evidence trail de quais sinais dispararam, trending sectors report (quais segmentos estão aquecendo), alertas de anomalia quando conta tier 1 dispara sinal crítico fora do ciclo normal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job de scan automático a cada 6h (cron); webhook de funding round detectado (Crunchbase API); alerta de job posting crítico detectado; Radar solicita scan emergencial para conta específica; revisão s…"
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

# Monitorar Sinais Mercado

**Task ID:** `pulse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais Mercado |
| **status** | `pending` |
| **responsible_executor** | Pulse (Pulse — Signal Intelligence Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Motor de monitoramento contínuo de sinais de mercado e intenção de compra. Agrega feeds de 8+ categorias: (1) Funding rounds e M&A via Crunchbase/PitchBook webhooks, (2) Job postings críticos via scraping estruturado e Clay, (3) Intent data B2B tópico-específico via Bombora/6sense, (4) Atividade em review sites G2/Capterra por produto concorrente, (5) Menções de marca/categoria em ChatGPT, Perplexity e AI Overviews via monitoramento de GEO, (6) Picos de busca orgânica por keyword de problema via SEMrush, (7) Adoção de tecnologia complementar via Technographics (Clay/BuiltWith), (8) Atividade social crítica no LinkedIn (nova liderança, company update estratégico). Calcula Signal Score agregado (0-100) por conta com breakdown por categoria.

## Input

- Lista de contas-alvo tier 1/2/3 (ICP validado), Signal Taxonomy Canvas com thresholds por categoria, credenciais de integração via MCP (Clay, Bombora, SEMrush, LinkedIn), janela de tempo de monitoramento por categoria de sinal

## Output

- Signal Feed diário (JSON estruturado com todas as contas acima do threshold mínimo), Signal Score por conta (0-100 com breakdown por categoria), lista de Hot Accounts (score > 70) com evidence trail de quais sinais dispararam, trending sectors report (quais segmentos estão aquecendo), alertas de anomalia quando conta tier 1 dispara sinal crítico fora do ciclo normal

## Trigger

Job de scan automático a cada 6h (cron); webhook de funding round detectado (Crunchbase API); alerta de job posting crítico detectado; Radar solicita scan emergencial para conta específica; revisão semanal de calibração de baseline

## Knowledge base (o que o executor consulta)

- Lista de contas ICP tier 1/2/3 com atributos firmográficos, Signal Taxonomy Canvas versionado com thresholds por categoria, baseline de ruído por categoria (calibrado nos primeiros 14 dias), histórico de sinais anteriores por conta para detecção de aceleração, mapeamento de job titles críticos por tipo de negócio (ex: 'VP Revenue Operations' = sinal de compra de RevOps tools)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de contas-alvo tier 1/2/3 (ICP validado), Signal Taxonomy Canvas com thresholds por categoria, credenciais de int…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Signal Feed diário (JSON estruturado com todas as contas acima do threshold mínimo), Signal Score por conta (0-100 com…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Signal Feed diário (JSON estruturado com todas as contas acima do threshold mínimo), Signal Score por conta (0-100 com breakdown por categoria), lista de Hot A…
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

- **to:** Vortex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
