---
task: mapFunnelStages()
agent: ce-strategist
description: "Mapear funil completo: tráfego → página → lead → nurture → venda → retenção. DIFERENCIAL vs concorrente."
elicit: true
responsavel: "Vortex"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing do produto gerado por discoverProduct()"

Saida:
  - nome: funnelMap
    tipo: file
    obrigatorio: true
    descricao: "Mapa do funil completo: tráfego → página → lead → nurture → venda → retenção"

Checklist:
  pre-conditions:
    - "[ ] Product brief disponível"
  post-conditions:
    - "[ ] Todas as etapas do funil mapeadas"
    - "[ ] Métricas por etapa definidas"
---

# Task: mapFunnelStages()

## Objetivo
Construir o mapa completo do funil de conversão do produto, identificando todas as etapas desde a aquisição de tráfego até a retenção do cliente. Esta visão sistêmica garante que a landing page seja projetada para o momento correto da jornada do comprador, não isoladamente.

## Inputs Necessários
- `product-brief.md` (output de `discoverProduct()`)
- Canal(is) de tráfego atual(is) ou planejado(s) (Google Ads, Meta Ads, orgânico, influencer, email, etc.)
- Canais de nurture existentes (email, WhatsApp, remarketing)
- Processo atual de vendas (self-service, SDR, closer, consultivo)
- Tempo médio de decisão de compra do cliente
- Canais de retenção e pós-venda (onboarding, suporte, comunidade, upsell)
- Dados de conversão existentes em qualquer etapa (se disponíveis)

## Processo
1. **Mapeamento de tráfego** — Identificar e documentar fontes de tráfego planejadas: tipo (pago/orgânico), temperatura do tráfego (frio/morno/quente), nível de consciência na chegada à LP (Schwartz: problem-aware, solution-aware, product-aware, most-aware).
2. **Definição do papel da LP no funil** — Classificar a LP como: topo (captura fria), meio (nurture para decisão) ou fundo (fechamento direto). Adaptar estratégia de copy e design conforme o papel.
3. **Mapeamento do fluxo pós-conversão** — Documentar o que acontece após o lead converter: sequência de emails, abordagem de SDR, acesso ao produto, onboarding. Identificar gargalos.
4. **Análise do diferencial competitivo no funil** — Comparar o funil do cliente com o padrão do nicho. Identificar onde o produto pode se diferenciar: velocidade de resposta, qualidade do nurture, oferta de entrada, garantia, experiência pós-compra.
5. **Identificação de pontos de vazamento** — Mapear onde leads tendem a sair do funil sem converter e propor soluções de copy ou UX para cada ponto.
6. **Definição de métricas-alvo por etapa** — Estabelecer benchmarks de conversão para cada etapa do funil com base em dados do nicho (pesquisa do ce-researcher).
7. **Consolidação do Funnel Map** — Criar diagrama visual do funil com taxas esperadas, pontos de decisão, touchpoints de nurture e flags de integração necessárias.

## Veto Conditions
- Funil sem definição clara de próximo passo após conversão → bloquear até definir fluxo pós-lead
- Tráfego frio direcionado a LP de venda direta sem nurture intermediário → sinalizar risco e recomendar lead magnet ou VSL antes do checkout
- Ausência de qualquer mecanismo de nurture para produto com ciclo de decisão superior a 48h → registrar como risco crítico

## Output Esperado
Documento `funnel-map.md` contendo:
- Diagrama de funil em texto (etapas, fluxos, taxas esperadas)
- Papel da LP no funil (topo/meio/fundo)
- Temperatura e nível de consciência do tráfego na chegada
- Fluxo pós-conversão detalhado
- Diferencial competitivo identificado em cada etapa
- Pontos de vazamento mapeados com recomendações
- Métricas-alvo por etapa
- Flags de integração necessárias (whatsapp/email/crm/payments)

## Completion Criteria
- [ ] Todas as etapas do funil mapeadas (tráfego → LP → lead → nurture → venda → retenção)
- [ ] Papel da LP no funil definido e justificado
- [ ] Temperatura e nível de consciência do tráfego documentados
- [ ] Diferencial competitivo identificado em pelo menos 2 etapas do funil
- [ ] Pontos de vazamento documentados com ações recomendadas
- [ ] Métricas-alvo definidas para cada etapa
- [ ] Flags de integração definidas (backend, analytics, a/b, social_proof, email, whatsapp, payments, crm)
- [ ] Arquivo `funnel-map.md` criado e disponível para os demais agentes
