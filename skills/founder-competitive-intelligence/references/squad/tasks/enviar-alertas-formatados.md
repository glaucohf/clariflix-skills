---
task: hermes()
responsavel: "Hermes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Counter-Play Brief de Ares aprovado por Veritas (para Competitive Flashes FLASH), Weekly Briefing consolidado por Atlas (para ciclo semanal), Competitive Landscape Report mensal de Atlas aprovado por Veritas, configuração de canais e preferências do founder (Slack workspace e canal, email, horários de não-perturbação, formato de preferência de briefing), credenciais de acesso ao ClickUp para criação de tasks via MCP"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Competitive Flash Card entregue via Slack e email (estrutura padrão: O QUE + QUEM + POR QUE IMPORTA + JANELA DE AÇÃO + PRÓXIMOS PASSOS), task criada no ClickUp com prioridade e prazo definidos e link para Counter-Play Brief completo, Competitive Intel Weekly Briefing publicado toda sexta-feira no canal Slack #competitive-intel + task semanal no ClickUp para revisão do founder, Competitive Landscape Report mensal publicado no Notion e task mensal no ClickUp, log de entrega rastreável com timestamp, canal e confirmação de leitura quando disponível"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Veritas aprova Counter-Play Brief de sinal FLASH (entrega imediata, latência máxima de 30min pós-aprovação); Atlas finaliza consolidação do Weekly Briefing (toda sexta-feira até 16h no horário config…"
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

# Enviar Alertas Formatados

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Inteligência Competitiva Contínua

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Alertas Formatados |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — Alert & Briefing Dispatcher) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Interface entre inteligência gerada e ação do founder — responsável por transformar Competitive Flashes e Weekly Briefings em comunicação clara, acionável e no canal certo, no momento certo. Para cada alerta FLASH aprovado por Veritas: (1) formata o Competitive Flash Card — estrutura padrão de 5 elementos: O QUE (o movimento específico com evidência), QUEM (qual concorrente, tier, relevância histórica), POR QUE IMPORTA (impacto direto no negócio do founder em 2 frases), JANELA DE AÇÃO (quanto tempo o founder tem para reagir antes que a janela feche), PRÓXIMOS PASSOS (a contra-jogada recomendada por Ares — específica, não genérica); (2) determina o canal e urgência de entrega: CRÍTICO (score 9-10, Tier 1) = notificação imediata no Slack + email com subject formatado para mobile; ALTO (score 7-8) = Slack message no canal configurado em menos de 2h; NORMAL (score 5-6) = incluído no Daily Digest se configurado, caso contrário no Weekly; (3) cria task no ClickUp com prioridade, prazo (baseado na janela de ação), responsável e link para o Counter-Play Brief de Ares. Para o Weekly Briefing: formata o documento completo seguindo template padrão, adiciona contexto narrativo de Atlas sobre a semana competitiva, e cria a task de revisão semanal para o founder.

## Input

- Counter-Play Brief de Ares aprovado por Veritas (para Competitive Flashes FLASH), Weekly Briefing consolidado por Atlas (para ciclo semanal), Competitive Landscape Report mensal de Atlas aprovado por Veritas, configuração de canais e preferências do founder (Slack workspace e canal, email, horários de não-perturbação, formato de preferência de briefing), credenciais de acesso ao ClickUp para criação de tasks via MCP

## Output

- Competitive Flash Card entregue via Slack e email (estrutura padrão: O QUE + QUEM + POR QUE IMPORTA + JANELA DE AÇÃO + PRÓXIMOS PASSOS), task criada no ClickUp com prioridade e prazo definidos e link para Counter-Play Brief completo, Competitive Intel Weekly Briefing publicado toda sexta-feira no canal Slack #competitive-intel + task semanal no ClickUp para revisão do founder, Competitive Landscape Report mensal publicado no Notion e task mensal no ClickUp, log de entrega rastreável com timestamp, canal e confirmação de leitura quando disponível

## Trigger

Veritas aprova Counter-Play Brief de sinal FLASH (entrega imediata, latência máxima de 30min pós-aprovação); Atlas finaliza consolidação do Weekly Briefing (toda sexta-feira até 16h no horário configurado); Atlas finaliza Competitive Landscape Report mensal aprovado por Veritas; founder solicita re-envio de briefing específico; configuração inicial de canais de alerta (setup no Discovery)

## Knowledge base (o que o executor consulta)

- Templates de Competitive Flash Card por categoria de movimento (template de pricing change e diferente de template de hiring burst ou funding announcement), preferências de comunicação do founder (canais, horários, nível de detalhe preferido, formato mobile vs
- desktop), mapeamento de stakeholders que devem receber cópia de alertas específicos (ex: mudança de preço pode notificar também o Head Comercial), histórico de entrega de alertas com timestamps para SLA tracking, configuração de ClickUp (workspace, listas por tipo de alerta, campos customizados de Competitive Intelligence)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Counter-Play Brief de Ares aprovado por Veritas (para Competitive Flashes FLASH), Weekly Briefing consolidado por Atlas…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Competitive Flash Card entregue via Slack e email (estrutura padrão: O QUE + QUEM + POR QUE IMPORTA + JANELA DE AÇÃO +…) e persistir no artefato do squad.
4. Entregar ao critic Veritas 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Competitive Flash Card entregue via Slack e email (estrutura padrão: O QUE + QUEM + POR QUE IMPORTA + JANELA DE AÇÃO + PRÓXIMOS PASSOS), task criada no ClickUp…
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

- **to:** Memo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
