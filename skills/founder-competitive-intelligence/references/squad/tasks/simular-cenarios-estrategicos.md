---
task: ares()
responsavel: "Ares"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal classificado por Lynx com contexto estratégico (para Reactive Mode), Movement Profile atualizado de todos os Tier 1 (para Wargame Mode), Corpus do Founder (frameworks, histórico de decisões estratégicas, posicionamento atual, recursos e restrições do negócio"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "atualizado mensalmente pelo founder via Atlas), histórico de contra-jogadas anteriores geradas por Ares e se foram executadas ou não (ciclo de aprendizado), estado atual do negócio (preço atual, roadmap de produto, capacidade comercial) para avaliar viabilidade de cada contra-jogada"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Counter-Play Brief para cada sinal FLASH ou ameaça elevada: hipótese de intenção estratégica do concorrente (1 parágrafo com nível de confiança), sequência de movimentos previstos nos próximos 30-90 dias, 2-4 contra-jogadas ranqueadas por impacto x viabilidade (cada uma com: ação específica, janela de ação, recursos necessários, risco de não executar, indicadores de que está funcionando), Wargame Report mensal (3 cenários competitivos dos próximos 90 dias com probabilidade estimada e playbook de resposta por cenario), Strategic Opportunity Map semestral (white spaces que o founder pode capturar antes da concorrência com base nos gaps de Movement Profiles)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lynx eleva sinal para FLASH em Tier 1 (Reactive Mode imediato, Counter-Play Brief em menos de 3h); Atlas escala ameaça para análise profunda; ciclo mensal de Wargame Mode antes do Competitive Landsca…"
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

# Simular Cenários Estratégicos

**Task ID:** `ares()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Inteligência Competitiva Contínua

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Simular Cenários Estratégicos |
| **status** | `pending` |
| **responsible_executor** | Ares (Áres — Wargame & Counter-Play Engine) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Cerebro estrategico do squad — transforma sinais classificados por Lynx em cenarios de wargame e contra-jogadas concretas com janela de acao. Opera em dois modos: (1) REACTIVE MODE — quando Lynx eleva um sinal para FLASH ou Atlas escalona uma ameaca, Ares simula a hipotese estrategica do concorrente (por que estao fazendo isso? qual e a sequencia de movimentos prevista nos proximos 30-90 dias?) e gera de 2 a 4 contra-jogadas ranqueadas por viabilidade e impacto potencial, cada uma com janela de acao, recursos necessarios e risco de nao executar; (2) WARGAME MODE (mensal) — simula cenarios competitivos para os proximos 90 dias com base no Movement Profile atualizado de cada Tier 1, identifica as tres ameacas mais provaleis e seus playbooks de resposta, e avalia white spaces estrategicos que o founder pode explorar antes que um concorrente o faca. Ares usa o Corpus do Founder como input primario — os frameworks de decisao, o historico de posicionamento e o estilo de resposta estrategica do founder para gerar contra-jogadas que o founder genuinamente executaria. Sem o Corpus do Founder calibrado, as contra-jogadas sao genericas e de baixa utilidade.

## Input

- Sinal classificado por Lynx com contexto estratégico (para Reactive Mode), Movement Profile atualizado de todos os Tier 1 (para Wargame Mode), Corpus do Founder (frameworks, histórico de decisões estratégicas, posicionamento atual, recursos e restrições do negócio
- atualizado mensalmente pelo founder via Atlas), histórico de contra-jogadas anteriores geradas por Ares e se foram executadas ou não (ciclo de aprendizado), estado atual do negócio (preço atual, roadmap de produto, capacidade comercial) para avaliar viabilidade de cada contra-jogada

## Output

- Counter-Play Brief para cada sinal FLASH ou ameaça elevada: hipótese de intenção estratégica do concorrente (1 parágrafo com nível de confiança), sequência de movimentos previstos nos próximos 30-90 dias, 2-4 contra-jogadas ranqueadas por impacto x viabilidade (cada uma com: ação específica, janela de ação, recursos necessários, risco de não executar, indicadores de que está funcionando), Wargame Report mensal (3 cenários competitivos dos próximos 90 dias com probabilidade estimada e playbook de resposta por cenario), Strategic Opportunity Map semestral (white spaces que o founder pode capturar antes da concorrência com base nos gaps de Movement Profiles)

## Trigger

Lynx eleva sinal para FLASH em Tier 1 (Reactive Mode imediato, Counter-Play Brief em menos de 3h); Atlas escala ameaça para análise profunda; ciclo mensal de Wargame Mode antes do Competitive Landscape Report; founder solicita análise estratégica de concorrente específico antes de decisão importante (preço, produto, parceria); Sequence Pattern Alert de Lynx sugerindo movimento maior em preparação; revisão semestral do Strategic Opportunity Map

## Knowledge base (o que o executor consulta)

- Corpus do Founder estruturado (frameworks de decisão estratégica, histórico de posicionamento, estilo de resposta a movimentos competitivos, valores e princípios inegociáveis do negócio, restrições reais de recursos e capacidade)
- este é o conhecimento mais crítico do agente, sem ele as contra-jogadas são genéricas, Movement Profiles atualizados de todos os Tier 1 com histórico de 12 meses de movimentos, biblioteca de playbooks competitivos por categoria de movimento (como responder a price war, feature launch, talent raid, funding announcement), histórico de efetividade de contra-jogadas anteriores (o que o founder executou, qual foi o resultado), benchmarks de respostas competitivas eficazes do setor para calibrar a qualidade das recomendações

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinal classificado por Lynx com contexto estratégico (para Reactive Mode), Movement Profile atualizado de todos os Tier…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Counter-Play Brief para cada sinal FLASH ou ameaça elevada: hipótese de intenção estratégica do concorrente (1 parágraf…) e persistir no artefato do squad.
4. Entregar ao critic Veritas 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Counter-Play Brief para cada sinal FLASH ou ameaça elevada: hipótese de intenção estratégica do concorrente (1 parágrafo com nível de confiança), sequência de…
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

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
