---
task: lynx()
responsavel: "Lynx"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Feed diário de sinais de Hawk com dados brutos, histórico de sinais classificados dos últimos 90 dias por concorrente para detecção de padrões de sequência, parâmetros de scoring configurados pelo founder via Atlas (pesos por categoria de movimento e por tier de concorrente), perfil estratégico de cada concorrente Tier 1 (modelo de negócio, histórico de movimentos, padrão de comportamento) para contextualizar sinais novos"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sinais classificados e pontuados (categoria, subtipo, score de relevância 0-10, urgência FLASH/WEEKLY/MONITOR, contexto estratégico de 2-3 frases explicando por que este sinal importa), Sequence Pattern Alert quando detecta padrão de múltiplos sinais de mesmo concorrente sugerindo movimento maior em preparação (ex: 3 contratações estratégicas em 60 dias antes de uma rodada ou lançamento), Movement Profile atualizado por concorrente Tier 1 (estado atual de cada dimensão estratégica: posicionamento de preço, foco de produto, capacidade comercial, saúde financeira aparente), input estruturado para Atlas priorizar o que vai ao Competitive Flash versus Weekly Briefing"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cada batch de sinais novos de Hawk (processamento contínuo com latência máxima de 1h entre coleta e classificação para sinais Tier 1); Sequence Pattern Alert quando 3+ sinais relacionados de mesmo co…"
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

# Classificar Movimentos Estrategicos

**Task ID:** `lynx()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Inteligência Competitiva Contínua

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Movimentos Estrategicos |
| **status** | `pending` |
| **responsible_executor** | Lynx (Lynx — Signal Intelligence Analyst) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Camada de análise e classificação entre a coleta bruta de Hawk e a síntese estratégica de Atlas. Lynx processa cada sinal novo detectado por Hawk e toma três decisões: (1) RELEVÂNCIA — este sinal é ruído (atividade rotineira sem implicação estratégica) ou sinal real (indica movimento ou intenção estratégica)? Usa scoring ponderado por categoria: mudança de preço Tier 1 = 10/10 por default, nova job posting de VP Sales = 7/10, novo post de blog = 2/10 salvo se tópico for de produto ou positioning direto; (2) CATEGORIA — classifica o sinal em uma das cinco categorias de movimento competitivo (Pricing, Product, Talent, Capital, Market Expansion) e, dentro da categoria, no subtipo específico (ex: Talent > Contratar C-Level vs. Talent > Escalar Time Comercial); (3) URGENCIA — com base no score de relevância e na janela de reação configurada pelo founder, classifica como: FLASH (alerta imediato, score >= 8 em Tier 1), WEEKLY (incluir no briefing semanal, score 5-7), MONITOR (registrar para contexto, score < 5). Constroi perfil de atividade estratégica por concorrente ao longo do tempo — detecta padrões de sequência (ex: funding > contratação de CRO > mudança de preço = padrão de ofensiva comercial pre-escalada).

## Input

- Feed diário de sinais de Hawk com dados brutos, histórico de sinais classificados dos últimos 90 dias por concorrente para detecção de padrões de sequência, parâmetros de scoring configurados pelo founder via Atlas (pesos por categoria de movimento e por tier de concorrente), perfil estratégico de cada concorrente Tier 1 (modelo de negócio, histórico de movimentos, padrão de comportamento) para contextualizar sinais novos

## Output

- Sinais classificados e pontuados (categoria, subtipo, score de relevância 0-10, urgência FLASH/WEEKLY/MONITOR, contexto estratégico de 2-3 frases explicando por que este sinal importa), Sequence Pattern Alert quando detecta padrão de múltiplos sinais de mesmo concorrente sugerindo movimento maior em preparação (ex: 3 contratações estratégicas em 60 dias antes de uma rodada ou lançamento), Movement Profile atualizado por concorrente Tier 1 (estado atual de cada dimensão estratégica: posicionamento de preço, foco de produto, capacidade comercial, saúde financeira aparente), input estruturado para Atlas priorizar o que vai ao Competitive Flash versus Weekly Briefing

## Trigger

Cada batch de sinais novos de Hawk (processamento contínuo com latência máxima de 1h entre coleta e classificação para sinais Tier 1); Sequence Pattern Alert quando 3+ sinais relacionados de mesmo concorrente em 30 dias; Atlas solicita análise profunda de concorrente específico para wargame de Ares; ciclo semanal de atualização de Movement Profiles antes do Weekly Briefing; revisão mensal de calibração de scoring com feedback do founder sobre acurácia dos alertas

## Knowledge base (o que o executor consulta)

- Histórico completo de sinais classificados por concorrente (últimos 12 meses) para detectar padrões sazonais e sequências estratégicas, biblioteca de padrões de movimento competitivo com sequências típicas por tipo de empresa (startup early-stage vs
- scale-up vs
- incumbente tem padrões distintos), scoring matrix por categoria e tier configurada pelo founder (pesos atualizados após cada revisão mensal), perfis estratégicos de cada Tier 1 com histórico de movimentos e padrão de comportamento documentado, fontes de calibração externa (relatórios de setor, earnings calls de concorrentes listados se aplicável) para contextualizar sinais individuais

## Action Items

1. Confirmar o gatilho e carregar a entrada (Feed diário de sinais de Hawk com dados brutos, histórico de sinais classificados dos últimos 90 dias por concorrente p…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sinais classificados e pontuados (categoria, subtipo, score de relevância 0-10, urgência FLASH/WEEKLY/MONITOR, contexto…) e persistir no artefato do squad.
4. Entregar ao critic Veritas 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sinais classificados e pontuados (categoria, subtipo, score de relevância 0-10, urgência FLASH/WEEKLY/MONITOR, contexto estratégico de 2-3 frases explicando po…
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

- **to:** Ares
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
