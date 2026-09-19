---
task: rex()
responsavel: "Rex"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pacote completo do experimento para publicação: variações de copy (Muse output), specs de layout (Pixel output), configuração do experimento (Darwin output), brand guidelines da empresa, histórico de aprovações e rejeições anteriores, URL do ad/fonte que chegará na página para verificar message match"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Experiment Approval Report: APPROVED (pode publicar), NEEDS_REVISION (lista específica de ajustes obrigatórios com justificativa por item) ou BLOCKED (violação crítica de brand/legal que requer revisão humana antes de qualquer ação)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para aprovações: checklist de 12 pontos assinado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para revisões: feedback específico e acionável por elemento (headline #2: muito agressivo para o tom da marca, substituir por [sugestão])"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Para bloqueios: descrição clara da violação e escalonamento para HITL"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Obrigatório: toda vez que Darwin aprova configuração de experimento e este está pronto para go-live (gate não é bypassável); Maestro solicita revisão de variação específica; entrada de nova página no…"
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

# Verificar Brand Voice Consistência

**Task ID:** `rex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Brand Voice Consistência |
| **status** | `pending` |
| **responsible_executor** | Rex (Rex — Crític & Brand Voice Verifier) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Verificador crítico e guardião de brand voice. Gate L3 obrigatório antes de qualquer publicação de variação no ar. Valida: (1) alinhamento com tom de voz e brand guidelines — nenhuma variação que soe fora do posicionamento da marca; (2) consistência de promessa entre o ad que trouxe o usuário e a copy da landing page (message match); (3) compliance legal — nenhuma claim sem substantiation, sem asteriscos enganosos, sem urgência falsa; (4) qualidade técnica de copy — sem erros gramaticais, sem ambiguidades, sem frases que possam ser interpretadas de forma negativa; (5) coerência com a jornada do usuário — a página não confunde quem veio de remarketing com quem é primeira visita. Implementa o padrão Skeptic Protocol para CRO. Alias: 'Rex' — o guardião que não deixa nada sair do forno antes do tempo.

## Input

- Pacote completo do experimento para publicação: variações de copy (Muse output), specs de layout (Pixel output), configuração do experimento (Darwin output), brand guidelines da empresa, histórico de aprovações e rejeições anteriores, URL do ad/fonte que chegará na página para verificar message match

## Output

- Experiment Approval Report: APPROVED (pode publicar), NEEDS_REVISION (lista específica de ajustes obrigatórios com justificativa por item) ou BLOCKED (violação crítica de brand/legal que requer revisão humana antes de qualquer ação)
- Para aprovações: checklist de 12 pontos assinado
- Para revisões: feedback específico e acionável por elemento (headline #2: muito agressivo para o tom da marca, substituir por [sugestão])
- Para bloqueios: descrição clara da violação e escalonamento para HITL

## Trigger

Obrigatório: toda vez que Darwin aprova configuração de experimento e este está pronto para go-live (gate não é bypassável); Maestro solicita revisão de variação específica; entrada de nova página no portfolio de testes; qualquer copy que mencione claims de resultado (% de melhora, garantias, depoimentos)

## Knowledge base (o que o executor consulta)

- Brand guidelines completos (tom de voz, palavras proibidas, posicionamento da marca, exemplos de copy aprovada e reprovada), histórico de aprovações e rejeições com justificativa (base de aprendizado de brand voice), checklist de compliance legal para o setor do cliente (claims, garantias, LGPD em formulários), exemplos de message match correto e incorreto para o contexto do cliente, princípios de copywriting ético (sem dark patterns, sem urgência falsa)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pacote completo do experimento para publicação: variações de copy (Muse output), specs de layout (Pixel output), config…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Experiment Approval Report: APPROVED (pode publicar), NEEDS_REVISION (lista específica de ajustes obrigatórios com just…) e persistir no artefato do squad.
4. Entregar ao critic Rex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Experiment Approval Report: APPROVED (pode publicar), NEEDS_REVISION (lista específica de ajustes obrigatórios com justificativa por item) ou BLOCKED (violação…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
