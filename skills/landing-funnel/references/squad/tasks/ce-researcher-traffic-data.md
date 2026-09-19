---
task: analyzeTrafficData()
agent: ce-researcher
description: "EXCLUSIVO: analisar dados de tráfego pago do cliente (se existir) ou benchmark do nicho. Inclui CPL, CTR, taxa de conversão esperada. DIFERENCIAL."
elicit: true
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: campaignData
    tipo: object
    obrigatorio: false
    descricao: "Dados de campanhas pagas existentes (CPL, CTR, taxa de conversão)"
  - nome: niche
    tipo: string
    obrigatorio: true
    descricao: "Nicho do produto para benchmark"

Saida:
  - nome: trafficIntelligence
    tipo: file
    obrigatorio: true
    descricao: "Análise de dados de tráfego pago com benchmarks do nicho"

Checklist:
  pre-conditions:
    - "[ ] Nicho definido"
  post-conditions:
    - "[ ] Benchmarks de CPL e conversão documentados"
    - "[ ] Canais de tráfego recomendados"
---

# Task: analyzeTrafficData()

## Objetivo
Analisar dados reais de tráfego pago do cliente ou, na ausência destes, estabelecer benchmarks precisos do nicho para definir metas realistas de conversão, CPL (Custo por Lead) e ROAS (Return on Ad Spend). Esta análise é o DIFERENCIAL que permite ao squad projetar uma LP baseada em dados — não em suposições.

## Inputs Necessários
- Dados de campanhas pagas existentes do cliente (Google Ads, Meta Ads, TikTok Ads) — se existir:
  - Impressões, cliques, CTR por criativo
  - Custo por clique (CPC)
  - Taxa de conversão da LP atual
  - Custo por lead (CPL) atual
  - Custo por aquisição (CPA) atual
  - Taxa de conversão lead → venda
- Se dados próprios não existirem:
  - Nicho exato do produto
  - Plataformas de tráfego planejadas
  - Budget mensal de tráfego
- `product-brief.md` (para contexto de nicho e preço)
- `scope.md` (plataformas de analytics e pixels planejados)

## Processo
1. **Coleta de dados do cliente** — Solicitar acesso de leitura às contas de anúncios do cliente:
   - Meta Ads Manager (nível de conta, últimos 90 dias)
   - Google Ads (relatório de conversões, últimos 90 dias)
   - Dados de GA4 ou analytics atual (se existir)
   Documentar cada métrica com período de referência.

2. **Análise de performance atual** — Se dados existirem:
   - Calcular CPL real e comparar com benchmark do nicho
   - Identificar criativos com melhor CTR (hooks que funcionam)
   - Identificar landing pages com melhor taxa de conversão
   - Mapear jornada do usuário via analytics: tempo na página, scroll depth, cliques em CTA
   - Identificar dispositivos predominantes (mobile/desktop) — impacta design

3. **Benchmarks do nicho** — Se dados próprios forem insuficientes ou inexistentes:

   | Métrica | E-commerce | SaaS B2B | Infoproduto | Serviço Local | Lead Gen |
   |---------|-----------|----------|-------------|---------------|----------|
   | CTR Meta Ads | 1-3% | 0.5-1.5% | 2-5% | 1-4% | 1-3% |
   | CTR Google Ads | 3-6% | 2-5% | 4-8% | 5-10% | 3-7% |
   | Taxa Conv. LP | 1-3% | 2-5% | 3-8% | 5-15% | 5-20% |
   | CPL médio | R$20-80 | R$50-200 | R$10-50 | R$30-150 | R$15-80 |

   Refinar benchmarks com pesquisa específica do sub-nicho do cliente.

4. **Definição de metas de conversão** — Baseado em dados reais ou benchmarks:
   - Taxa de conversão conservadora (p10 do nicho)
   - Taxa de conversão realista (p50 do nicho)
   - Taxa de conversão otimista (p90 do nicho — LP otimizada)
   - CPL alvo para viabilidade de negócio (calculado a partir do LTV do cliente)
   - ROAS mínimo viável

5. **Análise de dispositivos e comportamento** — Identificar:
   - Proporção mobile vs desktop vs tablet
   - Tempo médio de sessão esperado
   - Comportamento de scroll típico no nicho
   - Taxa de rejeição esperada
   Estes dados impactam diretamente decisões de design e posição dos CTAs.

6. **Recomendações estratégicas** — Traduzir dados em ações:
   - Onde focar o budget inicial de tráfego
   - Qual plataforma priorizar para o nicho
   - Qual temperatura de audiência testar primeiro
   - Qual KPI priorizar no início (volume ou qualidade)

## Veto Conditions
- Acesso aos dados de anúncios negado e cliente sem dados históricos → usar benchmarks do nicho e documentar como estimativa, não como dado real
- Dados históricos com menos de 500 cliques → volume insuficiente para análise estatística — tratar como anedótico e complementar com benchmarks
- Divergência > 3x entre dados do cliente e benchmark do nicho → investigar causa antes de definir metas

## Output Esperado
Arquivo `traffic-data-analysis.md` contendo:
- Dados de tráfego do cliente (se existirem) com período de referência
- Benchmarks do nicho por plataforma e métrica
- Metas de conversão em 3 cenários (conservador/realista/otimista)
- CPL alvo calculado a partir do LTV
- ROAS mínimo viável
- Perfil de dispositivos (mobile/desktop split)
- Recomendações estratégicas de tráfego
- Fonte de cada dado (dado real vs benchmark)

## Completion Criteria
- [ ] Dados do cliente coletados OU razão documentada para ausência
- [ ] Benchmarks do nicho obtidos de fontes verificáveis (com referência)
- [ ] Metas em 3 cenários definidas (conservador/realista/otimista)
- [ ] CPL alvo calculado e justificado pelo LTV
- [ ] Perfil de dispositivos definido
- [ ] Recomendações estratégicas de tráfego produzidas
- [ ] Arquivo `traffic-data-analysis.md` criado e disponível para squad
- [ ] Dados diferenciados entre reais e estimativas/benchmarks
