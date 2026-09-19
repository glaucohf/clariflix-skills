---
task: gaia()
responsavel: "Gaia"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Decision Package consolidado por Lens (BvB Analysis de Kai + Vendor Risk Assessment de Aegis + Adversarial Review de ARIA) para cada decisao que atingiu threshold L3, configuracoes de threshold de autonomia (quais decisoes requerem gate L3 versus podem ser implementadas autonomamente em L2) definidas pelo founder no Discovery, historico de decisoes anteriores no Technology Decision Log para context de decisoes relacionadas, configuracao de canais de comunicacao para gates HITL (Slack channel, email, urgencia por tipo de decisao)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Gate HITL criado no ClickUp (task de aprovacao com deadline, Decision Package anexado, link para todos os artefatos) e notificacao enviada ao founder/CTO via canal configurado, confirmacao de gate concluido (APPROVED/APPROVED_WITH_CONDITIONS/REJECTED/DEFERRED) com timestamp e comentarios do founder registrados, Architecture Decision Record (ADR) novo criado no Technology Decision Log para cada decisao aprovada (estrutura padrao: contexto, decisao, alternativas consideradas, consequencias esperadas, condicoes de revisao), Revisao Reminder criado para cada decisao com condicoes de revisao definidas (Gaia monitora as condicoes e dispara reminder quando sao atingidas"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "ex: renovacao de contrato, threshold de custo, data periodica)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lens triggra gate L3 para qualquer decisao de: (a) adocao de novo vendor Tier 1 (requer ARIA APPROVED + Aegis APPROVED + gate L3 do founder — triplo gate); (b) substituicao de componente Tier 1 exist…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic ARIA 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criticidade (Tier 1/2/3), e os criterios de threshold que trigam BvB Analysis automatica (custo minimo, nivel de impacto). Gate L3 obrigatorio — sem esta aprovacao o squad nao opera em producao. Define o escopo de toda a operacao"
    - "[ ] HITL: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/Trial/Assess/Hold, questionam posicionamentos que parecem incorretos com base em contexto interno nao capturado, e assinam o Vendor Risk Register inicial. Gate L3 — este documento se torna a linha de base de toda decisao futura"
    - "[ ] HITL: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPROVED com condicoes) + Gaia envia Decision Package consolidado para aprovacao explicita do founder/CTO via ClickUp task. Irreversivel por natureza: contratos assinados, integracao implementada e dados migrados sao difficeis e caros de desfazer"
    - "[ ] HITL: Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do threshold (ex: 3 meses de engenheiro ou R$50k) requer aprovacao explicita do founder com ARIA Worst-Case Scenarios documentados. Irreversivel: capacidade de engenheiro desviada nao pode ser recuperada"
    - "[ ] HITL: Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology Roadmap Recommendations para os proximos 2 trimestres. Gate L3: founder/CTO aprovam as recomendacoes antes de se tornarem diretriz tecnica do squad. Incluido no calendario de governanca do founder"
---

# Registrar Decisão Técnica

**Task ID:** `gaia()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Registrar Decisão Técnica |
| **status** | `pending` |
| **responsible_executor** | Gaia (Gaia — HITL Gate & Decision Registry) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Guardiao de processo e memoria institucional das decisoes tecnicas — garante que cada decisao de alto impacto passa pelo gate humano correto antes de ser implementada, e que toda decisao aprovada fica registrada com criterios explicitos e condicoes de revisao. Opera em dois modos: (1) HITL GATE MODE — intercepta todas as recomendacoes que atingem o threshold de autonomia L3 (decisoes irreversiveis ou de alto custo) e cria o gate de aprovacao formal: prepara o Decision Package para o founder/CTO (BvB Analysis de Kai + Vendor Risk Assessment de Aegis + Adversarial Review de ARIA em formato consolidado de 1-2 paginas), cria task de aprovacao no ClickUp com deadline baseado na urgencia, envia via canal configurado (Slack/email), aguarda confirmacao explicita do founder/CTO (nao apenas read receipt — exige resposta de aprovacao ou solicitacao de mais informacao), e registra o outcome da aprovacao com timestamp e qualquer comentario do founder; (2) DECISION REGISTRY MODE — mantem o Technology Decision Log (ADR — Architecture Decision Records) para todas as decisoes aprovadas: para cada decisao registra a data, o que foi decidido, quem aprovou, as alternativas consideradas, as premissas assumidas, as condicoes de revisao ('revisitar se o preco do vendor X superar R$Y/mes ou se o Lock-in Score exceder Z'), e o link para todos os artefatos de suporte (BvB Analysis, Vendor Risk Assessment, ARIA Review). O Technology Decision Log e o registro vivo do porque o stack atual existe — indispensavel para onboarding de novos tecnicos e para evitar que decisoes antigas sejam questionadas sem contexto.

## Input

- Decision Package consolidado por Lens (BvB Analysis de Kai + Vendor Risk Assessment de Aegis + Adversarial Review de ARIA) para cada decisao que atingiu threshold L3, configuracoes de threshold de autonomia (quais decisoes requerem gate L3 versus podem ser implementadas autonomamente em L2) definidas pelo founder no Discovery, historico de decisoes anteriores no Technology Decision Log para context de decisoes relacionadas, configuracao de canais de comunicacao para gates HITL (Slack channel, email, urgencia por tipo de decisao)

## Output

- Gate HITL criado no ClickUp (task de aprovacao com deadline, Decision Package anexado, link para todos os artefatos) e notificacao enviada ao founder/CTO via canal configurado, confirmacao de gate concluido (APPROVED/APPROVED_WITH_CONDITIONS/REJECTED/DEFERRED) com timestamp e comentarios do founder registrados, Architecture Decision Record (ADR) novo criado no Technology Decision Log para cada decisao aprovada (estrutura padrao: contexto, decisao, alternativas consideradas, consequencias esperadas, condicoes de revisao), Revisao Reminder criado para cada decisao com condicoes de revisao definidas (Gaia monitora as condicoes e dispara reminder quando sao atingidas
- ex: renovacao de contrato, threshold de custo, data periodica)

## Trigger

Lens triggra gate L3 para qualquer decisao de: (a) adocao de novo vendor Tier 1 (requer ARIA APPROVED + Aegis APPROVED + gate L3 do founder — triplo gate); (b) substituicao de componente Tier 1 existente; (c) decisao de Build para componente com TCO estimado acima de threshold definido no Discovery; (d) aprovacao de contrato acima de threshold de valor anual; (e) movimento de componente Tier 1 para HOLD com plano de substituicao; Review Reminder quando condicao de revisao de ADR anterior e atingida (preco do vendor ultrapassou threshold, data de revisao chegou, Lock-in Score mudou); ciclo trimestral de Technology Decision Log Review — Gaia compila todas as decisoes do trimestre com status de suas premissas para o Tech Strategy Quarterly de Lens

## Knowledge base (o que o executor consulta)

- Technology Decision Log completo (todos os ADRs desde o inicio do squad com status atualizado de cada premissa), thresholds de autonomia configurados pelo founder (valores em R$ e criterios de criticidade que definem quando gate L3 e obrigatorio), templates de ADR por tipo de decisao tecnica (adocao de novo vendor, decisao de build, migracao de plataforma, deprecacao de componente), historico de gates HITL com tempo de resposta do founder (para calibrar urgencia e formato de comunicacao
- se o founder tipicamente responde em 2h via Slack mas leva 2 dias via email, o canal de urgencia e Slack)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Decision Package consolidado por Lens (BvB Analysis de Kai + Vendor Risk Assessment de Aegis + Adversarial Review de AR…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Gate HITL criado no ClickUp (task de aprovacao com deadline, Decision Package anexado, link para todos os artefatos) e…) e persistir no artefato do squad.
4. Entregar ao critic ARIA 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Gate HITL criado no ClickUp (task de aprovacao com deadline, Decision Package anexado, link para todos os artefatos) e notificacao enviada ao founder/CTO via c…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic ARIA 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as cla…
- [ ] Gate HITL respeitado: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes n…
- [ ] Gate HITL respeitado: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adve…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criti… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPRO… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology R… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisao de Vendor Risk Alerts gerados por Aegis para vendors Tier 1 ativos — quando Aegis detecta mudanca em ToS, DPA ou historico de incidente de seguranca em… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Aprovacao de movimentos de quadrante com impacto em sistemas Tier 1 — quando Nox propoe mover componente Tier 1 para HOLD ou Tier 1/2 para ADOPT, gate L2 (CTO… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Conditions Review Reminder de Gaia — quando as condicoes de revisao de um ADR sao atingidas (preco do vendor ultrapassou threshold, data de revisao chegou, Loc… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic ARIA 2 | BLOQUEIA entrega |

## Handoff

- **to:** ARIA 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
