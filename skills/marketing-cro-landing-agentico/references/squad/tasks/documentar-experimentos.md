---
task: atlas()
responsavel: "Atlas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Experiment Conclusion Reports do Darwin, Behavioral Insights Reports do Hera, aprovações e rejeições do Rex, backlog atual de hipóteses, histórico completo de experimentos do cliente, resultados de pesquisa do Sage"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "CRO Playbook atualizado (markdown estruturado, versionado, organizado por elemento testado: headline / CTA / hero / formulário / social proof / pricing / urgência), Backlog de Hipóteses priorizado via ICE Score (Impact/Confidence/Ease) com status de cada item, Velocity Report quinzenal (quantos experimentos concluídos, lift médio por ciclo, taxa de vencedores vs perdedores vs inconclusivos), mapa de 'hipóteses que já falharam e por que' para evitar retrabalho, recomendação das próximas 3 hipóteses para a wave seguinte"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Encerramento de qualquer experimento (Darwin trigger); início de novo ciclo de planejamento (quinzenal); solicitação de Maestro para snapshot do estado atual do CRO Playbook; onboarding de nova págin…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Rex 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção"
    - "[ ] HITL: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final"
    - "[ ] HITL: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)"
    - "[ ] HITL: Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)"
    - "[ ] HITL: Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)"
---

# Documentar Experimentos

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Documentar Experimentos |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — CRO Knowledge Base Agent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Curador e organizador do conhecimento acumulado de CRO do squad. Documenta cada experimento encerrado no CRO Playbook (o que foi testado, resultado, learning, proxima hipotese derivada), mantém o backlog de hipoteses priorizado via ICE Score atualizado, e gera o relatorio quinzenal de velocidade de aprendizado para o Maestro. Garante que o squad nao repita experimentos ja testados e que o conhecimento acumulado informe as proximas waves. Analogia: o curador do museu de experimentos — sem Atlas, cada ciclo começa do zero. Alias: 'Atlas' — carrega o peso de todo o conhecimento acumulado para que os outros nao precisem.

## Input

- Experiment Conclusion Reports do Darwin, Behavioral Insights Reports do Hera, aprovações e rejeições do Rex, backlog atual de hipóteses, histórico completo de experimentos do cliente, resultados de pesquisa do Sage

## Output

- CRO Playbook atualizado (markdown estruturado, versionado, organizado por elemento testado: headline / CTA / hero / formulário / social proof / pricing / urgência), Backlog de Hipóteses priorizado via ICE Score (Impact/Confidence/Ease) com status de cada item, Velocity Report quinzenal (quantos experimentos concluídos, lift médio por ciclo, taxa de vencedores vs perdedores vs inconclusivos), mapa de 'hipóteses que já falharam e por que' para evitar retrabalho, recomendação das próximas 3 hipóteses para a wave seguinte

## Trigger

Encerramento de qualquer experimento (Darwin trigger); início de novo ciclo de planejamento (quinzenal); solicitação de Maestro para snapshot do estado atual do CRO Playbook; onboarding de nova página no portfolio — Atlas briefia Muse e Pixel com o histórico relevante

## Knowledge base (o que o executor consulta)

- Histórico completo de todos os experimentos (hipótese, configuração, resultado, learning), versões anteriores do CRO Playbook, framework ICE Score com pesos por contexto do cliente, biblioteca de hipóteses de CRO catalogadas por tipo de elemento e tipo de página, resultados de benchmark do Sage para calibrar o Confidence do ICE Score

## Action Items

1. Confirmar o gatilho e carregar a entrada (Experiment Conclusion Reports do Darwin, Behavioral Insights Reports do Hera, aprovações e rejeições do Rex, backlog at…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (CRO Playbook atualizado (markdown estruturado, versionado, organizado por elemento testado: headline / CTA / hero / for…) e persistir no artefato do squad.
4. Entregar ao critic Rex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: CRO Playbook atualizado (markdown estruturado, versionado, organizado por elemento testado: headline / CTA / hero / formulário / social proof / pricing / urgên…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Rex 2 registrado
- [ ] Gate HITL respeitado: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção d…
- [ ] Gate HITL respeitado: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na pág…
- [ ] Gate HITL respeitado: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel lega…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3)… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de pro… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qu… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão es… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hi… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Rex 2 | BLOQUEIA entrega |

## Handoff

- **to:** Rex 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
