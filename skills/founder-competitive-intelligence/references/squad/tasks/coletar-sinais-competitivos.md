---
task: hawk()
responsavel: "Hawk"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Competitive Map validado (lista de concorrentes Tier 1/2/3 com todos os URLs e identificadores de plataforma por fonte), critérios de monitoramento por concorrente e por fonte configurados por Atlas (frequência de varredura, threshold de mudança para sinalizar), snapshots anteriores de páginas monitoradas para cálculo de diff, credenciais de acesso via MCP a APIs e scrapers configurados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Feed diario de sinais novos detectados (JSON estruturado por concorrente: fonte, timestamp de deteccao, tipo de mudanca, dados brutos"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "texto anterior vs"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "atual para diffs de preco/pagina, job posting completo extraido, post ou review novo com URL, rodada de captacao com valor e investidor), Competitive Activity Index semanal por concorrente com variacao versus semana anterior, Burst Alert quando concorrente Tier 1 gera 3+ sinais de alta relevancia em 48h (sinal de campanha, lancamento ou evento strategico), snapshot semanal completo de estado de todos os Tier 1 para baseline de Lynx"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diário automático (páginas de preço e job postings Tier 1 a cada 6h, LinkedIn e blog a cada 12h, Crunchbase e Product Hunt a cada 24h, Tier 2 a cada 48h, Tier 3 semanal); Burst Alert quando 3+ s…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Veritas 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento por concorrente, critérios de alerta por categoria de movimento e janela de reação por tipo antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação e a sensibilidade dos alertas)"
    - "[ ] HITL: Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atual e as restrições reais do negócio capturados por Atlas para alimentar o Wargame Engine — sem calibração, as contra-jogadas de Ares são genéricas (L3, input crítico que define qualidade das recomendações)"
    - "[ ] HITL: Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirma se as classificações de movimento fazem sentido para o contexto real do mercado e calibra thresholds de scoring de Lynx (L3, calibração crítica antes de produção)"
    - "[ ] HITL: Aprovação de Competitive Flash antes de Counter-Play urgente (score >= 9 em Tier 1) — quando Hermes recebe sinal CRÍTICO aprovado por Veritás, o founder deve confirmar ciência e decisão antes de qualquer ação irreversível ser executada (L3, irreversível por natureza — resposta competitiva errada pode ser pior que nenhuma resposta)"
    - "[ ] HITL: Revisão mensal do Competitive Landscape Report — founder revisa com Atlas o cenário competitivo do mês, valida os cenários de wargame de Ares para os próximos 90 dias, aprova os playbooks de resposta como diretriz estratégica e ajusta os critérios de alerta do Competitive Map se necessário (L3, governança estratégica mensal obrigatória)"
---

# Coletar Sinais Competitivos

**Task ID:** `hawk()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Inteligência Competitiva Contínua

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coletar Sinais Competitivos |
| **status** | `pending` |
| **responsible_executor** | Hawk (Hawk — Competitive Signal Collector) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Motor de vigilância 24/7 de todos os pontos de presença digital dos concorrentes monitorados. Responsável pela coleta estruturada e contínua de sinais brutos de múltiplas fontes sem interpretação — seu trabalho é coletar e detectar mudanças com precisão, não interpretar. Opera em três camadas: (1) PRICING LAYER — varredura diária das páginas de preço de todos os Tier 1 com diff automático (detecta qualquer mudança de valor, estrutura de tier, adição ou remoção de plano, mudança de garantia ou política de trial) via scraping estruturado; (2) TALENT LAYER — monitoramento diário de LinkedIn Company Pages dos concorrentes para crescimento de headcount, novas job postings publicadas com extração de título, departamento, senioridade e descrição (padrões de hiring revelam onde o concorrente está investindo), e perfis de fundadores/C-level para posts e atividades relevantes; (3) SIGNAL LAYER — monitoramento de fontes de inteligência pública: Crunchbase para rodadas e valuations, Product Hunt para launches, G2/Capterra para novas reviews com delta de rating, blogs estratégicos e newsletters com detecção de novos posts, X e LinkedIn dos fundadores para sinais públicos de estratégia. Calcula Competitive Activity Index por concorrente (volume e velocidade de sinais novos na semana) para Lynx priorizar análise.

## Input

- Competitive Map validado (lista de concorrentes Tier 1/2/3 com todos os URLs e identificadores de plataforma por fonte), critérios de monitoramento por concorrente e por fonte configurados por Atlas (frequência de varredura, threshold de mudança para sinalizar), snapshots anteriores de páginas monitoradas para cálculo de diff, credenciais de acesso via MCP a APIs e scrapers configurados

## Output

- Feed diario de sinais novos detectados (JSON estruturado por concorrente: fonte, timestamp de deteccao, tipo de mudanca, dados brutos
- texto anterior vs
- atual para diffs de preco/pagina, job posting completo extraido, post ou review novo com URL, rodada de captacao com valor e investidor), Competitive Activity Index semanal por concorrente com variacao versus semana anterior, Burst Alert quando concorrente Tier 1 gera 3+ sinais de alta relevancia em 48h (sinal de campanha, lancamento ou evento strategico), snapshot semanal completo de estado de todos os Tier 1 para baseline de Lynx

## Trigger

Cron diário automático (páginas de preço e job postings Tier 1 a cada 6h, LinkedIn e blog a cada 12h, Crunchbase e Product Hunt a cada 24h, Tier 2 a cada 48h, Tier 3 semanal); Burst Alert quando 3+ sinais de Tier 1 em 48h; Atlas solicita varredura emergencial para concorrente específico; novo concorrente adicionado ao Competitive Map (setup inicial de todas as fontes); gate HITL de revisão mensal do Competitive Map que ajusta frequências

## Knowledge base (o que o executor consulta)

- Competitive Map completo com todos os identificadores por plataforma (URLs de páginas de preço, LinkedIn Company Page IDs, Crunchbase slugs, handles de fundadores, RSS feeds de blogs, perfis de review sites), snapshots históricos das últimas 12 semanas por fonte e concorrente para cálculo de diff e detecção de padrões de mudança sazonais, calendário de sazonalidade do setor para distinguir bursts esperados de anomalias reais, mapeamento de fontes prioritárias por tipo de concorrente (SaaS vs serviço vs marketplace tem padrões de sinal diferentes)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Competitive Map validado (lista de concorrentes Tier 1/2/3 com todos os URLs e identificadores de plataforma por fonte)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Feed diario de sinais novos detectados (JSON estruturado por concorrente: fonte, timestamp de deteccao, tipo de mudanca…) e persistir no artefato do squad.
4. Entregar ao critic Veritas 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Feed diario de sinais novos detectados (JSON estruturado por concorrente: fonte, timestamp de deteccao, tipo de mudanca, dados brutos
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Veritas 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento po…
- [ ] Gate HITL respeitado: Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atu…
- [ ] Gate HITL respeitado: Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirm…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento por concorrente, crité… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atual e as restrições r… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirma se as classificaçõ… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação de Competitive Flash antes de Counter-Play urgente (score >= 9 em Tier 1) — quando Hermes recebe sinal CRÍTICO aprovado por Veritás, o founder deve c… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão mensal do Competitive Landscape Report — founder revisa com Atlas o cenário competitivo do mês, valida os cenários de wargame de Ares para os próximos… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação pré-distribuição de Board Intelligence Pack e Decision Intelligence Brief de Memo — qualquer documento de Memo deve ser revisado e aprovado pelo foun… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibracao trimestral de scoring de Lynx — founder revisa junto com Atlas e Veritas os falsos positivos e falsos negativos dos ultimos 90 dias, ajusta os pesos… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Quando Veritas retorna BLOCKED em gate de rastreabilidade ou hipótese inflatada — revisão obrigatória do founder antes de reprocessamento ou descarte do item,… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Veritas 2 | BLOQUEIA entrega |

## Handoff

- **to:** Lynx
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
