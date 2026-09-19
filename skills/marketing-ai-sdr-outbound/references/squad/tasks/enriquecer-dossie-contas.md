---
task: scoutProfiler()
responsavel: "Scout Profiler"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Nome de empresa e/ou domínio"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "ICP Card da persona alvo (ICP Cartografo)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso a APIs de enriquecimento: Clay (waterfall enrichment), Apollo.io (275M+ contatos, emails verificados), Cognism, LinkedIn Sales Navigator"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Acesso à web para notícias recentes (EXA/WebSearch)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê de conta estruturado em Markdown com 6 seções: (1) Visão Geral da Empresa"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "segmento, porte, receita estimada, número de funcionários, sede, site"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Decisores Identificados"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "lista de 3-5 contatos por cargo com nome, LinkedIn URL, email verificado, senioridade e score de relevância"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Stack Tecnológico"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "ferramentas em uso que indicam fit ou concorrência, fonte de cada dado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Maestro para cada empresa aprovada no Calibre Scorer com score >= 60. Re-trigger se novos sinais de intent forem detectados para uma empresa ja no funil. Trigger em batch diario para lis…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR humano com draft completo, dossiê e score para aprovação ou rejeição com 1 clique antes de qualquer disparo."
    - "[ ] HITL: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o feedback detalhado do critic para reescritura manual."
    - "[ ] HITL: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente não envia com informação não verificada."
    - "[ ] HITL: Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para assumir a conversa — o squad nao conduz negociacao, apenas entrega o contexto completo e recua."
    - "[ ] HITL: Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do gestor comercial antes de qualquer envio."
---

# Enriquecer Dossiê Contas

**Task ID:** `scoutProfiler()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dossiê Contas |
| **status** | `pending` |
| **responsible_executor** | Scout Profiler (Scout Profiler — O Investigador de Contas) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Dado um domínio ou nome de empresa dentro do ICP, executa uma cascata de enriquecimento a partir de 100+ fontes para construir um dossiê completo e verificado antes de qualquer outreach. Identifica os decisores certos por cargo, encontra seus emails verificados e perfis de LinkedIn, mapeia o stack tecnológico atual da empresa, captura notícias e eventos recentes relevantes (rodada de investimento, expansão, mudança de liderança, lançamento de produto), e sintetiza 3 ângulos de personalização específicos e verificáveis para o Cyrano usar nas mensagens. Não fabrica informação — tudo no dossiê tem fonte rastreável.

## Input

- Nome de empresa e/ou domínio
- ICP Card da persona alvo (ICP Cartografo)
- Acesso a APIs de enriquecimento: Clay (waterfall enrichment), Apollo.io (275M+ contatos, emails verificados), Cognism, LinkedIn Sales Navigator
- Acesso à web para notícias recentes (EXA/WebSearch)

## Output

- Dossiê de conta estruturado em Markdown com 6 seções: (1) Visão Geral da Empresa
- segmento, porte, receita estimada, número de funcionários, sede, site
- (2) Decisores Identificados
- lista de 3-5 contatos por cargo com nome, LinkedIn URL, email verificado, senioridade e score de relevância
- (3) Stack Tecnológico
- ferramentas em uso que indicam fit ou concorrência, fonte de cada dado
- (4) Eventos Recentes (últimos 90 dias)
- max 3 notícias ou eventos relevantes com link e data
- (5) Dores Inferidas
- 3 hipóteses de dor baseadas nos dados coletados, não em suposições genéricas
- (6) Ângulos de Personalização
- 3 opções ranqueadas de hook específico para a mensagem, cada uma com evidência do dossiê
- Score de confiança do dossiê (0-100) baseado na completude e verificabilidade dos dados
- Artefato salvo no ClickUp e linkado ao lead no CRM

## Trigger

Ativado pelo Maestro para cada empresa aprovada no Calibre Scorer com score >= 60. Re-trigger se novos sinais de intent forem detectados para uma empresa ja no funil. Trigger em batch diario para lista de contas frias priorizadas pelo SDR humano.

## Knowledge base (o que o executor consulta)

- Playbook de fontes por tipo de dado: emails verificados (Apollo > Clay > Cognism > Hunter.io em cascata), tecnografias (BuiltWith > Wappalyzer > Clay), notícias (EXA + Google News), cargos de decisão por vertical
- Regras de qualidade: email sem verificação dupla não entra no dossiê
- Templates de dossiê por vertical (agência, SaaS, indústria, serviços)
- Histórico de dossiês de contas que converteram
- padrões de dados que indicam alta probabilidade de resposta

## Action Items

1. Confirmar o gatilho e carregar a entrada (Nome de empresa e/ou domínio).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossiê de conta estruturado em Markdown com 6 seções: (1) Visão Geral da Empresa) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossiê de conta estruturado em Markdown com 6 seções: (1) Visão Geral da Empresa
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloquei…
- [ ] Gate HITL respeitado: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para…
- [ ] Gate HITL respeitado: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR h… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o f… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente nã… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para a… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ICP Cartografo detecta shift significativo de mercado (nova objecao emergindo em >30% das respostas, queda de >20% no reply rate em 2 semanas consecutivas): al… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out ou resposta negativa agressiva: processado pelo Pulse Analyst, sequência cancelada automaticamente, CRM atualizado, notificação ao SDR para decisão sob… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Calibre Scorer
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
