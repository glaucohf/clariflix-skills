---
task: cipher()
responsavel: "Cipher"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Feed de novos ads de Falcon com screenshots/copies, histórico de ads anteriores do mesmo concorrente para contexto de evolução, landing page de destino do ad (capturada por Prism se disponível), briefing do ICP próprio da empresa para calibrar relevância do ângulo detectado, biblioteca de ângulos classificados anteriormente para consistência de taxonomia"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ad Intelligence Card por criativo analisado (ângulo narrativo, estrutura hook/body/CTA, ICP inferido, estimativa de budget relativo, score de relevância para a empresa de 0-10), Winning Ad Report para qualquer ad com 30+ dias de veiculação (análise completa com hipótese de por que está funcionando), Competitor Creative Strategy Profile atualizado por concorrente (como a estratégia criativa evoluiu nos últimos 90 dias, quais ângulos dominam, quais foram descartados), Test Pattern Alert quando concorrente está claramente em fase de testes intensivos (indica que provavelmente encontrarão novo vencedor em breve)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Feed diário de Falcon com novos ads para análise; Winning Ad Flag de Falcon (ad com 30+ dias — análise prioritária em 4h); Orion solicita análise profunda de concorrente específico antes de lançament…"
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

# Classificar Angulos Narrativos

**Task ID:** `cipher()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Angulos Narrativos |
| **status** | `pending` |
| **responsible_executor** | Cipher (Cipher — Ad Intelligence Analyst) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Camada de analise profunda de cada ad detectado por Falcon. Vai alem do screenshot — decodifica o que o ad esta tentando fazer. Para cada novo ad relevante ou grupo de ads: (1) Classifica o angulo narrativo principal (medo/perda, aspiracao/ganho, prova social/autoridade, curiosidade/ruptura, ROI/preco, identidade/tribo, urgencia/escassez); (2) Destrincha a estrutura do ad — hook dos primeiros 3 segundos ou primeira linha, body de desenvolvimento, CTA e oferta especifica; (3) Estima o budget relativo de veiculacao baseado em tempo de rodagem e diversidade de formatos (ad rodando em 5 formatos diferentes = escala real, nao teste); (4) Identifica o ICP alvo inferido pelo criativo (linguagem, dores mencionadas, contexto visual); (5) Detecta padroes de teste — quando concorrente lan varios ads com pequenas variacoes de hook ou CTA, identifica qual variavel esta sendo testada. Constroi perfil de estrategia criativa por concorrente ao longo do tempo.

## Input

- Feed de novos ads de Falcon com screenshots/copies, histórico de ads anteriores do mesmo concorrente para contexto de evolução, landing page de destino do ad (capturada por Prism se disponível), briefing do ICP próprio da empresa para calibrar relevância do ângulo detectado, biblioteca de ângulos classificados anteriormente para consistência de taxonomia

## Output

- Ad Intelligence Card por criativo analisado (ângulo narrativo, estrutura hook/body/CTA, ICP inferido, estimativa de budget relativo, score de relevância para a empresa de 0-10), Winning Ad Report para qualquer ad com 30+ dias de veiculação (análise completa com hipótese de por que está funcionando), Competitor Creative Strategy Profile atualizado por concorrente (como a estratégia criativa evoluiu nos últimos 90 dias, quais ângulos dominam, quais foram descartados), Test Pattern Alert quando concorrente está claramente em fase de testes intensivos (indica que provavelmente encontrarão novo vencedor em breve)

## Trigger

Feed diário de Falcon com novos ads para análise; Winning Ad Flag de Falcon (ad com 30+ dias — análise prioritária em 4h); Orion solicita análise profunda de concorrente específico antes de lançamento de campanha própria; ciclo semanal de atualização de Competitor Creative Strategy Profiles; CMO solicita análise comparativa para briefing de nova campanha

## Knowledge base (o que o executor consulta)

- Taxonomia de angulos narrativos com exemplos validados (biblioteca de referencia interna), historico completo de ads analisados por concorrente com classificacoes anteriores (para detectar mudanca de estrategia), perfil de ICP proprio da empresa (para pontuar relevancia de cada angulo detectado para o negocio), biblioteca de hooks de alta performance por categoria/setor (benchmark externo), metricas proprias de performance de ads internos (para calibrar o que 'funciona' na categoria)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Feed de novos ads de Falcon com screenshots/copies, histórico de ads anteriores do mesmo concorrente para contexto de e…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ad Intelligence Card por criativo analisado (ângulo narrativo, estrutura hook/body/CTA, ICP inferido, estimativa de bud…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ad Intelligence Card por criativo analisado (ângulo narrativo, estrutura hook/body/CTA, ICP inferido, estimativa de budget relativo, score de relevância para a…
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

- **to:** Prism
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
