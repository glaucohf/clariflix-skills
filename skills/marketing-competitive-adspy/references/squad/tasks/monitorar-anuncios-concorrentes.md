---
task: falcon()
responsavel: "Falcon"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Competitive Map validado (lista de concorrentes Tier 1/2/3 com URLs, nomes de página no Meta/Google/LinkedIn/TikTok), critérios de alerta configurados por Orion (thresholds de burst, plataformas prioritárias por concorrente, janela de tempo de varredura), credenciais de acesso via MCP a bibliotecas de ads públicas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Feed diário de novos ads detectados (JSON estruturado com: concorrente, plataforma, data de início estimada, formato, thumbnail/screenshot, copy headline, CTA, URL de destino), Competitive Activity Score semanal por concorrente com variação versus semana anterior, Burst Alert quando concorrente Tier 1 lança 5+ ads novos em 48h (sinal de campanha ou lançamento), Emerging Competitor Report mensal identificando novos players anunciando para o mesmo ICP, lista de ads com 30+ dias de veiculação contínua (proxies de vencedores para análise prioritária de Cipher"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job de varredura diária automática (cron 6h para Tier 1, 24h para Tier 2, 72h para Tier 3); webhook de alerta de burst (5+ ads novos de mesmo concorrente em 48h); Orion solicita varredura emergencial…"
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

# Monitorar Anúncios Concorrentes

**Task ID:** `falcon()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Anúncios Concorrentes |
| **status** | `pending` |
| **responsible_executor** | Falcon (Falcon — Scout & Competitive Mapper) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Motor de rastreamento continuo de atividade competitiva nas plataformas de ads e posicionamento digital. Responsavel por: (1) Varredura diaria de novos anuncios dos concorrentes Tier 1 nas bibliotecas de Meta Ads, Google Ads Transparency, TikTok Creative Center e LinkedIn Ad Library; (2) Deteccao de novos concorrentes emergentes que comecem a anunciar para o mesmo ICP (via monitoramento de keywords de categoria no Meta Ad Library e Google); (3) Rastreamento de atividade em plataformas secundarias — YouTube (video ads), Spotify (audio ads), conteudo organico em LinkedIn/Instagram que frequentemente precede campanhas pagas; (4) Sinalizacao de burst de atividade — quando concorrente aumenta drasticamente o volume de novos ads em curto periodo (sinal de lancamento ou teste intensivo). Calcula Competitive Activity Score por concorrente (volume de ads ativos, diversidade de formatos, frequencia de novos criativas) para priorizar quem merece analise profunda de Cipher.

## Input

- Competitive Map validado (lista de concorrentes Tier 1/2/3 com URLs, nomes de página no Meta/Google/LinkedIn/TikTok), critérios de alerta configurados por Orion (thresholds de burst, plataformas prioritárias por concorrente, janela de tempo de varredura), credenciais de acesso via MCP a bibliotecas de ads públicas

## Output

- Feed diário de novos ads detectados (JSON estruturado com: concorrente, plataforma, data de início estimada, formato, thumbnail/screenshot, copy headline, CTA, URL de destino), Competitive Activity Score semanal por concorrente com variação versus semana anterior, Burst Alert quando concorrente Tier 1 lança 5+ ads novos em 48h (sinal de campanha ou lançamento), Emerging Competitor Report mensal identificando novos players anunciando para o mesmo ICP, lista de ads com 30+ dias de veiculação contínua (proxies de vencedores para análise prioritária de Cipher

## Trigger

Job de varredura diária automática (cron 6h para Tier 1, 24h para Tier 2, 72h para Tier 3); webhook de alerta de burst (5+ ads novos de mesmo concorrente em 48h); Orion solicita varredura emergencial para concorrente específico; ciclo semanal de Competitive Activity Score; nova campanha interna sendo planejada (trigger manual pelo CMO para varredura targetada)

## Knowledge base (o que o executor consulta)

- Competitive Map completo com todos os identificadores por plataforma (Page IDs Meta, advertiser IDs Google, handles TikTok/LinkedIn), histórico de atividade de ads por concorrente (volume, formatos, frequência de novos criativas
- para detectar anomalias), calendário de sazonalidade do setor (períodos onde burst e esperado vs
- anomalias reais), lista de keywords de categoria para detectar concorrentes emergentes, mapeamento de ICP compartilhado para identificar overlap de audiência nos ads

## Action Items

1. Confirmar o gatilho e carregar a entrada (Competitive Map validado (lista de concorrentes Tier 1/2/3 com URLs, nomes de página no Meta/Google/LinkedIn/TikTok), c…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Feed diário de novos ads detectados (JSON estruturado com: concorrente, plataforma, data de início estimada, formato, t…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Feed diário de novos ads detectados (JSON estruturado com: concorrente, plataforma, data de início estimada, formato, thumbnail/screenshot, copy headline, CTA,…
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

- **to:** Cipher
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
