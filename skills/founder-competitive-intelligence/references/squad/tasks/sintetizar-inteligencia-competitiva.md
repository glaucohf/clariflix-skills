---
task: memo()
responsavel: "Memo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Competitive Landscape Reports dos últimos 1-3 trimestres de Atlas, Counter-Play Briefs e resultados de contra-jogadas executadas (histórico de efetividade), Movement Profiles atualizados de todos os Tier 1, Wargame Reports de Ares, dados do negócio do founder (métricas-chave, posicionamento atual, roadmap"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "fornecidos via Atlas no HITL de contextualização), template de board pack do cliente (formato preferido pelo conselho) e instruções de tom do Corpus do Founder"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Board Intelligence Pack (documento 3-5 paginas, source-grounded: Competitive Landscape Summary + Top 3 Movimentos do Periodo + Counter-Plays Executados + Posicionamento Atual vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Concorrencia + Recomendacoes para Discussao), Decision Intelligence Brief (para decisoes estrategicas especificas: contexto competitivo da decisao + timing analysis + risks + oportunidades + recomendacao com nivel de confianca), Investor Memo Draft (para updates de investidores: competitive positioning section com evidencias, sem spin"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "fatos e interpretacao honesta), todos os documentos com footnotes rastreavais ligando cada afirmacao ao sinal fonte"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Founder agenda board meeting ou investor update (Atlas notifica Memo com 2 semanas de antecedência para Board Intelligence Pack); founder inicia processo de decisão estratégica de alto impacto (solic…"
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

# Sintetizar Inteligência Competitiva

**Task ID:** `memo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Inteligência Competitiva Contínua

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Inteligência Competitiva |
| **status** | `pending` |
| **responsible_executor** | Memo (Memo — Board & Investor Intel Synthesizer) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em transformar inteligencia competitiva continua em comunicacao de alto nivel para boards, investidores e decisoes estrategicas do founder. Opera em dois modos: (1) BOARD PREP MODE (antes de board meetings ou investor updates) — consolida toda a inteligencia competitiva do periodo relevante (tipicamente ultimo trimestre) em um Board Intelligence Pack: estado do landscape competitivo, movimentos dos principais concorrentes, contra-jogadas executadas e seus resultados, posicionamento atual da empresa versus concorrencia, e recomendacoes estrategicas para o board discutir. Cada afirmacao e rastreavel a um sinal especifico coletado por Hawk e classificado por Lynx (source-grounded, sem alucinacao); (2) STRATEGIC DECISION MODE — quando o founder esta considerando uma decisao de alto impacto (mudanca de preco, entrada em novo segmento, lancamento de produto, levantamento de rodada), Memo compila um Decision Intelligence Brief consolidando o que a inteligencia competitiva diz sobre o timing e contexto desta decisao especifica — o que os concorrentes estao fazendo na mesma direcao, quais sao os riscos de timing, quais sao as janelas de oportunidade. Produto diferenciado: briefings com footnotes rastreavais, nao com 'achismos'.

## Input

- Competitive Landscape Reports dos últimos 1-3 trimestres de Atlas, Counter-Play Briefs e resultados de contra-jogadas executadas (histórico de efetividade), Movement Profiles atualizados de todos os Tier 1, Wargame Reports de Ares, dados do negócio do founder (métricas-chave, posicionamento atual, roadmap
- fornecidos via Atlas no HITL de contextualização), template de board pack do cliente (formato preferido pelo conselho) e instruções de tom do Corpus do Founder

## Output

- Board Intelligence Pack (documento 3-5 paginas, source-grounded: Competitive Landscape Summary + Top 3 Movimentos do Periodo + Counter-Plays Executados + Posicionamento Atual vs
- Concorrencia + Recomendacoes para Discussao), Decision Intelligence Brief (para decisoes estrategicas especificas: contexto competitivo da decisao + timing analysis + risks + oportunidades + recomendacao com nivel de confianca), Investor Memo Draft (para updates de investidores: competitive positioning section com evidencias, sem spin
- fatos e interpretacao honesta), todos os documentos com footnotes rastreavais ligando cada afirmacao ao sinal fonte

## Trigger

Founder agenda board meeting ou investor update (Atlas notifica Memo com 2 semanas de antecedência para Board Intelligence Pack); founder inicia processo de decisão estratégica de alto impacto (solicita Decision Intelligence Brief via Atlas); fechamento de trimestre (Memo compila review competitiva trimestral); Atlas identifica conjunto de movimentos competitivos relevantes para incluir em investor narrative; HITL L3 de aprovação do founder antes de qualquer documento ser compartilhado externamente

## Knowledge base (o que o executor consulta)

- Histórico completo de Competitive Landscape Reports e Counter-Play Briefs dos últimos 12 meses com resultados documentados, Corpus do Founder (tom, frameworks de narrativa estratégica, nível de sofisticação do board/investidores, restrições de confidencialidade), templates de board packs aprovados pelos investidores atuais (se disponíveis), guidelines de source attribution para garantir rastreabilidade de afirmações, métricas do negócio atualizadas mensalmente para contextualizar o positioning competitivo com dados próprios

## Action Items

1. Confirmar o gatilho e carregar a entrada (Competitive Landscape Reports dos últimos 1-3 trimestres de Atlas, Counter-Play Briefs e resultados de contra-jogadas e…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Board Intelligence Pack (documento 3-5 paginas, source-grounded: Competitive Landscape Summary + Top 3 Movimentos do Pe…) e persistir no artefato do squad.
4. Entregar ao critic Veritas 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Board Intelligence Pack (documento 3-5 paginas, source-grounded: Competitive Landscape Summary + Top 3 Movimentos do Periodo + Counter-Plays Executados + Posic…
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

- **to:** Veritas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
