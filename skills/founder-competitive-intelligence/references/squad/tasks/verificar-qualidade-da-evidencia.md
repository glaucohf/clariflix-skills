---
task: veritas()
responsavel: "Veritas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Counter-Play Briefs de Ares antes de entrega para Hermes (gate SEMPRE ativo para FLASH alerts), Board Intelligence Pack e Decision Intelligence Brief de Memo antes de qualquer entrega ao founder ou externos, Category Trend Alerts de Atlas antes de escalar como diretriz, Movement Profiles de Lynx trimestralmente para revisão de calibração, sinais brutos de Hawk quando Lynx pontua acima de 9 para validação direta da fonte"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa estruturada para cada item revisado (minimo 3 razoes para BLOCKED, 1-2 para NEEDS_REVISION), lista especifica de ajustes necessarios se NEEDS_REVISION (ex: 'hipotese de lancamento de produto tem confianca 8/10 mas evidencia suporta no maximo 5/10"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "rebaixar para hipotese exploratorio ou buscar evidencia adicional'), Alternative Hypothesis Flag quando Ares apresentou apenas uma hipotese para movimento de alta consequencia, Rastreability Audit para documentos de Memo (% de claims com footnote verificavel"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "meta 100% para Board Pack e Decision Brief), Intelligence Credibility Score por Counter-Play Brief (0-10 com breakdown das 5 dimensoes)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: SEMPRE antes de qualquer Competitive Flash FLASH ser entregue ao founder (gate obrigatório, latência máxima de 1h para não perder janela de reação); sempre antes de qualquer documento de Memo ser com…"
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

# Verificar Qualidade Da Evidencia

**Task ID:** `veritas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Inteligência Competitiva Contínua

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Qualidade Da Evidencia |
| **status** | `pending` |
| **responsible_executor** | Veritas (Veritás — Crític & Intelligênce Verífier) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gate de qualidade adversarial de todo o squad — implementa o padrao Skeptic Protocol adaptado para inteligencia competitiva de alto nivel. Funciona como um analista de inteligencia cético profissional que questiona cada claim antes de chegar ao founder. Valida cinco dimensoes em todo item critico: (1) QUALIDADE DA EVIDENCIA — o sinal e real e de fonte verificavel, ou e inferencia de segundo grau? (ex: alguem no LinkedIn postou que 'um concorrente vai lancar X' nao e o mesmo que a pagina de produto do concorrente mostrar a feature — Veritas distingue e ajusta o nivel de confianca correspondente); (2) SOLIDEZ DA HIPOTESE — a hipotese de intencao estrategica de Ares e defensavel com as evidencias disponiveis, ou e especulacao com confianca inflada? (falsa certeza em inteligencia competitiva e mais perigosa que admitir incerteza); (3) ALTERNATIVE HYPOTHESES — Veritas exige que Ares considere pelo menos uma hipotese alternativa para cada movimento antes de recomendar a contra-jogada (ex: nova contratacao de VP Sales pode ser para ofensiva comercial OU pode ser substituicao de demissao — a contra-jogada e diferente); (4) COMPLETUDE DO BRIEFING — o Competitive Flash Card de Hermes tem as cinco secoes completas e com informacao suficiente para o founder agir sem buscar contexto adicional?; (5) RASTREABILIDADE — todo claim no Board Intel Pack ou Decision Intelligence Brief de Memo tem footnote ligando ao sinal fonte? Sem isso, BLOCKED.

## Input

- Counter-Play Briefs de Ares antes de entrega para Hermes (gate SEMPRE ativo para FLASH alerts), Board Intelligence Pack e Decision Intelligence Brief de Memo antes de qualquer entrega ao founder ou externos, Category Trend Alerts de Atlas antes de escalar como diretriz, Movement Profiles de Lynx trimestralmente para revisão de calibração, sinais brutos de Hawk quando Lynx pontua acima de 9 para validação direta da fonte

## Output

- Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa estruturada para cada item revisado (minimo 3 razoes para BLOCKED, 1-2 para NEEDS_REVISION), lista especifica de ajustes necessarios se NEEDS_REVISION (ex: 'hipotese de lancamento de produto tem confianca 8/10 mas evidencia suporta no maximo 5/10
- rebaixar para hipotese exploratorio ou buscar evidencia adicional'), Alternative Hypothesis Flag quando Ares apresentou apenas uma hipotese para movimento de alta consequencia, Rastreability Audit para documentos de Memo (% de claims com footnote verificavel
- meta 100% para Board Pack e Decision Brief), Intelligence Credibility Score por Counter-Play Brief (0-10 com breakdown das 5 dimensoes)

## Trigger

SEMPRE antes de qualquer Competitive Flash FLASH ser entregue ao founder (gate obrigatório, latência máxima de 1h para não perder janela de reação); sempre antes de qualquer documento de Memo ser compartilhado com o founder para aprovação pré-distribuição; Atlas eleva ameaça para wargame de alto impacto (revisão de hipóteses de Ares antes de Counter-Play); calibração trimestral de scoring de Lynx (revisão de falsos positivos e falsos negativos do período); qualquer sinal de Hawk pontuado acima de 9.5 (revisão direta da fonte para confirmar autenticidade)

## Knowledge base (o que o executor consulta)

- Taxonomia de qualidade de evidencia por fonte (o que cada fonte pode e nao pode provar: LinkedIn headcount e proxi, nao dado preciso
- Crunchbase pode ter rodadas nao anunciadas
- diff de pagina de preco e evidencia direta de mudanca mas nao revela motivacao), historico de falsos positivos e falsos negativos do squad (para calibrar scoring de Lynx e hipoteses de Ares), biblioteca de Alternative Hypotheses por tipo de movimento competitivo (para garantir que Ares nao caia em pensamento de grupo), criterios de rastreabilidade por tipo de documento (threshold de footnotes por seccao no Board Pack), Intelligence Credibility Scores historicos para benchmark de qualidade do squad ao longo do tempo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Counter-Play Briefs de Ares antes de entrega para Hermes (gate SEMPRE ativo para FLASH alerts), Board Intelligence Pack…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa estruturada para cada item revisado (minimo 3 razoes para B…) e persistir no artefato do squad.
4. Entregar ao critic Veritas 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa estruturada para cada item revisado (minimo 3 razoes para BLOCKED, 1-2 para NEEDS_REVISION), lista…
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

- **to:** Veritas 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
