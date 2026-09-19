---
task: sigma()
responsavel: "Sigma"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ad Intelligence Cards de Cipher antes de serem incluídos em winning ad reports, itens de swipe file de Echo antes de serem publicados no ClickUp, Competitive Briefs de Nexus antes de serem entregues ao time, Category Trend Alerts de Volta antes de escalar para CMO, evidências brutas de Falcon e Prism para validação de qualidade de sinal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa especifica para cada item revisado, lista de ajustes necessarios se NEEDS_REVISION com sugestoes concretas (ex: 'hipotese de lancamento e fraca"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "o ad novo pode ser teste A/B dado que o concorrente tem 12 variantes ativas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "reformular como alerta de teste, nao lancamento'), Flag de RISCO quando briefing de reacao se aproxima demais do material original do concorrente (risco legal de plágio), Intelligence Quality Score por item (0-10 com breakdown: qualidade da evidencia, solidez da hipotese, relevancia para o negocio, acionabilidade do briefing)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: SEMPRE antes de qualquer entrega de intelligence ao time de marketing (gate obrigatorio — nenhum briefing, swipe file item, trend alert ou winning ad report chega ao time sem aprovacao de Sigma), ant…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sigma 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente e critérios de alerta antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação)"
    - "[ ] HITL: Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fazem sentido para o contexto do setor antes do squad entrar em produção completa (L3, calibração crítica de taxonomia)"
    - "[ ] HITL: Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e decidir sobre reação antes de qualquer briefing ser disparado ao time (L3, irreversível — reação de preço e decisão estratégica)"
    - "[ ] HITL: Aprovação de Category Trend Alert — quando Volta detecta convergência de 3+ concorrentes, o CMO deve validar a hipótese estratégica antes de escalar como diretriz de campanha (L3, decisão estratégica de posicionamento)"
    - "[ ] HITL: Revisão de Competitive Brief de reação urgente — qualquer briefing com prazo de reação de 4h (mudança de Tier 1) deve ser revisado por Head de Marketing antes de ser entregue ao time de criativo (L3, velocidade não elimina o gate humano em movimentos críticos)"
---

# Verificar Inteligência Competitiva

**Task ID:** `sigma()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Inteligência Competitiva |
| **status** | `pending` |
| **responsible_executor** | Sigma (Sigma — Critic & Intelligence Verifier) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gate de qualidade antes de qualquer inteligencia competitiva chegar ao time de marketing ou se converter em acao externa. Implementa o padrao Skeptic Protocol para o squad. Valida cinco dimensoes criticas: (1) Qualidade da evidencia — o movimento detectado e real e estatisticamente relevante, ou e ruido? (um ad novo pode ser teste A/B, nao lancamento — Sigma questiona a interpretacao); (2) Contexto competitivo — a hipotese de por que o concorrente esta fazendo este movimento e solida ou e especulacao de confirmacao? (evitar que o time reaja a algo que nao e o que parece); (3) Relevancia para o negocio — o angulo ou movimento detectado e realmente relevante para a estrategia da empresa, ou e um movimento do concorrente para um ICP diferente que nao compete diretamente?; (4) Qualidade do swipe file item — o item de Echo tem contexto de reutilizacao claro o suficiente para um briefing de criativo? Ou e um screenshot sem contexto que vai confundir o time?; (5) Compliance de uso — o briefing de reacao sugerido por Nexus respeita as diretrizes de brand voice e nao e uma copia direta de material de concorrente (risco legal/etico).

## Input

- Ad Intelligence Cards de Cipher antes de serem incluídos em winning ad reports, itens de swipe file de Echo antes de serem publicados no ClickUp, Competitive Briefs de Nexus antes de serem entregues ao time, Category Trend Alerts de Volta antes de escalar para CMO, evidências brutas de Falcon e Prism para validação de qualidade de sinal

## Output

- Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa especifica para cada item revisado, lista de ajustes necessarios se NEEDS_REVISION com sugestoes concretas (ex: 'hipotese de lancamento e fraca
- o ad novo pode ser teste A/B dado que o concorrente tem 12 variantes ativas
- reformular como alerta de teste, nao lancamento'), Flag de RISCO quando briefing de reacao se aproxima demais do material original do concorrente (risco legal de plágio), Intelligence Quality Score por item (0-10 com breakdown: qualidade da evidencia, solidez da hipotese, relevancia para o negocio, acionabilidade do briefing)

## Trigger

SEMPRE antes de qualquer entrega de intelligence ao time de marketing (gate obrigatorio — nenhum briefing, swipe file item, trend alert ou winning ad report chega ao time sem aprovacao de Sigma), antes de qualquer reacao tatica urgente proposta por Nexus, quando Cipher classifica ad como Winning Ad (revisao aprimorada dado o peso da classificacao), quando Volta emite Category Trend Alert (revisao da solidez das evidencias de convergencia)

## Knowledge base (o que o executor consulta)

- Criterios de qualidade de evidência por tipo de fonte (bibliotecas de ads públicas têm limitações conhecidas
- ex: Meta Ad Library não mostra budget real, apenas tempo de veiculação), histórico de falsos positivos anteriores do squad (para aprender padrões de ruído versus sinal real), guidelines completos de brand voice da empresa, regras de ética e compliance para uso de material competitivo em briefings internos, benchmark de Intelligence Quality Scores históricos para calibrar o threshold de aprovação

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ad Intelligence Cards de Cipher antes de serem incluídos em winning ad reports, itens de swipe file de Echo antes de se…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa especifica para cada item revisado, lista de ajustes necess…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredicto APPROVED/NEEDS_REVISION/BLOCKED com justificativa especifica para cada item revisado, lista de ajustes necessarios se NEEDS_REVISION com sugestoes co…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sigma 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente…
- [ ] Gate HITL respeitado: Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fa…
- [ ] Gate HITL respeitado: Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente e critérios de aler… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fazem sentido para o c… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e decidir sobre reação a… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação de Category Trend Alert — quando Volta detecta convergência de 3+ concorrentes, o CMO deve validar a hipótese estratégica antes de escalar como diret… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de Competitive Brief de reação urgente — qualquer briefing com prazo de reação de 4h (mudança de Tier 1) deve ser revisado por Head de Marketing antes… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de itens do swipe file antes de publicação no ClickUp — revisão quinzenal pelo Head de Marketing dos itens aprovados por Sigma para garantir alinhame… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisão mensal do Competitive Intelligence Baseline — CMO e Head de Vendas revisam com Orion quais concorrentes devem subir ou descer de tier, se novos concorr… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Quando Sigma retorna BLOCKED em gate de compliance (risco de plágio ou evidência muito fraca) — revisão humana obrigatória antes de reprocessar o item ou desca… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Sigma 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
