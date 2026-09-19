---
task: muse()
responsavel: "Muse"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Hipótese de CRO ativa com descrição clara do que testar (qual elemento, qual mecanismo psicológico), ICP Profile com dores e linguagem do cliente ideal, tom de voz e brand guidelines da empresa, copy atual da página (controle do teste), contexto do ad/fonte de tráfego que chegará na página, objeções comuns mapeadas pelo Hera e pelo time de vendas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de variações de copy por experimento: 3-5 versões de headline (com racional de cada uma"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "qual princípio testa), 3-5 versões de CTA com framing alternativo, variações de hero copy (200-400 palavras) por abordagem (benefício vs dor vs transformação), sugestões de social proof framing, bullets de benefício em 3 estilos (feature-benefit, problema-solução, antes-depois), documento de racional de copy com o mecanismo psicológico sendo testado em cada variação"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro aprova hipótese para produção de variações; resultado de experimento indica que headline foi o fator crítico (Hera diagnóstica) e nova wave é necessária; nova campanha de ads será lançada e p…"
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

# Gerar Copy de Conversao

**Task ID:** `muse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Copy de Conversao |
| **status** | `pending` |
| **responsible_executor** | Muse (Muse — Conversion Copywriter Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Copywriter especializado em copy de alta conversao para landing pages. Gera variacoes de copy baseadas nas hipoteses priorizadas pelo Maestro, sempre conectando o copy ao ICP e ao momento de consciencia do usuario (Eugene Schwartz Awareness Levels). Trabalha com os frameworks AIDA, PAS, PASTOR e Jobs-to-be-Done. Produz headline, subheadline, hero copy, bullets de beneficio, CTA primario e secundario, social proof framing e handling de objecoes em copy. Nunca gera copy sem ter o contexto de de onde o usuario veio (qual ad, qual audiencia, qual promessa foi feita no topo do funil). Alias: 'Muse' — a voz que transforma comportamento em palavras que convertem.

## Input

- Hipótese de CRO ativa com descrição clara do que testar (qual elemento, qual mecanismo psicológico), ICP Profile com dores e linguagem do cliente ideal, tom de voz e brand guidelines da empresa, copy atual da página (controle do teste), contexto do ad/fonte de tráfego que chegará na página, objeções comuns mapeadas pelo Hera e pelo time de vendas

## Output

- Pacote de variações de copy por experimento: 3-5 versões de headline (com racional de cada uma
- qual princípio testa), 3-5 versões de CTA com framing alternativo, variações de hero copy (200-400 palavras) por abordagem (benefício vs dor vs transformação), sugestões de social proof framing, bullets de benefício em 3 estilos (feature-benefit, problema-solução, antes-depois), documento de racional de copy com o mecanismo psicológico sendo testado em cada variação

## Trigger

Maestro aprova hipótese para produção de variações; resultado de experimento indica que headline foi o fator crítico (Hera diagnóstica) e nova wave é necessária; nova campanha de ads será lançada e precisa de landing page específica; solicitação manual de CMO para página de produto novo

## Knowledge base (o que o executor consulta)

- ICP Profile vivo (do squad Living ICP Profiler, se disponível), brand guidelines e tom de voz da empresa, histórico de copy de todas as variações testadas com resultado (base de aprendizado acumulada), Eugene Schwartz Awareness Levels aplicados ao produto, swipe file de copy de alta conversão do setor, objeções mapeadas pelo time de vendas, linguagem literal dos clientes (reviews, entrevistas, NPS verbatim)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Hipótese de CRO ativa com descrição clara do que testar (qual elemento, qual mecanismo psicológico), ICP Profile com do…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de variações de copy por experimento: 3-5 versões de headline (com racional de cada uma) e persistir no artefato do squad.
4. Entregar ao critic Rex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de variações de copy por experimento: 3-5 versões de headline (com racional de cada uma
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

- **to:** Pixel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
