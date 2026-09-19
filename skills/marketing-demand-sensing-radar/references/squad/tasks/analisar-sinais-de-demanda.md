---
task: vortex()
responsavel: "Vortex"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de clientes de maior LTV para análise retroativa, verticais de mercado a monitorar para tendências, contas Hot identificadas por Pulse que precisam de contexto adicional, briefing de concorrentes para análise de timing de campanha deles"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Buy Signal Fingerprint (perfil de quais combinações de sinais precederam compras históricas), Macro-Trend Report semanal (3-5 tendências com janela de oportunidade estimada em semanas), Competitor Signal Analysis (em que eventos de mercado os concorrentes aceleram campanhas, inferido de análise de ads/content timing), Context Card por conta Hot (1 página com contexto para personalizar abordagem do SDR/outreach)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo semanal automático de Macro-Trend Research; conta atinge status Hot no Pulse (gera Context Card em 2h); Radar solicita análise retroativa de ICP para calibrar fingerprint; novo segmento de merc…"
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

# Analisar Sinais De Demanda

**Task ID:** `vortex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Sinais De Demanda |
| **status** | `pending` |
| **responsible_executor** | Vortex (Vórtex — Market Deep Research Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa deepresearch estruturado para enriquecer o contexto dos sinais detectados por Pulse e identificar macro-tendências antecipadas de demanda. Opera em dois modos: (1) Modo Retroativo — analisa os 20 maiores clientes para identificar padrão de sinais que precedeu a compra deles, construindo o 'fingerprint de compra' do ICP; (2) Modo Prospectivo — pesquisa semanal de tendências setoriais (regulatórias, tecnológicas, competitivas) que criarão demanda nos próximos 60-90 dias antes do mercado reagir. Referência direta ao 'Profiling de PMF -> Deepresearch / Researchs do Alan' do board.

## Input

- Lista de clientes de maior LTV para análise retroativa, verticais de mercado a monitorar para tendências, contas Hot identificadas por Pulse que precisam de contexto adicional, briefing de concorrentes para análise de timing de campanha deles

## Output

- Buy Signal Fingerprint (perfil de quais combinações de sinais precederam compras históricas), Macro-Trend Report semanal (3-5 tendências com janela de oportunidade estimada em semanas), Competitor Signal Analysis (em que eventos de mercado os concorrentes aceleram campanhas, inferido de análise de ads/content timing), Context Card por conta Hot (1 página com contexto para personalizar abordagem do SDR/outreach)

## Trigger

Ciclo semanal automático de Macro-Trend Research; conta atinge status Hot no Pulse (gera Context Card em 2h); Radar solicita análise retroativa de ICP para calibrar fingerprint; novo segmento de mercado identificado com anomalia de sinal

## Knowledge base (o que o executor consulta)

- Base de clientes ganhos com timeline de sinais precedentes (construída no Discovery), relatórios setoriais e regulatórios por vertical do ICP, histórico de campanhas de concorrentes (datas, mensagens, formatos), pesquisas de mercado e earnings calls de empresas do setor, dados de churn com contexto de mercado

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de clientes de maior LTV para análise retroativa, verticais de mercado a monitorar para tendências, contas Hot id…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Buy Signal Fingerprint (perfil de quais combinações de sinais precederam compras históricas), Macro-Trend Report semana…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Buy Signal Fingerprint (perfil de quais combinações de sinais precederam compras históricas), Macro-Trend Report semanal (3-5 tendências com janela de oportuni…
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
