---
task: echo()
responsavel: "Echo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ad Intelligence Cards de Cipher (ads analisados e classificados), aprovação de Sigma antes de adicionar item ao swipe file, histórico de swipe files anteriores para evitar duplicação, feedback do time de criativo sobre quais itens foram mais úteis (ciclo de aprendizado), guidelines de brand voice para contextualizar restrições de reutilização por item"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Swipe File semanal no ClickUp com novos itens categorizados (formato padrão: screenshot/copy original + ângulo classificado + elementos reutilizáveis extraídos + contexto de uso + restrições de adaptação), Swipe File Digest mensal com top 10 itens mais acionáveis do mês com briefing de adaptação para a empresa, Saturation Alert quando ângulo específico está sendo usado por 3+ concorrentes simultaneamente (sinal de commodity"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "evitar ou diferenciar), Performance Loop report trimestral correlacionando itens do swipe file usados internamente com performance de ads resultantes"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cipher entrega Ad Intelligence Card aprovado para curadoria; gate de Sigma aprovado para novo item; ciclo semanal de atualização do swipe file; time de criativo solicita swipe file por categoria espe…"
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

# Curar Swipe File

**Task ID:** `echo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Curar Swipe File |
| **status** | `pending` |
| **responsible_executor** | Echo (Écho — Swipe File Curator) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Curador obsessivo do swipe file competitivo — transforma o volume bruto de ads e copies detectados em uma biblioteca acionável e reutilizável pelo time de criativo. Para cada item aprovado por Cipher: (1) Extrai os elementos reutilizáveis (hook template, estrutura de argumento, CTA formula, frame visual) independente da categoria ou produto — ângulos são transferíveis; (2) Categoriza em taxonomia própria do cliente (por ângulo narrativo, por formato, por plataforma, por estágio do funil, por tipo de CTA); (3) Adiciona contexto de reutilização — 'este hook funciona quando o público já conhece o problema; adaptar para audiência fria removendo jargão técnico'; (4) Monitora a performance dos ângulos que o time de criativo da empresa já usou baseado em swipe files anteriores (ciclo de aprendizado); (5) Mantém o swipe file 'vivo' — remove itens obsoletos, sinaliza quando um ângulo está saturando no mercado. Entregável semanal: Swipe File Update com novos itens e brief de reutilização para o time.

## Input

- Ad Intelligence Cards de Cipher (ads analisados e classificados), aprovação de Sigma antes de adicionar item ao swipe file, histórico de swipe files anteriores para evitar duplicação, feedback do time de criativo sobre quais itens foram mais úteis (ciclo de aprendizado), guidelines de brand voice para contextualizar restrições de reutilização por item

## Output

- Swipe File semanal no ClickUp com novos itens categorizados (formato padrão: screenshot/copy original + ângulo classificado + elementos reutilizáveis extraídos + contexto de uso + restrições de adaptação), Swipe File Digest mensal com top 10 itens mais acionáveis do mês com briefing de adaptação para a empresa, Saturation Alert quando ângulo específico está sendo usado por 3+ concorrentes simultaneamente (sinal de commodity
- evitar ou diferenciar), Performance Loop report trimestral correlacionando itens do swipe file usados internamente com performance de ads resultantes

## Trigger

Cipher entrega Ad Intelligence Card aprovado para curadoria; gate de Sigma aprovado para novo item; ciclo semanal de atualização do swipe file; time de criativo solicita swipe file por categoria específica antes de briefing; Orion identifica ângulo dominante de concorrente Tier 1 que merece entrada prioritária no swipe file; revisão trimestral de performance do swipe file

## Knowledge base (o que o executor consulta)

- Swipe file completo e versionado com todos os itens históricos e metadata de uso, taxonomia de ângulos narrativos com definições claras para consistência de categorização, guidelines de brand voice da empresa para contextualização de reutilização por item, histórico de performance de ads internos que usaram ângulos inspirados no swipe file (ciclo de aprendizado), framework de transferência de ângulo entre categorias (como adaptar um hook de SaaS para serviços, etc.)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ad Intelligence Cards de Cipher (ads analisados e classificados), aprovação de Sigma antes de adicionar item ao swipe f…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Swipe File semanal no ClickUp com novos itens categorizados (formato padrão: screenshot/copy original + ângulo classifi…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Swipe File semanal no ClickUp com novos itens categorizados (formato padrão: screenshot/copy original + ângulo classificado + elementos reutilizáveis extraídos…
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

- **to:** Volta
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
